Change Access Control ID Rule
=============================
Change Access Control ID Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Change Access Control ID Rule Attributes (LDAP Object: dcmChangeAccessControlIDRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _changeAccessControlIDRule-cn:

    :ref:`Name <changeAccessControlIDRule-cn>`",string,"Arbitrary/Meaningful name of the Change Access Control ID Rule

    (cn)"
    "
    .. _dicomAETitle:
    .. _changeAccessControlIDRule-dicomAETitle:

    :ref:`Archive Application Entity (AE) title <changeAccessControlIDRule-dicomAETitle>`",string,"Title of Archive Application Entity (AE) which configured Query Retrieve View and Access Control ID are applied in the selection of Studies or Series which assigned Access Control ID shall be changed.

    (dicomAETitle)"
    "
    .. _dcmStoreAccessControlID:
    .. _changeAccessControlIDRule-dcmStoreAccessControlID:

    :ref:`Store Access Control ID <changeAccessControlIDRule-dcmStoreAccessControlID>`",string,"New Access Control ID assigned to selected Studies or individual Series after specified delay after receive of the first object of the Study. '*' removes previous assigned Access Control ID, making the Study or Series accessible on all Archive AEs.

    (dcmStoreAccessControlID)"
    "
    .. _dcmAccessControlID:
    .. _changeAccessControlIDRule-dcmAccessControlID:

    :ref:`Access Control ID(s) <changeAccessControlIDRule-dcmAccessControlID>`",string,"Previous Access Control IDs assigned to selected Studies or individual Series to change. If no value is specified, all Access Control IDs accessible by the specified Archive Application Entity (AE) will be changed.

    (dcmAccessControlID)"
    "
    .. _dcmEntity:
    .. _changeAccessControlIDRule-dcmEntity:

    :ref:`Entity <changeAccessControlIDRule-dcmEntity>`",string,"Indicates if Access Control ID assigned to Studies or individual Series shall be changed.

    Enumerated values:

    Study

    Series

    (dcmEntity)"
    "
    .. _dcmEntitySelector:
    .. _changeAccessControlIDRule-dcmEntitySelector:

    :ref:`Entity Selector(s) <changeAccessControlIDRule-dcmEntitySelector>`",string,"Specifies matching keys used to select received Studies or Series which Access Control ID shall be updated. Format: {key}={value}[&{key}={value}]..., with {key} = {attributeID}. If no Entity Selector is specified, the Accession Control IDs of all Studies or Series visible for the specified Archive AE will be updated to the specified Store Access Control ID.

    (dcmEntitySelector)"
    "
    .. _dcmChangeAccessControlIDDelay:
    .. _changeAccessControlIDRule-dcmChangeAccessControlIDDelay:

    :ref:`Change Access Control ID Delay <changeAccessControlIDRule-dcmChangeAccessControlIDDelay>`",string,"Delay after receive of the first object of a Study/Series after which the Access Control ID associated with the Study or including Series shall be changed to the specified Store Access Control ID in ISO-8601 duration format PnDTnHnMn.nS.

    (dcmChangeAccessControlIDDelay)"
    "
    .. _dcmChangeAccessControlIDMaxDelay:
    .. _changeAccessControlIDRule-dcmChangeAccessControlIDMaxDelay:

    :ref:`Change Access Control ID Maximal Delay <changeAccessControlIDRule-dcmChangeAccessControlIDMaxDelay>`",string,"Indicates to stop applying this rule for Studies/Series which first object was received before the specified interval in ISO-8601 duration format PnDTnHnMn.nS. Required if there are other rules for changing the Access Control ID again in the future.

    (dcmChangeAccessControlIDMaxDelay)"
