RESTful Forward Rule
====================
RESTful Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: RESTful Forward Rule Attributes (LDAP Object: dcmRsForwardRule)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name of the RESTful Forward Rule","
    .. _cn:

    cn_"
    "Target Base URL",string,"Target URL without operation specific part, eg. http://<host>:<port>/dcm4chee-arc/aets/<aet>/rs/","
    .. _dcmURI:

    dcmURI_"
    "Keycloak Server ID",string,"Identifier of the Keycloak Server from which the access token shall be granted. If absent, no token will be sent.","
    .. _dcmKeycloakServerID:

    dcmKeycloakServerID_"
    "TLS Allow Any Hostname",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done.","
    .. _dcmTLSAllowAnyHostname:

    dcmTLSAllowAnyHostname_"
    "TLS Disable Trust Manager",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore","
    .. _dcmTLSDisableTrustManager:

    dcmTLSDisableTrustManager_"
    "RESTful Operation(s)",string,"Name of RESTful Operation which shall be forwarded to another archive instance. Enumerated values: CreatePatient, UpdatePatient, DeletePatient, ChangePatientID, MergePatient, MergePatients, UpdateStudy, DeleteStudy, RejectStudy, RejectSeries, RejectInstance, UpdateStudyExpirationDate, UpdateSeriesExpirationDate, CreateMWL, UpdateMWL or DeleteMWL","
    .. _dcmRSOperation:

    dcmRSOperation_"
