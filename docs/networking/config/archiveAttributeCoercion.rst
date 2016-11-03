Archive Attribute Coercion
==========================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive Attribute Coercion Attributes (LDAP Object: dcmArchiveAttributeCoercion)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name\ :sup:`*` ",string,"Arbitrary/Meaningful name of the Archive Compression Rule","
    .. _cn:

    cn_"
    "DIMSE\ :sup:`*` ",string,"DIMSE: 'C_STORE_RQ', 'C_FIND_RQ', 'C_FIND_RSP'","
    .. _dcmDIMSE:

    dcmDIMSE_"
    "DICOM Transfer Role\ :sup:`*` ",string,"Transfer role (either 'SCU' or 'SCP')","
    .. _dicomTransferRole:

    dicomTransferRole_"
    "Rule Priority",integer,"Rule Priority. 0 if absent.","
    .. _dcmRulePriority:

    dcmRulePriority_"
    "AE Title(s)",string,"Application Entity (AE) title","
    .. _dcmAETitle:

    dcmAETitle_"
    "Host Name(s)",string,"DNS hostname","
    .. _dcmHostname:

    dcmHostname_"
    "SOP Class UID(s)",string,"A SOP Class UID","
    .. _dcmSOPClass:

    dcmSOPClass_"
    "URI",string,"Specifies URI of the style sheet for Attribute Coercion","
    .. _dcmURI:

    dcmURI_"
    "No Keywords",boolean,"Indicates if keywords shall be omitted in generated DICOM XML or JSON presentations; false if absent","
    .. _dcmNoKeywords:

    dcmNoKeywords_"
    "MWL Matching Key",string,"Specifies attribute of received object to lookup MWL Item used to coerce request attributes. Enumerated values: AccessionNumber, StudyInstanceUID, ScheduledProcedureStepID. If absent, request attributes of received objects will not be coerced.","
    .. _dcmMergeMWLMatchingKey:

    dcmMergeMWLMatchingKey_"
    "Request Attributes Template URI",string,"Specifies URI for the style sheet to coerce request attributes of received objects from matching DICOM MWL items. Only effectiv, if dcmMergeMWLMatchingKey is specified.","
    .. _dcmMergeMWLTemplateURI:

    dcmMergeMWLTemplateURI_"
    "Leading C-FIND SCP",string,"AE Title of external C-FIND SCP for Attribute Coercion with Patient and Study attributes fetched from this AE.","
    .. _dcmLeadingCFindSCP:

    dcmLeadingCFindSCP_"
    "Attribute Update Policy",string,"Specifies how attributes shall be updated with attributes fetched from Leading C-FIND SCP. Enumerated values: SUPPLEMENT, MERGE, OVERWRITE. If absent, MERGE will be applied.","
    .. _dcmAttributeUpdatePolicy:

    dcmAttributeUpdatePolicy_"
