Network Connection Extension
============================
dcm4che proprietary Network Connection Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network Connection Extension Attributes (LDAP Object: dcmNetworkConnection)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmProtocol:
    .. _dcmNetworkConnection-dcmProtocol:

    :ref:`Protocol <dcmNetworkConnection-dcmProtocol>`",string,"Protocol of Network Connection.

    Enumerated values:

    DICOM

    HL7

    HL7_MLLP2

    SYSLOG_TLS

    SYSLOG_UDP

    HTTP

    (dcmProtocol)"
    "
    .. _dcmHTTPProxy:
    .. _dcmNetworkConnection-dcmHTTPProxy:

    :ref:`HTTP Proxy <dcmNetworkConnection-dcmHTTPProxy>`",string,"HTTP Proxy: [user:password@]host:port

    (dcmHTTPProxy)"
    "
    .. _dcmTLSNeedClientAuth:
    .. _dcmNetworkConnection-dcmTLSNeedClientAuth:

    :ref:`TLS Need Client Auth <dcmNetworkConnection-dcmTLSNeedClientAuth>`",boolean,"Indicates if TLS client authentication is required.

    (dcmTLSNeedClientAuth)"
    "
    .. _dcmTLSProtocol:
    .. _dcmNetworkConnection-dcmTLSProtocol:

    :ref:`TLS Protocol(s) <dcmNetworkConnection-dcmTLSProtocol>`",string,"The Supported TLS Protocols.

    Enumerated values:

    TLSv1.3

    TLSv1.2

    TLSv1.1

    TLSv1

    SSLv3

    (dcmTLSProtocol)"
    "
    .. _dcmTLSEndpointIdentificationAlgorithm:
    .. _dcmNetworkConnection-dcmTLSEndpointIdentificationAlgorithm:

    :ref:`TLS Endpoint Identification Algorithm <dcmNetworkConnection-dcmTLSEndpointIdentificationAlgorithm>`",string,"Indicates the endpoint identification or verification procedures during TLS handshaking.

    Enumerated values:

    HTTPS

    LDAPS

    (dcmTLSEndpointIdentificationAlgorithm)"
    "
    .. _dcmTCPBacklog:
    .. _dcmNetworkConnection-dcmTCPBacklog:

    :ref:`TCP Backlog <dcmNetworkConnection-dcmTCPBacklog>`",integer,"Maximum queue length for incoming TCP connections.

    (dcmTCPBacklog)"
    "
    .. _dcmTCPConnectTimeout:
    .. _dcmNetworkConnection-dcmTCPConnectTimeout:

    :ref:`TCP Connect Timeout <dcmNetworkConnection-dcmTCPConnectTimeout>`",integer,"TCP connect timeout in ms; no timeout if absent.

    (dcmTCPConnectTimeout)"
    "
    .. _dcmTCPCloseDelay:
    .. _dcmNetworkConnection-dcmTCPCloseDelay:

    :ref:`TCP Close Delay <dcmNetworkConnection-dcmTCPCloseDelay>`",integer,"TCP socket close delay in ms after send of A-ASSOCIATE-RJ, A-RELEASE-RP or A-ABORT PDU.

    (dcmTCPCloseDelay)"
    "
    .. _dcmTCPSendBufferSize:
    .. _dcmNetworkConnection-dcmTCPSendBufferSize:

    :ref:`TCP Send Buffer Size <dcmNetworkConnection-dcmTCPSendBufferSize>`",integer,"TCP send buffer size; use system defaults if absent

    (dcmTCPSendBufferSize)"
    "
    .. _dcmTCPReceiveBufferSize:
    .. _dcmNetworkConnection-dcmTCPReceiveBufferSize:

    :ref:`TCP Receive Buffer Size <dcmNetworkConnection-dcmTCPReceiveBufferSize>`",integer,"TCP receive buffer size; use system defaults if absent

    (dcmTCPReceiveBufferSize)"
    "
    .. _dcmTCPNoDelay:
    .. _dcmNetworkConnection-dcmTCPNoDelay:

    :ref:`TCP No Delay <dcmNetworkConnection-dcmTCPNoDelay>`",boolean,"Enable/disable TCP_NODELAY (disable/enable Nagle algorithm).

    (dcmTCPNoDelay)"
    "
    .. _dcmBindAddress:
    .. _dcmNetworkConnection-dcmBindAddress:

    :ref:`Bind Address <dcmNetworkConnection-dcmBindAddress>`",string,"Bind address of listening socket; use hostname of the connection if absent

    (dcmBindAddress)"
    "
    .. _dcmClientBindAddress:
    .. _dcmNetworkConnection-dcmClientBindAddress:

    :ref:`Client Bind Address <dcmNetworkConnection-dcmClientBindAddress>`",string,"Bind address of outgoing connections; use hostname of the connection if absent

    (dcmClientBindAddress)"
    "
    .. _dcmBlacklistedHostname:
    .. _dcmNetworkConnection-dcmBlacklistedHostname:

    :ref:`Blacklisted Hostname(s) <dcmNetworkConnection-dcmBlacklistedHostname>`",string,"blacklisted DNS hostnames

    (dcmBlacklistedHostname)"
    "
    .. _dcmSendPDULength:
    .. _dcmNetworkConnection-dcmSendPDULength:

    :ref:`Send PDU Length <dcmNetworkConnection-dcmSendPDULength>`",integer,"Maximal length of emitted PDUs.

    (dcmSendPDULength)"
    "
    .. _dcmReceivePDULength:
    .. _dcmNetworkConnection-dcmReceivePDULength:

    :ref:`Receive PDU Length <dcmNetworkConnection-dcmReceivePDULength>`",integer,"Maximal length of received PDUs.

    (dcmReceivePDULength)"
    "
    .. _dcmMaxOpsPerformed:
    .. _dcmNetworkConnection-dcmMaxOpsPerformed:

    :ref:`Max Ops Performed <dcmNetworkConnection-dcmMaxOpsPerformed>`",integer,"Maximal number of operations to perform asynchronously; 0 = infinite.

    (dcmMaxOpsPerformed)"
    "
    .. _dcmMaxOpsInvoked:
    .. _dcmNetworkConnection-dcmMaxOpsInvoked:

    :ref:`Max Ops Invoked <dcmNetworkConnection-dcmMaxOpsInvoked>`",integer,"Maximal number of operations to invoke asynchronously; 0 = infinite.

    (dcmMaxOpsInvoked)"
    "
    .. _dcmPackPDV:
    .. _dcmNetworkConnection-dcmPackPDV:

    :ref:`Pack PDV <dcmNetworkConnection-dcmPackPDV>`",boolean,"Enable/disable packing of command and data PDVs into one P-DATA-TF PDU.

    (dcmPackPDV)"
    "
    .. _dcmAARQTimeout:
    .. _dcmNetworkConnection-dcmAARQTimeout:

    :ref:`AA-RQ Timeout <dcmNetworkConnection-dcmAARQTimeout>`",integer,"Timeout in ms for receive of A-ASSOCIATE-RQ PDU after TCP connect; no timeout if absent

    (dcmAARQTimeout)"
    "
    .. _dcmAAACTimeout:
    .. _dcmNetworkConnection-dcmAAACTimeout:

    :ref:`AA-AC Timeout <dcmNetworkConnection-dcmAAACTimeout>`",integer,"Timeout in ms for receive of A-ASSOCIATE-AC PDU after send of A-ASSOCIATE-RQ PDU; no timeout if absent

    (dcmAAACTimeout)"
    "
    .. _dcmARRPTimeout:
    .. _dcmNetworkConnection-dcmARRPTimeout:

    :ref:`AR-RP Timeout <dcmNetworkConnection-dcmARRPTimeout>`",integer,"Timeout in ms for receive of A-RELEASE-RP PDU after send of A-RELEASE-RQ PDU; no timeout if absent

    (dcmARRPTimeout)"
    "
    .. _dcmSendTimeout:
    .. _dcmNetworkConnection-dcmSendTimeout:

    :ref:`Send Timeout <dcmNetworkConnection-dcmSendTimeout>`",integer,"Timeout in ms for sending other DIMSE RQs than C-STORE RQs; no timeout if absent

    (dcmSendTimeout)"
    "
    .. _dcmStoreTimeout:
    .. _dcmNetworkConnection-dcmStoreTimeout:

    :ref:`Store Timeout <dcmNetworkConnection-dcmStoreTimeout>`",integer,"Timeout in ms for sending C-STORE RQs; no timeout if absent

    (dcmStoreTimeout)"
    "
    .. _dcmResponseTimeout:
    .. _dcmNetworkConnection-dcmResponseTimeout:

    :ref:`Response Timeout <dcmNetworkConnection-dcmResponseTimeout>`",integer,"Timeout in ms for receive of outstanding 

	- DIMSE RSPs other than C-MOVE / C-GET RSPs 

	- responses of outgoing HL7 messages 

	- HTTP(S) responses 

	No timeout if absent

    (dcmResponseTimeout)"
    "
    .. _dcmRetrieveTimeout:
    .. _dcmNetworkConnection-dcmRetrieveTimeout:

    :ref:`Retrieve Timeout <dcmNetworkConnection-dcmRetrieveTimeout>`",integer,"Timeout in ms for receive of outstanding C-GET or C-MOVE RSPs; no timeout if absent

    (dcmRetrieveTimeout)"
    "
    .. _dcmRetrieveTimeoutTotal:
    .. _dcmNetworkConnection-dcmRetrieveTimeoutTotal:

    :ref:`Retrieve Timeout Total <dcmNetworkConnection-dcmRetrieveTimeoutTotal>`",boolean,"Indicates if the timer with the specified timeout for outstanding C-GET and C-MOVE RSPs shall be restarted on receive of pending RSPs (=false) or not (=true).

    (dcmRetrieveTimeoutTotal)"
    "
    .. _dcmIdleTimeout:
    .. _dcmNetworkConnection-dcmIdleTimeout:

    :ref:`Idle Timeout <dcmNetworkConnection-dcmIdleTimeout>`",integer,"Indicates aborting of idle Associations after specified timeout in ms; no timeout if absent

    (dcmIdleTimeout)"
    "
    .. _dcmAATimeout:
    .. _dcmNetworkConnection-dcmAATimeout:

    :ref:`A-ABORT Timeout <dcmNetworkConnection-dcmAATimeout>`",integer,"Timeout in ms for waiting for finishing sending any DIMSE before sending an A-ABORT PDU, triggered by the application or by expiration of a configured other timeout of this Connection. If the timeout expires, the TCP connection will be closed without sending the A-ABORT.

    (dcmAATimeout)"
