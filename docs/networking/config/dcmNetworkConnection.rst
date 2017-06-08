dcm4che Network Connection Attributes
=====================================
dcm4che proprietary Network Connection Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: dcm4che Network Connection Attributes Attributes (LDAP Object: dcmDcmNetworkConnection)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Protocol",string,"Protocol of Network Connection: DICOM, HL7, SYSLOG_TLS or SYSLOG_UDP. Enumerated values: DICOM, HL7, SYSLOG_TLS or SYSLOG_UDP","
    .. _dcmProtocol:

    dcmProtocol_"
    "HTTP Proxy",string,"HTTP Proxy: [user:password@]host:port","
    .. _dcmHTTPProxy:

    dcmHTTPProxy_"
    "TLS Need Client Auth",boolean,"Indicates if TLS client authentication is required.","
    .. _dcmTLSNeedClientAuth:

    dcmTLSNeedClientAuth_"
    "TLS Protocol(s)",string,"The Supported TLS Protocols.","
    .. _dcmTLSProtocol:

    dcmTLSProtocol_"
    "TCP Backlog",integer,"Maximum queue length for incoming TCP connections. 0 = unlimited","
    .. _dcmTCPBacklog:

    dcmTCPBacklog_"
    "TCP Connect Timeout",integer,"TCP connect timeout in ms; 0 = no timeout.","
    .. _dcmTCPConnectTimeout:

    dcmTCPConnectTimeout_"
    "TCP Close Delay",integer,"TCP socket close delay in ms after send of A-ASSOCIATE-RJ, A-RELEASE-RP or A-ABORT PDU.","
    .. _dcmTCPCloseDelay:

    dcmTCPCloseDelay_"
    "TCP Send Buffer Size",integer,"TCP send buffer size; 0 = use system defaults.","
    .. _dcmTCPSendBufferSize:

    dcmTCPSendBufferSize_"
    "TCP Receive Buffer Size",integer,"TCP receive buffer size; 0 = use system defaults","
    .. _dcmTCPReceiveBufferSize:

    dcmTCPReceiveBufferSize_"
    "TCP No Delay",boolean,"Enable/disable TCP_NODELAY (disable/enable Nagle algorithm).","
    .. _dcmTCPNoDelay:

    dcmTCPNoDelay_"
    "Bind Address",string,"Bind address of listening socket; use hostname of the connection if absent","
    .. _dcmBindAddress:

    dcmBindAddress_"
    "Client Bind Address",string,"Bind address of outgoing connections; use hostname of the connection if absent","
    .. _dcmClientBindAddress:

    dcmClientBindAddress_"
    "Blacklisted Hostname(s)",string,"blacklisted DNS hostnames","
    .. _dcmBlacklistedHostname:

    dcmBlacklistedHostname_"
    "Send PDU Length",integer,"Maximal length of emitted PDUs.","
    .. _dcmSendPDULength:

    dcmSendPDULength_"
    "Receive PDU Length",integer,"Maximal length of received PDUs.","
    .. _dcmReceivePDULength:

    dcmReceivePDULength_"
    "Max Ops Performed",integer,"Maximal number of operations to perform asynchronously; 0 = infinite.","
    .. _dcmMaxOpsPerformed:

    dcmMaxOpsPerformed_"
    "Max Ops Invoked",integer,"Maximal number of operations to invoke asynchronously; 0 = infinite.","
    .. _dcmMaxOpsInvoked:

    dcmMaxOpsInvoked_"
    "Pack PDV",boolean,"Enable/disable packing of command and data PDVs into one P-DATA-TF PDU.","
    .. _dcmPackPDV:

    dcmPackPDV_"
    "AA-RQ Timeout",integer,"Timeout in ms for receive of A-ASSOCIATE-RQ PDU after TCP connect; 0 = no timeout.","
    .. _dcmAARQTimeout:

    dcmAARQTimeout_"
    "AA-AC Timeout",integer,"Timeout in ms for receive of A-ASSOCIATE-AC PDU after send of A-ASSOCIATE-RQ PDU; 0 = no timeout.","
    .. _dcmAAACTimeout:

    dcmAAACTimeout_"
    "AR-RP Timeout",integer,"Timeout in ms for receive of A-RELEASE-RP PDU after send of A-RELEASE-RQ PDU; 0 = no timeout.","
    .. _dcmARRPTimeout:

    dcmARRPTimeout_"
    "Response Timeout",integer,"Timeout in ms for receive of response message; 0 = no timeout.","
    .. _dcmResponseTimeout:

    dcmResponseTimeout_"
    "Retrieve Timeout",integer,"Timeout in ms for receive of C-GET-RSP or C-MOVE-RSP; 0 = no timeout.","
    .. _dcmRetrieveTimeout:

    dcmRetrieveTimeout_"
    "Idle Timeout",integer,"Indicates aborting of idle Associations after specified timeout in ms; 0 = no timeout.","
    .. _dcmIdleTimeout:

    dcmIdleTimeout_"
