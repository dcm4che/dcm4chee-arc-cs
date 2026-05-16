Transfer Capability
===================
Each transfer capability specifies the SOP class that the Network AE can support, the mode that it can utilize (SCP or SCU), and the Transfer Syntax(es) that it can utilize

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Transfer Capability Attributes (LDAP Object: dicomTransferCapability)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _transferCapability-cn:

    :ref:`Name <transferCapability-cn>`",string,"Arbitrary/Meaningful name for the Transfer Capability object

    (cn)"
    "
    .. _dicomSOPClass:
    .. _transferCapability-dicomSOPClass:

    :ref:`SOP Class <transferCapability-dicomSOPClass>`",string,"SOP Class UID

    (dicomSOPClass)"
    "
    .. _dicomTransferRole:
    .. _transferCapability-dicomTransferRole:

    :ref:`DICOM Transfer Role <transferCapability-dicomTransferRole>`",string,"DICOM Transfer Role.

    Enumerated values:

    SCP

    SCU

    (dicomTransferRole)"
    "
    .. _dicomTransferSyntax:
    .. _transferCapability-dicomTransferSyntax:

    :ref:`Transfer Syntax(s) <transferCapability-dicomTransferSyntax>`",string,"Transfer syntax(es) that may be requested as an SCU or that are offered as an SCP.

    (dicomTransferSyntax)"
    ":doc:`dcmTransferCapability` ",object,"dcm4che proprietary Transfer Capability Attributes"

.. toctree::

    dcmTransferCapability
