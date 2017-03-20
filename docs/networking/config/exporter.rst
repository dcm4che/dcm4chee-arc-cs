Exporter Descriptor
===================
Exporter Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Exporter Descriptor Attributes (LDAP Object: dcmExporter)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Exporter ID**",string,"Exporter ID","
    .. _dcmExporterID:

    dcmExporterID_"
    "**URI**",string,"RFC2079: Uniform Resource Identifier","
    .. _dcmURI:

    dcmURI_"
    "**Queue Name**",string,"JMS Queue Name","
    .. _dcmQueueName:

    dcmQueueName_"
    "Exporter Description",string,"Unconstrained text description of the exporter","
    .. _dicomDescription:

    dicomDescription_"
    "Application Entity (AE) title",string,"Application Entity (AE) title","
    .. _dicomAETitle:

    dicomAETitle_"
    "Storage Commitment SCP AE Title",string,"AE Title of external Storage Commitment SCP used to verify export to another archive.","
    .. _dcmStgCmtSCP:

    dcmStgCmtSCP_"
    "Ian Destination(s)",string,"Destination to send IAN N-CREATE RQ","
    .. _dcmIanDestination:

    dcmIanDestination_"
    "Retrieve AE Title(s)",string,"AE Title associated with Network AE","
    .. _dcmRetrieveAET:

    dcmRetrieveAET_"
    "Retrieve Location UID",string,"Retrieve Location UID.","
    .. _dcmRetrieveLocationUID:

    dcmRetrieveLocationUID_"
    "Instance Availability",string,"Instance Availability: ONLINE, NEARLINE or OFFLINE. ONLINE if absent.","
    .. _dcmInstanceAvailability:

    dcmInstanceAvailability_"
    "Schedule(s)",string,"Schedule Expression in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)","
    .. _dcmSchedule:

    dcmSchedule_"
    "Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
