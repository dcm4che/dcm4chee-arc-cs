dcm4che Network AE Attributes
=============================
dcm4che proprietary Attributes of Network AE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: dcm4che Network AE Attributes Attributes (LDAP Object: dcmDcmNetworkAE)
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
