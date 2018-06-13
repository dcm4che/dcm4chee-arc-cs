UI Dashboard Configuration
==========================
UI Dashboard Configuration

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Dashboard Configuration Attributes (LDAP Object: dcmUiDashboard)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmuiDashboardConfigName:

    :ref:`UI Dashboard Configuration Name (dcmuiDashboardConfigName) <dcmuiDashboardConfigName>`",string,"UI Dashboard Configuration Name"
    "
    .. _dcmuiQueueName:

    :ref:`Queues(s) (dcmuiQueueName) <dcmuiQueueName>`",string,"Queue Names for UI Dashboard Configuration used in queue block"
    "
    .. _dicomuiDeviceName:

    :ref:`Device Names(s) (dicomuiDeviceName) <dicomuiDeviceName>`",string,"Device Names for UI Dashboard Configuration used for generating the Retrieve and Export block"
    "
    .. _dicomuiIgnoreParams:

    :ref:`Audit Events Ignore Parameters(s) (dicomuiIgnoreParams) <dicomuiIgnoreParams>`",string,"Set Elasticsearch parameters that should be ignored in the Audit Events. E.g. Source.UserID=TESTVALUE"
    "
    .. _dcmuiCountAET:

    :ref:`Count Aet (dcmuiCountAET) <dcmuiCountAET>`",string,"Selected Aet will be used to get the count of studies in the dashboard"
    ":doc:`uiCompareSide` (s)",object,"Compare Sides"

.. toctree::

    uiCompareSide
