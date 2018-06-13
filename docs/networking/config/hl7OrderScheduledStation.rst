Scheduled Station for HL7 Order
===============================
Scheduled Station selected on MWL HL7 Order Feed

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Scheduled Station for HL7 Order Attributes (LDAP Object: hl7OrderScheduledStation)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name for the Scheduled Station Order Mapping"
    "
    .. _hl7OrderScheduledStationDeviceName:

    :ref:`Scheduled Station Device Name (hl7OrderScheduledStationDeviceName) <hl7OrderScheduledStationDeviceName>`",string,"Device name of Scheduled Station used for HL7 Order Messages."
    "
    .. _dcmRulePriority:

    :ref:`Mapping Priority (dcmRulePriority) <dcmRulePriority>`",integer,"Mapping Priority."
    "
    .. _dcmProperty:

    :ref:`Conditions(s) (dcmProperty) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx} or MSH-#[!]={regEx} Examples: MSH-3=FORWARD or MSH-8=ADT\^A28\^ADT_A05"
