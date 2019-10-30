Store Access Control ID Rule
============================
Store Access Control ID Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Store Access Control ID Rule Attributes (LDAP Object: dcmStoreAccessControlIDRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Store Access Control ID Rule

    (cn)"
    "
    .. _dcmStoreAccessControlID:

    :ref:`Store Access Control ID <dcmStoreAccessControlID>`",string,"Access Control ID assigned to Studies which attributes match all conditions

    (dcmStoreAccessControlID)"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority <dcmRulePriority>`",integer,"Rule Priority.

    (dcmRulePriority)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format (SendingHostname|SendingApplicationEntityTitle|ReceivingHostname|ReceivingApplicationEntityTitle|{attributeID})[!]={regEx}

    (dcmProperty)"
