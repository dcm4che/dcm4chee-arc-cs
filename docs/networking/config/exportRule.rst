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

    :ref:`Export Entity <dcmEntity>`",string,"Entity of Export Enumerated values: Study, Series or Instance.

    (dcmEntity)"
    "
    .. _dcmExporterID:

    :ref:`Exporter ID(s) <dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dicomDeviceName:

    :ref:`Exporter Device Name <dicomDeviceName>`",string,"Specifies Device on which the Export Task(s) shall be scheduled. If not specified, the Export Task(s) is/are scheduled on the Device which received the objects. Attention: the specified Device must (also) have Exporters with the specified IDs configured!

    (dicomDeviceName)"
    "
    .. _dcmExportPreviousEntity:

    :ref:`Export Previous Entity <dcmExportPreviousEntity>`",boolean,"Specifies if the previous Entity of a replaced Instance shall be also exported.

    (dcmExportPreviousEntity)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Time Conditions(s) <dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmDuration:

    :ref:`Export Delay <dcmDuration>`",string,"Delay export of entities to accumulate multiple trigger events to one export task.

    (dcmDuration)"
    "
    .. _dcmExportReoccurredInstances:

    :ref:`Export Reoccurred Instances <dcmExportReoccurredInstances>`",string,"Indicates if the entity shall be exported on subsequent occurrence of instances Enumerated values: NEVER, ALWAYS or REPLACE.

    (dcmExportReoccurredInstances)"
