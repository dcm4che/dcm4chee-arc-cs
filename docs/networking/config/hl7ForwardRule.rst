HL7 Forward Rule
================
HL7 Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Forward Rule Attributes (LDAP Object: hl7ForwardRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the HL7 Forward Rule

    (cn)"
    "
    .. _hl7FwdApplicationName:

    :ref:`HL7 Forward Application Name(s) <hl7FwdApplicationName>`",string,"HL7 Forward Destination Application and Facility name (Application|Facility)

    (hl7FwdApplicationName)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Examples: MSH-4=FORWARD or MSH-9=ADT\^A28\^ADT_A05 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
