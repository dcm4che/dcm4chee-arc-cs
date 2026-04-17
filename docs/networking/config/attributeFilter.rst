Attribute Filter
================
Attributes stored in the database

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Attribute Filter Attributes (LDAP Object: dcmAttributeFilter)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmEntity:

    :ref:`Attribute Entity <dcmEntity>`",string,"Entity of the Attribute Filter or Export Rule ('Patient', 'Study', 'Series', 'Instance', 'MPPS', 'MWL', 'UPS').

    Enumerated values:

    Patient

    Study

    Series

    Instance

    MPPS

    MWL

    UPS

    (dcmEntity)"
    "
    .. _dcmTag:

    :ref:`Attribute Tag(s) <dcmTag>`",string,"DICOM Tag as hex string

    (dcmTag)"
    "
    .. _dcmCustomAttribute1:

    :ref:`Custom Attribute 1 <dcmCustomAttribute1>`",string,"Configure any attribute from the DICOM object which shall be inserted in database as Custom Attribute 1. Only applicable for Patient / Study / Series / Instance entities. Eg. DicomAttribute[@tag=""00200070""]/Value[@number=""1""] or for a Private attribute DicomAttribute[@tag=""00E10024"" and @privateCreator=""ELSCINT1""]/Value[@number=""1""]

    (dcmCustomAttribute1)"
    "
    .. _dcmCustomAttribute2:

    :ref:`Custom Attribute 2 <dcmCustomAttribute2>`",string,"Configure any attribute from the DICOM object which shall be inserted in database as Custom Attribute 2. Only applicable for Patient / Study / Series / Instance entities. Eg. DicomAttribute[@tag=""00200070""]/Value[@number=""1""] or for a Private attribute DicomAttribute[@tag=""00E10024"" and @privateCreator=""ELSCINT1""]/Value[@number=""1""]

    (dcmCustomAttribute2)"
    "
    .. _dcmCustomAttribute3:

    :ref:`Custom Attribute 3 <dcmCustomAttribute3>`",string,"Configure any attribute from the DICOM object which shall be inserted in database as Custom Attribute 3. Only applicable for Patient / Study / Series / Instance entities. Eg. DicomAttribute[@tag=""00200070""]/Value[@number=""1""] or for a Private attribute DicomAttribute[@tag=""00E10024"" and @privateCreator=""ELSCINT1""]/Value[@number=""1""]

    (dcmCustomAttribute3)"
    "
    .. _dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy <dcmAttributeUpdatePolicy>`",string,"Specifies update policy for extracted attributes into the DB on Series, Study & Patient level on receive of further instance of the entity.

    Enumerated values:

    PRESERVE (= The attributes will be preserved. Nullify attributes in the new dataset which are not present in the original dataset. Any extra attributes will be nullified)

    SUPPLEMENT (= The attributes will be overwritten. Attributes not present in original dataset will be supplemented. Any extra attributes with not null values will be added)

    MERGE (= The attributes will be overwritten. Attribute values will be written from new dataset. Any attributes with not null values, shall not be overwritten by attributes with null values)

    OVERWRITE (= The attributes will be overwritten. Attribute values if null in new dataset, will be nullified in original dataset. Any attributes with not null values, shall be overwritten by attributes with null values)

    REPLACE (= The attributes will be completely overwritten)

    (dcmAttributeUpdatePolicy)"
