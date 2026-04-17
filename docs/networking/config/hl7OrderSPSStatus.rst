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

    NW_SC (= ORC.1 = NW & ORC.5 = SC => SPSStatus = SCHEDULED)

    NW_IP (= ORC.1 = NW & ORC.5 = IP => SPSStatus = SCHEDULED)

    CA_CA (= ORC.1 = CA & ORC.5 = CA => SPSStatus = CANCELED)

    DC_CA (= ORC.1 = DC & ORC.5 = CA => SPSStatus = DISCONTINUED)

    XO_SC (= ORC.1 = XO & ORC.5 = SC => SPSStatus = SCHEDULED)

    XO_CM (= ORC.1 = XO & ORC.5 = CM => SPSStatus = COMPLETED)

    SC_CM (= ORC.1 = SC & ORC.5 = CM => SPSStatus = COMPLETED)

    SC_A (= ORC.1 = SC & ORC.5 = A => SPSStatus = COMPLETED)

    (hl7OrderControlStatus)"
