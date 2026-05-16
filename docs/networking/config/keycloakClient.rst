Keycloak Client
===============
Keycloak Client

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Keycloak Client Attributes (LDAP Object: dcmKeycloakClient)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmKeycloakClientID:
    .. _keycloakClient-dcmKeycloakClientID:

    :ref:`Keycloak Client ID <keycloakClient-dcmKeycloakClientID>`",string,"Client ID used in token requests.

    (dcmKeycloakClientID)"
    "
    .. _dcmURI:
    .. _keycloakClient-dcmURI:

    :ref:`Server URL <keycloakClient-dcmURI>`",string,"The base URL of the Keycloak server.

    (dcmURI)"
    "
    .. _dcmKeycloakRealm:
    .. _keycloakClient-dcmKeycloakRealm:

    :ref:`Keycloak Realm <keycloakClient-dcmKeycloakRealm>`",string,"Name of the realm in token requests.

    (dcmKeycloakRealm)"
    "
    .. _dcmKeycloakGrantType:
    .. _keycloakClient-dcmKeycloakGrantType:

    :ref:`Keycloak grant type <keycloakClient-dcmKeycloakGrantType>`",string,"Keycloak grant type used in token requests.

    Enumerated values:

    client_credentials

    password

    (dcmKeycloakGrantType)"
    "
    .. _dcmKeycloakClientSecret:
    .. _keycloakClient-dcmKeycloakClientSecret:

    :ref:`Keycloak Client secret <keycloakClient-dcmKeycloakClientSecret>`",string,"Keycloak client secret. Required if grant type = client_credentials.

    (dcmKeycloakClientSecret)"
    "
    .. _dcmTLSAllowAnyHostname:
    .. _keycloakClient-dcmTLSAllowAnyHostname:

    :ref:`TLS Allow Any Hostname <keycloakClient-dcmTLSAllowAnyHostname>`",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done.

    (dcmTLSAllowAnyHostname)"
    "
    .. _dcmTLSDisableTrustManager:
    .. _keycloakClient-dcmTLSDisableTrustManager:

    :ref:`TLS Disable Trust Manager <keycloakClient-dcmTLSDisableTrustManager>`",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore

    (dcmTLSDisableTrustManager)"
    "
    .. _uid:
    .. _keycloakClient-uid:

    :ref:`User ID <keycloakClient-uid>`",string,"User ID. Required if grant type = password.

    (uid)"
    "
    .. _userPassword:
    .. _keycloakClient-userPassword:

    :ref:`User Password <keycloakClient-userPassword>`",string,"User Password. Required if grant type = password.

    (userPassword)"
