Study Retention Policy
======================
Study Retention Policy

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Study Retention Policy Attributes (LDAP Object: dcmStudyRetentionPolicy)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name of the Study Retention Policy"
    "
    .. _dcmRetentionPeriod:

    :ref:`Study Retention Period (dcmRetentionPeriod) <dcmRetentionPeriod>`",string,"Study Retention Period in ISO-8601 period format PnYnMnD or PnW"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority (dcmRulePriority) <dcmRulePriority>`",integer,"Rule Priority."
    "
    .. _dcmProperty:

    :ref:`Conditions(s) (dcmProperty) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx}"
    "
    .. _dcmExpireSeriesIndividually:

    :ref:`Expire Series Individually (dcmExpireSeriesIndividually) <dcmExpireSeriesIndividually>`",boolean,"Indicates if series should be expired individually or not."
    "
    .. _dcmStartRetentionPeriodOnStudyDate:

    :ref:`Start Retention Period on Study Date (dcmStartRetentionPeriodOnStudyDate) <dcmStartRetentionPeriodOnStudyDate>`",boolean,"Indicates if retention period should be started on Study Date"
