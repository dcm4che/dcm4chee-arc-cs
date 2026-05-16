UPS on HL7
==========
Create/Update Workitem in unified Worklist on receive of HL7v2 message

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS on HL7 Attributes (LDAP Object: dcmUpsOnHL7)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _hl7UPSOnHL7ID:
    .. _upsOnHL7-hl7UPSOnHL7ID:

    :ref:`UPS on HL7 ID <upsOnHL7-hl7UPSOnHL7ID>`",string,"ID of UPS on HL7 Rule

    (hl7UPSOnHL7ID)"
    "
    .. _dcmProperty:
    .. _upsOnHL7-dcmProperty:

    :ref:`Conditions(s) <upsOnHL7-dcmProperty>`",string,"Conditions in format <SEG>-<Seq#>[.<Comp#>[.<SubComp#>]][!]=<regEx>. Example: MSH-4=FORWARD or MSH-9=ORM\^O01 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmSchedule:
    .. _upsOnHL7-dcmSchedule:

    :ref:`Time Conditions(s) <upsOnHL7-dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmUPSLabel:
    .. _upsOnHL7-dcmUPSLabel:

    :ref:`Procedure Step Label <upsOnHL7-dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:
    .. _upsOnHL7-dcmUPSWorklistLabel:

    :ref:`Worklist Label <upsOnHL7-dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. If absent or if value could not be found in HL7 Message, HL7 Application Name of the receiving HL7 Application will be used. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSPriority:
    .. _upsOnHL7-dcmUPSPriority:

    :ref:`Priority <upsOnHL7-dcmUPSPriority>`",string,"Value of Scheduled Procedure Step Priority (0074,1200) in created UPS.

    Enumerated values:

    HIGH

    MEDIUM

    LOW

    (dcmUPSPriority)"
    "
    .. _dcmUPSInputReadinessState:
    .. _upsOnHL7-dcmUPSInputReadinessState:

    :ref:`Input Readiness State <upsOnHL7-dcmUPSInputReadinessState>`",string,"Value of Input Readiness State (0040,4041) in created UPS

    Enumerated values:

    INCOMPLETE

    UNAVAILABLE

    READY

    (dcmUPSInputReadinessState)"
    "
    .. _dcmUPSStartDateTimeDelay:
    .. _upsOnHL7-dcmUPSStartDateTimeDelay:

    :ref:`Scheduled Procedure Step Start DateTime Delay <upsOnHL7-dcmUPSStartDateTimeDelay>`",string,"Delay of Scheduled Procedure Step Start DateTime (0040,4005) in created UPS from receive time in format PnDTnHnMn.nS. Only effective, if no Scheduled Procedure Step Start DateTime is found in HL7 Message.

    (dcmUPSStartDateTimeDelay)"
    "
    .. _dcmUPSCompletionDateTimeDelay:
    .. _upsOnHL7-dcmUPSCompletionDateTimeDelay:

    :ref:`Expected Completion DateTime Delay <upsOnHL7-dcmUPSCompletionDateTimeDelay>`",string,"Delay of Expected Completion DateTime (0040,4011) in created UPS from receive time in format PnDTnHnMn.nS. If absent, no Expected Completion Date and Time will be set.

    (dcmUPSCompletionDateTimeDelay)"
    "
    .. _dcmUPSInstanceUIDBasedOnName:
    .. _upsOnHL7-dcmUPSInstanceUIDBasedOnName:

    :ref:`UPS Instance UID based on name <upsOnHL7-dcmUPSInstanceUIDBasedOnName>`",string,"Value used to generate name based SOP Instance UID (0008,0018) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. If absent, a random generated SOP Instance UID (0008,0018) will be used. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmUPSInstanceUIDBasedOnName)"
    "
    .. _dcmDestinationAE:
    .. _upsOnHL7-dcmDestinationAE:

    :ref:`Destination AE <upsOnHL7-dcmDestinationAE>`",string,"Title of a DICOM Application Entity to which Instances will be stored.

    (dcmDestinationAE)"
    "
    .. _dcmUPSScheduledWorkitemCode:
    .. _upsOnHL7-dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <upsOnHL7-dcmUPSScheduledWorkitemCode>`",string,"Item of Scheduled Workitem Code Sequence (0040,4018) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:
    .. _upsOnHL7-dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code(s) <upsOnHL7-dcmUPSScheduledStationNameCode>`",string,"Item of Scheduled Station Name Code Sequence (0040,4025) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:
    .. _upsOnHL7-dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code(s) <upsOnHL7-dcmUPSScheduledStationClassCode>`",string,"Item of Scheduled Station Class Code Sequence (0040,4026) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:
    .. _upsOnHL7-dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code(s) <upsOnHL7-dcmUPSScheduledStationLocationCode>`",string,"Item of Scheduled Station Geographic Location Code Sequence (0040,4027) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSScheduledHumanPerformerCode:
    .. _upsOnHL7-dcmUPSScheduledHumanPerformerCode:

    :ref:`Scheduled Human Performer Code(s) <upsOnHL7-dcmUPSScheduledHumanPerformerCode>`",string,"Item of Human Performer Code Sequence (0040,4009) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledHumanPerformerCode)"
    "
    .. _dcmUPSScheduledHumanPerformerName:
    .. _upsOnHL7-dcmUPSScheduledHumanPerformerName:

    :ref:`Scheduled Human Performer Name <upsOnHL7-dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:
    .. _upsOnHL7-dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <upsOnHL7-dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:
    .. _upsOnHL7-dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <upsOnHL7-dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) in the received HL7 message shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
    "
    .. _dcmUPSIncludeReferencedRequest:
    .. _upsOnHL7-dcmUPSIncludeReferencedRequest:

    :ref:`Include Referenced Request <upsOnHL7-dcmUPSIncludeReferencedRequest>`",boolean,"Indicates if the Study Instance UID (0020,000D) in the received HL7 message and the specified Accession Number (0008,0050), Requested Procedure ID (0040,1001) and Requesting Service (0032,1033) shall be included in the item of the Referenced Request Sequence (0040,A370) in the created UPS. Otherwise an empty Referenced Request Sequence (0040,A370) is included.

    (dcmUPSIncludeReferencedRequest)"
    "
    .. _dcmStudyInstanceUID:
    .. _upsOnHL7-dcmStudyInstanceUID:

    :ref:`Study Instance UID <upsOnHL7-dcmStudyInstanceUID>`",string,"Value of Study Instance UID (0020,000D) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmStudyInstanceUID)"
    "
    .. _dcmAdmissionID:
    .. _upsOnHL7-dcmAdmissionID:

    :ref:`Admission Number <upsOnHL7-dcmAdmissionID>`",string,"Value of Admission ID (0038,0010) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmAdmissionID)"
    "
    .. _dicomIssuerOfAdmissionID:
    .. _upsOnHL7-dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID <upsOnHL7-dicomIssuerOfAdmissionID>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAdmissionID)"
    "
    .. _dcmAccessionNumber:
    .. _upsOnHL7-dcmAccessionNumber:

    :ref:`Accession Number <upsOnHL7-dcmAccessionNumber>`",string,"Value of Accession Number (0008,0050) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmAccessionNumber)"
    "
    .. _dicomIssuerOfAccessionNumber:
    .. _upsOnHL7-dicomIssuerOfAccessionNumber:

    :ref:`Issuer of Accession Number <upsOnHL7-dicomIssuerOfAccessionNumber>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) in Item of Issuer of Accession Number Sequence (0008,0051) in Item of Referenced Request Sequence (0040,A370) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAccessionNumber)"
    "
    .. _dcmRequestedProcedureID:
    .. _upsOnHL7-dcmRequestedProcedureID:

    :ref:`Requested Procedure ID <upsOnHL7-dcmRequestedProcedureID>`",string,"Value of Requested Procedure ID (0040,1001) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmRequestedProcedureID)"
    "
    .. _dcmRequestedProcedureDescription:
    .. _upsOnHL7-dcmRequestedProcedureDescription:

    :ref:`Requested Procedure Description <upsOnHL7-dcmRequestedProcedureDescription>`",string,"Value of Requested Procedure Description (0032,1060) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmRequestedProcedureDescription)"
    "
    .. _dcmRequestingPhysician:
    .. _upsOnHL7-dcmRequestingPhysician:

    :ref:`Requesting Physician <upsOnHL7-dcmRequestingPhysician>`",string,"Value of Requesting Physician (0032,1032) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmRequestingPhysician)"
    "
    .. _dcmRequestingService:
    .. _upsOnHL7-dcmRequestingService:

    :ref:`Requesting Service <upsOnHL7-dcmRequestingService>`",string,"Value of Requesting Service (0032,1033) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message. Examples: MSH-9 or ORC-1[.1] or ORC-10[.2[.1]]

    (dcmRequestingService)"
    "
    .. _dcmURI:
    .. _upsOnHL7-dcmURI:

    :ref:`XSL Stylesheet URI <upsOnHL7-dcmURI>`",string,"Specifies URI of the XSL style sheet to to transcode received HL7 message to include attributes in created UPS.

    (dcmURI)"
