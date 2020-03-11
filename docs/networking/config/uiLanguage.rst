UI Language Config
==================
UI Language Config

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Language Config Attributes (LDAP Object: dcmUiLanguage)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiLanguageConfigName:

    :ref:`Language Config Name <dcmuiLanguageConfigName>`",string,"Name of the Language Config

    (dcmuiLanguageConfigName)"
    "
    .. _dcmLanguages:

    :ref:`Available languages(s) <dcmLanguages>`",string,"Set languages that should be available in the UI (The JSON-files to those language must exist in the code, if they don't exist open an Issue in github

    (dcmLanguages)"
    ":doc:`uiLanguageProfile` (s)",object,"Language profile for username, role or everyone"

.. toctree::

    uiLanguageProfile
