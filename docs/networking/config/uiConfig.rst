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
    ":doc:`uiLanguage` (s)",object,"Config the languages of the UI"
    "
    .. _dcmuiWidgetAets:

    :ref:`Widget AETs(s) <dcmuiWidgetAets>`",string,"Select the AETs that you wan't to see in the AET widget, where you can select in which of them the newly added AET should be as `Accepted Calling AE Title`

    (dcmuiWidgetAets)"
    "
    .. _dcmuiBackgroundURL:

    :ref:`Background URL <dcmuiBackgroundURL>`",string,"Background URL for changing the background of the UI, it can be relative or absolute URL, the image should have the width of at least of 1024px 

    (dcmuiBackgroundURL)"
    "
    .. _dcmuiLogoURL:

    :ref:`Logo URL <dcmuiLogoURL>`",string,"Logo URL for changing the logo of the UI, it can be relative or absolute URL, the image should have the width of 140px and should be in format png with the transparent background

    (dcmuiLogoURL)"
    "
    .. _dcmuiDefaultWidgetAets:

    :ref:`Default Widget AETs(s) <dcmuiDefaultWidgetAets>`",string,"Select the AETs that should be preselected on Widget AETs

    (dcmuiDefaultWidgetAets)"
    ":doc:`uiAet` (s)",object,"Define which AETs should be visible in the drop-down lists in the UI"
    ":doc:`uiWebApp` (s)",object,"Define which WebApps should be visible on the top of the drop-down list in the UI"
    ":doc:`uiPermission` (s)",object,"Permission"
    ":doc:`uiFilterTemplate` (s)",object,"Defined filter template"
    ":doc:`uiDiffConfig` (s)",object,"Study Diff Configuration"
    ":doc:`uiDashboard` (s)",object,"UI Dashboard Configuration"
    ":doc:`uiTable` (s)",object,"Configuration of table"
    ":doc:`uiElasticsearch` (s)",object,"Elasticsearch Configuration for the pro version"
    ":doc:`uiDeviceURL` (s)",object,"Other UI Device URLs"
    ":doc:`uiDeviceCluster` (s)",object,"Group Devices in Clusters"

.. toctree::

    uiLanguage
    uiAet
    uiWebApp
    uiPermission
    uiFilterTemplate
    uiDiffConfig
    uiDashboard
    uiTable
    uiElasticsearch
    uiDeviceURL
    uiDeviceCluster
