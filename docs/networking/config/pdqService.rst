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

    :ref:`PDQ Service URI <dcmURI>`",string,"PDQ Service URI, e.g. 'pdq-dicom:FINDSCP' or 'pdq-hl7:SendingApplication/SendingFacility:ReceivingApplication/ReceivingFacility'.

    (dcmURI)"
    "
    .. _dicomDescription:

    :ref:`PDQ Service Description <dicomDescription>`",string,"Unconstrained text description of the PDQ Service

    (dicomDescription)"
    "
    .. _dcmTag:

    :ref:`Patient Attributes(s) <dcmTag>`",string,"Queried Patient Attributes - if not specified all available Patient attributes will be queried

    (dcmTag)"
    "
    .. _dcmEntity:

    :ref:`Query Entity <dcmEntity>`",string,"Indicates if the C-FIND SCP is queried for a particular Patient or for Studies of a particular Patient. Only effective for DICOM PDQ Services (URI: pdq-dicom:{AETitle}). Enumerated values: Patient or Study.

    (dcmEntity)"
    "
    .. _dcmProperty:

    :ref:`PDQ Service Property(s) <dcmProperty>`",string,"Property in format <name>=<value>, e.g. 'LocalAET=DCM4CHEE' or 'XSLStylesheetURI=${jboss.server.temp.url}/dcm4chee-arc/hl7-adt2dcm.xsl'

    (dcmProperty)"
