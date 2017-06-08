Archive HL7 Application
=======================
DICOM Archive HL7 Application related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive HL7 Application Attributes (LDAP Object: dcmArchiveHL7Application)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "AE Title",string,"Archive AE Title associated with this HL7 Application.","
    .. _dicomAETitle:

    dicomAETitle_"
    "HL7 Patient Update Template URI",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service. Overwrites value specified on Device level.","
    .. _hl7PatientUpdateTemplateURI:

    hl7PatientUpdateTemplateURI_"
    "HL7 Import Report Template URI",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR. Overwrites value specified on Device level.","
    .. _hl7ImportReportTemplateURI:

    hl7ImportReportTemplateURI_"
    "HL7 Schedule Procedure Template URI",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items. Overwrites value specified on Device level.","
    .. _hl7ScheduleProcedureTemplateURI:

    hl7ScheduleProcedureTemplateURI_"
    "HL7 Schedule Protocol Code in Order",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. Overwrites value specified on Device level. Enumerated values: OBR_4_1 or OBR_4_4","
    .. _hl7ScheduledProtocolCodeInOrder:

    hl7ScheduledProtocolCodeInOrder_"
    "HL7 Schedule Station AET in Order",string,"Specifies location of Scheduled Station AE Title in received HL7 Order message. Not effective for HL7 v2.5.1 OMI^O23 with IPC segment. Overwrites value specified on Device level. Enumerated values: ORC_18","
    .. _hl7ScheduledStationAETInOrder:

    hl7ScheduledStationAETInOrder_"
    "HL7 Log File Pattern",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging. Overwrites value specified on Device level.","
    .. _hl7LogFilePattern:

    hl7LogFilePattern_"
    "HL7 Error Log File Pattern",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging. Overwrites value specified on Device level.","
    .. _hl7ErrorLogFilePattern:

    hl7ErrorLogFilePattern_"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rule. Supplements values specified on Device level.","
    .. _hl7ForwardRule:

    hl7ForwardRule_"
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed. Supplements values specified on Device level.","
    .. _hl7OrderScheduledStation:

    hl7OrderScheduledStation_"
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages. Overwrites values specified on Device level.","
    .. _hl7OrderSPSStatus:

    hl7OrderSPSStatus_"
