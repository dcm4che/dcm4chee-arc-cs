Transfer Capability
===================
Each transfer capability specifies the SOP class that the Network AE can support, the mode that it can utilize (SCP or SCU), and the Transfer Syntax(es) that it can utilize

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Transfer Capability Attributes (LDAP Object: dcmTransferCapability)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name for the Transfer Capability object","
    .. _cn:

    cn_"
    "SOP Class",string,"SOP Class UID","
    .. _dicomSOPClass:

    dicomSOPClass_"
    "DICOM Transfer Role",string,"DICOM Transfer Role. Enumerated values: SCP or SCU","
    .. _dicomTransferRole:

    dicomTransferRole_"
    "Transfer Syntax(s)",string,"Transfer syntax(es) that may be requested as an SCU or that are offered as an SCP.","
    .. _dicomTransferSyntax:

    dicomTransferSyntax_"
    ":doc:`dcmTransferCapability` ",object,"dcm4che proprietary Transfer Capability Attributes","
    .. _dcmTransferCapability:

    dcmTransferCapability_"

.. toctree::

    dcmTransferCapability
