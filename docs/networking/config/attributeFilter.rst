Attribute Filter
================
Attributes stored in the database

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Attribute Filter Attributes (LDAP Object: dcmAttributeFilter)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Attribute Entity**",string,"Entity of the Attribute Filter or Export Rule ('Patient', 'Study', 'Series', 'Instance', 'MPPS', 'MWL').","
    .. _dcmEntity:

    dcmEntity_"
    "**Attribute Tag(s)**",string,"DICOM Tag as hex string","
    .. _dcmTag:

    dcmTag_"
    "Custom Attribute 1",string,"Custom Attribute 1","
    .. _dcmCustomAttribute1:

    dcmCustomAttribute1_"
    "Custom Attribute 2",string,"Custom Attribute 2","
    .. _dcmCustomAttribute2:

    dcmCustomAttribute2_"
    "Custom Attribute 3",string,"Custom Attribute 3","
    .. _dcmCustomAttribute3:

    dcmCustomAttribute3_"
    "Attribute Update Policy",string,"Specifies update policy for extracted attributes into the DB on Series, Study & Patient level on receive of further instance of the entity. Enumerated values: SUPPLEMENT, MERGE, OVERWRITE. If absent, the attributes will not be updated","
    .. _dcmAttributeUpdatePolicy:

    dcmAttributeUpdatePolicy_"
