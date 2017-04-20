Audit Logger
============
Audit Logger related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Audit Logger Attributes (LDAP Object: dcmAuditLogger)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Name**",string,"Arbitrary/Meaningful name for the Network Connection object","
    .. _cn:

    cn_"
    "**Network Connection Reference(s)**",string,"The JSON Pointers to the Network Connection objects used by this Audit Logger","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "Audit Record Repository Device Name",string,"Device Name of Audit Record Repository to which Audit Messages are sent","
    .. _dcmAuditRecordRepositoryDeviceName:

    dcmAuditRecordRepositoryDeviceName_"
    "Source ID",string,"RFC 3881 Audit Source ID; device name if absent","
    .. _dcmAuditSourceID:

    dcmAuditSourceID_"
    "Enterprise Site ID",string,"RFC 3881 Audit Enterprise Site ID; value 'dicomInstitutionName' is replaced by the institution name of the DICOM device","
    .. _dcmAuditEnterpriseSiteID:

    dcmAuditEnterpriseSiteID_"
    "Source Type Code(s)",string,"RFC 3881 Audit Source Type Code; value 'dicomPrimaryDeviceType' is replaced by the primary type of the DICOM device","
    .. _dcmAuditSourceTypeCode:

    dcmAuditSourceTypeCode_"
    "Syslog Facility",string,"RFC 5424 Syslog Facility string value of audit message; 'authpriv' if absent","
    .. _dcmAuditFacility:

    dcmAuditFacility_"
    "Syslog Severity - Success",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 0 (Success); 'notice' if absent","
    .. _dcmAuditSuccessSeverity:

    dcmAuditSuccessSeverity_"
    "Syslog Severity - Failure",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 4 (Minor failure); 'warning' if absent","
    .. _dcmAuditMinorFailureSeverity:

    dcmAuditMinorFailureSeverity_"
    "Syslog Severity - Failure",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 8 (Serious failure); 'err' if absent","
    .. _dcmAuditSeriousFailureSeverity:

    dcmAuditSeriousFailureSeverity_"
    "Syslog Severity - Major",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 12 (Major failure); 'crit' if absent","
    .. _dcmAuditMajorFailureSeverity:

    dcmAuditMajorFailureSeverity_"
    "Syslog Application Name",string,"RFC 5424 Syslog APP-NAME of audit message; Audit Source ID if absent","
    .. _dcmAuditApplicationName:

    dcmAuditApplicationName_"
    "Syslog Message ID",string,"RFC 5424 Syslog MSGID of audit message; DICOM+RFC3881 if absent","
    .. _dcmAuditMessageID:

    dcmAuditMessageID_"
    "Message Encoding",string,"Character encoding of RFC 5424 Syslog MSG part of audit message; UTF-8 if absent","
    .. _dcmAuditMessageEncoding:

    dcmAuditMessageEncoding_"
    "Message BOM",boolean,"Enable/disable Unicode BOM prefix of RFC 5424 Syslog MSG part of audit message; include BOM if absent","
    .. _dcmAuditMessageBOM:

    dcmAuditMessageBOM_"
    "Timestamp in UTC",boolean,"Specify if RFC 5424 Syslog TIMESTAMP and the Event Date/Time of the audit message are specified in Coordinated Universal Time or in Local Time; use Local Time zone if absent","
    .. _dcmAuditTimestampInUTC:

    dcmAuditTimestampInUTC_"
    "Message Format XML",boolean,"Specify whether or not the XML audit message is formatted with linefeeds and indentation; disabled if absent","
    .. _dcmAuditMessageFormatXML:

    dcmAuditMessageFormatXML_"
    "Message Schema URI",string,"URI of DICOM Audit Message Schema referenced in audit message","
    .. _dcmAuditMessageSchemaURI:

    dcmAuditMessageSchemaURI_"
    "Include Instance UIDs",boolean,"Indicates if Audit Log Message should contain optional Instance UIDs","
    .. _dcmAuditIncludeInstanceUID:

    dcmAuditIncludeInstanceUID_"
    "Spool Directory URI",string,"URI of spool directory used to store messages which could not delivered to the record repository; use system temporary directory if absent","
    .. _dcmAuditLoggerSpoolDirectoryURI:

    dcmAuditLoggerSpoolDirectoryURI_"
    "Retry Interval",string,"Retry interval in s to re-sent messages which could not delivered to the record repository; do no retry to re-sent messages if absent","
    .. _dcmAuditLoggerRetryInterval:

    dcmAuditLoggerRetryInterval_"
    "installed",boolean,"True if the Audit Logger is installed on network. If not present, information about the installed status of the Audit Logger is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
    ":doc:`auditSuppressCriteria` (s)",object,"Audit Suppress Criteria","
    .. _dcmAuditSuppressCriteria:

    dcmAuditSuppressCriteria_"

.. toctree::

    auditSuppressCriteria
