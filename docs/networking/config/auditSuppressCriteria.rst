Audit Suppress Criteria
=======================
Audit Suppress Criteria

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Audit Suppress Criteria Attributes (LDAP Object: dcmAuditSuppressCriteria)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name of the Audit Suppress Criteria","
    .. _cn:

    cn_"
    "Audit Event ID(s)",string,"RFC 3881 Audit Event ID code and codeSystemName in format (CV, CSD, ""CM"")","
    .. _dcmAuditEventID:

    dcmAuditEventID_"
    "Audit Event Type Code(s)",string,"RFC 3881 Audit Event Type code in format (CV, CSD, ""CM"")","
    .. _dcmAuditEventTypeCode:

    dcmAuditEventTypeCode_"
    "Event Action Code(s)",string,"RFC 3881 Audit Event Action Type code.","
    .. _dcmAuditEventActionCode:

    dcmAuditEventActionCode_"
    "Event Outcome Indicator(s)",string,"RFC 3881 Audit Event Outcome Indicator.","
    .. _dcmAuditEventOutcomeIndicator:

    dcmAuditEventOutcomeIndicator_"
    "User ID(s)",string,"RFC 3881 Audit Active Participant User ID","
    .. _dcmAuditUserID:

    dcmAuditUserID_"
    "Alternative User ID(s)",string,"RFC 3881 Audit Active Participant Alternative User ID","
    .. _dcmAuditAlternativeUserID:

    dcmAuditAlternativeUserID_"
    "User Role ID Code(s)",string,"RFC 3881 Audit Active Participant User Role ID code in format (CV, CSD, ""CM"")","
    .. _dcmAuditUserRoleIDCode:

    dcmAuditUserRoleIDCode_"
    "Network Access Point ID(s)",string,"RFC 3881 Audit Active Participant Network Access Point ID","
    .. _dcmAuditNetworkAccessPointID:

    dcmAuditNetworkAccessPointID_"
    "User is Requestor",boolean,"Indicates if Active Participant is initiator/requestor of the Audit Event as specified by RFC 3881","
    .. _dcmAuditUserIsRequestor:

    dcmAuditUserIsRequestor_"
