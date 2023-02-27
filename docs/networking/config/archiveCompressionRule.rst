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
    .. _dicomTransferSyntax:

    :ref:`DICOM Transfer Syntax UID <dicomTransferSyntax>`",string,"Transfer Syntax to which received images shall be compressed

    (dicomTransferSyntax)"
    "
    .. _dcmRulePriority:

    :ref:`Rule Priority <dcmRulePriority>`",integer,"If the condition of several Compression rules matches for a received image, the rule with the highest priority will get applied. If there are several matching rules with equal priority it is undefined which rule get applied.

    (dcmRulePriority)"
    "
    .. _dcmProperty:

    :ref:`Conditions(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression

    (dcmImageWriteParam)"
    "
    .. _dcmCompressionDelay:

    :ref:`Compression Delay <dcmCompressionDelay>`",string,"Compression delay in ISO-8601 duration format PnDTnHnMn.nS. Compress on receive if absent.

    (dcmCompressionDelay)"
