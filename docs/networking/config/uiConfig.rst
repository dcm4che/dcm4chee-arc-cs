UI Configuration
================
UI Configuration

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Configuration Attributes (LDAP Object: dcmUiConfig)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmuiConfigName:

    :ref:`UI Configuration Name (dcmuiConfigName) <dcmuiConfigName>`",string,"UI Configuration Name"
    ":doc:`uiPermission` (s)",object,"Permission"
    ":doc:`uiDiffConfig` (s)",object,"Study Diff Configuration"
    ":doc:`uiDashboard` (s)",object,"UI Dashboard Configuration"
    ":doc:`uiElasticsearch` (s)",object,"Elasticsearch Configuration for the pro version"
    ":doc:`uiDeviceURL` (s)",object,"Other UI Device URLs"
    ":doc:`uiDeviceCluster` (s)",object,"Group Devices in Clusters"

.. toctree::

    uiPermission
    uiDiffConfig
    uiDashboard
    uiElasticsearch
    uiDeviceURL
    uiDeviceCluster
