UPS on HL7
==========
Create/Update Workitem in unified Worklist on receive of HL7v2 message

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS on HL7 Attributes (LDAP Object: dcmUpsOnHL7)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _hl7UPSOnHL7ID:

    :ref:`UPS on HL7 ID <hl7UPSOnHL7ID>`",string,"ID of UPS on HL7 Rule

    (hl7UPSOnHL7ID)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format <SEG>-<Seq#>[.<Comp#>[.<SubComp#>]][!]=<regEx>. Example: MSH-4=FORWARD or MSH-9=ORM\^O01 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Time Conditions(s) <dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmUPSLabel:

    :ref:`Procedure Step Label <dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. If absent or if value could not be found in HL7 Message, HL7 Application Name of the receiving HL7 Application will be used.

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

    :ref:`Scheduled Procedure Step Start DateTime Delay <dcmUPSStartDateTimeDelay>`",string,"Delay of Scheduled Procedure Step Start DateTime (0040,4005) in created UPS from receive time in format PnDTnHnMn.nS. Only effective, if no Scheduled Procedure Step Start DateTime is found in HL7 Message.

    (dcmUPSStartDateTimeDelay)"
    "
    .. _dcmUPSCompletionDateTimeDelay:

    :ref:`Expected Completion DateTime Delay <dcmUPSCompletionDateTimeDelay>`",string,"Delay of Expected Completion DateTime (0040,4011) in created UPS from receive time in format PnDTnHnMn.nS. If absent, no Expected Completion Date and Time will be set.

    (dcmUPSCompletionDateTimeDelay)"
    "
    .. _dcmUPSInstanceUIDBasedOnName:

    :ref:`UPS Instance UID based on name <dcmUPSInstanceUIDBasedOnName>`",string,"Value used to generate name based SOP Instance UID (0008,0018) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. If absent, a random generated SOP Instance UID (0008,0018) will be used.

    (dcmUPSInstanceUIDBasedOnName)"
    "
    .. _dcmDestinationAE:

    :ref:`Destination AE <dcmDestinationAE>`",string,"Title of a DICOM Application Entity to which Instances will be stored.

    (dcmDestinationAE)"
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

    :ref:`Scheduled Human Performer Name <dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) in the received HL7 message shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
    "
    .. _dcmUPSIncludeReferencedRequest:

    :ref:`Include Referenced Request <dcmUPSIncludeReferencedRequest>`",boolean,"Indicates if the Study Instance UID (0020,000D) in the received HL7 message and the specified Accession Number (0008,0050), Requested Procedure ID (0040,1001) and Requesting Service (0032,1033) shall be included in the item of the Referenced Request Sequence (0040,A370) in the created UPS. Otherwise an empty Referenced Request Sequence (0040,A370) is included.

    (dcmUPSIncludeReferencedRequest)"
    "
    .. _dcmStudyInstanceUID:

    :ref:`Study Instance UID <dcmStudyInstanceUID>`",string,"Value of Study Instance UID (0020,000D) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmStudyInstanceUID)"
    "
    .. _dcmAdmissionID:

    :ref:`Admission Number <dcmAdmissionID>`",string,"Value of Admission ID (0038,0010) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmAdmissionID)"
    "
    .. _dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID <dicomIssuerOfAdmissionID>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAdmissionID)"
    "
    .. _dcmAccessionNumber:

    :ref:`Accession Number <dcmAccessionNumber>`",string,"Value of Accession Number (0008,0050) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmAccessionNumber)"
    "
    .. _dicomIssuerOfAccessionNumber:

    :ref:`Issuer of Accession Number <dicomIssuerOfAccessionNumber>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) in Item of Issuer of Accession Number Sequence (0008,0051) in Item of Referenced Request Sequence (0040,A370) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAccessionNumber)"
    "
    .. _dcmRequestedProcedureID:

    :ref:`Requested Procedure ID <dcmRequestedProcedureID>`",string,"Value of Requested Procedure ID (0040,1001) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmRequestedProcedureID)"
    "
    .. _dcmRequestedProcedureDescription:

    :ref:`Requested Procedure Description <dcmRequestedProcedureDescription>`",string,"Value of Requested Procedure Description (0032,1060) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmRequestedProcedureDescription)"
    "
    .. _dcmRequestingPhysician:

    :ref:`Requesting Physician <dcmRequestingPhysician>`",string,"Value of Requesting Physician (0032,1032) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmRequestingPhysician)"
    "
    .. _dcmRequestingService:

    :ref:`Requesting Service <dcmRequestingService>`",string,"Value of Requesting Service (0032,1033) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmRequestingService)"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI <dcmURI>`",string,"Specifies URI of the XSL style sheet to to transcode received HL7 message to include attributes in created UPS.

    (dcmURI)"
