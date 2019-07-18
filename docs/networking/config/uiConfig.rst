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
    "
    .. _dcmuiModalities:

    :ref:`Statistic Modalities(s) <dcmuiModalities>`",string,"Preselected Modalities that should show in the Statistic page

    (dcmuiModalities)"
    "
    .. _dcmuiWidgetAets:

    :ref:`Widget AETs(s) <dcmuiWidgetAets>`",string,"Select the AETs that you wan't to see in the AET widget, where you can select in which of them the newly added AET should be as `Accepted Calling AE Title`

    (dcmuiWidgetAets)"
    "
    .. _dcmuiDefaultWidgetAets:

    :ref:`Default Widget AETs(s) <dcmuiDefaultWidgetAets>`",string,"Select the AETs that should be preselected on Widget AETs

    (dcmuiDefaultWidgetAets)"
    ":doc:`uiAet` (s)",object,"Define which AETs should be visible in the drop-down lists in the UI"
    ":doc:`uiPermission` (s)",object,"Permission"
    ":doc:`uiFilterTemplate` (s)",object,"Defined filter template"
    ":doc:`uiDiffConfig` (s)",object,"Study Diff Configuration"
    ":doc:`uiDashboard` (s)",object,"UI Dashboard Configuration"
    ":doc:`uiTable` (s)",object,"Configuration of table"
    ":doc:`uiElasticsearch` (s)",object,"Elasticsearch Configuration for the pro version"
    ":doc:`uiDeviceURL` (s)",object,"Other UI Device URLs"
    ":doc:`uiDeviceCluster` (s)",object,"Group Devices in Clusters"

.. toctree::

    uiAet
    uiPermission
    uiFilterTemplate
    uiDiffConfig
    uiDashboard
    uiTable
    uiElasticsearch
    uiDeviceURL
    uiDeviceCluster
