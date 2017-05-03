Network AE
==========
Application entity that provides services on a network

.. toctree::

    transferCapability
    dcmNetworkAE
    archiveNetworkAE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Network AE Attributes (LDAP Object: dcmNetworkAE)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**AE Title**",string,"Unique AE title for this Network AE","
    .. _dicomAETitle:

    dicomAETitle_"
    "**Network Connection Reference(s)**",string,"JSON Pointers to the Network Connection objects for this AE","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "**Association Initiator**",boolean,"True if the Network AE can initiate associations, false otherwise","
    .. _dicomAssociationInitiator:

    dicomAssociationInitiator_"
    "**Association Acceptor**",boolean,"True if the Network AE can accept associations, false otherwise","
    .. _dicomAssociationAcceptor:

    dicomAssociationAcceptor_"
    "AE Description",string,"Unconstrained text description of the application entity","
    .. _dicomDescription:

    dicomDescription_"
    "Application Cluster(s)",string,"Locally defined names for a subset of related applications","
    .. _dicomApplicationCluster:

    dicomApplicationCluster_"
    "Preferred Called AE Title(s)",string,"AE Title(s) that are preferred for initiating associations","
    .. _dicomPreferredCalledAETitle:

    dicomPreferredCalledAETitle_"
    "Preferred Calling AE Title(s)",string,"AE Title(s) that are preferred for accepting associations","
    .. _dicomPreferredCallingAETitle:

    dicomPreferredCallingAETitle_"
    "Supported Character Set(s)",string,"Character Set(s) supported by the Network AE for data sets it receives","
    .. _dicomSupportedCharacterSet:

    dicomSupportedCharacterSet_"
    "installed",boolean,"True if the AE is installed on network. If not present, information about the installed status of the AE is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
    ":doc:`transferCapability` (s)",object,"transfer capabilities provided by the application entity","
    .. _dicomTransferCapability:

    dicomTransferCapability_"
    ":doc:`dcmNetworkAE` ",object,"dcm4che proprietary Attributes of Network AE","
    .. _dcmNetworkAE:

    dcmNetworkAE_"
    ":doc:`archiveNetworkAE` ",object,"DICOM Archive Network AE related information","
    .. _dcmArchiveNetworkAE:

    dcmArchiveNetworkAE_"
