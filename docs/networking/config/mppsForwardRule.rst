MPPS Forward Rule
=================
MPPS Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: MPPS Forward Rule Attributes (LDAP Object: dcmMppsForwardRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _mppsForwardRule-cn:

    :ref:`Name <mppsForwardRule-cn>`",string,"Arbitrary/Meaningful name of the MPPS Forward Rule

    (cn)"
    "
    .. _dcmFwdMppsDestination:
    .. _mppsForwardRule-dcmFwdMppsDestination:

    :ref:`MPPS Forward Destination(s) <mppsForwardRule-dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ

    (dcmFwdMppsDestination)"
    "
    .. _dcmProperty:
    .. _mppsForwardRule-dcmProperty:

    :ref:`Conditions(s) <mppsForwardRule-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmSchedule:
    .. _mppsForwardRule-dcmSchedule:

    :ref:`Time Conditions(s) <mppsForwardRule-dcmSchedule>`",string,"Apply this rule only within specified time ranges.

    (dcmSchedule)"
