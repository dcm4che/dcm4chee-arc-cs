Study Retention Policy
======================
Study Retention Policy

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Study Retention Policy Attributes (LDAP Object: dcmStudyRetentionPolicy)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name\ :sup:`*` ",string,"Arbitrary/Meaningful name of the Study Retention Policy","
    .. _cn:

    cn_"
    "Study Retention Period\ :sup:`*` ",string,"Study Retention Period in ISO-8601 period format PnYnMnD or PnW","
    .. _dcmRetentionPeriod:

    dcmRetentionPeriod_"
    "Rule Priority",integer,"Rule Priority. 0 if absent.","
    .. _dcmRulePriority:

    dcmRulePriority_"
    "Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
    "Expire Series Individually",boolean,"Indicates if series should be expired individually or not. If absent, it is false.","
    .. _dcmExpireSeriesIndividually:

    dcmExpireSeriesIndividually_"
