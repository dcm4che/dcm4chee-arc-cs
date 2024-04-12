Archive Attribute Coercion - Legacy
===================================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Attribute Coercion - Legacy Attributes (LDAP Object: dcmArchiveAttributeCoercion)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Archive Attribute Coercion

    (cn)"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority <dcmRulePriority>`",integer,"If the condition of several archive attribute coercion (legacy) matches for a received image, higher priority coercion is applied. If there are several matching coercions with equal priority, it is undefined which coercion gets applied.

    (dcmRulePriority)"
    "
    .. _dcmDIMSE:

    :ref:`DIMSE <dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied. Also `applicable if the requests are received over web. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Legacy-Archive-Attribute-Coercion---Application-of-multiple-coercions-using-one-coercion-rule#dimse>`_

    Enumerated values:

    N_CREATE_RQ

    C_STORE_RQ

    C_FIND_RQ

    C_FIND_RSP

    (dcmDIMSE)"
    "
    .. _dicomTransferRole:

    :ref:`DICOM Transfer Role <dicomTransferRole>`",string,"DICOM Transfer Role of peer DICOM AE.

    Enumerated values:

    SCU

    SCP

    (dicomTransferRole)"
    "
    .. _dcmSOPClass:

    :ref:`SOP Class UID(s) <dcmSOPClass>`",string,"UID of SOP Class for which this Attribute Coercion shall be applied. Apply on any if absent.

    (dcmSOPClass)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmRetrieveAsReceived:

    :ref:`Retrieve as Received <dcmRetrieveAsReceived>`",boolean,"Disables merge of DB information into the retrieved Composite Object, returning the objects as received. Only effective with DIMSE = C_STORE_RQ and DICOM Transfer Role = SCP.

    (dcmRetrieveAsReceived)"
    "
    .. _dcmDeIdentification:

    :ref:`De-identification(s) <dcmDeIdentification>`",string,"De-identify objects according the Basic Application Level Confidentiality Profile specified in DICOM PS3.15. Selecting any Option implicitly includes the Basic Application Level Confidentiality Profile.

    Enumerated values:

    BasicApplicationConfidentialityProfile

    RetainLongitudinalTemporalInformationFullDatesOption

    RetainDeviceIdentityOption

    RetainInstitutionIdentityOption

    RetainUIDsOption

    RetainPatientIDHashOption

    (dcmDeIdentification)"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI <dcmURI>`",string,"Specifies URI of the XSL style sheet for Attribute Coercion

    (dcmURI)"
    "
    .. _dcmNoKeywords:

    :ref:`No Attribute Keyword <dcmNoKeywords>`",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT

    (dcmNoKeywords)"
    "
    .. _dcmMergeMWLMatchingKey:

    :ref:`Merge MWL Matching Key <dcmMergeMWLMatchingKey>`",string,"Specifies attribute of received object to lookup MWL Item used to coerce request attributes. If absent, request attributes of received objects will not be coerced. Refer `applicability of merge MWL matching keys. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Legacy-Archive-Attribute-Coercion---Application-of-multiple-coercions-using-one-coercion-rule#configurations-specific-to-merging-from-mwl-coercion-type>`_

    Enumerated values:

    PatientID

    PatientIDOnly

    PatientIDAccessionNumber

    AccessionNumber

    StudyInstanceUID

    ScheduledProcedureStepID

    (dcmMergeMWLMatchingKey)"
    "
    .. _dcmMergeMWLTemplateURI:

    :ref:`Merge MWL Template URI <dcmMergeMWLTemplateURI>`",string,"Specifies URI for the style sheet to coerce request attributes of received objects from matching DICOM MWL items. Only effective, if dcmMergeMWLMatchingKey is specified.

    (dcmMergeMWLTemplateURI)"
    "
    .. _dcmMergeMWLSCP:

    :ref:`Merge MWL SCP <dcmMergeMWLSCP>`",string,"AE Title of External MWL SCP used to lookup MWL Item to coerce request attributes of received objects. If configured, external MWL SCP is queried by invoking a C-FIND RQ of the DICOM MWL Service and Merge Local MWL SCP is ignored.

    (dcmMergeMWLSCP)"
    "
    .. _dcmMergeLocalMWLWorklistLabel:

    :ref:`Merge Local MWL Worklist Label(s) <dcmMergeLocalMWLWorklistLabel>`",string,"Only consider MWL items with one of the specified values of its Worklist Label (0074,1202) in the Archive DB to coerce request attributes of received objects. If absent, the Archive DB is queried for matching MWL items with any Worklist Label (0074,1202).

    (dcmMergeLocalMWLWorklistLabel)"
    "
    .. _dcmMergeLocalMWLWithStatus:

    :ref:`Merge Local MWL With Status(s) <dcmMergeLocalMWLWithStatus>`",string,"Only consider MWL items with one of the specified Scheduled Procedure Step Status codes. If absent, MWL items with any Scheduled Procedure Step Status are considered.

    Enumerated values:

    SCHEDULED

    ARRIVED

    READY

    STARTED

    DEPARTED

    CANCELED

    DISCONTINUED

    COMPLETED

    (dcmMergeLocalMWLWithStatus)"
    "
    .. _dcmMWLImportFilterBySCU:

    :ref:`Merge MWL Filter by SCU <dcmMWLImportFilterBySCU>`",boolean,"Indicates to apply specified filter on matches returned by external MWL SCP.

    (dcmMWLImportFilterBySCU)"
    "
    .. _dcmLeadingCFindSCP:

    :ref:`Leading C-FIND SCP <dcmLeadingCFindSCP>`",string,"AE Title of external C-FIND SCP for Attribute Coercion with Patient and Study attributes fetched from this AE. If no particular Attribute Set is specified for the C-FIND SCP, all Attributes of the configured Patient and Study Attribute Filter will be fetched.

    (dcmLeadingCFindSCP)"
    "
    .. _dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy <dcmAttributeUpdatePolicy>`",string,"Specifies how attributes shall be updated with attributes fetched from Leading C-FIND SCP. Refer `Attribute Update Policies meanings. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Attribute-Update-Policy>`_

    Enumerated values:

    PRESERVE

    SUPPLEMENT

    MERGE

    OVERWRITE

    (dcmAttributeUpdatePolicy)"
    "
    .. _dcmTrimISO2022CharacterSet:

    :ref:`Trim ISO 2022 Character Set <dcmTrimISO2022CharacterSet>`",boolean,"Replace single code for Single-Byte Character Sets with Code Extensions by code for Single-Byte Character Sets without Code Extensions. Refer `character sets to which this coercion applies. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Legacy-Archive-Attribute-Coercion---Application-of-multiple-coercions-using-one-coercion-rule#configurations-specific-to-trim-iso-2022-character-set-coercion-type>`_

    (dcmTrimISO2022CharacterSet)"
    "
    .. _dcmUseCallingAETitleAs:

    :ref:`Use Calling AE Title as <dcmUseCallingAETitleAs>`",string,"Identifies the attribute which is set to the value of the Calling AET if it is absent or empty. ScheduledStationAETitle (= Scheduled Station AE Title (0040,0001) in item of Scheduled Procedure Step Sequence (0040,0100)), SendingApplicationEntityTitleOfSeries (= Sending Application Entity Title of Series (7777,xx37)).

    Enumerated values:

    ScheduledStationAETitle

    SendingApplicationEntityTitleOfSeries

    (dcmUseCallingAETitleAs)"
    "
    .. _dcmNullifyTag:

    :ref:`Nullify Attribute Tag(s) <dcmNullifyTag>`",string,"DICOM Tag of Attribute to be nullified as hex string

    (dcmNullifyTag)"
    "
    .. _dcmMergeAttribute:

    :ref:`Merge Attribute(s) <dcmMergeAttribute>`",string,"Merge DICOM Attribute in format {attributeID}={value}. {attributeID} inside {value} will be replaced by the value of that attribute in the original dataset. Refer `applicability, formats and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Legacy-Archive-Attribute-Coercion---Application-of-multiple-coercions-using-one-coercion-rule#configurations-specific-to-merge-attributes-coercion-type>`_

    (dcmMergeAttribute)"
    "
    .. _dcmNullifyIssuerOfPatientID:

    :ref:`Nullify Issuer of Patient ID <dcmNullifyIssuerOfPatientID>`",string,"Conditionally nullify Issuer of Patient ID (0010,0021) and Issuer of Patient ID Qualifiers Sequence (0010,0024) from received objects

    Enumerated values:

    ALWAYS

    MATCHING

    NOT_MATCHING

    (dcmNullifyIssuerOfPatientID)"
    "
    .. _dcmIssuerOfPatientID:

    :ref:`Issuer of Patient ID(s) <dcmIssuerOfPatientID>`",string,"Issuer of Patient ID (0010,0021), and optionally also values for the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Patient ID Qualifiers Sequence (0010,0024) against values in received objects are matched, if Nullify Issuer of Patient ID is set to MATCHING or NOT_MATCHING. Specify values in format: {IssuerOfPatientID}[&{UniversalEntityID&UniversalEntityIDType}].

    (dcmIssuerOfPatientID)"
    "
    .. _dcmIssuerOfPatientIDFormat:

    :ref:`Issuer Of Patient ID Format <dcmIssuerOfPatientIDFormat>`",string,"Format of Issuer of Patient ID (0010,0021) derived from other attributes. E.g. ""{00100010,hash}-{00100030}"": use hash value of Patient Name and Birth Date separated by ""-"". Refer `applicability of this field and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Legacy-Archive-Attribute-Coercion---Application-of-multiple-coercions-using-one-coercion-rule#configurations-specific-to-supplement-issuer-of-patient-id-format-coercion-type>`_

    (dcmIssuerOfPatientIDFormat)"
    "
    .. _dcmSupplementFromDeviceReference:

    :ref:`Supplement from Device <dcmSupplementFromDeviceReference>`",string,"Name of Device from which Assigning Authorities and other information is supplemented. Refer `applicability to entities and information supplemented from device. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Legacy-Archive-Attribute-Coercion---Application-of-multiple-coercions-using-one-coercion-rule#configurations-specific-to-supplementing-from-device-coercion-type>`_

    (dcmSupplementFromDeviceReference)"
