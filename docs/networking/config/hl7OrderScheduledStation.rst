Scheduled Station for HL7 Order
===============================
Scheduled Station selected on MWL HL7 Order Feed

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Scheduled Station for HL7 Order Attributes (LDAP Object: hl7OrderScheduledStation)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name for the Scheduled Station Order Mapping

    (cn)"
    "
    .. _hl7OrderScheduledStationDeviceName:

    :ref:`Scheduled Station Device Name <hl7OrderScheduledStationDeviceName>`",string,"Device name of Scheduled Station used for HL7 Order Messages.

    (hl7OrderScheduledStationDeviceName)"
    "
    .. _dcmRulePriority:

    :ref:`Mapping Priority <dcmRulePriority>`",integer,"If the condition of several Scheduled Station for HL7 Order rules match for a received HL7 message and each have different priority, Scheduled Station Device Name of highest priority is applied. If the condition of several Scheduled Station for HL7 Order rules match for a received HL7 message and each have equal priority, Scheduled Station Device Name of each is applied.

    (dcmRulePriority)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Examples: MSH-4=FORWARD or MSH-9=ADT\^A28\^ADT_A05 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
