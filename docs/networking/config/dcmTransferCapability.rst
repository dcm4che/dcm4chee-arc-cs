Transfer Capability Extension
=============================
dcm4che proprietary Transfer Capability Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Transfer Capability Extension Attributes (LDAP Object: dcmTransferCapability)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmPreferredTransferSyntax:

    :ref:`PreferredTransferSyntax(s) <dcmPreferredTransferSyntax>`",string,"Preferred Transfer Syntax for selection of Transfer Syntax within a Presentation Context, ordered by priority. Overwrites values specified on AE level.

    (dcmPreferredTransferSyntax)"
    "
    .. _dcmRelationalQueries:

    :ref:`Relational Queries <dcmRelationalQueries>`",boolean,"Enable/disable relational queries.

    (dcmRelationalQueries)"
    "
    .. _dcmCombinedDateTimeMatching:

    :ref:`Combined Date Time Matching <dcmCombinedDateTimeMatching>`",boolean,"Enable/disable combined date time matching.

    (dcmCombinedDateTimeMatching)"
    "
    .. _dcmFuzzySemanticMatching:

    :ref:`Fuzzy Semantic Matching <dcmFuzzySemanticMatching>`",boolean,"Enable/disable fuzzy semantic matching of person  names.

    (dcmFuzzySemanticMatching)"
    "
    .. _dcmTimezoneQueryAdjustment:

    :ref:`Timezone Query Adjustment <dcmTimezoneQueryAdjustment>`",boolean,"Enable/disable timezone query adjustment

    (dcmTimezoneQueryAdjustment)"
    "
    .. _dcmStorageConformance:

    :ref:`Storage Conformance <dcmStorageConformance>`",integer,"Indicates level of Conformance of a Storage SCP Enumerated values: 0, 1, 2 or 3.

    (dcmStorageConformance)"
    "
    .. _dcmDigitalSignatureSupport:

    :ref:`Digital Signature Support <dcmDigitalSignatureSupport>`",integer,"Indicates level of Digital Signature Support of a Storage SCP Enumerated values: 0, 1, 2 or 3.

    (dcmDigitalSignatureSupport)"
    "
    .. _dcmDataElementCoercion:

    :ref:`Data Element Coercion <dcmDataElementCoercion>`",integer,"Indicates coercion of Data Elements of a Storage SCP Enumerated values: 0, 1 or 2.

    (dcmDataElementCoercion)"
