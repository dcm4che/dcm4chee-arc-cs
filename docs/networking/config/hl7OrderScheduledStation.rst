Scheduled Station for HL7 Order
===============================
Scheduled Station selected on MWL HL7 Order Feed

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Scheduled Station for HL7 Order Attributes (LDAP Object: hl7OrderScheduledStation)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Name**",string,"Arbitrary/Meaningful name for the Scheduled Station Order Mapping","
    .. _cn:

    cn_"
    "**Scheduled Station Device Name**",string,"Device Name of Scheduled Station","
    .. _hl7OrderScheduledStationDeviceName:

    hl7OrderScheduledStationDeviceName_"
    "Mapping Priority",integer,"Mapping Priority. 0 if absent.","
    .. _dcmRulePriority:

    dcmRulePriority_"
    "Conditions(s)",string,"Conditions in format {attributeID}[!]={regEx} or MSH-#[!]={regEx}","
    .. _dcmProperty:

    dcmProperty_"
