Network Connection Extension
============================
dcm4che proprietary Network Connection Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network Connection Extension Attributes (LDAP Object: dcmNetworkConnection)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmProtocol:

    :ref:`Protocol <dcmProtocol>`",string,"Protocol of Network Connection. Enumerated values: DICOM, HL7, SYSLOG_TLS, SYSLOG_UDP or HTTP.

    (dcmProtocol)"
    "
    .. _dcmHTTPProxy:

    :ref:`HTTP Proxy <dcmHTTPProxy>`",string,"HTTP Proxy: [user:password@]host:port

    (dcmHTTPProxy)"
    "
    .. _dcmTLSNeedClientAuth:

    :ref:`TLS Need Client Auth <dcmTLSNeedClientAuth>`",boolean,"Indicates if TLS client authentication is required.

    (dcmTLSNeedClientAuth)"
    "
    .. _dcmTLSProtocol:

    :ref:`TLS Protocol(s) <dcmTLSProtocol>`",string,"The Supported TLS Protocols. Enumerated values: TLSv1.2, TLSv1.1, TLSv1 or SSLv3.

    (dcmTLSProtocol)"
    "
    .. _dcmTCPBacklog:

    :ref:`TCP Backlog <dcmTCPBacklog>`",integer,"Maximum queue length for incoming TCP connections. 0 = unlimited

    (dcmTCPBacklog)"
    "
    .. _dcmTCPConnectTimeout:

    :ref:`TCP Connect Timeout <dcmTCPConnectTimeout>`",integer,"TCP connect timeout in ms; no timeout if absent

    (dcmTCPConnectTimeout)"
    "
    .. _dcmTCPCloseDelay:

    :ref:`TCP Close Delay <dcmTCPCloseDelay>`",integer,"TCP socket close delay in ms after send of A-ASSOCIATE-RJ, A-RELEASE-RP or A-ABORT PDU.

    (dcmTCPCloseDelay)"
    "
    .. _dcmTCPSendBufferSize:

    :ref:`TCP Send Buffer Size <dcmTCPSendBufferSize>`",integer,"TCP send buffer size; use system defaults if absent

    (dcmTCPSendBufferSize)"
    "
    .. _dcmTCPReceiveBufferSize:

    :ref:`TCP Receive Buffer Size <dcmTCPReceiveBufferSize>`",integer,"TCP receive buffer size; use system defaults if absent

    (dcmTCPReceiveBufferSize)"
    "
    .. _dcmTCPNoDelay:

    :ref:`TCP No Delay <dcmTCPNoDelay>`",boolean,"Enable/disable TCP_NODELAY (disable/enable Nagle algorithm).

    (dcmTCPNoDelay)"
    "
    .. _dcmBindAddress:

    :ref:`Bind Address <dcmBindAddress>`",string,"Bind address of listening socket; use hostname of the connection if absent

    (dcmBindAddress)"
    "
    .. _dcmClientBindAddress:

    :ref:`Client Bind Address <dcmClientBindAddress>`",string,"Bind address of outgoing connections; use hostname of the connection if absent

    (dcmClientBindAddress)"
    "
    .. _dcmBlacklistedHostname:

    :ref:`Blacklisted Hostname(s) <dcmBlacklistedHostname>`",string,"blacklisted DNS hostnames

    (dcmBlacklistedHostname)"
    "
    .. _dcmSendPDULength:

    :ref:`Send PDU Length <dcmSendPDULength>`",integer,"Maximal length of emitted PDUs.

    (dcmSendPDULength)"
    "
    .. _dcmReceivePDULength:

    :ref:`Receive PDU Length <dcmReceivePDULength>`",integer,"Maximal length of received PDUs.

    (dcmReceivePDULength)"
    "
    .. _dcmMaxOpsPerformed:

    :ref:`Max Ops Performed <dcmMaxOpsPerformed>`",integer,"Maximal number of operations to perform asynchronously; 0 = infinite.

    (dcmMaxOpsPerformed)"
    "
    .. _dcmMaxOpsInvoked:

    :ref:`Max Ops Invoked <dcmMaxOpsInvoked>`",integer,"Maximal number of operations to invoke asynchronously; 0 = infinite.

    (dcmMaxOpsInvoked)"
    "
    .. _dcmPackPDV:

    :ref:`Pack PDV <dcmPackPDV>`",boolean,"Enable/disable packing of command and data PDVs into one P-DATA-TF PDU.

    (dcmPackPDV)"
    "
    .. _dcmAARQTimeout:

    :ref:`AA-RQ Timeout <dcmAARQTimeout>`",integer,"Timeout in ms for receive of A-ASSOCIATE-RQ PDU after TCP connect; no timeout if absent

    (dcmAARQTimeout)"
    "
    .. _dcmAAACTimeout:

    :ref:`AA-AC Timeout <dcmAAACTimeout>`",integer,"Timeout in ms for receive of A-ASSOCIATE-AC PDU after send of A-ASSOCIATE-RQ PDU; no timeout if absent

    (dcmAAACTimeout)"
    "
    .. _dcmARRPTimeout:

    :ref:`AR-RP Timeout <dcmARRPTimeout>`",integer,"Timeout in ms for receive of A-RELEASE-RP PDU after send of A-RELEASE-RQ PDU; no timeout if absent

    (dcmARRPTimeout)"
    "
    .. _dcmSendTimeout:

    :ref:`Send Timeout <dcmSendTimeout>`",integer,"Timeout in ms for sending other DIMSE RQs than C-STORE RQs; no timeout if absent

    (dcmSendTimeout)"
    "
    .. _dcmStoreTimeout:

    :ref:`Store Timeout <dcmStoreTimeout>`",integer,"Timeout in ms for sending C-STORE RQs; no timeout if absent

    (dcmStoreTimeout)"
    "
    .. _dcmResponseTimeout:

    :ref:`Response Timeout <dcmResponseTimeout>`",integer,"Timeout in ms for receive of other outstanding DIMSE RSPs than C-MOVE  or C-GET RSPs; no timeout if absent

    (dcmResponseTimeout)"
    "
    .. _dcmRetrieveTimeout:

    :ref:`Retrieve Timeout <dcmRetrieveTimeout>`",integer,"Timeout in ms for receive of outstanding C-GET or C-MOVE RSPs; no timeout if absent

    (dcmRetrieveTimeout)"
    "
    .. _dcmRetrieveTimeoutTotal:

    :ref:`Retrieve Timeout Total <dcmRetrieveTimeoutTotal>`",boolean,"Indicates if the timer with the specified timeout for outstanding C-GET and C-MOVE RSPs shall be restarted on receive of pending RSPs (=false) or not (=true).

    (dcmRetrieveTimeoutTotal)"
    "
    .. _dcmIdleTimeout:

    :ref:`Idle Timeout <dcmIdleTimeout>`",integer,"Indicates aborting of idle Associations after specified timeout in ms; no timeout if absent

    (dcmIdleTimeout)"
