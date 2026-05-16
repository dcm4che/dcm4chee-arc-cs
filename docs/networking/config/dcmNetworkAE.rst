Network AE Extension
====================
dcm4che proprietary Attributes of Network AE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network AE Extension Attributes (LDAP Object: dcmNetworkAE)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmRoleSelectionNegotiationLenient:
    .. _dcmNetworkAE-dcmRoleSelectionNegotiationLenient:

    :ref:`Role Selection Negotiation Lenient <dcmNetworkAE-dcmRoleSelectionNegotiationLenient>`",boolean,"Indicates to disable check for required SCP/SCU role selection negotiation on sending of DIMSE-RQs. Overwrites value specified on Device level.

    (dcmRoleSelectionNegotiationLenient)"
    "
    .. _dcmAcceptedCallingAETitle:
    .. _dcmNetworkAE-dcmAcceptedCallingAETitle:

    :ref:`Accepted Calling AE Title(s) <dcmNetworkAE-dcmAcceptedCallingAETitle>`",string,"Prohibit accepting associations from unlisted AE. If not present, any AE will be accepted

    (dcmAcceptedCallingAETitle)"
    "
    .. _dcmOtherAETitle:
    .. _dcmNetworkAE-dcmOtherAETitle:

    :ref:`Other AE Title(s) <dcmNetworkAE-dcmOtherAETitle>`",string,"Additional AE Title of Network AE - will also accept Association RQs with such Called AE Title

    (dcmOtherAETitle)"
    "
    .. _dcmNoAsyncModeCalledAETitle:
    .. _dcmNetworkAE-dcmNoAsyncModeCalledAETitle:

    :ref:`No Async Mode Called AE Title(s) <dcmNetworkAE-dcmNoAsyncModeCalledAETitle>`",string,"Blacklist AE Title of peer Network AE as not capable to handle Asynchronous Operations Window Negotiation correctly. Suppress including corresponding User-data sub-Item in A-ASSOCIATE RQs to that Network AEs.

    (dcmNoAsyncModeCalledAETitle)"
    "
    .. _dcmMasqueradeCalledAETitle:
    .. _dcmNetworkAE-dcmMasqueradeCalledAETitle:

    :ref:`Masquerade Called AE Title(s) <dcmNetworkAE-dcmMasqueradeCalledAETitle>`",string,"Called AE Title used for initiating network associations, masquerading the configured AE Title of the remote Network AE. Format <Configured AE Title>:<Used Called AE Title>.

    (dcmMasqueradeCalledAETitle)"
    "
    .. _dcmMasqueradeCallingAETitle:
    .. _dcmNetworkAE-dcmMasqueradeCallingAETitle:

    :ref:`Masquerade Calling AE Title(s) <dcmNetworkAE-dcmMasqueradeCallingAETitle>`",string,"Calling AE Title used for initiating network associations, masquerading the actual AE Title for this Network AE - optional prefix [<Called AE Title>] limits the masquerading to association to a particular AE Title.

    (dcmMasqueradeCallingAETitle)"
    "
    .. _dcmPreferredTransferSyntax:
    .. _dcmNetworkAE-dcmPreferredTransferSyntax:

    :ref:`Preferred Transfer Syntax(s) <dcmNetworkAE-dcmPreferredTransferSyntax>`",string,"Preferred Transfer Syntax for selection of Transfer Syntax within a Presentation Context, ordered by priority. If absent, the first acceptable Transfer Syntax in the offered Presentation Context will be selected. May be overwritten by configured values for particular Transfer Capabilities of this AE.

    (dcmPreferredTransferSyntax)"
    "
    .. _dcmShareTransferCapabilitiesFromAETitle:
    .. _dcmNetworkAE-dcmShareTransferCapabilitiesFromAETitle:

    :ref:`Share Transfer Capabilities from AE Title <dcmNetworkAE-dcmShareTransferCapabilitiesFromAETitle>`",string,"Indicates that this Network AE supports the Transfer Capabilities specified for another Network AE of the same Device.

    (dcmShareTransferCapabilitiesFromAETitle)"
    "
    .. _hl7ApplicationName:
    .. _dcmNetworkAE-hl7ApplicationName:

    :ref:`HL7 Application name <dcmNetworkAE-hl7ApplicationName>`",string,"HL7 Application and Facility name (Application|Facility) associated with this AE

    (hl7ApplicationName)"
    ":doc:`archiveNetworkAE` ",object,"DICOM Archive Network AE related information"

.. toctree::

    archiveNetworkAE
