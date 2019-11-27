UPS on Store
============
Create/Update Workitem in unified Worklist on receive of Composite Object

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS on Store Attributes (LDAP Object: dcmUpsOnStore)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of UPS on Store Rule

    (cn)"
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

    :ref:`Procedure Step Label <dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) of created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) of created UPS. {attributeID} will be replaced by the value of that attribute in the received dataset.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSPriority:

    :ref:`Priority <dcmUPSPriority>`",string,"Value of Scheduled Procedure Step Priority (0074,1200) of created UPS. Enumerated Values: HIGH, MEDIUM, LOW. If absent, MEDIUM will be applied. Enumerated values: HIGH, MEDIUM or LOW.

    (dcmUPSPriority)"
    "
    .. _dcmUPSInputReadinessState:

    :ref:`Priority <dcmUPSInputReadinessState>`",string,"Value of Input Readiness State (0040,4041) of created UPS Enumerated values: INCOMPLETE, UNAVAILABLE or READY.

    (dcmUPSInputReadinessState)"
    "
    .. _dcmDuration:

    :ref:`Schedule Delay <dcmDuration>`",string,"Delay of Scheduled Procedure Step Start DateTime (0040,4005) of created UPS from receive time in format PnDTnHnMn.nS. No delay if absent.

    (dcmDuration)"
    "
    .. _dcmUPSInstanceUIDBasedOnName:

    :ref:`UPS Instance UID based on name <dcmUPSInstanceUIDBasedOnName>`",string,"Value used to generate name based SOP Instance UID (0008,0018) of created UPS. Typically, the value will include {StudyInstanceUID}, {SeriesInstanceUID} or {SOPInstanceUID} to create a different UPS for each received Study, Series or Object. If absent, a random generated SOP Instance UID (0008,0018) will be used.

    (dcmUPSInstanceUIDBasedOnName)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) of the received object shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
    "
    .. _dcmUPSIncludeInputInformation:

    :ref:`Include Input Information <dcmUPSIncludeInputInformation>`",string,"Indicates if received objects shall be referenced in the Input Information Sequence (0040,4021) of created UPS. SINGLE (= do not updating existing UPS), APPEND (= update existing UPS in state SCHEDULED), SINGLE_OR_CREATE (= if UPS already exists, create new UPS with derived UID), APPEND_OR_CREATE (= if existing UPS is no longer in state SCHEDULED, create new UPS with derived UID). Enumerated values: NO, SINGLE, APPEND, SINGLE_OR_CREATE or APPEND_OR_CREATE.

    (dcmUPSIncludeInputInformation)"
    "
    .. _dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <dcmUPSScheduledWorkitemCode>`",string,"Item of Scheduled Workitem Code Sequence (0040,4018) of created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code <dcmUPSScheduledStationNameCode>`",string,"Item of Scheduled Station Name Code Sequence (0040,4025) of created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code Seence <dcmUPSScheduledStationClassCode>`",string,"Item of Scheduled Station Class Code Sequence (0040,4026) of created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code <dcmUPSScheduledStationLocationCode>`",string,"Item of Scheduled Station Geographic Location Code Sequence (0040,4027) of created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSScheduledHumanPerformerCode:

    :ref:`Scheduled Human Performer Code <dcmUPSScheduledHumanPerformerCode>`",string,"Item of Human Performer Code Sequence (0040,4009) of Item of Scheduled Human Performers Sequence (0040,4034) of created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledHumanPerformerCode)"
    "
    .. _dcmUPSScheduledHumanPerformerName:

    :ref:`Scheduled Human Performer Name <dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) of Item of Scheduled Human Performers Sequence (0040,4034) of created UPS.

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) of Item of Scheduled Human Performers Sequence (0040,4034) of created UPS.

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI <dcmURI>`",string,"Specifies URI of the XSL style sheet to include additional attributes in created UPS.

    (dcmURI)"
    "
    .. _dcmNoKeywords:

    :ref:`No Attribute Keyword <dcmNoKeywords>`",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT.

    (dcmNoKeywords)"
