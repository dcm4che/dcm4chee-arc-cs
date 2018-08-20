Archive Compression rule
========================
Archive Compression rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Compression rule Attributes (LDAP Object: dcmArchiveCompressionRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Archive Compression Rule

    (cn)"
    "
    .. _dcmCompressionDelay:

    :ref:`Compression Delay <dcmCompressionDelay>`",string,"Compression delay in ISO-8601 period format PnYnMnD or PnW.

    (dcmCompressionDelay)"
    "
    .. _dicomTransferSyntax:

    :ref:`DICOM Transfer Syntax UID <dicomTransferSyntax>`",string,"A Transfer Syntax UID

    (dicomTransferSyntax)"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority <dcmRulePriority>`",integer,"Rule Priority

    (dcmRulePriority)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx}

    (dcmProperty)"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression

    (dcmImageWriteParam)"
