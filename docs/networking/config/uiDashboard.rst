UI Dashboard Configuration
==========================
UI Dashboard Configuration

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Dashboard Configuration Attributes (LDAP Object: dcmUiDashboard)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiDashboardConfigName:

    :ref:`UI Dashboard Configuration Name <dcmuiDashboardConfigName>`",string,"UI Dashboard Configuration Name

    (dcmuiDashboardConfigName)"
    "
    .. _dcmuiQueueName:

    :ref:`Queues(s) <dcmuiQueueName>`",string,"Queue Names for UI Dashboard Configuration used in queue block

    (dcmuiQueueName)"
    "
    .. _dcmuiExportName:

    :ref:`Exporter IDs(s) <dcmuiExportName>`",string,"Exporter ID-s for UI Dashboard Configuration used in queue and compare block

    (dcmuiExportName)"
    "
    .. _dicomuiDeviceName:

    :ref:`Device Names(s) <dicomuiDeviceName>`",string,"Device Names for UI Dashboard Configuration used for generating the Retrieve and Export block

    (dicomuiDeviceName)"
    "
    .. _dicomuiIgnoreParams:

    :ref:`Audit Events Ignore Parameters(s) <dicomuiIgnoreParams>`",string,"Set Elasticsearch parameters that should be ignored in the Audit Events. E.g. Source.UserID=TESTVALUE

    (dicomuiIgnoreParams)"
    "
    .. _dcmuiCountAET:

    :ref:`Count Aet <dcmuiCountAET>`",string,"Selected Aet will be used to get the count of studies in the dashboard

    (dcmuiCountAET)"
    ":doc:`uiCompareSide` (s)",object,"Compare Sides"
    "
    .. _dicomuiDockerContainer:

    :ref:`Archive Docker Containers(s) <dicomuiDockerContainer>`",string,"Names of the archive docker containers used in the hardware page

    (dicomuiDockerContainer)"

.. toctree::

    uiCompareSide
