Keycloak Server
===============
Keycloak Server

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Keycloak Server Attributes (LDAP Object: dcmKeycloakServer)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmKeycloakServerID:

    :ref:`Keycloak Server ID (dcmKeycloakServerID) <dcmKeycloakServerID>`",string,"Identifier for this Keycloak Server."
    "
    .. _dcmURI:

    :ref:`Server URL (dcmURI) <dcmURI>`",string,"The base URL of the Keycloak server."
    "
    .. _dcmKeycloakRealm:

    :ref:`Keycloak Realm (dcmKeycloakRealm) <dcmKeycloakRealm>`",string,"Name of the realm in token requests."
    "
    .. _dcmKeycloakClientID:

    :ref:`OAuth 2.0 Client ID (dcmKeycloakClientID) <dcmKeycloakClientID>`",string,"Client ID used in token requests."
    "
    .. _dcmKeycloakGrantType:

    :ref:`OAuth 2.0 grant type (dcmKeycloakGrantType) <dcmKeycloakGrantType>`",string,"OAuth 2.0 grant type used in token requests. Enumerated values: client_credentials or password"
    "
    .. _dcmKeycloakClientSecret:

    :ref:`OAuth Client secret (dcmKeycloakClientSecret) <dcmKeycloakClientSecret>`",string,"OAuth client secret. Required if grant type = client_credentials."
    "
    .. _dcmTLSAllowAnyHostname:

    :ref:`TLS Allow Any Hostname (dcmTLSAllowAnyHostname) <dcmTLSAllowAnyHostname>`",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done."
    "
    .. _dcmTLSDisableTrustManager:

    :ref:`TLS Disable Trust Manager (dcmTLSDisableTrustManager) <dcmTLSDisableTrustManager>`",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore"
    "
    .. _uid:

    :ref:`User ID (uid) <uid>`",string,"User ID. Required if grant type = password."
    "
    .. _userPassword:

    :ref:`User Password (userPassword) <userPassword>`",string,"User Password. Required if grant type = password."
