Web App drop-down list
======================
Web App drop-down list

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Web App drop-down list Attributes (LDAP Object: dcmUiWebApp)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiWebAppListName:
    .. _uiWebApp-dcmuiWebAppListName:

    :ref:`List Name <uiWebApp-dcmuiWebAppListName>`",string,"Define a name for this config

    (dcmuiWebAppListName)"
    "
    .. _dcmuiWebAppListDescription:
    .. _uiWebApp-dcmuiWebAppListDescription:

    :ref:`Description <uiWebApp-dcmuiWebAppListDescription>`",string,"Web Application List description

    (dcmuiWebAppListDescription)"
    "
    .. _dcmuiMode:
    .. _uiWebApp-dcmuiMode:

    :ref:`List mode <uiWebApp-dcmuiMode>`",string,"You have two possibilities how to show the defined list: 1.) On top on the rest of list 'separated' with a line, 2.) Show only those hir defined ( 'exclusive' ).

    Enumerated values:

    separated

    exclusive

    (dcmuiMode)"
    "
    .. _dcmuiWebApps:
    .. _uiWebApp-dcmuiWebApps:

    :ref:`WebApps(s) <uiWebApp-dcmuiWebApps>`",string,"Web Application

    (dcmuiWebApps)"
    "
    .. _dcmAcceptedUserRole:
    .. _uiWebApp-dcmAcceptedUserRole:

    :ref:`Accepted User Role(s) <uiWebApp-dcmAcceptedUserRole>`",string,"Define the roles for which this config should be available, use 'user' to be available for all roles ( You should either define a username ( following attribute ) or user role ( this attribute ))

    (dcmAcceptedUserRole)"
    "
    .. _dcmAcceptedUserName:
    .. _uiWebApp-dcmAcceptedUserName:

    :ref:`Accepted User Name(s) <uiWebApp-dcmAcceptedUserName>`",string,"Define the Username for which this config should be available ( You should either define a username ( this attribute ) or user role ( previous attribute ))

    (dcmAcceptedUserName)"
