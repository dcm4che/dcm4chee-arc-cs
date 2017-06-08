SPS Status for HL7 Order
========================
Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: SPS Status for HL7 Order Attributes (LDAP Object: hl7OrderSPSStatus)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Scheduled Procedure Step Status code",string,"Scheduled Procedure Step Status code Enumerated values: SCHEDULED, ARRIVED, READY, STARTED, DEPARTED, CANCELLED, DISCONTINUED or COMPLETED","
    .. _dcmSPSStatus:

    dcmSPSStatus_"
    "HL7 Order Control Status(s)",string,"HL7 Order Control Status Code combinations. Enumerated values: NW_SC, NW_IP, CA_CA, DC_CA, XO_SC, XO_CM, SC_CM, SC_DC, SC_IP or SC_A","
    .. _hl7OrderControlStatus:

    hl7OrderControlStatus_"
