Exporter Descriptor
===================
Exporter Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Exporter Descriptor Attributes (LDAP Object: dcmExporter)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmExporterID:

    :ref:`Exporter ID <dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmURI:

    :ref:`URI <dcmURI>`",string,"RFC2079: Uniform Resource Identifier

    (dcmURI)"
    "
    .. _dcmQueueName:

    :ref:`Queue Name <dcmQueueName>`",string,"JMS Queue Name Enumerated values: Export1, Export2, Export3, Export4, Export5, Export6, Export7, Export8, Export9 or Export10.

    (dcmQueueName)"
    "
    .. _dcmExportPriority:

    :ref:`Export Priority <dcmExportPriority>`",integer,"JMS Priority Level for processing the Export Task from 0 (lowest) to 9 (highest).

    (dcmExportPriority)"
    "
    .. _dicomDescription:

    :ref:`Exporter Description <dicomDescription>`",string,"Unconstrained text description of the exporter

    (dicomDescription)"
    "
    .. _dicomAETitle:

    :ref:`Application Entity (AE) title <dicomAETitle>`",string,"Application Entity (AE) title

    (dicomAETitle)"
    "
    .. _dcmDeleteStudyFromStorageID:

    :ref:`Delete Study From Storage ID <dcmDeleteStudyFromStorageID>`",string,"ID of Storage System from which the objects of the exported Study shall be deleted. Only effective for Export Tasks on Study level.

    (dcmDeleteStudyFromStorageID)"
    "
    .. _dcmRejectForDataRetentionExpiry:

    :ref:`Reject Entity for Data Retention Expiry <dcmRejectForDataRetentionExpiry>`",boolean,"Reject entity for Data Retention Expiry after export on completion of Export Task.

    (dcmRejectForDataRetentionExpiry)"
    "
    .. _dcmStgCmtSCP:

    :ref:`Storage Commitment SCP AE Title <dcmStgCmtSCP>`",string,"AE Title of external Storage Commitment SCP used to verify export to another archive.

    (dcmStgCmtSCP)"
    "
    .. _dcmIanDestination:

    :ref:`Ian Destination(s) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ

    (dcmIanDestination)"
    "
    .. _dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) <dcmRetrieveAET>`",string,"AE Title associated with Network AE

    (dcmRetrieveAET)"
    "
    .. _dcmRetrieveLocationUID:

    :ref:`Retrieve Location UID <dcmRetrieveLocationUID>`",string,"Retrieve Location UID.

    (dcmRetrieveLocationUID)"
    "
    .. _dcmInstanceAvailability:

    :ref:`Instance Availability <dcmInstanceAvailability>`",string,"Instance Availability. Enumerated values: ONLINE, NEARLINE or OFFLINE.

    (dcmInstanceAvailability)"
    "
    .. _dcmSchedule:

    :ref:`Export Schedule(s) <dcmSchedule>`",string,"Delay export to specified time periods. If no Export Schedule is specified, queue the export task for processing immediately. Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
    "
    .. _dcmProperty:

    :ref:`Property(s) <dcmProperty>`",string,"Property in format <name>=<value>

    (dcmProperty)"
