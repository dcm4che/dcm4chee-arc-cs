Network AE
==========
Application entity that provides services on a network

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network AE Attributes (LDAP Object: dcmNetworkAE)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dicomAETitle:

    :ref:`AE Title (dicomAETitle) <dicomAETitle>`",string,"Unique AE title for this Network AE"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) (dicomNetworkConnectionReference) <dicomNetworkConnectionReference>`",string,"JSON Pointers to the Network Connection objects for this AE"
    "
    .. _dicomAssociationInitiator:

    :ref:`Association Initiator (dicomAssociationInitiator) <dicomAssociationInitiator>`",boolean,"True if the Network AE can initiate associations."
    "
    .. _dicomAssociationAcceptor:

    :ref:`Association Acceptor (dicomAssociationAcceptor) <dicomAssociationAcceptor>`",boolean,"True if the Network AE can accept associations."
    "
    .. _dicomDescription:

    :ref:`AE Description (dicomDescription) <dicomDescription>`",string,"Unconstrained text description of the application entity"
    "
    .. _dicomApplicationCluster:

    :ref:`Application Cluster(s) (dicomApplicationCluster) <dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications"
    "
    .. _dicomPreferredCalledAETitle:

    :ref:`Preferred Called AE Title(s) (dicomPreferredCalledAETitle) <dicomPreferredCalledAETitle>`",string,"AE Title(s) that are preferred for initiating associations"
    "
    .. _dicomPreferredCallingAETitle:

    :ref:`Preferred Calling AE Title(s) (dicomPreferredCallingAETitle) <dicomPreferredCallingAETitle>`",string,"AE Title(s) that are preferred for accepting associations"
    "
    .. _dicomSupportedCharacterSet:

    :ref:`Supported Character Set(s) (dicomSupportedCharacterSet) <dicomSupportedCharacterSet>`",string,"Character Set(s) supported by the Network AE for data sets it receives"
    "
    .. _dicomInstalled:

    :ref:`installed (dicomInstalled) <dicomInstalled>`",boolean,"True if the AE is installed on network. If not present, information about the installed status of the AE is inherited from the device"
    ":doc:`transferCapability` (s)",object,"Transfer capabilities provided by the application entity"
    ":doc:`dcmNetworkAE` ",object,"dcm4che proprietary Attributes of Network AE"

.. toctree::

    transferCapability
    dcmNetworkAE
