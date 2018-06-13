Exporter Descriptor
===================
Exporter Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Exporter Descriptor Attributes (LDAP Object: dcmExporter)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmExporterID:

    :ref:`Exporter ID (dcmExporterID) <dcmExporterID>`",string,"Exporter ID"
    "
    .. _dcmURI:

    :ref:`URI (dcmURI) <dcmURI>`",string,"RFC2079: Uniform Resource Identifier"
    "
    .. _dcmQueueName:

    :ref:`Queue Name (dcmQueueName) <dcmQueueName>`",string,"JMS Queue Name Enumerated values: Export1, Export2, Export3, Export4 or Export5"
    "
    .. _dcmExportPriority:

    :ref:`Export Priority (dcmExportPriority) <dcmExportPriority>`",integer,"JMS Priority Level for processing the Export Task from 0 (lowest) to 9 (highest)."
    "
    .. _dicomDescription:

    :ref:`Exporter Description (dicomDescription) <dicomDescription>`",string,"Unconstrained text description of the exporter"
    "
    .. _dicomAETitle:

    :ref:`Application Entity (AE) title (dicomAETitle) <dicomAETitle>`",string,"Application Entity (AE) title"
    "
    .. _dcmStgCmtSCP:

    :ref:`Storage Commitment SCP AE Title (dcmStgCmtSCP) <dcmStgCmtSCP>`",string,"AE Title of external Storage Commitment SCP used to verify export to another archive."
    "
    .. _dcmIanDestination:

    :ref:`Ian Destination(s) (dcmIanDestination) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ"
    "
    .. _dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) (dcmRetrieveAET) <dcmRetrieveAET>`",string,"AE Title associated with Network AE"
    "
    .. _dcmRetrieveLocationUID:

    :ref:`Retrieve Location UID (dcmRetrieveLocationUID) <dcmRetrieveLocationUID>`",string,"Retrieve Location UID."
    "
    .. _dcmInstanceAvailability:

    :ref:`Instance Availability (dcmInstanceAvailability) <dcmInstanceAvailability>`",string,"Instance Availability. Enumerated values: ONLINE, NEARLINE or OFFLINE"
    "
    .. _dcmSchedule:

    :ref:`Schedule(s) (dcmSchedule) <dcmSchedule>`",string,"Schedule Expression in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)"
    "
    .. _dcmProperty:

    :ref:`Property(s) (dcmProperty) <dcmProperty>`",string,"Property in format <name>=<value>"
