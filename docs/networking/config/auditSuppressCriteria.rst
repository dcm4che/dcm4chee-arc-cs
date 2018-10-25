Audit Suppress Criteria
=======================
Audit Suppress Criteria

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Audit Suppress Criteria Attributes (LDAP Object: dcmAuditSuppressCriteria)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Audit Suppress Criteria

    (cn)"
    "
    .. _dcmAuditEventID:

    :ref:`Audit Event ID(s) <dcmAuditEventID>`",string,"RFC 3881 Audit Event ID code and codeSystemName in format (CV, CSD, ""CM"") Enumerated values: (110100, DCM, \Application Activity\), (110101, DCM, \Audit Log Used\), (110102, DCM, \Begin Transferring DICOM Instances\), (110103, DCM, \DICOM Instances Accessed\), (110104, DCM, \DICOM Instances Transferred\), (110105, DCM, \DICOM Study Deleted\), (110106, DCM, \Export\), (110107, DCM, \Import\), (110108, DCM, \Network Entry\), (110109, DCM, \Order Record\), (110110, DCM, \Patient Record\), (110111, DCM, \Procedure Record\), (110112, DCM, \Query\), (110113, DCM, \Security Alert\), (110114, DCM, \User Authentication\), (IHE0001, IHE, \Health Services Provision Event\), (IHE0002, IHE, \Medication Event\), (IHE0003, IHE, \Patient Care Resource Assignment\), (IHE0004, IHE, \Patient Care Episode\) or (IHE0005, IHE, \Patient Care Protocol\).

    (dcmAuditEventID)"
    "
    .. _dcmAuditEventTypeCode:

    :ref:`Audit Event Type Code(s) <dcmAuditEventTypeCode>`",string,"RFC 3881 Audit Event Type code in format (CV, CSD, ""CM"") Enumerated values: (110120, DCM, \Application Start\), (110121, DCM, \Application Stop\), (110122, DCM, \Login\), (110123, DCM, \Logout\), (110124, DCM, \Attach\), (110125, DCM, \Detach\), (110126, DCM, \Node Authentication\), (110127, DCM, \Emergency Override Started\), (110128, DCM, \Network Configuration\), (110129, DCM, \Security Configuration\), (110130, DCM, \Hardware Configuration\), (110131, DCM, \Software Configuration\), (110132, DCM, \Use of Restricted Function\), (110133, DCM, \Audit Recording Stopped\), (110134, DCM, \Audit Recording Started\), (110135, DCM, \Object Security Attributes Changed\), (110136, DCM, \Security Roles Changed\), (110137, DCM, \User security Attributes Changed\), (110138, DCM, \Emergency Override Stopped\), (110139, DCM, \Remote Service Operation Started\), (110140, DCM, \Remote Service Operation Stopped\), (110141, DCM, \Local Service Operation Started\), (110142, DCM, \Local Service Operation Stopped\), (ITI-8, IHE Transactions, \Patient Identity Feed\), (ITI-9, IHE Transactions, \PIX Query\), (ITI-10, IHE Transactions, \PIX Update Notification\), (ITI-18, IHE Transactions, \Registry Stored Query\), (ITI-21, IHE Transactions, \Patient Demographics Query\), (ITI-22, IHE Transactions, \Patient Demographics and Visit Query\), (ITI-38, IHE Transactions, \Cross Gateway Query\), (ITI-39, IHE Transactions, \Cross Gateway Retrieve\), (ITI-41, IHE Transactions, \Provide and Register Document Set-b\), (ITI-42, IHE Transactions, \Register Document Set-b\), (ITI-43, IHE Transactions, \Retrieve Document Set\), (ITI-44, IHE Transactions, \Patient Identity Feed\), (ITI-45, IHE Transactions, \PIX Query\), (ITI-46, IHE Transactions, \PIX Update Notification\), (ITI-47, IHE Transactions, \Patient Demographics Query\), (ITI-51, IHE Transactions, \Multi-Patient Query\) or (ITI-63, IHE Transactions, \XCF Fetch\).

    (dcmAuditEventTypeCode)"
    "
    .. _dcmAuditEventActionCode:

    :ref:`Event Action Code(s) <dcmAuditEventActionCode>`",string,"RFC 3881 Audit Event Action Type code. Enumerated values: C, R, U, D or E.

    (dcmAuditEventActionCode)"
    "
    .. _dcmAuditEventOutcomeIndicator:

    :ref:`Event Outcome Indicator(s) <dcmAuditEventOutcomeIndicator>`",string,"RFC 3881 Audit Event Outcome Indicator. Enumerated values: 0, 4, 8 or 12.

    (dcmAuditEventOutcomeIndicator)"
    "
    .. _dcmAuditUserID:

    :ref:`User ID(s) <dcmAuditUserID>`",string,"RFC 3881 Audit Active Participant User ID

    (dcmAuditUserID)"
    "
    .. _dcmAuditAlternativeUserID:

    :ref:`Alternative User ID(s) <dcmAuditAlternativeUserID>`",string,"RFC 3881 Audit Active Participant Alternative User ID

    (dcmAuditAlternativeUserID)"
    "
    .. _dcmAuditUserRoleIDCode:

    :ref:`User Role ID Code(s) <dcmAuditUserRoleIDCode>`",string,"RFC 3881 Audit Active Participant User Role ID code in format (CV, CSD, ""CM"") Enumerated values: (110150, DCM, \Application\), (110151, DCM, \Application Launcher\), (110152, DCM, \Destination\), (110153, DCM, \Source\), (110154, DCM, \Destination Media\) or (110155, DCM, \Source Media\).

    (dcmAuditUserRoleIDCode)"
    "
    .. _dcmAuditNetworkAccessPointID:

    :ref:`Network Access Point ID(s) <dcmAuditNetworkAccessPointID>`",string,"RFC 3881 Audit Active Participant Network Access Point ID

    (dcmAuditNetworkAccessPointID)"
    "
    .. _dcmAuditUserIsRequestor:

    :ref:`User is Requestor <dcmAuditUserIsRequestor>`",boolean,"Indicates if Active Participant is initiator/requestor of the Audit Event as specified by RFC 3881

    (dcmAuditUserIsRequestor)"
