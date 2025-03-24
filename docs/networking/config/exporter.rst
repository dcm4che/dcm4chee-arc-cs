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

    :ref:`Exporter URI <dcmURI>`",string,"RFC2079: Uniform Resource Identifier. Refer various `Exporter URI <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Exporter-Properties>`_ that can be configured based on the exporter type.

    (dcmURI)"
    "
    .. _dcmQueueName:

    :ref:`Queue Name <dcmQueueName>`",string,"Task Queue Name

    (dcmQueueName)"
    "
    .. _dicomDescription:

    :ref:`Exporter Description <dicomDescription>`",string,"Unconstrained text description of the exporter

    (dicomDescription)"
    "
    .. _dicomAETitle:

    :ref:`Archive Application Entity (AE) title <dicomAETitle>`",string,"Archive Application Entity (AE) title

    (dicomAETitle)"
    "
    .. _dcmExportAsSourceAE:

    :ref:`Export as Source Application Entity (AE) <dcmExportAsSourceAE>`",boolean,"Mask the Archive Application Entity (AE) title by the title of the Application Entity (AE) from which a Series was received on establishing the Association to the Destination Application Entity (AE).

    (dcmExportAsSourceAE)"
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

    :ref:`IAN Destination(s) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ

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

    :ref:`Instance Availability <dcmInstanceAvailability>`",string,"Instance Availability.

    Enumerated values:

    ONLINE

    NEARLINE

    OFFLINE

    (dcmInstanceAvailability)"
    "
    .. _dcmSchedule:

    :ref:`Export Schedule(s) <dcmSchedule>`",string,"Delay export to specified time periods. If no Export Schedule is specified, queue the export task for processing immediately. Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
    "
    .. _dcmProperty:

    :ref:`Exporter Property(s) <dcmProperty>`",string,"Specify exporter properties in format {name}={value}. Refer various `Exporter Properties <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Exporter-Properties>`_ that can be configured based on the exporter type.

    (dcmProperty)"
