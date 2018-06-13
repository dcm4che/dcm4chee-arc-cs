Archive Compression rule
========================
Archive Compression rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Compression rule Attributes (LDAP Object: dcmArchiveCompressionRule)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name of the Archive Compression Rule"
    "
    .. _dicomTransferSyntax:

    :ref:`DICOM Transfer Syntax UID (dicomTransferSyntax) <dicomTransferSyntax>`",string,"A Transfer Syntax UID"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority (dcmRulePriority) <dcmRulePriority>`",integer,"Rule Priority"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) (dcmProperty) <dcmProperty>`",string,"Conditions in format {attributeID}[!]={regEx}"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) (dcmImageWriteParam) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression"
