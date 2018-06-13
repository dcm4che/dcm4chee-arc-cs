Export Rule
===========
Export Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Export Rule Attributes (LDAP Object: dcmExportRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Export Rule

    (cn)"
    "
    .. _dcmEntity:

    :ref:`Attribute Entity <dcmEntity>`",string,"Entity of the Attribute Filter or Export Rule ('Patient', 'Study', 'Series', 'Instance', 'MPPS', 'MWL'). Enumerated values: Patient, Study, Series, Instance, MPPS or MWL.

    (dcmEntity)"
    "
    .. _dcmExporterID:

    :ref:`Exporter ID(s) <dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmExportPreviousEntity:

    :ref:`Export Previous Entity <dcmExportPreviousEntity>`",boolean,"Specifies if the previous Entity of a replaced Instance shall be also exported.

    (dcmExportPreviousEntity)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx}

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Schedule(s) <dcmSchedule>`",string,"Schedule Expression in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmSchedule)"
    "
    .. _dcmDuration:

    :ref:`Duration <dcmDuration>`",string,"Duration in ISO-8601 duration format PnDTnHnMn.nS

    (dcmDuration)"
