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

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Example: MSH-4=FORWARD or MSH-9=ORM\^O01 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmEntitySelector:

    :ref:`Entity Selector(s) <dcmEntitySelector>`",string,"Specifies matching keys used to select Studies to export. Format: {key}={value}[&{key}={value)]..., with {key} = 'StudyAge' | {attributeID}. {value} in the format '$'{SEG}-{Seq#}[.{Comp#}[.{SubComp#}]] are replaced by the value of the specified HL7 field from the received HL7 message which triggered the export. If no Entity Selector is specified, all Studies for the Patient will be exported. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=CT' => select at most 2 prior Studies not older than 5 years containing at least one CT Series.

    (dcmEntitySelector)"
    "
    .. _dcmNullifyIssuerOfPatientID:

    :ref:`Ignore Assigning Authority of Patient ID <dcmNullifyIssuerOfPatientID>`",string,"Conditionally ignore Assigning Authority of Patient ID (PID-3.4) in received HL7 message which triggered the export for selecting Studies of the Patient. Enumerated values: ALWAYS, MATCHING or NOT_MATCHING.

    (dcmNullifyIssuerOfPatientID)"
    "
    .. _dcmIssuerOfPatientID:

    :ref:`Assigning Authority of Patient ID(s) <dcmIssuerOfPatientID>`",string,"Assigning Authority of Patient ID against values in received HL7 message are matched, if Assigning Authority of Patient ID is set to MATCHING or NOT_MATCHING. Format: <Issuer of Patient ID> [& <Universal Entity ID> & <Universal Entity ID Type>].

    (dcmIssuerOfPatientID)"
    "
    .. _dcmDuration:

    :ref:`Suppress Duplicate Export Interval <dcmDuration>`",string,"Suppress Export of Studies already exported not earlier than the specified interval to avoid duplicate exports.

    (dcmDuration)"
