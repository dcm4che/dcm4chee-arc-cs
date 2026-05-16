Bulk Data Descriptor
====================
Bulk Data Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Bulk Data Descriptor Attributes (LDAP Object: dcmBulkData)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmBulkDataDescriptorID:
    .. _bulkData-dcmBulkDataDescriptorID:

    :ref:`Bulk Data Descriptor ID <bulkData-dcmBulkDataDescriptorID>`",string,"Bulk Data Descriptor ID

    (dcmBulkDataDescriptorID)"
    "
    .. _dcmBulkDataExcludeDefaults:
    .. _bulkData-dcmBulkDataExcludeDefaults:

    :ref:`Exclude Defaults <bulkData-dcmBulkDataExcludeDefaults>`",boolean,"Indicates if Attributes specified by the 'Composite Instance Retrieve Without Bulk Data Service Class' shall be implicitly treated as Bulk Data (=false) or not (=true).

    (dcmBulkDataExcludeDefaults)"
    "
    .. _dcmAttributeSelector:
    .. _bulkData-dcmAttributeSelector:

    :ref:`Attribute Selector(s) <bulkData-dcmAttributeSelector>`",string,"Specifies individual Attributes treated as Bulk Data by XPath (e.g. 'DicomAttribute[@tag=""54000100""]/Item/DicomAttribute[@tag=""54001010""]' ).

    (dcmAttributeSelector)"
    "
    .. _dcmBulkDataVRLengthThreshold:
    .. _bulkData-dcmBulkDataVRLengthThreshold:

    :ref:`VR Length Threshold(s) <bulkData-dcmBulkDataVRLengthThreshold>`",string,"Specifies to treat all Attributes with a particular Value Representation (VR) which value length exceeds the specified threshold as Bulk Date. Format: <VR>=<length-threshold>.

    (dcmBulkDataVRLengthThreshold)"
