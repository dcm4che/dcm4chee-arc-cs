Archive Compression rule
========================
Archive Compression rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Compression rule Attributes (LDAP Object: dcmArchiveCompressionRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _archiveCompressionRule-cn:

    :ref:`Name <archiveCompressionRule-cn>`",string,"Arbitrary/Meaningful name of the Archive Compression Rule

    (cn)"
    "
    .. _dicomTransferSyntax:
    .. _archiveCompressionRule-dicomTransferSyntax:

    :ref:`DICOM Transfer Syntax UID <archiveCompressionRule-dicomTransferSyntax>`",string,"Transfer Syntax to which received images shall be compressed

    (dicomTransferSyntax)"
    "
    .. _dcmRulePriority:
    .. _archiveCompressionRule-dcmRulePriority:

    :ref:`Rule Priority <archiveCompressionRule-dcmRulePriority>`",integer,"If the condition of several Compression rules matches for a received image, the rule with the highest priority will get applied. If there are several matching rules with equal priority it is undefined which rule get applied.

    (dcmRulePriority)"
    "
    .. _dcmProperty:
    .. _archiveCompressionRule-dcmProperty:

    :ref:`Conditions(s) <archiveCompressionRule-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmImageWriteParam:
    .. _archiveCompressionRule-dcmImageWriteParam:

    :ref:`Image Write Param(s) <archiveCompressionRule-dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression

    (dcmImageWriteParam)"
    "
    .. _dcmCompressionDelay:
    .. _archiveCompressionRule-dcmCompressionDelay:

    :ref:`Compression Delay <archiveCompressionRule-dcmCompressionDelay>`",string,"Compression delay in ISO-8601 duration format PnDTnHnMn.nS. Compress on receive if absent.

    (dcmCompressionDelay)"
