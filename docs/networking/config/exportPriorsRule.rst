Export Priors Rule
==================
Export Priors Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Export Priors Rule Attributes (LDAP Object: dcmExportPriorsRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _exportPriorsRule-cn:

    :ref:`Name <exportPriorsRule-cn>`",string,"Arbitrary/Meaningful name of the Export Priors Rule

    (cn)"
    "
    .. _dcmExporterID:
    .. _exportPriorsRule-dcmExporterID:

    :ref:`Exporter ID(s) <exportPriorsRule-dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmProperty:
    .. _exportPriorsRule-dcmProperty:

    :ref:`Conditions(s) <exportPriorsRule-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmSchedule:
    .. _exportPriorsRule-dcmSchedule:

    :ref:`Time Conditions(s) <exportPriorsRule-dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmEntitySelector:
    .. _exportPriorsRule-dcmEntitySelector:

    :ref:`Entity Selector(s) <exportPriorsRule-dcmEntitySelector>`",string,"Specifies matching keys used to select prior Studies to export. Format: {key}={value}[&{key}={value}]..., with {key} = 'priors' | 'StudyAge' | {attributeID}. {value} in the format '$'{attributeID} are replaced by the value of the specified attribute from the received object which triggered the export. If no Entity Selector is specified, all prior Studies for the Patient will be exported. Example: 'priors=2&StudyAge=-5Y&ModalitiesInStudy=CT' => select at most 2 prior Studies not older than 5 years containing at least one CT Series.

    (dcmEntitySelector)"
    "
    .. _dcmDuration:
    .. _exportPriorsRule-dcmDuration:

    :ref:`Suppress Duplicate Export Interval <exportPriorsRule-dcmDuration>`",string,"Suppress Export of Studies already exported not earlier than the specified interval to avoid duplicate exports.

    (dcmDuration)"
    "
    .. _dcmExportReoccurredInstances:
    .. _exportPriorsRule-dcmExportReoccurredInstances:

    :ref:`Export Reoccurred Instances <exportPriorsRule-dcmExportReoccurredInstances>`",string,"Indicates if prior studies shall be exported on subsequent occurrence of instances

    Enumerated values:

    NEVER (= Never export prior Studies on reoccurrence of instances)

    ALWAYS (= Always export prior Studies on reoccurrence of instances)

    REPLACE (= Export prior Studies only on reoccurrence of replaced instances)

    (dcmExportReoccurredInstances)"
