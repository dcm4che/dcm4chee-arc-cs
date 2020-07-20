UPS Template
============
UPS Template

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS Template Attributes (LDAP Object: dcmUpsTemplate)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmUPSTemplateID:

    :ref:`UPS Template ID <dcmUPSTemplateID>`",string,"ID of UPS Template

    (dcmUPSTemplateID)"
    "
    .. _dcmUPSLabel:

    :ref:`Procedure Step Label <dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) in created UPS.

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) in created UPS.

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
    .. _dcmDestinationAE:

    :ref:`Destination AE <dcmDestinationAE>`",string,"Value of Destination AE (2100,0140) in created UPS.

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

    :ref:`Scheduled Human Performer Name <dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS.

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS.

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
