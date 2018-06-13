Device Extension
================
dcm4che proprietary Device Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Device Extension Attributes (LDAP Object: dcmDcmDevice)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmLimitOpenAssociations:

    :ref:`Limit Open Associations (dcmLimitOpenAssociations) <dcmLimitOpenAssociations>`",integer,"Limit open DICOM connections; rejects Association requests if the limit is exceeded. 0 = unlimited."
    "
    .. _dcmTrustStoreURL:

    :ref:`Trust Store URL (dcmTrustStoreURL) <dcmTrustStoreURL>`",string,"URL of Trust Store with Certificates for DICOM nodes that are authorized to connect to this node; overrides dicomAuthorizedNodeCertificateReference"
    "
    .. _dcmTrustStoreType:

    :ref:`Trust Store Type (dcmTrustStoreType) <dcmTrustStoreType>`",string,"Key Store Type of Trust Store specified by dcmTrustStoreURL. Enumerated values: JKS or PKCS12"
    "
    .. _dcmTrustStorePin:

    :ref:`Trust Store Pin (dcmTrustStorePin) <dcmTrustStorePin>`",string,"Key Store Password of Trust Store specified by Trust Store URL"
    "
    .. _dcmTrustStorePinProperty:

    :ref:`Trust Store Pin Property (dcmTrustStorePinProperty) <dcmTrustStorePinProperty>`",string,"System property of Key Store Password of Trust Store specified by Trust Store URL"
    "
    .. _dcmKeyStoreURL:

    :ref:`Key Store URL (dcmKeyStoreURL) <dcmKeyStoreURL>`",string,"URL of Key Store with private Key and certificate used to identify this DICOM node in TLS connections"
    "
    .. _dcmKeyStoreType:

    :ref:`Key Store Type (dcmKeyStoreType) <dcmKeyStoreType>`",string,"Key Store Type of Key Store specified by Key Store URL. Enumerated values: JKS or PKCS12"
    "
    .. _dcmKeyStorePin:

    :ref:`Key Store Pin (dcmKeyStorePin) <dcmKeyStorePin>`",string,"Key Store Password of Key Store specified by Key Store URL"
    "
    .. _dcmKeyStorePinProperty:

    :ref:`Key Store Pin Property (dcmKeyStorePinProperty) <dcmKeyStorePinProperty>`",string,"System property of Key Store Password of Key Store specified by Key Store URL"
    "
    .. _dcmKeyStoreKeyPin:

    :ref:`Key Store Key Pin (dcmKeyStoreKeyPin) <dcmKeyStoreKeyPin>`",string,"Key Password of Key Store specified by Key Store URL"
    "
    .. _dcmKeyStoreKeyPinProperty:

    :ref:`Key Store Key Pin Property (dcmKeyStoreKeyPinProperty) <dcmKeyStoreKeyPinProperty>`",string,"System property of Key Password of Key Store specified by Key Store URL"
    "
    .. _dcmTimeZoneOfDevice:

    :ref:`Time Zone of Device (dcmTimeZoneOfDevice) <dcmTimeZoneOfDevice>`",string,"Time Zone ID of the Device; matches Java TimeZone ID"
    ":doc:`webApplication` (s)",object,"Web Applications provided by the Device"
    ":doc:`hl7Application` (s)",object,"HL7 Applications provided by the Device"
    ":doc:`imageWriter` (s)",object,"Specifies Java Image IO Image Writers with Write Parameters used for compressing DICOM images"
    ":doc:`imageReader` (s)",object,"Specifies Java Image IO Image Readers used for decompressing compressed DICOM images"
    ":doc:`auditLogger` (s)",object,"Audit Logger related information"
    ":doc:`auditRecordRepository` ",object,"Audit Record Repository related information"
    ":doc:`archiveDevice` ",object,"DICOM Archive Device related information"
    ":doc:`uiConfig` (s)",object,"UI Configuration"

.. toctree::

    webApplication
    hl7Application
    imageWriter
    imageReader
    auditLogger
    auditRecordRepository
    archiveDevice
    uiConfig
