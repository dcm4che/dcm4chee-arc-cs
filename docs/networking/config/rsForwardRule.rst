RESTful Forward Rule
====================
RESTful Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: RESTful Forward Rule Attributes (LDAP Object: dcmRsForwardRule)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name of the RESTful Forward Rule"
    "
    .. _dcmURI:

    :ref:`Target Base URL (dcmURI) <dcmURI>`",string,"Target URL without operation specific part, eg. http://<host>:<port>/dcm4chee-arc/aets/<aet>/rs/"
    "
    .. _dcmKeycloakServerID:

    :ref:`Keycloak Server ID (dcmKeycloakServerID) <dcmKeycloakServerID>`",string,"Identifier of the Keycloak Server from which the access token shall be granted. If absent, no token will be sent."
    "
    .. _dcmTLSAllowAnyHostname:

    :ref:`TLS Allow Any Hostname (dcmTLSAllowAnyHostname) <dcmTLSAllowAnyHostname>`",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done."
    "
    .. _dcmTLSDisableTrustManager:

    :ref:`TLS Disable Trust Manager (dcmTLSDisableTrustManager) <dcmTLSDisableTrustManager>`",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore"
    "
    .. _dcmRSOperation:

    :ref:`RESTful Operation(s) (dcmRSOperation) <dcmRSOperation>`",string,"Name of RESTful Operation which shall be forwarded to another archive instance. Enumerated values: CreatePatient, UpdatePatient, DeletePatient, ChangePatientID, MergePatient, MergePatients, UpdateStudy, DeleteStudy, RejectStudy, RejectSeries, RejectInstance, UpdateStudyExpirationDate, UpdateSeriesExpirationDate, CreateMWL, UpdateMWL or DeleteMWL"
