Store Access Control ID Rule
============================
Store Access Control ID Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Store Access Control ID Rule Attributes (LDAP Object: dcmStoreAccessControlIDRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _storeAccessControlIDRule-cn:

    :ref:`Name <storeAccessControlIDRule-cn>`",string,"Arbitrary/Meaningful name of the Store Access Control ID Rule

    (cn)"
    "
    .. _dcmStoreAccessControlID:
    .. _storeAccessControlIDRule-dcmStoreAccessControlID:

    :ref:`Store Access Control ID(s) <storeAccessControlIDRule-dcmStoreAccessControlID>`",string,"Access Control IDs assigned to whole Studies or individual Series which attributes match all conditions.

    (dcmStoreAccessControlID)"
    "
    .. _dcmEntity:
    .. _storeAccessControlIDRule-dcmEntity:

    :ref:`Entity <storeAccessControlIDRule-dcmEntity>`",string,"Indicates if the Access Control ID shall be assigned to whole Studies or individual Series.

    Enumerated values:

    Study

    Series

    (dcmEntity)"
    "
    .. _dcmRulePriority:
    .. _storeAccessControlIDRule-dcmRulePriority:

    :ref:`Rule Priority <storeAccessControlIDRule-dcmRulePriority>`",integer,"If the condition of several Store Access Control ID rules match for a received image, higher priority rule is applied. If there are several matching rules with equal priority, it is undefined which rule gets applied.

    (dcmRulePriority)"
    "
    .. _dcmProperty:
    .. _storeAccessControlIDRule-dcmProperty:

    :ref:`Conditions(s) <storeAccessControlIDRule-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
