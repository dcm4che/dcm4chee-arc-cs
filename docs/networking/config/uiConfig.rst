UI Configuration
================
UI Configuration

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Configuration Attributes (LDAP Object: dcmUiConfig)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiConfigName:
    .. _uiConfig-dcmuiConfigName:

    :ref:`UI Configuration Name <uiConfig-dcmuiConfigName>`",string,"UI Configuration Name

    (dcmuiConfigName)"
    "
    .. _dcmuiModalities:
    .. _uiConfig-dcmuiModalities:

    :ref:`Statistic Modalities(s) <uiConfig-dcmuiModalities>`",string,"Preselected Modalities that should show in the Statistic page

    (dcmuiModalities)"
    ":doc:`uiLanguage` (s)",object,"Config the languages of the UI"
    "
    .. _dcmuiWidgetAets:
    .. _uiConfig-dcmuiWidgetAets:

    :ref:`Widget AETs(s) <uiConfig-dcmuiWidgetAets>`",string,"Select the AETs that you wan't to see in the AET widget, where you can select in which of them the newly added AET should be as `Accepted Calling AE Title`

    (dcmuiWidgetAets)"
    "
    .. _dcmuiHideOtherPatientIDs:
    .. _uiConfig-dcmuiHideOtherPatientIDs:

    :ref:`Hide Other Patient IDs <uiConfig-dcmuiHideOtherPatientIDs>`",boolean,"Indicates if other patient identifiers of patient record present in Other Patient IDs Sequence (0010,1002) shall be hidden. By default, all patient identifiers of patient record are displayed separated by comma.

    (dcmuiHideOtherPatientIDs)"
    "
    .. _dcmuiDateTimeFormat:
    .. _uiConfig-dcmuiDateTimeFormat:

    :ref:`Format Date Time <uiConfig-dcmuiDateTimeFormat>`",string,"Here you can format the date time in the UI by using 'yyyy' for the year, 'MM' for the Month, 'dd' for the date, 'HH' for the hour 'mm' for the minutes, 'ss' for the seconds and 'SSS' for milliseconds. To format Date, Time and Date-Time you should use `DATE`, `TIME` and `DATE-TIME` for example like this: `DATE=yyyy-MM-dd, TIME=HH:mm, DATE-TIME=yyyy-MM-dd HH:mm`

    (dcmuiDateTimeFormat)"
    "
    .. _dcmuiHideClock:
    .. _uiConfig-dcmuiHideClock:

    :ref:`Hide Clock <uiConfig-dcmuiHideClock>`",boolean,"Set to true if you want to hide the clock in the UI

    (dcmuiHideClock)"
    "
    .. _dcmuiPageTitle:
    .. _uiConfig-dcmuiPageTitle:

    :ref:`Page Title <uiConfig-dcmuiPageTitle>`",string,"If set, it will be used as UI page Title ( The Text shown in the Tab of the Browser ) 

    (dcmuiPageTitle)"
    "
    .. _dcmuiPersonNameFormat:
    .. _uiConfig-dcmuiPersonNameFormat:

    :ref:`Format Person Name <uiConfig-dcmuiPersonNameFormat>`",string,"Here you can format the person Name in the UI by using:{FAMILY-NAME}, {GIVEN-NAME}, {MIDDLE-NAME}, {NAME-PREFIX}, {NAME-SUFFIX} for Alphabetic, or by appending 'I_' for the Ideographic and 'P_' for the Phonetic version like {P_FAMILY-NAME}, {I_NAME-SUFFIX}

    (dcmuiPersonNameFormat)"
    "
    .. _dcmuiDefaultWidgetAets:
    .. _uiConfig-dcmuiDefaultWidgetAets:

    :ref:`Default Widget AETs(s) <uiConfig-dcmuiDefaultWidgetAets>`",string,"Select the AETs that should be preselected on Widget AETs

    (dcmuiDefaultWidgetAets)"
    "
    .. _dcmuiMWLWorklistLabel:
    .. _uiConfig-dcmuiMWLWorklistLabel:

    :ref:`MWL Worklist Label(s) <uiConfig-dcmuiMWLWorklistLabel>`",string,"Selectable values for MWL Worklist Label

    (dcmuiMWLWorklistLabel)"
    "
    .. _dcmuiInstitutionNameFilterType:
    .. _uiConfig-dcmuiInstitutionNameFilterType:

    :ref:`Institution Name Filter Type <uiConfig-dcmuiInstitutionNameFilterType>`",string,"This will define how the Institution Name filter used in the Navigation Page should be displayed and if there should be a prefilled dropdown and where to get those data from

    Enumerated values:

    simple_filed (= Simple input field (= Simple input field)

    ui_config (= Dropdown by using this config ( See next field 'Institution Names' ) (= Dropdown by using this config)

    db (= Dropdown will be prefilled with the strings coming by calling the service '../institutions' (= Dropdown by querying the Database)

    (dcmuiInstitutionNameFilterType)"
    "
    .. _dcmuiInstitutionName:
    .. _uiConfig-dcmuiInstitutionName:

    :ref:`Institution Names(s) <uiConfig-dcmuiInstitutionName>`",string,"This will be used in combination with the previous field 'Institution Name Filter Type' to prefill the Dropdown of the Filter Institution Names in the Navigation Page

    (dcmuiInstitutionName)"
    "
    .. _dcmuiIssuerOfPatientIDSequence:
    .. _uiConfig-dcmuiIssuerOfPatientIDSequence:

    :ref:`Issuer of Patient ID Sequence(s) <uiConfig-dcmuiIssuerOfPatientIDSequence>`",string,"This will be used to show a dropdown in the Patient Identifier widget instead of the Issuer of Patient ID, Issuer of Patient ID Qualifiers Sequence - Universal Entity ID and Issuer of Patient ID Qualifiers Sequence - Universal Entity ID Type input fields. You can use the & character between the strings to mark the different fields like: 'issuerOfP&ipIDQuSeUniversalEntityID&ipIDQuSeUniversalEntityIDType'

    (dcmuiIssuerOfPatientIDSequence)"
    "
    .. _dcmuiIssuerOfAccessionNumberSequence:
    .. _uiConfig-dcmuiIssuerOfAccessionNumberSequence:

    :ref:`Issuer of Accession Number Sequence(s) <uiConfig-dcmuiIssuerOfAccessionNumberSequence>`",string,"This will be used to show a dropdown in the Accession Number widget instead of the ""Local Namespace Entity ID"", ""Universal Entity ID"" and ""Universal Entity ID Type"" input fields. You can use the ^ character between the strings to mark the different fields like: 'dummylNamespace^uEntityID^uEntityIDType'

    (dcmuiIssuerOfAccessionNumberSequence)"
    "
    .. _dcmuiIssuerOfAdmissionIDSequence:
    .. _uiConfig-dcmuiIssuerOfAdmissionIDSequence:

    :ref:`Issuer of Admission ID Sequence(s) <uiConfig-dcmuiIssuerOfAdmissionIDSequence>`",string,"This will be used to show a dropdown in the Admission ID widget instead of the ""Local Namespace Entity ID"",""Universal Entity ID"" and ""Universal Entity ID Type"" input fields. You can use the & character between the strings to mark the different fields like: 'dummylNamespace&uEntityID&uEntityIDType'

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
