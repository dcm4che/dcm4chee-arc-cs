Attribute Set
=============
Named Attribute Set for Query Parameter 'comparefield' of DIFF-RS and Query Parameter 'includefields' of WADO-RS Metadata requests.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Attribute Set Attributes (LDAP Object: dcmAttributeSet)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Attribute Set Description",string,"Unconstrained text description of this Attribute Set","
    .. _dicomDescription:

    dicomDescription_"
    "Attribute Set Type",string,"Specifies if this Attribute Set is used by Query Parameter 'comparefield' of DIFF-RS or by Query Parameter 'includefields' of WADO-RS requests. Enumerated values: DIFF_RS or WADO_RS","
    .. _dcmAttributeSetType:

    dcmAttributeSetType_"
    "Attribute Set Number",integer,"Number used to order Attribute Sets.","
    .. _dcmAttributeSetID:

    dcmAttributeSetID_"
    "Attribute Set Title",string,"Title of this Attribute Set.","
    .. _dcmAttributeSetTitle:

    dcmAttributeSetTitle_"
    "installed",boolean,"Boolean to indicate whether this Attribute Set is presently installed on the archive device","
    .. _dicomInstalled:

    dicomInstalled_"
    "Attribute Tag(s)",string,"DICOM Tag as hex string","
    .. _dcmTag:

    dcmTag_"
