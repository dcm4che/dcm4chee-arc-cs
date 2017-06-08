HL7 Forward Rule
================
HL7 Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: HL7 Forward Rule Attributes (LDAP Object: hl7ForwardRule)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name of the HL7 Forward Rule","
    .. _cn:

    cn_"
    "HL7 Sending Application",string,"HL7 Sending Application and Facility name (Application|Facility) in forwarded HL7 Message. If absent, use original Sending Application and Facility from received HL7 Message.","
    .. _hl7ApplicationName:

    hl7ApplicationName_"
    "HL7 Forward Application Name(s)",string,"HL7 Forward Destination Application and Facility name (Application|Facility)","
    .. _hl7FwdApplicationName:

    hl7FwdApplicationName_"
    "Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
