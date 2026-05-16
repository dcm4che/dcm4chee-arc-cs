Export Rule
===========
Export Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Export Rule Attributes (LDAP Object: dcmExportRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _exportRule-cn:

    :ref:`Name <exportRule-cn>`",string,"Arbitrary/Meaningful name of the Export Rule

    (cn)"
    "
    .. _dcmEntity:
    .. _exportRule-dcmEntity:

    :ref:`Export Entity <exportRule-dcmEntity>`",string,"Entity of Export

    Enumerated values:

    Study

    Series

    Instance

    (dcmEntity)"
    "
    .. _dcmExporterID:
    .. _exportRule-dcmExporterID:

    :ref:`Exporter ID(s) <exportRule-dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dicomDeviceName:
    .. _exportRule-dicomDeviceName:

    :ref:`Exporter Device Name <exportRule-dicomDeviceName>`",string,"Specifies Device on which the Export Task(s) shall be scheduled. If not specified, the Export Task(s) is/are scheduled on the Device which received the objects. Attention: the specified Device must (also) have Exporters with the specified IDs configured!

    (dicomDeviceName)"
    "
    .. _dcmExportPreviousEntity:
    .. _exportRule-dcmExportPreviousEntity:

    :ref:`Export Previous Entity <exportRule-dcmExportPreviousEntity>`",boolean,"Specifies if the previous Entity of a replaced Instance shall be also exported.

    (dcmExportPreviousEntity)"
    "
    .. _dcmProperty:
    .. _exportRule-dcmProperty:

    :ref:`Conditions(s) <exportRule-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmSchedule:
    .. _exportRule-dcmSchedule:

    :ref:`Time Conditions(s) <exportRule-dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmDuration:
    .. _exportRule-dcmDuration:

    :ref:`Export Delay <exportRule-dcmDuration>`",string,"Delay export of entities to accumulate multiple trigger events to one export task.

    (dcmDuration)"
    "
    .. _dcmExportReoccurredInstances:
    .. _exportRule-dcmExportReoccurredInstances:

    :ref:`Export Reoccurred Instances <exportRule-dcmExportReoccurredInstances>`",string,"Indicates if the entity shall be exported on subsequent occurrence of instances

    Enumerated values:

    NEVER (= Never export entity on reoccurrence of instances)

    ALWAYS (= Always export entity on reoccurrence of instances)

    REPLACE (= Export entity only on reoccurrence of replaced instances)

    (dcmExportReoccurredInstances)"
