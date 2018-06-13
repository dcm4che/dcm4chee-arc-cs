Export Rule
===========
Export Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Export Rule Attributes (LDAP Object: dcmExportRule)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name of the Export Rule"
    "
    .. _dcmEntity:

    :ref:`Attribute Entity (dcmEntity) <dcmEntity>`",string,"Entity of the Attribute Filter or Export Rule ('Patient', 'Study', 'Series', 'Instance', 'MPPS', 'MWL'). Enumerated values: Patient, Study, Series, Instance, MPPS or MWL"
    "
    .. _dcmExporterID:

    :ref:`Exporter ID(s) (dcmExporterID) <dcmExporterID>`",string,"Exporter ID"
    "
    .. _dcmExportPreviousEntity:

    :ref:`Export Previous Entity (dcmExportPreviousEntity) <dcmExportPreviousEntity>`",boolean,"Specifies if the previous Entity of a replaced Instance shall be also exported."
    "
    .. _dcmProperty:

    :ref:`Conditions(s) (dcmProperty) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx}"
    "
    .. _dcmSchedule:

    :ref:`Schedule(s) (dcmSchedule) <dcmSchedule>`",string,"Schedule Expression in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)"
    "
    .. _dcmDuration:

    :ref:`Duration (dcmDuration) <dcmDuration>`",string,"Duration in ISO-8601 duration format PnDTnHnMn.nS"
