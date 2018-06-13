Transfer Capability Extension
=============================
dcm4che proprietary Transfer Capability Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Transfer Capability Extension Attributes (LDAP Object: dcmDcmTransferCapability)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmPreferredTransferSyntax:

    :ref:`PreferredTransferSyntax(s) (dcmPreferredTransferSyntax) <dcmPreferredTransferSyntax>`",string,"Preferred Transfer Syntax for selection of Transfer Syntax within a Presentation Context, ordered by priority. Overwrites values specified on AE level."
    "
    .. _dcmRelationalQueries:

    :ref:`Relational Queries (dcmRelationalQueries) <dcmRelationalQueries>`",boolean,"Enable/disable relational queries."
    "
    .. _dcmCombinedDateTimeMatching:

    :ref:`Combined Date Time Matching (dcmCombinedDateTimeMatching) <dcmCombinedDateTimeMatching>`",boolean,"Enable/disable combined date time matching."
    "
    .. _dcmFuzzySemanticMatching:

    :ref:`Fuzzy Semantic Matching (dcmFuzzySemanticMatching) <dcmFuzzySemanticMatching>`",boolean,"Enable/disable fuzzy semantic matching of person  names."
    "
    .. _dcmTimezoneQueryAdjustment:

    :ref:`Timezone Query Adjustment (dcmTimezoneQueryAdjustment) <dcmTimezoneQueryAdjustment>`",boolean,"Enable/disable timezone query adjustment"
    "
    .. _dcmStorageConformance:

    :ref:`Storage Conformance (dcmStorageConformance) <dcmStorageConformance>`",integer,"Indicates level of Conformance of a Storage SCP Enumerated values: 0, 1, 2 or 3"
    "
    .. _dcmDigitalSignatureSupport:

    :ref:`Digital Signature Support (dcmDigitalSignatureSupport) <dcmDigitalSignatureSupport>`",integer,"Indicates level of Digital Signature Support of a Storage SCP Enumerated values: 0, 1, 2 or 3"
    "
    .. _dcmDataElementCoercion:

    :ref:`Data Element Coercion (dcmDataElementCoercion) <dcmDataElementCoercion>`",integer,"Indicates coercion of Data Elements of a Storage SCP Enumerated values: 0, 1 or 2"
