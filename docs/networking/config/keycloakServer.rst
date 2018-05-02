Keycloak Server
===============
Keycloak Server

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Keycloak Server Attributes (LDAP Object: dcmKeycloakServer)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Keycloak Server ID",string,"Keycloak Server ID","
    .. _dcmKeycloakServerID:

    dcmKeycloakServerID_"
    "Server URL",string,"The base URL of the Keycloak server.","
    .. _dcmURI:

    dcmURI_"
    "Keycloak Realm",string,"Name of the realm in token requests to Keycloak.","
    .. _dcmKeycloakRealm:

    dcmKeycloakRealm_"
    "OAuth 2.0 Client ID",string,"Client ID used in token requests to Keycloak.","
    .. _dcmKeycloakClientID:

    dcmKeycloakClientID_"
    "OAuth 2.0 grant type",string,"OAuth 2.0 grant type. Enumerated values: password or client_credentials","
    .. _dcmKeycloakGrantType:

    dcmKeycloakGrantType_"
    "OAuth Client secret",string,"OAuth client secret. Required if grant type = client_credentials.","
    .. _dcmKeycloakClientSecret:

    dcmKeycloakClientSecret_"
    "User ID",string,"User ID. Required if grant type = password.","
    .. _uid:

    uid_"
    "User Password",string,"User Password. Required if grant type = password.","
    .. _userPassword:

    userPassword_"
