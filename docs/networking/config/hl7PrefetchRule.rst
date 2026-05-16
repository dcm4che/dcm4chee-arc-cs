HL7 Prefetch Rule
=================
HL7 Prefetch Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Prefetch Rule Attributes (LDAP Object: hl7PrefetchRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _hl7PrefetchRule-cn:

    :ref:`Name <hl7PrefetchRule-cn>`",string,"Arbitrary/Meaningful name of the Prefetch Rule

    (cn)"
    "
    .. _dcmQueueName:
    .. _hl7PrefetchRule-dcmQueueName:

    :ref:`Queue Name <hl7PrefetchRule-dcmQueueName>`",string,"Name of Task Queue used for scheduling retrieve tasks triggered by this Prefetch Rule

    (dcmQueueName)"
    "
    .. _dicomAETitle:
    .. _hl7PrefetchRule-dicomAETitle:

    :ref:`Archive AE title <hl7PrefetchRule-dicomAETitle>`",string,"AE Title of Archive Application Entity used for retrieving selected Studies from Prefetch C-Move SCP.

    (dicomAETitle)"
    "
    .. _dcmPrefetchCFindSCP:
    .. _hl7PrefetchRule-dcmPrefetchCFindSCP:

    :ref:`Prefetch C-Find SCP <hl7PrefetchRule-dcmPrefetchCFindSCP>`",string,"AE Title of C-FIND SCP which is queried for Studies matching the specified Entity Selector.

    (dcmPrefetchCFindSCP)"
    "
    .. _dcmPrefetchCMoveSCP:
    .. _hl7PrefetchRule-dcmPrefetchCMoveSCP:

    :ref:`Prefetch C-Move SCP <hl7PrefetchRule-dcmPrefetchCMoveSCP>`",string,"AE Title of C-MOVE SCP from which selected Studies are retrieved.

    (dcmPrefetchCMoveSCP)"
    "
    .. _dcmPrefetchCStoreSCP:
    .. _hl7PrefetchRule-dcmPrefetchCStoreSCP:

    :ref:`Prefetch C-Store SCP(s) <hl7PrefetchRule-dcmPrefetchCStoreSCP>`",string,"AE Title of C-STORE SCP to which selected Studies are retrieved.

    (dcmPrefetchCStoreSCP)"
    "
    .. _dcmDestinationCFindSCP:
    .. _hl7PrefetchRule-dcmDestinationCFindSCP:

    :ref:`Destination C-FIND SCP <hl7PrefetchRule-dcmDestinationCFindSCP>`",string,"Suppress retrieve of selected Studies from Prefetch C-Move SCP which are (already) available at specified Destination C-FIND SCP with equal or more Number of Study Related Instances as returned by Prefetch C-FIND SCP. Retrieve all selected Studies if absent.

    (dcmDestinationCFindSCP)"
    "
    .. _dicomDeviceName:
    .. _hl7PrefetchRule-dicomDeviceName:

    :ref:`Prefetch Device Name <hl7PrefetchRule-dicomDeviceName>`",string,"Specifies Device on which the Retrieve Task(s) shall be scheduled. If not specified, the Retrieve Task(s) is/are scheduled on the Device which received the HL7 messages.

    (dicomDeviceName)"
    "
    .. _dcmProperty:
    .. _hl7PrefetchRule-dcmProperty:

    :ref:`Conditions(s) <hl7PrefetchRule-dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Example: MSH-4=FORWARD or MSH-9=ORM\^O01 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmEntitySelector:
    .. _hl7PrefetchRule-dcmEntitySelector:

    :ref:`Entity Selector(s) <hl7PrefetchRule-dcmEntitySelector>`",string,"Specifies matching keys used to select Studies to prefetch. Format: {key}={value}[&{key}={value)]..., with {key} = 'priors' | 'StudyAge' | {attributeID}. {value} in the format '$'{SEG}-{Seq#}[.{Comp#}[.{SubComp#}]] are replaced by the value of the specified HL7 field from the received HL7 message which triggered the prefetch. If no Entity Selector is specified, all Studies for the Patient will be pre-fetched. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=$OBR-24' => select at most 2 prior Studies not older than 5 years containing at least one Series with Modality from OBR-24.

    (dcmEntitySelector)"
    "
    .. _dcmNullifyIssuerOfPatientID:
    .. _hl7PrefetchRule-dcmNullifyIssuerOfPatientID:

    :ref:`Ignore Assigning Authority of Patient ID <hl7PrefetchRule-dcmNullifyIssuerOfPatientID>`",string,"Conditionally ignore Assigning Authority of Patient ID (PID-3.4) in received HL7 message which triggered the prefetch for selecting Studies of the Patient.

    Enumerated values:

    ALWAYS (= Always ignore Assigning Authority of Patient ID (PID-3.4) for selecting Studies of the Patient)

    MATCHING (= Ignore matching Assigning Authority of Patient ID (PID-3.4) for selecting Studies of the Patient)

    NOT_MATCHING (= Ignore not matching Assigning Authority of Patient ID (PID-3.4) for selecting Studies of the Patient)

    (dcmNullifyIssuerOfPatientID)"
    "
    .. _dcmIssuerOfPatientID:
    .. _hl7PrefetchRule-dcmIssuerOfPatientID:

    :ref:`Assigning Authority of Patient ID(s) <hl7PrefetchRule-dcmIssuerOfPatientID>`",string,"Assigning Authority of Patient ID against values in received HL7 message are matched, if Assigning Authority of Patient ID is set to MATCHING or NOT_MATCHING. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmIssuerOfPatientID)"
    "
    .. _dcmPrefetchForIssuerOfPatientID:
    .. _hl7PrefetchRule-dcmPrefetchForIssuerOfPatientID:

    :ref:`Prefetch for Assigning Authority of Patient ID <hl7PrefetchRule-dcmPrefetchForIssuerOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search qualified patient identifier in list of identifiers in PID-3. Studies matching the specified Entity Selector of this qualified patient identifier shall be queried. If absent, by default the first qualified patient identifier in PID-3 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmPrefetchForIssuerOfPatientID)"
    "
    .. _dcmDuration:
    .. _hl7PrefetchRule-dcmDuration:

    :ref:`Suppress Duplicate Retrieve Interval <hl7PrefetchRule-dcmDuration>`",string,"Suppress Retrieve of Studies already retrieved not earlier than the specified interval to avoid duplicate retrieves.

    (dcmDuration)"
    "
    .. _dcmHistorySize:
    .. _hl7PrefetchRule-dcmHistorySize:

    :ref:`Suppress Duplicate History Size <hl7PrefetchRule-dcmHistorySize>`",integer,"Maximum number of HL7 messages with distinct PID-3 triggering this rule to remember on the history list.

    (dcmHistorySize)"
    "
    .. _dcmPrefetchDateTimeField:
    .. _hl7PrefetchRule-dcmPrefetchDateTimeField:

    :ref:`Prefetch Date Time Field <hl7PrefetchRule-dcmPrefetchDateTimeField>`",string,"Delay retrieve of selected Studies to time from referred HL7 TS field in format {SEG}-{Seq#}[.{Comp#}]. Example: TQ1-7 or SCH-11.4. Schedule retrieve of selected Studies immediate if absent.

    (dcmPrefetchDateTimeField)"
    "
    .. _dcmPrefetchInAdvance:
    .. _hl7PrefetchRule-dcmPrefetchInAdvance:

    :ref:`Prefetch In Advance <hl7PrefetchRule-dcmPrefetchInAdvance>`",string,"Schedule retrieve of selected Studies in advance to the time from configured dcmPrefetchDateTimeField with given time span in ISO-8601 duration format PnDTnHnMn.nS. Not effective, if dcmPrefetchDateTimeField is absent.

    (dcmPrefetchInAdvance)"
    "
    .. _dcmSchedule:
    .. _hl7PrefetchRule-dcmSchedule:

    :ref:`Prefetch Schedule(s) <hl7PrefetchRule-dcmSchedule>`",string,"Delay prefetch to specified time periods in addition to configured Prefetch Date Time field. If no Prefetch Schedule is specified, queue a Prefetch Task for the selected Studies of the Patient based on configured Prefetch Date Time field. Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
