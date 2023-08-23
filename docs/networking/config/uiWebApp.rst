Web App drop-down list
======================
Web App drop-down list

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Web App drop-down list Attributes (LDAP Object: dcmUiWebApp)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiWebAppListName:

    :ref:`List Name <dcmuiWebAppListName>`",string,"Define a name for this config

    (dcmuiWebAppListName)"
    "
    .. _dcmuiWebAppListDescription:

    :ref:`Description <dcmuiWebAppListDescription>`",string,"Web Application List description

    (dcmuiWebAppListDescription)"
    "
    .. _dcmuiMode:

    :ref:`List mode <dcmuiMode>`",string,"You have two possibilities how to show the defined list: 1.) On top on the rest of list 'separated' with a line, 2.) Show only those hir defined ( 'exclusive' ). Enumerated values: separated or exclusive.

    (dcmuiMode)"
    "
    .. _dcmuiWebApps:

    :ref:`WebApps(s) <dcmuiWebApps>`",string,"Web Application

    (dcmuiWebApps)"
    "
    .. _dcmAcceptedUserRole:

    :ref:`Accepted User Role(s) <dcmAcceptedUserRole>`",string,"Define the roles for which this config should be available, use 'user' to be available for all roles ( You should either define a username ( following attribute ) or user role ( this attribute ))

    (dcmAcceptedUserRole)"
    "
    .. _dcmAcceptedUserName:

    :ref:`Accepted User Name(s) <dcmAcceptedUserName>`",string,"Define the Username for which this config should be available ( You should either define a username ( this attribute ) or user role ( previous attribute ))

    (dcmAcceptedUserName)"
