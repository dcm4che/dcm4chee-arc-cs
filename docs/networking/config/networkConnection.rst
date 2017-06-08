Network Connection
==================
Describes one TCP/UDP port on one network device.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Network Connection Attributes (LDAP Object: dcmNetworkConnection)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name for the Network Connection object","
    .. _cn:

    cn_"
    "Hostname",string,"DNS name for this particular connection","
    .. _dicomHostname:

    dicomHostname_"
    "Port",integer,"TCP/UDP port that a service is listening on. May be missing if this network connection is only used for outbound connections","
    .. _dicomPort:

    dicomPort_"
    "TLS CipherSuites(s)",string,"The TLS CipherSuites that are supported on this particular connection. If not present TLS is disabled Enumerated values: SSL_RSA_WITH_NULL_SHA, TLS_RSA_WITH_AES_128_CBC_SHA or SSL_RSA_WITH_3DES_EDE_CBC_SHA","
    .. _dicomTLSCipherSuite:

    dicomTLSCipherSuite_"
    "installed",boolean,"True if the Network Connection is installed on the network. If not present, information about the installed status of the Network Connection is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
    ":doc:`dcmNetworkConnection` ",object,"dcm4che proprietary Network Connection Attributes","
    .. _dcmNetworkConnection:

    dcmNetworkConnection_"

.. toctree::

    dcmNetworkConnection
