UPS Processing Rule
===================
Process matching Workitems in unified Worklist

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS Processing Rule Attributes (LDAP Object: dcmUpsProcessingRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmUPSProcessingRuleID:
    .. _upsProcessingRule-dcmUPSProcessingRuleID:

    :ref:`UPS Processing Rule ID <upsProcessingRule-dcmUPSProcessingRuleID>`",string,"ID of UPS Processing Rule

    (dcmUPSProcessingRuleID)"
    "
    .. _dicomAETitle:
    .. _upsProcessingRule-dicomAETitle:

    :ref:`Application Entity (AE) title <upsProcessingRule-dicomAETitle>`",string,"Application Entity (AE) title

    (dicomAETitle)"
    "
    .. _dcmURI:
    .. _upsProcessingRule-dcmURI:

    :ref:`UPS Processor URI <upsProcessingRule-dcmURI>`",string,"Identifies UPS Processor for processing matching Workitems

    (dcmURI)"
    "
    .. _dcmProperty:
    .. _upsProcessingRule-dcmProperty:

    :ref:`Processing Property(s) <upsProcessingRule-dcmProperty>`",string,"UPS Processor dependent property in format <name>=<value>

    (dcmProperty)"
    "
    .. _dcmSchedule:
    .. _upsProcessingRule-dcmSchedule:

    :ref:`Processing Schedule(s) <upsProcessingRule-dcmSchedule>`",string,"Delay processing to specified time periods. If no Processing Schedule is specified, process Workitems at their Scheduled Procedure Step Start Date Time (0040,4005). Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
    "
    .. _dcmMaxThreads:
    .. _upsProcessingRule-dcmMaxThreads:

    :ref:`Maximum Number of Threads <upsProcessingRule-dcmMaxThreads>`",integer,"Maximal number of threads used for processing of matching Workitems.

    (dcmMaxThreads)"
    "
    .. _dcmUPSInputReadinessState:
    .. _upsProcessingRule-dcmUPSInputReadinessState:

    :ref:`Input Readiness State <upsProcessingRule-dcmUPSInputReadinessState>`",string,"Process Workitems with matching Input Readiness State (0040,4041).

    Enumerated values:

    INCOMPLETE

    UNAVAILABLE

    READY

    (dcmUPSInputReadinessState)"
    "
    .. _dcmUPSPriority:
    .. _upsProcessingRule-dcmUPSPriority:

    :ref:`Priority <upsProcessingRule-dcmUPSPriority>`",string,"Process Workitems with matching Scheduled Procedure Step Priority (0074,1200). If absent, process Workitems of any priority, but order the processing according their priority.

    Enumerated values:

    HIGH

    MEDIUM

    LOW

    (dcmUPSPriority)"
    "
    .. _dcmUPSLabel:
    .. _upsProcessingRule-dcmUPSLabel:

    :ref:`Procedure Step Label <upsProcessingRule-dcmUPSLabel>`",string,"Process Workitems with matching Procedure Step Label (0074,1204). If absent, process Workitems with any Procedure Step Label.

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:
    .. _upsProcessingRule-dcmUPSWorklistLabel:

    :ref:`Worklist Label <upsProcessingRule-dcmUPSWorklistLabel>`",string,"Process Workitems with matching Worklist Label (0074,1202). If absent, process Workitems with any Worklist Label.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSScheduledWorkitemCode:
    .. _upsProcessingRule-dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <upsProcessingRule-dcmUPSScheduledWorkitemCode>`",string,"Process Workitems with matching Code in Scheduled Workitem Code Sequence (0040,4018) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Workitem Code.

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:
    .. _upsProcessingRule-dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code <upsProcessingRule-dcmUPSScheduledStationNameCode>`",string,"Process Workitems with matching Code in Scheduled Station Name Code Sequence (0040,4025) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Station Name Code.

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:
    .. _upsProcessingRule-dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code <upsProcessingRule-dcmUPSScheduledStationClassCode>`",string,"Process Workitems with matching Code in Scheduled Station Name Class Sequence (0040,4026) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Station Class Code.

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:
    .. _upsProcessingRule-dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code <upsProcessingRule-dcmUPSScheduledStationLocationCode>`",string,"Process Workitems with matching Code in Scheduled Station Geographic Location Class Sequence (0040,4027) in format (CV, CSD, ""CM""). If absent, process Workitems with any Scheduled Station Geographic Location Code.

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSPerformedWorkitemCode:
    .. _upsProcessingRule-dcmUPSPerformedWorkitemCode:

    :ref:`Performed Workitem Code <upsProcessingRule-dcmUPSPerformedWorkitemCode>`",string,"Item of Performed Workitem Code Sequence (0040,4019) in processed UPS in format (CV, CSD, ""CM"").

    (dcmUPSPerformedWorkitemCode)"
    "
    .. _dcmUPSPerformedStationNameCode:
    .. _upsProcessingRule-dcmUPSPerformedStationNameCode:

    :ref:`Performed Station Name Code <upsProcessingRule-dcmUPSPerformedStationNameCode>`",string,"Item of Performed Station Name Code Sequence (0040,4028) in processed UPS in format (CV, CSD, ""CM"").

    (dcmUPSPerformedStationNameCode)"
    "
    .. _dcmUPSIgnoreDiscontinuationReasonCode:
    .. _upsProcessingRule-dcmUPSIgnoreDiscontinuationReasonCode:

    :ref:`Ignore Discontinuation Reason Code(s) <upsProcessingRule-dcmUPSIgnoreDiscontinuationReasonCode>`",string,"Specifies Discontinuation Reason Code in format (CV, CSD, ""CM"") to ignore and change UPS State to COMPLETED - instead of CANCELED.

    (dcmUPSIgnoreDiscontinuationReasonCode)"
    "
    .. _dcmUPSRescheduleDiscontinuationReasonCode:
    .. _upsProcessingRule-dcmUPSRescheduleDiscontinuationReasonCode:

    :ref:`Reschedule Discontinuation Reason Code(s) <upsProcessingRule-dcmUPSRescheduleDiscontinuationReasonCode>`",string,"Specifies Discontinuation Reason Code in format (CV, CSD, ""CM"") to reschedule the canceled UPS. If absent, UPS canceled with any Discontinuation Reason Code will be rescheduled according specified Maximum Number of Rescheduling.

    (dcmUPSRescheduleDiscontinuationReasonCode)"
    "
    .. _dcmUPSTemplateID:
    .. _upsProcessingRule-dcmUPSTemplateID:

    :ref:`Create UPS on Cancel <upsProcessingRule-dcmUPSTemplateID>`",string,"Specifies UPS Template Workitem Instance UID for creating an UPS if the processing failed and retry is not scheduled any more. If absent, no UPS will be created on failures.

    (dcmUPSTemplateID)"
    "
    .. _dcmMaxRetries:
    .. _upsProcessingRule-dcmMaxRetries:

    :ref:`Maximum Number of Rescheduling <upsProcessingRule-dcmMaxRetries>`",integer,"Maximal number a Workitem which processing failed is rescheduled.

    (dcmMaxRetries)"
    "
    .. _dcmRetryDelay:
    .. _upsProcessingRule-dcmRetryDelay:

    :ref:`Reschedule Delay <upsProcessingRule-dcmRetryDelay>`",string,"Delay to reschedule a Workitem which processing failed in ISO-8601 duration format PnDTnHnMn.nS.

    (dcmRetryDelay)"
    "
    .. _dcmMaxRetryDelay:
    .. _upsProcessingRule-dcmMaxRetryDelay:

    :ref:`Maximum Reschedule Delay <upsProcessingRule-dcmMaxRetryDelay>`",string,"Maximal Delay to reschedule a Workitem which processing failed in ISO-8601 duration format PnDTnHnMn.nS. Infinite if absent.

    (dcmMaxRetryDelay)"
    "
    .. _dcmRetryDelayMultiplier:
    .. _upsProcessingRule-dcmRetryDelayMultiplier:

    :ref:`Reschedule Delay Multiplier <upsProcessingRule-dcmRetryDelayMultiplier>`",integer,"Multiplier in % that will take effect on top of Reschedule Delay with Maximum Reschedule Delay to be taken into account.

    (dcmRetryDelayMultiplier)"
