Web Application
===============
Web Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Web Application Attributes (LDAP Object: dcmWebApplication)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmWebAppName:

    :ref:`Web Application name <dcmWebAppName>`",string,"Name of the Web Application

    (dcmWebAppName)"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Web Application Network Connection(s)(s) <dicomNetworkConnectionReference>`",string,"Network Connection(s) on which the services of the Web application are available

    (dicomNetworkConnectionReference)"
    "
    .. _dicomDescription:

    :ref:`Web Application Description <dicomDescription>`",string,"Unconstrained text description of the Web Application

    (dicomDescription)"
    "
    .. _dcmWebServicePath:

    :ref:`Web Service Path <dcmWebServicePath>`",string,"HTTP Path of the services of the Web application

    (dcmWebServicePath)"
    "
    .. _dcmWebServiceClass:

    :ref:`Web Service Class(s) <dcmWebServiceClass>`",string,"Web Service Classes provided by the Web application Enumerated values: QIDO_RS, STOW_RS, WADO_RS, WADO_URI, UPS_RS, MWL_RS, QIDO_COUNT, DCM4CHEE_ARC, DCM4CHEE_ARC_AET, DCM4CHEE_ARC_AET_DIFF, PAM, REJECT, MOVE, MOVE_MATCHING or ELASTICSEARCH.

    (dcmWebServiceClass)"
    "
    .. _dcmKeycloakClientID:

    :ref:`Keycloak Client ID <dcmKeycloakClientID>`",string,"Keycloak Client ID for the Web application

    (dcmKeycloakClientID)"
    "
    .. _dicomAETitle:

    :ref:`AE Title <dicomAETitle>`",string,"AE title of Network AE associated with this Web Application

    (dicomAETitle)"
    "
    .. _dicomApplicationCluster:

    :ref:`Application Cluster(s) <dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications

    (dicomApplicationCluster)"
    "
    .. _dcmProperty:

    :ref:`Property(s) <dcmProperty>`",string,"Property in format <name>=<value>. E.g.: roles=<accepted-user-role>[,...], IID_PATIENT_URL=http(s)://<viewer-host>:<viewer-port>/IHEInvokeImageDisplay?requestType=PATIENT&patientID={{patientID}} or IID_STUDY_URL=http(s)://<viewer-host>:<viewer-port>/IHEInvokeImageDisplay?requestType=STUDY&studyUID={{studyUID}}, ( Other valid parameters are: 'patientBirthDate' and 'accessionNumber' ) , you could define the target of the Url by setting it to the parameter 'IID_URL_TARGET=_blank|_self'

    (dcmProperty)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"True if the Web Application is installed on network. If not present, information about the installed status of the Web Application is inherited from the device

    (dicomInstalled)"
