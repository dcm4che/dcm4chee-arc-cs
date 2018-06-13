Network AE Extension
====================
dcm4che proprietary Attributes of Network AE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Network AE Extension Attributes (LDAP Object: dcmDcmNetworkAE)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmAcceptedCallingAETitle:

    :ref:`Accepted Calling AE Title(s) (dcmAcceptedCallingAETitle) <dcmAcceptedCallingAETitle>`",string,"Prohibit accepting associations from unlisted AE. If not present, any AE will be accepted"
    "
    .. _dcmOtherAETitle:

    :ref:`Other AE Title(s) (dcmOtherAETitle) <dcmOtherAETitle>`",string,"Additional AE Title of Network AE - will also accept Association RQs with such Called AE Title"
    "
    .. _dcmMasqueradeCallingAETitle:

    :ref:`Masquerade Calling AE Title(s) (dcmMasqueradeCallingAETitle) <dcmMasqueradeCallingAETitle>`",string,"AE Title used for initiating network associations, masquerading the actual AE Title for this Network AE - optional prefix [<Called AE Title>] limits the masquerading to association to a particular AE Title"
    "
    .. _dcmPreferredTransferSyntax:

    :ref:`Preferred Transfer Syntax(s) (dcmPreferredTransferSyntax) <dcmPreferredTransferSyntax>`",string,"Preferred Transfer Syntax for selection of Transfer Syntax within a Presentation Context, ordered by priority. If absent, the first acceptable Transfer Syntax in the offered Presentation Context will be selected. May be overwritten by configured values for particular Transfer Capabilities of this AE."
    "
    .. _hl7ApplicationName:

    :ref:`HL7 Application name (hl7ApplicationName) <hl7ApplicationName>`",string,"HL7 Application and Facility name (Application|Facility) associated with this AE"
    ":doc:`archiveNetworkAE` ",object,"DICOM Archive Network AE related information"

.. toctree::

    archiveNetworkAE
