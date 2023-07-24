SPS Status for HL7 Order
========================
Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: SPS Status for HL7 Order Attributes (LDAP Object: hl7OrderSPSStatus)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmSPSStatus:

    :ref:`Scheduled Procedure Step Status code <dcmSPSStatus>`",string,"Scheduled Procedure Step Status code

    Enumerated values:

    SCHEDULED

    CANCELED

    DISCONTINUED

    COMPLETED

    (dcmSPSStatus)"
    "
    .. _hl7OrderControlStatus:

    :ref:`HL7 Order Control Status(s) <hl7OrderControlStatus>`",string,"HL7 Order Control Status Code combinations. These combinations refer to values present in ORC-1_ORC-5.

    Enumerated values:

    NW_SC

    NW_IP

    CA_CA

    DC_CA

    XO_SC

    XO_CM

    SC_CM

    SC_A

    (hl7OrderControlStatus)"
