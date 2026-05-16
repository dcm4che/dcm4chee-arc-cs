MWL Idle Timeout
================
MWL Idle Timeout

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: MWL Idle Timeout Attributes (LDAP Object: dcmMwlIdleTimeout)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _mwlIdleTimeout-cn:

    :ref:`Name <mwlIdleTimeout-cn>`",string,"Arbitrary/Meaningful name of the MWL Idle Timeout.

    (cn)"
    "
    .. _dicomAETitle:
    .. _mwlIdleTimeout-dicomAETitle:

    :ref:`MWL SCP AE Title <mwlIdleTimeout-dicomAETitle>`",string,"Archive AE Title of MWL SCP on which the MWL Idle Timeout shall be applied.

    (dicomAETitle)"
    "
    .. _dcmAETitle:
    .. _mwlIdleTimeout-dcmAETitle:

    :ref:`Scheduled Station AE Title(s) <mwlIdleTimeout-dcmAETitle>`",string,"Scheduled Station AE Title(s) of Scheduled Procedure Steps for which the MWL Idle Timeout shall be applied. If none is specified, the MWL Idle Timeout is applied to all Scheduled Procedure Steps provided by the MWL SCP.

    (dcmAETitle)"
    "
    .. _dcmMWLStatusOnIdle:
    .. _mwlIdleTimeout-dcmMWLStatusOnIdle:

    :ref:`MWL Status on Idle <mwlIdleTimeout-dcmMWLStatusOnIdle>`",string,"Change Status of idle Scheduled Procedure Steps to specified value.

    Enumerated values:

    CANCELED

    DISCONTINUED

    COMPLETED

    (dcmMWLStatusOnIdle)"
    "
    .. _dcmDuration:
    .. _mwlIdleTimeout-dcmDuration:

    :ref:`Idle Timeout <mwlIdleTimeout-dcmDuration>`",string,"Timeout after which the Status of matching Scheduled Procedure Steps is changed to the specified final status.

    (dcmDuration)"
