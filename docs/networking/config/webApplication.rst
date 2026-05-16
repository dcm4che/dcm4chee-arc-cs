Web Application
===============
Web Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Web Application Attributes (LDAP Object: dcmWebApplication)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmWebAppName:
    .. _webApplication-dcmWebAppName:

    :ref:`Web Application name <webApplication-dcmWebAppName>`",string,"Name of the Web Application

    (dcmWebAppName)"
    "
    .. _dicomNetworkConnectionReference:
    .. _webApplication-dicomNetworkConnectionReference:

    :ref:`Web Application Network Connection(s) <webApplication-dicomNetworkConnectionReference>`",string,"Network Connection(s) on which the services of the Web application are available

    (dicomNetworkConnectionReference)"
    "
    .. _dicomDescription:
    .. _webApplication-dicomDescription:

    :ref:`Web Application Description <webApplication-dicomDescription>`",string,"Unconstrained text description of the Web Application

    (dicomDescription)"
    "
    .. _dcmWebServicePath:
    .. _webApplication-dcmWebServicePath:

    :ref:`Web Service Path <webApplication-dcmWebServicePath>`",string,"HTTP Path of the services of the Web application

    (dcmWebServicePath)"
    "
    .. _dcmWebServiceClass:
    .. _webApplication-dcmWebServiceClass:

    :ref:`Web Service Class(s) <webApplication-dcmWebServiceClass>`",string,"Web Service Classes provided by the Web application

    Enumerated values:

    QIDO_RS

    AI_CHAT

    DOCUMENTATION

    STOW_RS

    WADO_RS

    WADO_URI

    UPS_RS

    MWL_RS

    MPPS_RS

    QIDO_COUNT

    DCM4CHEE_ARC

    DCM4CHEE_ARC_AET

    DCM4CHEE_ARC_AET_DIFF

    PAM

    REJECT

    MOVE

    MOVE_MATCHING

    UPS_MATCHING

    ELASTICSEARCH

    PROMETHEUS

    GRAFANA

    XDS_RS

    AGFA_BLOB

    J4C_ROUTER

    FHIR

    WORKFLOW_MANAGER

    (dcmWebServiceClass)"
    "
    .. _dcmKeycloakClientID:
    .. _webApplication-dcmKeycloakClientID:

    :ref:`Keycloak Client ID <webApplication-dcmKeycloakClientID>`",string,"Keycloak Client ID for the Web application

    (dcmKeycloakClientID)"
    "
    .. _dicomAETitle:
    .. _webApplication-dicomAETitle:

    :ref:`AE Title <webApplication-dicomAETitle>`",string,"AE title of Network AE associated with this Web Application

    (dicomAETitle)"
    "
    .. _dicomApplicationCluster:
    .. _webApplication-dicomApplicationCluster:

    :ref:`Application Cluster(s) <webApplication-dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications

    (dicomApplicationCluster)"
    "
    .. _dcmProperty:
    .. _webApplication-dcmProperty:

    :ref:`Web Application Property(s) <webApplication-dcmProperty>`",string,"Web application property in format {name}={value}. Refer `Web Application Properties <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Web-Application-Properties>`_ configuration examples based on use cases.

    (dcmProperty)"
    "
    .. _dicomInstalled:
    .. _webApplication-dicomInstalled:

    :ref:`installed <webApplication-dicomInstalled>`",boolean,"True if the Web Application is installed on network. If not present, information about the installed status of the Web Application is inherited from the device

    (dicomInstalled)"
