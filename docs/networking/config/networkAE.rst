Network AE
==========
Application entity that provides services on a network

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Network AE Attributes (LDAP Object: dcmNetworkAE)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "AE Title",string,"Unique AE title for this Network AE","
    .. _dicomAETitle:

    dicomAETitle_"
    "Network Connection Reference(s)",string,"JSON Pointers to the Network Connection objects for this AE","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "Association Initiator",boolean,"True if the Network AE can initiate associations.","
    .. _dicomAssociationInitiator:

    dicomAssociationInitiator_"
    "Association Acceptor",boolean,"True if the Network AE can accept associations.","
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
    "Supported Character Set(s)",string,"Character Set(s) supported by the Network AE for data sets it receives Enumerated values: ISO_IR 100, ISO_IR 101, ISO_IR 109, ISO_IR 110, ISO_IR 144, ISO_IR 127, ISO_IR 126, ISO_IR 138, ISO_IR 148, ISO_IR 13, ISO_IR 166, ISO 2022 IR 6, ISO 2022 IR 100, ISO 2022 IR 101, ISO 2022 IR 109, ISO 2022 IR 110, ISO 2022 IR 144, ISO 2022 IR 127, ISO 2022 IR 126, ISO 2022 IR 138, ISO 2022 IR 148, ISO 2022 IR 13, ISO 2022 IR 166, ISO 2022 IR 87, ISO 2022 IR 159, ISO 2022 IR 149, ISO 2022 IR 58, ISO_IR 192, GB18030 or GBK","
    .. _dicomSupportedCharacterSet:

    dicomSupportedCharacterSet_"
    "installed",boolean,"True if the AE is installed on network. If not present, information about the installed status of the AE is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
    ":doc:`transferCapability` (s)",object,"Transfer capabilities provided by the application entity","
    .. _dicomTransferCapability:

    dicomTransferCapability_"
    ":doc:`dcmNetworkAE` ",object,"dcm4che proprietary Attributes of Network AE","
    .. _dcmNetworkAE:

    dcmNetworkAE_"

.. toctree::

    transferCapability
    dcmNetworkAE
