Network Connection Extension
============================
dcm4che proprietary Network Connection Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network Connection Extension Attributes (LDAP Object: dcmDcmNetworkConnection)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmProtocol:

    :ref:`Protocol (dcmProtocol) <dcmProtocol>`",string,"Protocol of Network Connection. Enumerated values: DICOM, HL7, SYSLOG_TLS, SYSLOG_UDP or HTTP"
    "
    .. _dcmHTTPProxy:

    :ref:`HTTP Proxy (dcmHTTPProxy) <dcmHTTPProxy>`",string,"HTTP Proxy: [user:password@]host:port"
    "
    .. _dcmTLSNeedClientAuth:

    :ref:`TLS Need Client Auth (dcmTLSNeedClientAuth) <dcmTLSNeedClientAuth>`",boolean,"Indicates if TLS client authentication is required."
    "
    .. _dcmTLSProtocol:

    :ref:`TLS Protocol(s) (dcmTLSProtocol) <dcmTLSProtocol>`",string,"The Supported TLS Protocols. Enumerated values: TLSv1.2, TLSv1.1, TLSv1 or SSLv3"
    "
    .. _dcmTCPBacklog:

    :ref:`TCP Backlog (dcmTCPBacklog) <dcmTCPBacklog>`",integer,"Maximum queue length for incoming TCP connections. 0 = unlimited"
    "
    .. _dcmTCPConnectTimeout:

    :ref:`TCP Connect Timeout (dcmTCPConnectTimeout) <dcmTCPConnectTimeout>`",integer,"TCP connect timeout in ms; no timeout if absent"
    "
    .. _dcmTCPCloseDelay:

    :ref:`TCP Close Delay (dcmTCPCloseDelay) <dcmTCPCloseDelay>`",integer,"TCP socket close delay in ms after send of A-ASSOCIATE-RJ, A-RELEASE-RP or A-ABORT PDU."
    "
    .. _dcmTCPSendBufferSize:

    :ref:`TCP Send Buffer Size (dcmTCPSendBufferSize) <dcmTCPSendBufferSize>`",integer,"TCP send buffer size; use system defaults if absent"
    "
    .. _dcmTCPReceiveBufferSize:

    :ref:`TCP Receive Buffer Size (dcmTCPReceiveBufferSize) <dcmTCPReceiveBufferSize>`",integer,"TCP receive buffer size; use system defaults if absent"
    "
    .. _dcmTCPNoDelay:

    :ref:`TCP No Delay (dcmTCPNoDelay) <dcmTCPNoDelay>`",boolean,"Enable/disable TCP_NODELAY (disable/enable Nagle algorithm)."
    "
    .. _dcmBindAddress:

    :ref:`Bind Address (dcmBindAddress) <dcmBindAddress>`",string,"Bind address of listening socket; use hostname of the connection if absent"
    "
    .. _dcmClientBindAddress:

    :ref:`Client Bind Address (dcmClientBindAddress) <dcmClientBindAddress>`",string,"Bind address of outgoing connections; use hostname of the connection if absent"
    "
    .. _dcmBlacklistedHostname:

    :ref:`Blacklisted Hostname(s) (dcmBlacklistedHostname) <dcmBlacklistedHostname>`",string,"blacklisted DNS hostnames"
    "
    .. _dcmSendPDULength:

    :ref:`Send PDU Length (dcmSendPDULength) <dcmSendPDULength>`",integer,"Maximal length of emitted PDUs."
    "
    .. _dcmReceivePDULength:

    :ref:`Receive PDU Length (dcmReceivePDULength) <dcmReceivePDULength>`",integer,"Maximal length of received PDUs."
    "
    .. _dcmMaxOpsPerformed:

    :ref:`Max Ops Performed (dcmMaxOpsPerformed) <dcmMaxOpsPerformed>`",integer,"Maximal number of operations to perform asynchronously; 0 = infinite."
    "
    .. _dcmMaxOpsInvoked:

    :ref:`Max Ops Invoked (dcmMaxOpsInvoked) <dcmMaxOpsInvoked>`",integer,"Maximal number of operations to invoke asynchronously; 0 = infinite."
    "
    .. _dcmPackPDV:

    :ref:`Pack PDV (dcmPackPDV) <dcmPackPDV>`",boolean,"Enable/disable packing of command and data PDVs into one P-DATA-TF PDU."
    "
    .. _dcmAARQTimeout:

    :ref:`AA-RQ Timeout (dcmAARQTimeout) <dcmAARQTimeout>`",integer,"Timeout in ms for receive of A-ASSOCIATE-RQ PDU after TCP connect; no timeout if absent"
    "
    .. _dcmAAACTimeout:

    :ref:`AA-AC Timeout (dcmAAACTimeout) <dcmAAACTimeout>`",integer,"Timeout in ms for receive of A-ASSOCIATE-AC PDU after send of A-ASSOCIATE-RQ PDU; no timeout if absent"
    "
    .. _dcmARRPTimeout:

    :ref:`AR-RP Timeout (dcmARRPTimeout) <dcmARRPTimeout>`",integer,"Timeout in ms for receive of A-RELEASE-RP PDU after send of A-RELEASE-RQ PDU; no timeout if absent"
    "
    .. _dcmResponseTimeout:

    :ref:`Response Timeout (dcmResponseTimeout) <dcmResponseTimeout>`",integer,"Timeout in ms for receive of response message; no timeout if absent"
    "
    .. _dcmRetrieveTimeout:

    :ref:`Retrieve Timeout (dcmRetrieveTimeout) <dcmRetrieveTimeout>`",integer,"Timeout in ms for receive of C-GET-RSP or C-MOVE-RSP; no timeout if absent"
    "
    .. _dcmRetrieveTimeoutTotal:

    :ref:`Retrieve Timeout Total (dcmRetrieveTimeoutTotal) <dcmRetrieveTimeoutTotal>`",boolean,"Indicates if the timer with the specified timeout for outstanding C-GET and C-MOVE RSPs shall be restarted on receive of pending RSPs (=false) or not (=true)."
    "
    .. _dcmIdleTimeout:

    :ref:`Idle Timeout (dcmIdleTimeout) <dcmIdleTimeout>`",integer,"Indicates aborting of idle Associations after specified timeout in ms; no timeout if absent"
