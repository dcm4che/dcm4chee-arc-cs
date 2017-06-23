dcm4che Device Attributes
=========================
dcm4che proprietary Device Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: dcm4che Device Attributes Attributes (LDAP Object: dcmDcmDevice)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Limit Open Associations",integer,"Limit open DICOM connections; rejects Association requests if the limit is exceeded. 0 = unlimited.","
    .. _dcmLimitOpenAssociations:

    dcmLimitOpenAssociations_"
    "Trust Store URL",string,"URL of Trust Store with Certificates for DICOM nodes that are authorized to connect to this node; overrides dicomAuthorizedNodeCertificateReference","
    .. _dcmTrustStoreURL:

    dcmTrustStoreURL_"
    "Trust Store Type",string,"Key Store Type of Trust Store specified by dcmTrustStoreURL. Enumerated values: JKS or PKCS12","
    .. _dcmTrustStoreType:

    dcmTrustStoreType_"
    "Trust Store Pin",string,"Key Store Password of Trust Store specified by Trust Store URL","
    .. _dcmTrustStorePin:

    dcmTrustStorePin_"
    "Trust Store Pin Property",string,"System property of Key Store Password of Trust Store specified by Trust Store URL","
    .. _dcmTrustStorePinProperty:

    dcmTrustStorePinProperty_"
    "Key Store URL",string,"URL of Key Store with private Key and certificate used to identify this DICOM node in TLS connections","
    .. _dcmKeyStoreURL:

    dcmKeyStoreURL_"
    "Key Store Type",string,"Key Store Type of Key Store specified by Key Store URL. Enumerated values: JKS or PKCS12","
    .. _dcmKeyStoreType:

    dcmKeyStoreType_"
    "Key Store Pin",string,"Key Store Password of Key Store specified by Key Store URL","
    .. _dcmKeyStorePin:

    dcmKeyStorePin_"
    "Key Store Pin Property",string,"System property of Key Store Password of Key Store specified by Key Store URL","
    .. _dcmKeyStorePinProperty:

    dcmKeyStorePinProperty_"
    "Key Store Key Pin",string,"Key Password of Key Store specified by Key Store URL","
    .. _dcmKeyStoreKeyPin:

    dcmKeyStoreKeyPin_"
    "Key Store Key Pin Property",string,"System property of Key Password of Key Store specified by Key Store URL","
    .. _dcmKeyStoreKeyPinProperty:

    dcmKeyStoreKeyPinProperty_"
    "Time Zone of Device",string,"Time Zone ID of the Device; matches Java TimeZone ID","
    .. _dcmTimeZoneOfDevice:

    dcmTimeZoneOfDevice_"
