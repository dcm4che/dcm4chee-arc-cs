UPS on Store
============
Create/Update Workitem in unified Worklist on receive of Composite Object

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS on Store Attributes (LDAP Object: dcmUpsOnStore)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmUPSOnStoreID:

    :ref:`UPS on Store ID <dcmUPSOnStoreID>`",string,"ID of UPS on Store Rule

    (dcmUPSOnStoreID)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format (SendingHostname|SendingApplicationEntityTitle|ReceivingHostname|ReceivingApplicationEntityTitle|{attributeID})[!]={regEx}

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Time Conditions(s) <dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmUPSLabel:

    :ref:`Procedure Step Label <dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSPriority:

    :ref:`Priority <dcmUPSPriority>`",string,"Value of Scheduled Procedure Step Priority (0074,1200) in created UPS. Enumerated Values: HIGH, MEDIUM, LOW. If absent, MEDIUM will be applied. Enumerated values: HIGH, MEDIUM or LOW.

    (dcmUPSPriority)"
    "
    .. _dcmUPSInputReadinessState:

    :ref:`Input Readiness State <dcmUPSInputReadinessState>`",string,"Value of Input Readiness State (0040,4041) in created UPS Enumerated values: INCOMPLETE, UNAVAILABLE or READY.

    (dcmUPSInputReadinessState)"
    "
    .. _dcmUPSStartDateTimeDelay:

    :ref:`Scheduled Procedure Step Start DateTime Delay <dcmUPSStartDateTimeDelay>`",string,"Delay of Scheduled Procedure Step Start DateTime (0040,4005) in created UPS from receive time in format PnDTnHnMn.nS. No delay if absent.

    (dcmUPSStartDateTimeDelay)"
    "
    .. _dcmUPSCompletionDateTimeDelay:

    :ref:`Expected Completion DateTime Delay <dcmUPSCompletionDateTimeDelay>`",string,"Delay of Expected Completion DateTime (0040,4011) in created UPS from receive time in format PnDTnHnMn.nS. If absent, no Expected Completion Date and Time will be set.

    (dcmUPSCompletionDateTimeDelay)"
    "
    .. _dcmUPSInstanceUIDBasedOnName:

    :ref:`UPS Instance UID based on name <dcmUPSInstanceUIDBasedOnName>`",string,"Value used to generate name based SOP Instance UID (0008,0018) in created UPS. Typically, the value will include {StudyInstanceUID}, {SeriesInstanceUID} or {SOPInstanceUID} to create a different UPS for each received Study, Series or Object. If absent, a random generated SOP Instance UID (0008,0018) will be used.

    (dcmUPSInstanceUIDBasedOnName)"
    "
    .. _dcmUPSIncludeInputInformation:

    :ref:`Include Input Information <dcmUPSIncludeInputInformation>`",string,"Indicates if received objects shall be referenced in the Input Information Sequence (0040,4021) in created UPS. SINGLE (= do not updating existing UPS), APPEND (= update existing UPS in state SCHEDULED), SINGLE_OR_CREATE (= if UPS already exists, create new UPS with derived UID), APPEND_OR_CREATE (= if existing UPS is no longer in state SCHEDULED, create new UPS with derived UID). Enumerated values: NO, SINGLE, APPEND, SINGLE_OR_CREATE or APPEND_OR_CREATE.

    (dcmUPSIncludeInputInformation)"
    "
    .. _dcmDestinationAE:

    :ref:`Destination AE <dcmDestinationAE>`",string,"Title of a DICOM Application Entity to which Instances will be stored.

    (dcmDestinationAE)"
    "
    .. _dcmEntity:

    :ref:`Scope of Accumulation <dcmEntity>`",string,"Scope of Accumulation Enumerated values: Study, Series or MPPS.

    (dcmEntity)"
    "
    .. _dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <dcmUPSScheduledWorkitemCode>`",string,"Item of Scheduled Workitem Code Sequence (0040,4018) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code <dcmUPSScheduledStationNameCode>`",string,"Item of Scheduled Station Name Code Sequence (0040,4025) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code <dcmUPSScheduledStationClassCode>`",string,"Item of Scheduled Station Class Code Sequence (0040,4026) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code <dcmUPSScheduledStationLocationCode>`",string,"Item of Scheduled Station Geographic Location Code Sequence (0040,4027) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSScheduledHumanPerformerCode:

    :ref:`Scheduled Human Performer Code <dcmUPSScheduledHumanPerformerCode>`",string,"Item of Human Performer Code Sequence (0040,4009) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledHumanPerformerCode)"
    "
    .. _dcmUPSScheduledHumanPerformerName:

    :ref:`Scheduled Human Performer Name <dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmAdmissionID:

    :ref:`Admission Number <dcmAdmissionID>`",string,"Value of Admission ID (0038,0010) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmAdmissionID)"
    "
    .. _dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID <dicomIssuerOfAdmissionID>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAdmissionID)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) of the received object shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
    "
    .. _dcmUPSIncludeReferencedRequest:

    :ref:`Include Referenced Request <dcmUPSIncludeReferencedRequest>`",boolean,"Indicates if the Study Instance UID (0020,000D) of the received object and the specified Accession Number (0008,0050), Requested Procedure ID (0040,1001) and Requesting Service (0032,1033) shall be included in the item of the Referenced Request Sequence (0040,A370) in the created UPS. Otherwise an empty Referenced Request Sequence (0040,A370) is included.

    (dcmUPSIncludeReferencedRequest)"
    "
    .. _dcmAccessionNumber:

    :ref:`Accession Number <dcmAccessionNumber>`",string,"Value of Accession Number (0008,0050) in Item of Referenced Request Sequence (0040,A370) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmAccessionNumber)"
    "
    .. _dicomIssuerOfAccessionNumber:

    :ref:`Issuer of Accession Number <dicomIssuerOfAccessionNumber>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) in Item of Issuer of Accession Number Sequence (0008,0051) in Item of Referenced Request Sequence (0040,A370) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAccessionNumber)"
    "
    .. _dcmRequestedProcedureID:

    :ref:`Requested Procedure ID <dcmRequestedProcedureID>`",string,"Value of Requested Procedure ID (0040,1001) in Item of Referenced Request Sequence (0040,A370) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmRequestedProcedureID)"
    "
    .. _dcmRequestedProcedureDescription:

    :ref:`Requested Procedure Description <dcmRequestedProcedureDescription>`",string,"Value of Requested Procedure Description (0032,1060) in Item of Referenced Request Sequence (0040,A370) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmRequestedProcedureDescription)"
    "
    .. _dcmRequestingPhysician:

    :ref:`Requesting Physician <dcmRequestingPhysician>`",string,"Value of Requesting Physician (0032,1032) in Item of Referenced Request Sequence (0040,A370) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmRequestingPhysician)"
    "
    .. _dcmRequestingService:

    :ref:`Requesting Service <dcmRequestingService>`",string,"Value of Requesting Service (0032,1033) in Item of Referenced Request Sequence (0040,A370) in created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmRequestingService)"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI <dcmURI>`",string,"Specifies URI of the XSL style sheet to include additional attributes in created UPS.

    (dcmURI)"
    "
    .. _dcmNoKeywords:

    :ref:`No Attribute Keyword <dcmNoKeywords>`",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT.

    (dcmNoKeywords)"
