Web Application
===============
Web Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Web Application Attributes (LDAP Object: dcmWebApplication)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Web Application name",string,"Name of the Web Application","
    .. _dcmWebAppName:

    dcmWebAppName_"
    "Web Application Network Connection(s)(s)",string,"Network Connection(s) on which the services of the Web application are available","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "Web Application Description",string,"Unconstrained text description of the Web Application","
    .. _dicomDescription:

    dicomDescription_"
    "Web Service Path",string,"HTTP Path of the services of the Web application","
    .. _dcmWebServicePath:

    dcmWebServicePath_"
    "Web Service Class(s)",string,"Web Service Classes provided by the Web application Enumerated values: QIDO_RS, STOW_RS, WADO_RS, WADO_URI, UPS_RS or DCM4CHEE_ARC","
    .. _dcmWebServiceClass:

    dcmWebServiceClass_"
    "AE Title",string,"AE title of Network AE associated with this Web Application","
    .. _dicomAETitle:

    dicomAETitle_"
    "Application Cluster(s)",string,"Locally defined names for a subset of related applications","
    .. _dicomApplicationCluster:

    dicomApplicationCluster_"
    "installed",boolean,"True if the Web Application is installed on network. If not present, information about the installed status of the Web Application is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
