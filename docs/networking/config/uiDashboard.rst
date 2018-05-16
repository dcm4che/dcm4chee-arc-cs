UI Dashboard Configuration
==========================
UI Dashboard Configuration

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: UI Dashboard Configuration Attributes (LDAP Object: dcmUiDashboard)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "UI Dashboard Configuration Name",string,"UI Dashboard Configuration Name","
    .. _dcmuiDashboardConfigName:

    dcmuiDashboardConfigName_"
    "Queues(s)",string,"Queue Names for UI Dashboard Configuration used in queue block","
    .. _dcmuiQueueName:

    dcmuiQueueName_"
    "Device Names(s)",string,"Device Names for UI Dashboard Configuration used for generating the Retrieve and Export block","
    .. _dicomuiDeviceName:

    dicomuiDeviceName_"
    "Audit Events Ignore Parameters(s)",string,"Set Elasticsearch parameters that should be ignored in the Audit Events. E.g. Source.UserID=TESTVALUE","
    .. _dicomuiIgnoreParams:

    dicomuiIgnoreParams_"
    "Count Aet",string,"Selected Aet will be used to get the count of studies in the dashboard","
    .. _dcmuiCountAET:

    dcmuiCountAET_"
