UI Configuration
================
UI Configuration

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Configuration Attributes (LDAP Object: dcmUiConfig)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiConfigName:

    :ref:`UI Configuration Name <dcmuiConfigName>`",string,"UI Configuration Name

    (dcmuiConfigName)"
    ":doc:`uiPermission` (s)",object,"Permission

    (dcmuiPermission)"
    ":doc:`uiDiffConfig` (s)",object,"Study Diff Configuration

    (dcmuiDiffConfig)"
    ":doc:`uiDashboard` (s)",object,"UI Dashboard Configuration

    (dcmuiDashboardConfig)"
    ":doc:`uiElasticsearch` (s)",object,"Elasticsearch Configuration for the pro version

    (dcmuiElasticsearchConfig)"
    ":doc:`uiDeviceURL` (s)",object,"Other UI Device URLs

    (dcmuiDeviceURLObject)"
    ":doc:`uiDeviceCluster` (s)",object,"Group Devices in Clusters

    (dcmuiDeviceClusterObject)"

.. toctree::

    uiPermission
    uiDiffConfig
    uiDashboard
    uiElasticsearch
    uiDeviceURL
    uiDeviceCluster
