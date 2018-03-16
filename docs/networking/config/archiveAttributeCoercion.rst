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
    "DIMSE",string,"DICOM Message Element on which this Attribute Coercion shall be applied Enumerated values: N_CREATE_RQ, C_STORE_RQ, C_FIND_RQ or C_FIND_RSP","
    .. _dcmDIMSE:

    dcmDIMSE_"
    "DICOM Transfer Role",string,"DICOM Transfer Role of peer DICOM AE. Enumerated values: SCU or SCP","
    .. _dicomTransferRole:

    dicomTransferRole_"
    "Rule Priority",integer,"Rule Priority.","
    .. _dcmRulePriority:

    dcmRulePriority_"
    "AE Title(s)",string,"Application Entity (AE) title of peer DICOM AE for which this Attribute Coercion shall be applied. Apply on any if absent.","
    .. _dcmAETitle:

    dcmAETitle_"
    "Hostname(s)",string,"DNS hostname of peer DICOM AE for which this Attribute Coercion shall be applied. Apply on any if absent.","
    .. _dcmHostname:

    dcmHostname_"
    "SOP Class UID(s)",string,"UID of SOP Class for which this Attribute Coercion shall be applied. Apply on any if absent.","
    .. _dcmSOPClass:

    dcmSOPClass_"
    "De-identification(s)",string,"De-identify objects according the Basic Application Level Confidentiality Profile specified in DICOM PS3.15. Selecting any Option implicitly includes the Basic Application Level Confidentiality Profile. Enumerated values: BasicApplicationConfidentialityProfile, RetainLongitudinalTemporalInformationFullDatesOption, RetainDeviceIdentityOption, RetainInstitutionIdentityOption or RetainUIDsOption","
    .. _dcmDeIdentification:

    dcmDeIdentification_"
    "XSL Stylesheet URI",string,"Specifies URI of the XSL style sheet for Attribute Coercion","
    .. _dcmURI:

    dcmURI_"
    "No Attribute Keyword",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT","
    .. _dcmNoKeywords:

    dcmNoKeywords_"
    "Merge MWL Matching Key",string,"Specifies attribute of received object to lookup MWL Item used to coerce request attributes. If absent, request attributes of received objects will not be coerced. Enumerated values: AccessionNumber, StudyInstanceUID or ScheduledProcedureStepID","
    .. _dcmMergeMWLMatchingKey:

    dcmMergeMWLMatchingKey_"
    "Merge MWL Template URI",string,"Specifies URI for the style sheet to coerce request attributes of received objects from matching DICOM MWL items. Only effective, if dcmMergeMWLMatchingKey is specified.","
    .. _dcmMergeMWLTemplateURI:

    dcmMergeMWLTemplateURI_"
    "Leading C-FIND SCP",string,"AE Title of external C-FIND SCP for Attribute Coercion with Patient and Study attributes fetched from this AE. If no particular Attribute Set is specified for the C-FIND SCP, all Attributes of the configured Patient and Study Attribute Filter will be fetched.","
    .. _dcmLeadingCFindSCP:

    dcmLeadingCFindSCP_"
    "Attribute Update Policy",string,"Specifies how attributes shall be updated with attributes fetched from Leading C-FIND SCP. Enumerated values: SUPPLEMENT, MERGE or OVERWRITE","
    .. _dcmAttributeUpdatePolicy:

    dcmAttributeUpdatePolicy_"
    "Nullify Attribute Tag(s)",string,"DICOM Tag of Attribute to be nullified as hex string","
    .. _dcmNullifyTag:

    dcmNullifyTag_"
    "Nullify Issuer of Patient ID",string,"Conditionally nullify Issuer of Patient ID (0010,0021) and Issuer of Patient ID Qualifiers Sequence (0010,0024) from received objects Enumerated values: ALWAYS, MATCHING or NOT_MATCHING","
    .. _dcmNullifyIssuerOfPatientID:

    dcmNullifyIssuerOfPatientID_"
    "Issuer of Patient ID(s)",string,"Issuer of Patient ID (0010,0021), and optionally also values for the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Patient ID Qualifiers Sequence (0010,0024) against values in received objects are matched, if Nullify Issuer of Patient ID is set to MATCHING or NOT_MATCHING. Format: <Issuer of Patient ID> [& <Universal Entity ID> & <Universal Entity ID Type>].","
    .. _dcmIssuerOfPatientID:

    dcmIssuerOfPatientID_"
    "Supplement from Device",string,"Name of Device from which Assigning Authorities and other information is taken to supplement received Composite Objects and MPPS.","
    .. _dcmSupplementFromDeviceName:

    dcmSupplementFromDeviceName_"
