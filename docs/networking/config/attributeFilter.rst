Attribute Filter
================
Attributes stored in the database

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Attribute Filter Attributes (LDAP Object: dcmAttributeFilter)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmEntity:

    :ref:`Attribute Entity (dcmEntity) <dcmEntity>`",string,"Entity of the Attribute Filter or Export Rule ('Patient', 'Study', 'Series', 'Instance', 'MPPS', 'MWL'). Enumerated values: Patient, Study, Series, Instance, MPPS or MWL"
    "
    .. _dcmTag:

    :ref:`Attribute Tag(s) (dcmTag) <dcmTag>`",string,"DICOM Tag as hex string"
    "
    .. _dcmCustomAttribute1:

    :ref:`Custom Attribute 1 (dcmCustomAttribute1) <dcmCustomAttribute1>`",string,"Custom Attribute 1"
    "
    .. _dcmCustomAttribute2:

    :ref:`Custom Attribute 2 (dcmCustomAttribute2) <dcmCustomAttribute2>`",string,"Custom Attribute 2"
    "
    .. _dcmCustomAttribute3:

    :ref:`Custom Attribute 3 (dcmCustomAttribute3) <dcmCustomAttribute3>`",string,"Custom Attribute 3"
    "
    .. _dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy (dcmAttributeUpdatePolicy) <dcmAttributeUpdatePolicy>`",string,"Specifies update policy for extracted attributes into the DB on Series, Study & Patient level on receive of further instance of the entity. If absent, the attributes will not be updated Enumerated values: SUPPLEMENT, MERGE or OVERWRITE"
