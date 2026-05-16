UI Table Configuration
======================
Study Table configuration for the pro version

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Table Configuration Attributes (LDAP Object: dcmUiTable)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiTableConfigName:
    .. _uiTable-dcmuiTableConfigName:

    :ref:`Configuration Name <uiTable-dcmuiTableConfigName>`",string,"UI  Table Configuration Name

    (dcmuiTableConfigName)"
    "
    .. _dcmuiTableConfigUsername:
    .. _uiTable-dcmuiTableConfigUsername:

    :ref:`Username(s) <uiTable-dcmuiTableConfigUsername>`",string,"Username to which this set should be available

    (dcmuiTableConfigUsername)"
    "
    .. _dcmuiTableConfigRoles:
    .. _uiTable-dcmuiTableConfigRoles:

    :ref:`Role(s) <uiTable-dcmuiTableConfigRoles>`",string,"Username role that can use this Set ( If you set the username, the role will be ignored )

    (dcmuiTableConfigRoles)"
    "
    .. _dcmuiTableID:
    .. _uiTable-dcmuiTableID:

    :ref:`Table ID <uiTable-dcmuiTableID>`",string,"The ID of the Table in the UI for which the config should be effective

    (dcmuiTableID)"
    "
    .. _dcmuiTableConfigIsDefault:
    .. _uiTable-dcmuiTableConfigIsDefault:

    :ref:`Is Default <uiTable-dcmuiTableConfigIsDefault>`",boolean,"Set this Column-Set to the default one. (Make sure that only one of the Set - siblings child is set to default).

    (dcmuiTableConfigIsDefault)"
    ":doc:`uiTableColumns` (s)",object,"Define Table Columns"

.. toctree::

    uiTableColumns
