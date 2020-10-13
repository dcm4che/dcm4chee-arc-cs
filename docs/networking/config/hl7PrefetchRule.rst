HL7 Prefetch Rule
=================
HL7 Prefetch Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Prefetch Rule Attributes (LDAP Object: hl7PrefetchRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Prefetch Rule

    (cn)"
    "
    .. _dcmQueueName:

    :ref:`Queue Name <dcmQueueName>`",string,"Name of JMS Queue used for scheduling retrieve tasks triggered by this Prefetch Rule Enumerated values: Retrieve1, Retrieve2, Retrieve3, Retrieve4, Retrieve5, Retrieve6, Retrieve7, Retrieve8, Retrieve9, Retrieve10, Retrieve11, Retrieve12 or Retrieve13.

    (dcmQueueName)"
    "
    .. _dicomAETitle:

    :ref:`Archive AE title <dicomAETitle>`",string,"AE Title of Archive Application Entity used for retrieving selected Studies from Prefetch C-Move SCP.

    (dicomAETitle)"
    "
    .. _dcmPrefetchCFindSCP:

    :ref:`Prefetch C-Find SCP <dcmPrefetchCFindSCP>`",string,"AE Title of C-FIND SCP which is queried for Studies matching the specified Entity Selector.

    (dcmPrefetchCFindSCP)"
    "
    .. _dcmPrefetchCMoveSCP:

    :ref:`Prefetch C-Move SCP <dcmPrefetchCMoveSCP>`",string,"AE Title of C-MOVE SCP from which selected Studies are retrieved.

    (dcmPrefetchCMoveSCP)"
    "
    .. _dcmPrefetchCStoreSCP:

    :ref:`Prefetch C-Store SCP(s) <dcmPrefetchCStoreSCP>`",string,"AE Title of C-STORE SCP to which selected Studies are retrieved.

    (dcmPrefetchCStoreSCP)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Example: MSH-4=FORWARD or MSH-9=ORM\^O01 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmEntitySelector:

    :ref:`Entity Selector(s) <dcmEntitySelector>`",string,"Specifies matching keys used to select Studies to prefetch. Format: {key}={value}[&{key}={value)]..., with {key} = 'priors' | 'StudyAge' | {attributeID}. {value} in the format '$'{SEG}-{Seq#}[.{Comp#}[.{SubComp#}]] are replaced by the value of the specified HL7 field from the received HL7 message which triggered the prefetch. If no Entity Selector is specified, all Studies for the Patient will be pre-fetched. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=$OBR-24' => select at most 2 prior Studies not older than 5 years containing at least one Series with Modality from OBR-24.

    (dcmEntitySelector)"
    "
    .. _dcmNullifyIssuerOfPatientID:

    :ref:`Ignore Assigning Authority of Patient ID <dcmNullifyIssuerOfPatientID>`",string,"Conditionally ignore Assigning Authority of Patient ID (PID-3.4) in received HL7 message which triggered the prefetch for selecting Studies of the Patient. Enumerated values: ALWAYS, MATCHING or NOT_MATCHING.

    (dcmNullifyIssuerOfPatientID)"
    "
    .. _dcmIssuerOfPatientID:

    :ref:`Assigning Authority of Patient ID(s) <dcmIssuerOfPatientID>`",string,"Assigning Authority of Patient ID against values in received HL7 message are matched, if Assigning Authority of Patient ID is set to MATCHING or NOT_MATCHING. Format: <Issuer of Patient ID> [& <Universal Entity ID> & <Universal Entity ID Type>].

    (dcmIssuerOfPatientID)"
    "
    .. _dcmDuration:

    :ref:`Suppress Duplicate Retrieve Interval <dcmDuration>`",string,"Suppress Retrieve of Studies already retrieved not earlier than the specified interval to avoid duplicate retrieves.

    (dcmDuration)"
    "
    .. _dcmSchedule:

    :ref:`Prefetch Schedule(s) <dcmSchedule>`",string,"Delay prefetch to specified time periods. If no Prefetch Schedule is specified, queue a Prefetch Task for the selected Studies of the Patient immediately. Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
