UI Filter Template
==================
Defined filter template

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Filter Template Attributes (LDAP Object: dcmUiFilterTemplate)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiFilterTemplateGroupName:

    :ref:`Name <dcmuiFilterTemplateGroupName>`",string,"Name of the template

    (dcmuiFilterTemplateGroupName)"
    "
    .. _dcmuiFilterTemplateID:

    :ref:`ID <dcmuiFilterTemplateID>`",string,"ID of the filter where this template can apply

    (dcmuiFilterTemplateID)"
    "
    .. _dcmuiFilterTemplateDescription:

    :ref:`Description <dcmuiFilterTemplateDescription>`",string,"Filter template description

    (dcmuiFilterTemplateDescription)"
    "
    .. _dcmuiFilterTemplateFilters:

    :ref:`Filters(s) <dcmuiFilterTemplateFilters>`",string,"Default filters in this template, filter pare key=value (example LocalAET=DCM4CHEE). For date filter you can use the predefined keywords 'today' and 'yesterday' so the dynamic values of the filters can be generated.

    (dcmuiFilterTemplateFilters)"
    "
    .. _dcmuiFilterTemplateDefault:

    :ref:`Default <dcmuiFilterTemplateDefault>`",boolean,"Use this template as default

    (dcmuiFilterTemplateDefault)"
