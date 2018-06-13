Audit Logger
============
Audit Logger related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Audit Logger Attributes (LDAP Object: dcmAuditLogger)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name for the Audit Logger object

    (cn)"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) <dicomNetworkConnectionReference>`",string,"The JSON Pointers to the Network Connection objects used by this Audit Logger

    (dicomNetworkConnectionReference)"
    "
    .. _dcmAuditRecordRepositoryDeviceName:

    :ref:`Audit Record Repository Device Name <dcmAuditRecordRepositoryDeviceName>`",string,"Device Name of Audit Record Repository to which Audit Messages are sent

    (dcmAuditRecordRepositoryDeviceName)"
    "
    .. _dcmAuditSourceID:

    :ref:`Source ID <dcmAuditSourceID>`",string,"RFC 3881 Audit Source ID; device name if absent

    (dcmAuditSourceID)"
    "
    .. _dcmAuditEnterpriseSiteID:

    :ref:`Enterprise Site ID <dcmAuditEnterpriseSiteID>`",string,"RFC 3881 Audit Enterprise Site ID; value 'dicomInstitutionName' is replaced by the institution name of the DICOM device

    (dcmAuditEnterpriseSiteID)"
    "
    .. _dcmAuditSourceTypeCode:

    :ref:`Source Type Code(s) <dcmAuditSourceTypeCode>`",string,"RFC 3881 Audit Source Type Code; value 'dicomPrimaryDeviceType' is replaced by the primary type of the DICOM device

    (dcmAuditSourceTypeCode)"
    "
    .. _dcmAuditFacility:

    :ref:`Syslog Facility <dcmAuditFacility>`",string,"RFC 5424 Syslog Facility string value of audit message. Enumerated values: kern, user, mail, daemon, auth, syslog, lpr, news, uucp, cron, authpriv, ftp, ntp, audit, console, cron2, local0, local1, local2, local3, local4, local5, local6 or local7.

    (dcmAuditFacility)"
    "
    .. _dcmAuditSuccessSeverity:

    :ref:`Syslog Severity - Success <dcmAuditSuccessSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 0 (Success). Enumerated values: emerg, alert, crit, err, warning, notice, info or debug.

    (dcmAuditSuccessSeverity)"
    "
    .. _dcmAuditMinorFailureSeverity:

    :ref:`Syslog Severity - Failure <dcmAuditMinorFailureSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 4 (Minor failure). Enumerated values: emerg, alert, crit, err, warning, notice, info or debug.

    (dcmAuditMinorFailureSeverity)"
    "
    .. _dcmAuditSeriousFailureSeverity:

    :ref:`Syslog Severity - Failure <dcmAuditSeriousFailureSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 8 (Serious failure). Enumerated values: emerg, alert, crit, err, warning, notice, info or debug.

    (dcmAuditSeriousFailureSeverity)"
    "
    .. _dcmAuditMajorFailureSeverity:

    :ref:`Syslog Severity - Major <dcmAuditMajorFailureSeverity>`",string,"RFC 5424 Syslog Severity string value of audit message with Event Outcome Indicator 12 (Major failure). Enumerated values: emerg, alert, crit, err, warning, notice, info or debug.

    (dcmAuditMajorFailureSeverity)"
    "
    .. _dcmAuditApplicationName:

    :ref:`Syslog Application Name <dcmAuditApplicationName>`",string,"RFC 5424 Syslog APP-NAME of audit message; Audit Source ID if absent

    (dcmAuditApplicationName)"
    "
    .. _dcmAuditMessageID:

    :ref:`Syslog Message ID <dcmAuditMessageID>`",string,"RFC 5424 Syslog MSGID of audit message.

    (dcmAuditMessageID)"
    "
    .. _dcmAuditMessageEncoding:

    :ref:`Message Encoding <dcmAuditMessageEncoding>`",string,"Character encoding of RFC 5424 Syslog MSG part of audit message.

    (dcmAuditMessageEncoding)"
    "
    .. _dcmAuditMessageBOM:

    :ref:`Message BOM <dcmAuditMessageBOM>`",boolean,"Enable/disable Unicode BOM prefix of RFC 5424 Syslog MSG part of audit message; include BOM if absent

    (dcmAuditMessageBOM)"
    "
    .. _dcmAuditTimestampInUTC:

    :ref:`Timestamp in UTC <dcmAuditTimestampInUTC>`",boolean,"Specify if RFC 5424 Syslog TIMESTAMP and the Event Date/Time of the audit message are specified in Coordinated Universal Time. Default indicates it will be in Local Time zone.

    (dcmAuditTimestampInUTC)"
    "
    .. _dcmAuditMessageFormatXML:

    :ref:`Message Format XML <dcmAuditMessageFormatXML>`",boolean,"Specify whether or not the XML audit message is formatted with line feeds and indentation.

    (dcmAuditMessageFormatXML)"
    "
    .. _dcmAuditMessageSchemaURI:

    :ref:`Message Schema URI <dcmAuditMessageSchemaURI>`",string,"URI of DICOM Audit Message Schema referenced in audit message

    (dcmAuditMessageSchemaURI)"
    "
    .. _dcmAuditIncludeInstanceUID:

    :ref:`Include Instance UIDs <dcmAuditIncludeInstanceUID>`",boolean,"Indicates if Audit Log Message should contain optional Instance UIDs

    (dcmAuditIncludeInstanceUID)"
    "
    .. _dcmAuditLoggerSpoolDirectoryURI:

    :ref:`Spool Directory URI <dcmAuditLoggerSpoolDirectoryURI>`",string,"URI of spool directory used to store messages which could not delivered to the record repository; use system temporary directory if absent.

    (dcmAuditLoggerSpoolDirectoryURI)"
    "
    .. _dcmAuditLoggerRetryInterval:

    :ref:`Retry Interval <dcmAuditLoggerRetryInterval>`",integer,"Retry interval in s to re-sent messages which could not delivered to the record repository; do no retry to re-sent messages if absent

    (dcmAuditLoggerRetryInterval)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"True if the Audit Logger is installed on network. If not present, information about the installed status of the Audit Logger is inherited from the device

    (dicomInstalled)"
    ":doc:`auditSuppressCriteria` (s)",object,"Audit Suppress Criteria

    (dcmAuditSuppressCriteria)"

.. toctree::

    auditSuppressCriteria
