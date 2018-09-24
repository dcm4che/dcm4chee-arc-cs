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
    .. _dcmExporterID:

    :ref:`Exporter ID(s) <dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmEntitySelector:

    :ref:`Entity Selector(s) <dcmEntitySelector>`",string,"Specifies matching keys used to select entities to prefetch. Format: {key}={value}][&{key}={value}]..., with {key} = 'priors' | 'StudyAge' | {attributeID}. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=CT' => select at most 2 prior Studies not older than 5 years containing at least one CT Series.

    (dcmEntitySelector)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Examples: MSH-4=FORWARD or MSH-9=ADT\^A28\^ADT_A05

    (dcmProperty)"
    "
    .. _dcmDuration:

    :ref:`Suppress Duplicate Export Interval <dcmDuration>`",string,"Suppress Export of entities already exported not earlier than the specified interval to avoid duplicate exports.

    (dcmDuration)"
