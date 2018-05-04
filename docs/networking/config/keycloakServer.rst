Keycloak Server
===============
Keycloak Server

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Keycloak Server Attributes (LDAP Object: dcmKeycloakServer)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Keycloak Server ID",string,"Identifier for this Keycloak Server.","
    .. _dcmKeycloakServerID:

    dcmKeycloakServerID_"
    "Server URL",string,"The base URL of the Keycloak server.","
    .. _dcmURI:

    dcmURI_"
    "Keycloak Realm",string,"Name of the realm in token requests.","
    .. _dcmKeycloakRealm:

    dcmKeycloakRealm_"
    "OAuth 2.0 Client ID",string,"Client ID used in token requests.","
    .. _dcmKeycloakClientID:

    dcmKeycloakClientID_"
    "OAuth 2.0 grant type",string,"OAuth 2.0 grant type used in token requests. Enumerated values: client_credentials or password","
    .. _dcmKeycloakGrantType:

    dcmKeycloakGrantType_"
    "OAuth Client secret",string,"OAuth client secret. Required if grant type = client_credentials.","
    .. _dcmKeycloakClientSecret:

    dcmKeycloakClientSecret_"
    "TLS Allow Any Hostname",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done.","
    .. _dcmTLSAllowAnyHostname:

    dcmTLSAllowAnyHostname_"
    "TLS Disable Trust Manager",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore","
    .. _dcmTLSDisableTrustManager:

    dcmTLSDisableTrustManager_"
    "User ID",string,"User ID. Required if grant type = password.","
    .. _uid:

    uid_"
    "User Password",string,"User Password. Required if grant type = password.","
    .. _userPassword:

    userPassword_"
