Transfer Capability
===================
Each transfer capability specifies the SOP class that the Network AE can support, the mode that it can utilize (SCP or SCU), and the Transfer Syntax(es) that it can utilize

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Transfer Capability Attributes (LDAP Object: dcmTransferCapability)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name (cn) <cn>`",string,"Arbitrary/Meaningful name for the Transfer Capability object"
    "
    .. _dicomSOPClass:

    :ref:`SOP Class (dicomSOPClass) <dicomSOPClass>`",string,"SOP Class UID"
    "
    .. _dicomTransferRole:

    :ref:`DICOM Transfer Role (dicomTransferRole) <dicomTransferRole>`",string,"DICOM Transfer Role. Enumerated values: SCP or SCU"
    "
    .. _dicomTransferSyntax:

    :ref:`Transfer Syntax(s) (dicomTransferSyntax) <dicomTransferSyntax>`",string,"Transfer syntax(es) that may be requested as an SCU or that are offered as an SCP."
    ":doc:`dcmTransferCapability` ",object,"dcm4che proprietary Transfer Capability Attributes"

.. toctree::

    dcmTransferCapability
