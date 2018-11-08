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

    :ref:`Prefetch C-Store SCP <dcmPrefetchCStoreSCP>`",string,"AE Title of C-STORE SCP to which selected Studies are retrieved.

    (dcmPrefetchCStoreSCP)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Example: MSH-9=ORM\^O01

    (dcmProperty)"
    "
    .. _dcmEntitySelector:

    :ref:`Entity Selector(s) <dcmEntitySelector>`",string,"Specifies matching keys used to select Studies to prefetch. Format: {key}={value}[&{key}={value)]..., with {key} = 'StudyAge' | {attributeID}. {value} in the format '$'{SEG}-{Seq#}[.{Comp#}[.{SubComp#}]] are replaced by the value of the specified HL7 field from the received HL7 message which triggered the prefetch. If no Entity Selector is specified, all Studies for the Patient will be pre-fetched. Example: 'StudyInstanceUID=$ZDS-1.1' => select the Study with the Study Instance UID from ZDS-1.1.

    (dcmEntitySelector)"
    "
    .. _dcmDuration:

    :ref:`Suppress Duplicate Retrieve Interval <dcmDuration>`",string,"Suppress Retrieve of Studies already retrieved not earlier than the specified interval to avoid duplicate retrieves.

    (dcmDuration)"
