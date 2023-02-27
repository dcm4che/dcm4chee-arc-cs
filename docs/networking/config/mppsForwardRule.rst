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

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmSchedule:

    :ref:`Time Conditions(s) <dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
