Network AE
==========
Application entity that provides services on a network

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network AE Attributes (LDAP Object: dicomNetworkAE)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomAETitle:
    .. _networkAE-dicomAETitle:

    :ref:`AE Title <networkAE-dicomAETitle>`",string,"Unique AE title for this Network AE

    (dicomAETitle)"
    "
    .. _dicomNetworkConnectionReference:
    .. _networkAE-dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) <networkAE-dicomNetworkConnectionReference>`",string,"JSON Pointers to the Network Connection objects for this AE

    (dicomNetworkConnectionReference)"
    "
    .. _dicomAssociationInitiator:
    .. _networkAE-dicomAssociationInitiator:

    :ref:`Association Initiator <networkAE-dicomAssociationInitiator>`",boolean,"True if the Network AE can initiate associations.

    (dicomAssociationInitiator)"
    "
    .. _dicomAssociationAcceptor:
    .. _networkAE-dicomAssociationAcceptor:

    :ref:`Association Acceptor <networkAE-dicomAssociationAcceptor>`",boolean,"True if the Network AE can accept associations.

    (dicomAssociationAcceptor)"
    "
    .. _dicomDescription:
    .. _networkAE-dicomDescription:

    :ref:`AE Description <networkAE-dicomDescription>`",string,"Unconstrained text description of the application entity

    (dicomDescription)"
    "
    .. _dicomApplicationCluster:
    .. _networkAE-dicomApplicationCluster:

    :ref:`Application Cluster(s) <networkAE-dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications

    (dicomApplicationCluster)"
    "
    .. _dicomPreferredCalledAETitle:
    .. _networkAE-dicomPreferredCalledAETitle:

    :ref:`Preferred Called AE Title(s) <networkAE-dicomPreferredCalledAETitle>`",string,"AE Title(s) that are preferred for initiating associations

    (dicomPreferredCalledAETitle)"
    "
    .. _dicomPreferredCallingAETitle:
    .. _networkAE-dicomPreferredCallingAETitle:

    :ref:`Preferred Calling AE Title(s) <networkAE-dicomPreferredCallingAETitle>`",string,"AE Title(s) that are preferred for accepting associations

    (dicomPreferredCallingAETitle)"
    "
    .. _dicomSupportedCharacterSet:
    .. _networkAE-dicomSupportedCharacterSet:

    :ref:`Supported Character Set(s) <networkAE-dicomSupportedCharacterSet>`",string,"Character Set(s) supported by the Network AE for data sets it receives

    (dicomSupportedCharacterSet)"
    "
    .. _dicomInstalled:
    .. _networkAE-dicomInstalled:

    :ref:`installed <networkAE-dicomInstalled>`",boolean,"True if the AE is installed on network. If not present, information about the installed status of the AE is inherited from the device

    (dicomInstalled)"
    ":doc:`transferCapability` (s)",object,"Transfer capabilities provided by the application entity"
    ":doc:`dcmNetworkAE` ",object,"dcm4che proprietary Attributes of Network AE"

.. toctree::

    transferCapability
    dcmNetworkAE
