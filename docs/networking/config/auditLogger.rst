Audit Logger
============
Audit Logger related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Audit Logger Attributes (LDAP Object: dcmAuditLogger)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _auditLogger-cn:

    :ref:`Name <auditLogger-cn>`",string,"Arbitrary/Meaningful name for the Audit Logger object

    (cn)"
    "
    .. _dicomNetworkConnectionReference:
    .. _auditLogger-dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) <auditLogger-dicomNetworkConnectionReference>`",string,"The JSON Pointers to the Network Connection objects used by this Audit Logger

    (dicomNetworkConnectionReference)"
    "
    .. _dcmAuditRecordRepositoryDeviceName:
    .. _auditLogger-dcmAuditRecordRepositoryDeviceName:

    :ref:`Audit Record Repository Device Name <auditLogger-dcmAuditRecordRepositoryDeviceName>`",string,"Device Name of Audit Record Repository to which Audit Messages are sent

    (dcmAuditRecordRepositoryDeviceName)"
    "
    .. _dcmAuditSourceID:
    .. _auditLogger-dcmAuditSourceID:

    :ref:`Source ID <auditLogger-dcmAuditSourceID>`",string,"RFC 3881 Audit Source ID; device name if absent

    (dcmAuditSourceID)"
    "
    .. _dcmAuditEnterpriseSiteID:
    .. _auditLogger-dcmAuditEnterpriseSiteID:

    :ref:`Enterprise Site ID <auditLogger-dcmAuditEnterpriseSiteID>`",string,"RFC 3881 Audit Enterprise Site ID; value 'dicomInstitutionName' is replaced by the institution name of the DICOM device

    (dcmAuditEnterpriseSiteID)"
    "
    .. _dcmAuditSourceTypeCode:
    .. _auditLogger-dcmAuditSourceTypeCode:

    :ref:`Source Type Code(s) <auditLogger-dcmAuditSourceTypeCode>`",string,"RFC 3881 Audit Source Type Code; value 'dicomPrimaryDeviceType' is replaced by the primary type of the DICOM device

    (dcmAuditSourceTypeCode)"
    "
    .. _dcmAuditFacility:
    .. _auditLogger-dcmAuditFacility:

    :ref:`Syslog Facility <auditLogger-dcmAuditFacility>`",string,"RFC 5424 Syslog Facility string value of audit message.

    Enumerated values:

    kern (= kernel messages)

    user (= user-level messages)

    mail (= mail system messages)

    daemon (= system daemons' messages)

    auth (= authorization messages)

    syslog (= messages generated internally by syslogd)

    lpr (= line printer subsystem messages)

    news (= network news subsystem messages)

    uucp (= UUCP subsystem messages)

    cron (= clock daemon messages)

    authpriv (= security/authorization messages)

    ftp (= ftp daemon messages)

    ntp (= NTP subsystem messages)

    audit (= audit messages)

    console (= console messages)

    cron2 (= clock daemon messages)

    local0

    local1

    local2

    local3

    local4

    local5

    local6

    local7

    (dcmAuditFacility)"
    "
    .. _dcmAuditSuccessSeverity:
    .. _auditLogger-dcmAuditSuccessSeverity:

    :ref:`Syslog Severity - Success <auditLogger-dcmAuditSuccessSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 0 (Success).

    Enumerated values:

    emerg (= emergency; system is unusable)

    alert (= action must be taken immediately)

    crit (= critical condition)

    err (= error condition)

    warning (= warning condition)

    notice (= normal but significant condition)

    info (= informational message)

    debug (= debug-level messages)

    (dcmAuditSuccessSeverity)"
    "
    .. _dcmAuditMinorFailureSeverity:
    .. _auditLogger-dcmAuditMinorFailureSeverity:

    :ref:`Syslog Severity - Failure <auditLogger-dcmAuditMinorFailureSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 4 (Minor failure).

    Enumerated values:

    emerg (= emergency; system is unusable)

    alert (= action must be taken immediately)

    crit (= critical condition)

    err (= error condition)

    warning (= warning condition)

    notice (= normal but significant condition)

    info (= informational message)

    debug (= debug-level messages)

    (dcmAuditMinorFailureSeverity)"
    "
    .. _dcmAuditSeriousFailureSeverity:
    .. _auditLogger-dcmAuditSeriousFailureSeverity:

    :ref:`Syslog Severity - Failure <auditLogger-dcmAuditSeriousFailureSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 8 (Serious failure).

    Enumerated values:

    emerg (= emergency; system is unusable)

    alert (= action must be taken immediately)

    crit (= critical condition)

    err (= error condition)

    warning (= warning condition)

    notice (= normal but significant condition)

    info (= informational message)

    debug (= debug-level messages)

    (dcmAuditSeriousFailureSeverity)"
    "
    .. _dcmAuditMajorFailureSeverity:
    .. _auditLogger-dcmAuditMajorFailureSeverity:

    :ref:`Syslog Severity - Major <auditLogger-dcmAuditMajorFailureSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 12 (Major failure).

    Enumerated values:

    emerg (= emergency; system is unusable)

    alert (= action must be taken immediately)

    crit (= critical condition)

    err (= error condition)

    warning (= warning condition)

    notice (= normal but significant condition)

    info (= informational message)

    debug (= debug-level messages)

    (dcmAuditMajorFailureSeverity)"
    "
    .. _dcmAuditApplicationName:
    .. _auditLogger-dcmAuditApplicationName:

    :ref:`Syslog Application Name <auditLogger-dcmAuditApplicationName>`",string,"RFC 5424 Syslog APP-NAME of audit message; Audit Source ID if absent

    (dcmAuditApplicationName)"
    "
    .. _dcmAuditMessageID:
    .. _auditLogger-dcmAuditMessageID:

    :ref:`Syslog Message ID <auditLogger-dcmAuditMessageID>`",string,"RFC 5424 Syslog MSGID of audit message.

    (dcmAuditMessageID)"
    "
    .. _dcmAuditMessageEncoding:
    .. _auditLogger-dcmAuditMessageEncoding:

    :ref:`Message Encoding <auditLogger-dcmAuditMessageEncoding>`",string,"Character encoding of RFC 5424 Syslog MSG part of audit message.

    (dcmAuditMessageEncoding)"
    "
    .. _dcmAuditMessageBOM:
    .. _auditLogger-dcmAuditMessageBOM:

    :ref:`Message BOM <auditLogger-dcmAuditMessageBOM>`",boolean,"Enable/disable Unicode BOM prefix of RFC 5424 Syslog MSG part of audit message; include BOM if absent

    (dcmAuditMessageBOM)"
    "
    .. _dcmAuditTimestampInUTC:
    .. _auditLogger-dcmAuditTimestampInUTC:

    :ref:`Timestamp in UTC <auditLogger-dcmAuditTimestampInUTC>`",boolean,"Specify if RFC 5424 Syslog TIMESTAMP and the Event Date/Time of the audit message are specified in Coordinated Universal Time. Default indicates it will be in Local Time zone.

    (dcmAuditTimestampInUTC)"
    "
    .. _dcmAuditMessageFormatXML:
    .. _auditLogger-dcmAuditMessageFormatXML:

    :ref:`Message Format XML <auditLogger-dcmAuditMessageFormatXML>`",boolean,"Specify whether or not the XML audit message is formatted with line feeds and indentation.

    (dcmAuditMessageFormatXML)"
    "
    .. _dcmAuditMessageSchemaURI:
    .. _auditLogger-dcmAuditMessageSchemaURI:

    :ref:`Message Schema URI <auditLogger-dcmAuditMessageSchemaURI>`",string,"URI of DICOM Audit Message Schema referenced in audit message

    (dcmAuditMessageSchemaURI)"
    "
    .. _dcmAuditIncludeInstanceUID:
    .. _auditLogger-dcmAuditIncludeInstanceUID:

    :ref:`Include Instance UIDs <auditLogger-dcmAuditIncludeInstanceUID>`",boolean,"Indicates if Audit Log Message should contain optional Instance UIDs

    (dcmAuditIncludeInstanceUID)"
    "
    .. _dcmAuditLoggerSpoolDirectoryURI:
    .. _auditLogger-dcmAuditLoggerSpoolDirectoryURI:

    :ref:`Spool Directory URI <auditLogger-dcmAuditLoggerSpoolDirectoryURI>`",string,"URI of spool directory used to store messages which could not delivered to the record repository; use system temporary directory if absent.

    (dcmAuditLoggerSpoolDirectoryURI)"
    "
    .. _dcmAuditLoggerRetryInterval:
    .. _auditLogger-dcmAuditLoggerRetryInterval:

    :ref:`Retry Interval <auditLogger-dcmAuditLoggerRetryInterval>`",integer,"Retry interval in s to re-sent messages which could not delivered to the record repository; do no retry to re-sent messages if absent

    (dcmAuditLoggerRetryInterval)"
    "
    .. _dicomInstalled:
    .. _auditLogger-dicomInstalled:

    :ref:`installed <auditLogger-dicomInstalled>`",boolean,"True if the Audit Logger is installed on network. If not present, information about the installed status of the Audit Logger is inherited from the device

    (dicomInstalled)"
    ":doc:`auditSuppressCriteria` (s)",object,"Audit Suppress Criteria"

.. toctree::

    auditSuppressCriteria
