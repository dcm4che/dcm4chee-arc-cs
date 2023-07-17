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
    .. _dcmLocationStatus:

    :ref:`Location Status <dcmLocationStatus>`",string,"Initial Location Status of DICOM files written to this Storage System: 'OK' or 'VERIFY_QSTAR_ACCESS_STATE'; 'OK' if absent. Enumerated values: OK or VERIFY_QSTAR_ACCESS_STATE.

    (dcmLocationStatus)"
    "
    .. _dcmDigestAlgorithm:

    :ref:`Digest Algorithm <dcmDigestAlgorithm>`",string,"Algorithm for generation of check sums. Enumerated values: MD5 or SHA-1.

    (dcmDigestAlgorithm)"
    "
    .. _dcmMaxRetries:

    :ref:`Maximum Number of Retries <dcmMaxRetries>`",integer,"Maximum number of retries to store an object on the storage system.

    (dcmMaxRetries)"
    "
    .. _dcmRetryDelay:

    :ref:`Retry Delay <dcmRetryDelay>`",string,"Delay to retry to store an object on the storage system in ISO-8601 duration format PnDTnHnMn.nS. Retry immediately if absent.

    (dcmRetryDelay)"
    "
    .. _dcmInstanceAvailability:

    :ref:`Instance Availability <dcmInstanceAvailability>`",string,"Instance Availability. Enumerated values: ONLINE, NEARLINE or OFFLINE.

    (dcmInstanceAvailability)"
    "
    .. _dcmStorageDuration:

    :ref:`Storage Duration <dcmStorageDuration>`",string,"Indicates if the Storage is used as permanent (=PERMANENT), cache (=CACHE) or temporary (=TEMPORARY) storage. Objects get purged from cache and temporary storage according configured deleter thresholds or - if no deleter threshold is specified and no Retention Periods are configured - all objects on the Storage will get purged. In the case of temporary storage, the studies which objects were purged are also deleted from the database. Enumerated values: PERMANENT, CACHE or TEMPORARY.

    (dcmStorageDuration)"
    "
    .. _dcmReadOnly:

    :ref:`Read Only <dcmReadOnly>`",boolean,"Indicates if a Storage System is read only.

    (dcmReadOnly)"
    "
    .. _dcmStorageClusterID:

    :ref:`Storage Cluster ID <dcmStorageClusterID>`",string,"Identifies a CACHE Storage belonging to a Storage Cluster. Objects of one Study may be distributed over Storage Systems of one Storage Cluster. Used by threshold triggered deletion.

    (dcmStorageClusterID)"
    "
    .. _dcmStorageThreshold:

    :ref:`Storage Threshold <dcmStorageThreshold>`",string,"Minimal Usable Space on Storage System. If the usable space falls below that value the Storage System will be marked as full by setting Storage Threshold Exceeds to the current time and - if Storage Threshold Exceeds Permanently is true - the Storage System will be removed from the list of configured Storage Systems of the Network AE requesting that Storage System. Format nnn(MB|GB|MiB|GiB)

    (dcmStorageThreshold)"
    "
    .. _dcmStorageThresholdExceeded:

    :ref:`Storage Threshold Exceeded <dcmStorageThresholdExceeded>`",string,"Date and time in format YYYYMMDDHHMMSS.FFFFFF when the Storage Threshold exceeded.

    (dcmStorageThresholdExceeded)"
    "
    .. _dcmStorageThresholdExceedsPermanently:

    :ref:`Storage Threshold Exceeds Permanently <dcmStorageThresholdExceedsPermanently>`",boolean,"Indicates to removed the Storage System from the list of configured Storage Systems of the Network AE requesting that Storage System when the Storage Threshold exceeds.

    (dcmStorageThresholdExceedsPermanently)"
    "
    .. _dcmNoDeletionConstraint:

    :ref:`No Deletion Constraint <dcmNoDeletionConstraint>`",boolean,"Delete Studies from cache/temporary Storage System, if no Deleter Threshold and no other deletion constraint is configured.

    (dcmNoDeletionConstraint)"
    "
    .. _dcmDeleterThreshold:

    :ref:`Deleter Threshold(s) <dcmDeleterThreshold>`",string,"Minimal Usable Space on Storage System to trigger deletion. If present, studies are deleted from the Storage System configured for cache (Storage Duration = CACHE) or temporary (Storage Duration = TEMPORARY) storage, if the usable space fall below that value. Format [nn'['<schedule>']']nnn(MB|GB|MiB|GiB).

    (dcmDeleterThreshold)"
    "
    .. _dcmDeleteStudiesOlderThan:

    :ref:`Delete Studies Older Than(s) <dcmDeleteStudiesOlderThan>`",string,"Delete Studies from the Storage System configured for cache (dcmStorageDuration=CACHE) or temporary (dcmStorageDuration=TEMPORARY) storage, if their Study Date is longer ago than the specified value in ISO-8601 period format. Format [nn""[""<schedule>""]""](PnYnMnD|PnW).

    (dcmDeleteStudiesOlderThan)"
    "
    .. _dcmDeleteStudiesReceivedBefore:

    :ref:`Delete Studies Received Before(s) <dcmDeleteStudiesReceivedBefore>`",string,"Delete Studies from the Storage System configured for cache (dcmStorageDuration=CACHE) or temporary (dcmStorageDuration=TEMPORARY) storage, if they were received longer ago than the specified value in ISO-8601 period format. Format [nn""[""<schedule>""]""](PnYnMnD|PnW).

    (dcmDeleteStudiesReceivedBefore)"
    "
    .. _dcmDeleteStudiesNotUsedSince:

    :ref:`Delete Studies Not Used Since(s) <dcmDeleteStudiesNotUsedSince>`",string,"Delete Studies from the Storage System configured for cache (dcmStorageDuration=CACHE) or temporary (dcmStorageDuration=TEMPORARY) storage, if they were last accessed longer ago than the specified value in ISO-8601 period format. Format [nn""[""<schedule>""]""](PnYnMnD|PnW).

    (dcmDeleteStudiesNotUsedSince)"
    "
    .. _dcmDeleterThreads:

    :ref:`Deleter Threads <dcmDeleterThreads>`",integer,"Number of Threads used for deletion of objects from the Storage System.

    (dcmDeleterThreads)"
    "
    .. _dcmExternalRetrieveAET:

    :ref:`External Retrieve AETs(s) <dcmExternalRetrieveAET>`",string,"Constrains deletion of Studies, additionally to configured deleter thresholds and/or deletion retention period constraints, from the Storage System to Studies which objects are retrievable using one of the AEs from an external C-MOVE SCP.

    (dcmExternalRetrieveAET)"
    "
    .. _dcmExternalRetrieveInstanceAvailability:

    :ref:`External Retrieve Instance Availability <dcmExternalRetrieveInstanceAvailability>`",string,"Updates instance availability on deletion of studies for instances available on external retrieve archive. Enumerated values: ONLINE, NEARLINE or OFFLINE.

    (dcmExternalRetrieveInstanceAvailability)"
    "
    .. _dcmExportStorageID:

    :ref:`Export Storage ID(s) <dcmExportStorageID>`",string,"Constrains deletion of Studies, additionally to configured deleter thresholds and/or deletion retention period constraints, from the Storage System to Studies whose objects are also accessible from the specified other storages.

    (dcmExportStorageID)"
    "
    .. _dcmRetrieveCacheStorageID:

    :ref:`Retrieve Cache Storage ID <dcmRetrieveCacheStorageID>`",string,"Specifies another Storage to which objects are copied in parallel on retrieve to increase the performance on accessing storage systems which provides more bandwidth using multiple connections in parallel.

    (dcmRetrieveCacheStorageID)"
    "
    .. _dcmNoRetrieveCacheOnDestinationAETitle:

    :ref:`No Retrieve Cache on Destination AE Title(s) <dcmNoRetrieveCacheOnDestinationAETitle>`",string,"Specifies AE Titles of C-STORE SCPs to which objects are retrieved without copying them to a configured Retrieve Cache Storage.

    (dcmNoRetrieveCacheOnDestinationAETitle)"
    "
    .. _dcmNoRetrieveCacheOnPurgedInstanceRecords:

    :ref:`No Retrieve Cache on Purged Instance Records <dcmNoRetrieveCacheOnPurgedInstanceRecords>`",boolean,"Indicates to NOT copy retrieved objects to a configured Retrieve Cache Storage, wherein corresponding Instance Records were already purged from the DB.

    (dcmNoRetrieveCacheOnPurgedInstanceRecords)"
    "
    .. _dcmRetrieveCacheMaxParallel:

    :ref:`Retrieve Cache Max Parallel <dcmRetrieveCacheMaxParallel>`",integer,"Maximal number of parallel copies to cache storage on retrieve. Only effective if a Retrieve Cache Storage ID is configured.

    (dcmRetrieveCacheMaxParallel)"
    "
    .. _dcmProperty:

    :ref:`Storage Property(s) <dcmProperty>`",string,"Specify storage properties in format {name}={value}. Refer various `Storage Properties <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Storage-Properties>`_ that can be configured based on the storage type.

    (dcmProperty)"
