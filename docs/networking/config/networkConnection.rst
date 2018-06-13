Network Connection
==================
Describes one TCP/UDP port on one network device.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network Connection Attributes (LDAP Object: dicomNetworkConnection)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name for the Network Connection object

    (cn)"
    "
    .. _dicomHostname:

    :ref:`Hostname <dicomHostname>`",string,"DNS name for this particular connection

    (dicomHostname)"
    "
    .. _dicomPort:

    :ref:`Port <dicomPort>`",integer,"TCP/UDP port that a service is listening on. May be missing if this network connection is only used for outbound connections

    (dicomPort)"
    "
    .. _dicomTLSCipherSuite:

    :ref:`TLS CipherSuites(s) <dicomTLSCipherSuite>`",string,"The TLS CipherSuites that are supported on this particular connection. If not present TLS is disabled Enumerated values: SSL_RSA_WITH_NULL_SHA, TLS_RSA_WITH_AES_128_CBC_SHA or SSL_RSA_WITH_3DES_EDE_CBC_SHA.

    (dicomTLSCipherSuite)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"True if the Network Connection is installed on the network. If not present, information about the installed status of the Network Connection is inherited from the device

    (dicomInstalled)"
    ":doc:`dcmNetworkConnection` ",object,"dcm4che proprietary Network Connection Attributes"

.. toctree::

    dcmNetworkConnection
