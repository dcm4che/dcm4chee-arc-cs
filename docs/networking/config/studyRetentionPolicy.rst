Study Retention Policy
======================
Study Retention Policy

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Study Retention Policy Attributes (LDAP Object: dcmStudyRetentionPolicy)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Study Retention Policy

    (cn)"
    "
    .. _dcmRetentionPeriod:

    :ref:`Study Retention Period <dcmRetentionPeriod>`",string,"Study Retention Period in ISO-8601 period format PnYnMnD or PnW

    (dcmRetentionPeriod)"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority <dcmRulePriority>`",integer,"If the condition of several Study Retention policies match for a received image, higher priority policy is applied. If there are several matching policies with equal priority, it is undefined which policy gets applied.

    (dcmRulePriority)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmExpireSeriesIndividually:

    :ref:`Expire Series Individually <dcmExpireSeriesIndividually>`",boolean,"Indicates if series should be expired individually or not.

    (dcmExpireSeriesIndividually)"
    "
    .. _dcmStartRetentionPeriodOnStudyDate:

    :ref:`Start Retention Period on Study Date <dcmStartRetentionPeriodOnStudyDate>`",boolean,"Indicates if retention period should be started on Study Date instead on receive of an object of the Study

    (dcmStartRetentionPeriodOnStudyDate)"
    "
    .. _dcmExporterID:

    :ref:`Export expired Study <dcmExporterID>`",string,"Export expired Study/Series using the specified Exporter

    (dcmExporterID)"
    "
    .. _dcmFreezeExpirationDate:

    :ref:`Freeze Expiration Date <dcmFreezeExpirationDate>`",boolean,"Indicate to disable changes of the Expiration Date by following events.

    (dcmFreezeExpirationDate)"
    "
    .. _dcmRevokeExpiration:

    :ref:`Revoke Expiration Date <dcmRevokeExpiration>`",boolean,"Indicate to revoke a previous set Expiration Date.

    (dcmRevokeExpiration)"
