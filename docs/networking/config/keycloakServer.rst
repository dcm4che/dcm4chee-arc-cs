Keycloak Server
===============
Keycloak Server

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Keycloak Server Attributes (LDAP Object: dcmKeycloakServer)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmKeycloakServerID:

    :ref:`Keycloak Server ID <dcmKeycloakServerID>`",string,"Identifier for this Keycloak Server.

    (dcmKeycloakServerID)"
    "
    .. _dcmURI:

    :ref:`Server URL <dcmURI>`",string,"The base URL of the Keycloak server.

    (dcmURI)"
    "
    .. _dcmKeycloakRealm:

    :ref:`Keycloak Realm <dcmKeycloakRealm>`",string,"Name of the realm in token requests.

    (dcmKeycloakRealm)"
    "
    .. _dcmKeycloakClientID:

    :ref:`OAuth 2.0 Client ID <dcmKeycloakClientID>`",string,"Client ID used in token requests.

    (dcmKeycloakClientID)"
    "
    .. _dcmKeycloakGrantType:

    :ref:`OAuth 2.0 grant type <dcmKeycloakGrantType>`",string,"OAuth 2.0 grant type used in token requests. Enumerated values: client_credentials or password.

    (dcmKeycloakGrantType)"
    "
    .. _dcmKeycloakClientSecret:

    :ref:`OAuth Client secret <dcmKeycloakClientSecret>`",string,"OAuth client secret. Required if grant type = client_credentials.

    (dcmKeycloakClientSecret)"
    "
    .. _dcmTLSAllowAnyHostname:

    :ref:`TLS Allow Any Hostname <dcmTLSAllowAnyHostname>`",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done.

    (dcmTLSAllowAnyHostname)"
    "
    .. _dcmTLSDisableTrustManager:

    :ref:`TLS Disable Trust Manager <dcmTLSDisableTrustManager>`",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore

    (dcmTLSDisableTrustManager)"
    "
    .. _uid:

    :ref:`User ID <uid>`",string,"User ID. Required if grant type = password.

    (uid)"
    "
    .. _userPassword:

    :ref:`User Password <userPassword>`",string,"User Password. Required if grant type = password.

    (userPassword)"
