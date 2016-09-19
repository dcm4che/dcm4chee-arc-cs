Archive HL7 Application
=======================
DICOM Archive HL7 Application related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive HL7 Application Attributes (LDAP Object: dcmArchiveHL7Application)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "HL7 Patient Update Template URI",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service.","
    .. _hl7PatientUpdateTemplateURI:

    hl7PatientUpdateTemplateURI_"
    "HL7 Import Report Template URI",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR.","
    .. _hl7ImportReportTemplateURI:

    hl7ImportReportTemplateURI_"
    "HL7 Schedule Procedure Template URI",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items.","
    .. _hl7ScheduleProcedureTemplateURI:

    hl7ScheduleProcedureTemplateURI_"
    "HL7 Log File Pattern",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging.","
    .. _hl7LogFilePattern:

    hl7LogFilePattern_"
    "HL7 Error Log File Pattern",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging.","
    .. _hl7ErrorLogFilePattern:

    hl7ErrorLogFilePattern_"
    "AE Title",string,"Associated AE Title.","
    .. _dicomAETitle:

    dicomAETitle_"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rule","
    .. _hl7ForwardRule:

    hl7ForwardRule_"
