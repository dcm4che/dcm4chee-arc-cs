Web Application
===============
Web Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Web Application Attributes (LDAP Object: dcmWebApplication)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmWebAppName:

    :ref:`Web Application name (dcmWebAppName) <dcmWebAppName>`",string,"Name of the Web Application"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Web Application Network Connection(s)(s) (dicomNetworkConnectionReference) <dicomNetworkConnectionReference>`",string,"Network Connection(s) on which the services of the Web application are available"
    "
    .. _dicomDescription:

    :ref:`Web Application Description (dicomDescription) <dicomDescription>`",string,"Unconstrained text description of the Web Application"
    "
    .. _dcmWebServicePath:

    :ref:`Web Service Path (dcmWebServicePath) <dcmWebServicePath>`",string,"HTTP Path of the services of the Web application"
    "
    .. _dcmWebServiceClass:

    :ref:`Web Service Class(s) (dcmWebServiceClass) <dcmWebServiceClass>`",string,"Web Service Classes provided by the Web application Enumerated values: QIDO_RS, STOW_RS, WADO_RS, WADO_URI, UPS_RS or DCM4CHEE_ARC"
    "
    .. _dicomAETitle:

    :ref:`AE Title (dicomAETitle) <dicomAETitle>`",string,"AE title of Network AE associated with this Web Application"
    "
    .. _dicomApplicationCluster:

    :ref:`Application Cluster(s) (dicomApplicationCluster) <dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications"
    "
    .. _dicomInstalled:

    :ref:`installed (dicomInstalled) <dicomInstalled>`",boolean,"True if the Web Application is installed on network. If not present, information about the installed status of the Web Application is inherited from the device"
