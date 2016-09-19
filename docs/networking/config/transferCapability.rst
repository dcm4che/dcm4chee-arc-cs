Transfer Capability
===================
Each transfer capability specifies the SOP class that the Network AE can support, the mode that it can utilize (SCP or SCU), and the Transfer Syntax(es) that it can utilize

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Transfer Capability Attributes (LDAP Object: dcmTransferCapability)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name for the Transfer Capability object","
    .. _cn:

    cn_"
    "SOP Class\ :sup:`*` ",string,"SOP Class UID","
    .. _dicomSOPClass:

    dicomSOPClass_"
    "Transfer Role\ :sup:`*` ",string,"Either SCU or SCP","
    .. _dicomTransferRole:

    dicomTransferRole_"
    "Transfer Syntax(s)\ :sup:`*` ",string,"Transfer syntax(es) that may be requested as an SCU or that are offered as an SCP","
    .. _dicomTransferSyntax:

    dicomTransferSyntax_"
    "Relational Queries",boolean,"Enable/disable relational queries; disabled if absent","
    .. _dcmRelationalQueries:

    dcmRelationalQueries_"
    "Combined Date Time Matching",boolean,"Enable/disable combined date time matching; disabled if absent","
    .. _dcmCombinedDateTimeMatching:

    dcmCombinedDateTimeMatching_"
    "Fuzzy Semantic Matching",boolean,"Enable/disable fuzzy semantic matching of person  names; disabled if absent","
    .. _dcmFuzzySemanticMatching:

    dcmFuzzySemanticMatching_"
    "Timezone Query Adjustment",boolean,"Enable/disable timezone query adjustment; disabled if absent","
    .. _dcmTimezoneQueryAdjustment:

    dcmTimezoneQueryAdjustment_"
    "Storage Conformance",integer,"Indicates level of Conformance of a Storage SCP","
    .. _dcmStorageConformance:

    dcmStorageConformance_"
    "Digital Signature Support",integer,"Indicates level of Digital Signature Support of a Storage SCP","
    .. _dcmDigitalSignatureSupport:

    dcmDigitalSignatureSupport_"
    "Data Element Coercion",integer,"Indicates coercion of Data Elements of a Storage SCP","
    .. _dcmDataElementCoercion:

    dcmDataElementCoercion_"
