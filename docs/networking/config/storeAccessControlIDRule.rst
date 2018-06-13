Store Access Control ID Rule
============================
Store Access Control ID Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Store Access Control ID Rule Attributes (LDAP Object: dcmStoreAccessControlIDRule)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name of the Store Access Control ID Rule"
    "
    .. _dcmStoreAccessControlID:

    :ref:`Store Access Control ID (dcmStoreAccessControlID) <dcmStoreAccessControlID>`",string,"Access Control ID assigned to Studies which attributes match all conditions"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority (dcmRulePriority) <dcmRulePriority>`",integer,"Rule Priority."
    "
    .. _dcmProperty:

    :ref:`Conditions(s) (dcmProperty) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx}"
