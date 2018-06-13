Network AE
==========
Application entity that provides services on a network

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network AE Attributes (LDAP Object: dicomNetworkAE)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomAETitle:

    :ref:`AE Title <dicomAETitle>`",string,"Unique AE title for this Network AE

    (dicomAETitle)"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) <dicomNetworkConnectionReference>`",string,"JSON Pointers to the Network Connection objects for this AE

    (dicomNetworkConnectionReference)"
    "
    .. _dicomAssociationInitiator:

    :ref:`Association Initiator <dicomAssociationInitiator>`",boolean,"True if the Network AE can initiate associations.

    (dicomAssociationInitiator)"
    "
    .. _dicomAssociationAcceptor:

    :ref:`Association Acceptor <dicomAssociationAcceptor>`",boolean,"True if the Network AE can accept associations.

    (dicomAssociationAcceptor)"
    "
    .. _dicomDescription:

    :ref:`AE Description <dicomDescription>`",string,"Unconstrained text description of the application entity

    (dicomDescription)"
    "
    .. _dicomApplicationCluster:

    :ref:`Application Cluster(s) <dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications

    (dicomApplicationCluster)"
    "
    .. _dicomPreferredCalledAETitle:

    :ref:`Preferred Called AE Title(s) <dicomPreferredCalledAETitle>`",string,"AE Title(s) that are preferred for initiating associations

    (dicomPreferredCalledAETitle)"
    "
    .. _dicomPreferredCallingAETitle:

    :ref:`Preferred Calling AE Title(s) <dicomPreferredCallingAETitle>`",string,"AE Title(s) that are preferred for accepting associations

    (dicomPreferredCallingAETitle)"
    "
    .. _dicomSupportedCharacterSet:

    :ref:`Supported Character Set(s) <dicomSupportedCharacterSet>`",string,"Character Set(s) supported by the Network AE for data sets it receives

    (dicomSupportedCharacterSet)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"True if the AE is installed on network. If not present, information about the installed status of the AE is inherited from the device

    (dicomInstalled)"
    ":doc:`transferCapability` (s)",object,"Transfer capabilities provided by the application entity

    (dicomTransferCapability)"
    ":doc:`dcmNetworkAE` ",object,"dcm4che proprietary Attributes of Network AE

    (dcmNetworkAE)"

.. toctree::

    transferCapability
    dcmNetworkAE
