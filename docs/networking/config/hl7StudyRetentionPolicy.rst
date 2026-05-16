HL7 Study Retention Policy
==========================
HL7 Study Retention Policy

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Study Retention Policy Attributes (LDAP Object: hl7StudyRetentionPolicy)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _hl7StudyRetentionPolicy-cn:

    :ref:`Name <hl7StudyRetentionPolicy-cn>`",string,"Arbitrary/Meaningful name of the HL7 Study Retention Policy

    (cn)"
    "
    .. _dicomAETitle:
    .. _hl7StudyRetentionPolicy-dicomAETitle:

    :ref:`Application Entity (AE) title <hl7StudyRetentionPolicy-dicomAETitle>`",string,"Application Entity (AE) title

    (dicomAETitle)"
    "
    .. _dcmRetentionPeriod:
    .. _hl7StudyRetentionPolicy-dcmRetentionPeriod:

    :ref:`Minimal Study Retention Period <hl7StudyRetentionPolicy-dcmRetentionPeriod>`",string,"Minimal Study Retention Period in ISO-8601 period format PnYnMnD or PnW. Ineffective if 'Maximal Study Retention Period' is also set.

    (dcmRetentionPeriod)"
    "
    .. _dcmMaxRetentionPeriod:
    .. _hl7StudyRetentionPolicy-dcmMaxRetentionPeriod:

    :ref:`Maximal Study Retention Period <hl7StudyRetentionPolicy-dcmMaxRetentionPeriod>`",string,"Maximal Study Retention Period in ISO-8601 period format PnYnMnD or PnW

    (dcmMaxRetentionPeriod)"
    "
    .. _dcmRulePriority:
    .. _hl7StudyRetentionPolicy-dcmRulePriority:

    :ref:`Rule Priority <hl7StudyRetentionPolicy-dcmRulePriority>`",integer,"If the condition of several HL7 Study Retention policies match for a received HL7 message, higher priority policy is applied. If there are several matching policies with equal priority, it is undefined which policy gets applied.

    (dcmRulePriority)"
    "
    .. _dcmProperty:
    .. _hl7StudyRetentionPolicy-dcmProperty:

    :ref:`Conditions(s) <hl7StudyRetentionPolicy-dcmProperty>`",string,"Conditions in format {SEG}-{Seq#}[.{Comp#}[.{SubComp#}]][!]={regEx}. Examples: MSH-4=FORWARD or MSH-9=ADT\^A28\^ADT_A05 or PID-3[.3]=PIDIssuer or PID-3[.3[.2]]=PIDIssuerUniversalEntityIDType

    (dcmProperty)"
    "
    .. _dcmStartRetentionPeriodOnStudyDate:
    .. _hl7StudyRetentionPolicy-dcmStartRetentionPeriodOnStudyDate:

    :ref:`Start Retention Period on Study Date <hl7StudyRetentionPolicy-dcmStartRetentionPeriodOnStudyDate>`",boolean,"Indicates if retention period should be started on individual Study Dates instead on receive of the HL7 message triggering this rule.

    (dcmStartRetentionPeriodOnStudyDate)"
    "
    .. _dcmExporterID:
    .. _hl7StudyRetentionPolicy-dcmExporterID:

    :ref:`Export expired Study <hl7StudyRetentionPolicy-dcmExporterID>`",string,"Export expired Study/Series using the specified Exporter

    (dcmExporterID)"
    "
    .. _dcmFreezeExpirationDate:
    .. _hl7StudyRetentionPolicy-dcmFreezeExpirationDate:

    :ref:`Freeze Expiration Date <hl7StudyRetentionPolicy-dcmFreezeExpirationDate>`",boolean,"Indicate to disable changes of the Expiration Date by following events.

    (dcmFreezeExpirationDate)"
    "
    .. _dcmRevokeExpiration:
    .. _hl7StudyRetentionPolicy-dcmRevokeExpiration:

    :ref:`Revoke Expiration Date <hl7StudyRetentionPolicy-dcmRevokeExpiration>`",boolean,"Indicate to revoke a previous set Expiration Date.

    (dcmRevokeExpiration)"
