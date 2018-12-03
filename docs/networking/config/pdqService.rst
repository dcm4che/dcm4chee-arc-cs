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

    :ref:`PDQ Service URI <dcmURI>`",string,"PDQ Service URI, e.g. 'pdq-dicom:FINDSCP'.

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
    .. _dcmDefaultCharacterSet:

    :ref:`Default Character Set <dcmDefaultCharacterSet>`",string,"Value of Specific Character Set (0008,0005) added to Data Sets without Specific Character Set (0008,0005) attribute received from the C-FIND SCP. Only effective for DICOM PDQ Services (URI: pdq-dicom:{AETitle}).

    (dcmDefaultCharacterSet)"
    "
    .. _dcmProperty:

    :ref:`PDQ Service Property(s) <dcmProperty>`",string,"Property in format <name>=<value>, e.g. 'LocalAET=DCM4CHEE'

    (dcmProperty)"
