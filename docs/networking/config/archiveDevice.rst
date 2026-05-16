Archive Device
==============
DICOM Archive Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Device Attributes (LDAP Object: dcmArchiveDevice)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmFuzzyAlgorithmClass:
    .. _archiveDevice-dcmFuzzyAlgorithmClass:

    :ref:`Fuzzy Algorithm Class <archiveDevice-dcmFuzzyAlgorithmClass>`",string,"Specifies Fuzzy Algorithm Implementation Class.

    Enumerated values:

    org.dcm4che3.soundex.Soundex (= Classic Soundex phonetic algorithm that encodes names into a 4-character code based on English pronunciation so similarly sounding names match despite spelling differences)

    org.dcm4che3.soundex.ESoundex (= Extended Soundex variant that produces variable-length phonetic codes (instead of fixed 4 characters) to improve matching accuracy for longer words)

    org.dcm4che3.soundex.ESoundex9 (= Extended Soundex variant that generates phonetic codes up to 9 characters long for higher precision fuzzy matching than standard Soundex)

    org.dcm4che3.soundex.Metaphone (= Metaphone phonetic algorithm that encodes words based on English pronunciation rules and spelling patterns, providing more accurate phonetic matching than Soundex)

    org.dcm4che3.soundex.KPhonetik (= Cologne Phonetic (Kölner Phonetik) algorithm optimized for German phonetics to match words that sound similar in German pronunciation)

    org.dcm4che3.soundex.Phonem (= Phonem algorithm that normalizes words into a simplified phonetic representation to improve fuzzy matching across spelling variations (commonly used for Germanic names))

    (dcmFuzzyAlgorithmClass)"
    "
    .. _dcmStoreImplementationVersionName:
    .. _archiveDevice-dcmStoreImplementationVersionName:

    :ref:`Store Implementation Version Name <archiveDevice-dcmStoreImplementationVersionName>`",boolean,"Indicates to include Implementation Version Name (0002,0012) in the File Meta Information of stored DICOM objects.

    (dcmStoreImplementationVersionName)"
    "
    .. _dcmBulkDataDescriptorID:
    .. _archiveDevice-dcmBulkDataDescriptorID:

    :ref:`Bulk Data Descriptor ID <archiveDevice-dcmBulkDataDescriptorID>`",string,"ID of Bulk Data Descriptor applied by all services providing Metadata of archived instances. If absent, only Attributes specified by the Composite Instance Retrieve Without Bulk Data Service Class are treated as Bulk Data. May be overwritten by configured values for particular Archive Network AEs.

    (dcmBulkDataDescriptorID)"
    "
    .. _dcmCalculateStudySizeDelay:
    .. _archiveDevice-dcmCalculateStudySizeDelay:

    :ref:`Calculate Study Size Delay <archiveDevice-dcmCalculateStudySizeDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for eager calculation of Study Size and Query Attributes. If absent, no (minimal) delay for eager calculation of the Study Size and Query Attributes is applied.

    (dcmCalculateStudySizeDelay)"
    "
    .. _dcmCalculateStudySizePollingInterval:
    .. _archiveDevice-dcmCalculateStudySizePollingInterval:

    :ref:`Calculate Study Size Polling Interval <archiveDevice-dcmCalculateStudySizePollingInterval>`",string,"Polling Interval for Studies with unknown size in ISO-8601 duration format PnDTnHnMnS. If absent, there is no eager calculation of the Study Size and Query Attributes.

    (dcmCalculateStudySizePollingInterval)"
    "
    .. _dcmCalculateStudySizeFetchSize:
    .. _archiveDevice-dcmCalculateStudySizeFetchSize:

    :ref:`Calculate Study Size Fetch Size <archiveDevice-dcmCalculateStudySizeFetchSize>`",integer,"Limit result set of DB query for Studies with unknown size.

    (dcmCalculateStudySizeFetchSize)"
    "
    .. _dcmCalculateQueryAttributes:
    .. _archiveDevice-dcmCalculateQueryAttributes:

    :ref:`Calculate Query Attributes <archiveDevice-dcmCalculateQueryAttributes>`",boolean,"Indicates to eager calculate Query Attributes according configured Calculate Study Size Delay and Calculate Study Size Polling Interval.

    (dcmCalculateQueryAttributes)"
    "
    .. _dcmSeriesMetadataStorageID:
    .. _archiveDevice-dcmSeriesMetadataStorageID:

    :ref:`Series Metadata Storage ID(s) <archiveDevice-dcmSeriesMetadataStorageID>`",string,"ID of Storage on which ZIP archives with aggregated Metadata of all instances of a Series is stored. Multiple Storage Systems may be configured. If absent, no aggregated Series Metadata will be stored.

    (dcmSeriesMetadataStorageID)"
    "
    .. _dcmSeriesMetadataDelay:
    .. _archiveDevice-dcmSeriesMetadataDelay:

    :ref:`Aggregate Series Metadata Delay <archiveDevice-dcmSeriesMetadataDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for storing aggregated Series Metadata on storage. If absent, no aggregated Series Metadata will be stored. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSeriesMetadataDelay)"
    "
    .. _dcmUpdateSeriesMetadata:
    .. _archiveDevice-dcmUpdateSeriesMetadata:

    :ref:`Update Series Metadata <archiveDevice-dcmUpdateSeriesMetadata>`",boolean,"Indicates to update aggregated Series Metadata on attributes update.

    (dcmUpdateSeriesMetadata)"
    "
    .. _dcmSeriesMetadataPollingInterval:
    .. _archiveDevice-dcmSeriesMetadataPollingInterval:

    :ref:`Update Series Metadata Polling Interval <archiveDevice-dcmSeriesMetadataPollingInterval>`",string,"Polling Interval for Series scheduled for Metadata update in ISO-8601 duration format PnDTnHnMnS. If absent, no aggregated Series Metadata will be stored.

    (dcmSeriesMetadataPollingInterval)"
    "
    .. _dcmSeriesMetadataFetchSize:
    .. _archiveDevice-dcmSeriesMetadataFetchSize:

    :ref:`Update Series Metadata Fetch Size <archiveDevice-dcmSeriesMetadataFetchSize>`",integer,"Maximal number of Series scheduled for Metadata update fetched by one query.

    (dcmSeriesMetadataFetchSize)"
    "
    .. _dcmSeriesMetadataThreads:
    .. _archiveDevice-dcmSeriesMetadataThreads:

    :ref:`Update Series Metadata Threads <archiveDevice-dcmSeriesMetadataThreads>`",integer,"Number of Threads used for creation and update of Series Metadata.

    (dcmSeriesMetadataThreads)"
    "
    .. _dcmSeriesMetadataMaxRetries:
    .. _archiveDevice-dcmSeriesMetadataMaxRetries:

    :ref:`Update Series Metadata Maximum Number of Retries <archiveDevice-dcmSeriesMetadataMaxRetries>`",integer,"Maximum number of retries to create/update aggregated Series Metadata. Only effective if Update Series Metadata Retry Interval is specified. -1 = forever.

    (dcmSeriesMetadataMaxRetries)"
    "
    .. _dcmSeriesMetadataRetryInterval:
    .. _archiveDevice-dcmSeriesMetadataRetryInterval:

    :ref:`Update Series Metadata Retry Interval <archiveDevice-dcmSeriesMetadataRetryInterval>`",string,"Interval in ISO-8601 duration format PnDTnHnMnS in which failed attempts to create/update aggregated Series Metadata will be retried. Only effective if Update Series Metadata Maximum Number of Retries != 0. If absent, failed attempts will not be retried.

    (dcmSeriesMetadataRetryInterval)"
    "
    .. _dcmPurgeInstanceRecords:
    .. _archiveDevice-dcmPurgeInstanceRecords:

    :ref:`Purge(d) Instance Records <archiveDevice-dcmPurgeInstanceRecords>`",boolean,"Indicates to purge instance records from DB. Also indicates to explicitly query series metadata zip files to check for purged instances for subsequent processing of archive functions. Set to 'True' if 'Purge Instance Records Delay' is configured.

    (dcmPurgeInstanceRecords)"
    "
    .. _dcmPurgeInstanceRecordsDelay:
    .. _archiveDevice-dcmPurgeInstanceRecordsDelay:

    :ref:`Purge Instance Records Delay <archiveDevice-dcmPurgeInstanceRecordsDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for purging Instance Records from the DB. May be overwritten by configured values for particular Archive Network AEs. Only effective, if Purge Instance Records = true.

    (dcmPurgeInstanceRecordsDelay)"
    "
    .. _dcmPurgeInstanceRecordsPollingInterval:
    .. _archiveDevice-dcmPurgeInstanceRecordsPollingInterval:

    :ref:`Purge Instance Records Polling Interval <archiveDevice-dcmPurgeInstanceRecordsPollingInterval>`",string,"Polling Interval for Series scheduled for purging Instance Records from the DB in ISO-8601 duration format PnDTnHnMnS. Only effective, if Purge Instance Records = true.

    (dcmPurgeInstanceRecordsPollingInterval)"
    "
    .. _dcmPurgeInstanceRecordsFetchSize:
    .. _archiveDevice-dcmPurgeInstanceRecordsFetchSize:

    :ref:`Purge Instance Records Fetch Size <archiveDevice-dcmPurgeInstanceRecordsFetchSize>`",integer,"Maximal number of Series scheduled for purging Instance Records from the DB fetched by one query. Only effective, if Purge Instance Records = true.

    (dcmPurgeInstanceRecordsFetchSize)"
    "
    .. _dcmMWLPollingInterval:
    .. _archiveDevice-dcmMWLPollingInterval:

    :ref:`MWL Polling Interval <archiveDevice-dcmMWLPollingInterval>`",string,"Polling Interval for updating the status of idle MWL items and deleting MWL items in ISO-8601 duration format PnDTnHnMnS. If absent, MWL Items will not get update or deleted.

    (dcmMWLPollingInterval)"
    "
    .. _dcmMWLFetchSize:
    .. _archiveDevice-dcmMWLFetchSize:

    :ref:`MWL Fetch Size <archiveDevice-dcmMWLFetchSize>`",integer,"Maximal number of MWL items to update or delete in one transaction.

    (dcmMWLFetchSize)"
    "
    .. _dcmMWLImportInterval:
    .. _archiveDevice-dcmMWLImportInterval:

    :ref:`MWL Import Interval <archiveDevice-dcmMWLImportInterval>`",string,"Interval for import of Scheduled Procedure Steps from external MWL SCPs in ISO-8601 duration format PnDTnHnMn.nS; disabled if absent.

    (dcmMWLImportInterval)"
    "
    .. _dcmDeleteMWLDelay:
    .. _archiveDevice-dcmDeleteMWLDelay:

    :ref:`Delete MWL Delay(s) <archiveDevice-dcmDeleteMWLDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for deleting MWL items, whose updated_time is older than the specified delay. Status specific delays can be specified by prefix 'SCHEDULED:', 'ARRIVED:', 'READY:', 'STARTED:', 'DEPARTED:', 'CANCELED:', 'DISCONTINUED:', 'COMPLETED:'. Examples: PT5M or CANCELED:PT10M. If absent, MWL Items will not get deleted.

    (dcmDeleteMWLDelay)"
    "
    .. _dcmDeleteUPSPollingInterval:
    .. _archiveDevice-dcmDeleteUPSPollingInterval:

    :ref:`Delete UPS Polling Interval <archiveDevice-dcmDeleteUPSPollingInterval>`",string,"Polling Interval for deleting Unified Procedure Steps (UPS) in ISO-8601 duration format PnDTnHnMnS. If absent, Unified Procedure Steps will not get deleted.

    (dcmDeleteUPSPollingInterval)"
    "
    .. _dcmDeleteUPSFetchSize:
    .. _archiveDevice-dcmDeleteUPSFetchSize:

    :ref:`Delete UPS Fetch Size <archiveDevice-dcmDeleteUPSFetchSize>`",integer,"Maximal number of Unified Procedure Steps (UPS) to delete in one transaction.

    (dcmDeleteUPSFetchSize)"
    "
    .. _dcmDeleteUPSCompletedDelay:
    .. _archiveDevice-dcmDeleteUPSCompletedDelay:

    :ref:`Delete UPS Completed Delay <archiveDevice-dcmDeleteUPSCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for deleting completed Unified Procedure Steps without Deletion Lock. If absent, completed Unified Procedure Steps without Deletion Lock are deleted immediately.

    (dcmDeleteUPSCompletedDelay)"
    "
    .. _dcmDeleteUPSCanceledDelay:
    .. _archiveDevice-dcmDeleteUPSCanceledDelay:

    :ref:`Delete UPS Canceled Delay <archiveDevice-dcmDeleteUPSCanceledDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for deleting canceled Unified Procedure Steps without Deletion Lock. If absent, canceled Unified Procedure Steps without Deletion Lock are deleted immediately.

    (dcmDeleteUPSCanceledDelay)"
    "
    .. _dcmOverwritePolicy:
    .. _archiveDevice-dcmOverwritePolicy:

    :ref:`Overwrite Policy <archiveDevice-dcmOverwritePolicy>`",string,"Specifies behavior on receive of objects, which SOP Instance UID matches a previous received object. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NEVER (= Never overwrite previous received object on receive of object with matching SOP Instance UID)

    ALWAYS (= Always overwrite previous received object on receive of object with matching SOP Instance UID and if instance location digest is unequal)

    SAME_SOURCE (= Overwrite previous received object on receive of object with matching SOP Instance UID if it is from same source (Calling AET))

    EVEN_WITH_EQUAL_DIGEST (= Overwrite previous received object on receive of object with matching SOP Instance UID even if instance location digest is equal)

    (dcmOverwritePolicy)"
    "
    .. _dcmRelationalMismatchPolicy:
    .. _archiveDevice-dcmRelationalMismatchPolicy:

    :ref:`Relational Mismatch Policy <archiveDevice-dcmRelationalMismatchPolicy>`",string,"Specifies behavior on receive of objects, which SOP Instance UID matches a previous received object belonging to a different Series. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    IGNORE (= Silently ignores the received object)

    REJECT (= Reject the received object with error status A77BH)

    OVERWRITE (= Replace previous received object by new one belonging to other Series (\poor-man IOCM\))

    STORE_ADDITIONALLY (= Store received object, retaining the previous received object, replacing the value SAME_SOURCE of config field Overwrite Policy)

    (dcmRelationalMismatchPolicy)"
    "
    .. _dcmRecordAttributeModification:
    .. _archiveDevice-dcmRecordAttributeModification:

    :ref:`Record Attribute Modification <archiveDevice-dcmRecordAttributeModification>`",boolean,"Indicates if modifications of attributes of stored objects are recorded in Items of the Original Attributes Sequence. May be overwritten by configured values for particular Archive Network AE or Archive HL7 Application.

    (dcmRecordAttributeModification)"
    "
    .. _dcmAcceptMissingPatientID:
    .. _archiveDevice-dcmAcceptMissingPatientID:

    :ref:`Accept Missing Patient ID <archiveDevice-dcmAcceptMissingPatientID>`",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    YES (= Accept missing Patient ID (0010,0020) in DICOM dataset)

    NO (= Do not accept missing Patient ID (0010,0020) in DICOM dataset)

    CREATE (= Create patient identifier if missing Patient ID (0010,0020) in DICOM dataset)

    (dcmAcceptMissingPatientID)"
    "
    .. _dcmAcceptConflictingPatientID:
    .. _archiveDevice-dcmAcceptConflictingPatientID:

    :ref:`Accept Conflicting Patient ID <archiveDevice-dcmAcceptConflictingPatientID>`",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    YES (= Accept patient identifier in DICOM dataset differing from patient identifier in previous received objects of study)

    NO (= Do not accept patient identifier in DICOM dataset differing from patient identifier in previous received objects of study)

    MERGED (= Accept patient identifier in DICOM dataset if already merged with another patient identifier)

    (dcmAcceptConflictingPatientID)"
    "
    .. _dcmIdentifyPatientByIDAndName:
    .. _archiveDevice-dcmIdentifyPatientByIDAndName:

    :ref:`Identify Patient by ID and Name <archiveDevice-dcmIdentifyPatientByIDAndName>`",boolean,"Indicates to consider also the Patient Name on receive of DICOM objects to determine if they belongs to an already existing Patient in the archive.

    (dcmIdentifyPatientByIDAndName)"
    "
    .. _dcmIdentifyPatientByAllAttributes:
    .. _archiveDevice-dcmIdentifyPatientByAllAttributes:

    :ref:`Identify Patient by all Attributes <archiveDevice-dcmIdentifyPatientByAllAttributes>`",boolean,"Indicates if all Patient attributes in received objects shall be used for associating an already existing Patient in the archive, if the Assigning Authority of the Patient ID is not specified by an Issuer of Patient ID or Universal Entity ID. Attention: disables the coercion of stale Patient attributes in received objects and breaks Patient Management functions relying on the unambiguity of Patient IDs.

    (dcmIdentifyPatientByAllAttributes)"
    "
    .. _dcmBulkDataSpoolDirectory:
    .. _archiveDevice-dcmBulkDataSpoolDirectory:

    :ref:`Bulk Data Spool Directory <archiveDevice-dcmBulkDataSpoolDirectory>`",string,"Path to Bulk Data Spool Directory. May be overwritten by configured values for particular Archive Network AEs.

    (dcmBulkDataSpoolDirectory)"
    "
    .. _dcmHideSPSWithStatusFromMWL:
    .. _archiveDevice-dcmHideSPSWithStatusFromMWL:

    :ref:`Hide SPS with Status by MWL SCP(s) <archiveDevice-dcmHideSPSWithStatusFromMWL>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    SCHEDULED

    ARRIVED

    READY

    STARTED

    DEPARTED

    CANCELED

    DISCONTINUED

    COMPLETED

    (dcmHideSPSWithStatusFromMWL)"
    "
    .. _dcmHideSPSWithStatusFromMWLRS:
    .. _archiveDevice-dcmHideSPSWithStatusFromMWLRS:

    :ref:`Hide SPS with Status by MWL RS(s) <archiveDevice-dcmHideSPSWithStatusFromMWLRS>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL RS. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    SCHEDULED

    ARRIVED

    READY

    STARTED

    DEPARTED

    CANCELED

    DISCONTINUED

    COMPLETED

    (dcmHideSPSWithStatusFromMWLRS)"
    "
    .. _dcmEncodeAsJSONNumber:
    .. _archiveDevice-dcmEncodeAsJSONNumber:

    :ref:`Encode as JSON Number(s) <archiveDevice-dcmEncodeAsJSONNumber>`",string,"VR encoded as JSON Number. If not listed, IS, DS, SV and UV values are encoded as JSON Strings. May be supplemented by configured values for particular Archive Network AEs.

    Enumerated values:

    DS (= Decimal String)

    IS (= Integer String)

    SV (= Signed 64-bit Very Long)

    UV (= Unsigned 64-bit Very Long)

    (dcmEncodeAsJSONNumber)"
    "
    .. _dcmValidateCallingAEHostname:
    .. _archiveDevice-dcmValidateCallingAEHostname:

    :ref:`Validate Calling AE Hostname <archiveDevice-dcmValidateCallingAEHostname>`",boolean,"Validate Calling AE Hostname or IP Address of Association requestors. May be overwritten by configured values for particular Archive Network AEs.

    (dcmValidateCallingAEHostname)"
    "
    .. _dcmUserIdentityNegotiation:
    .. _archiveDevice-dcmUserIdentityNegotiation:

    :ref:`User Identity Negotiation <archiveDevice-dcmUserIdentityNegotiation>`",string,"Specifies to ignore User Identity Negotiation Sub-Item in Association requests (=NOT_SUPPORTED), to verify passed Username and password or JSON Web Token are against a Keycloak server (=SUPPORTS), or to reject Association requests without a valid Username and password or JSON Web Token in its Identity Negotiation Sub-Item (=REQUIRED). May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NOT_SUPPORTED (= Ignore User Identity Negotiation Sub-Item in Association requests)

    SUPPORTS (= Verify passed Username and password or JSON Web Token are against a Keycloak server)

    REQUIRED (= Reject Association requests without a valid Username and password or JSON Web Token in its Identity Negotiation Sub-Item)

    (dcmUserIdentityNegotiation)"
    "
    .. _dcmUserIdentityNegotiationRole:
    .. _archiveDevice-dcmUserIdentityNegotiationRole:

    :ref:`User Identity Negotiation Role <archiveDevice-dcmUserIdentityNegotiationRole>`",string,"Constrain accepted User Identity Negotiation requests to users with specified role. If absent, only verify passed username and password or JSON Web Token. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUserIdentityNegotiationRole)"
    "
    .. _dcmUserIdentityNegotiationKeycloakClientID:
    .. _archiveDevice-dcmUserIdentityNegotiationKeycloakClientID:

    :ref:`User Identity Negotiation Keycloak Client ID <archiveDevice-dcmUserIdentityNegotiationKeycloakClientID>`",string,"Keycloak Client ID referring Keycloak connection configuration for verifying passed username and password or JSON Web Token. If absent, System Properties ${auth-server-url}, ${realm-name:dcm4che}, ${ui-client-id:dcm4chee-arc-ui}, ${disable-trust-manager:false}, ${allow-any-hostname:true} will be applied. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUserIdentityNegotiationKeycloakClientID)"
    "
    .. _dcmPersonNameComponentOrderInsensitiveMatching:
    .. _archiveDevice-dcmPersonNameComponentOrderInsensitiveMatching:

    :ref:`Person Name Component Order Insensitive Matching <archiveDevice-dcmPersonNameComponentOrderInsensitiveMatching>`",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names. May be overwritten by configured values for particular Archive Network AEs.

    (dcmPersonNameComponentOrderInsensitiveMatching)"
    "
    .. _dcmSendPendingCGet:
    .. _archiveDevice-dcmSendPendingCGet:

    :ref:`Send Pending C-Get <archiveDevice-dcmSendPendingCGet>`",boolean,"Enables pending C-GET responses. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSendPendingCGet)"
    "
    .. _dcmSendPendingCMoveInterval:
    .. _archiveDevice-dcmSendPendingCMoveInterval:

    :ref:`Send Pending C-Move Interval <archiveDevice-dcmSendPendingCMoveInterval>`",string,"Interval of pending C-MOVE responses in ISO-8601 duration format PnDTnHnMnS; disabled if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSendPendingCMoveInterval)"
    "
    .. _dcmWadoSupportedSRClasses:
    .. _archiveDevice-dcmWadoSupportedSRClasses:

    :ref:`Wado Supported SR Classes(s) <archiveDevice-dcmWadoSupportedSRClasses>`",string,"Supported SR SOP classes for WADO retrieval

    (dcmWadoSupportedSRClasses)"
    "
    .. _dcmWadoSupportedPRClasses:
    .. _archiveDevice-dcmWadoSupportedPRClasses:

    :ref:`Wado Supported PR Classes(s) <archiveDevice-dcmWadoSupportedPRClasses>`",string,"Supported PR SOP classes for WADO retrieval

    (dcmWadoSupportedPRClasses)"
    "
    .. _dcmWadoSR2HtmlTemplateURI:
    .. _archiveDevice-dcmWadoSR2HtmlTemplateURI:

    :ref:`Wado SR2 Html Template URI <archiveDevice-dcmWadoSR2HtmlTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to html. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoSR2HtmlTemplateURI)"
    "
    .. _dcmWadoSR2TextTemplateURI:
    .. _archiveDevice-dcmWadoSR2TextTemplateURI:

    :ref:`Wado SR2 Text Template URI <archiveDevice-dcmWadoSR2TextTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to plain text. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoSR2TextTemplateURI)"
    "
    .. _dcmWadoCDA2HtmlTemplateURI:
    .. _archiveDevice-dcmWadoCDA2HtmlTemplateURI:

    :ref:`Wado CDA to HTML Template URI <archiveDevice-dcmWadoCDA2HtmlTemplateURI>`",string,"URL to XSL style sheet inserted as <?xml-stylesheet type=""text/xsl"" href=""<url>"" > in CDA documents returned by WADO-URI service. If absent, the embedded CDI document is returned verbatim. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoCDA2HtmlTemplateURI)"
    "
    .. _dcmWadoThumbnailViewport:
    .. _archiveDevice-dcmWadoThumbnailViewport:

    :ref:`Wado Thumbnail Viewport <archiveDevice-dcmWadoThumbnailViewport>`",string,"Dimension of Thumbnails returned by WADO retrieve of Instance Thumbnails, if no Viewport is specified in the request. Format: <width>,<height>. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoThumbnailViewport)"
    "
    .. _dcmWadoZIPEntryNameFormat:
    .. _archiveDevice-dcmWadoZIPEntryNameFormat:

    :ref:`Wado ZIP Entry Name Format <archiveDevice-dcmWadoZIPEntryNameFormat>`",string,"Format of entry names in ZIP archive returned by WADO-RS. May be overwritten by configured value for particular Archive Network AEs.

    (dcmWadoZIPEntryNameFormat)"
    "
    .. _dcmWadoIgnorePresentationLUTShape:
    .. _archiveDevice-dcmWadoIgnorePresentationLUTShape:

    :ref:`Wado Ignore Presentation LUT Shape <archiveDevice-dcmWadoIgnorePresentationLUTShape>`",boolean,"Indicates to ignore (2050,0020) Presentation LUT Shape, but prioritize value of (0028,0004) Photometric Interpretation to determine if minimum sample value is intended to be displayed as white (=MONCHROME1) or as black (=MONCHROME2) on retrieve of rendered DICOM images by WADO-RS or WADO-URI services. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoIgnorePresentationLUTShape)"
    "
    .. _dcmWadoMetadataExcludePrivate:
    .. _archiveDevice-dcmWadoMetadataExcludePrivate:

    :ref:`Wado Metadata Exclude Private <archiveDevice-dcmWadoMetadataExcludePrivate>`",boolean,"Indicates to exclude Private Data Elements from Metadata returned by WADO-RS Retrieve Transaction. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoMetadataExcludePrivate)"
    "
    .. _dcmWadoVideoAcceptRanges:
    .. _archiveDevice-dcmWadoVideoAcceptRanges:

    :ref:`Wado Video Accept Ranges <archiveDevice-dcmWadoVideoAcceptRanges>`",string,"Indicates if Range Requests accessing encapsulated videos by WADO-URI or WADO-RS Rendered Instance are supported. May be overwritten by configured value for particular Archive Network AEs.

    Enumerated values:

    YES (= HTTP Range Requests supported)

    NO (= HTTP Range Requests not supported)

    KNOWN_TOTAL_LENGTH (= HTTP Range Requests supported if Encapsulated Pixel Data Value Total Length is known)

    (dcmWadoVideoAcceptRanges)"
    "
    .. _dcmQueryFetchSize:
    .. _archiveDevice-dcmQueryFetchSize:

    :ref:`Query Fetch Size <archiveDevice-dcmQueryFetchSize>`",integer,"Number of rows fetched from the database at once by the Query Service.

    (dcmQueryFetchSize)"
    "
    .. _dcmQueryMaxNumberOfResults:
    .. _archiveDevice-dcmQueryMaxNumberOfResults:

    :ref:`Query Max Number Of Results <archiveDevice-dcmQueryMaxNumberOfResults>`",integer,"Maximal number of return results by C-FIND SCP. If the number of matches extends the limit, the C-FIND request will be refused. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQueryMaxNumberOfResults)"
    "
    .. _dcmQidoMaxNumberOfResults:
    .. _archiveDevice-dcmQidoMaxNumberOfResults:

    :ref:`QIDO Max Number Of Results <archiveDevice-dcmQidoMaxNumberOfResults>`",integer,"Maximal number of return results by QIDO-RS Service. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoMaxNumberOfResults)"
    "
    .. _dcmQidoETag:
    .. _archiveDevice-dcmQidoETag:

    :ref:`QIDO ETag <archiveDevice-dcmQidoETag>`",boolean,"Indicates to return Last-Modified and ETag for Search Series or Instances of a Study; disabled if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoETag)"
    "
    .. _dcmQidoResultOrderBy:
    .. _archiveDevice-dcmQidoResultOrderBy:

    :ref:`QIDO Result Order By(s) <archiveDevice-dcmQidoResultOrderBy>`",string,"Specifies order of matching results returned by QIDO-RS, UPS-RS and proprietary Search Services, if not specified by query parameter orderby. Format: {service}:[-]{attributeID}[,...], with {service} is patients, studies, series, instances, workitems, mwlitems or mpps. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoResultOrderBy)"
    "
    .. _dcmFwdMppsDestination:
    .. _archiveDevice-dcmFwdMppsDestination:

    :ref:`MPPS Forward Destination(s) <archiveDevice-dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFwdMppsDestination)"
    "
    .. _dcmIanDestination:
    .. _archiveDevice-dcmIanDestination:

    :ref:`IAN Destination(s) <archiveDevice-dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanDestination)"
    "
    .. _dcmIanTrigger:
    .. _archiveDevice-dcmIanTrigger:

    :ref:`IAN Trigger(s) <archiveDevice-dcmIanTrigger>`",string,"Events triggering to send an IAN N-CREATE RQ to Application Entities configured by IAN Destination. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    STUDY_RECEIVED (= Send IAN on receiving studies)

    MPPS_RECEIVED (= Send IAN on receiving MPPS)

    REJECTION_NOTE_RECEIVED (= Send IAN on IOCM trigger)

    FIRST_OBJECT_OF_STUDY_RECEIVED (= Send IAN on receiving first object of study)

    (dcmIanTrigger)"
    "
    .. _dcmIanDelay:
    .. _archiveDevice-dcmIanDelay:

    :ref:`IAN Delay <archiveDevice-dcmIanDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which an IAN for a received study is sent to configured IAN destinations. Only effective if IAN Trigger includes STUDY_RECEIVED. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanDelay)"
    "
    .. _dcmIanTimeout:
    .. _archiveDevice-dcmIanTimeout:

    :ref:`IAN Timeout <archiveDevice-dcmIanTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMnS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. Only effective if IAN Trigger includes MPPS_RECEIVED. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanTimeout)"
    "
    .. _dcmIanOnTimeout:
    .. _archiveDevice-dcmIanOnTimeout:

    :ref:`IAN On Timeout <archiveDevice-dcmIanOnTimeout>`",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced in MPPS is exceeded. Only effective if IAN Trigger includes MPPS_RECEIVED. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanOnTimeout)"
    "
    .. _dcmIanTaskPollingInterval:
    .. _archiveDevice-dcmIanTaskPollingInterval:

    :ref:`IAN Task Polling Interval <archiveDevice-dcmIanTaskPollingInterval>`",string,"Polling Interval for IAN Tasks in ISO-8601 duration format PnDTnHnMnS for checking vor completeness of study or instances referenced in MPPS. If absent, configured IAN Trigger STUDY_RECEIVED or MPPS_RECEIVED will not be effective.

    (dcmIanTaskPollingInterval)"
    "
    .. _dcmIanTaskFetchSize:
    .. _archiveDevice-dcmIanTaskFetchSize:

    :ref:`IAN Task Fetch Size <archiveDevice-dcmIanTaskFetchSize>`",integer,"Maximal number of IAN Tasks scheduled in one transaction.

    (dcmIanTaskFetchSize)"
    "
    .. _dcmSpanningCFindSCP:
    .. _archiveDevice-dcmSpanningCFindSCP:

    :ref:`Spanning C-Find SCP <archiveDevice-dcmSpanningCFindSCP>`",string,"AE Title of external C-FIND SCP to forward C-FIND RQs and backward responses according configured Spanning C-Find SCP Policy. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSpanningCFindSCP)"
    "
    .. _dcmSpanningCFindSCPPolicy:
    .. _archiveDevice-dcmSpanningCFindSCPPolicy:

    :ref:`Spanning C-Find SCP Policy <archiveDevice-dcmSpanningCFindSCPPolicy>`",string,"Specifies policy for combining matches returned from configured Spanning C-Find SCP with matching entries from the archive DB. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    SUPPLEMENT (= Returns local matches before additional matches from Spanning C-Find SCP)

    MERGE (= Returns matches from Spanning C-Find SCP before additional local matches)

    REPLACE (= Returns only matches from Spanning C-Find SCP)

    (dcmSpanningCFindSCPPolicy)"
    "
    .. _dcmSpanningCFindSCPRetrieveAET:
    .. _archiveDevice-dcmSpanningCFindSCPRetrieveAET:

    :ref:`Spanning C-Find SCP Retrieve AE Title(s) <archiveDevice-dcmSpanningCFindSCPRetrieveAET>`",string,"Specifies Retrieve AE Title(s) in returned matches from Spanning C-Find SCP. Keep original Retrieve AE Title(s) returned by Spanning C-Find SCP if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSpanningCFindSCPRetrieveAET)"
    "
    .. _dcmFallbackCMoveSCP:
    .. _archiveDevice-dcmFallbackCMoveSCP:

    :ref:`Fallback C-Move SCP <archiveDevice-dcmFallbackCMoveSCP>`",string,"AE Title of external C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not managed by this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFallbackCMoveSCP)"
    "
    .. _dcmFallbackCMoveSCPDestination:
    .. _archiveDevice-dcmFallbackCMoveSCPDestination:

    :ref:`Fallback C-Move SCP Destination <archiveDevice-dcmFallbackCMoveSCPDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to the external C-MOVE SCP specified by dcmFallbackCMoveSCP

    (dcmFallbackCMoveSCPDestination)"
    "
    .. _dcmFallbackCMoveSCPStudyOlderThan:
    .. _archiveDevice-dcmFallbackCMoveSCPStudyOlderThan:

    :ref:`Fallback C-Move SCP Study Older Than <archiveDevice-dcmFallbackCMoveSCPStudyOlderThan>`",string,"Specifies threshold for Study Date in format YYYYMMDD for marking received Studies as (potential) incomplete to enforce the retrieve from configured dcmFallbackCMoveSCP

    (dcmFallbackCMoveSCPStudyOlderThan)"
    "
    .. _dcmFallbackCMoveSCPLeadingCFindSCP:
    .. _archiveDevice-dcmFallbackCMoveSCPLeadingCFindSCP:

    :ref:`Fallback C-Move SCP Leading C-Find SCP <archiveDevice-dcmFallbackCMoveSCPLeadingCFindSCP>`",string,"AE Title of external C-FIND SCP for Verification of Number of Instances retrieved from external C-MOVE SCP specified by dcmFallbackCMoveSCP.

    (dcmFallbackCMoveSCPLeadingCFindSCP)"
    "
    .. _dcmFallbackCMoveSCPRetries:
    .. _archiveDevice-dcmFallbackCMoveSCPRetries:

    :ref:`Fallback C-Move SCP Retries <archiveDevice-dcmFallbackCMoveSCPRetries>`",integer,"Maximal number of retries to retrieve not available objects from C-MOVE SCP configured by dcmFallbackCMoveSCP. -1 = forever.

    (dcmFallbackCMoveSCPRetries)"
    "
    .. _dcmFallbackWadoURIWebAppName:
    .. _archiveDevice-dcmFallbackWadoURIWebAppName:

    :ref:`Fallback WADO-URI Web Application Name <archiveDevice-dcmFallbackWadoURIWebAppName>`",string,"Name of external Web Application to redirect WADO-URI requests if the requested Object is not available by this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFallbackWadoURIWebAppName)"
    "
    .. _dcmFallbackWadoURIHttpStatusCode:
    .. _archiveDevice-dcmFallbackWadoURIHttpStatusCode:

    :ref:`Fallback WADO-URI Http Status Code <archiveDevice-dcmFallbackWadoURIHttpStatusCode>`",integer,"HTTP Status code of Redirect Response configured by Fallback WADO-URI Web Application Name. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    301 (= Moved Permanently)

    302 (= Found)

    303 (= See Other)

    307 (= Temporary Redirect)

    (dcmFallbackWadoURIHttpStatusCode)"
    "
    .. _dcmFallbackWadoURIRedirectOnNotFound:
    .. _archiveDevice-dcmFallbackWadoURIRedirectOnNotFound:

    :ref:`Fallback WADO-URI Redirect On Not Found <archiveDevice-dcmFallbackWadoURIRedirectOnNotFound>`",boolean,"Indicates if WADO-URI requests are redirected to configured Fallback WADO-URI Web Application Name even if the object was not found or - if set to false - only if the object is no longer accessible on this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFallbackWadoURIRedirectOnNotFound)"
    "
    .. _dcmExternalWadoRSWebAppName:
    .. _archiveDevice-dcmExternalWadoRSWebAppName:

    :ref:`External WADO-RS Web Application Name <archiveDevice-dcmExternalWadoRSWebAppName>`",string,"Name of external Web Application to redirect WADO-RS requests if some of the requested objects are no longer accessible on this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmExternalWadoRSWebAppName)"
    "
    .. _dcmExternalWadoRSHttpStatusCode:
    .. _archiveDevice-dcmExternalWadoRSHttpStatusCode:

    :ref:`External WADO-RS Http Status Code <archiveDevice-dcmExternalWadoRSHttpStatusCode>`",integer,"HTTP Status code of Redirect Response configured by External WADO-RS Web Application Name. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    301 (= Moved Permanently)

    302 (= Found)

    303 (= See Other)

    307 (= Temporary Redirect)

    (dcmExternalWadoRSHttpStatusCode)"
    "
    .. _dcmExternalWadoRSRedirectOnNotFound:
    .. _archiveDevice-dcmExternalWadoRSRedirectOnNotFound:

    :ref:`External WADO-RS Redirect On Not Found <archiveDevice-dcmExternalWadoRSRedirectOnNotFound>`",boolean,"Indicates if WADO-RS requests are redirected to configured External WADO-RS Web Application Name even if the requested objects were not found or - if set to false - only if some of the requested objects are no longer accessible on this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmExternalWadoRSRedirectOnNotFound)"
    "
    .. _dcmFallbackCMoveSCPCallingAET:
    .. _archiveDevice-dcmFallbackCMoveSCPCallingAET:

    :ref:`Fallback C-Move SCP Calling AE title <archiveDevice-dcmFallbackCMoveSCPCallingAET>`",string,"Calling AE Title used in A-ASSOCIATE-RQ to configured Fallback C-MOVE SCP. If absent, the AE Title of the external C-MOVE SCU is used. May be overwritten by configured value for particular Archive Network AEs.

    (dcmFallbackCMoveSCPCallingAET)"
    "
    .. _dcmAltCMoveSCP:
    .. _archiveDevice-dcmAltCMoveSCP:

    :ref:`Alternative C-Move SCP <archiveDevice-dcmAltCMoveSCP>`",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage

    (dcmAltCMoveSCP)"
    "
    .. _dcmCStoreSCUOfCMoveSCP:
    .. _archiveDevice-dcmCStoreSCUOfCMoveSCP:

    :ref:`C-STORE SCU of C-MOVE SCP(s) <archiveDevice-dcmCStoreSCUOfCMoveSCP>`",string,"Indicates to identify received C-STORE RQs as caused by a forwarded C-MOVE RQs by the Calling AET in the A-Associate-RQ in format <Calling AET>=<C-MOVE-SCP>. Typically <Calling AET> and <C-MOVE-SCP> are equal. If no value is configured for a particular C-MOVE SCP, attribute (0000,1030) Move Originator Application Entity Title in the C-STORE RQ is used to find the corresponding forwarded C-MOVE RQ to forward the received C-STORE RQ to the original Move Destination.

    (dcmCStoreSCUOfCMoveSCP)"
    "
    .. _dcmTaskPollingInterval:
    .. _archiveDevice-dcmTaskPollingInterval:

    :ref:`Task Polling Interval <archiveDevice-dcmTaskPollingInterval>`",string,"Polling Interval for scheduled Tasks in ISO-8601 duration format PnDTnHnMnS. If absent, Tasks will not get processed.

    (dcmTaskPollingInterval)"
    "
    .. _dcmTaskFetchSize:
    .. _archiveDevice-dcmTaskFetchSize:

    :ref:`Task Fetch Size <archiveDevice-dcmTaskFetchSize>`",integer,"Limit result set of DB query for scheduled Tasks.

    (dcmTaskFetchSize)"
    "
    .. _dcmUPSProcessingPollingInterval:
    .. _archiveDevice-dcmUPSProcessingPollingInterval:

    :ref:`UPS Processing Polling Interval <archiveDevice-dcmUPSProcessingPollingInterval>`",string,"Polling Interval for Workitems ready for processing in ISO-8601 duration format PnDTnHnMnS.

    (dcmUPSProcessingPollingInterval)"
    "
    .. _dcmUPSProcessingFetchSize:
    .. _archiveDevice-dcmUPSProcessingFetchSize:

    :ref:`UPS Processing  Fetch Size <archiveDevice-dcmUPSProcessingFetchSize>`",integer,"Limit result set of DB query for Workitems ready for processing.

    (dcmUPSProcessingFetchSize)"
    "
    .. _dcmRetrieveTaskWarningOnNoMatch:
    .. _archiveDevice-dcmRetrieveTaskWarningOnNoMatch:

    :ref:`Retrieve Task Warning on no Match <archiveDevice-dcmRetrieveTaskWarningOnNoMatch>`",boolean,"Indicates if the result status of Retrieve Tasks shall be set to WARNING if none of the requested objects was found on the C-MOVE SCP. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveTaskWarningOnNoMatch)"
    "
    .. _dcmRetrieveTaskWarningOnWarnings:
    .. _archiveDevice-dcmRetrieveTaskWarningOnWarnings:

    :ref:`Retrieve Task Warning on Warnings <archiveDevice-dcmRetrieveTaskWarningOnWarnings>`",boolean,"Indicates if the result status of Retrieve Tasks shall be set to WARNING if there are Warning Sub-Operations, even if the retrieve of all objects was successful. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveTaskWarningOnWarnings)"
    "
    .. _dcmPurgeStoragePollingInterval:
    .. _archiveDevice-dcmPurgeStoragePollingInterval:

    :ref:`Purge Storage Polling Interval <archiveDevice-dcmPurgeStoragePollingInterval>`",string,"Polling Interval for deleting objects in ISO-8601 duration format PnDTnHnMnS.

    (dcmPurgeStoragePollingInterval)"
    "
    .. _dcmPurgeStorageFetchSize:
    .. _archiveDevice-dcmPurgeStorageFetchSize:

    :ref:`Purge Storage Fetch Size <archiveDevice-dcmPurgeStorageFetchSize>`",integer,"Maximal number of objects to delete in one task.

    (dcmPurgeStorageFetchSize)"
    "
    .. _dcmFailedToDeletePollingInterval:
    .. _archiveDevice-dcmFailedToDeletePollingInterval:

    :ref:`Failed to delete Polling Interval <archiveDevice-dcmFailedToDeletePollingInterval>`",string,"Polling Interval for resolving deletion failures in ISO-8601 duration format PnDTnHnMnS.

    (dcmFailedToDeletePollingInterval)"
    "
    .. _dcmFailedToDeleteFetchSize:
    .. _archiveDevice-dcmFailedToDeleteFetchSize:

    :ref:`Failed to delete Fetch Size <archiveDevice-dcmFailedToDeleteFetchSize>`",integer,"Maximal number of Location records fetched for resolving deletion failures in one query.

    (dcmFailedToDeleteFetchSize)"
    "
    .. _dcmDeleteStudyBatchSize:
    .. _archiveDevice-dcmDeleteStudyBatchSize:

    :ref:`Delete Study Batch Size <archiveDevice-dcmDeleteStudyBatchSize>`",integer,"Number of Studies to delete from the Storage System, if the usable space fall below configured Usable Space, before checking the usable space again.

    (dcmDeleteStudyBatchSize)"
    "
    .. _dcmDeleteStudyInterval:
    .. _archiveDevice-dcmDeleteStudyInterval:

    :ref:`Delete Study Interval <archiveDevice-dcmDeleteStudyInterval>`",string,"Specifies maximum range of access time of studies, in ISO-8601 duration format PnDTnHnMnS, to be deleted from the storage system, if the usable space falls below configured Deleter Thresholds, before checking the Deleter Thresholds again. If absent, the number of Studies to be deleted is only limited by configured Delete Study Batch Size.

    (dcmDeleteStudyInterval)"
    "
    .. _dcmPreserveStudyInterval:
    .. _archiveDevice-dcmPreserveStudyInterval:

    :ref:`Preserve Study Interval <archiveDevice-dcmPreserveStudyInterval>`",string,"Protect studies which were accessed later than the specified time interval, in ISO-8601 duration format PnDTnHnMnS, from deletion from the storage system, if the usable space falls below configured Deleter Thresholds. If absent, most recently accessed studies shall also get deleted from the storage system, if least recently accessed studies were not found or if Delete Least Recently Accessed Study First is set to FALSE.

    (dcmPreserveStudyInterval)"
    "
    .. _dcmDeleteStudyLeastRecentlyAccessedFirst:
    .. _archiveDevice-dcmDeleteStudyLeastRecentlyAccessedFirst:

    :ref:`Delete Least Recently Accessed Study First <archiveDevice-dcmDeleteStudyLeastRecentlyAccessedFirst>`",boolean,"Indicates to delete studies beginning with the least recently accessed study first, if the usable space falls below configured Deleter Thresholds. By default, TRUE.

    (dcmDeleteStudyLeastRecentlyAccessedFirst)"
    "
    .. _dcmDeleteStudyChunkSize:
    .. _archiveDevice-dcmDeleteStudyChunkSize:

    :ref:`Delete Study Chunk Size <archiveDevice-dcmDeleteStudyChunkSize>`",integer,"Number of Instances deleted in one DB transaction on permanent deletion of Studies.

    (dcmDeleteStudyChunkSize)"
    "
    .. _dcmDeletePatientOnDeleteLastStudy:
    .. _archiveDevice-dcmDeletePatientOnDeleteLastStudy:

    :ref:`Delete Patient On Delete Last Study <archiveDevice-dcmDeletePatientOnDeleteLastStudy>`",boolean,"Specifies if a Patient shall be deleted on deletion of its last study.

    (dcmDeletePatientOnDeleteLastStudy)"
    "
    .. _dcmDeleteRejectedPollingInterval:
    .. _archiveDevice-dcmDeleteRejectedPollingInterval:

    :ref:`Delete Rejected Polling Interval <archiveDevice-dcmDeleteRejectedPollingInterval>`",string,"Polling Interval for deleting rejected instances from the DB in ISO-8601 duration format PnDTnHnMnS.

    (dcmDeleteRejectedPollingInterval)"
    "
    .. _dcmDeleteRejectedFetchSize:
    .. _archiveDevice-dcmDeleteRejectedFetchSize:

    :ref:`Delete Rejected Fetch Size <archiveDevice-dcmDeleteRejectedFetchSize>`",integer,"Maximal number of rejected instances to delete from the DB in one task.

    (dcmDeleteRejectedFetchSize)"
    "
    .. _dcmDBReadOnly:
    .. _archiveDevice-dcmDBReadOnly:

    :ref:`DB Read Only <archiveDevice-dcmDBReadOnly>`",boolean,"Indicates read-only access to the database, preventing DB updates on query/retrieve.

    (dcmDBReadOnly)"
    "
    .. _dcmMaxAccessTimeStaleness:
    .. _archiveDevice-dcmMaxAccessTimeStaleness:

    :ref:`Maximum Access Time Staleness <archiveDevice-dcmMaxAccessTimeStaleness>`",string,"Maximal staleness of recorded study accession time in ISO-8601 duration format PnDTnHnMnS. Update of the access time disabled, if absent.

    (dcmMaxAccessTimeStaleness)"
    "
    .. _dcmAECacheStaleTimeout:
    .. _archiveDevice-dcmAECacheStaleTimeout:

    :ref:`AE Cache Stale Timeout <archiveDevice-dcmAECacheStaleTimeout>`",string,"Maximal staleness of cached AE in ISO-8601 duration format PnDTnHnMnS. If absent, cached AE entries will not be refetched from LDAP.

    (dcmAECacheStaleTimeout)"
    "
    .. _dcmLeadingCFindSCPQueryCacheStaleTimeout:
    .. _archiveDevice-dcmLeadingCFindSCPQueryCacheStaleTimeout:

    :ref:`Leading C-Find SCP Query Cache Stale Timeout <archiveDevice-dcmLeadingCFindSCPQueryCacheStaleTimeout>`",string,"Maximal staleness of cached Patient and Study attributes fetched from leading C-Find SCP in ISO-8601 duration format PnDTnHnMnS. If absent, cache Study attributes are only removed on reaching the maximal cache size.

    (dcmLeadingCFindSCPQueryCacheStaleTimeout)"
    "
    .. _dcmLeadingCFindSCPQueryCacheSize:
    .. _archiveDevice-dcmLeadingCFindSCPQueryCacheSize:

    :ref:`Leading C-Find SCP Query Cache Size <archiveDevice-dcmLeadingCFindSCPQueryCacheSize>`",integer,"Maximum number of cached Patient and Study attributes fetched from leading C-Find SCP.

    (dcmLeadingCFindSCPQueryCacheSize)"
    "
    .. _dcmAuditSpoolDirectory:
    .. _archiveDevice-dcmAuditSpoolDirectory:

    :ref:`Audit Spool Directory <archiveDevice-dcmAuditSpoolDirectory>`",string,"Path to Audit Service Spool Directory.

    (dcmAuditSpoolDirectory)"
    "
    .. _dcmAuditPollingInterval:
    .. _archiveDevice-dcmAuditPollingInterval:

    :ref:`Audit Polling Interval <archiveDevice-dcmAuditPollingInterval>`",string,"Polling Interval for aggregating Audit Messages in ISO-8601 duration format PnDTnHnMnS. Audit Message aggregation disabled, if absent.

    (dcmAuditPollingInterval)"
    "
    .. _dcmAuditAggregateDuration:
    .. _archiveDevice-dcmAuditAggregateDuration:

    :ref:`Audit Aggregate Duration <archiveDevice-dcmAuditAggregateDuration>`",string,"Audit Message Aggregation Duration in ISO-8601 duration format PnDTnHnMnS. Audit Message aggregation disabled, if absent.

    (dcmAuditAggregateDuration)"
    "
    .. _dcmAuditUnknownStudyInstanceUID:
    .. _archiveDevice-dcmAuditUnknownStudyInstanceUID:

    :ref:`Audit Unknown Study Instance UID <archiveDevice-dcmAuditUnknownStudyInstanceUID>`",string,"Indicates study instance uid value to be sent in audit message when not known.

    (dcmAuditUnknownStudyInstanceUID)"
    "
    .. _dcmAuditUnknownPatientID:
    .. _archiveDevice-dcmAuditUnknownPatientID:

    :ref:`Audit Unknown Patient ID <archiveDevice-dcmAuditUnknownPatientID>`",string,"Indicates patient id value to be sent in audit message when not known.

    (dcmAuditUnknownPatientID)"
    "
    .. _dcmAudit2JsonFhirTemplateURI:
    .. _archiveDevice-dcmAudit2JsonFhirTemplateURI:

    :ref:`Audit to json+fhir Template URI <archiveDevice-dcmAudit2JsonFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR JSON Resource Audit Event

    (dcmAudit2JsonFhirTemplateURI)"
    "
    .. _dcmAudit2XmlFhirTemplateURI:
    .. _archiveDevice-dcmAudit2XmlFhirTemplateURI:

    :ref:`Audit to xml+fhir Template URI <archiveDevice-dcmAudit2XmlFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR XML Resource Audit Event

    (dcmAudit2XmlFhirTemplateURI)"
    "
    .. _dcmAuditSoftwareConfigurationVerbose:
    .. _archiveDevice-dcmAuditSoftwareConfigurationVerbose:

    :ref:`Audit Software Configuration Verbose <archiveDevice-dcmAuditSoftwareConfigurationVerbose>`",boolean,"Specifies if Child Objects and Attributes of created Objects should be included in Software Configuration Audit Message.

    (dcmAuditSoftwareConfigurationVerbose)"
    "
    .. _dcmAuditAssigningAuthorityOfPatientID:
    .. _archiveDevice-dcmAuditAssigningAuthorityOfPatientID:

    :ref:`Assigning Authority of Patient ID for Audit <archiveDevice-dcmAuditAssigningAuthorityOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search qualified patient identifier in list of identifiers in PID-3. This qualified patient identifier shall be used in the patient details participant object. If absent, by default the first qualified patient identifier in PID-3 shall be used. If none of the qualified patient identifiers in the list match with the configured issuer, archive server log shall contain a log INFO message and by default the first qualified patient identifier in PID-3 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmAuditAssigningAuthorityOfPatientID)"
    "
    .. _dcmShowPatientInfoInSystemLog:
    .. _archiveDevice-dcmShowPatientInfoInSystemLog:

    :ref:`Show Patient Info In System Log <archiveDevice-dcmShowPatientInfoInSystemLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in system logs.

    Enumerated values:

    PLAIN_TEXT (= Patient Identifier and Patient Name shown as plain text in system logs)

    HASH_NAME (= Patient Identifier shown as plain text, Patient Name shown as hashed in system logs)

    HASH_NAME_AND_ID (= Patient Identifier and Patient Name shown as hashed in system logs)

    (dcmShowPatientInfoInSystemLog)"
    "
    .. _dcmShowPatientInfoInAuditLog:
    .. _archiveDevice-dcmShowPatientInfoInAuditLog:

    :ref:`Show Patient Info In Audit Log <archiveDevice-dcmShowPatientInfoInAuditLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in emitted audit messages.

    Enumerated values:

    PLAIN_TEXT (= Patient Identifier and Patient Name shown as plain text in audit logs)

    HASH_NAME (= Patient Identifier shown as plain text, Patient Name shown as hashed in audit logs)

    HASH_NAME_AND_ID (= Patient Identifier and Patient Name shown as hashed in audit logs)

    (dcmShowPatientInfoInAuditLog)"
    "
    .. _dcmStowSpoolDirectory:
    .. _archiveDevice-dcmStowSpoolDirectory:

    :ref:`STOW-RS Spool Directory <archiveDevice-dcmStowSpoolDirectory>`",string,"Path to Directory used by STOW-RS Service to spool Bulkdata of XML/JSON Metadata and Bulk Data Request Messages.

    (dcmStowSpoolDirectory)"
    "
    .. _dcmMWLAccessionNumberGenerator:
    .. _archiveDevice-dcmMWLAccessionNumberGenerator:

    :ref:`MWL Accession Number Generator <archiveDevice-dcmMWLAccessionNumberGenerator>`",string,"Identifies ID Generator to supplement missing Accession Numbers of Scheduled Procedures Steps created on receive of HL7 Order messages or by RESTful service. May be overwritten by configured values for particular Archive Network AEs or Archive HL7 Application.

    (dcmMWLAccessionNumberGenerator)"
    "
    .. _dcmMWLRequestedProcedureIDGenerator:
    .. _archiveDevice-dcmMWLRequestedProcedureIDGenerator:

    :ref:`MWL Requested Procedure ID Generator <archiveDevice-dcmMWLRequestedProcedureIDGenerator>`",string,"Identifies ID Generator to supplement missing Requested Procedure IDs of Scheduled Procedures Steps created on receive of HL7 Order messages or by RESTful service. May be overwritten by configured values for particular Archive Network AEs or Archive HL7 Application.

    (dcmMWLRequestedProcedureIDGenerator)"
    "
    .. _dcmMWLScheduledProcedureStepIDGenerator:
    .. _archiveDevice-dcmMWLScheduledProcedureStepIDGenerator:

    :ref:`MWL Scheduled Procedure Step ID Generator <archiveDevice-dcmMWLScheduledProcedureStepIDGenerator>`",string,"Identifies ID Generator to supplement missing Scheduled Procedure Step IDs of Scheduled Procedures Steps created on receive of HL7 Order messages or by RESTful service. May be overwritten by configured values for particular Archive Network AEs or Archive HL7 Application.

    (dcmMWLScheduledProcedureStepIDGenerator)"
    "
    .. _dcmAuditHL7MsgLimit:
    .. _archiveDevice-dcmAuditHL7MsgLimit:

    :ref:`Audit HL7 Message Limit <archiveDevice-dcmAuditHL7MsgLimit>`",integer,"Limit length of HL7 messages included in emitted Audit Records. May be overwritten by configured values for particular Archive HL7 Application.

    (dcmAuditHL7MsgLimit)"
    "
    .. _hl7ORUAction:
    .. _archiveDevice-hl7ORUAction:

    :ref:`HL7 ORU Action(s) <archiveDevice-hl7ORUAction>`",string,"Specifies action on receive of HL7 ORU^R01 message. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    IMPORT_REPORT (= Transcode received HL7 ORU^R01 to DICOM SR or PDF or CDA)

    MWL_COMPLETED (= Set Status of matching MWL items to COMPLETED)

    (hl7ORUAction)"
    "
    .. _hl7PatientUpdateTemplateURI:
    .. _archiveDevice-hl7PatientUpdateTemplateURI:

    :ref:`HL7 Patient Update Template URI <archiveDevice-hl7PatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7PatientUpdateTemplateURI)"
    "
    .. _hl7ImportReportTemplateURI:
    .. _archiveDevice-hl7ImportReportTemplateURI:

    :ref:`HL7 Import Report Template URI <archiveDevice-hl7ImportReportTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ImportReportTemplateURI)"
    "
    .. _hl7ImportReportTemplateParam:
    .. _archiveDevice-hl7ImportReportTemplateParam:

    :ref:`HL7 Import Report Template Parameter(s) <archiveDevice-hl7ImportReportTemplateParam>`",string,"XSLT parameters passed to style sheet specified by HL7 Import Report Template URI. Format: {name}={value}. E.g.: 'langCodeValue=et', 'langCodingSchemeDesignator=RFC5646', 'langCodeMeaning=Estonian'. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ImportReportTemplateParam)"
    "
    .. _hl7ScheduleProcedureTemplateURI:
    .. _archiveDevice-hl7ScheduleProcedureTemplateURI:

    :ref:`HL7 Schedule Procedure Template URI <archiveDevice-hl7ScheduleProcedureTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ScheduleProcedureTemplateURI)"
    "
    .. _hl7OutgoingPatientUpdateTemplateURI:
    .. _archiveDevice-hl7OutgoingPatientUpdateTemplateURI:

    :ref:`HL7 Outgoing Patient Update Template URI <archiveDevice-hl7OutgoingPatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet to transcode DICOM object patient attributes to HL7 ADT messages.

    (hl7OutgoingPatientUpdateTemplateURI)"
    "
    .. _hl7ScheduledProtocolCodeInOrder:
    .. _archiveDevice-hl7ScheduledProtocolCodeInOrder:

    :ref:`HL7 Schedule Protocol Code in Order <archiveDevice-hl7ScheduledProtocolCodeInOrder>`",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    OBR_4_1 (= HL7 Schedule Protocol Code in Order in OBR.4.1 to OBR.4.3)

    OBR_4_4 (= HL7 Schedule Protocol Code in Order in OBR.4.4 to OBR.4.6)

    (hl7ScheduledProtocolCodeInOrder)"
    "
    .. _hl7ScheduledStationAETInOrder:
    .. _archiveDevice-hl7ScheduledStationAETInOrder:

    :ref:`HL7 Schedule Station AET in Order <archiveDevice-hl7ScheduledStationAETInOrder>`",string,"Specifies location of Scheduled Station AE Title in received HL7 Order message. Should not be configured for HL7 v2.5.1 OMI^O23 with IPC segment. If absent or no value is provided in the configured field, the Scheduled Station AE Title is selected according configured rules. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ORC_18 (= HL7 Schedule Station AET in Order in ORC.18)

    (hl7ScheduledStationAETInOrder)"
    "
    .. _hl7LogFilePattern:
    .. _archiveDevice-hl7LogFilePattern:

    :ref:`HL7 Log File Pattern <archiveDevice-hl7LogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7LogFilePattern)"
    "
    .. _hl7ErrorLogFilePattern:
    .. _archiveDevice-hl7ErrorLogFilePattern:

    :ref:`HL7 Error Log File Pattern <archiveDevice-hl7ErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7ErrorLogFilePattern)"
    "
    .. _hl7OutgoingLogFilePattern:
    .. _archiveDevice-hl7OutgoingLogFilePattern:

    :ref:`HL7 Outgoing Log File Pattern <archiveDevice-hl7OutgoingLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as sent. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-out/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7OutgoingLogFilePattern)"
    "
    .. _hl7OutgoingErrorLogFilePattern:
    .. _archiveDevice-hl7OutgoingErrorLogFilePattern:

    :ref:`HL7 Outgoing Error Log File Pattern <archiveDevice-hl7OutgoingErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as sent, when processing of sent HL7 messages fails. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-out-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7OutgoingErrorLogFilePattern)"
    "
    .. _hl7NoPatientCreateMessageType:
    .. _archiveDevice-hl7NoPatientCreateMessageType:

    :ref:`HL7 No Patient Create Message Type(s) <archiveDevice-hl7NoPatientCreateMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of HL7 messages which are only processed, if there is already a Patient record in the database, which Patient ID matches the Patient ID in the PID or MRG segment of the message. Thus no new Patient record will be created by messages of the specified types. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7NoPatientCreateMessageType)"
    "
    .. _hl7NoPatientUpdateMessageType:
    .. _archiveDevice-hl7NoPatientUpdateMessageType:

    :ref:`HL7 No Patient Update Message Type(s) <archiveDevice-hl7NoPatientUpdateMessageType>`",string,"Patient record will be not be updated by HL7 messages of specified Message Type(s) (MessageType^TriggerEvent). May be overwritten by configured values for particular Archive HL7 Application.

    (hl7NoPatientUpdateMessageType)"
    "
    .. _hl7PatientArrivalMessageType:
    .. _archiveDevice-hl7PatientArrivalMessageType:

    :ref:`HL7 Patient Arrival Message Type <archiveDevice-hl7PatientArrivalMessageType>`",string,"Message Type of HL7 messages which triggers the change the status of Scheduled Procedure Steps associated with the Patient from SCHEDULED to ARRIVED. If absent, the status of Scheduled Procedure Steps will not be affected by HL7 ADT messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ADT^A10 (= Patient Arriving / Tracking)

    (hl7PatientArrivalMessageType)"
    "
    .. _dcmUnzipVendorDataToURI:
    .. _archiveDevice-dcmUnzipVendorDataToURI:

    :ref:`Unzip Vendor Data To URI <archiveDevice-dcmUnzipVendorDataToURI>`",string,"Specifies URI of directory into which ZIP stream in Device Vendor Data attribute will be extracted

    (dcmUnzipVendorDataToURI)"
    "
    .. _dcmPurgeQueueMessagePollingInterval:
    .. _archiveDevice-dcmPurgeQueueMessagePollingInterval:

    :ref:`Purge Task Polling Interval <archiveDevice-dcmPurgeQueueMessagePollingInterval>`",string,"Polling Interval for purging tasks in ISO-8601 duration format PnDTnHnMnS. If absent, there is no deletion

    (dcmPurgeQueueMessagePollingInterval)"
    "
    .. _dcmWadoSpoolDirectory:
    .. _archiveDevice-dcmWadoSpoolDirectory:

    :ref:`Wado-RS Spool Directory <archiveDevice-dcmWadoSpoolDirectory>`",string,"Path to Wado-RS spool directory used to aggregate uncompressed frames.

    (dcmWadoSpoolDirectory)"
    "
    .. _dcmRejectExpiredStudiesPollingInterval:
    .. _archiveDevice-dcmRejectExpiredStudiesPollingInterval:

    :ref:`Reject Expired Studies Polling Interval <archiveDevice-dcmRejectExpiredStudiesPollingInterval>`",string,"Polling Interval for rejecting expired Studies and Series in ISO-8601 duration format PnDTnHnMnS. If absent, neither expired Studies nor Series will be rejected automatically

    (dcmRejectExpiredStudiesPollingInterval)"
    "
    .. _dcmRejectExpiredStudiesSchedule:
    .. _archiveDevice-dcmRejectExpiredStudiesSchedule:

    :ref:`Reject Expired Studies Schedule(s) <archiveDevice-dcmRejectExpiredStudiesSchedule>`",string,"Limits Rejection of Expired Studies to specified times in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday).

    (dcmRejectExpiredStudiesSchedule)"
    "
    .. _dcmRejectExpiredStudiesFetchSize:
    .. _archiveDevice-dcmRejectExpiredStudiesFetchSize:

    :ref:`Reject Expired Studies Fetch Size <archiveDevice-dcmRejectExpiredStudiesFetchSize>`",integer,"Maximal number of expired Studies fetched in one query; If absent, expired Studies will not be rejected automatically

    (dcmRejectExpiredStudiesFetchSize)"
    "
    .. _dcmRejectExpiredSeriesFetchSize:
    .. _archiveDevice-dcmRejectExpiredSeriesFetchSize:

    :ref:`Reject Expired Series Fetch Size <archiveDevice-dcmRejectExpiredSeriesFetchSize>`",integer,"Maximal number of expired Series fetched in one query; If absent, expired Series will not be rejected automatically

    (dcmRejectExpiredSeriesFetchSize)"
    "
    .. _dcmRejectExpiredStudiesAETitle:
    .. _archiveDevice-dcmRejectExpiredStudiesAETitle:

    :ref:`Reject Expired Studies AE Title <archiveDevice-dcmRejectExpiredStudiesAETitle>`",string,"AE Title of Local Application Entity performing the automatic rejection of expired Studies and Series. If absent, neither expired Studies nor Series will be rejected automatically.

    (dcmRejectExpiredStudiesAETitle)"
    "
    .. _dcmStorePermissionServiceURL:
    .. _archiveDevice-dcmStorePermissionServiceURL:

    :ref:`Store Permission Service URL <archiveDevice-dcmStorePermissionServiceURL>`",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study by any AE. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http(s)://<store-permission-service-provider-host>:<store-permission-service-provider-port>/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030,urlencoded}. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceURL)"
    "
    .. _dcmStorePermissionServiceResponse:
    .. _archiveDevice-dcmStorePermissionServiceResponse:

    :ref:`Store Permission Service Response <archiveDevice-dcmStorePermissionServiceResponse>`",string,"Emulate Store Permission Service Response on receive of the first object of a study by any AE. {<dicomTag>} will be replaced by the value of the attribute in the object. Only effective if no Store Permission Service URL is configured. Example: patientID={00100020},patientName={00100010},errorCode=0110H,errorComment=errorMessage. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceResponse)"
    "
    .. _dcmStorePermissionServiceResponsePattern:
    .. _archiveDevice-dcmStorePermissionServiceResponsePattern:

    :ref:`Store Permission Service Response Pattern <archiveDevice-dcmStorePermissionServiceResponsePattern>`",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" or '(?<=patientName=)[^null].*?(?=,)'. If absent, every success response will be treated as agreement for storage. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceResponsePattern)"
    "
    .. _dcmStorePermissionServiceErrorCommentPattern:
    .. _archiveDevice-dcmStorePermissionServiceErrorCommentPattern:

    :ref:`Store Permission Service Error Comment Pattern <archiveDevice-dcmStorePermissionServiceErrorCommentPattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". If absent, ""Storage denied."" will be used as Error Comment. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceErrorCommentPattern)"
    "
    .. _dcmStorePermissionServiceErrorCodePattern:
    .. _archiveDevice-dcmStorePermissionServiceErrorCodePattern:

    :ref:`Store Permission Service Error Code Pattern <archiveDevice-dcmStorePermissionServiceErrorCodePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". If absent, the Error Code will be 0124H (Not Authorized). May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceErrorCodePattern)"
    "
    .. _dcmStorePermissionServiceExpirationDatePattern:
    .. _archiveDevice-dcmStorePermissionServiceExpirationDatePattern:

    :ref:`Store Permission Service Expiration Date Pattern <archiveDevice-dcmStorePermissionServiceExpirationDatePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". If absent, locally configured Study Retention Policy Rules will be applied. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceExpirationDatePattern)"
    "
    .. _dcmStorePermissionCacheStaleTimeout:
    .. _archiveDevice-dcmStorePermissionCacheStaleTimeout:

    :ref:`Store Permission Cache Stale Timeout <archiveDevice-dcmStorePermissionCacheStaleTimeout>`",string,"Maximal staleness of cached responses from Storage Permission Service in ISO-8601 duration format PnDTnHnMnS. If absent, cached responses are only removed on reaching the maximal cache size.

    (dcmStorePermissionCacheStaleTimeout)"
    "
    .. _dcmStorePermissionCacheSize:
    .. _archiveDevice-dcmStorePermissionCacheSize:

    :ref:`Store Permission Cache Size <archiveDevice-dcmStorePermissionCacheSize>`",integer,"Maximum number of cached responses from Storage Permission Service.

    (dcmStorePermissionCacheSize)"
    "
    .. _dcmMergeMWLCacheStaleTimeout:
    .. _archiveDevice-dcmMergeMWLCacheStaleTimeout:

    :ref:`Merge MWL Cache Stale Timeout <archiveDevice-dcmMergeMWLCacheStaleTimeout>`",string,"Maximal staleness of Request Attributes extracted from matching DICOM MWL items in ISO-8601 duration format PnDTnHnMnS. If absent, cached Request Attributes are only removed on reaching the maximal cache size.

    (dcmMergeMWLCacheStaleTimeout)"
    "
    .. _dcmMergeMWLCacheSize:
    .. _archiveDevice-dcmMergeMWLCacheSize:

    :ref:`Merge MWL Cache Size <archiveDevice-dcmMergeMWLCacheSize>`",integer,"Maximum number of cached Request Attributes extracted from matching DICOM MWL items.

    (dcmMergeMWLCacheSize)"
    "
    .. _dcmStoreUpdateDBMaxRetries:
    .. _archiveDevice-dcmStoreUpdateDBMaxRetries:

    :ref:`Store Update DB Maximum Number of Retries <archiveDevice-dcmStoreUpdateDBMaxRetries>`",integer,"Maximum number of retries to update the database on storage.

    (dcmStoreUpdateDBMaxRetries)"
    "
    .. _dcmStoreUpdateDBMinRetryDelay:
    .. _archiveDevice-dcmStoreUpdateDBMinRetryDelay:

    :ref:`Minimal Store Update DB Delay of Retry <archiveDevice-dcmStoreUpdateDBMinRetryDelay>`",integer,"Minimal Delay in ms between retries to update the database on storage.

    (dcmStoreUpdateDBMinRetryDelay)"
    "
    .. _dcmStoreUpdateDBMaxRetryDelay:
    .. _archiveDevice-dcmStoreUpdateDBMaxRetryDelay:

    :ref:`Maximal Store Update DB Delay of Retry <archiveDevice-dcmStoreUpdateDBMaxRetryDelay>`",integer,"Maximal Delay in ms between retries to update the database on storage.

    (dcmStoreUpdateDBMaxRetryDelay)"
    "
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:
    .. _archiveDevice-dcmAllowRejectionForDataRetentionPolicyExpired:

    :ref:`Allow Rejection For Data Retention Policy Expired <archiveDevice-dcmAllowRejectionForDataRetentionPolicyExpired>`",string,"Allow Rejection For Data Retention Policy Expired. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NEVER (= Never allow rejection for Data Retention Policy Expired)

    ALWAYS (= Always allow rejection for Data Retention Policy Expired)

    EXPIRED_UNSET (= Allow rejection for Data Retention Policy Expired for expired studies or studies with no expiration date)

    ONLY_EXPIRED (= Allow rejection for Data Retention Policy Expired only for expired studies)

    (dcmAllowRejectionForDataRetentionPolicyExpired)"
    "
    .. _dcmAllowDeleteStudyPermanently:
    .. _archiveDevice-dcmAllowDeleteStudyPermanently:

    :ref:`Allow Delete Study permanently <archiveDevice-dcmAllowDeleteStudyPermanently>`",string,"Allow to delete Study permanently. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    ALWAYS (= Always allow delete study permanently)

    REJECTED (= Allow delete study permanently only for study with all objects rejected)

    (dcmAllowDeleteStudyPermanently)"
    "
    .. _dcmAllowDeletePatient:
    .. _archiveDevice-dcmAllowDeletePatient:

    :ref:`Allow Delete Patient <archiveDevice-dcmAllowDeletePatient>`",string,"Allow permanent deletion of Patients. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NEVER (= Never allow delete patient permanently)

    ALWAYS (= Always allow delete patient permanently)

    WITHOUT_STUDIES (= Allow delete patient permanently only for patient without studies)

    (dcmAllowDeletePatient)"
    "
    .. _dcmPurgeStgCmtCompletedDelay:
    .. _archiveDevice-dcmPurgeStgCmtCompletedDelay:

    :ref:`Purge Storage Commitment Completed Delay <archiveDevice-dcmPurgeStgCmtCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which results of completed Storage Commitment requests are purged. If absent, there is no deletion.

    (dcmPurgeStgCmtCompletedDelay)"
    "
    .. _dcmPurgeStgCmtPollingInterval:
    .. _archiveDevice-dcmPurgeStgCmtPollingInterval:

    :ref:`Purge Storage Commitment Polling Interval <archiveDevice-dcmPurgeStgCmtPollingInterval>`",string,"Polling Interval for purging Storage Commitment Results in ISO-8601 duration format PnDTnHnMnS. If absent, there is no deletion

    (dcmPurgeStgCmtPollingInterval)"
    "
    .. _dcmDefaultCharacterSet:
    .. _archiveDevice-dcmDefaultCharacterSet:

    :ref:`Default Character Set <archiveDevice-dcmDefaultCharacterSet>`",string,"Value of Specific Character Set (0008,0005) added to Data Sets of C-STORE RQs and pending C-FIND RSPs without Specific Character Set (0008,0005) attribute received by any AE. May be overwritten by configured values for particular Archive Network AEs.

    (dcmDefaultCharacterSet)"
    "
    .. _dcmCharsetNameMapping:
    .. _archiveDevice-dcmCharsetNameMapping:

    :ref:`DICOM Character Set Name Mapping(s) <archiveDevice-dcmCharsetNameMapping>`",string,"Customize mapping of value of DICOM Specific Character Set (0008,0005) to named charset in format <value>=<charset name>. E.g.: ""ISO_IR 100=windows-1252"".

    (dcmCharsetNameMapping)"
    "
    .. _hl7CharsetNameMapping:
    .. _archiveDevice-hl7CharsetNameMapping:

    :ref:`HL7 Character Set Name Mapping(s) <archiveDevice-hl7CharsetNameMapping>`",string,"Add mapping of value of HL7 MSH-18 to named charset in format <value>=<charset name>. E.g.: ""Windows-1252=windows-1252"". Typically you will also have to specify the HL7 DICOM Character Set of the Archive HL7 Application to use for received HL7 messages with such Character Set.

    (hl7CharsetNameMapping)"
    "
    .. _dcmUPSWorklistLabel:
    .. _archiveDevice-dcmUPSWorklistLabel:

    :ref:`UPS Worklist Label <archiveDevice-dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) of created UPS by any Network AE, if the UPS Push SCU or UPS-RS User Agent does not provide a value for this attribute. If absent, the AE Title of the receiving AE will be used. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSEventSCU:
    .. _archiveDevice-dcmUPSEventSCU:

    :ref:`UPS Event SCU(s) <archiveDevice-dcmUPSEventSCU>`",string,"AE Title of UPS Event SOP Class SCU, to which UPS Event Reports are sent - independently if the subscription was created by the N-ACTION DIMSE service, or by a corresponding UPS RESTful service. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUPSEventSCU)"
    "
    .. _dcmUPSEventSCUKeepAlive:
    .. _archiveDevice-dcmUPSEventSCUKeepAlive:

    :ref:`UPS Event SCU Keep Alive <archiveDevice-dcmUPSEventSCUKeepAlive>`",integer,"Timeout in ms to keep associations to UPS Event SCUs alive. If absent, associations will not be reused for sending multiple UPS Event Reports to one UPS Event SCU. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUPSEventSCUKeepAlive)"
    "
    .. _dcmUPSEventWebSocketQueueSize:
    .. _archiveDevice-dcmUPSEventWebSocketQueueSize:

    :ref:`UPS Event Web Socket Queue Size(s) <archiveDevice-dcmUPSEventWebSocketQueueSize>`",string,"Indicates to queue UPS events to be sent to a particular Web Client identified by its Subscriber AET in case there is no open Web Socket connection to that client at the time of the event. Format: <aet>=<size>.

    (dcmUPSEventWebSocketQueueSize)"
    "
    .. _dcmRetrieveAET:
    .. _archiveDevice-dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) <archiveDevice-dcmRetrieveAET>`",string,"Specifies Retrieve AE Titles associated with received DICOM objects. If absent, the Called AE Title of the receiving AE will be used. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveAET)"
    "
    .. _dcmReturnRetrieveAET:
    .. _archiveDevice-dcmReturnRetrieveAET:

    :ref:`Return Retrieve AE Title(s) <archiveDevice-dcmReturnRetrieveAET>`",string,"Retrieve AE Title returned in C-FIND and QIDO responses. If absent, the Retrieve AET associated with the archived entity will be returned. May be overwritten by configured values for particular Archive Network AEs.

    (dcmReturnRetrieveAET)"
    "
    .. _dcmMultipleStoreAssociations:
    .. _archiveDevice-dcmMultipleStoreAssociations:

    :ref:`Multiple Store Associations(s) <archiveDevice-dcmMultipleStoreAssociations>`",string,"Number of Storage Associations used for retrieve of Composite Objects. C-STORE SCP specific numbers can be specified by prefix '<AETitle>:'. If absent, only one Association will be used. Examples : 2 or STORESCP:3 May be supplemented by configured Multiple Store Associations for particular Archive Network AEs.

    (dcmMultipleStoreAssociations)"
    "
    .. _dcmExternalRetrieveAEDestination:
    .. _archiveDevice-dcmExternalRetrieveAEDestination:

    :ref:`External Retrieve AE Destination <archiveDevice-dcmExternalRetrieveAEDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to external retrieve AE. May be overwritten by configured values for particular Archive Network AEs.

    (dcmExternalRetrieveAEDestination)"
    "
    .. _dcmXDSiImagingDocumentSourceAETitle:
    .. _archiveDevice-dcmXDSiImagingDocumentSourceAETitle:

    :ref:`XDS-I Imaging Document Source AE Title <archiveDevice-dcmXDSiImagingDocumentSourceAETitle>`",string,"AE Title of local Application Entity associated with XDS-I Imaging Document Source.

    (dcmXDSiImagingDocumentSourceAETitle)"
    "
    .. _dcmXDSiFallbackCMoveSCP:
    .. _archiveDevice-dcmXDSiFallbackCMoveSCP:

    :ref:`XDS-I Fallback C-MOVE SCP <archiveDevice-dcmXDSiFallbackCMoveSCP>`",string,"AE Title of external C-MOVE SCP to invoke C-MOVE RQs if the requested Entities are not managed by this XDS-I Imaging Document Source.

    (dcmXDSiFallbackCMoveSCP)"
    "
    .. _dcmXDSiFallbackCMoveSCPCallingAET:
    .. _archiveDevice-dcmXDSiFallbackCMoveSCPCallingAET:

    :ref:`XDS-I Fallback C-MOVE SCP Calling AET <archiveDevice-dcmXDSiFallbackCMoveSCPCallingAET>`",string,"Calling AE Title used in A-ASSOCIATE-RQ to configured XDSi Fallback C-MOVE SCP. If not specified, the configured XDS-I Imaging Document Source AE Title will be used.

    (dcmXDSiFallbackCMoveSCPCallingAET)"
    "
    .. _dcmXDSiFallbackCMoveSCPDestination:
    .. _archiveDevice-dcmXDSiFallbackCMoveSCPDestination:

    :ref:`XDS-I Fallback C-MOVE SCP Destination <archiveDevice-dcmXDSiFallbackCMoveSCPDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs invoked to configured XDSi Fallback C-MOVE SCP. If not specified, the configured XDS-I Imaging Document Source AE Title will be used.

    (dcmXDSiFallbackCMoveSCPDestination)"
    "
    .. _dcmQueueTasksFetchSize:
    .. _archiveDevice-dcmQueueTasksFetchSize:

    :ref:`Queue Tasks Fetch Size <archiveDevice-dcmQueueTasksFetchSize>`",integer,"Maximal number of Tasks rescheduled or deleted or canceled in one transaction.

    (dcmQueueTasksFetchSize)"
    "
    .. _dcmRemapRetrieveURL:
    .. _archiveDevice-dcmRemapRetrieveURL:

    :ref:`Remap Retrieve URL <archiveDevice-dcmRemapRetrieveURL>`",string,"Remap Retrieve URL used in QIDO-RS and WADO-RS Metadata responses. Optionally prefixed with ""[<http-client-host>]"". E.g.: ""[cache-proxy]http://cache-proxy:8080"". If absent or if the specified <http-client-host> does not match, scheme and server authority of the QIDO-RS or WADO-RS request URL are used.

    (dcmRemapRetrieveURL)"
    "
    .. _dcmProxyUpstreamURL:
    .. _archiveDevice-dcmProxyUpstreamURL:

    :ref:`Proxy Upstream URL <archiveDevice-dcmProxyUpstreamURL>`",string,"URL for the upstream endpoint that shall be proxied.

    (dcmProxyUpstreamURL)"
    "
    .. _dcmCopyMoveUpdatePolicy:
    .. _archiveDevice-dcmCopyMoveUpdatePolicy:

    :ref:`Copy Move Update Policy <archiveDevice-dcmCopyMoveUpdatePolicy>`",string,"Specifies update policy for attributes of the destination Study on Copy/Move of Instances from another Study. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    PRESERVE (= The attributes will be preserved. Nullify attributes in the new dataset which are not present in the original dataset. Any extra attributes will be nullified)

    SUPPLEMENT (= The attributes will be overwritten. Attributes not present in original dataset will be supplemented. Any extra attributes with not null values will be added)

    MERGE (= The attributes will be overwritten. Attribute values will be written from new dataset. Any attributes with not null values, shall not be overwritten by attributes with null values)

    OVERWRITE (= The attributes will be overwritten. Attribute values if null in new dataset, will be nullified in original dataset. Any attributes with not null values, shall be overwritten by attributes with null values)

    REPLACE (= The attributes will be completely overwritten)

    (dcmCopyMoveUpdatePolicy)"
    "
    .. _dcmLinkMWLEntryUpdatePolicy:
    .. _archiveDevice-dcmLinkMWLEntryUpdatePolicy:

    :ref:`Link MWL Entry Update Policy <archiveDevice-dcmLinkMWLEntryUpdatePolicy>`",string,"Specifies update policy for Study attributes on Link of Instances of another Study with a MWL Entry referring an existing Study. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    PRESERVE (= The attributes will be preserved. Nullify attributes in the new dataset which are not present in the original dataset. Any extra attributes will be nullified)

    SUPPLEMENT (= The attributes will be overwritten. Attributes not present in original dataset will be supplemented. Any extra attributes with not null values will be added)

    MERGE (= The attributes will be overwritten. Attribute values will be written from new dataset. Any attributes with not null values, shall not be overwritten by attributes with null values)

    OVERWRITE (= The attributes will be overwritten. Attribute values if null in new dataset, will be nullified in original dataset. Any attributes with not null values, shall be overwritten by attributes with null values)

    REPLACE (= The attributes will be completely overwritten)

    (dcmLinkMWLEntryUpdatePolicy)"
    "
    .. _dcmStorageVerificationPolicy:
    .. _archiveDevice-dcmStorageVerificationPolicy:

    :ref:`Storage Verification Policy <archiveDevice-dcmStorageVerificationPolicy>`",string,"Policy applied on storage verification of studies. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    DB_RECORD_EXISTS (= Only check for existence of DB records)

    OBJECT_EXISTS (= Check if object exists on Storage System)

    OBJECT_SIZE (= Check size of object on Storage System)

    OBJECT_FETCH (= Fetch object from Storage System)

    OBJECT_CHECKSUM (= Recalculate checksum of object on Storage System)

    S3_MD5SUM (= Check MD5 checksum of object on S3 Storage System)

    (dcmStorageVerificationPolicy)"
    "
    .. _dcmStorageVerificationUpdateLocationStatus:
    .. _archiveDevice-dcmStorageVerificationUpdateLocationStatus:

    :ref:`Storage Verification Update Location Status <archiveDevice-dcmStorageVerificationUpdateLocationStatus>`",boolean,"Indicates if the Status of the Location DB record shall be updated on Storage Verification accordingly. Not effective with Storage Verification Policy: DB_RECORD_EXISTS. False if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationUpdateLocationStatus)"
    "
    .. _dcmStorageVerificationStorageID:
    .. _archiveDevice-dcmStorageVerificationStorageID:

    :ref:`Storage Verification Storage IDs(s) <archiveDevice-dcmStorageVerificationStorageID>`",string,"Indicates that for successful Storage Verification the object must be stored on (one of) the specified Storage System. If absent, successful verification of the storage on any Storage System is sufficient. Not effective with Storage Validation Policy: DB_RECORD_EXISTS. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationStorageID)"
    "
    .. _dcmStorageVerificationAETitle:
    .. _archiveDevice-dcmStorageVerificationAETitle:

    :ref:`Storage Verification AE Title <archiveDevice-dcmStorageVerificationAETitle>`",string,"Archive AE Title used for scheduled Storage Verifications.

    (dcmStorageVerificationAETitle)"
    "
    .. _dcmStorageVerificationBatchID:
    .. _archiveDevice-dcmStorageVerificationBatchID:

    :ref:`Storage Verification Batch ID <archiveDevice-dcmStorageVerificationBatchID>`",string,"Batch ID of Storage Verification Tasks triggered by scheduler.

    (dcmStorageVerificationBatchID)"
    "
    .. _dcmStorageVerificationInitialDelay:
    .. _archiveDevice-dcmStorageVerificationInitialDelay:

    :ref:`Storage Verification Initial Delay <archiveDevice-dcmStorageVerificationInitialDelay>`",string,"Delay of first Storage Verification of a Series after it was received. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationInitialDelay)"
    "
    .. _dcmStorageVerificationPeriod:
    .. _archiveDevice-dcmStorageVerificationPeriod:

    :ref:`Storage Verification Period <archiveDevice-dcmStorageVerificationPeriod>`",string,"Period in which the storage of individual Series is verified. If absent, storage of individual Series are only verified once after configured Storage Verification Initial Delay.

    (dcmStorageVerificationPeriod)"
    "
    .. _dcmStorageVerificationMaxScheduled:
    .. _archiveDevice-dcmStorageVerificationMaxScheduled:

    :ref:`Maximal scheduled Storage Verifications <archiveDevice-dcmStorageVerificationMaxScheduled>`",integer,"Maximal number of scheduled Storage Verification tasks on this device. Shall be set > 0 to distribute tasks over nodes of a clustered archive.

    (dcmStorageVerificationMaxScheduled)"
    "
    .. _dcmStorageVerificationPollingInterval:
    .. _archiveDevice-dcmStorageVerificationPollingInterval:

    :ref:`Storage Verification Polling Interval <archiveDevice-dcmStorageVerificationPollingInterval>`",string,"Polling Interval for Series scheduled for Storage Verification in ISO-8601 duration format PnDTnHnMnS.

    (dcmStorageVerificationPollingInterval)"
    "
    .. _dcmStorageVerificationSchedule:
    .. _archiveDevice-dcmStorageVerificationSchedule:

    :ref:`Storage Verification Schedule(s) <archiveDevice-dcmStorageVerificationSchedule>`",string,"Limits Storage Verification to specified times in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday).

    (dcmStorageVerificationSchedule)"
    "
    .. _dcmStorageVerificationFetchSize:
    .. _archiveDevice-dcmStorageVerificationFetchSize:

    :ref:`Storage Verification Fetch Size <archiveDevice-dcmStorageVerificationFetchSize>`",integer,"Maximal number of Series scheduled for Storage Verification fetched by one query.

    (dcmStorageVerificationFetchSize)"
    "
    .. _dcmUpdateLocationStatusOnRetrieve:
    .. _archiveDevice-dcmUpdateLocationStatusOnRetrieve:

    :ref:`Update Location Status on Retrieve <archiveDevice-dcmUpdateLocationStatusOnRetrieve>`",boolean,"Indicates if the Status of the Location DB record shall be updated for objects failed to get fetched from storage on retrieve to MISSING_OBJECT or FAILED_TO_FETCH_OBJECT. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUpdateLocationStatusOnRetrieve)"
    "
    .. _dcmStorageVerificationOnRetrieve:
    .. _archiveDevice-dcmStorageVerificationOnRetrieve:

    :ref:`Storage Verification on Retrieve <archiveDevice-dcmStorageVerificationOnRetrieve>`",boolean,"Indicates if failures to fetch an object from Storage on retrieve shall trigger a Storage Verification of the whole Series. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationOnRetrieve)"
    "
    .. _dcmCompressionAETitle:
    .. _archiveDevice-dcmCompressionAETitle:

    :ref:`Compression AE Title <archiveDevice-dcmCompressionAETitle>`",string,"Archive AE Title used for delayed Compression.

    (dcmCompressionAETitle)"
    "
    .. _dcmCompressionPollingInterval:
    .. _archiveDevice-dcmCompressionPollingInterval:

    :ref:`Compression Polling Interval <archiveDevice-dcmCompressionPollingInterval>`",string,"Polling Interval for Series to be compressed in ISO-8601 duration format PnDTnHnMnS.

    (dcmCompressionPollingInterval)"
    "
    .. _dcmCompressionThreads:
    .. _archiveDevice-dcmCompressionThreads:

    :ref:`Compression Threads <archiveDevice-dcmCompressionThreads>`",integer,"Number of Threads used for Compression.

    (dcmCompressionThreads)"
    "
    .. _dcmCompressionSchedule:
    .. _archiveDevice-dcmCompressionSchedule:

    :ref:`Compression Schedule(s) <archiveDevice-dcmCompressionSchedule>`",string,"Limits compression to specified times in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmCompressionSchedule)"
    "
    .. _dcmCompressionFetchSize:
    .. _archiveDevice-dcmCompressionFetchSize:

    :ref:`Compression Fetch Size <archiveDevice-dcmCompressionFetchSize>`",integer,"Maximal number of Series fetched for compression by one query.

    (dcmCompressionFetchSize)"
    "
    .. _dcmChangeAccessControlIDPollingInterval:
    .. _archiveDevice-dcmChangeAccessControlIDPollingInterval:

    :ref:`Change Access Control ID Polling Interval <archiveDevice-dcmChangeAccessControlIDPollingInterval>`",string,"Polling Interval for Studies or Series to change its assigned Access Control ID according configured Change Access Control ID rules in ISO-8601 duration format PnDTnHnMnS.

    (dcmChangeAccessControlIDPollingInterval)"
    "
    .. _dcmDiffTaskProgressUpdateInterval:
    .. _archiveDevice-dcmDiffTaskProgressUpdateInterval:

    :ref:`Diff Task Progress Update Interval <archiveDevice-dcmDiffTaskProgressUpdateInterval>`",string,"Interval of updating Diff Tasks in process for progress monitoring; disabled if absent.

    (dcmDiffTaskProgressUpdateInterval)"
    "
    .. _dcmPatientVerificationPDQServiceID:
    .. _archiveDevice-dcmPatientVerificationPDQServiceID:

    :ref:`Patient Verification PDQ Service ID <archiveDevice-dcmPatientVerificationPDQServiceID>`",string,"ID of Patient Demographics Query Service used for Verification of Patient Demographic. If absent, no Patient Verification will be performed.

    (dcmPatientVerificationPDQServiceID)"
    "
    .. _dcmPatientVerificationPollingInterval:
    .. _archiveDevice-dcmPatientVerificationPollingInterval:

    :ref:`Patient Verification Polling Interval <archiveDevice-dcmPatientVerificationPollingInterval>`",string,"Patient Verification Polling Interval. If absent, no Patient Verification will be performed.

    (dcmPatientVerificationPollingInterval)"
    "
    .. _dcmPatientVerificationFetchSize:
    .. _archiveDevice-dcmPatientVerificationFetchSize:

    :ref:`Patient Verification Fetch Size <archiveDevice-dcmPatientVerificationFetchSize>`",integer,"Maximal number of Patients fetched for Patient Verification in one query.

    (dcmPatientVerificationFetchSize)"
    "
    .. _dcmPatientVerificationAdjustIssuerOfPatientID:
    .. _archiveDevice-dcmPatientVerificationAdjustIssuerOfPatientID:

    :ref:`Patient Verification Adjust Issuer of Patient ID <archiveDevice-dcmPatientVerificationAdjustIssuerOfPatientID>`",boolean,"Indicates if the Issuer Of Patient ID shall be adjusted to the value returned by the PDQ Service.

    (dcmPatientVerificationAdjustIssuerOfPatientID)"
    "
    .. _dcmPatientVerificationPeriod:
    .. _archiveDevice-dcmPatientVerificationPeriod:

    :ref:`Patient Verification Period <archiveDevice-dcmPatientVerificationPeriod>`",string,"Period in which Patient Demographic will be verified. If absent, Patient Verification will not be renewed for Patients verified in the past.

    (dcmPatientVerificationPeriod)"
    "
    .. _dcmPatientVerificationPeriodOnNotFound:
    .. _archiveDevice-dcmPatientVerificationPeriodOnNotFound:

    :ref:`Patient Verification Period Not Found <archiveDevice-dcmPatientVerificationPeriodOnNotFound>`",string,"Period in which Patient Demographic will be retried for Patients which were not found by the configured PDQ Service on last attempt. If absent, Patient Verification will not be retried for Patients not found in the past.

    (dcmPatientVerificationPeriodOnNotFound)"
    "
    .. _dcmPatientVerificationRetryInterval:
    .. _archiveDevice-dcmPatientVerificationRetryInterval:

    :ref:`Patient Verification Retry Interval <archiveDevice-dcmPatientVerificationRetryInterval>`",string,"Patient Verification Retry Interval in which failed attempts to verify Patient Demographics against the PDQ Service configured by Patient Verification PDQ Service ID will be retried until the maximal number of retries specified by Patient Verification Max Retries is reached. If absent, failed Patient Verification attempts will not be retried.

    (dcmPatientVerificationRetryInterval)"
    "
    .. _dcmPatientVerificationMaxRetries:
    .. _archiveDevice-dcmPatientVerificationMaxRetries:

    :ref:`Patient Verification Maximum Number of Retries <archiveDevice-dcmPatientVerificationMaxRetries>`",integer,"Maximum number of retries to verify Patient Demographics against the PDQ Service configured by dcmPatientVerificationPDQServiceID. Only effective if Patient Verification Retry Interval is specified. -1 = forever.

    (dcmPatientVerificationMaxRetries)"
    "
    .. _dcmPatientVerificationMaxStaleness:
    .. _archiveDevice-dcmPatientVerificationMaxStaleness:

    :ref:`Patient Verification Maximum Staleness <archiveDevice-dcmPatientVerificationMaxStaleness>`",string,"Indicates to renew the verification of Patient Demographics on receive of objects for a patient, if previous executed verification is older than specified interval. If absent, Patient Verification on receive of objects is disabled.

    (dcmPatientVerificationMaxStaleness)"
    "
    .. _dcmSupplementIssuerFetchSize:
    .. _archiveDevice-dcmSupplementIssuerFetchSize:

    :ref:`Supplement Issuer Fetch Size <archiveDevice-dcmSupplementIssuerFetchSize>`",integer,"Limit result set of DB query for matching Patients by RESTful service for supplementing Issuer of Patient ID.

    (dcmSupplementIssuerFetchSize)"
    "
    .. _dcmUpdateCharsetFetchSize:
    .. _archiveDevice-dcmUpdateCharsetFetchSize:

    :ref:`Update Charset Fetch Size <archiveDevice-dcmUpdateCharsetFetchSize>`",integer,"Limit result set of DB query for matching Patients by RESTful service to update the character set of Patient Attributes in DB BLOB fields.

    (dcmUpdateCharsetFetchSize)"
    "
    .. _dcmInExpressionCountLimit:
    .. _archiveDevice-dcmInExpressionCountLimit:

    :ref:`IN Expression Count Limit <archiveDevice-dcmInExpressionCountLimit>`",integer,"Limit the number of elements in the IN predicate used for matching SOP Instance UIDs in SQL queries (0 - only limited by DB specific constraint).

    (dcmInExpressionCountLimit)"
    "
    .. _hl7ADTSendingApplication:
    .. _archiveDevice-hl7ADTSendingApplication:

    :ref:`HL7 ADT Sending Application <archiveDevice-hl7ADTSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 ADT messages to synchronize external systems about performed Patient Information updates. If absent, synchronization of external systems by HL7 ADT messages is disabled.

    (hl7ADTSendingApplication)"
    "
    .. _hl7ADTReceivingApplication:
    .. _archiveDevice-hl7ADTReceivingApplication:

    :ref:`HL7 ADT Receiving Application(s) <archiveDevice-hl7ADTReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 ADT messages to synchronize external systems about performed Patient Information updates. If absent, synchronization of external systems by HL7 ADT messages is disabled.

    (hl7ADTReceivingApplication)"
    "
    .. _hl7PSUSendingApplication:
    .. _archiveDevice-hl7PSUSendingApplication:

    :ref:`HL7 Procedure Status Update Sending Application <archiveDevice-hl7PSUSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 Procedure Status Update. HL7 Procedure Status Update disabled, if absent. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUSendingApplication)"
    "
    .. _hl7PSUReceivingApplication:
    .. _archiveDevice-hl7PSUReceivingApplication:

    :ref:`HL7 Procedure Status Update Receiving Application(s) <archiveDevice-hl7PSUReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 Procedure Status Update. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUReceivingApplication)"
    "
    .. _hl7PSUTaskPollingInterval:
    .. _archiveDevice-hl7PSUTaskPollingInterval:

    :ref:`HL7 Procedure Status Update Task Polling Interval <archiveDevice-hl7PSUTaskPollingInterval>`",string,"Polling Interval for HL7 Procedure Status Update Tasks in ISO-8601 duration format PnDTnHnMnS. Disabled, if absent.

    (hl7PSUTaskPollingInterval)"
    "
    .. _hl7PSUTaskFetchSize:
    .. _archiveDevice-hl7PSUTaskFetchSize:

    :ref:`HL7 Procedure Status Update Tasks Fetch Size <archiveDevice-hl7PSUTaskFetchSize>`",integer,"Maximal number of HL7 Procedure Status Update Tasks fetched in one query.

    (hl7PSUTaskFetchSize)"
    "
    .. _hl7PSUAction:
    .. _archiveDevice-hl7PSUAction:

    :ref:`HL7 Procedure Status Update Action(s) <archiveDevice-hl7PSUAction>`",string,"Specifies HL7 Procedure Status Update action. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    SEND_NOTIFICATION (= Send HL7 Procedure Status Update Notification message to configured HL7 Procedure Status Update Receiving Applications)

    UPDATE_MWL_STATUS (= Set Scheduled Procedure Step Status of MWL Items associated to STUDY to COMPLETED)

    (hl7PSUAction)"
    "
    .. _hl7PSUTrigger:
    .. _archiveDevice-hl7PSUTrigger:

    :ref:`HL7 Procedure Status Update Trigger(s) <archiveDevice-hl7PSUTrigger>`",string,"Specifies trigger events to send a HL7 Procedure Status Update notification to HL7 Receivers configured by HL7 Procedure Status Update Receiving Application. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    STUDY_RECEIVED (= Send notification on receive of studies)

    MPPS_RECEIVED (= Send notification on receive of MPPS)

    REJECTION_NOTE_RECEIVED (= Send notification on receive of IOCM KO)

    FIRST_OBJECT_OF_STUDY_RECEIVED (= Send notification on receive of first object of study)

    (hl7PSUTrigger)"
    "
    .. _hl7PSUDelay:
    .. _archiveDevice-hl7PSUDelay:

    :ref:`HL7 Procedure Status Update Delay <archiveDevice-hl7PSUDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUDelay)"
    "
    .. _hl7PSUStudyTemplateURI:
    .. _archiveDevice-hl7PSUStudyTemplateURI:

    :ref:`HL7 Procedure Status Update Study Template URI <archiveDevice-hl7PSUStudyTemplateURI>`",string,"URL of XSL style sheet to create HL7v2 message to notify configured HL7 receivers about changes of the Status of requested Procedures triggered by received Study. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUStudyTemplateURI)"
    "
    .. _hl7PSUTimeout:
    .. _archiveDevice-hl7PSUTimeout:

    :ref:`HL7 Procedure Status Update Timeout <archiveDevice-hl7PSUTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMnS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUTimeout)"
    "
    .. _hl7PSUOnTimeout:
    .. _archiveDevice-hl7PSUOnTimeout:

    :ref:`HL7 Procedure Status Update On Timeout <archiveDevice-hl7PSUOnTimeout>`",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUOnTimeout)"
    "
    .. _hl7PSUMppsTemplateURI:
    .. _archiveDevice-hl7PSUMppsTemplateURI:

    :ref:`HL7 Procedure Status Update MPPS Template URI <archiveDevice-hl7PSUMppsTemplateURI>`",string,"URL of XSL style sheet to create HL7v2 message to notify configured HL7 receivers about changes of the Status of requested Procedures triggered by MPPS. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUMppsTemplateURI)"
    "
    .. _hl7PSUCondition:
    .. _archiveDevice-hl7PSUCondition:

    :ref:`HL7 Procedure Status Update Conditions(s) <archiveDevice-hl7PSUCondition>`",string,"Restrict notification of configured HL7 Procedure Status Update Receiving Applications about Procedure Status Update by conditions on attributes of received composite object in format {key}[!]={value}. Refer `applicability, format and some examples <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUCondition)"
    "
    .. _hl7PSUForRequestedProcedure:
    .. _archiveDevice-hl7PSUForRequestedProcedure:

    :ref:`HL7 Procedure Status Update for Requested Procedure <archiveDevice-hl7PSUForRequestedProcedure>`",boolean,"Restrict notification of configured HL7 Procedure Status Update Receiving Applications about Procedure Status Update to existence of Scheduled Procedure Steps of a Requested Procedure (MWL Items in the DB) with matching Study Instance UID. May be overwritten by configured value for particular Archive Network AEs.

    (hl7PSUForRequestedProcedure)"
    "
    .. _hl7PSUTemplateParam:
    .. _archiveDevice-hl7PSUTemplateParam:

    :ref:`HL7 Procedure Status Update Template Parameters(s) <archiveDevice-hl7PSUTemplateParam>`",string,"XSLT parameters in format {attributeID}={value} passed to style sheet specified by HL7 Procedure Status Update MPPS Template URI or HL7 Procedure Status Update Study Template URI. {attributeID} inside of {value} will be replaced by the value of that attribute in the original dataset. E.g.: 'RequestedProcedureID={StudyInstanceUID}' or 'AccessionNumber={0020000D}'. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUTemplateParam)"
    "
    .. _hl7PSUMessageType:
    .. _archiveDevice-hl7PSUMessageType:

    :ref:`HL7 Procedure Status Update Message Type <archiveDevice-hl7PSUMessageType>`",string,"Message Type of HL7 Procedure Status Update message. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    OMG_O19 (= Eyecare Order Message)

    ORU_R01 (= Unsolicited Observation Message)

    OMI_O23 (= Clinical Order Message)

    (hl7PSUMessageType)"
    "
    .. _hl7PSUPIDPV1:
    .. _archiveDevice-hl7PSUPIDPV1:

    :ref:`HL7 Procedure Status Update PID PV1 <archiveDevice-hl7PSUPIDPV1>`",boolean,"Indicates to include a Patient Identification (PID) and a Patient Visit (PV1) segment in the HL7 Procedure Status Update message. Implicitly set, if HL7 Procedure Status Message Type = ORU_R01. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUPIDPV1)"
    "
    .. _hl7PSUMWLMatchingKey:
    .. _archiveDevice-hl7PSUMWLMatchingKey:

    :ref:`HL7 Procedure Status Update MWL Matching Key <archiveDevice-hl7PSUMWLMatchingKey>`",string,"Specifies attribute of received object to lookup MWL Item whose status is to be updated to COMPLETED. Only applicable is 'HL7 Procedure Status Update MWL' is configured as or implicitly set to true. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    AccessionNumber (= Use Accession Number (0008,0050) for matching MWL)

    StudyInstanceUID (= Use Study Instance UID (0020,000D) for matching MWL)

    (hl7PSUMWLMatchingKey)"
    "
    .. _hl7TrackChangedPatientID:
    .. _archiveDevice-hl7TrackChangedPatientID:

    :ref:`HL7 Track Changed Patient ID <archiveDevice-hl7TrackChangedPatientID>`",boolean,"Enable to keep track of the prior Patient ID on a change of the Patient ID by HL7 ADT^A47 or by the RESTful Patient Update Service.

    (hl7TrackChangedPatientID)"
    "
    .. _hl7UseNullValue:
    .. _archiveDevice-hl7UseNullValue:

    :ref:`Use HL7 Null Value <archiveDevice-hl7UseNullValue>`",boolean,"Specifies if HL7 v2 null values (specified in segment field as `|""""|`) are used in sent HL7 messages for not present or empty entity attributes. Required to unset entity attributes at the remote HL7 Application. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7UseNullValue)"
    "
    .. _hl7VeterinaryUsePatientName:
    .. _archiveDevice-hl7VeterinaryUsePatientName:

    :ref:`HL7 Veterinary use Patient Name <archiveDevice-hl7VeterinaryUsePatientName>`",boolean,"Indicates to force veterinary use of Patient Names on mapping HL7 PID fields to DICOM attributes: only use the first two components of PID.5 as DICOM Patient Name; if PID.5 only contains one component, use that value as given name, and the first component of PID.9 as family name of the DICOM Patient Name. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7VeterinaryUsePatientName)"
    "
    .. _hl7PrimaryAssigningAuthorityOfPatientID:
    .. _archiveDevice-hl7PrimaryAssigningAuthorityOfPatientID:

    :ref:`HL7 Primary Assigning Authority of Patient ID <archiveDevice-hl7PrimaryAssigningAuthorityOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search primary qualified patient identifier in the list of identifiers in PID-3 / MRG.1. This qualified patient identifier shall be used on the root dataset. If absent, by default the first patient identifier pair in PID-3 / MRG.1 shall be used as primary patient identifier on root dataset. If none of the qualified patient identifiers in the list match with the configured issuer, archive server log shall contain a log INFO message and by default the first qualified patient identifier in PID-3 / MRG.1 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}]. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7PrimaryAssigningAuthorityOfPatientID)"
    "
    .. _hl7OtherPatientIDs:
    .. _archiveDevice-hl7OtherPatientIDs:

    :ref:`HL7 Other Patient IDs <archiveDevice-hl7OtherPatientIDs>`",string,"Specifies inclusion policy for patient identifiers in PID-3 / MRG-1 of HL7 message in Other Patient IDs Sequence (0010,1002). May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ALL (= Include all patient identifiers in PID.3 / MRG.1, including patient identifier on root dataset in Other Patient IDs Sequence (0010,1002))

    NONE (= Include no patient identifiers from PID.3 / MRG.1 in Other Patient IDs Sequence (0010,1002))

    OTHER (= Include all patient identifiers in PID.3 / MRG.1, except patient identifier on root dataset in Other Patient IDs Sequence (0010,1002))

    (hl7OtherPatientIDs)"
    "
    .. _hl7OrderMissingStudyIUIDPolicy:
    .. _archiveDevice-hl7OrderMissingStudyIUIDPolicy:

    :ref:`HL7 Order Missing Study Instance UID Policy <archiveDevice-hl7OrderMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Order messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    REJECT (= Reject HL7 Order Messages with missing Study Instance UID in ZDS.1 / IPC.3)

    GENERATE (= Generate random Study Instance UID if missing in HL7 Order Messages in ZDS.1 / IPC.3)

    ACCESSION_BASED (= Generate Study Instance UID based on Accession Number present in OBR.18 / IPC.1 if Study Instance UID missing in HL7 Order Messages in ZDS.1 / IPC.3)

    (hl7OrderMissingStudyIUIDPolicy)"
    "
    .. _hl7OrderMissingAdmissionIDPolicy:
    .. _archiveDevice-hl7OrderMissingAdmissionIDPolicy:

    :ref:`HL7 Order Missing Admission ID Policy <archiveDevice-hl7OrderMissingAdmissionIDPolicy>`",string,"Specifies policy on incoming HL7 Order messages without a value for PID-18 Patient Account Number nor field PV1-19 Visit Number. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ACCEPT (= Accept HL7 Order Messages with missing Admission ID in PV1.19 / PID.18)

    REJECT (= Reject HL7 Order Messages with missing Admission ID in PV1.19 / PID.18)

    ACCESSION_AS_ADMISSION (= Use Accession Number present in OBR.18 / IPC.1 as Admission ID if it is missing in HL7 Order Message in PV1.19 / PID.18)

    (hl7OrderMissingAdmissionIDPolicy)"
    "
    .. _hl7ImportReportMissingStudyIUIDPolicy:
    .. _archiveDevice-hl7ImportReportMissingStudyIUIDPolicy:

    :ref:`HL7 Import Report Missing Study Instance UID Policy <archiveDevice-hl7ImportReportMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Import Report (ORU) messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    REJECT (= Reject HL7 ORU^R01 message with missing Study Instance UID in OBX.5 for OBX segment with OBX.3 as 'Study Instance UID' / 'DICOM Study')

    GENERATE (= Generate random Study Instance UID if it is missing in HL7 ORU^R01 Message in OBX.5 for OBX segment with OBX.3 as 'Study Instance UID' / 'DICOM Study')

    ACCESSION_BASED (= Generate Study Instance UID based on Accession Number present in OBR.18 if Study Instance UID missing in HL7 ORU^R01 Messages in OBX.5 for OBX segment with OBX.3 as 'Study Instance UID' / 'DICOM Study')

    (hl7ImportReportMissingStudyIUIDPolicy)"
    "
    .. _hl7ImportReportMissingAdmissionIDPolicy:
    .. _archiveDevice-hl7ImportReportMissingAdmissionIDPolicy:

    :ref:`HL7 Import Report Missing Admission ID Policy <archiveDevice-hl7ImportReportMissingAdmissionIDPolicy>`",string,"Specifies policy on incoming HL7 ImportReport (ORU) messages without a value for PID-18 Patient Account Number nor field PV1-19 Visit Number. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ACCEPT (= Accept HL7 ORU^R01 Messages with missing Admission ID in PV1.19 / PID.18)

    REJECT (= Reject HL7 ORU^R01 Messages with missing Admission ID in PV1.19 / PID.18)

    ACCESSION_AS_ADMISSION (= Use Accession Number present in OBR.18 as Admission ID if it is missing in HL7 ORU^R01 Message in PV1.19 / PID.18)

    (hl7ImportReportMissingAdmissionIDPolicy)"
    "
    .. _hl7ImportReportMissingStudyIUIDCFindSCP:
    .. _archiveDevice-hl7ImportReportMissingStudyIUIDCFindSCP:

    :ref:`HL7 Import Report Missing Study Instance UID C-FIND SCP <archiveDevice-hl7ImportReportMissingStudyIUIDCFindSCP>`",string,"AE Title of external C-FIND SCP to query for missing Study Instance UID in incoming HL7 Import Report (ORU) messages by given Accession Number. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ImportReportMissingStudyIUIDCFindSCP)"
    "
    .. _hl7ImportReportAdjustIUID:
    .. _archiveDevice-hl7ImportReportAdjustIUID:

    :ref:`HL7 Import Report Adjust Instance UID <archiveDevice-hl7ImportReportAdjustIUID>`",string,"Specifies adjustment of Series and SOP Instances UIDs returned by XSLT on incoming HL7 Import Report (ORU) messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    NONE (= No adjustment done to Study / Series / SOP IUIDs)

    APPEND_HASH_OF_STUDY_INSTANCE_UID (= Hash of Study Instance UID appended as suffix to Study / Series / SOP IUIDs)

    (hl7ImportReportAdjustIUID)"
    "
    .. _hl7ReferredMergedPatientPolicy:
    .. _archiveDevice-hl7ReferredMergedPatientPolicy:

    :ref:`HL7 Referred Merged Patient Policy <archiveDevice-hl7ReferredMergedPatientPolicy>`",string,"Specifies policy on incoming HL7 messages referring an already merged Patient. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    REJECT (= Reject any incoming HL7 messages referring an already merged Patient)

    IGNORE (= Ignore any incoming HL7 messages referring an already merged Patient)

    IGNORE_DUPLICATE_MERGE (= Ignore only duplicate incoming HL7 Patient Merge (ADT^A40) messages referring an already merged Patient. Reject any other incoming HL7 messages referring an already merged Patient.)

    ACCEPT_INVERSE_MERGE (= Accept any incoming inverse HL7 Patient Merge (ADT^A40) messages referring an already merged Patient, optionally allowing inverse merging of patient records if clients send duplicated ADT^A40 patient merge messages repeatedly, just reversing the patient identifier values in PID / MRG segments.)

    (hl7ReferredMergedPatientPolicy)"
    "
    .. _hl7DicomCharacterSet:
    .. _archiveDevice-hl7DicomCharacterSet:

    :ref:`HL7 Dicom Character Set <archiveDevice-hl7DicomCharacterSet>`",string,"Indicates to use specified Value of Specific Character Set (0008,0005) in Data Sets transcoded from received HL7 messages. Use Value corresponding to Character Set of the HL7 message specified by MSH-18 if absent.

    (hl7DicomCharacterSet)"
    "
    .. _dcmRejectionNoteStorageAET:
    .. _archiveDevice-dcmRejectionNoteStorageAET:

    :ref:`Rejection Note Storage AE title <archiveDevice-dcmRejectionNoteStorageAET>`",string,"Title of Archive Application Entity, of which first configured Object Storage will be used for storing Rejection Notes generated either by IOCM-RS services or by Delete Expired Studies Scheduler. If absent, for IOCM services the Object Storage configured for Archive AE referred in the IOCM-RS request will be used, or for Delete Expired Studies Scheduler the Object Storage configured for Reject Expired Studies AE will be used.

    (dcmRejectionNoteStorageAET)"
    "
    .. _dcmUIConfigurationDeviceName:
    .. _archiveDevice-dcmUIConfigurationDeviceName:

    :ref:`UI Configuration Device Name <archiveDevice-dcmUIConfigurationDeviceName>`",string,"Specifies the device name containing the Archive UI Configuration.

    (dcmUIConfigurationDeviceName)"
    "
    .. _dcmCSVUploadChunkSize:
    .. _archiveDevice-dcmCSVUploadChunkSize:

    :ref:`CSV Upload Chunk Size <archiveDevice-dcmCSVUploadChunkSize>`",integer,"Number of CSV file upload tasks to be processed in one chunk.

    (dcmCSVUploadChunkSize)"
    "
    .. _dcmValidateUID:
    .. _archiveDevice-dcmValidateUID:

    :ref:`Validate UID <archiveDevice-dcmValidateUID>`",boolean,"Indicates if UIDs shall be validated or not.

    (dcmValidateUID)"
    "
    .. _dcmRelationalQueryNegotiationLenient:
    .. _archiveDevice-dcmRelationalQueryNegotiationLenient:

    :ref:`Relational Query Negotiation Lenient <archiveDevice-dcmRelationalQueryNegotiationLenient>`",boolean,"Indicates to accept C-FIND RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRelationalQueryNegotiationLenient)"
    "
    .. _dcmRelationalRetrieveNegotiationLenient:
    .. _archiveDevice-dcmRelationalRetrieveNegotiationLenient:

    :ref:`Relational Retrieve Negotiation Lenient <archiveDevice-dcmRelationalRetrieveNegotiationLenient>`",boolean,"Indicates to accept C-MOVE and C-GET RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRelationalRetrieveNegotiationLenient)"
    "
    .. _dcmRestrictRetrieveSilently:
    .. _archiveDevice-dcmRestrictRetrieveSilently:

    :ref:`Restrict Retrieve Silently <archiveDevice-dcmRestrictRetrieveSilently>`",boolean,"Indicates if the set of requested objects to retrieve shall be silently (=without counting not transferred object as failures) restricted according the Transfer Capabilities of the Retrieve Destination. Otherwise the number of requested objects for which no Transfer Capability is configured for the Retrieve Destination and therefore are not retrieved is counted as failures. Only effective, if the Retrieve Destination has configured at least one Transfer Capability with SCP role. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRestrictRetrieveSilently)"
    "
    .. _dcmSchedulerMinStartDelay:
    .. _archiveDevice-dcmSchedulerMinStartDelay:

    :ref:`Scheduler Minimum Start Delay <archiveDevice-dcmSchedulerMinStartDelay>`",integer,"Minimal delay in s to start schedulers on system start up.

    (dcmSchedulerMinStartDelay)"
    "
    .. _dcmRejectConflictingPatientAttribute:
    .. _archiveDevice-dcmRejectConflictingPatientAttribute:

    :ref:`Reject Conflicting Patient Attribute(s) <archiveDevice-dcmRejectConflictingPatientAttribute>`",string,"DICOM Tag of Patient Attribute which have to match in received objects with the value in previous received objects with equal Patient ID to be accepted. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRejectConflictingPatientAttribute)"
    "
    .. _dcmStowRetiredTransferSyntax:
    .. _archiveDevice-dcmStowRetiredTransferSyntax:

    :ref:`STOW Retired Transfer Syntax <archiveDevice-dcmStowRetiredTransferSyntax>`",boolean,"Store received JPEG Full Progression, Non-Hierarchical JPEG images in DICOM images with corresponding (retired) Transfer Syntax UID 1.2.840.10008.1.2.4.55. Otherwise set 1.2.840.10008.1.2.4.50 (= JPEG Baseline) or 1.2.840.10008.1.2.4.51 (= JPEG Extended) as Transfer Syntax UID of the stored DICOM image, without transcoding to JPEG Baseline or JPEG Extended, but including the JPEG image as received. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowRetiredTransferSyntax)"
    "
    .. _dcmStowExcludeAPPMarkers:
    .. _archiveDevice-dcmStowExcludeAPPMarkers:

    :ref:`STOW Exclude Application Markers <archiveDevice-dcmStowExcludeAPPMarkers>`",boolean,"Indicates if APP markers in JPEG images received in STOW-RS Metadata and Bulkdata requests shall be excluded from the JPEG bit streams encapsulated in created DICOM instances. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowExcludeAPPMarkers)"
    "
    .. _dcmStowQuicktime2MP4:
    .. _archiveDevice-dcmStowQuicktime2MP4:

    :ref:`STOW Quicktime to MP4 <archiveDevice-dcmStowQuicktime2MP4>`",boolean,"Indicates if QuickTime containers received in STOW-RS Metadata and Bulkdata requests shall be converted to MP4 containers encapsulated in created DICOM instances. The conversion requires that ffmpeg is installed and the ffmpeg CLI utility is available in the PATH. Otherwise Quicktime containers will get encapsulated in the stored DICOM object verbatim, with a declared DICOM MPEG-4 Transfer Syntax which reflects the encoding of the video stream in the container, but contradicts the actual container format. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowQuicktime2MP4)"
    "
    .. _dcmStowMaxFragmentLength:
    .. _archiveDevice-dcmStowMaxFragmentLength:

    :ref:`STOW Maximum Fragment Length <archiveDevice-dcmStowMaxFragmentLength>`",integer,"Maximum length of data fragments of encapsulated JPEG/MPEG stream in stored DICOM object. If the received JPEG/MPEG stream exceeds that value, it will be split into several fragments, using a Fragmentable Encapsulated Transfer Syntax. Valid range: 1024..4294967294. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowMaxFragmentLength)"
    "
    .. _dcmChangeRequesterAET:
    .. _archiveDevice-dcmChangeRequesterAET:

    :ref:`Change Requester AET <archiveDevice-dcmChangeRequesterAET>`",string,"Indicates change requester AET in rejections triggered by archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmChangeRequesterAET)"
    "
    .. _dcmFilterByIssuerOfPatientID:
    .. _archiveDevice-dcmFilterByIssuerOfPatientID:

    :ref:`Filter by Issuer of Patient ID <archiveDevice-dcmFilterByIssuerOfPatientID>`",boolean,"Filter by Issuer of Patient ID even if no matching key for Patient ID is specified. May be overwritten by configured value for particular Archive Network AEs.

    (dcmFilterByIssuerOfPatientID)"
    "
    .. _dcmMatchSOPClassOnInstanceLevel:
    .. _archiveDevice-dcmMatchSOPClassOnInstanceLevel:

    :ref:`Match SOP Class on Instance level <archiveDevice-dcmMatchSOPClassOnInstanceLevel>`",boolean,"Indicates to consider the SOP Class UID on Instance level for calculation of matches with SOP Classes in Study (0008,0062); otherwise rely on stored SOP Class UID on Series level, which may result in missing matches if one Series includes Instances of different SOP Classes. May be overwritten by configured value for particular Archive Network AEs.

    (dcmMatchSOPClassOnInstanceLevel)"
    "
    .. _dcmKeyValueRetentionPollingInterval:
    .. _archiveDevice-dcmKeyValueRetentionPollingInterval:

    :ref:`Key Value Retention Polling Interval <archiveDevice-dcmKeyValueRetentionPollingInterval>`",string,"Polling Interval for Key Value pairs which retention period expired in ISO-8601 duration format PnDTnHnMnS. If absent, Key Value pairs will not get deleted automatically.

    (dcmKeyValueRetentionPollingInterval)"
    "
    .. _dcmKeyValueRetentionFetchSize:
    .. _archiveDevice-dcmKeyValueRetentionFetchSize:

    :ref:`Key Value Retention Fetch Size <archiveDevice-dcmKeyValueRetentionFetchSize>`",integer,"Limit result set of DB query for Key Value pairs which retention period expired; 100 if absent

    (dcmKeyValueRetentionFetchSize)"
    "
    .. _dcmKeyValueRetentionPeriod:
    .. _archiveDevice-dcmKeyValueRetentionPeriod:

    :ref:`Key Value Retention Period <archiveDevice-dcmKeyValueRetentionPeriod>`",string,"Retention period in ISO-8601 duration format PnDTnHnMn.nS of stored Key Value pairs. If absent, Key Value pairs will not get deleted automatically.

    (dcmKeyValueRetentionPeriod)"
    "
    .. _dcmUPSUpdateWithoutTransactionUID:
    .. _archiveDevice-dcmUPSUpdateWithoutTransactionUID:

    :ref:`UPS Update Without Transaction UID <archiveDevice-dcmUPSUpdateWithoutTransactionUID>`",boolean,"Indicates to permit an UPS Pull SCU or UPS-RS Web client to update or change the state of an UPS workitem in state IN PROCESS without specifying a Transaction UID. May be overwritten by configured value for particular Archive Network AEs.

    (dcmUPSUpdateWithoutTransactionUID)"
    "
    .. _dcmUPS2MWLCFindSCP:
    .. _archiveDevice-dcmUPS2MWLCFindSCP:

    :ref:`UPS 2 MWL C-Find SCP <archiveDevice-dcmUPS2MWLCFindSCP>`",boolean,"Indicates to feed Modality Worklist C-FIND SCP service from managed list of Unified Procedure Step (UPS) instances mapped to MWL items. May be overwritten by configured value for particular Archive Network AEs.

    (dcmUPS2MWLCFindSCP)"
    "
    .. _dcmUPS2MWLScheduledStationNameCode:
    .. _archiveDevice-dcmUPS2MWLScheduledStationNameCode:

    :ref:`UPS 2 MWL Scheduled Station Name Code(s) <archiveDevice-dcmUPS2MWLScheduledStationNameCode>`",string,"Defines list of Station Name Codes in format (CV, CSD, ""CM"") used to map Scheduled Station AE Titles (0040,0001) in MWL C-FIND RQ/RSPs to Station Name Code Sequence (0040,4025) items of Unified Procedure Step (UPS) instances.

    (dcmUPS2MWLScheduledStationNameCode)"
    "
    .. _dcmUPS2MWLScheduledStationNameCodeValueAsAET:
    .. _archiveDevice-dcmUPS2MWLScheduledStationNameCodeValueAsAET:

    :ref:`UPS 2 MWL Scheduled Station Name Code Value as AE Title <archiveDevice-dcmUPS2MWLScheduledStationNameCodeValueAsAET>`",boolean,"Indicates to map Code Value (0008,0101) - instead Code Meaning (0008,0104) - of Scheduled Station Name Code Sequence (0040,4025) items of Unified Procedure Step (UPS) instances to Scheduled Station AE Titles (0040,0001) of MWL C-FIND RQ/RSPs.

    (dcmUPS2MWLScheduledStationNameCodeValueAsAET)"
    "
    .. _dcmQStarVerificationStorageID:
    .. _archiveDevice-dcmQStarVerificationStorageID:

    :ref:`QStar Verification Storage ID <archiveDevice-dcmQStarVerificationStorageID>`",string,"ID of QStar Tape File System to which objects were stored which Access State shall be verified. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationStorageID)"
    "
    .. _dcmQStarVerificationPollingInterval:
    .. _archiveDevice-dcmQStarVerificationPollingInterval:

    :ref:`QStar Verification Polling Interval <archiveDevice-dcmQStarVerificationPollingInterval>`",string,"Polling Interval for Verification of Access State of objects stored on QStar Tape File System in ISO-8601 duration format PnDTnHnMnS. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationPollingInterval)"
    "
    .. _dcmQStarVerificationFetchSize:
    .. _archiveDevice-dcmQStarVerificationFetchSize:

    :ref:`QStar Verification Fetch Size <archiveDevice-dcmQStarVerificationFetchSize>`",integer,"Limit result set of DB query for Verification of Access State of objects stored on QStar Tape File System; 100 if absent.

    (dcmQStarVerificationFetchSize)"
    "
    .. _dcmQStarVerificationDelay:
    .. _archiveDevice-dcmQStarVerificationDelay:

    :ref:`QStar Verification Delay <archiveDevice-dcmQStarVerificationDelay>`",string,"Delay for Verification of Access State after objects stored on QStar Tape File System in ISO-8601 duration format PnDTnHnMnS. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationDelay)"
    "
    .. _dcmQStarVerificationURL:
    .. _archiveDevice-dcmQStarVerificationURL:

    :ref:`QStar Verification URL <archiveDevice-dcmQStarVerificationURL>`",string,"URL of QStar Archive Storage Manager WEB Services - including username and password (http://username:password@qstar.host:port/) - invoked for Verification of Access State after objects stored on QStar Tape File System. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationURL)"
    "
    .. _dcmQStarVerificationMockAccessState:
    .. _archiveDevice-dcmQStarVerificationMockAccessState:

    :ref:`QStar Verification Mock Access State <archiveDevice-dcmQStarVerificationMockAccessState>`",integer,"Indicates to mock invoke of QStar Archive Storage Manager (ASM) WEB Services by return of specified Access State for testing.

    Enumerated values:

    0 (= ACCESS_STATE_NONE)

    1 (= ACCESS_STATE_EMPTY)

    2 (= ACCESS_STATE_UNSTABLE)

    3 (= ACCESS_STATE_STABLE)

    4 (= ACCESS_STATE_OUT_OF_CACHE)

    5 (= ACCESS_STATE_OFFLINE)

    -1 (= simulate error response)

    (dcmQStarVerificationMockAccessState)"
    "
    .. _dcmTrustedPatientIDPattern:
    .. _archiveDevice-dcmTrustedPatientIDPattern:

    :ref:`Trusted Patient ID Pattern(s) <archiveDevice-dcmTrustedPatientIDPattern>`",string,"Regular Expression identifying trusted Patient IDs in HL7 v2 CX format: {Patient ID}^^^{Issuer of Patient ID}&{Universal Entity ID}&{Universal Entity ID Type} in received DICOM objects and HL7 messages. Only Patient IDs matching one of the specified patterns or Patient IDs qualified by an Assigning Authority matching one of the configured 'Trusted Issuers of Patient IDs' will be used for identifying the Patient. If neither this attribute nor any 'Trusted Issuers of Patient ID' is configured, all Patient IDs in received DICOM Objects and HL7 messages will be used for identifying the Patient.

    (dcmTrustedPatientIDPattern)"
    "
    .. _dcmTrustedIssuerOfPatientID:
    .. _archiveDevice-dcmTrustedIssuerOfPatientID:

    :ref:`Trusted Issuer of Patient ID(s) <archiveDevice-dcmTrustedIssuerOfPatientID>`",string,"Trusted Assigning Authority of Patient IDs in received DICOM objects and HL7 messages. Only Patient IDs qualified by an Assigning Authority matching one of the specified values or Patient IDs matching one of the configured 'Trusted Patient ID Patterns' will be used for identifying the Patient. If neither this attribute nor dcmTrustedPatientIDPattern is configured, all Patient IDs in received DICOM Objects and HL7 messages will be used for identifying the Patient. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmTrustedIssuerOfPatientID)"
    "
    .. _fhirPreferredAssigningAuthorityOfPatientID:
    .. _archiveDevice-fhirPreferredAssigningAuthorityOfPatientID:

    :ref:`FHIR Preferred Assigning Authority of Patient ID(s) <archiveDevice-fhirPreferredAssigningAuthorityOfPatientID>`",string,"Assigning Authority of Patient IDs included in outgoing FHIR messages. If absent, all Patient IDs of the Patient are included. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (fhirPreferredAssigningAuthorityOfPatientID)"
    "
    .. _fhirDefaultSystemOfPatientID:
    .. _archiveDevice-fhirDefaultSystemOfPatientID:

    :ref:`FHIR Default System of Patient ID <archiveDevice-fhirDefaultSystemOfPatientID>`",string,"Namespace (system) of the Patient ID in logical references of Patients in outgoing FHIR messages, if no value is derived from the 'Issuer of Patient ID' or the 'Universal Entity ID' according configured 'FHIR System of Patient ID', 'FHIR System by Issuer of Patient ID' and 'FHIR System Issuer of Patient ID Prefix'.

    (fhirDefaultSystemOfPatientID)"
    "
    .. _fhirSystemOfPatientID:
    .. _archiveDevice-fhirSystemOfPatientID:

    :ref:`FHIR System of Patient ID(s) <archiveDevice-fhirSystemOfPatientID>`",string,"Specifies if the 'Issuer of Patient ID' (= Local Namespace Entity ID) or the 'Universal Entity ID' shall be used as namespace (system) of the Patient ID in logical references of Patients in outgoing FHIR messages. If both are specified, the 'Issuer of Patient ID' will only be used if there is no the 'Universal Entity ID'.

    Enumerated values:

    LocalNamespaceEntityID (= Use IssuerOfPatientID as namespace (system) of the Patient ID in logical references of Patients in outgoing FHIR messages)

    UniversalEntityID (= Use IssuerOfPatientIDQualifiersSequence.UniversalEntityID as namespace (system) of the Patient ID in logical references of Patients in outgoing FHIR messages)

    (fhirSystemOfPatientID)"
    "
    .. _fhirSystemByIssuerOfPatientID:
    .. _archiveDevice-fhirSystemByIssuerOfPatientID:

    :ref:`FHIR System by Issuer of Patient ID(s) <archiveDevice-fhirSystemByIssuerOfPatientID>`",string,"Specifies mapping of 'Issuer of Patient ID' to namespace (system) of the Patient ID in outgoing FHIR messages. Format: {Issuer of Patient ID}={system}. Required if 'FHIR System of Patient ID' includes 'LocalNamespaceEntityID'.

    (fhirSystemByIssuerOfPatientID)"
    "
    .. _fhirSystemIssuerOfPatientIDPrefix:
    .. _archiveDevice-fhirSystemIssuerOfPatientIDPrefix:

    :ref:`FHIR System Issuer of Patient ID Prefix <archiveDevice-fhirSystemIssuerOfPatientIDPrefix>`",string,"Specifies prefix used to convert the 'Issuer of Patient ID' to namespace (system) of the Patient ID in outgoing FHIR messages, if 'FHIR System by Issuer of Patient ID' does not contain a matching entry for the 'Issuer of Patient ID'.

    (fhirSystemIssuerOfPatientIDPrefix)"
    "
    .. _fhirDefaultSystemOfAccessionNumber:
    .. _archiveDevice-fhirDefaultSystemOfAccessionNumber:

    :ref:`FHIR Default System of Accession Number <archiveDevice-fhirDefaultSystemOfAccessionNumber>`",string,"Namespace (system) of the Accession Number in logical references of Service Requests in outgoing FHIR messages, if no value is derived from the Local Namespace Entity ID or the Universal Entity ID according configured 'FHIR System of Accession Number', 'FHIR System by Local Namespace Entity ID of Accession Number' and 'FHIR System Local Namespace Entity ID of Accession Number Prefix'.

    (fhirDefaultSystemOfAccessionNumber)"
    "
    .. _fhirSystemOfAccessionNumber:
    .. _archiveDevice-fhirSystemOfAccessionNumber:

    :ref:`FHIR System of Accession Number(s) <archiveDevice-fhirSystemOfAccessionNumber>`",string,"Specifies if the 'Local Namespace Entity ID' or the 'Universal Entity ID' shall be used as namespace (system) of the Accession Number in logical references of Service Requests in outgoing FHIR messages. If both are specified, the 'Local Namespace Entity ID' will only be used if there is no 'Universal Entity ID'.

    Enumerated values:

    LocalNamespaceEntityID (= Use IssuerOfAccessionNumberSequence.LocalNamespaceEntityID as namespace (system) of the Accession Number in logical references of Service Requests in outgoing FHIR messages)

    UniversalEntityID (= Use IssuerOfAccessionNumberSequence.UniversalEntityID as namespace (system) of the Accession Number in logical references of Service Requests in outgoing FHIR messages)

    (fhirSystemOfAccessionNumber)"
    "
    .. _fhirSystemByLocalNamespaceEntityIDOfAccessionNumber:
    .. _archiveDevice-fhirSystemByLocalNamespaceEntityIDOfAccessionNumber:

    :ref:`FHIR System by Local Namespace Entity ID of Accession Number(s) <archiveDevice-fhirSystemByLocalNamespaceEntityIDOfAccessionNumber>`",string,"Specifies Mapping of 'Local Namespace Entity ID' to namespace (system) of the Accession Number in logical references of Service Requests in outgoing FHIR messages. Format: {Local Namespace Entity ID}={system}. Required if 'FHIR System of Accession Number' includes 'LocalNamespaceEntityID'.

    (fhirSystemByLocalNamespaceEntityIDOfAccessionNumber)"
    "
    .. _fhirSystemLocalNamespaceEntityIDOfAccessionNumberPrefix:
    .. _archiveDevice-fhirSystemLocalNamespaceEntityIDOfAccessionNumberPrefix:

    :ref:`FHIR System Local Namespace Entity ID of Accession Number Prefix <archiveDevice-fhirSystemLocalNamespaceEntityIDOfAccessionNumberPrefix>`",string,"Specifies prefix used to convert the 'Local Namespace Entity ID' to namespace (system) of the Accession Number in logical references of Service Requests in outgoing FHIR messages, if 'FHIR System by Local Namespace Entity ID of Accession Number' does not contain a matching entry for the 'Local Namespace Entity ID'.

    (fhirSystemLocalNamespaceEntityIDOfAccessionNumberPrefix)"
    ":doc:`attributeFilter` (s)",object,"Specifies Attributes stored in the database"
    ":doc:`attributeSet` (s)",object,"Named Attribute Set for Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata or by Query Parameter 'comparefield' of DIFF-RS requests."
    ":doc:`bulkData` (s)",object,"Specifies Bulk Data Descriptors applied by services providing Metadata of archived instances."
    ":doc:`storage` (s)",object,"Specifies Storage System"
    ":doc:`queryRetrieveView` (s)",object,"Specifies behavior on Rejection Note Stored"
    ":doc:`queue` (s)",object,"Managed Task Queue"
    ":doc:`metrics` (s)",object,"Activated Metrics"
    ":doc:`pdqService` (s)",object,"Patient Demographics Query Service Descriptor"
    ":doc:`exporter` (s)",object,"Exporter Descriptor"
    ":doc:`exportRule` (s)",object,"Export Rules applied to DICOM objects received by any AE. May be supplemented by configured Export Rules for particular Archive Network AEs."
    ":doc:`exportPriorsRule` (s)",object,"Export Priors Rules applied to DICOM objects received by any AE. May be supplemented by configured Export Priors Rules for particular Archive Network AEs."
    ":doc:`mppsForwardRule` (s)",object,"MPPS Forward Rules applied to MPPS received by any AE. May be supplemented by configured MPPS Forward Rules for particular Archive Network AEs."
    ":doc:`rsForwardRule` (s)",object,"RESTful Forward Rules. May be supplemented by configured RESTful Forward Rules for particular Archive Network AEs."
    ":doc:`archiveCompressionRule` (s)",object,"Compression rules applied to DICOM objects received by any AE. May be supplemented by configured Compression Rules for particular Archive Network AEs."
    ":doc:`archiveAttributeCoercion` (s)",object,"Attribute Coercion applied to DIMSE received/sent by any AE. May be supplemented by configured Attribute Coercions for particular Archive Network AEs."
    ":doc:`archiveAttributeCoercion2` (s)",object,"Attribute Coercion applied to DIMSE received/sent by any AE. May be supplemented by configured Attribute Coercions for particular Archive Network AEs."
    ":doc:`rejectionNote` (s)",object,"Specifies behavior on Rejection Note Stored"
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policies applied to Studies received by any AE. May be supplemented by configured Study Retention Policies for particular Archive Network AEs."
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by any AE. May be supplemented by configured Store Access Control Rules for particular Archive Network AEs."
    ":doc:`changeAccessControlIDRule` (s)",object,"Change Access Control Rules applied to received Studies or Series."
    ":doc:`upsOnStore` (s)",object,"UPS on Store Rules applied to DICOM objects received by any AE. May be supplemented by configured UPS on Store Rules for particular Archive Network AEs."
    ":doc:`upsOnHL7` (s)",object,"UPS on HL7 Rules applied to HL7 messages received by any HL7 Application. May be supplemented by configured UPS on HL7 Rules for particular HL7 Applications."
    ":doc:`upsOnUPSCompleted` (s)",object,"UPS on UPS Completed Rules applied to UPS managed by any AE. May be supplemented by configured UPS on UPS Completed Rules for particular Archive Network AEs."
    ":doc:`upsOnUPSCanceled` (s)",object,"UPS on UPS Canceled Rules applied to UPS managed by any AE. May be supplemented by configured UPS on UPS Canceled Rules for particular Archive Network AEs."
    ":doc:`upsProcessingRule` (s)",object,"UPS Processing Rules."
    ":doc:`idGenerator` (s)",object,"ID Generator"
    ":doc:`mwlImport` (s)",object,"MWL Import"
    ":doc:`mwlIdleTimeout` (s)",object,"MWL Idle Timeout"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rules for HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Forward Rules for particular HL7 Applications."
    ":doc:`hl7ExportRule` (s)",object,"Export Rules applied to HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Export Rules for particular HL7 Application."
    ":doc:`hl7PrefetchRule` (s)",object,"HL7 Prefetch Rules applied to HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Prefetch Rules for particular HL7 Application."
    ":doc:`hl7StudyRetentionPolicy` (s)",object,"HL7 Study Retention Policies triggered by HL7 messages received by any HL7 Application. May be supplemented by configured Study Retention Policies for particular HL7 Applications."
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed received by any HL7 Application. May be supplemented by configured values for particular HL7 Applications."
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _dcmXRoadProperty:
    .. _archiveDevice-dcmXRoadProperty:

    :ref:`X-Road Property(s) <archiveDevice-dcmXRoadProperty>`",string,"Properties for accessing Estonian National Patient Registry in format {name}={value}

    (dcmXRoadProperty)"
    "
    .. _dcmImpaxReportProperty:
    .. _archiveDevice-dcmImpaxReportProperty:

    :ref:`Impax Report Property(s) <archiveDevice-dcmImpaxReportProperty>`",string,"Properties for accessing Agfa Impax Report Service in format {name}={value}

    (dcmImpaxReportProperty)"

.. toctree::

    attributeFilter
    attributeSet
    bulkData
    storage
    queryRetrieveView
    queue
    metrics
    pdqService
    exporter
    exportRule
    exportPriorsRule
    mppsForwardRule
    rsForwardRule
    archiveCompressionRule
    archiveAttributeCoercion
    archiveAttributeCoercion2
    rejectionNote
    studyRetentionPolicy
    storeAccessControlIDRule
    changeAccessControlIDRule
    upsOnStore
    upsOnHL7
    upsOnUPSCompleted
    upsOnUPSCanceled
    upsProcessingRule
    idGenerator
    mwlImport
    mwlIdleTimeout
    hl7ForwardRule
    hl7ExportRule
    hl7PrefetchRule
    hl7StudyRetentionPolicy
    hl7OrderScheduledStation
    hl7OrderSPSStatus
