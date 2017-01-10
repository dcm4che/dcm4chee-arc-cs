Export Rule
===========
Export Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Export Rule Attributes (LDAP Object: dcmExportRule)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Name**",string,"Arbitrary/Meaningful name of the Export Rule","
    .. _cn:

    cn_"
    "**Attribute Entity**",string,"Entity of the Attribute Filter or Export Rule ('Patient', 'Study', 'Series', 'Instance', 'MPPS', 'MWL').","
    .. _dcmEntity:

    dcmEntity_"
    "Export Previous Entity",boolean,"Specifies if the previous Entity of a replaced Instance shall be also exported. Disabled if absent.","
    .. _dcmExportPreviousEntity:

    dcmExportPreviousEntity_"
    "**Exporter ID(s)**",string,"Exporter ID","
    .. _dcmExporterID:

    dcmExporterID_"
    "Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
    "Schedule(s)",string,"Schedule Expression in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)","
    .. _dcmSchedule:

    dcmSchedule_"
    "Duration",string,"Duration in ISO-8601 duration format PnDTnHnMn.nS","
    .. _dcmDuration:

    dcmDuration_"
