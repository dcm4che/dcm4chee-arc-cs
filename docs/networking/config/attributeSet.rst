Attribute Set
=============
Named Attribute Set for Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata or by Query Parameter 'comparefield' of DIFF-RS requests.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Attribute Set Attributes (LDAP Object: dcmAttributeSet)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomDescription:
    .. _attributeSet-dicomDescription:

    :ref:`Attribute Set Description <attributeSet-dicomDescription>`",string,"Unconstrained text description of this Attribute Set

    (dicomDescription)"
    "
    .. _dcmAttributeSetType:
    .. _attributeSet-dcmAttributeSetType:

    :ref:`Attribute Set Type <attributeSet-dcmAttributeSetType>`",string,"Specifies usage of this Attribute Set Type.

    Enumerated values:

    QIDO_RS (= Attribute Set is used by Query Parameter 'includefields' of QIDO-RS requests)

    WADO_RS (= Attribute Set is used by Query Parameter 'includefields' of WADO-RS requests)

    DIFF_RS (= Attribute Set is used by Query Parameter 'comparefields' of DIFF-RS requests)

    LEADING_CFIND_SCP (= Attribute Set is used by Leading C-FIND SCP coercion)

    (dcmAttributeSetType)"
    "
    .. _dcmAttributeSetID:
    .. _attributeSet-dcmAttributeSetID:

    :ref:`Attribute Set ID <attributeSet-dcmAttributeSetID>`",string,"ID used by Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata requests and by Query Parameter 'comparefield' of DIFF-RS requests to refer this Attribute Set.

    (dcmAttributeSetID)"
    "
    .. _dcmAttributeSetTitle:
    .. _attributeSet-dcmAttributeSetTitle:

    :ref:`Attribute Set Title <attributeSet-dcmAttributeSetTitle>`",string,"Title of this Attribute Set.

    (dcmAttributeSetTitle)"
    "
    .. _dcmAttributeSetNumber:
    .. _attributeSet-dcmAttributeSetNumber:

    :ref:`Attribute Set Number <attributeSet-dcmAttributeSetNumber>`",integer,"Number used to order Attribute Sets.

    (dcmAttributeSetNumber)"
    "
    .. _dicomInstalled:
    .. _attributeSet-dicomInstalled:

    :ref:`installed <attributeSet-dicomInstalled>`",boolean,"Boolean to indicate whether this Attribute Set is presently installed on the archive device

    (dicomInstalled)"
    "
    .. _dcmTag:
    .. _attributeSet-dcmTag:

    :ref:`Attribute Tag(s) <attributeSet-dcmTag>`",string,"DICOM Tag as hex string

    (dcmTag)"
    "
    .. _dcmProperty:
    .. _attributeSet-dcmProperty:

    :ref:`Property(s) <attributeSet-dcmProperty>`",string,"Property in format <name>=<value>

    (dcmProperty)"
