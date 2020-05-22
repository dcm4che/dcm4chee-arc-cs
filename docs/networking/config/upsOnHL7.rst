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

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format <SEG>-<Seq#>[.<Comp#>[.<SubComp#>]][!]=<regEx>. Example: MSH-9=ORM\^O01

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
    .. _dcmRequestingService:

    :ref:`Requesting Service <dcmRequestingService>`",string,"Value of Requesting Service (0032,1033) in Item of Referenced Request Sequence (0040,A370) in created UPS. {<SEG>-<Seq#>[.<Comp#>[.<SubComp#>]]} will be replaced by the value of that field in the received HL7 message.

    (dcmRequestingService)"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI <dcmURI>`",string,"Specifies URI of the XSL style sheet to to transcode received HL7 message to include attributes in created UPS.

    (dcmURI)"
