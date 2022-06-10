PDQ Service
===========
PDQ Service Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: PDQ Service Attributes (LDAP Object: dcmPdqService)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmPDQServiceID:

    :ref:`PDQ Service ID <dcmPDQServiceID>`",string,"PDQ Service ID

    (dcmPDQServiceID)"
    "
    .. _dcmURI:

    :ref:`PDQ Service URI <dcmURI>`",string,"PDQ Service URI, e.g. 'pdq-dicom:FINDSCP' or 'pdq-hl7:SendingApplication/SendingFacility:ReceivingApplication/ReceivingFacility' or pdq-fhir:HL7-FHIR-R4-WebApplication.

    (dcmURI)"
    "
    .. _dicomDescription:

    :ref:`PDQ Service Description <dicomDescription>`",string,"Unconstrained text description of the PDQ Service

    (dicomDescription)"
    "
    .. _dcmTag:

    :ref:`Patient Attributes(s) <dcmTag>`",string,"Queried Patient Attributes - if not specified all available Patient attributes will be queried. Only applicable for 'pdq-dicom' PDQ Service

    (dcmTag)"
    "
    .. _dcmEntity:

    :ref:`Query Entity <dcmEntity>`",string,"Indicates if the C-FIND SCP is queried for a particular Patient or for Studies of a particular Patient. Only effective for DICOM PDQ Services (URI: pdq-dicom:{AETitle}). Enumerated values: Patient or Study.

    (dcmEntity)"
    "
    .. _dcmProperty:

    :ref:`PDQ Service Property(s) <dcmProperty>`",string,"Property in format <name>=<value>, e.g. 'LocalAET=DCM4CHEE' for URI with schema pdq-dicom or 'XSLStylesheetURI=${jboss.server.temp.url}/dcm4chee-arc/hl7-adt2dcm.xsl' for URI with schema pdq-hl7 or 'XSLStylesheetURI=${jboss.server.temp.url}/dcm4chee-arc/fhir-pat2dcm.xsl' for URI with schema pdq-fhir. Additional properties for URI with schema pdq-fhir may be set eg. 'search._format=xml', 'search.identifier.system={issuer}'. For complete list of properties, refer https://github.com/dcm4che/dcm4chee-arc-light/issues/3307

    (dcmProperty)"
