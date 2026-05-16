Device Extension
================
dcm4che proprietary Device Attributes

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Device Extension Attributes (LDAP Object: dcmDevice)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmRoleSelectionNegotiationLenient:
    .. _dcmDevice-dcmRoleSelectionNegotiationLenient:

    :ref:`Role Selection Negotiation Lenient <dcmDevice-dcmRoleSelectionNegotiationLenient>`",boolean,"Indicates to disable check for required SCP/SCU role selection negotiation on sending of DIMSE-RQs. May be overwritten by configured value for particular Network AEs.

    (dcmRoleSelectionNegotiationLenient)"
    "
    .. _dcmLimitOpenAssociations:
    .. _dcmDevice-dcmLimitOpenAssociations:

    :ref:`Association Limit <dcmDevice-dcmLimitOpenAssociations>`",integer,"Maximal number of open DICOM connections; rejects Association requests if the limit is exceeded; 0 = unlimited.

    (dcmLimitOpenAssociations)"
    "
    .. _dcmLimitAssociationsInitiatedBy:
    .. _dcmDevice-dcmLimitAssociationsInitiatedBy:

    :ref:`Association Limit for AE(s) <dcmDevice-dcmLimitAssociationsInitiatedBy>`",string,"Maximal number of open DICOM connections initiated by a particular Application Entity (AE) in format <ae-title>=<number>; rejects Association requests from that AE if the limit is exceeded.

    (dcmLimitAssociationsInitiatedBy)"
    "
    .. _dcmTrustStoreURL:
    .. _dcmDevice-dcmTrustStoreURL:

    :ref:`Trust Store URL <dcmDevice-dcmTrustStoreURL>`",string,"URL of Trust Store with Certificates for DICOM nodes that are authorized to connect to this node; overrides dicomAuthorizedNodeCertificateReference

    (dcmTrustStoreURL)"
    "
    .. _dcmTrustStoreType:
    .. _dcmDevice-dcmTrustStoreType:

    :ref:`Trust Store Type <dcmDevice-dcmTrustStoreType>`",string,"Key Store Type of Trust Store specified by dcmTrustStoreURL.

    Enumerated values:

    JKS (= Java KeyStore)

    PKCS12 (= Public-Key Cryptography Standards #12)

    (dcmTrustStoreType)"
    "
    .. _dcmTrustStorePin:
    .. _dcmDevice-dcmTrustStorePin:

    :ref:`Trust Store Pin <dcmDevice-dcmTrustStorePin>`",string,"Key Store Password of Trust Store specified by Trust Store URL

    (dcmTrustStorePin)"
    "
    .. _dcmTrustStorePinProperty:
    .. _dcmDevice-dcmTrustStorePinProperty:

    :ref:`Trust Store Pin Property <dcmDevice-dcmTrustStorePinProperty>`",string,"System property of Key Store Password of Trust Store specified by Trust Store URL

    (dcmTrustStorePinProperty)"
    "
    .. _dcmKeyStoreURL:
    .. _dcmDevice-dcmKeyStoreURL:

    :ref:`Key Store URL <dcmDevice-dcmKeyStoreURL>`",string,"URL of Key Store with private Key and certificate used to identify this DICOM node in TLS connections

    (dcmKeyStoreURL)"
    "
    .. _dcmKeyStoreType:
    .. _dcmDevice-dcmKeyStoreType:

    :ref:`Key Store Type <dcmDevice-dcmKeyStoreType>`",string,"Key Store Type of Key Store specified by Key Store URL.

    Enumerated values:

    JKS (= Java KeyStore)

    PKCS12 (= Public-Key Cryptography Standards #12)

    (dcmKeyStoreType)"
    "
    .. _dcmKeyStorePin:
    .. _dcmDevice-dcmKeyStorePin:

    :ref:`Key Store Pin <dcmDevice-dcmKeyStorePin>`",string,"Key Store Password of Key Store specified by Key Store URL

    (dcmKeyStorePin)"
    "
    .. _dcmKeyStorePinProperty:
    .. _dcmDevice-dcmKeyStorePinProperty:

    :ref:`Key Store Pin Property <dcmDevice-dcmKeyStorePinProperty>`",string,"System property of Key Store Password of Key Store specified by Key Store URL

    (dcmKeyStorePinProperty)"
    "
    .. _dcmKeyStoreKeyPin:
    .. _dcmDevice-dcmKeyStoreKeyPin:

    :ref:`Key Store Key Pin <dcmDevice-dcmKeyStoreKeyPin>`",string,"Key Password of Key Store specified by Key Store URL

    (dcmKeyStoreKeyPin)"
    "
    .. _dcmKeyStoreKeyPinProperty:
    .. _dcmDevice-dcmKeyStoreKeyPinProperty:

    :ref:`Key Store Key Pin Property <dcmDevice-dcmKeyStoreKeyPinProperty>`",string,"System property of Key Password of Key Store specified by Key Store URL

    (dcmKeyStoreKeyPinProperty)"
    "
    .. _dcmTimeZoneOfDevice:
    .. _dcmDevice-dcmTimeZoneOfDevice:

    :ref:`Time Zone of Device <dcmDevice-dcmTimeZoneOfDevice>`",string,"Time Zone ID of the Device; matches Java TimeZone ID

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
