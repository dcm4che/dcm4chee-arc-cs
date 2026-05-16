Transfer Capability Extension
=============================
dcm4che proprietary Transfer Capability Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Transfer Capability Extension Attributes (LDAP Object: dcmTransferCapability)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmPreferredTransferSyntax:
    .. _dcmTransferCapability-dcmPreferredTransferSyntax:

    :ref:`PreferredTransferSyntax(s) <dcmTransferCapability-dcmPreferredTransferSyntax>`",string,"Preferred Transfer Syntax for selection of Transfer Syntax within a Presentation Context, ordered by priority. Overwrites values specified on AE level.

    (dcmPreferredTransferSyntax)"
    "
    .. _dcmRelationalQueries:
    .. _dcmTransferCapability-dcmRelationalQueries:

    :ref:`Relational Queries <dcmTransferCapability-dcmRelationalQueries>`",boolean,"Enable/disable relational queries.

    (dcmRelationalQueries)"
    "
    .. _dcmCombinedDateTimeMatching:
    .. _dcmTransferCapability-dcmCombinedDateTimeMatching:

    :ref:`Combined Date Time Matching <dcmTransferCapability-dcmCombinedDateTimeMatching>`",boolean,"Enable/disable combined date time matching.

    (dcmCombinedDateTimeMatching)"
    "
    .. _dcmFuzzySemanticMatching:
    .. _dcmTransferCapability-dcmFuzzySemanticMatching:

    :ref:`Fuzzy Semantic Matching <dcmTransferCapability-dcmFuzzySemanticMatching>`",boolean,"Enable/disable fuzzy semantic matching of person  names.

    (dcmFuzzySemanticMatching)"
    "
    .. _dcmTimezoneQueryAdjustment:
    .. _dcmTransferCapability-dcmTimezoneQueryAdjustment:

    :ref:`Timezone Query Adjustment <dcmTransferCapability-dcmTimezoneQueryAdjustment>`",boolean,"Enable/disable timezone query adjustment

    (dcmTimezoneQueryAdjustment)"
    "
    .. _dcmStorageConformance:
    .. _dcmTransferCapability-dcmStorageConformance:

    :ref:`Storage Conformance <dcmTransferCapability-dcmStorageConformance>`",integer,"Indicates level of Conformance of a Storage SCP

    Enumerated values:

    0

    1

    2

    3

    (dcmStorageConformance)"
    "
    .. _dcmDigitalSignatureSupport:
    .. _dcmTransferCapability-dcmDigitalSignatureSupport:

    :ref:`Digital Signature Support <dcmTransferCapability-dcmDigitalSignatureSupport>`",integer,"Indicates level of Digital Signature Support of a Storage SCP

    Enumerated values:

    0

    1

    2

    3

    (dcmDigitalSignatureSupport)"
    "
    .. _dcmDataElementCoercion:
    .. _dcmTransferCapability-dcmDataElementCoercion:

    :ref:`Data Element Coercion <dcmTransferCapability-dcmDataElementCoercion>`",integer,"Indicates coercion of Data Elements of a Storage SCP

    Enumerated values:

    0

    1

    2

    (dcmDataElementCoercion)"
