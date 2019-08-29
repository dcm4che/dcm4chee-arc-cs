UI Elasticsearch URL Configuration
==================================
Elasticsearch URL

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Elasticsearch URL Configuration Attributes (LDAP Object: dcmUiTableColumns)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiColumnName:

    :ref:`Column Name <dcmuiColumnName>`",string,"The Name of the Column in the Study Table

    (dcmuiColumnName)"
    "
    .. _dcmuiColumnTitle:

    :ref:`Column Description <dcmuiColumnTitle>`",string,"Description of the Column, shown on hover

    (dcmuiColumnTitle)"
    "
    .. _dcmuiValuePath:

    :ref:`Value path <dcmuiValuePath>`",string,"Value (json-Object) Path of the column (for Example: '00100010.Value[0].Alphabetic' for Patient's Name or '00100020.Value[0]' for Patient ID

    (dcmuiValuePath)"
    "
    .. _dcmuiValueType:

    :ref:`Type of the value <dcmuiValueType>`",string,"Type of the column how to get the value, default should be 'value' Enumerated values: value or pipe.

    (dcmuiValueType)"
    "
    .. _dcmuiColumnWidth:

    :ref:`Column width in weight <dcmuiColumnWidth>`",string,"Width of the column in weight ( x > 0.1 - x < infinite ) default 1

    (dcmuiColumnWidth)"
    "
    .. _dcmuiColumnOrder:

    :ref:`Column width in weight <dcmuiColumnOrder>`",string,"Width of the column in weight ( x > 0.1 - x < infinite ) default 1

    (dcmuiColumnOrder)"
