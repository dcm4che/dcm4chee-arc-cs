MPPS Forward Rule
=================
MPPS Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: MPPS Forward Rule Attributes (LDAP Object: dcmMppsForwardRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the MPPS Forward Rule

    (cn)"
    "
    .. _dcmFwdMppsDestination:

    :ref:`MPPS Forward Destination(s) <dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ

    (dcmFwdMppsDestination)"
    "
    .. _dcmProperty:

    :ref:`Attribute Conditions(s) <dcmProperty>`",string,"Attribute Conditions in format (SendingHostname|SendingApplicationEntityTitle|ReceivingHostname|ReceivingApplicationEntityTitle|{AttributeTagOrKeyword[number]}|{SequenceTagOrKeyword.AttributeTagOrKeyword})[!]={regEx}. More than one value can be specified for a given attribute by separating them with a | symbol. Examples: SendingApplicationEntityTitle=FORWARD or Modality=MR|CT or ProcedureCodeSequence.CodeValue=MRProcedure or 00180015=KNEE or 00321034.00080100=RequestingServiceCode or ImageType[3]=LOCALIZER

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Time Conditions(s) <dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
