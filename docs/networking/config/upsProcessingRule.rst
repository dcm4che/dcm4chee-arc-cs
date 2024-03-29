UPS Processing Rule
===================
Process matching Workitems in unified Worklist

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS Processing Rule Attributes (LDAP Object: dcmUpsProcessingRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmUPSProcessingRuleID:

    :ref:`UPS Processing Rule ID <dcmUPSProcessingRuleID>`",string,"ID of UPS Processing Rule

    (dcmUPSProcessingRuleID)"
    "
    .. _dicomAETitle:

    :ref:`Application Entity (AE) title <dicomAETitle>`",string,"Application Entity (AE) title

    (dicomAETitle)"
    "
    .. _dcmURI:

    :ref:`UPS Processor URI <dcmURI>`",string,"Identifies UPS Processor for processing matching Workitems

    (dcmURI)"
    "
    .. _dcmProperty:

    :ref:`Processing Property(s) <dcmProperty>`",string,"UPS Processor dependent property in format <name>=<value>

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Processing Schedule(s) <dcmSchedule>`",string,"Delay processing to specified time periods. If no Processing Schedule is specified, process Workitems at their Scheduled Procedure Step Start Date Time (0040,4005). Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
    "
    .. _dcmMaxThreads:

    :ref:`Maximum Number of Threads <dcmMaxThreads>`",integer,"Maximal number of threads used for processing of matching Workitems.

    (dcmMaxThreads)"
    "
    .. _dcmUPSInputReadinessState:

    :ref:`Input Readiness State <dcmUPSInputReadinessState>`",string,"Process Workitems with matching Input Readiness State (0040,4041).

    Enumerated values:

    INCOMPLETE

    UNAVAILABLE

    READY

    (dcmUPSInputReadinessState)"
    "
    .. _dcmUPSPriority:

    :ref:`Priority <dcmUPSPriority>`",string,"Process Workitems with matching Scheduled Procedure Step Priority (0074,1200). If absent, process Workitems of any priority, but order the processing according their priority.

    Enumerated values:

    HIGH

    MEDIUM

    LOW

    (dcmUPSPriority)"
    "
    .. _dcmUPSLabel:

    :ref:`Procedure Step Label <dcmUPSLabel>`",string,"Process Workitems with matching Procedure Step Label (0074,1204). If absent, process Workitems with any Procedure Step Label.

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`Worklist Label <dcmUPSWorklistLabel>`",string,"Process Workitems with matching Worklist Label (0074,1202). If absent, process Workitems with any Worklist Label.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <dcmUPSScheduledWorkitemCode>`",string,"Process Workitems with matching Code in Scheduled Workitem Code Sequence (0040,4018) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Workitem Code.

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code <dcmUPSScheduledStationNameCode>`",string,"Process Workitems with matching Code in Scheduled Station Name Code Sequence (0040,4025) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Station Name Code.

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code <dcmUPSScheduledStationClassCode>`",string,"Process Workitems with matching Code in Scheduled Station Name Class Sequence (0040,4026) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Station Class Code.

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code <dcmUPSScheduledStationLocationCode>`",string,"Process Workitems with matching Code in Scheduled Station Geographic Location Class Sequence (0040,4027) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Station Geographic Location Code.

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSPerformedWorkitemCode:

    :ref:`Performed Workitem Code <dcmUPSPerformedWorkitemCode>`",string,"Item of Performed Workitem Code Sequence (0040,4019) in processed UPS in format (CV, CSD, ""CM"").

    (dcmUPSPerformedWorkitemCode)"
    "
    .. _dcmUPSPerformedStationNameCode:

    :ref:`Performed Station Name Code <dcmUPSPerformedStationNameCode>`",string,"Item of Performed Station Name Code Sequence (0040,4028) in processed UPS in format (CV, CSD, ""CM"").

    (dcmUPSPerformedStationNameCode)"
    "
    .. _dcmUPSIgnoreDiscontinuationReasonCode:

    :ref:`Ignore Discontinuation Reason Code(s) <dcmUPSIgnoreDiscontinuationReasonCode>`",string,"Specifies Discontinuation Reason Code in format (CV, CSD, ""CM"") to ignore and change UPS State to COMPLETED - instead of CANCELED.

    (dcmUPSIgnoreDiscontinuationReasonCode)"
    "
    .. _dcmUPSRescheduleDiscontinuationReasonCode:

    :ref:`Reschedule Discontinuation Reason Code(s) <dcmUPSRescheduleDiscontinuationReasonCode>`",string,"Specifies Discontinuation Reason Code in format (CV, CSD, ""CM"") to reschedule the canceled UPS. If absent, UPS canceled with any Discontinuation Reason Code will be rescheduled according specified Maximum Number of Rescheduling.

    (dcmUPSRescheduleDiscontinuationReasonCode)"
    "
    .. _dcmUPSTemplateID:

    :ref:`Create UPS on Cancel <dcmUPSTemplateID>`",string,"Specifies UPS Template Workitem Instance UID for creating an UPS if the processing failed and retry is not scheduled any more. If absent, no UPS will be created on failures.

    (dcmUPSTemplateID)"
    "
    .. _dcmMaxRetries:

    :ref:`Maximum Number of Rescheduling <dcmMaxRetries>`",integer,"Maximal number a Workitem which processing failed is rescheduled.

    (dcmMaxRetries)"
    "
    .. _dcmRetryDelay:

    :ref:`Reschedule Delay <dcmRetryDelay>`",string,"Delay to reschedule a Workitem which processing failed in ISO-8601 duration format PnDTnHnMn.nS.

    (dcmRetryDelay)"
    "
    .. _dcmMaxRetryDelay:

    :ref:`Maximum Reschedule Delay <dcmMaxRetryDelay>`",string,"Maximal Delay to reschedule a Workitem which processing failed in ISO-8601 duration format PnDTnHnMn.nS. Infinite if absent.

    (dcmMaxRetryDelay)"
    "
    .. _dcmRetryDelayMultiplier:

    :ref:`Reschedule Delay Multiplier <dcmRetryDelayMultiplier>`",integer,"Multiplier in % that will take effect on top of Reschedule Delay with Maximum Reschedule Delay to be taken into account.

    (dcmRetryDelayMultiplier)"
