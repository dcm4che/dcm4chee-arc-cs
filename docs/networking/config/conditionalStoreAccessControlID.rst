Conditional Store Access Control ID
===================================
Conditional Store Access Control ID

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Conditional Store Access Control ID Attributes (LDAP Object: dcmConditionalStoreAccessControlID)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name\ :sup:`*` ",string,"Arbitrary/Meaningful name of the Conditional Store Access Control ID","
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
