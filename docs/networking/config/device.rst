Device
======
DICOM Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Device Attributes (LDAP Object: dcmDevice)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dicomDeviceName:

    :ref:`Device Name (dicomDeviceName) <dicomDeviceName>`",string,"A unique name for this device"
    "
    .. _dicomDescription:

    :ref:`Device Description (dicomDescription) <dicomDescription>`",string,"Unconstrained text description of the device"
    "
    .. _dicomVendorData:

    :ref:`Vendor Device Data (dicomVendorData) <dicomVendorData>`",boolean,"Device specific vendor configuration information"
    "
    .. _dicomDeviceUID:

    :ref:`Device UID (dicomDeviceUID) <dicomDeviceUID>`",string,"Unique identifier of the device"
    "
    .. _dicomManufacturer:

    :ref:`Manufacturer (dicomManufacturer) <dicomManufacturer>`",string,"Should be the same as the value of Manufacturer (0008,0070) in SOP instances created by this device"
    "
    .. _dicomManufacturerModelName:

    :ref:`Manufacturer Model Name (dicomManufacturerModelName) <dicomManufacturerModelName>`",string,"Should be the same as the value of Manufacturer Model Name (0008,1090) in SOP instances created by this device"
    "
    .. _dicomSoftwareVersion:

    :ref:`Software Version(s) (dicomSoftwareVersion) <dicomSoftwareVersion>`",string,"Should be the same as the values of Software Versions (0018,1020) in SOP instances created by this device"
    "
    .. _dicomStationName:

    :ref:`Station Name (dicomStationName) <dicomStationName>`",string,"Should be the same as the value of Station Name (0008,1010) in SOP instances created by this device"
    "
    .. _dicomDeviceSerialNumber:

    :ref:`Device Serial Number (dicomDeviceSerialNumber) <dicomDeviceSerialNumber>`",string,"Should be the same as the value of Device Serial Number (0018,1000) in SOP instances created by this device"
    "
    .. _dicomPrimaryDeviceType:

    :ref:`Primary Device Type(s) (dicomPrimaryDeviceType) <dicomPrimaryDeviceType>`",string,"Represents the kind of device and is most applicable for acquisition modalities"
    "
    .. _dicomInstitutionName:

    :ref:`Institution Name(s) (dicomInstitutionName) <dicomInstitutionName>`",string,"Should be the same as the value of Institution Name (0008,0080) in SOP Instances created by this device"
    "
    .. _dicomInstitutionCode:

    :ref:`Institution Code(s) (dicomInstitutionCode) <dicomInstitutionCode>`",string,"Institution Code(s) in format (CV, CSD, ""CM"")"
    "
    .. _dicomInstitutionAddress:

    :ref:`Institution Address(s) (dicomInstitutionAddress) <dicomInstitutionAddress>`",string,"Should be the same as the value of Institution Address (0008,0081) attribute in SOP Instances created by this device"
    "
    .. _dicomInstitutionDepartmentName:

    :ref:`Institution Department Name(s) (dicomInstitutionDepartmentName) <dicomInstitutionDepartmentName>`",string,"Should be the same as the value of Institutional Department Name (0008,1040) in SOP Instances created by this device"
    "
    .. _dicomIssuerOfPatientID:

    :ref:`Issuer of Patient ID (dicomIssuerOfPatientID) <dicomIssuerOfPatientID>`",string,"Default value for the Issuer of Patient ID (0010,0021), and optionally also default values for the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Patient ID Qualifiers Sequence (0010,0024) for SOP Instances created or queried by this device. Format: <Issuer of Patient ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomIssuerOfAccessionNumber:

    :ref:`Issuer of Accession Number (dicomIssuerOfAccessionNumber) <dicomIssuerOfAccessionNumber>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Accession Number Sequence (0008,0051) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomOrderPlacerIdentifier:

    :ref:`Order Placer Identifier (dicomOrderPlacerIdentifier) <dicomOrderPlacerIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Order Placer Identifier Sequence (0040,0026) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomOrderFillerIdentifier:

    :ref:`Order Filler Identifier (dicomOrderFillerIdentifier) <dicomOrderFillerIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Order Filler Identifier Sequence (0040,0027) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID (dicomIssuerOfAdmissionID) <dicomIssuerOfAdmissionID>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomIssuerOfServiceEpisodeID:

    :ref:`Issuer of Service Episode ID (dicomIssuerOfServiceEpisodeID) <dicomIssuerOfServiceEpisodeID>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Service Episode ID Sequence (0038,0064) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomIssuerOfContainerIdentifier:

    :ref:`Issuer of Container Identifier (dicomIssuerOfContainerIdentifier) <dicomIssuerOfContainerIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Container Identifier Sequence (0040,0513) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomIssuerOfSpecimenIdentifier:

    :ref:`Issuer of Specimen Identifier (dicomIssuerOfSpecimenIdentifier) <dicomIssuerOfSpecimenIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Specimen Identifier Sequence (0040,0562) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]"
    "
    .. _dicomAuthorizedNodeCertificateReference:

    :ref:`Authorized Node Certificate Reference(s) (dicomAuthorizedNodeCertificateReference) <dicomAuthorizedNodeCertificateReference>`",string,"The DNs for the certificates of nodes that are authorized to connect to this device"
    "
    .. _dicomThisNodeCertificateReference:

    :ref:`This Node Certificate Reference(s) (dicomThisNodeCertificateReference) <dicomThisNodeCertificateReference>`",string,"The DNs of the public certificate(s) for this node"
    "
    .. _dicomInstalled:

    :ref:`installed (dicomInstalled) <dicomInstalled>`",boolean,"Boolean to indicate whether this device is presently installed on the network"
    ":doc:`networkConnection` (s)",object,"network connections of the device"
    ":doc:`networkAE` (s)",object,"Application entity provided by the device"
    ":doc:`dcmDevice` ",object,"dcm4che proprietary Device Attributes"

.. toctree::

    networkConnection
    networkAE
    dcmDevice
