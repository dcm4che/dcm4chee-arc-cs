HL7 Export Rule
===============
HL7 Export Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Export Rule Attributes (LDAP Object: hl7ExportRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the HL7 Export Rule

    (cn)"
    "
    .. _dcmExporterID:

    :ref:`Exporter ID(s) <dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Example: MSH-9=ORM\^O01

    (dcmProperty)"
    "
    .. _dcmEntitySelector:

    :ref:`Entity Selector(s) <dcmEntitySelector>`",string,"Specifies matching keys used to select Studies to export. Format: {key}={value}[&{key}={value)]..., with {key} = 'StudyAge' | {attributeID}. {value} in the format '$'{SEG}-{Seq#}[.{Comp#}[.{SubComp#}]] are replaced by the value of the specified HL7 field from the received HL7 message which triggered the export. If no Entity Selector is specified, all Studies for the Patient will be exported. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=CT' => select at most 2 prior Studies not older than 5 years containing at least one CT Series.

    (dcmEntitySelector)"
    "
    .. _dcmDuration:

    :ref:`Suppress Duplicate Export Interval <dcmDuration>`",string,"Suppress Export of Studies already exported not earlier than the specified interval to avoid duplicate exports.

    (dcmDuration)"
