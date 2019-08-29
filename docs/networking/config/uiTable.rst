UI Study Table Configuration
============================
Study Table configuration for the pro version

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Study Table Configuration Attributes (LDAP Object: dcmUiTable)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiStudyTableConfigName:

    :ref:`Configuration Name <dcmuiStudyTableConfigName>`",string,"UI Study Table Configuration Name

    (dcmuiStudyTableConfigName)"
    "
    .. _dcmuiStudyTableConfigUsername:

    :ref:`Username <dcmuiStudyTableConfigUsername>`",string,"Username to which this set should be available

    (dcmuiStudyTableConfigUsername)"
    "
    .. _dcmuiStudyTableConfigRoles:

    :ref:`Role <dcmuiStudyTableConfigRoles>`",string,"Username role that can use this Set ( If you set the username, the role will be ignored )

    (dcmuiStudyTableConfigRoles)"
    "
    .. _dcmuiStudyTableConfigIsDefault:

    :ref:`Is Default <dcmuiStudyTableConfigIsDefault>`",boolean,"Set this Column-Set to the default one. (Make sure that only one of the Set - siblings child is set to default).

    (dcmuiStudyTableConfigIsDefault)"
    ":doc:`uiTableColumns` (s)",object,"Define Study Table Columns"

.. toctree::

    uiTableColumns
