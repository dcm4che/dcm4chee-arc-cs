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
    .. _dcmArchiveSeriesAsTAR:

    :ref:`Archive Series as TAR <dcmArchiveSeriesAsTAR>`",boolean,"Indicates that binary DICOM objects of one Series are packed in one TAR archive on this Storage System; false if absent.

    (dcmArchiveSeriesAsTAR)"
    "
    .. _dcmStoragePathFormat:

    :ref:`Storage Path Format <dcmStoragePathFormat>`",string,"Format of file path of DICOM binary objects or metadata in JSON format or of ZIP archives containing metadata in JSON format for each DICOM object of one Series, written to this Storage System. '{now,date,yyyy/MM/dd}/{0020000D,hash}/{0020000E,hash}/{00080018,hash}', if absent.

    (dcmStoragePathFormat)"
    "
    .. _dcmOnStoragePathAlreadyExists:

    :ref:`Already Exists on Storage Path <dcmOnStoragePathAlreadyExists>`",string,"Specifies behavior if an object already exists on the storage path on the storage system, assembled according to the configured 'Storage Path Format'. Default behaviour 'RANDOM_PATH'. (hover on options to see their descriptions) Enumerated values: FAILURE|Signals failure writing the new object, NOOP|Proceed without writing the new object or RANDOM_PATH|Replace last path element be random 8 hex digit number and try again.

    (dcmOnStoragePathAlreadyExists)"
    "
    .. _dcmRetryCreateDirectories:

    :ref:`Retry Create Directories <dcmRetryCreateDirectories>`",integer,"Specifies number of retries to create parent directories of the storage file path - may workaround issues concerning NFS; 0 if absent.

    (dcmRetryCreateDirectories)"
    "
    .. _dcmAltCreateDirectories:

    :ref:`Alt Create Directories <dcmAltCreateDirectories>`",boolean,"Indicate to not rely on 'createDirectories' function in 'java.nio.file.Files' Java class, to create all nonexistent parent directories first, but instead explicitly create parent directories if NoSuchFileException is thrown. May workaround issues concerning NFS.

    (dcmAltCreateDirectories)"
    "
    .. _dcmCheckMountFilePath:

    :ref:`Check Mount File Path <dcmCheckMountFilePath>`",string,"Indicates to check if a mounted file system did not get detached from its mount point, by specifying the path of a shadow file in the directory used as mount point. If the shadow file becomes inaccessible, write to storage operation fails. Checked for each DICOM object storage (write operation). Typically applicable to NFS / external file systems.

    (dcmCheckMountFilePath)"
    "
    .. _dcmFileOpenOption:

    :ref:`File Open Option(s)(s) <dcmFileOpenOption>`",string,"Options specifying how the file is opened for writing. Default behaviour 'CREATE_NEW'. (hover on options to see their descriptions) Enumerated values: CREATE_NEW|Create a new file, failing if the file already exists, DSYNC|Requires that every update to the file's content be written synchronously to the underlying storage device or SYNC|Requires that every update to the file's content or metadata be written synchronously to the underlying storage device.

    (dcmFileOpenOption)"
    "
    .. _dcmLocationStatus:

    :ref:`Location Status <dcmLocationStatus>`",string,"Initial Location Status of DICOM files written to this Storage System. Default behaviour 'OK'. (hover on options to see their descriptions) Enumerated values: OK|Indicates access state of stored objects is stable or VERIFY_QSTAR_ACCESS_STATE|Indicates to verify access state of stored objects from QStar Tape File System.

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
