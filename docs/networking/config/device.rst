Device
======
DICOM Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Device Attributes (LDAP Object: dicomDevice)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomDeviceName:

    :ref:`Device Name <dicomDeviceName>`",string,"A unique name for this device

    (dicomDeviceName)"
    "
    .. _dicomDescription:

    :ref:`Device Description <dicomDescription>`",string,"Unconstrained text description of the device

    (dicomDescription)"
    "
    .. _dicomVendorData:

    :ref:`Vendor Device Data <dicomVendorData>`",boolean,"Device specific vendor configuration information

    (dicomVendorData)"
    "
    .. _dicomDeviceUID:

    :ref:`Device UID <dicomDeviceUID>`",string,"Unique identifier of the device

    (dicomDeviceUID)"
    "
    .. _dicomManufacturer:

    :ref:`Manufacturer <dicomManufacturer>`",string,"Manufacturer of the device. Default value of Manufacturer (0008,0070) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device.

    (dicomManufacturer)"
    "
    .. _dicomManufacturerModelName:

    :ref:`Manufacturer Model Name <dicomManufacturerModelName>`",string,"Manufacturer Model Name of the device. Default value of Manufacturer Model Name (0008,1090) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device.

    (dicomManufacturerModelName)"
    "
    .. _dicomSoftwareVersion:

    :ref:`Software Version(s) <dicomSoftwareVersion>`",string,"Software Versions of the device. Default values of Software Versions (0018,1020) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device.

    (dicomSoftwareVersion)"
    "
    .. _dicomStationName:

    :ref:`Station Name <dicomStationName>`",string,"Station Name of the device. Default value of Station Name (0008,1010) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device.

    (dicomStationName)"
    "
    .. _dicomDeviceSerialNumber:

    :ref:`Device Serial Number <dicomDeviceSerialNumber>`",string,"Device Serial Number of the device. Default value of Device Serial Number (0018,1000) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device.

    (dicomDeviceSerialNumber)"
    "
    .. _dicomPrimaryDeviceType:

    :ref:`Primary Device Type(s) <dicomPrimaryDeviceType>`",string,"Represents the kind of device and is most applicable for acquisition modalities Enumerated values: ARCHIVE, COMP, CAD, DSS, FILMD, M3D, MCD, PRINT, CAPTURE, LOG, RT, WSD, AR, BMD, BDUS, EPS, CR, CT, DX, ECG, ES, XC, GM, HD, IO, IVOCT, IVUS, KER, LEN, MR, MG, NM, OAM, OCT, OPM, OP, OPR, OPT, OPTBSV, OPTENF, OPV, OSS, PX, PT, RF, RG, SM, SRF, US, VA or XA.

    (dicomPrimaryDeviceType)"
    "
    .. _dicomInstitutionName:

    :ref:`Institution Name(s) <dicomInstitutionName>`",string,"Institution Name of the device. Default value of Institution Name (0008,0080) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device. Only the first configured value gets used by supplementing coercion, as the field is single-valued according to the `General Equipment Module Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_C.7-8>`_. Multi-valued possibility for this field here is to fulfill the requirement in `DICOM Part 15 - Security and System Management Profiles - LDAP Schema For Objects and Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_H.1.3>`_.

    (dicomInstitutionName)"
    "
    .. _dicomInstitutionCode:

    :ref:`Institution Code(s) <dicomInstitutionCode>`",string,"Institution Code of the device. Default value of Institution Code Sequence (0008,0082) in format (CV, CSD, ""CM"") on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device. Only the first configured value gets used by supplementing coercion, as the field is single-valued according to the `General Equipment Module Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_C.7-8>`_. Multi-valued possibility for this field here is to fulfill the requirement in `DICOM Part 15 - Security and System Management Profiles - LDAP Schema For Objects and Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_H.1.3>`_.

    (dicomInstitutionCode)"
    "
    .. _dicomInstitutionAddress:

    :ref:`Institution Address(s) <dicomInstitutionAddress>`",string,"Institution Address of the device. Default value of Institution Address (0008,0081) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device. Only the first configured value gets used by supplementing coercion, as the field is single-valued according to the `General Equipment Module Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_C.7-8>`_. Multi-valued possibility for this field here is to fulfill the requirement in `DICOM Part 15 - Security and System Management Profiles - LDAP Schema For Objects and Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_H.1.3>`_.

    (dicomInstitutionAddress)"
    "
    .. _dicomInstitutionDepartmentName:

    :ref:`Institution Department Name(s) <dicomInstitutionDepartmentName>`",string,"Institutional Department Name of the device. Default value of Institutional Department Name (0008,1040) on `invocation by archive attribute coercions on an archive device to supplement this attribute from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when it is missing in the SOP Instances created by the invoking archive device. Only the first configured value gets used by supplementing coercion, as the field is single-valued according to the `General Equipment Module Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_C.7-8>`_. Multi-valued possibility for this field here is to fulfill the requirement in `DICOM Part 15 - Security and System Management Profiles - LDAP Schema For Objects and Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_H.1.3>`_.

    (dicomInstitutionDepartmentName)"
    "
    .. _dicomIssuerOfPatientID:

    :ref:`Issuer of Patient ID <dicomIssuerOfPatientID>`",string,"Default value for the Issuer of Patient ID (0010,0021), and optionally also default values for the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Patient ID Qualifiers Sequence (0010,0024) for SOP Instances created by this device when Patient ID (0010,0020) is missing; may be overridden with values received in a worklist or other source. It is also used on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Patient ID (0010,0020) is missing : 

	 # on receive and creation of SOP instances by the invoking archive device

	 # on receive and creation of MPPS by the invoking archive device

	 # on DICOM (MWl) C-FIND requests from external systems to invoking archive device

	 # on DICOM (MWl) C-FIND requests from invoking archive device to external systems

	 # on DICOM (MWl) C-FIND responses from external systems to invoking archive device.

	Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomIssuerOfPatientID)"
    "
    .. _dicomIssuerOfAccessionNumber:

    :ref:`Issuer of Accession Number <dicomIssuerOfAccessionNumber>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Accession Number Sequence (0008,0051) for Modality Worklist items created or updated by this device when Accession Number (0008,0050) is missing; may be overridden with values received in a worklist or other source. It is also used on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Accession Number (0008,0050) is missing : 

	- within Request Attributes Sequence (0040,0275) item and root level attributes on receive and creation of SOP instances by the invoking archive device

	- within Scheduled Step Attributes Sequence (0040,0270) item and root level attributes on receive and creation of MPPS by the invoking archive device

	- within Request Attributes Sequence (0040,0275) item and root level attributes on DICOM (MWl) C-FIND requests from external systems to invoking archive device

	- within Request Attributes Sequence (0040,0275) item and root level attributes on DICOM (MWl) C-FIND requests from invoking archive device to external systems 

	- within Request Attributes Sequence (0040,0275) item and root level attributes on DICOM (MWl) C-FIND responses from external systems to invoking archive device. 

	Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomIssuerOfAccessionNumber)"
    "
    .. _dicomOrderPlacerIdentifier:

    :ref:`Order Placer Identifier <dicomOrderPlacerIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Order Placer Identifier Sequence (0040,0026) on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Placer Order Number / Imaging Service Request (0040,2016) is missing : 

	- within Request Attributes Sequence (0040,0275) item on receive and creation of SOP instances by the invoking archive device

	- within Scheduled Step Attributes Sequence (0040,0270) on receive and creation of MPPS by the invoking archive device

	- within Request Attributes Sequence (0040,0275) item on DICOM C-FIND / root level attributes on DICOM MWL C-FIND requests respectively, from external systems to invoking archive device

	- within Request Attributes Sequence (0040,0275) item on DICOM C-FIND / root level attributes on DICOM MWL C-FIND requests respectively, from invoking archive device to external systems 

	- within Request Attributes Sequence (0040,0275) item on DICOM C-FIND / root level attributes on DICOM MWL C-FIND responses respectively, from external systems to invoking archive device. 

	May be overridden by the values received in a worklist or other source. Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomOrderPlacerIdentifier)"
    "
    .. _dicomOrderFillerIdentifier:

    :ref:`Order Filler Identifier <dicomOrderFillerIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Order Filler Identifier Sequence (0040,0027) on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Filler Order Number / Imaging Service Request (0040,2017) is missing : 

	- within Request Attributes Sequence (0040,0275) item on receive and creation of SOP instances by the invoking archive device

	- within Scheduled Step Attributes Sequence (0040,0270) on receive and creation of MPPS by the invoking archive device

	- within Request Attributes Sequence (0040,0275) item on DICOM C-FIND / root level attributes on DICOM MWL C-FIND requests respectively, from external systems to invoking archive device

	- within Request Attributes Sequence (0040,0275) item on DICOM C-FIND / root level attributes on DICOM MWL C-FIND requests respectively, from invoking archive device to external systems 

	- within Request Attributes Sequence (0040,0275) item on DICOM C-FIND / root level attributes on DICOM MWL C-FIND responses respectively, from external systems to invoking archive device. 

	May be overridden by the values received in a worklist or other source. Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomOrderFillerIdentifier)"
    "
    .. _dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID <dicomIssuerOfAdmissionID>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Admission ID (0038,0010) is missing : 

	- on receive and creation of SOP instances by the invoking archive device

	- on receive and creation of MPPS by the invoking archive device

	- on DICOM (MWl) C-FIND requests from external systems to invoking archive device

	- on DICOM (MWl) C-FIND requests from invoking archive device to external systems 

	- on DICOM (MWl) C-FIND responses from external systems to invoking archive device. 

	May be overridden by the values received in a worklist or other source. Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomIssuerOfAdmissionID)"
    "
    .. _dicomIssuerOfServiceEpisodeID:

    :ref:`Issuer of Service Episode ID <dicomIssuerOfServiceEpisodeID>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Service Episode ID Sequence (0038,0064) on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Service Episode ID (0038,0060) is missing : 

	- on receive and creation of SOP instances by the invoking archive device

	- on receive and creation of MPPS by the invoking archive device

	- on DICOM (MWl) C-FIND requests from external systems to invoking archive device

	- on DICOM (MWl) C-FIND requests from invoking archive device to external systems 

	- on DICOM (MWl) C-FIND responses from external systems to invoking archive device. 

	May be overridden by the values received in a worklist or other source. Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomIssuerOfServiceEpisodeID)"
    "
    .. _dicomIssuerOfContainerIdentifier:

    :ref:`Issuer of Container Identifier <dicomIssuerOfContainerIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Container Identifier Sequence (0040,0513) on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Container Identifier (0040,0512) is missing : 

	- on receive and creation of SOP instances by the invoking archive device

	- on receive and creation of MPPS by the invoking archive device

	- on DICOM (MWl) C-FIND requests from external systems to invoking archive device

	- on DICOM (MWl) C-FIND requests from invoking archive device to external systems 

	- on DICOM (MWl) C-FIND responses from external systems to invoking archive device. 

	May be overridden by the values received in a worklist or other source. Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomIssuerOfContainerIdentifier)"
    "
    .. _dicomIssuerOfSpecimenIdentifier:

    :ref:`Issuer of Specimen Identifier <dicomIssuerOfSpecimenIdentifier>`",string,"Default values for the Local Namespace Entity ID (0040,0031), the Universal Entity ID (0040,0032) and the Universal Entity ID Type (0040,0033) of the Item of the Issuer of Specimen Identifier Sequence (0040,0562) on `invocation by archive attribute coercions on an archive device to supplement from this device <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Supplement-Dataset-Attributes-from-Device#overview>`_ when assigning authority of Specimen Identifier (0040,0551) is missing : 

	- on receive and creation of SOP instances by the invoking archive device

	- on receive and creation of MPPS by the invoking archive device

	- on DICOM (MWl) C-FIND requests from external systems to invoking archive device

	- on DICOM (MWl) C-FIND requests from invoking archive device to external systems 

	- on DICOM (MWl) C-FIND responses from external systems to invoking archive device. 

	May be overridden by the values received in a worklist or other source. Format: {LocalNamespaceEntityID}[&{UniversalEntityID}&{UniversalEntityIDType}]

    (dicomIssuerOfSpecimenIdentifier)"
    "
    .. _dicomAuthorizedNodeCertificateReference:

    :ref:`Authorized Node Certificate Reference(s) <dicomAuthorizedNodeCertificateReference>`",string,"The DNs for the certificates of nodes that are authorized to connect to this device

    (dicomAuthorizedNodeCertificateReference)"
    "
    .. _dicomThisNodeCertificateReference:

    :ref:`This Node Certificate Reference(s) <dicomThisNodeCertificateReference>`",string,"The DNs of the public certificate(s) for this node

    (dicomThisNodeCertificateReference)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"Boolean to indicate whether this device is presently installed on the network

    (dicomInstalled)"
    ":doc:`networkConnection` (s)",object,"network connections of the device"
    ":doc:`networkAE` (s)",object,"Application entity provided by the device"
    ":doc:`dcmDevice` ",object,"dcm4che proprietary Device Attributes"

.. toctree::

    networkConnection
    networkAE
    dcmDevice
