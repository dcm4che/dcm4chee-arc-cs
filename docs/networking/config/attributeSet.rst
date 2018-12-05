Attribute Set
=============
Named Attribute Set for Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata or by Query Parameter 'comparefield' of DIFF-RS requests.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Attribute Set Attributes (LDAP Object: dcmAttributeSet)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomDescription:

    :ref:`Attribute Set Description <dicomDescription>`",string,"Unconstrained text description of this Attribute Set

    (dicomDescription)"
    "
    .. _dcmAttributeSetType:

    :ref:`Attribute Set Type <dcmAttributeSetType>`",string,"Specifies if this Attribute Set is used by Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata or by Query Parameter 'comparefield' of DIFF-RS requests. Enumerated values: QIDO_RS, WADO_RS, DIFF_RS or LEADING_CFIND_SCP.

    (dcmAttributeSetType)"
    "
    .. _dcmAttributeSetID:

    :ref:`Attribute Set ID <dcmAttributeSetID>`",string,"ID used by Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata requests and by Query Parameter 'comparefield' of DIFF-RS requests to refer this Attribute Set.

    (dcmAttributeSetID)"
    "
    .. _dcmAttributeSetTitle:

    :ref:`Attribute Set Title <dcmAttributeSetTitle>`",string,"Title of this Attribute Set.

    (dcmAttributeSetTitle)"
    "
    .. _dcmAttributeSetNumber:

    :ref:`Attribute Set Number <dcmAttributeSetNumber>`",integer,"Number used to order Attribute Sets.

    (dcmAttributeSetNumber)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"Boolean to indicate whether this Attribute Set is presently installed on the archive device

    (dicomInstalled)"
    "
    .. _dcmTag:

    :ref:`Attribute Tag(s) <dcmTag>`",string,"DICOM Tag as hex string

    (dcmTag)"
    "
    .. _dcmProperty:

    :ref:`Property(s) <dcmProperty>`",string,"Property in format <name>=<value>

    (dcmProperty)"
