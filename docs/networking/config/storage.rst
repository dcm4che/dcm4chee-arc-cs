Storage
=======
Storage Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Storage Attributes (LDAP Object: dcmStorage)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmStorageID:

    :ref:`Storage ID (dcmStorageID) <dcmStorageID>`",string,"Storage ID"
    "
    .. _dcmURI:

    :ref:`Storage URI (dcmURI) <dcmURI>`",string,"RFC2079: Uniform Resource Identifier"
    "
    .. _dcmDigestAlgorithm:

    :ref:`Digest Algorithm (dcmDigestAlgorithm) <dcmDigestAlgorithm>`",string,"Algorithm for generation of check sums. Enumerated values: MD5 or SHA-1"
    "
    .. _dcmInstanceAvailability:

    :ref:`Instance Availability (dcmInstanceAvailability) <dcmInstanceAvailability>`",string,"Instance Availability. Enumerated values: ONLINE, NEARLINE or OFFLINE"
    "
    .. _dcmReadOnly:

    :ref:`Read Only (dcmReadOnly) <dcmReadOnly>`",boolean,"Indicates if a Storage System is read only."
    "
    .. _dcmStorageThreshold:

    :ref:`Storage Threshold (dcmStorageThreshold) <dcmStorageThreshold>`",string,"Minimal Usable Space on Storage System. If the usable space fall below that value the Storage System will be removed from the list of configured Storage Systems of the Network AE requesting that Storage System. Format nnn(MB|GB|MiB|GiB)"
    "
    .. _dcmDeleterThreshold:

    :ref:`Deleter Threshold(s) (dcmDeleterThreshold) <dcmDeleterThreshold>`",string,"Minimal Usable Space on Storage System to trigger deletion. If present, studies are deleted from the Storage System, if the usable space fall below that value. Format [nn'['<schedule>']']nnn(MB|GB|MiB|GiB)"
    "
    .. _dcmExternalRetrieveAET:

    :ref:`External Retrieve AET (dcmExternalRetrieveAET) <dcmExternalRetrieveAET>`",string,"Constrain deletion of Studies, if usable space falls below the configured threshold, to Studies which objects are retrievable using this AE from an external C-MOVE SCP."
    "
    .. _dcmExportStorageID:

    :ref:`Export Storage ID (dcmExportStorageID) <dcmExportStorageID>`",string,"Constrain deletion of Studies, if usable space falls below the configured threshold, to Studies which objects are also accessible from the specified other storage."
    "
    .. _dcmRetrieveCacheStorageID:

    :ref:`Retrieve Cache Storage ID (dcmRetrieveCacheStorageID) <dcmRetrieveCacheStorageID>`",string,"Specifies another Storage to which objects are copied in parallel on retrieve to increase the performance on accessing storage systems which provides more bandwidth using multiple connections in parallel."
    "
    .. _dcmRetrieveCacheMaxParallel:

    :ref:`Retrieve Cache Max Parallel (dcmRetrieveCacheMaxParallel) <dcmRetrieveCacheMaxParallel>`",integer,"Maximal number of parallel copies to cache storage on retrieve. Only effective if a Retrieve Cache Storage ID is configured."
    "
    .. _dcmNoDeletionConstraint:

    :ref:`No Deletion Constraint (dcmNoDeletionConstraint) <dcmNoDeletionConstraint>`",boolean,"If no External Retrieve AET or Export Storage ID is configured on Storage Descriptor and deleter threshold is reached, by default studies will not be deleted."
    "
    .. _dcmProperty:

    :ref:`Storage Property(s) (dcmProperty) <dcmProperty>`",string,"Property in format <name>=<value>"
