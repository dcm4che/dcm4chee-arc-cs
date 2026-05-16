#!/usr/bin/env python3
"""
Per-page scoped labels for dcm4chee-arc-cs.

Option B: stack labels (preserve old URL anchors) + rewrite intra-file
:ref: targets to the scoped form. Idempotent.

Convention:
    label `dcmRulePriority` in `archiveAttributeCoercion.rst`
    becomes also defined as `archiveAttributeCoercion-dcmRulePriority`.

    `:ref:`Rule Priority <dcmRulePriority>`` → `:ref:`Rule Priority <archiveAttributeCoercion-dcmRulePriority>``

The original `.. _dcmRulePriority:` declaration stays put so external URLs
(`page.html#dcmrulepriority`) keep working.

Run with:
    python3 rewrite_labels.py <DOCS_DIR> [--dry-run]
"""
import re
import sys
from pathlib import Path

LABEL_RE   = re.compile(r"^(\s*)\.\. _([A-Za-z_][A-Za-z0-9_-]*):\s*$")
REF_RE     = re.compile(r":ref:`([^`<]+?)\s*<([A-Za-z_][A-Za-z0-9_-]*)>`")

def page_slug(path: Path) -> str:
    return path.stem  # filename without .rst

def scoped(slug: str, label: str) -> str:
    return f"{slug}-{label}"

def already_scoped(slug: str, label: str) -> bool:
    return label.startswith(f"{slug}-")

def process_file(p: Path, dry_run: bool):
    slug = page_slug(p)
    src = p.read_text()
    lines = src.split("\n")
    labels_in_file = set()
    out_lines = []
    label_added_count = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        m = LABEL_RE.match(line)
        if m:
            indent, label = m.group(1), m.group(2)
            # Skip if already scoped (idempotent)
            if not already_scoped(slug, label):
                labels_in_file.add(label)
                out_lines.append(line)
                # Check if scoped twin already exists in following 2 lines
                twin = f"{indent}.. _{scoped(slug, label)}:"
                lookahead = "\n".join(lines[i+1:i+3])
                if twin not in lookahead:
                    out_lines.append(twin)
                    label_added_count += 1
                i += 1
                continue
            else:
                # already scoped — leave alone
                out_lines.append(line)
                i += 1
                continue
        out_lines.append(line)
        i += 1
    intermediate = "\n".join(out_lines)

    # Now rewrite :ref:`text <label>` for labels declared in this file
    ref_count = 0
    def replace_ref(m):
        nonlocal ref_count
        text, label = m.group(1), m.group(2)
        if label in labels_in_file:
            ref_count += 1
            return f":ref:`{text} <{scoped(slug, label)}>`"
        return m.group(0)
    rewritten = REF_RE.sub(replace_ref, intermediate)

    changed = rewritten != src
    if changed and not dry_run:
        p.write_text(rewritten)
    return label_added_count, ref_count, changed

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    dry_run = "--dry-run" in args
    args = [a for a in args if not a.startswith("--")]
    docs_dir = Path(args[0]).resolve()
    rst_files = sorted(docs_dir.rglob("*.rst"))
    total_labels, total_refs, changed_files = 0, 0, 0
    per_file = []
    for p in rst_files:
        la, ra, changed = process_file(p, dry_run)
        if la or ra:
            per_file.append((p.relative_to(docs_dir), la, ra))
            total_labels += la
            total_refs += ra
            if changed: changed_files += 1
    mode = "DRY-RUN" if dry_run else "APPLIED"
    print(f"[{mode}] files changed: {changed_files} | scoped labels added: {total_labels} | refs rewritten: {total_refs}")
    for path, la, ra in per_file[:15]:
        print(f"  {path}: +{la} labels, {ra} refs")
    if len(per_file) > 15:
        print(f"  ... and {len(per_file)-15} more files")

if __name__ == "__main__":
    main()
