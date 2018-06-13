Archive Attribute Coercion
==========================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Attribute Coercion Attributes (LDAP Object: dcmArchiveAttributeCoercion)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name of the Archive Attribute Coercion"
    "
    .. _dcmDIMSE:

    :ref:`DIMSE (dcmDIMSE) <dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied Enumerated values: N_CREATE_RQ, C_STORE_RQ, C_FIND_RQ or C_FIND_RSP"
    "
    .. _dicomTransferRole:

    :ref:`DICOM Transfer Role (dicomTransferRole) <dicomTransferRole>`",string,"DICOM Transfer Role of peer DICOM AE. Enumerated values: SCU or SCP"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority (dcmRulePriority) <dcmRulePriority>`",integer,"Rule Priority."
    "
    .. _dcmAETitle:

    :ref:`AE Title(s) (dcmAETitle) <dcmAETitle>`",string,"Application Entity (AE) title of peer DICOM AE for which this Attribute Coercion shall be applied. Apply on any if absent."
    "
    .. _dcmHostname:

    :ref:`Hostname(s) (dcmHostname) <dcmHostname>`",string,"DNS hostname of peer DICOM AE for which this Attribute Coercion shall be applied. Apply on any if absent."
    "
    .. _dcmSOPClass:

    :ref:`SOP Class UID(s) (dcmSOPClass) <dcmSOPClass>`",string,"UID of SOP Class for which this Attribute Coercion shall be applied. Apply on any if absent."
    "
    .. _dcmDeIdentification:

    :ref:`De-identification(s) (dcmDeIdentification) <dcmDeIdentification>`",string,"De-identify objects according the Basic Application Level Confidentiality Profile specified in DICOM PS3.15. Selecting any Option implicitly includes the Basic Application Level Confidentiality Profile. Enumerated values: BasicApplicationConfidentialityProfile, RetainLongitudinalTemporalInformationFullDatesOption, RetainDeviceIdentityOption, RetainInstitutionIdentityOption or RetainUIDsOption"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI (dcmURI) <dcmURI>`",string,"Specifies URI of the XSL style sheet for Attribute Coercion"
    "
    .. _dcmNoKeywords:

    :ref:`No Attribute Keyword (dcmNoKeywords) <dcmNoKeywords>`",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT"
    "
    .. _dcmMergeMWLMatchingKey:

    :ref:`Merge MWL Matching Key (dcmMergeMWLMatchingKey) <dcmMergeMWLMatchingKey>`",string,"Specifies attribute of received object to lookup MWL Item used to coerce request attributes. If absent, request attributes of received objects will not be coerced. Enumerated values: AccessionNumber, StudyInstanceUID or ScheduledProcedureStepID"
    "
    .. _dcmMergeMWLTemplateURI:

    :ref:`Merge MWL Template URI (dcmMergeMWLTemplateURI) <dcmMergeMWLTemplateURI>`",string,"Specifies URI for the style sheet to coerce request attributes of received objects from matching DICOM MWL items. Only effective, if dcmMergeMWLMatchingKey is specified."
    "
    .. _dcmLeadingCFindSCP:

    :ref:`Leading C-FIND SCP (dcmLeadingCFindSCP) <dcmLeadingCFindSCP>`",string,"AE Title of external C-FIND SCP for Attribute Coercion with Patient and Study attributes fetched from this AE. If no particular Attribute Set is specified for the C-FIND SCP, all Attributes of the configured Patient and Study Attribute Filter will be fetched."
    "
    .. _dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy (dcmAttributeUpdatePolicy) <dcmAttributeUpdatePolicy>`",string,"Specifies how attributes shall be updated with attributes fetched from Leading C-FIND SCP. Enumerated values: SUPPLEMENT, MERGE or OVERWRITE"
    "
    .. _dcmNullifyTag:

    :ref:`Nullify Attribute Tag(s) (dcmNullifyTag) <dcmNullifyTag>`",string,"DICOM Tag of Attribute to be nullified as hex string"
    "
    .. _dcmNullifyIssuerOfPatientID:

    :ref:`Nullify Issuer of Patient ID (dcmNullifyIssuerOfPatientID) <dcmNullifyIssuerOfPatientID>`",string,"Conditionally nullify Issuer of Patient ID (0010,0021) and Issuer of Patient ID Qualifiers Sequence (0010,0024) from received objects Enumerated values: ALWAYS, MATCHING or NOT_MATCHING"
    "
    .. _dcmIssuerOfPatientID:

    :ref:`Issuer of Patient ID(s) (dcmIssuerOfPatientID) <dcmIssuerOfPatientID>`",string,"Issuer of Patient ID (0010,0021), and optionally also values for the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Patient ID Qualifiers Sequence (0010,0024) against values in received objects are matched, if Nullify Issuer of Patient ID is set to MATCHING or NOT_MATCHING. Format: <Issuer of Patient ID> [& <Universal Entity ID> & <Universal Entity ID Type>]."
    "
    .. _dcmSupplementFromDeviceName:

    :ref:`Supplement from Device (dcmSupplementFromDeviceName) <dcmSupplementFromDeviceName>`",string,"Name of Device from which Assigning Authorities and other information is taken to supplement received Composite Objects and MPPS."
