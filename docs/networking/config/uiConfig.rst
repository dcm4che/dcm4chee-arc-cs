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
    .. _dcmuiHideOtherPatientIDs:

    :ref:`Hide Other Patient IDs <dcmuiHideOtherPatientIDs>`",boolean,"Indicates if other patient identifiers of patient record present in Other Patient IDs Sequence (0010,1002) shall be hidden. By default, all patient identifiers of patient record are displayed separated by comma.

    (dcmuiHideOtherPatientIDs)"
    "
    .. _dcmuiLogoURL:

    :ref:`Logo URL <dcmuiLogoURL>`",string,"Logo URL for changing the logo of the UI, it can be relative or absolute URL, the image should have the width of 140px and should be in format png with the transparent background

    (dcmuiLogoURL)"
    "
    .. _dcmuiDateTimeFormat:

    :ref:`Format Date Time <dcmuiDateTimeFormat>`",string,"Here you can format the date time in the UI by using 'yyyy' for the year, 'MM' for the Month, 'dd' for the date, 'HH' for the hour 'mm' for the minutes, 'ss' for the seconds and 'SSS' for milliseconds. To format Date, Time and Date-Time you should use `DATE`, `TIME` and `DATE-TIME` for example like this: `DATE=yyyy-MM-dd, TIME=HH:mm, DATE-TIME=yyyy-MM-dd HH:mm`

    (dcmuiDateTimeFormat)"
    "
    .. _dcmuiHideClock:

    :ref:`Hide Clock <dcmuiHideClock>`",boolean,"Set to true if you want to hide the clock in the UI

    (dcmuiHideClock)"
    "
    .. _dcmuiPageTitle:

    :ref:`Page Title <dcmuiPageTitle>`",string,"If set, it will be used as UI page Title ( The Text shown in the Tab of the Browser ) 

    (dcmuiPageTitle)"
    "
    .. _dcmuiPersonNameFormat:

    :ref:`Format Person Name <dcmuiPersonNameFormat>`",string,"Here you can format the person Name in the UI by using:{FAMILY-NAME}, {GIVEN-NAME}, {MIDDLE-NAME}, {NAME-PREFIX}, {NAME-SUFFIX} for Alphabetic, or by appending 'I_' for the Ideographic and 'P_' for the Phonetic version like {P_FAMILY-NAME}, {I_NAME-SUFFIX}

    (dcmuiPersonNameFormat)"
    "
    .. _dcmuiDefaultWidgetAets:

    :ref:`Default Widget AETs(s) <dcmuiDefaultWidgetAets>`",string,"Select the AETs that should be preselected on Widget AETs

    (dcmuiDefaultWidgetAets)"
    "
    .. _dcmuiMWLWorklistLabel:

    :ref:`MWL Worklist Label(s) <dcmuiMWLWorklistLabel>`",string,"Selectable values for MWL Worklist Label

    (dcmuiMWLWorklistLabel)"
    ":doc:`uiAet` (s)",object,"Define which AETs should be visible in the drop-down lists in the UI"
    ":doc:`uiWebApp` (s)",object,"Define which WebApps should be visible on the top of the drop-down list in the UI"
    ":doc:`uiPermission` (s)",object,"Permission"
    ":doc:`uiFilterTemplate` (s)",object,"Defined filter template"
    ":doc:`uiDiffConfig` (s)",object,"Study Diff Configuration"
    ":doc:`uiTable` (s)",object,"Configuration of table"
    ":doc:`uiElasticsearch` (s)",object,"Elasticsearch Configuration for the pro version"
    ":doc:`uiDeviceCluster` (s)",object,"Group Devices in Clusters"
    ":doc:`uiDashboard` (s)",object,"UI Dashboard Configuration"
    ":doc:`uiDialogTemplate` (s)",object,"UI Create Dialog Templates Configuration"

.. toctree::

    uiLanguage
    uiAet
    uiWebApp
    uiPermission
    uiFilterTemplate
    uiDiffConfig
    uiTable
    uiElasticsearch
    uiDeviceCluster
    uiDashboard
    uiDialogTemplate
