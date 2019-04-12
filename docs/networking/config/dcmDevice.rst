Device Extension
================
dcm4che proprietary Device Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Device Extension Attributes (LDAP Object: dcmDevice)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmLimitOpenAssociations:

    :ref:`Association Limit <dcmLimitOpenAssociations>`",integer,"Maximal number of open DICOM connections; rejects Association requests if the limit is exceeded; 0 = unlimited.

    (dcmLimitOpenAssociations)"
    "
    .. _dcmLimitAssociationsInitiatedBy:

    :ref:`Association Limit for AE(s) <dcmLimitAssociationsInitiatedBy>`",string,"Maximal number of open DICOM connections initiated by a particular Application Entity (AE) in format <ae-title>=<number>; rejects Association requests from that AE if the limit is exceeded.

    (dcmLimitAssociationsInitiatedBy)"
    "
    .. _dcmTrustStoreURL:

    :ref:`Trust Store URL <dcmTrustStoreURL>`",string,"URL of Trust Store with Certificates for DICOM nodes that are authorized to connect to this node; overrides dicomAuthorizedNodeCertificateReference

    (dcmTrustStoreURL)"
    "
    .. _dcmTrustStoreType:

    :ref:`Trust Store Type <dcmTrustStoreType>`",string,"Key Store Type of Trust Store specified by dcmTrustStoreURL. Enumerated values: JKS or PKCS12.

    (dcmTrustStoreType)"
    "
    .. _dcmTrustStorePin:

    :ref:`Trust Store Pin <dcmTrustStorePin>`",string,"Key Store Password of Trust Store specified by Trust Store URL

    (dcmTrustStorePin)"
    "
    .. _dcmTrustStorePinProperty:

    :ref:`Trust Store Pin Property <dcmTrustStorePinProperty>`",string,"System property of Key Store Password of Trust Store specified by Trust Store URL

    (dcmTrustStorePinProperty)"
    "
    .. _dcmKeyStoreURL:

    :ref:`Key Store URL <dcmKeyStoreURL>`",string,"URL of Key Store with private Key and certificate used to identify this DICOM node in TLS connections

    (dcmKeyStoreURL)"
    "
    .. _dcmKeyStoreType:

    :ref:`Key Store Type <dcmKeyStoreType>`",string,"Key Store Type of Key Store specified by Key Store URL. Enumerated values: JKS or PKCS12.

    (dcmKeyStoreType)"
    "
    .. _dcmKeyStorePin:

    :ref:`Key Store Pin <dcmKeyStorePin>`",string,"Key Store Password of Key Store specified by Key Store URL

    (dcmKeyStorePin)"
    "
    .. _dcmKeyStorePinProperty:

    :ref:`Key Store Pin Property <dcmKeyStorePinProperty>`",string,"System property of Key Store Password of Key Store specified by Key Store URL

    (dcmKeyStorePinProperty)"
    "
    .. _dcmKeyStoreKeyPin:

    :ref:`Key Store Key Pin <dcmKeyStoreKeyPin>`",string,"Key Password of Key Store specified by Key Store URL

    (dcmKeyStoreKeyPin)"
    "
    .. _dcmKeyStoreKeyPinProperty:

    :ref:`Key Store Key Pin Property <dcmKeyStoreKeyPinProperty>`",string,"System property of Key Password of Key Store specified by Key Store URL

    (dcmKeyStoreKeyPinProperty)"
    "
    .. _dcmTimeZoneOfDevice:

    :ref:`Time Zone of Device <dcmTimeZoneOfDevice>`",string,"Time Zone ID of the Device; matches Java TimeZone ID

    (dcmTimeZoneOfDevice)"
    ":doc:`webApplication` (s)",object,"Web Applications provided by the Device"
    ":doc:`keycloakClient` (s)",object,"Keycloak Clients provided by the Device"
    ":doc:`hl7Application` (s)",object,"HL7 Applications provided by the Device"
    ":doc:`imageWriter` (s)",object,"Specifies Java Image IO Image Writers with Write Parameters used for compressing DICOM images"
    ":doc:`imageReader` (s)",object,"Specifies Java Image IO Image Readers used for decompressing compressed DICOM images"
    ":doc:`auditLogger` (s)",object,"Audit Logger related information"
    ":doc:`auditRecordRepository` ",object,"Audit Record Repository related information"
    ":doc:`archiveDevice` ",object,"DICOM Archive Device related information"
    ":doc:`uiConfig` (s)",object,"UI Configuration"

.. toctree::

    webApplication
    keycloakClient
    hl7Application
    imageWriter
    imageReader
    auditLogger
    auditRecordRepository
    archiveDevice
    uiConfig
