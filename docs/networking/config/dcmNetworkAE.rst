Network AE Extension
====================
dcm4che proprietary Attributes of Network AE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Network AE Extension Attributes (LDAP Object: dcmDcmNetworkAE)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Accepted Calling AE Title(s)",string,"Prohibit accepting associations from unlisted AE. If not present, any AE will be accepted","
    .. _dcmAcceptedCallingAETitle:

    dcmAcceptedCallingAETitle_"
    "Other AE Title(s)",string,"Additional AE Title of Network AE - will also accept Association RQs with such Called AE Title","
    .. _dcmOtherAETitle:

    dcmOtherAETitle_"
    "Masquerade Calling AE Title(s)",string,"AE Title used for initiating network associations, masquerading the actual AE Title for this Network AE - optional prefix [<Called AE Title>] limits the masquerading to association to a particular AE Title","
    .. _dcmMasqueradeCallingAETitle:

    dcmMasqueradeCallingAETitle_"
    "PreferredTransferSyntax(s)",string,"Preferred Transfer Syntax for selection of Transfer Syntax within a Presentation Context, ordered by priority. If absent, the first acceptable Transfer Syntax in the offered Presentation Context will be selected. May be overwritten by configured values for particular Transfer Capabilities of this AE.","
    .. _dcmPreferredTransferSyntax:

    dcmPreferredTransferSyntax_"
    "HL7 Application name",string,"HL7 Application and Facility name (Application|Facility) associated with this AE","
    .. _hl7ApplicationName:

    hl7ApplicationName_"
    ":doc:`archiveNetworkAE` ",object,"DICOM Archive Network AE related information","
    .. _dcmArchiveNetworkAE:

    dcmArchiveNetworkAE_"

.. toctree::

    archiveNetworkAE
