Device
======
DICOM Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Device Attributes (LDAP Object: dcmDevice)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Device Name",string,"A unique name for this device","
    .. _dicomDeviceName:

    dicomDeviceName_"
    "Device Description",string,"Unconstrained text description of the device","
    .. _dicomDescription:

    dicomDescription_"
    "Vendor Device Data",boolean,"Device specific vendor configuration information","
    .. _dicomVendorData:

    dicomVendorData_"
    "Device UID",string,"Unique identifier of the device","
    .. _dicomDeviceUID:

    dicomDeviceUID_"
    "Manufacturer",string,"Should be the same as the value of Manufacturer (0008,0070) in SOP instances created by this device","
    .. _dicomManufacturer:

    dicomManufacturer_"
    "Manufacturer Model Name",string,"Should be the same as the value of Manufacturer Model Name (0008,1090) in SOP instances created by this device","
    .. _dicomManufacturerModelName:

    dicomManufacturerModelName_"
    "Software Version(s)",string,"Should be the same as the values of Software Versions (0018,1020) in SOP instances created by this device","
    .. _dicomSoftwareVersion:

    dicomSoftwareVersion_"
    "Station Name",string,"Should be the same as the value of Station Name (0008,1010) in SOP instances created by this device","
    .. _dicomStationName:

    dicomStationName_"
    "Device Serial Number",string,"Should be the same as the value of Device Serial Number (0018,1000) in SOP instances created by this device","
    .. _dicomDeviceSerialNumber:

    dicomDeviceSerialNumber_"
    "Primary Device Type(s)",string,"Represents the kind of device and is most applicable for acquisition modalities","
    .. _dicomPrimaryDeviceType:

    dicomPrimaryDeviceType_"
    "Institution Name(s)",string,"Should be the same as the value of Institution Name (0008,0080) in SOP Instances created by this device","
    .. _dicomInstitutionName:

    dicomInstitutionName_"
    "Institution Code(s)",string,"Institution Code(s) in format (CV, CSD, ""CM"")","
    .. _dicomInstitutionCode:

    dicomInstitutionCode_"
    "Institution Address(s)",string,"Should be the same as the value of Institution Address (0008,0081) attribute in SOP Instances created by this device","
    .. _dicomInstitutionAddress:

    dicomInstitutionAddress_"
    "Institution Department Name(s)",string,"Should be the same as the value of Institutional Department Name (0008,1040) in SOP Instances created by this device","
    .. _dicomInstitutionDepartmentName:

    dicomInstitutionDepartmentName_"
    "Issuer of Patient ID",string,"Default value for the Issuer of Patient ID (0010,0021), and optionally also default values for the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Patient ID Qualifiers Sequence (0010,0024) for SOP Instances created or queried by this device. Format: <Issuer of Patient ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomIssuerOfPatientID:

    dicomIssuerOfPatientID_"
    "Issuer of Accession Number",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Accession Number Sequence (0008,0051) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomIssuerOfAccessionNumber:

    dicomIssuerOfAccessionNumber_"
    "Order Placer Identifier",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Order Placer Identifier Sequence (0040,0026) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomOrderPlacerIdentifier:

    dicomOrderPlacerIdentifier_"
    "Order Filler Identifier",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Order Filler Identifier Sequence (0040,0027) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomOrderFillerIdentifier:

    dicomOrderFillerIdentifier_"
    "Issuer of Admission ID",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomIssuerOfAdmissionID:

    dicomIssuerOfAdmissionID_"
    "Issuer of Service Episode ID",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Service Episode ID Sequence (0038,0064) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomIssuerOfServiceEpisodeID:

    dicomIssuerOfServiceEpisodeID_"
    "Issuer of Container Identifier",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Container Identifier Sequence (0040,0513) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomIssuerOfContainerIdentifier:

    dicomIssuerOfContainerIdentifier_"
    "Issuer of Specimen Identifier",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Specimen Identifier Sequence (0040,0562) for SOP Instances created or queried by this device. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]","
    .. _dicomIssuerOfSpecimenIdentifier:

    dicomIssuerOfSpecimenIdentifier_"
    "Authorized Node Certificate Reference(s)",string,"The DNs for the certificates of nodes that are authorized to connect to this device","
    .. _dicomAuthorizedNodeCertificateReference:

    dicomAuthorizedNodeCertificateReference_"
    "This Node Certificate Reference(s)",string,"The DNs of the public certificate(s) for this node","
    .. _dicomThisNodeCertificateReference:

    dicomThisNodeCertificateReference_"
    "installed",boolean,"Boolean to indicate whether this device is presently installed on the network","
    .. _dicomInstalled:

    dicomInstalled_"
    ":doc:`networkConnection` (s)",object,"network connections of the device","
    .. _dicomNetworkConnection:

    dicomNetworkConnection_"
    ":doc:`networkAE` (s)",object,"Application entity provided by the device","
    .. _dicomNetworkAE:

    dicomNetworkAE_"
    ":doc:`dcmDevice` ",object,"dcm4che proprietary Device Attributes","
    .. _dcmDevice:

    dcmDevice_"

.. toctree::

    networkConnection
    networkAE
    dcmDevice
