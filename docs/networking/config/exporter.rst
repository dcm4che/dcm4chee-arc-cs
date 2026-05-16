Exporter Descriptor
===================
Exporter Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Exporter Descriptor Attributes (LDAP Object: dcmExporter)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmExporterID:
    .. _exporter-dcmExporterID:

    :ref:`Exporter ID <exporter-dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmURI:
    .. _exporter-dcmURI:

    :ref:`Exporter URI <exporter-dcmURI>`",string,"RFC2079: Uniform Resource Identifier. Refer various `Exporter URI <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Exporter-Properties>`_ that can be configured based on the exporter type.

    (dcmURI)"
    "
    .. _dcmQueueName:
    .. _exporter-dcmQueueName:

    :ref:`Queue Name <exporter-dcmQueueName>`",string,"Task Queue Name

    (dcmQueueName)"
    "
    .. _dicomDescription:
    .. _exporter-dicomDescription:

    :ref:`Exporter Description <exporter-dicomDescription>`",string,"Unconstrained text description of the exporter

    (dicomDescription)"
    "
    .. _dicomAETitle:
    .. _exporter-dicomAETitle:

    :ref:`Archive Application Entity (AE) title <exporter-dicomAETitle>`",string,"Archive Application Entity (AE) title

    (dicomAETitle)"
    "
    .. _dcmExportAsSourceAE:
    .. _exporter-dcmExportAsSourceAE:

    :ref:`Export as Source Application Entity (AE) <exporter-dcmExportAsSourceAE>`",boolean,"Mask the Archive Application Entity (AE) title by the title of the Application Entity (AE) from which a Series was received on establishing the Association to the Destination Application Entity (AE).

    (dcmExportAsSourceAE)"
    "
    .. _dcmDeleteStudyFromStorageID:
    .. _exporter-dcmDeleteStudyFromStorageID:

    :ref:`Delete Study From Storage ID <exporter-dcmDeleteStudyFromStorageID>`",string,"ID of Storage System from which the objects of the exported Study shall be deleted. Only effective for Export Tasks on Study level.

    (dcmDeleteStudyFromStorageID)"
    "
    .. _dcmRejectForDataRetentionExpiry:
    .. _exporter-dcmRejectForDataRetentionExpiry:

    :ref:`Reject Entity for Data Retention Expiry <exporter-dcmRejectForDataRetentionExpiry>`",boolean,"Reject entity for Data Retention Expiry after export on completion of Export Task.

    (dcmRejectForDataRetentionExpiry)"
    "
    .. _dcmCheckIfAlreadyExistsOnDestination:
    .. _exporter-dcmCheckIfAlreadyExistsOnDestination:

    :ref:`Check if already exists on Destination <exporter-dcmCheckIfAlreadyExistsOnDestination>`",boolean,"Indicates to only export an object if there is not already an object with such Storage Path on the destination storage.

    (dcmCheckIfAlreadyExistsOnDestination)"
    "
    .. _dcmStgCmtSCP:
    .. _exporter-dcmStgCmtSCP:

    :ref:`Storage Commitment SCP AE Title <exporter-dcmStgCmtSCP>`",string,"AE Title of external Storage Commitment SCP used to verify export to another archive.

    (dcmStgCmtSCP)"
    "
    .. _dcmIanDestination:
    .. _exporter-dcmIanDestination:

    :ref:`IAN Destination(s) <exporter-dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ

    (dcmIanDestination)"
    "
    .. _dcmRetrieveAET:
    .. _exporter-dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) <exporter-dcmRetrieveAET>`",string,"AE Title associated with Network AE

    (dcmRetrieveAET)"
    "
    .. _dcmRetrieveLocationUID:
    .. _exporter-dcmRetrieveLocationUID:

    :ref:`Retrieve Location UID <exporter-dcmRetrieveLocationUID>`",string,"Retrieve Location UID.

    (dcmRetrieveLocationUID)"
    "
    .. _dcmInstanceAvailability:
    .. _exporter-dcmInstanceAvailability:

    :ref:`Instance Availability <exporter-dcmInstanceAvailability>`",string,"Instance Availability.

    Enumerated values:

    ONLINE

    NEARLINE

    OFFLINE

    (dcmInstanceAvailability)"
    "
    .. _dcmSchedule:
    .. _exporter-dcmSchedule:

    :ref:`Export Schedule(s) <exporter-dcmSchedule>`",string,"Delay export to specified time periods. If no Export Schedule is specified, queue the export task for processing immediately. Format: 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
    "
    .. _dcmProperty:
    .. _exporter-dcmProperty:

    :ref:`Exporter Property(s) <exporter-dcmProperty>`",string,"Specify exporter properties in format {name}={value}. Refer various `Exporter Properties <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Exporter-Properties>`_ that can be configured based on the exporter type.

    (dcmProperty)"
