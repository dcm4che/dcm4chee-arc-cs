Prefetch Rule
=============
Prefetch Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Prefetch Rule Attributes (LDAP Object: dcmPrefetchRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Prefetch Rule

    (cn)"
    "
    .. _dcmExporterID:

    :ref:`Exporter ID(s) <dcmExporterID>`",string,"Exporter ID

    (dcmExporterID)"
    "
    .. _dcmEntitySelector:

    :ref:`Entity Selector(s) <dcmEntitySelector>`",string,"Specifies matching keys used to select entities to prefetch. Format: (study|series)[?{attributeID}={value}[&...][&priors=<n>]].

    (dcmEntitySelector)"
    "
    .. _dcmProperty:

    :ref:`Attribute Conditions(s) <dcmProperty>`",string,"Attribute conditions in format {attributeID}[!]={regEx}.

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Time Conditions(s) <dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
    "
    .. _dcmDuration:

    :ref:`Suppress Duplicate Export Interval <dcmDuration>`",string,"Suppress Export of entities already exported not earlier than the specified interval to avoid duplicate exports.

    (dcmDuration)"
