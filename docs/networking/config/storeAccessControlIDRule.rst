Store Access Control ID Rule
============================
Store Access Control ID Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Store Access Control ID Rule Attributes (LDAP Object: dcmStoreAccessControlIDRule)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name\ :sup:`*` ",string,"Arbitrary/Meaningful name of the Store Access Control ID Rule","
    .. _cn:

    cn_"
    "Store Access Control ID\ :sup:`*` ",string,"Access Contol ID assigned to Studies which attributes match all conditions","
    .. _dcmStoreAccessControlID:

    dcmStoreAccessControlID_"
    "Rule Priority",integer,"Rule Priority. 0 if absent.","
    .. _dcmRulePriority:

    dcmRulePriority_"
    "Conditions(s)",string,"Conditions in format {attributeID}[!]={regEx}","
    .. _dcmProperty:

    dcmProperty_"
