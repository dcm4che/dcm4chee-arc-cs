Network Connection
==================
Describes one TCP/UDP port on one network device.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network Connection Attributes (LDAP Object: dcmNetworkConnection)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name for the Network Connection object"
    "
    .. _dicomHostname:

    :ref:`Hostname (dicomHostname) <dicomHostname>`",string,"DNS name for this particular connection"
    "
    .. _dicomPort:

    :ref:`Port (dicomPort) <dicomPort>`",integer,"TCP/UDP port that a service is listening on. May be missing if this network connection is only used for outbound connections"
    "
    .. _dicomTLSCipherSuite:

    :ref:`TLS CipherSuites(s) (dicomTLSCipherSuite) <dicomTLSCipherSuite>`",string,"The TLS CipherSuites that are supported on this particular connection. If not present TLS is disabled Enumerated values: SSL_RSA_WITH_NULL_SHA, TLS_RSA_WITH_AES_128_CBC_SHA or SSL_RSA_WITH_3DES_EDE_CBC_SHA"
    "
    .. _dicomInstalled:

    :ref:`installed (dicomInstalled) <dicomInstalled>`",boolean,"True if the Network Connection is installed on the network. If not present, information about the installed status of the Network Connection is inherited from the device"
    ":doc:`dcmNetworkConnection` ",object,"dcm4che proprietary Network Connection Attributes"

.. toctree::

    dcmNetworkConnection
