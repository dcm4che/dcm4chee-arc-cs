HL7 Export Rule
===============
HL7 Export Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Export Rule Attributes (LDAP Object: hl7ExportRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _hl7ExportRule-cn:

    :ref:`Name <hl7ExportRule-cn>`",string,"Arbitrary/Meaningful name of the HL7 Export Rule

    (cn)"
    "
    .. _dcmExporterID:
    .. _hl7ExportRule-dcmExporterID:

    :ref:`Exporter ID(s) <hl7ExportRule-dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmProperty:
    .. _hl7ExportRule-dcmProperty:

    :ref:`Conditions(s) <hl7ExportRule-dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Example: MSH-4=FORWARD or MSH-9=ORM\^O01 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmEntitySelector:
    .. _hl7ExportRule-dcmEntitySelector:

    :ref:`Entity Selector(s) <hl7ExportRule-dcmEntitySelector>`",string,"Specifies matching keys used to select Studies to export. Format: {key}={value}[&{key}={value)]..., with {key} = 'StudyAge' | {attributeID}. {value} in the format '$'{SEG}-{Seq#}[.{Comp#}[.{SubComp#}]] are replaced by the value of the specified HL7 field from the received HL7 message which triggered the export. If no Entity Selector is specified, all Studies for the Patient will be exported. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=CT' => select at most 2 prior Studies not older than 5 years containing at least one CT Series.

    (dcmEntitySelector)"
    "
    .. _dcmNullifyIssuerOfPatientID:
    .. _hl7ExportRule-dcmNullifyIssuerOfPatientID:

    :ref:`Ignore Assigning Authority of Patient ID <hl7ExportRule-dcmNullifyIssuerOfPatientID>`",string,"Conditionally ignore Assigning Authority of Patient ID (PID-3.4) in received HL7 message which triggered the export for selecting Studies of the Patient.

    Enumerated values:

    ALWAYS (= Always ignore Assigning Authority of Patient ID (PID-3.4) for selecting Studies of the Patient)

    MATCHING (= Ignore matching Assigning Authority of Patient ID (PID-3.4) for selecting Studies of the Patient)

    NOT_MATCHING (= Ignore not matching Assigning Authority of Patient ID (PID-3.4) for selecting Studies of the Patient)

    (dcmNullifyIssuerOfPatientID)"
    "
    .. _dcmIssuerOfPatientID:
    .. _hl7ExportRule-dcmIssuerOfPatientID:

    :ref:`Assigning Authority of Patient ID(s) <hl7ExportRule-dcmIssuerOfPatientID>`",string,"Assigning Authority of Patient ID against values in received HL7 message are matched, if Assigning Authority of Patient ID is set to MATCHING or NOT_MATCHING. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmIssuerOfPatientID)"
    "
    .. _dcmPrefetchForIssuerOfPatientID:
    .. _hl7ExportRule-dcmPrefetchForIssuerOfPatientID:

    :ref:`Export for Assigning Authority of Patient ID <hl7ExportRule-dcmPrefetchForIssuerOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search qualified patient identifier in list of identifiers in PID-3. Studies matching the specified Entity Selector of this qualified patient identifier shall be queried. If absent, by default the first qualified patient identifier in PID-3 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmPrefetchForIssuerOfPatientID)"
    "
    .. _dcmDuration:
    .. _hl7ExportRule-dcmDuration:

    :ref:`Suppress Duplicate Export Interval <hl7ExportRule-dcmDuration>`",string,"Suppress Export of Studies already exported not earlier than the specified interval to avoid duplicate exports.

    (dcmDuration)"
    "
    .. _dcmHistorySize:
    .. _hl7ExportRule-dcmHistorySize:

    :ref:`Suppress Duplicate History Size <hl7ExportRule-dcmHistorySize>`",integer,"Maximum number of HL7 messages with distinct PID-3 triggering this rule to remember on the history list.

    (dcmHistorySize)"
