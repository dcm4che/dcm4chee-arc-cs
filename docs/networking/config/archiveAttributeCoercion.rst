Archive Attribute Coercion
==========================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive Attribute Coercion Attributes (LDAP Object: dcmArchiveAttributeCoercion)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name of the Archive Attribute Coercion","
    .. _cn:

    cn_"
    "DIMSE",string,"DICOM Message Element. Enumerated values: C_STORE_RQ, C_FIND_RQ or C_FIND_RSP","
    .. _dcmDIMSE:

    dcmDIMSE_"
    "DICOM Transfer Role",string,"DICOM Transfer Role. Enumerated values: SCU or SCP","
    .. _dicomTransferRole:

    dicomTransferRole_"
    "Rule Priority",integer,"Rule Priority.","
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
    "No Keywords",boolean,"Indicates if keywords shall be omitted in generated DICOM XML or JSON presentations","
    .. _dcmNoKeywords:

    dcmNoKeywords_"
    "Merge MWL Matching Key",string,"Specifies attribute of received object to lookup MWL Item used to coerce request attributes. If absent, request attributes of received objects will not be coerced. Enumerated values: AccessionNumber, StudyInstanceUID or ScheduledProcedureStepID","
    .. _dcmMergeMWLMatchingKey:

    dcmMergeMWLMatchingKey_"
    "Merge MWL Template URI",string,"Specifies URI for the style sheet to coerce request attributes of received objects from matching DICOM MWL items. Only effective, if dcmMergeMWLMatchingKey is specified.","
    .. _dcmMergeMWLTemplateURI:

    dcmMergeMWLTemplateURI_"
    "Leading C-FIND SCP",string,"AE Title of external C-FIND SCP for Attribute Coercion with Patient and Study attributes fetched from this AE.","
    .. _dcmLeadingCFindSCP:

    dcmLeadingCFindSCP_"
    "Leading C-FIND SCP return keys(s)",string,"DICOM Tag as hex string of attributes fetched from external C-FIND SCP for Attribute Coercion. If absent, all Patient and Study Attributes extracted into the DB - configured by the Patient and Study Attribute Filter - are fetched.","
    .. _dcmTag:

    dcmTag_"
    "Attribute Update Policy",string,"Specifies how attributes shall be updated with attributes fetched from Leading C-FIND SCP. Enumerated values: SUPPLEMENT, MERGE or OVERWRITE","
    .. _dcmAttributeUpdatePolicy:

    dcmAttributeUpdatePolicy_"
    "Supplement from Device",string,"Name of Device from which Assigning Authorities and other information is taken to supplement received Composite Objects and MPPS.","
    .. _dcmSupplementFromDeviceName:

    dcmSupplementFromDeviceName_"
