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
    .. _dcmuiHideOtherPatientIDs:

    :ref:`Hide Other Patient IDs <dcmuiHideOtherPatientIDs>`",boolean,"Indicates if other patient identifiers of patient record present in Other Patient IDs Sequence (0010,1002) shall be hidden. By default, all patient identifiers of patient record are displayed separated by comma.

    (dcmuiHideOtherPatientIDs)"
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
    "
    .. _dcmuiInstitutionNameFilterType:

    :ref:`Institution Name Filter Type <dcmuiInstitutionNameFilterType>`",string,"This will define how the Institution Name filter used in the Navigation Page should be displayed and if there should be a prefilled dropdown and where to get those data from

    Enumerated values:

    simple_filed (= Simple input field (= Simple input field)

    ui_config (= Dropdown by using this config ( See next field 'Institution Names' ) (= Dropdown by using this config)

    db (= Dropdown will be prefilled with the strings coming by calling the service '../institutions' (= Dropdown by querying the Database)

    (dcmuiInstitutionNameFilterType)"
    "
    .. _dcmuiInstitutionName:

    :ref:`Institution Names(s) <dcmuiInstitutionName>`",string,"This will be used in combination with the previous field 'Institution Name Filter Type' to prefill the Dropdown of the Filter Institution Names in the Navigation Page

    (dcmuiInstitutionName)"
    "
    .. _dcmuiIssuerOfPatientIDSequence:

    :ref:`Issuer of Patient ID Sequence(s) <dcmuiIssuerOfPatientIDSequence>`",string,"This will be used to show a dropdown in the Patient Identifier widget instead of the Issuer of Patient ID, Issuer of Patient ID Qualifiers Sequence - Universal Entity ID and Issuer of Patient ID Qualifiers Sequence - Universal Entity ID Type input fields. You can use the & character between the strings to mark the different fields like: 'issuerOfP&ipIDQuSeUniversalEntityID&ipIDQuSeUniversalEntityIDType'

    (dcmuiIssuerOfPatientIDSequence)"
    "
    .. _dcmuiIssuerOfAccessionNumberSequence:

    :ref:`Issuer of Accession Number Sequence(s) <dcmuiIssuerOfAccessionNumberSequence>`",string,"This will be used to show a dropdown in the Accession Number widget instead of the ""Local Namespace Entity ID"", ""Universal Entity ID"" and ""Universal Entity ID Type"" input fields. You can use the ^ character between the strings to mark the different fields like: 'dummylNamespace^uEntityID^uEntityIDType'

    (dcmuiIssuerOfAccessionNumberSequence)"
    "
    .. _dcmuiIssuerOfAdmissionIDSequence:

    :ref:`Issuer of Admission ID Sequence(s) <dcmuiIssuerOfAdmissionIDSequence>`",string,"This will be used to show a dropdown in the Admission ID widget instead of the ""Local Namespace Entity ID"",""Universal Entity ID"" and ""Universal Entity ID Type"" input fields. You can use the & character between the strings to mark the different fields like: 'dummylNamespace&uEntityID&uEntityIDType'

    (dcmuiIssuerOfAdmissionIDSequence)"
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
