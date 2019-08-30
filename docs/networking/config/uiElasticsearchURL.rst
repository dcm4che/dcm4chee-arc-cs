UI Elasticsearch URL Configuration
==================================
Elasticsearch URL

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Elasticsearch URL Configuration Attributes (LDAP Object: dcmUiElasticsearchURL)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiElasticsearchURLName:

    :ref:`Elasticsearch URL Name <dcmuiElasticsearchURLName>`",string,"UI Elasticsearch URL Name

    (dcmuiElasticsearchURLName)"
    "
    .. _dcmuiElasticsearchURL:

    :ref:`Elasticsearch URL <dcmuiElasticsearchURL>`",string,"Access URL of Elastic Search. E.g. http(s)://<elasticsearch-host>:<elasticsearch-port>

    (dcmuiElasticsearchURL)"
    "
    .. _dcmuiElasticsearchURLKeycloakServer:

    :ref:`Keycloak Server <dcmuiElasticsearchURLKeycloakServer>`",string,"Select Keycloak Server from where to get the bearer token for accessing the Elasticsearch

    (dcmuiElasticsearchURLKeycloakServer)"
    "
    .. _dcmuiAuditEnterpriseSiteID:

    :ref:`Audit Enterprise SiteID <dcmuiAuditEnterpriseSiteID>`",string,"Set Audit Enterprise SiteID which should be used on Elasticsearch queries

    (dcmuiAuditEnterpriseSiteID)"
    "
    .. _dcmuiElasticsearchIsDefault:

    :ref:`Is Default <dcmuiElasticsearchIsDefault>`",boolean,"Set this URL to the default one. (Make sure that only one of the urls - siblings child is set to default).

    (dcmuiElasticsearchIsDefault)"
    "
    .. _dcmuiElasticsearchInstalled:

    :ref:`Installed <dcmuiElasticsearchInstalled>`",boolean,"Use this URL in the UI

    (dcmuiElasticsearchInstalled)"
