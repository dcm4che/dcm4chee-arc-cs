Storage
=======
Storage Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Storage Attributes (LDAP Object: dcmStorage)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Storage ID",string,"Storage ID","
    .. _dcmStorageID:

    dcmStorageID_"
    "Storage URI",string,"RFC2079: Uniform Resource Identifier","
    .. _dcmURI:

    dcmURI_"
    "Digest Algorithm",string,"Algorithm for generation of check sums. Enumerated values: MD5 or SHA-1","
    .. _dcmDigestAlgorithm:

    dcmDigestAlgorithm_"
    "Instance Availability",string,"Instance Availability. Enumerated values: ONLINE, NEARLINE or OFFLINE","
    .. _dcmInstanceAvailability:

    dcmInstanceAvailability_"
    "Read Only",boolean,"Indicates if a Storage System is read only.","
    .. _dcmReadOnly:

    dcmReadOnly_"
    "Storage Threshold",string,"Minimal Usable Space on Storage System. If the usable space fall below that value the Storage System will be removed from the list of configured Storage Systems of the Network AE requesting that Storage System. Format nnn(MB|GB|MiB|GiB)","
    .. _dcmStorageThreshold:

    dcmStorageThreshold_"
    "Deleter Threshold(s)",string,"Minimal Usable Space on Storage System to trigger deletion. If present, studies are deleted from the Storage System, if the usable space fall below that value. Format [nn'['<schedule>']']nnn(MB|GB|MiB|GiB)","
    .. _dcmDeleterThreshold:

    dcmDeleterThreshold_"
    "External Retrieve AET",string,"Constrain deletion of Studies, if usable space falls below the configured threshold, to Studies which objects are retrievable using this AE from an external C-MOVE SCP.","
    .. _dcmExternalRetrieveAET:

    dcmExternalRetrieveAET_"
    "Export Storage ID",string,"Constrain deletion of Studies, if usable space falls below the configured threshold, to Studies which objects are also accessible from the specified other storage.","
    .. _dcmExportStorageID:

    dcmExportStorageID_"
    "No Deletion Constraint",boolean,"If no External Retrieve AET or Export Storage ID is configured on Storage Descriptor and deleter threshold is reached, by default studies will not be deleted.","
    .. _dcmNoDeletionConstraint:

    dcmNoDeletionConstraint_"
    "Storage Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
