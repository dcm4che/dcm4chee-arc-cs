Storage
=======
Storage Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Storage Attributes (LDAP Object: dcmStorage)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmStorageID:

    :ref:`Storage ID <dcmStorageID>`",string,"Storage ID

    (dcmStorageID)"
    "
    .. _dcmURI:

    :ref:`Storage URI <dcmURI>`",string,"RFC2079: Uniform Resource Identifier

    (dcmURI)"
    "
    .. _dcmDigestAlgorithm:

    :ref:`Digest Algorithm <dcmDigestAlgorithm>`",string,"Algorithm for generation of check sums. Enumerated values: MD5 or SHA-1.

    (dcmDigestAlgorithm)"
    "
    .. _dcmInstanceAvailability:

    :ref:`Instance Availability <dcmInstanceAvailability>`",string,"Instance Availability. Enumerated values: ONLINE, NEARLINE or OFFLINE.

    (dcmInstanceAvailability)"
    "
    .. _dcmReadOnly:

    :ref:`Read Only <dcmReadOnly>`",boolean,"Indicates if a Storage System is read only.

    (dcmReadOnly)"
    "
    .. _dcmStorageClusterID:

    :ref:`Storage Cluster ID <dcmStorageClusterID>`",string,"Identifies a Storage to belong to a Storage Cluster. Objects of one Study may be distributed over Storage Systems of one Storage Cluster. Used by threshold triggered deletion.

    (dcmStorageClusterID)"
    "
    .. _dcmStorageThreshold:

    :ref:`Storage Threshold <dcmStorageThreshold>`",string,"Minimal Usable Space on Storage System. If the usable space fall below that value the Storage System will be removed from the list of configured Storage Systems of the Network AE requesting that Storage System. Format nnn(MB|GB|MiB|GiB)

    (dcmStorageThreshold)"
    "
    .. _dcmDeleterThreshold:

    :ref:`Deleter Threshold(s) <dcmDeleterThreshold>`",string,"Minimal Usable Space on Storage System to trigger deletion. If present, studies are deleted from the Storage System, if the usable space fall below that value. Format [nn'['<schedule>']']nnn(MB|GB|MiB|GiB)

    (dcmDeleterThreshold)"
    "
    .. _dcmDeleterThreads:

    :ref:`Deleter Threads <dcmDeleterThreads>`",integer,"Number of Threads used for deletion of objects from the Storage System.

    (dcmDeleterThreads)"
    "
    .. _dcmExternalRetrieveAET:

    :ref:`External Retrieve AET <dcmExternalRetrieveAET>`",string,"Constrain deletion of Studies, if usable space falls below the configured threshold, to Studies which objects are retrievable using this AE from an external C-MOVE SCP.

    (dcmExternalRetrieveAET)"
    "
    .. _dcmExportStorageID:

    :ref:`Export Storage ID <dcmExportStorageID>`",string,"Constrain deletion of Studies, if usable space falls below the configured threshold, to Studies which objects are also accessible from the specified other storage.

    (dcmExportStorageID)"
    "
    .. _dcmRetrieveCacheStorageID:

    :ref:`Retrieve Cache Storage ID <dcmRetrieveCacheStorageID>`",string,"Specifies another Storage to which objects are copied in parallel on retrieve to increase the performance on accessing storage systems which provides more bandwidth using multiple connections in parallel.

    (dcmRetrieveCacheStorageID)"
    "
    .. _dcmRetrieveCacheMaxParallel:

    :ref:`Retrieve Cache Max Parallel <dcmRetrieveCacheMaxParallel>`",integer,"Maximal number of parallel copies to cache storage on retrieve. Only effective if a Retrieve Cache Storage ID is configured.

    (dcmRetrieveCacheMaxParallel)"
    "
    .. _dcmNoDeletionConstraint:

    :ref:`No Deletion Constraint <dcmNoDeletionConstraint>`",boolean,"If no External Retrieve AET or Export Storage ID is configured on Storage Descriptor and deleter threshold is reached, by default studies will not be deleted.

    (dcmNoDeletionConstraint)"
    "
    .. _dcmProperty:

    :ref:`Storage Property(s) <dcmProperty>`",string,"Property in format <name>=<value>

    (dcmProperty)"
