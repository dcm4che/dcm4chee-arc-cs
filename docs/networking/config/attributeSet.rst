Attribute Set
=============
Named Attribute Set for Query Parameter 'comparefield' of DIFF-RS and Query Parameter 'includefields' of WADO-RS Metadata requests.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Attribute Set Attributes (LDAP Object: dcmAttributeSet)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dicomDescription:

    :ref:`Attribute Set Description (dicomDescription) <dicomDescription>`",string,"Unconstrained text description of this Attribute Set"
    "
    .. _dcmAttributeSetType:

    :ref:`Attribute Set Type (dcmAttributeSetType) <dcmAttributeSetType>`",string,"Specifies if this Attribute Set is used by Query Parameter 'comparefield' of DIFF-RS or by Query Parameter 'includefields' of WADO-RS requests. Enumerated values: DIFF_RS, WADO_RS or LEADING_CFIND_SCP"
    "
    .. _dcmAttributeSetID:

    :ref:`Attribute Set ID (dcmAttributeSetID) <dcmAttributeSetID>`",string,"ID used by Query Parameter 'comparefield' of DIFF-RS requests and by Query Parameter 'includefields' of WADO-RS Metadata requests to refer this Attribute Set."
    "
    .. _dcmAttributeSetTitle:

    :ref:`Attribute Set Title (dcmAttributeSetTitle) <dcmAttributeSetTitle>`",string,"Title of this Attribute Set."
    "
    .. _dcmAttributeSetNumber:

    :ref:`Attribute Set Number (dcmAttributeSetNumber) <dcmAttributeSetNumber>`",integer,"Number used to order Attribute Sets."
    "
    .. _dicomInstalled:

    :ref:`installed (dicomInstalled) <dicomInstalled>`",boolean,"Boolean to indicate whether this Attribute Set is presently installed on the archive device"
    "
    .. _dcmTag:

    :ref:`Attribute Tag(s) (dcmTag) <dcmTag>`",string,"DICOM Tag as hex string"
    "
    .. _dcmProperty:

    :ref:`Property(s) (dcmProperty) <dcmProperty>`",string,"Property in format <name>=<value>"
