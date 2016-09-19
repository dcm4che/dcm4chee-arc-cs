Network AE
==========
Application entity that provides services on a network

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Network AE Attributes (LDAP Object: dcmNetworkAE)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "AE Title\ :sup:`*` ",string,"Unique AE title for this Network AE","
    .. _dicomAETitle:

    dicomAETitle_"
    "Network Connection Reference(s)\ :sup:`*` ",string,"JSON Pointers to the Network Connection objects for this AE","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "Association Initiator\ :sup:`*` ",boolean,"True if the Network AE can initiate associations, false otherwise","
    .. _dicomAssociationInitiator:

    dicomAssociationInitiator_"
    "Association Acceptor\ :sup:`*` ",boolean,"True if the Network AE can accept associations, false otherwise","
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
    "Accepted Calling AE Title(s)",string,"Prohibit accepting associations from unlisted AE. If not present, any AE will be accepted","
    .. _dcmAcceptedCallingAETitle:

    dcmAcceptedCallingAETitle_"
    "Other AE Title(s)",string,"Additional AE Title of Network AE - will also accept Association RQs with such Called AE Title","
    .. _dcmOtherAETitle:

    dcmOtherAETitle_"
    "Masquerade Calling AE Title(s)",string,"AE Title used for initiating network associations, masquerading the actual AE Title for this Network AE - optional prefix [<Called AE Title>] limits the masquerading to association to a particular AE Title","
    .. _dcmMasqueradeCallingAETitle:

    dcmMasqueradeCallingAETitle_"
    ":doc:`archiveNetworkAE` ",object,"DICOM Archive Network AE related information","
    .. _dcmArchiveNetworkAE:

    dcmArchiveNetworkAE_"

.. toctree::

    transferCapability
    archiveNetworkAE
