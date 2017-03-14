Archive HL7 Application
=======================
DICOM Archive HL7 Application related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive HL7 Application Attributes (LDAP Object: dcmArchiveHL7Application)
    :header: Name, Type, Description, LDAP Attribute
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
    "HL7 Schedule Protocol Code in Order",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. Enumerated values: OBR_4_1, OBR_4_4. If absent, OBR_4_4 will be applied.","
    .. _hl7ScheduledProtocolCodeInOrder:

    hl7ScheduledProtocolCodeInOrder_"
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
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed","
    .. _hl7OrderScheduledStation:

    hl7OrderScheduledStation_"
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages","
    .. _hl7OrderSPSStatus:

    hl7OrderSPSStatus_"

.. toctree::

    hl7ForwardRule
    hl7OrderScheduledStation
    hl7OrderSPSStatus
