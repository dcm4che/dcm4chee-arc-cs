UI Study Table Columns Configuration
====================================
Study Table Columns

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Study Table Columns Configuration Attributes (LDAP Object: dcmUiTableColumns)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiColumnName:
    .. _uiTableColumns-dcmuiColumnName:

    :ref:`Column Name <uiTableColumns-dcmuiColumnName>`",string,"The Name of the Column in the Study Table

    (dcmuiColumnName)"
    "
    .. _dcmuiColumnId:
    .. _uiTableColumns-dcmuiColumnId:

    :ref:`Column ID <uiTableColumns-dcmuiColumnId>`",string,"Every possible column that is used in the UI, has and ID, by using the ID you can change some of the properties of that Column, like Name, Description, Order or width

    (dcmuiColumnId)"
    "
    .. _dcmuiColumnTitle:
    .. _uiTableColumns-dcmuiColumnTitle:

    :ref:`Column Description <uiTableColumns-dcmuiColumnTitle>`",string,"Description of the Column, shown on hover

    (dcmuiColumnTitle)"
    "
    .. _dcmuiValuePath:
    .. _uiTableColumns-dcmuiValuePath:

    :ref:`Value path <uiTableColumns-dcmuiValuePath>`",string,"Value (json-Object) Path of the column (for Example: '00100010.Value[0].Alphabetic' for Patient's Name or '00100020.Value[0]' for Patient ID

    (dcmuiValuePath)"
    "
    .. _dcmuiValueType:
    .. _uiTableColumns-dcmuiValueType:

    :ref:`Type of the value <uiTableColumns-dcmuiValueType>`",string,"Type of the column how to get the value, default should be 'value'

    Enumerated values:

    value

    pipe

    (dcmuiValueType)"
    "
    .. _dcmuiColumnWidth:
    .. _uiTableColumns-dcmuiColumnWidth:

    :ref:`Column width in weight <uiTableColumns-dcmuiColumnWidth>`",string,"Width of the column in weight ( x > 0.1 - x < infinite ) default 1

    (dcmuiColumnWidth)"
    "
    .. _dcmuiColumnOrder:
    .. _uiTableColumns-dcmuiColumnOrder:

    :ref:`Order of the Column <uiTableColumns-dcmuiColumnOrder>`",number,"Order of the Column

    (dcmuiColumnOrder)"
