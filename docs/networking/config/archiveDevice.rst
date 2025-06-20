Archive Device
==============
DICOM Archive Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Device Attributes (LDAP Object: dcmArchiveDevice)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmFuzzyAlgorithmClass:

    :ref:`Fuzzy Algorithm Class <dcmFuzzyAlgorithmClass>`",string,"Specifies Fuzzy Algorithm Implementation Class.

    Enumerated values:

    org.dcm4che3.soundex.Soundex

    org.dcm4che3.soundex.ESoundex

    org.dcm4che3.soundex.ESoundex9

    org.dcm4che3.soundex.Metaphone

    org.dcm4che3.soundex.KPhonetik

    org.dcm4che3.soundex.Phonem

    (dcmFuzzyAlgorithmClass)"
    "
    .. _dcmStoreImplementationVersionName:

    :ref:`Store Implementation Version Name <dcmStoreImplementationVersionName>`",boolean,"Indicates to include Implementation Version Name (0002,0012) in the File Meta Information of stored DICOM objects.

    (dcmStoreImplementationVersionName)"
    "
    .. _dcmBulkDataDescriptorID:

    :ref:`Bulk Data Descriptor ID <dcmBulkDataDescriptorID>`",string,"ID of Bulk Data Descriptor applied by all services providing Metadata of archived instances. If absent, only Attributes specified by the Composite Instance Retrieve Without Bulk Data Service Class are treated as Bulk Data. May be overwritten by configured values for particular Archive Network AEs.

    (dcmBulkDataDescriptorID)"
    "
    .. _dcmCalculateStudySizeDelay:

    :ref:`Calculate Study Size Delay <dcmCalculateStudySizeDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for eager calculation of Study Size and Query Attributes. If absent, no (minimal) delay for eager calculation of the Study Size and Query Attributes is applied.

    (dcmCalculateStudySizeDelay)"
    "
    .. _dcmCalculateStudySizePollingInterval:

    :ref:`Calculate Study Size Polling Interval <dcmCalculateStudySizePollingInterval>`",string,"Polling Interval for Studies with unknown size in ISO-8601 duration format PnDTnHnMnS. If absent, there is no eager calculation of the Study Size and Query Attributes.

    (dcmCalculateStudySizePollingInterval)"
    "
    .. _dcmCalculateStudySizeFetchSize:

    :ref:`Calculate Study Size Fetch Size <dcmCalculateStudySizeFetchSize>`",integer,"Limit result set of DB query for Studies with unknown size.

    (dcmCalculateStudySizeFetchSize)"
    "
    .. _dcmCalculateQueryAttributes:

    :ref:`Calculate Query Attributes <dcmCalculateQueryAttributes>`",boolean,"Indicates to eager calculate Query Attributes according configured Calculate Study Size Delay and Calculate Study Size Polling Interval.

    (dcmCalculateQueryAttributes)"
    "
    .. _dcmSeriesMetadataStorageID:

    :ref:`Series Metadata Storage ID(s) <dcmSeriesMetadataStorageID>`",string,"ID of Storage on which ZIP archives with aggregated Metadata of all instances of a Series is stored. Multiple Storage Systems may be configured. If absent, no aggregated Series Metadata will be stored.

    (dcmSeriesMetadataStorageID)"
    "
    .. _dcmSeriesMetadataDelay:

    :ref:`Aggregate Series Metadata Delay <dcmSeriesMetadataDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for storing aggregated Series Metadata on storage. If absent, no aggregated Series Metadata will be stored. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSeriesMetadataDelay)"
    "
    .. _dcmUpdateSeriesMetadata:

    :ref:`Update Series Metadata <dcmUpdateSeriesMetadata>`",boolean,"Indicates to update aggregated Series Metadata on attributes update.

    (dcmUpdateSeriesMetadata)"
    "
    .. _dcmSeriesMetadataPollingInterval:

    :ref:`Update Series Metadata Polling Interval <dcmSeriesMetadataPollingInterval>`",string,"Polling Interval for Series scheduled for Metadata update in ISO-8601 duration format PnDTnHnMnS. If absent, no aggregated Series Metadata will be stored.

    (dcmSeriesMetadataPollingInterval)"
    "
    .. _dcmSeriesMetadataFetchSize:

    :ref:`Update Series Metadata Fetch Size <dcmSeriesMetadataFetchSize>`",integer,"Maximal number of Series scheduled for Metadata update fetched by one query.

    (dcmSeriesMetadataFetchSize)"
    "
    .. _dcmSeriesMetadataThreads:

    :ref:`Update Series Metadata Threads <dcmSeriesMetadataThreads>`",integer,"Number of Threads used for creation and update of Series Metadata.

    (dcmSeriesMetadataThreads)"
    "
    .. _dcmSeriesMetadataMaxRetries:

    :ref:`Update Series Metadata Maximum Number of Retries <dcmSeriesMetadataMaxRetries>`",integer,"Maximum number of retries to create/update aggregated Series Metadata. Only effective if Update Series Metadata Retry Interval is specified. -1 = forever.

    (dcmSeriesMetadataMaxRetries)"
    "
    .. _dcmSeriesMetadataRetryInterval:

    :ref:`Update Series Metadata Retry Interval <dcmSeriesMetadataRetryInterval>`",string,"Interval in ISO-8601 duration format PnDTnHnMnS in which failed attempts to create/update aggregated Series Metadata will be retried. Only effective if Update Series Metadata Maximum Number of Retries != 0. If absent, failed attempts will not be retried.

    (dcmSeriesMetadataRetryInterval)"
    "
    .. _dcmPurgeInstanceRecords:

    :ref:`Purge(d) Instance Records <dcmPurgeInstanceRecords>`",boolean,"Indicates to purge instance records from DB. Also indicates to explicitly query series metadata zip files to check for purged instances for subsequent processing of archive functions. Set to 'True' if 'Purge Instance Records Delay' is configured.

    (dcmPurgeInstanceRecords)"
    "
    .. _dcmPurgeInstanceRecordsDelay:

    :ref:`Purge Instance Records Delay <dcmPurgeInstanceRecordsDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for purging Instance Records from the DB. May be overwritten by configured values for particular Archive Network AEs. Only effective, if Purge Instance Records = true.

    (dcmPurgeInstanceRecordsDelay)"
    "
    .. _dcmPurgeInstanceRecordsPollingInterval:

    :ref:`Purge Instance Records Polling Interval <dcmPurgeInstanceRecordsPollingInterval>`",string,"Polling Interval for Series scheduled for purging Instance Records from the DB in ISO-8601 duration format PnDTnHnMnS. Only effective, if Purge Instance Records = true.

    (dcmPurgeInstanceRecordsPollingInterval)"
    "
    .. _dcmPurgeInstanceRecordsFetchSize:

    :ref:`Purge Instance Records Fetch Size <dcmPurgeInstanceRecordsFetchSize>`",integer,"Maximal number of Series scheduled for purging Instance Records from the DB fetched by one query. Only effective, if Purge Instance Records = true.

    (dcmPurgeInstanceRecordsFetchSize)"
    "
    .. _dcmMWLPollingInterval:

    :ref:`MWL Polling Interval <dcmMWLPollingInterval>`",string,"Polling Interval for updating the status of idle MWL items and deleting MWL items in ISO-8601 duration format PnDTnHnMnS. If absent, MWL Items will not get update or deleted.

    (dcmMWLPollingInterval)"
    "
    .. _dcmMWLFetchSize:

    :ref:`MWL Fetch Size <dcmMWLFetchSize>`",integer,"Maximal number of MWL items to update or delete in one transaction.

    (dcmMWLFetchSize)"
    "
    .. _dcmMWLImportInterval:

    :ref:`MWL Import Interval <dcmMWLImportInterval>`",string,"Interval for import of Scheduled Procedure Steps from external MWL SCPs in ISO-8601 duration format PnDTnHnMn.nS; disabled if absent.

    (dcmMWLImportInterval)"
    "
    .. _dcmDeleteMWLDelay:

    :ref:`Delete MWL Delay(s) <dcmDeleteMWLDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for deleting MWL items, whose updated_time is older than the specified delay. Status specific delays can be specified by prefix 'SCHEDULED:', 'ARRIVED:', 'READY:', 'STARTED:', 'DEPARTED:', 'CANCELED:', 'DISCONTINUED:', 'COMPLETED:'. Examples: PT5M or CANCELED:PT10M. If absent, MWL Items will not get deleted.

    (dcmDeleteMWLDelay)"
    "
    .. _dcmDeleteUPSPollingInterval:

    :ref:`Delete UPS Polling Interval <dcmDeleteUPSPollingInterval>`",string,"Polling Interval for deleting Unified Procedure Steps (UPS) in ISO-8601 duration format PnDTnHnMnS. If absent, Unified Procedure Steps will not get deleted.

    (dcmDeleteUPSPollingInterval)"
    "
    .. _dcmDeleteUPSFetchSize:

    :ref:`Delete UPS Fetch Size <dcmDeleteUPSFetchSize>`",integer,"Maximal number of Unified Procedure Steps (UPS) to delete in one transaction.

    (dcmDeleteUPSFetchSize)"
    "
    .. _dcmDeleteUPSCompletedDelay:

    :ref:`Delete UPS Completed Delay <dcmDeleteUPSCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for deleting completed Unified Procedure Steps without Deletion Lock. If absent, completed Unified Procedure Steps without Deletion Lock are deleted immediately.

    (dcmDeleteUPSCompletedDelay)"
    "
    .. _dcmDeleteUPSCanceledDelay:

    :ref:`Delete UPS Canceled Delay <dcmDeleteUPSCanceledDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for deleting canceled Unified Procedure Steps without Deletion Lock. If absent, canceled Unified Procedure Steps without Deletion Lock are deleted immediately.

    (dcmDeleteUPSCanceledDelay)"
    "
    .. _dcmOverwritePolicy:

    :ref:`Overwrite Policy <dcmOverwritePolicy>`",string,"Specifies behavior on receive of objects, which SOP Instance UID matches a previous received object. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NEVER

    ALWAYS

    SAME_SOURCE

    EVEN_WITH_EQUAL_DIGEST

    (dcmOverwritePolicy)"
    "
    .. _dcmRelationalMismatchPolicy:

    :ref:`Relational Mismatch Policy <dcmRelationalMismatchPolicy>`",string,"Specifies behavior on receive of objects, which SOP Instance UID matches a previous received object belonging to a different Series. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    IGNORE

    REJECT

    OVERWRITE

    STORE_ADDITIONALLY

    (dcmRelationalMismatchPolicy)"
    "
    .. _dcmRecordAttributeModification:

    :ref:`Record Attribute Modification <dcmRecordAttributeModification>`",boolean,"Indicates if modifications of attributes of stored objects are recorded in Items of the Original Attributes Sequence. May be overwritten by configured values for particular Archive Network AE or Archive HL7 Application.

    (dcmRecordAttributeModification)"
    "
    .. _dcmAcceptMissingPatientID:

    :ref:`Accept Missing Patient ID <dcmAcceptMissingPatientID>`",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    YES

    NO

    CREATE

    (dcmAcceptMissingPatientID)"
    "
    .. _dcmAcceptConflictingPatientID:

    :ref:`Accept Conflicting Patient ID <dcmAcceptConflictingPatientID>`",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    YES

    NO

    MERGED

    (dcmAcceptConflictingPatientID)"
    "
    .. _dcmIdentifyPatientByIDAndName:

    :ref:`Identify Patient by ID and Name <dcmIdentifyPatientByIDAndName>`",boolean,"Indicates to consider also the Patient Name on receive of DICOM objects to determine if they belongs to an already existing Patient in the archive.

    (dcmIdentifyPatientByIDAndName)"
    "
    .. _dcmIdentifyPatientByAllAttributes:

    :ref:`Identify Patient by all Attributes <dcmIdentifyPatientByAllAttributes>`",boolean,"Indicates if all Patient attributes in received objects shall be used for associating an already existing Patient in the archive, if the Assigning Authority of the Patient ID is not specified by an Issuer of Patient ID or Universal Entity ID. Attention: disables the coercion of stale Patient attributes in received objects and breaks Patient Management functions relying on the unambiguity of Patient IDs.

    (dcmIdentifyPatientByAllAttributes)"
    "
    .. _dcmBulkDataSpoolDirectory:

    :ref:`Bulk Data Spool Directory <dcmBulkDataSpoolDirectory>`",string,"Path to Bulk Data Spool Directory. May be overwritten by configured values for particular Archive Network AEs.

    (dcmBulkDataSpoolDirectory)"
    "
    .. _dcmHideSPSWithStatusFromMWL:

    :ref:`Hide SPS with Status by MWL SCP(s) <dcmHideSPSWithStatusFromMWL>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP. May be overwritten by configured values for particular Archive Network AEs.

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

    :ref:`Hide SPS with Status by MWL RS(s) <dcmHideSPSWithStatusFromMWLRS>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL RS. May be overwritten by configured values for particular Archive Network AEs.

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

    :ref:`Encode as JSON Number(s) <dcmEncodeAsJSONNumber>`",string,"VR encoded as JSON Number. If not listed, IS, DS, SV and UV values are encoded as JSON Strings. May be supplemented by configured values for particular Archive Network AEs.

    Enumerated values:

    DS

    IS

    SV

    UV

    (dcmEncodeAsJSONNumber)"
    "
    .. _dcmValidateCallingAEHostname:

    :ref:`Validate Calling AE Hostname <dcmValidateCallingAEHostname>`",boolean,"Validate Calling AE Hostname or IP Address of Association requestors. May be overwritten by configured values for particular Archive Network AEs.

    (dcmValidateCallingAEHostname)"
    "
    .. _dcmUserIdentityNegotiation:

    :ref:`User Identity Negotiation <dcmUserIdentityNegotiation>`",string,"Specifies to ignore User Identity Negotiation Sub-Item in Association requests (=NOT_SUPPORTED), to verify passed Username and password or JSON Web Token are against a Keycloak server (=SUPPORTS), or to reject Association requests without a valid Username and password or JSON Web Token in its Identity Negotiation Sub-Item (=REQUIRED). May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NOT_SUPPORTED

    SUPPORTS

    REQUIRED

    (dcmUserIdentityNegotiation)"
    "
    .. _dcmUserIdentityNegotiationRole:

    :ref:`User Identity Negotiation Role <dcmUserIdentityNegotiationRole>`",string,"Constrain accepted User Identity Negotiation requests to users with specified role. If absent, only verify passed username and password or JSON Web Token. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUserIdentityNegotiationRole)"
    "
    .. _dcmUserIdentityNegotiationKeycloakClientID:

    :ref:`User Identity Negotiation Keycloak Client ID <dcmUserIdentityNegotiationKeycloakClientID>`",string,"Keycloak Client ID referring Keycloak connection configuration for verifying passed username and password or JSON Web Token. If absent, System Properties ${auth-server-url}, ${realm-name:dcm4che}, ${ui-client-id:dcm4chee-arc-ui}, ${disable-trust-manager:false}, ${allow-any-hostname:true} will be applied. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUserIdentityNegotiationKeycloakClientID)"
    "
    .. _dcmPersonNameComponentOrderInsensitiveMatching:

    :ref:`Person Name Component Order Insensitive Matching <dcmPersonNameComponentOrderInsensitiveMatching>`",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names. May be overwritten by configured values for particular Archive Network AEs.

    (dcmPersonNameComponentOrderInsensitiveMatching)"
    "
    .. _dcmSendPendingCGet:

    :ref:`Send Pending C-Get <dcmSendPendingCGet>`",boolean,"Enables pending C-GET responses. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSendPendingCGet)"
    "
    .. _dcmSendPendingCMoveInterval:

    :ref:`Send Pending C-Move Interval <dcmSendPendingCMoveInterval>`",string,"Interval of pending C-MOVE responses in ISO-8601 duration format PnDTnHnMnS; disabled if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSendPendingCMoveInterval)"
    "
    .. _dcmWadoSupportedSRClasses:

    :ref:`Wado Supported SR Classes(s) <dcmWadoSupportedSRClasses>`",string,"Supported SR SOP classes for WADO retrieval

    (dcmWadoSupportedSRClasses)"
    "
    .. _dcmWadoSupportedPRClasses:

    :ref:`Wado Supported PR Classes(s) <dcmWadoSupportedPRClasses>`",string,"Supported PR SOP classes for WADO retrieval

    (dcmWadoSupportedPRClasses)"
    "
    .. _dcmWadoSR2HtmlTemplateURI:

    :ref:`Wado SR2 Html Template URI <dcmWadoSR2HtmlTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to html. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoSR2HtmlTemplateURI)"
    "
    .. _dcmWadoSR2TextTemplateURI:

    :ref:`Wado SR2 Text Template URI <dcmWadoSR2TextTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to plain text. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoSR2TextTemplateURI)"
    "
    .. _dcmWadoCDA2HtmlTemplateURI:

    :ref:`Wado CDA to HTML Template URI <dcmWadoCDA2HtmlTemplateURI>`",string,"URL to XSL style sheet inserted as <?xml-stylesheet type=""text/xsl"" href=""<url>"" > in CDA documents returned by WADO-URI service. If absent, the embedded CDI document is returned verbatim. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoCDA2HtmlTemplateURI)"
    "
    .. _dcmWadoThumbnailViewport:

    :ref:`Wado Thumbnail Viewport <dcmWadoThumbnailViewport>`",string,"Dimension of Thumbnails returned by WADO retrieve of Instance Thumbnails, if no Viewport is specified in the request. Format: <width>,<height>. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoThumbnailViewport)"
    "
    .. _dcmWadoZIPEntryNameFormat:

    :ref:`Wado ZIP Entry Name Format <dcmWadoZIPEntryNameFormat>`",string,"Format of entry names in ZIP archive returned by WADO-RS. May be overwritten by configured value for particular Archive Network AEs.

    (dcmWadoZIPEntryNameFormat)"
    "
    .. _dcmWadoIgnorePresentationLUTShape:

    :ref:`Wado Ignore Presentation LUT Shape <dcmWadoIgnorePresentationLUTShape>`",boolean,"Indicates to ignore (2050,0020) Presentation LUT Shape, but prioritize value of (0028,0004) Photometric Interpretation to determine if minimum sample value is intended to be displayed as white (=MONCHROME1) or as black (=MONCHROME2) on retrieve of rendered DICOM images by WADO-RS or WADO-URI services. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoIgnorePresentationLUTShape)"
    "
    .. _dcmWadoMetadataExcludePrivate:

    :ref:`Wado Metadata Exclude Private <dcmWadoMetadataExcludePrivate>`",boolean,"Indicates to exclude Private Data Elements from Metadata returned by WADO-RS Retrieve Transaction. May be overwritten by configured values for particular Archive Network AEs.

    (dcmWadoMetadataExcludePrivate)"
    "
    .. _dcmQueryFetchSize:

    :ref:`Query Fetch Size <dcmQueryFetchSize>`",integer,"Number of rows fetched from the database at once by the Query Service.

    (dcmQueryFetchSize)"
    "
    .. _dcmQueryMaxNumberOfResults:

    :ref:`Query Max Number Of Results <dcmQueryMaxNumberOfResults>`",integer,"Maximal number of return results by C-FIND SCP. If the number of matches extends the limit, the C-FIND request will be refused. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQueryMaxNumberOfResults)"
    "
    .. _dcmQidoMaxNumberOfResults:

    :ref:`QIDO Max Number Of Results <dcmQidoMaxNumberOfResults>`",integer,"Maximal number of return results by QIDO-RS Service. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoMaxNumberOfResults)"
    "
    .. _dcmQidoETag:

    :ref:`QIDO ETag <dcmQidoETag>`",boolean,"Indicates to return Last-Modified and ETag for Search Series or Instances of a Study; disabled if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoETag)"
    "
    .. _dcmQidoResultOrderBy:

    :ref:`QIDO Result Order By(s) <dcmQidoResultOrderBy>`",string,"Specifies order of matching results returned by QIDO-RS, UPS-RS and proprietary Search Services, if not specified by query parameter orderby. Format: {service}:[-]{attributeID}[,...], with {service} is patients, studies, series, instances, workitems, mwlitems or mpps. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoResultOrderBy)"
    "
    .. _dcmFwdMppsDestination:

    :ref:`MPPS Forward Destination(s) <dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFwdMppsDestination)"
    "
    .. _dcmIanDestination:

    :ref:`IAN Destination(s) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanDestination)"
    "
    .. _dcmIanTrigger:

    :ref:`IAN Trigger(s) <dcmIanTrigger>`",string,"Events triggering to send an IAN N-CREATE RQ to Application Entities configured by IAN Destination. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    STUDY_RECEIVED

    MPPS_RECEIVED

    REJECTION_NOTE_RECEIVED

    FIRST_OBJECT_OF_STUDY_RECEIVED

    (dcmIanTrigger)"
    "
    .. _dcmIanDelay:

    :ref:`IAN Delay <dcmIanDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which an IAN for a received study is sent to configured IAN destinations. Only effective if IAN Trigger includes STUDY_RECEIVED. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanDelay)"
    "
    .. _dcmIanTimeout:

    :ref:`IAN Timeout <dcmIanTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMnS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. Only effective if IAN Trigger includes MPPS_RECEIVED. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanTimeout)"
    "
    .. _dcmIanOnTimeout:

    :ref:`IAN On Timeout <dcmIanOnTimeout>`",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced in MPPS is exceeded. Only effective if IAN Trigger includes MPPS_RECEIVED. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanOnTimeout)"
    "
    .. _dcmIanTaskPollingInterval:

    :ref:`IAN Task Polling Interval <dcmIanTaskPollingInterval>`",string,"Polling Interval for IAN Tasks in ISO-8601 duration format PnDTnHnMnS for checking vor completeness of study or instances referenced in MPPS. If absent, configured IAN Trigger STUDY_RECEIVED or MPPS_RECEIVED will not be effective.

    (dcmIanTaskPollingInterval)"
    "
    .. _dcmIanTaskFetchSize:

    :ref:`IAN Task Fetch Size <dcmIanTaskFetchSize>`",integer,"Maximal number of IAN Tasks scheduled in one transaction.

    (dcmIanTaskFetchSize)"
    "
    .. _dcmSpanningCFindSCP:

    :ref:`Spanning C-Find SCP <dcmSpanningCFindSCP>`",string,"AE Title of external C-FIND SCP to forward C-FIND RQs and backward responses according configured Spanning C-Find SCP Policy. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSpanningCFindSCP)"
    "
    .. _dcmSpanningCFindSCPPolicy:

    :ref:`Spanning C-Find SCP Policy <dcmSpanningCFindSCPPolicy>`",string,"Specifies policy for combining matches returned from configured Spanning C-Find SCP with matching entries from the archive DB. SUPPLEMENT (= returns local matches before additional matches from Spanning C-Find SCP ), MERGE (= returns matches from Spanning C-Find SCP before additional local matches), REPLACE (= returns only matches from Spanning C-Find SCP). May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    SUPPLEMENT

    MERGE

    REPLACE

    (dcmSpanningCFindSCPPolicy)"
    "
    .. _dcmSpanningCFindSCPRetrieveAET:

    :ref:`Spanning C-Find SCP Retrieve AE Title(s) <dcmSpanningCFindSCPRetrieveAET>`",string,"Specifies Retrieve AE Title(s) in returned matches from Spanning C-Find SCP. Keep original Retrieve AE Title(s) returned by Spanning C-Find SCP if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSpanningCFindSCPRetrieveAET)"
    "
    .. _dcmFallbackCMoveSCP:

    :ref:`Fallback C-Move SCP <dcmFallbackCMoveSCP>`",string,"AE Title of external C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not managed by this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFallbackCMoveSCP)"
    "
    .. _dcmFallbackCMoveSCPDestination:

    :ref:`Fallback C-Move SCP Destination <dcmFallbackCMoveSCPDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to the external C-MOVE SCP specified by dcmFallbackCMoveSCP

    (dcmFallbackCMoveSCPDestination)"
    "
    .. _dcmFallbackCMoveSCPStudyOlderThan:

    :ref:`Fallback C-Move SCP Study Older Than <dcmFallbackCMoveSCPStudyOlderThan>`",string,"Specifies threshold for Study Date in format YYYYMMDD for marking received Studies as (potential) incomplete to enforce the retrieve from configured dcmFallbackCMoveSCP

    (dcmFallbackCMoveSCPStudyOlderThan)"
    "
    .. _dcmFallbackCMoveSCPLeadingCFindSCP:

    :ref:`Fallback C-Move SCP Leading C-Find SCP <dcmFallbackCMoveSCPLeadingCFindSCP>`",string,"AE Title of external C-FIND SCP for Verification of Number of Instances retrieved from external C-MOVE SCP specified by dcmFallbackCMoveSCP.

    (dcmFallbackCMoveSCPLeadingCFindSCP)"
    "
    .. _dcmFallbackCMoveSCPRetries:

    :ref:`Fallback C-Move SCP Retries <dcmFallbackCMoveSCPRetries>`",integer,"Maximal number of retries to retrieve not available objects from C-MOVE SCP configured by dcmFallbackCMoveSCP. -1 = forever.

    (dcmFallbackCMoveSCPRetries)"
    "
    .. _dcmFallbackWadoURIWebAppName:

    :ref:`Fallback WADO-URI Web Application Name <dcmFallbackWadoURIWebAppName>`",string,"Name of external Web Application to redirect WADO-URI requests if the requested Object is not available by this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFallbackWadoURIWebAppName)"
    "
    .. _dcmFallbackWadoURIHttpStatusCode:

    :ref:`Fallback WADO-URI Http Status Code <dcmFallbackWadoURIHttpStatusCode>`",integer,"HTTP Status code of Redirect Response configured by Fallback WADO-URI Web Application Name. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    301

    302

    303

    307

    (dcmFallbackWadoURIHttpStatusCode)"
    "
    .. _dcmFallbackWadoURIRedirectOnNotFound:

    :ref:`Fallback WADO-URI Redirect On Not Found <dcmFallbackWadoURIRedirectOnNotFound>`",boolean,"Indicates if WADO-URI requests are redirected to configured Fallback WADO-URI Web Application Name even if the object was not found or - if set to false - only if the object is no longer accessible on this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFallbackWadoURIRedirectOnNotFound)"
    "
    .. _dcmExternalWadoRSWebAppName:

    :ref:`External WADO-RS Web Application Name <dcmExternalWadoRSWebAppName>`",string,"Name of external Web Application to redirect WADO-RS requests if some of the requested objects are no longer accessible on this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmExternalWadoRSWebAppName)"
    "
    .. _dcmExternalWadoRSHttpStatusCode:

    :ref:`External WADO-RS Http Status Code <dcmExternalWadoRSHttpStatusCode>`",integer,"HTTP Status code of Redirect Response configured by External WADO-RS Web Application Name. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    301

    302

    303

    307

    (dcmExternalWadoRSHttpStatusCode)"
    "
    .. _dcmExternalWadoRSRedirectOnNotFound:

    :ref:`External WADO-RS Redirect On Not Found <dcmExternalWadoRSRedirectOnNotFound>`",boolean,"Indicates if WADO-RS requests are redirected to configured External WADO-RS Web Application Name even if the requested objects were not found or - if set to false - only if some of the requested objects are no longer accessible on this archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmExternalWadoRSRedirectOnNotFound)"
    "
    .. _dcmFallbackCMoveSCPCallingAET:

    :ref:`Fallback C-Move SCP Calling AE title <dcmFallbackCMoveSCPCallingAET>`",string,"Calling AE Title used in A-ASSOCIATE-RQ to configured Fallback C-MOVE SCP. If absent, the AE Title of the external C-MOVE SCU is used. May be overwritten by configured value for particular Archive Network AEs.

    (dcmFallbackCMoveSCPCallingAET)"
    "
    .. _dcmAltCMoveSCP:

    :ref:`Alternative C-Move SCP <dcmAltCMoveSCP>`",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage

    (dcmAltCMoveSCP)"
    "
    .. _dcmCStoreSCUOfCMoveSCP:

    :ref:`C-STORE SCU of C-MOVE SCP(s) <dcmCStoreSCUOfCMoveSCP>`",string,"Indicates to identify received C-STORE RQs as caused by a forwarded C-MOVE RQs by the Calling AET in the A-Associate-RQ in format <Calling AET>=<C-MOVE-SCP>. Typically <Calling AET> and <C-MOVE-SCP> are equal. If no value is configured for a particular C-MOVE SCP, attribute (0000,1030) Move Originator Application Entity Title in the C-STORE RQ is used to find the corresponding forwarded C-MOVE RQ to forward the received C-STORE RQ to the original Move Destination.

    (dcmCStoreSCUOfCMoveSCP)"
    "
    .. _dcmTaskPollingInterval:

    :ref:`Task Polling Interval <dcmTaskPollingInterval>`",string,"Polling Interval for scheduled Tasks in ISO-8601 duration format PnDTnHnMnS. If absent, Tasks will not get processed.

    (dcmTaskPollingInterval)"
    "
    .. _dcmTaskFetchSize:

    :ref:`Task Fetch Size <dcmTaskFetchSize>`",integer,"Limit result set of DB query for scheduled Tasks.

    (dcmTaskFetchSize)"
    "
    .. _dcmUPSProcessingPollingInterval:

    :ref:`UPS Processing Polling Interval <dcmUPSProcessingPollingInterval>`",string,"Polling Interval for Workitems ready for processing in ISO-8601 duration format PnDTnHnMnS.

    (dcmUPSProcessingPollingInterval)"
    "
    .. _dcmUPSProcessingFetchSize:

    :ref:`UPS Processing  Fetch Size <dcmUPSProcessingFetchSize>`",integer,"Limit result set of DB query for Workitems ready for processing.

    (dcmUPSProcessingFetchSize)"
    "
    .. _dcmRetrieveTaskWarningOnNoMatch:

    :ref:`Retrieve Task Warning on no Match <dcmRetrieveTaskWarningOnNoMatch>`",boolean,"Indicates if the result status of Retrieve Tasks shall be set to WARNING if none of the requested objects was found on the C-MOVE SCP. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveTaskWarningOnNoMatch)"
    "
    .. _dcmRetrieveTaskWarningOnWarnings:

    :ref:`Retrieve Task Warning on Warnings <dcmRetrieveTaskWarningOnWarnings>`",boolean,"Indicates if the result status of Retrieve Tasks shall be set to WARNING if there are Warning Sub-Operations, even if the retrieve of all objects was successful. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveTaskWarningOnWarnings)"
    "
    .. _dcmPurgeStoragePollingInterval:

    :ref:`Purge Storage Polling Interval <dcmPurgeStoragePollingInterval>`",string,"Polling Interval for deleting objects in ISO-8601 duration format PnDTnHnMnS.

    (dcmPurgeStoragePollingInterval)"
    "
    .. _dcmPurgeStorageFetchSize:

    :ref:`Purge Storage Fetch Size <dcmPurgeStorageFetchSize>`",integer,"Maximal number of objects to delete in one task.

    (dcmPurgeStorageFetchSize)"
    "
    .. _dcmFailedToDeletePollingInterval:

    :ref:`Failed to delete Polling Interval <dcmFailedToDeletePollingInterval>`",string,"Polling Interval for resolving deletion failures in ISO-8601 duration format PnDTnHnMnS.

    (dcmFailedToDeletePollingInterval)"
    "
    .. _dcmFailedToDeleteFetchSize:

    :ref:`Failed to delete Fetch Size <dcmFailedToDeleteFetchSize>`",integer,"Maximal number of Location records fetched for resolving deletion failures in one query.

    (dcmFailedToDeleteFetchSize)"
    "
    .. _dcmDeleteStudyBatchSize:

    :ref:`Delete Study Batch Size <dcmDeleteStudyBatchSize>`",integer,"Number of Studies to delete from the Storage System, if the usable space fall below configured Usable Space, before checking the usable space again.

    (dcmDeleteStudyBatchSize)"
    "
    .. _dcmDeleteStudyInterval:

    :ref:`Delete Study Interval <dcmDeleteStudyInterval>`",string,"Specifies maximum range of access time of studies, in ISO-8601 duration format PnDTnHnMnS, to be deleted from the storage system, if the usable space falls below configured Deleter Thresholds, before checking the Deleter Thresholds again. If absent, the number of Studies to be deleted is only limited by configured Delete Study Batch Size.

    (dcmDeleteStudyInterval)"
    "
    .. _dcmPreserveStudyInterval:

    :ref:`Preserve Study Interval <dcmPreserveStudyInterval>`",string,"Protect studies which were accessed later than the specified time interval, in ISO-8601 duration format PnDTnHnMnS, from deletion from the storage system, if the usable space falls below configured Deleter Thresholds. If absent, most recently accessed studies shall also get deleted from the storage system, if least recently accessed studies were not found or if Delete Least Recently Accessed Study First is set to FALSE.

    (dcmPreserveStudyInterval)"
    "
    .. _dcmDeleteStudyLeastRecentlyAccessedFirst:

    :ref:`Delete Least Recently Accessed Study First <dcmDeleteStudyLeastRecentlyAccessedFirst>`",boolean,"Indicates to delete studies beginning with the least recently accessed study first, if the usable space falls below configured Deleter Thresholds. By default, TRUE.

    (dcmDeleteStudyLeastRecentlyAccessedFirst)"
    "
    .. _dcmDeleteStudyChunkSize:

    :ref:`Delete Study Chunk Size <dcmDeleteStudyChunkSize>`",integer,"Number of Instances deleted in one DB transaction on permanent deletion of Studies.

    (dcmDeleteStudyChunkSize)"
    "
    .. _dcmDeletePatientOnDeleteLastStudy:

    :ref:`Delete Patient On Delete Last Study <dcmDeletePatientOnDeleteLastStudy>`",boolean,"Specifies if a Patient shall be deleted on deletion of its last study.

    (dcmDeletePatientOnDeleteLastStudy)"
    "
    .. _dcmDeleteRejectedPollingInterval:

    :ref:`Delete Rejected Polling Interval <dcmDeleteRejectedPollingInterval>`",string,"Polling Interval for deleting rejected instances from the DB in ISO-8601 duration format PnDTnHnMnS.

    (dcmDeleteRejectedPollingInterval)"
    "
    .. _dcmDeleteRejectedFetchSize:

    :ref:`Delete Rejected Fetch Size <dcmDeleteRejectedFetchSize>`",integer,"Maximal number of rejected instances to delete from the DB in one task.

    (dcmDeleteRejectedFetchSize)"
    "
    .. _dcmDBReadOnly:

    :ref:`DB Read Only <dcmDBReadOnly>`",boolean,"Indicates read-only access to the database, preventing DB updates on query/retrieve.

    (dcmDBReadOnly)"
    "
    .. _dcmMaxAccessTimeStaleness:

    :ref:`Maximum Access Time Staleness <dcmMaxAccessTimeStaleness>`",string,"Maximal staleness of recorded study accession time in ISO-8601 duration format PnDTnHnMnS. Update of the access time disabled, if absent.

    (dcmMaxAccessTimeStaleness)"
    "
    .. _dcmAECacheStaleTimeout:

    :ref:`AE Cache Stale Timeout <dcmAECacheStaleTimeout>`",string,"Maximal staleness of cached AE in ISO-8601 duration format PnDTnHnMnS. If absent, cached AE entries will not be refetched from LDAP.

    (dcmAECacheStaleTimeout)"
    "
    .. _dcmLeadingCFindSCPQueryCacheStaleTimeout:

    :ref:`Leading C-Find SCP Query Cache Stale Timeout <dcmLeadingCFindSCPQueryCacheStaleTimeout>`",string,"Maximal staleness of cached Patient and Study attributes fetched from leading C-Find SCP in ISO-8601 duration format PnDTnHnMnS. If absent, cache Study attributes are only removed on reaching the maximal cache size.

    (dcmLeadingCFindSCPQueryCacheStaleTimeout)"
    "
    .. _dcmLeadingCFindSCPQueryCacheSize:

    :ref:`Leading C-Find SCP Query Cache Size <dcmLeadingCFindSCPQueryCacheSize>`",integer,"Maximum number of cached Patient and Study attributes fetched from leading C-Find SCP.

    (dcmLeadingCFindSCPQueryCacheSize)"
    "
    .. _dcmAuditSpoolDirectory:

    :ref:`Audit Spool Directory <dcmAuditSpoolDirectory>`",string,"Path to Audit Service Spool Directory.

    (dcmAuditSpoolDirectory)"
    "
    .. _dcmAuditPollingInterval:

    :ref:`Audit Polling Interval <dcmAuditPollingInterval>`",string,"Polling Interval for aggregating Audit Messages in ISO-8601 duration format PnDTnHnMnS. Audit Message aggregation disabled, if absent.

    (dcmAuditPollingInterval)"
    "
    .. _dcmAuditAggregateDuration:

    :ref:`Audit Aggregate Duration <dcmAuditAggregateDuration>`",string,"Audit Message Aggregation Duration in ISO-8601 duration format PnDTnHnMnS. Audit Message aggregation disabled, if absent.

    (dcmAuditAggregateDuration)"
    "
    .. _dcmAuditUnknownStudyInstanceUID:

    :ref:`Audit Unknown Study Instance UID <dcmAuditUnknownStudyInstanceUID>`",string,"Indicates study instance uid value to be sent in audit message when not known.

    (dcmAuditUnknownStudyInstanceUID)"
    "
    .. _dcmAuditUnknownPatientID:

    :ref:`Audit Unknown Patient ID <dcmAuditUnknownPatientID>`",string,"Indicates patient id value to be sent in audit message when not known.

    (dcmAuditUnknownPatientID)"
    "
    .. _dcmAudit2JsonFhirTemplateURI:

    :ref:`Audit to json+fhir Template URI <dcmAudit2JsonFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR JSON Resource Audit Event

    (dcmAudit2JsonFhirTemplateURI)"
    "
    .. _dcmAudit2XmlFhirTemplateURI:

    :ref:`Audit to xml+fhir Template URI <dcmAudit2XmlFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR XML Resource Audit Event

    (dcmAudit2XmlFhirTemplateURI)"
    "
    .. _dcmAuditSoftwareConfigurationVerbose:

    :ref:`Audit Software Configuration Verbose <dcmAuditSoftwareConfigurationVerbose>`",boolean,"Specifies if Child Objects and Attributes of created Objects should be included in Software Configuration Audit Message.

    (dcmAuditSoftwareConfigurationVerbose)"
    "
    .. _dcmAuditAssigningAuthorityOfPatientID:

    :ref:`Assigning Authority of Patient ID for Audit <dcmAuditAssigningAuthorityOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search qualified patient identifier in list of identifiers in PID-3. This qualified patient identifier shall be used in the patient details participant object. If absent, by default the first qualified patient identifier in PID-3 shall be used. If none of the qualified patient identifiers in the list match with the configured issuer, archive server log shall contain a log INFO message and by default the first qualified patient identifier in PID-3 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmAuditAssigningAuthorityOfPatientID)"
    "
    .. _dcmShowPatientInfoInSystemLog:

    :ref:`Show Patient Info In System Log <dcmShowPatientInfoInSystemLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in system logs.

    Enumerated values:

    PLAIN_TEXT

    HASH_NAME

    HASH_NAME_AND_ID

    (dcmShowPatientInfoInSystemLog)"
    "
    .. _dcmShowPatientInfoInAuditLog:

    :ref:`Show Patient Info In Audit Log <dcmShowPatientInfoInAuditLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in emitted audit messages.

    Enumerated values:

    PLAIN_TEXT

    HASH_NAME

    HASH_NAME_AND_ID

    (dcmShowPatientInfoInAuditLog)"
    "
    .. _dcmStowSpoolDirectory:

    :ref:`STOW-RS Spool Directory <dcmStowSpoolDirectory>`",string,"Path to Directory used by STOW-RS Service to spool Bulkdata of XML/JSON Metadata and Bulk Data Request Messages.

    (dcmStowSpoolDirectory)"
    "
    .. _dcmMWLAccessionNumberGenerator:

    :ref:`MWL Accession Number Generator <dcmMWLAccessionNumberGenerator>`",string,"Identifies ID Generator to supplement missing Accession Numbers of Scheduled Procedures Steps created on receive of HL7 Order messages or by RESTful service. May be overwritten by configured values for particular Archive Network AEs or Archive HL7 Application.

    (dcmMWLAccessionNumberGenerator)"
    "
    .. _dcmMWLRequestedProcedureIDGenerator:

    :ref:`MWL Requested Procedure ID Generator <dcmMWLRequestedProcedureIDGenerator>`",string,"Identifies ID Generator to supplement missing Requested Procedure IDs of Scheduled Procedures Steps created on receive of HL7 Order messages or by RESTful service. May be overwritten by configured values for particular Archive Network AEs or Archive HL7 Application.

    (dcmMWLRequestedProcedureIDGenerator)"
    "
    .. _dcmMWLScheduledProcedureStepIDGenerator:

    :ref:`MWL Scheduled Procedure Step ID Generator <dcmMWLScheduledProcedureStepIDGenerator>`",string,"Identifies ID Generator to supplement missing Scheduled Procedure Step IDs of Scheduled Procedures Steps created on receive of HL7 Order messages or by RESTful service. May be overwritten by configured values for particular Archive Network AEs or Archive HL7 Application.

    (dcmMWLScheduledProcedureStepIDGenerator)"
    "
    .. _dcmAuditHL7MsgLimit:

    :ref:`Audit HL7 Message Limit <dcmAuditHL7MsgLimit>`",integer,"Limit length of HL7 messages included in emitted Audit Records. May be overwritten by configured values for particular Archive HL7 Application.

    (dcmAuditHL7MsgLimit)"
    "
    .. _hl7ORUAction:

    :ref:`HL7 ORU Action(s) <hl7ORUAction>`",string,"Specifies action on receive of HL7 ORU^R01 message: IMPORT_REPORT (= transcode received HL7 ORU^R01 to DICOM SR), MWL_COMPLETED (= set Status of matching MWL items to COMPLETED). May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    IMPORT_REPORT

    MWL_COMPLETED

    (hl7ORUAction)"
    "
    .. _hl7PatientUpdateTemplateURI:

    :ref:`HL7 Patient Update Template URI <hl7PatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7PatientUpdateTemplateURI)"
    "
    .. _hl7ImportReportTemplateURI:

    :ref:`HL7 Import Report Template URI <hl7ImportReportTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ImportReportTemplateURI)"
    "
    .. _hl7ImportReportTemplateParam:

    :ref:`HL7 Import Report Template Parameter(s) <hl7ImportReportTemplateParam>`",string,"XSLT parameters passed to style sheet specified by HL7 Import Report Template URI. Format: {name}={value}. E.g.: 'langCodeValue=et', 'langCodingSchemeDesignator=RFC5646', 'langCodeMeaning=Estonian'. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ImportReportTemplateParam)"
    "
    .. _hl7ScheduleProcedureTemplateURI:

    :ref:`HL7 Schedule Procedure Template URI <hl7ScheduleProcedureTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ScheduleProcedureTemplateURI)"
    "
    .. _hl7OutgoingPatientUpdateTemplateURI:

    :ref:`HL7 Outgoing Patient Update Template URI <hl7OutgoingPatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet to transcode DICOM object patient attributes to HL7 ADT messages.

    (hl7OutgoingPatientUpdateTemplateURI)"
    "
    .. _hl7ScheduledProtocolCodeInOrder:

    :ref:`HL7 Schedule Protocol Code in Order <hl7ScheduledProtocolCodeInOrder>`",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    OBR_4_1

    OBR_4_4

    (hl7ScheduledProtocolCodeInOrder)"
    "
    .. _hl7ScheduledStationAETInOrder:

    :ref:`HL7 Schedule Station AET in Order <hl7ScheduledStationAETInOrder>`",string,"Specifies location of Scheduled Station AE Title in received HL7 Order message. Should not be configured for HL7 v2.5.1 OMI^O23 with IPC segment. If absent or no value is provided in the configured field, the Scheduled Station AE Title is selected according configured rules. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ORC_18

    (hl7ScheduledStationAETInOrder)"
    "
    .. _hl7LogFilePattern:

    :ref:`HL7 Log File Pattern <hl7LogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7LogFilePattern)"
    "
    .. _hl7ErrorLogFilePattern:

    :ref:`HL7 Error Log File Pattern <hl7ErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7ErrorLogFilePattern)"
    "
    .. _hl7OutgoingLogFilePattern:

    :ref:`HL7 Outgoing Log File Pattern <hl7OutgoingLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as sent. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-out/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7OutgoingLogFilePattern)"
    "
    .. _hl7OutgoingErrorLogFilePattern:

    :ref:`HL7 Outgoing Error Log File Pattern <hl7OutgoingErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as sent, when processing of sent HL7 messages fails. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-out-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7OutgoingErrorLogFilePattern)"
    "
    .. _hl7NoPatientCreateMessageType:

    :ref:`HL7 No Patient Create Message Type(s) <hl7NoPatientCreateMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of HL7 messages which are only processed, if there is already a Patient record in the database, which Patient ID matches the Patient ID in the PID or MRG segment of the message. Thus no new Patient record will be created by messages of the specified types. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7NoPatientCreateMessageType)"
    "
    .. _hl7NoPatientUpdateMessageType:

    :ref:`HL7 No Patient Update Message Type(s) <hl7NoPatientUpdateMessageType>`",string,"Patient record will be not be updated by HL7 messages of specified Message Type(s) (MessageType^TriggerEvent). May be overwritten by configured values for particular Archive HL7 Application.

    (hl7NoPatientUpdateMessageType)"
    "
    .. _hl7PatientArrivalMessageType:

    :ref:`HL7 Patient Arrival Message Type <hl7PatientArrivalMessageType>`",string,"Message Type of HL7 messages which triggers the change the status of Scheduled Procedure Steps associated with the Patient from SCHEDULED to ARRIVED. If absent, the status of Scheduled Procedure Steps will not be affected by HL7 ADT messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ADT^A10

    (hl7PatientArrivalMessageType)"
    "
    .. _dcmUnzipVendorDataToURI:

    :ref:`Unzip Vendor Data To URI <dcmUnzipVendorDataToURI>`",string,"Specifies URI of directory into which ZIP stream in Device Vendor Data attribute will be extracted

    (dcmUnzipVendorDataToURI)"
    "
    .. _dcmPurgeQueueMessagePollingInterval:

    :ref:`Purge Task Polling Interval <dcmPurgeQueueMessagePollingInterval>`",string,"Polling Interval for purging tasks in ISO-8601 duration format PnDTnHnMnS. If absent, there is no deletion

    (dcmPurgeQueueMessagePollingInterval)"
    "
    .. _dcmWadoSpoolDirectory:

    :ref:`Wado-RS Spool Directory <dcmWadoSpoolDirectory>`",string,"Path to Wado-RS spool directory used to aggregate uncompressed frames.

    (dcmWadoSpoolDirectory)"
    "
    .. _dcmRejectExpiredStudiesPollingInterval:

    :ref:`Reject Expired Studies Polling Interval <dcmRejectExpiredStudiesPollingInterval>`",string,"Polling Interval for rejecting expired Studies and Series in ISO-8601 duration format PnDTnHnMnS. If absent, neither expired Studies nor Series will be rejected automatically

    (dcmRejectExpiredStudiesPollingInterval)"
    "
    .. _dcmRejectExpiredStudiesSchedule:

    :ref:`Reject Expired Studies Schedule(s) <dcmRejectExpiredStudiesSchedule>`",string,"Limits Rejection of Expired Studies to specified times in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday).

    (dcmRejectExpiredStudiesSchedule)"
    "
    .. _dcmRejectExpiredStudiesFetchSize:

    :ref:`Reject Expired Studies Fetch Size <dcmRejectExpiredStudiesFetchSize>`",integer,"Maximal number of expired Studies fetched in one query; If absent, expired Studies will not be rejected automatically

    (dcmRejectExpiredStudiesFetchSize)"
    "
    .. _dcmRejectExpiredSeriesFetchSize:

    :ref:`Reject Expired Series Fetch Size <dcmRejectExpiredSeriesFetchSize>`",integer,"Maximal number of expired Series fetched in one query; If absent, expired Series will not be rejected automatically

    (dcmRejectExpiredSeriesFetchSize)"
    "
    .. _dcmRejectExpiredStudiesAETitle:

    :ref:`Reject Expired Studies AE Title <dcmRejectExpiredStudiesAETitle>`",string,"AE Title of Local Application Entity performing the automatic rejection of expired Studies and Series. If absent, neither expired Studies nor Series will be rejected automatically.

    (dcmRejectExpiredStudiesAETitle)"
    "
    .. _dcmStorePermissionServiceURL:

    :ref:`Store Permission Service URL <dcmStorePermissionServiceURL>`",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study by any AE. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http(s)://<store-permission-service-provider-host>:<store-permission-service-provider-port>/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030,urlencoded}. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceURL)"
    "
    .. _dcmStorePermissionServiceResponse:

    :ref:`Store Permission Service Response <dcmStorePermissionServiceResponse>`",string,"Emulate Store Permission Service Response on receive of the first object of a study by any AE. {<dicomTag>} will be replaced by the value of the attribute in the object. Only effective if no Store Permission Service URL is configured. Example: patientID={00100020},patientName={00100010},errorCode=0110H,errorComment=errorMessage. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceResponse)"
    "
    .. _dcmStorePermissionServiceResponsePattern:

    :ref:`Store Permission Service Response Pattern <dcmStorePermissionServiceResponsePattern>`",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" or '(?<=patientName=)[^null].*?(?=,)'. If absent, every success response will be treated as agreement for storage. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceResponsePattern)"
    "
    .. _dcmStorePermissionServiceErrorCommentPattern:

    :ref:`Store Permission Service Error Comment Pattern <dcmStorePermissionServiceErrorCommentPattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". If absent, ""Storage denied."" will be used as Error Comment. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceErrorCommentPattern)"
    "
    .. _dcmStorePermissionServiceErrorCodePattern:

    :ref:`Store Permission Service Error Code Pattern <dcmStorePermissionServiceErrorCodePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". If absent, the Error Code will be 0124H (Not Authorized). May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceErrorCodePattern)"
    "
    .. _dcmStorePermissionServiceExpirationDatePattern:

    :ref:`Store Permission Service Expiration Date Pattern <dcmStorePermissionServiceExpirationDatePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". If absent, locally configured Study Retention Policy Rules will be applied. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceExpirationDatePattern)"
    "
    .. _dcmStorePermissionCacheStaleTimeout:

    :ref:`Store Permission Cache Stale Timeout <dcmStorePermissionCacheStaleTimeout>`",string,"Maximal staleness of cached responses from Storage Permission Service in ISO-8601 duration format PnDTnHnMnS. If absent, cached responses are only removed on reaching the maximal cache size.

    (dcmStorePermissionCacheStaleTimeout)"
    "
    .. _dcmStorePermissionCacheSize:

    :ref:`Store Permission Cache Size <dcmStorePermissionCacheSize>`",integer,"Maximum number of cached responses from Storage Permission Service.

    (dcmStorePermissionCacheSize)"
    "
    .. _dcmMergeMWLCacheStaleTimeout:

    :ref:`Merge MWL Cache Stale Timeout <dcmMergeMWLCacheStaleTimeout>`",string,"Maximal staleness of Request Attributes extracted from matching DICOM MWL items in ISO-8601 duration format PnDTnHnMnS. If absent, cached Request Attributes are only removed on reaching the maximal cache size.

    (dcmMergeMWLCacheStaleTimeout)"
    "
    .. _dcmMergeMWLCacheSize:

    :ref:`Merge MWL Cache Size <dcmMergeMWLCacheSize>`",integer,"Maximum number of cached Request Attributes extracted from matching DICOM MWL items.

    (dcmMergeMWLCacheSize)"
    "
    .. _dcmStoreUpdateDBMaxRetries:

    :ref:`Store Update DB Maximum Number of Retries <dcmStoreUpdateDBMaxRetries>`",integer,"Maximum number of retries to update the database on storage.

    (dcmStoreUpdateDBMaxRetries)"
    "
    .. _dcmStoreUpdateDBMinRetryDelay:

    :ref:`Minimal Store Update DB Delay of Retry <dcmStoreUpdateDBMinRetryDelay>`",integer,"Minimal Delay in ms between retries to update the database on storage.

    (dcmStoreUpdateDBMinRetryDelay)"
    "
    .. _dcmStoreUpdateDBMaxRetryDelay:

    :ref:`Maximal Store Update DB Delay of Retry <dcmStoreUpdateDBMaxRetryDelay>`",integer,"Maximal Delay in ms between retries to update the database on storage.

    (dcmStoreUpdateDBMaxRetryDelay)"
    "
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:

    :ref:`Allow Rejection For Data Retention Policy Expired <dcmAllowRejectionForDataRetentionPolicyExpired>`",string,"Allow Rejection For Data Retention Policy Expired. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    NEVER

    ALWAYS

    EXPIRED_UNSET

    ONLY_EXPIRED

    (dcmAllowRejectionForDataRetentionPolicyExpired)"
    "
    .. _dcmAllowDeleteStudyPermanently:

    :ref:`Allow Delete Study permanently <dcmAllowDeleteStudyPermanently>`",string,"Allow to delete Study permanently. REJECTED = only already rejected Studies. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    ALWAYS

    REJECTED

    (dcmAllowDeleteStudyPermanently)"
    "
    .. _dcmAllowDeletePatient:

    :ref:`Allow Delete Patient <dcmAllowDeletePatient>`",string,"Allow permanent deletion of Patients. WITHOUT_STUDIES = only Patients without Studies.

    Enumerated values:

    NEVER

    ALWAYS

    WITHOUT_STUDIES

    (dcmAllowDeletePatient)"
    "
    .. _dcmPurgeStgCmtCompletedDelay:

    :ref:`Purge Storage Commitment Completed Delay <dcmPurgeStgCmtCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which results of completed Storage Commitment requests are purged. If absent, there is no deletion.

    (dcmPurgeStgCmtCompletedDelay)"
    "
    .. _dcmPurgeStgCmtPollingInterval:

    :ref:`Purge Storage Commitment Polling Interval <dcmPurgeStgCmtPollingInterval>`",string,"Polling Interval for purging Storage Commitment Results in ISO-8601 duration format PnDTnHnMnS. If absent, there is no deletion

    (dcmPurgeStgCmtPollingInterval)"
    "
    .. _dcmDefaultCharacterSet:

    :ref:`Default Character Set <dcmDefaultCharacterSet>`",string,"Value of Specific Character Set (0008,0005) added to Data Sets of C-STORE RQs and pending C-FIND RSPs without Specific Character Set (0008,0005) attribute received by any AE. May be overwritten by configured values for particular Archive Network AEs.

    (dcmDefaultCharacterSet)"
    "
    .. _dcmCharsetNameMapping:

    :ref:`DICOM Character Set Name Mapping(s) <dcmCharsetNameMapping>`",string,"Customize mapping of value of DICOM Specific Character Set (0008,0005) to named charset in format <value>=<charset name>. E.g.: ""ISO_IR 100=windows-1252"".

    (dcmCharsetNameMapping)"
    "
    .. _hl7CharsetNameMapping:

    :ref:`HL7 Character Set Name Mapping(s) <hl7CharsetNameMapping>`",string,"Add mapping of value of HL7 MSH-18 to named charset in format <value>=<charset name>. E.g.: ""Windows-1252=windows-1252"". Typically you will also have to specify the HL7 DICOM Character Set of the Archive HL7 Application to use for received HL7 messages with such Character Set.

    (hl7CharsetNameMapping)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`UPS Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) of created UPS by any Network AE, if the UPS Push SCU or UPS-RS User Agent does not provide a value for this attribute. If absent, the AE Title of the receiving AE will be used. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSEventSCU:

    :ref:`UPS Event SCU(s) <dcmUPSEventSCU>`",string,"AE Title of UPS Event SOP Class SCU, to which UPS Event Reports are sent - independently if the subscription was created by the N-ACTION DIMSE service, or by a corresponding UPS RESTful service. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUPSEventSCU)"
    "
    .. _dcmUPSEventSCUKeepAlive:

    :ref:`UPS Event SCU Keep Alive <dcmUPSEventSCUKeepAlive>`",integer,"Timeout in ms to keep associations to UPS Event SCUs alive. If absent, associations will not be reused for sending multiple UPS Event Reports to one UPS Event SCU. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUPSEventSCUKeepAlive)"
    "
    .. _dcmUPSEventWebSocketQueueSize:

    :ref:`UPS Event Web Socket Queue Size(s) <dcmUPSEventWebSocketQueueSize>`",string,"Indicates to queue UPS events to be sent to a particular Web Client identified by its Subscriber AET in case there is no open Web Socket connection to that client at the time of the event. Format: <aet>=<size>.

    (dcmUPSEventWebSocketQueueSize)"
    "
    .. _dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) <dcmRetrieveAET>`",string,"Specifies Retrieve AE Titles associated with received DICOM objects. If absent, the Called AE Title of the receiving AE will be used. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveAET)"
    "
    .. _dcmReturnRetrieveAET:

    :ref:`Return Retrieve AE Title(s) <dcmReturnRetrieveAET>`",string,"Retrieve AE Title returned in C-FIND and QIDO responses. If absent, the Retrieve AET associated with the archived entity will be returned. May be overwritten by configured values for particular Archive Network AEs.

    (dcmReturnRetrieveAET)"
    "
    .. _dcmMultipleStoreAssociations:

    :ref:`Multiple Store Associations(s) <dcmMultipleStoreAssociations>`",string,"Number of Storage Associations used for retrieve of Composite Objects. C-STORE SCP specific numbers can be specified by prefix '<AETitle>:'. If absent, only one Association will be used. Examples : 2 or STORESCP:3 May be supplemented by configured Multiple Store Associations for particular Archive Network AEs.

    (dcmMultipleStoreAssociations)"
    "
    .. _dcmExternalRetrieveAEDestination:

    :ref:`External Retrieve AE Destination <dcmExternalRetrieveAEDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to external retrieve AE. May be overwritten by configured values for particular Archive Network AEs.

    (dcmExternalRetrieveAEDestination)"
    "
    .. _dcmXDSiImagingDocumentSourceAETitle:

    :ref:`XDS-I Imaging Document Source AE Title <dcmXDSiImagingDocumentSourceAETitle>`",string,"AE Title of local Application Entity associated with XDS-I Imaging Document Source.

    (dcmXDSiImagingDocumentSourceAETitle)"
    "
    .. _dcmQueueTasksFetchSize:

    :ref:`Queue Tasks Fetch Size <dcmQueueTasksFetchSize>`",integer,"Maximal number of Tasks rescheduled or deleted or canceled in one transaction.

    (dcmQueueTasksFetchSize)"
    "
    .. _dcmRemapRetrieveURL:

    :ref:`Remap Retrieve URL <dcmRemapRetrieveURL>`",string,"Remap Retrieve URL used in QIDO-RS and WADO-RS Metadata responses. Optionally prefixed with ""[<http-client-host>]"". E.g.: ""[cache-proxy]http://cache-proxy:8080"". If absent or if the specified <http-client-host> does not match, scheme and server authority of the QIDO-RS or WADO-RS request URL are used.

    (dcmRemapRetrieveURL)"
    "
    .. _dcmProxyUpstreamURL:

    :ref:`Proxy Upstream URL <dcmProxyUpstreamURL>`",string,"URL for the upstream endpoint that shall be proxied.

    (dcmProxyUpstreamURL)"
    "
    .. _dcmCopyMoveUpdatePolicy:

    :ref:`Copy Move Update Policy <dcmCopyMoveUpdatePolicy>`",string,"Specifies update policy for attributes of the destination Study on Copy/Move of Instances from another Study. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    PRESERVE

    SUPPLEMENT

    MERGE

    OVERWRITE

    REPLACE

    (dcmCopyMoveUpdatePolicy)"
    "
    .. _dcmLinkMWLEntryUpdatePolicy:

    :ref:`Link MWL Entry Update Policy <dcmLinkMWLEntryUpdatePolicy>`",string,"Specifies update policy for Study attributes on Link of Instances of another Study with a MWL Entry referring an existing Study. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    PRESERVE

    SUPPLEMENT

    MERGE

    OVERWRITE

    REPLACE

    (dcmLinkMWLEntryUpdatePolicy)"
    "
    .. _dcmStorageVerificationPolicy:

    :ref:`Storage Verification Policy <dcmStorageVerificationPolicy>`",string,"DB_RECORD_EXISTS: only check for existence of DB records, OBJECT_EXISTS: check if object exists on Storage System, OBJECT_SIZE: check size of object on Storage System, OBJECT_FETCH: fetch object from Storage System), OBJECT_CHECKSUM: recalculate checksum of object on Storage System, S3_MD5SUM: check MD5 checksum of object on S3 Storage System. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    DB_RECORD_EXISTS

    OBJECT_EXISTS

    OBJECT_SIZE

    OBJECT_FETCH

    OBJECT_CHECKSUM

    S3_MD5SUM

    (dcmStorageVerificationPolicy)"
    "
    .. _dcmStorageVerificationUpdateLocationStatus:

    :ref:`Storage Verification Update Location Status <dcmStorageVerificationUpdateLocationStatus>`",boolean,"Indicates if the Status of the Location DB record shall be updated on Storage Verification accordingly. Not effective with Storage Verification Policy: DB_RECORD_EXISTS. False if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationUpdateLocationStatus)"
    "
    .. _dcmStorageVerificationStorageID:

    :ref:`Storage Verification Storage IDs(s) <dcmStorageVerificationStorageID>`",string,"Indicates that for successful Storage Verification the object must be stored on (one of) the specified Storage System. If absent, successful verification of the storage on any Storage System is sufficient. Not effective with Storage Validation Policy: DB_RECORD_EXISTS. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationStorageID)"
    "
    .. _dcmStorageVerificationAETitle:

    :ref:`Storage Verification AE Title <dcmStorageVerificationAETitle>`",string,"Archive AE Title used for scheduled Storage Verifications.

    (dcmStorageVerificationAETitle)"
    "
    .. _dcmStorageVerificationBatchID:

    :ref:`Storage Verification Batch ID <dcmStorageVerificationBatchID>`",string,"Batch ID of Storage Verification Tasks triggered by scheduler.

    (dcmStorageVerificationBatchID)"
    "
    .. _dcmStorageVerificationInitialDelay:

    :ref:`Storage Verification Initial Delay <dcmStorageVerificationInitialDelay>`",string,"Delay of first Storage Verification of a Series after it was received. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationInitialDelay)"
    "
    .. _dcmStorageVerificationPeriod:

    :ref:`Storage Verification Period <dcmStorageVerificationPeriod>`",string,"Period in which the storage of individual Series is verified. If absent, storage of individual Series are only verified once after configured Storage Verification Initial Delay.

    (dcmStorageVerificationPeriod)"
    "
    .. _dcmStorageVerificationMaxScheduled:

    :ref:`Maximal scheduled Storage Verifications <dcmStorageVerificationMaxScheduled>`",integer,"Maximal number of scheduled Storage Verification tasks on this device. Shall be set > 0 to distribute tasks over nodes of a clustered archive.

    (dcmStorageVerificationMaxScheduled)"
    "
    .. _dcmStorageVerificationPollingInterval:

    :ref:`Storage Verification Polling Interval <dcmStorageVerificationPollingInterval>`",string,"Polling Interval for Series scheduled for Storage Verification in ISO-8601 duration format PnDTnHnMnS.

    (dcmStorageVerificationPollingInterval)"
    "
    .. _dcmStorageVerificationSchedule:

    :ref:`Storage Verification Schedule(s) <dcmStorageVerificationSchedule>`",string,"Limits Storage Verification to specified times in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday).

    (dcmStorageVerificationSchedule)"
    "
    .. _dcmStorageVerificationFetchSize:

    :ref:`Storage Verification Fetch Size <dcmStorageVerificationFetchSize>`",integer,"Maximal number of Series scheduled for Storage Verification fetched by one query.

    (dcmStorageVerificationFetchSize)"
    "
    .. _dcmUpdateLocationStatusOnRetrieve:

    :ref:`Update Location Status on Retrieve <dcmUpdateLocationStatusOnRetrieve>`",boolean,"Indicates if the Status of the Location DB record shall be updated for objects failed to get fetched from storage on retrieve to MISSING_OBJECT or FAILED_TO_FETCH_OBJECT. May be overwritten by configured values for particular Archive Network AEs.

    (dcmUpdateLocationStatusOnRetrieve)"
    "
    .. _dcmStorageVerificationOnRetrieve:

    :ref:`Storage Verification on Retrieve <dcmStorageVerificationOnRetrieve>`",boolean,"Indicates if failures to fetch an object from Storage on retrieve shall trigger a Storage Verification of the whole Series. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorageVerificationOnRetrieve)"
    "
    .. _dcmCompressionAETitle:

    :ref:`Compression AE Title <dcmCompressionAETitle>`",string,"Archive AE Title used for delayed Compression.

    (dcmCompressionAETitle)"
    "
    .. _dcmCompressionPollingInterval:

    :ref:`Compression Polling Interval <dcmCompressionPollingInterval>`",string,"Polling Interval for Series to be compressed in ISO-8601 duration format PnDTnHnMnS.

    (dcmCompressionPollingInterval)"
    "
    .. _dcmCompressionThreads:

    :ref:`Compression Threads <dcmCompressionThreads>`",integer,"Number of Threads used for Compression.

    (dcmCompressionThreads)"
    "
    .. _dcmCompressionSchedule:

    :ref:`Compression Schedule(s) <dcmCompressionSchedule>`",string,"Limits compression to specified times in format 'hour=[0-23] dayOfWeek=[0-6]' (0=Sunday)

    (dcmCompressionSchedule)"
    "
    .. _dcmCompressionFetchSize:

    :ref:`Compression Fetch Size <dcmCompressionFetchSize>`",integer,"Maximal number of Series fetched for compression by one query.

    (dcmCompressionFetchSize)"
    "
    .. _dcmChangeAccessControlIDPollingInterval:

    :ref:`Change Access Control ID Polling Interval <dcmChangeAccessControlIDPollingInterval>`",string,"Polling Interval for Studies or Series to change its assigned Access Control ID according configured Change Access Control ID rules in ISO-8601 duration format PnDTnHnMnS.

    (dcmChangeAccessControlIDPollingInterval)"
    "
    .. _dcmDiffTaskProgressUpdateInterval:

    :ref:`Diff Task Progress Update Interval <dcmDiffTaskProgressUpdateInterval>`",string,"Interval of updating Diff Tasks in process for progress monitoring; disabled if absent.

    (dcmDiffTaskProgressUpdateInterval)"
    "
    .. _dcmPatientVerificationPDQServiceID:

    :ref:`Patient Verification PDQ Service ID <dcmPatientVerificationPDQServiceID>`",string,"ID of Patient Demographics Query Service used for Verification of Patient Demographic. If absent, no Patient Verification will be performed.

    (dcmPatientVerificationPDQServiceID)"
    "
    .. _dcmPatientVerificationPollingInterval:

    :ref:`Patient Verification Polling Interval <dcmPatientVerificationPollingInterval>`",string,"Patient Verification Polling Interval. If absent, no Patient Verification will be performed.

    (dcmPatientVerificationPollingInterval)"
    "
    .. _dcmPatientVerificationFetchSize:

    :ref:`Patient Verification Fetch Size <dcmPatientVerificationFetchSize>`",integer,"Maximal number of Patients fetched for Patient Verification in one query.

    (dcmPatientVerificationFetchSize)"
    "
    .. _dcmPatientVerificationAdjustIssuerOfPatientID:

    :ref:`Patient Verification Adjust Issuer of Patient ID <dcmPatientVerificationAdjustIssuerOfPatientID>`",boolean,"Indicates if the Issuer Of Patient ID shall be adjusted to the value returned by the PDQ Service.

    (dcmPatientVerificationAdjustIssuerOfPatientID)"
    "
    .. _dcmPatientVerificationPeriod:

    :ref:`Patient Verification Period <dcmPatientVerificationPeriod>`",string,"Period in which Patient Demographic will be verified. If absent, Patient Verification will not be renewed for Patients verified in the past.

    (dcmPatientVerificationPeriod)"
    "
    .. _dcmPatientVerificationPeriodOnNotFound:

    :ref:`Patient Verification Period Not Found <dcmPatientVerificationPeriodOnNotFound>`",string,"Period in which Patient Demographic will be retried for Patients which were not found by the configured PDQ Service on last attempt. If absent, Patient Verification will not be retried for Patients not found in the past.

    (dcmPatientVerificationPeriodOnNotFound)"
    "
    .. _dcmPatientVerificationRetryInterval:

    :ref:`Patient Verification Retry Interval <dcmPatientVerificationRetryInterval>`",string,"Patient Verification Retry Interval in which failed attempts to verify Patient Demographics against the PDQ Service configured by Patient Verification PDQ Service ID will be retried until the maximal number of retries specified by Patient Verification Max Retries is reached. If absent, failed Patient Verification attempts will not be retried.

    (dcmPatientVerificationRetryInterval)"
    "
    .. _dcmPatientVerificationMaxRetries:

    :ref:`Patient Verification Maximum Number of Retries <dcmPatientVerificationMaxRetries>`",integer,"Maximum number of retries to verify Patient Demographics against the PDQ Service configured by dcmPatientVerificationPDQServiceID. Only effective if Patient Verification Retry Interval is specified. -1 = forever.

    (dcmPatientVerificationMaxRetries)"
    "
    .. _dcmPatientVerificationMaxStaleness:

    :ref:`Patient Verification Maximum Staleness <dcmPatientVerificationMaxStaleness>`",string,"Indicates to renew the verification of Patient Demographics on receive of objects for a patient, if previous executed verification is older than specified interval. If absent, Patient Verification on receive of objects is disabled.

    (dcmPatientVerificationMaxStaleness)"
    "
    .. _dcmSupplementIssuerFetchSize:

    :ref:`Supplement Issuer Fetch Size <dcmSupplementIssuerFetchSize>`",integer,"Limit result set of DB query for matching Patients by RESTful service for supplementing Issuer of Patient ID.

    (dcmSupplementIssuerFetchSize)"
    "
    .. _dcmUpdateCharsetFetchSize:

    :ref:`Update Charset Fetch Size <dcmUpdateCharsetFetchSize>`",integer,"Limit result set of DB query for matching Patients by RESTful service to update the character set of Patient Attributes in DB BLOB fields.

    (dcmUpdateCharsetFetchSize)"
    "
    .. _hl7ADTSendingApplication:

    :ref:`HL7 ADT Sending Application <hl7ADTSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 ADT messages to synchronize external systems about performed Patient Information updates. If absent, synchronization of external systems by HL7 ADT messages is disabled.

    (hl7ADTSendingApplication)"
    "
    .. _hl7ADTReceivingApplication:

    :ref:`HL7 ADT Receiving Application(s) <hl7ADTReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 ADT messages to synchronize external systems about performed Patient Information updates. If absent, synchronization of external systems by HL7 ADT messages is disabled.

    (hl7ADTReceivingApplication)"
    "
    .. _hl7PSUSendingApplication:

    :ref:`HL7 Procedure Status Update Sending Application <hl7PSUSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 Procedure Status Update. HL7 Procedure Status Update disabled, if absent. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUSendingApplication)"
    "
    .. _hl7PSUReceivingApplication:

    :ref:`HL7 Procedure Status Update Receiving Application(s) <hl7PSUReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 Procedure Status Update. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUReceivingApplication)"
    "
    .. _hl7PSUTaskPollingInterval:

    :ref:`HL7 Procedure Status Update Task Polling Interval <hl7PSUTaskPollingInterval>`",string,"Polling Interval for HL7 Procedure Status Update Tasks in ISO-8601 duration format PnDTnHnMnS. Disabled, if absent.

    (hl7PSUTaskPollingInterval)"
    "
    .. _hl7PSUTaskFetchSize:

    :ref:`HL7 Procedure Status Update Tasks Fetch Size <hl7PSUTaskFetchSize>`",integer,"Maximal number of HL7 Procedure Status Update Tasks fetched in one query.

    (hl7PSUTaskFetchSize)"
    "
    .. _hl7PSUAction:

    :ref:`HL7 Procedure Status Update Action(s) <hl7PSUAction>`",string,"Specifies HL7 Procedure Status Update action: SEND_NOTIFICATION (= send HL7 Procedure Status Update Notification message to configured HL7 Procedure Status Update Receiving Applications), UPDATE_MWL_STATUS (= set Scheduled Procedure Step Status of MWL Items associated to STUDY to COMPLETED). May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    SEND_NOTIFICATION

    UPDATE_MWL_STATUS

    (hl7PSUAction)"
    "
    .. _hl7PSUTrigger:

    :ref:`HL7 Procedure Status Update Trigger(s) <hl7PSUTrigger>`",string,"Specifies trigger events to send a HL7 Procedure Status Update notification to HL7 Receivers configured by HL7 Procedure Status Update Receiving Application. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    STUDY_RECEIVED

    MPPS_RECEIVED

    REJECTION_NOTE_RECEIVED

    FIRST_OBJECT_OF_STUDY_RECEIVED

    (hl7PSUTrigger)"
    "
    .. _hl7PSUDelay:

    :ref:`HL7 Procedure Status Update Delay <hl7PSUDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUDelay)"
    "
    .. _hl7PSUStudyTemplateURI:

    :ref:`HL7 Procedure Status Update Study Template URI <hl7PSUStudyTemplateURI>`",string,"URL of XSL style sheet to create HL7v2 message to notify configured HL7 receivers about changes of the Status of requested Procedures triggered by received Study. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUStudyTemplateURI)"
    "
    .. _hl7PSUTimeout:

    :ref:`HL7 Procedure Status Update Timeout <hl7PSUTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMnS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUTimeout)"
    "
    .. _hl7PSUOnTimeout:

    :ref:`HL7 Procedure Status Update On Timeout <hl7PSUOnTimeout>`",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUOnTimeout)"
    "
    .. _hl7PSUMppsTemplateURI:

    :ref:`HL7 Procedure Status Update MPPS Template URI <hl7PSUMppsTemplateURI>`",string,"URL of XSL style sheet to create HL7v2 message to notify configured HL7 receivers about changes of the Status of requested Procedures triggered by MPPS. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUMppsTemplateURI)"
    "
    .. _hl7PSUCondition:

    :ref:`HL7 Procedure Status Update Conditions(s) <hl7PSUCondition>`",string,"Restrict notification of configured HL7 Procedure Status Update Receiving Applications about Procedure Status Update by conditions on attributes of received composite object in format {key}[!]={value}. Refer `applicability, format and some examples <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUCondition)"
    "
    .. _hl7PSUForRequestedProcedure:

    :ref:`HL7 Procedure Status Update for Requested Procedure <hl7PSUForRequestedProcedure>`",boolean,"Restrict notification of configured HL7 Procedure Status Update Receiving Applications about Procedure Status Update to existence of Scheduled Procedure Steps of a Requested Procedure (MWL Items in the DB) with matching Study Instance UID. May be overwritten by configured value for particular Archive Network AEs.

    (hl7PSUForRequestedProcedure)"
    "
    .. _hl7PSUTemplateParam:

    :ref:`HL7 Procedure Status Update Template Parameters(s) <hl7PSUTemplateParam>`",string,"XSLT parameters in format {attributeID}={value} passed to style sheet specified by HL7 Procedure Status Update MPPS Template URI or HL7 Procedure Status Update Study Template URI. {attributeID} inside of {value} will be replaced by the value of that attribute in the original dataset. E.g.: 'RequestedProcedureID={StudyInstanceUID,hash}' or 'AccessionNumber={0020000D,hash}'. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUTemplateParam)"
    "
    .. _hl7PSUMessageType:

    :ref:`HL7 Procedure Status Update Message Type <hl7PSUMessageType>`",string,"Message Type of HL7 Procedure Status Update message. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    OMG_O19

    ORU_R01

    OMI_O23

    (hl7PSUMessageType)"
    "
    .. _hl7PSUPIDPV1:

    :ref:`HL7 Procedure Status Update PID PV1 <hl7PSUPIDPV1>`",boolean,"Indicates to include a Patient Identification (PID) and a Patient Visit (PV1) segment in the HL7 Procedure Status Update message. Implicitly set, if HL7 Procedure Status Message Type = ORU_R01. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUPIDPV1)"
    "
    .. _hl7PSUMWL:

    :ref:`HL7 Procedure Status Update MWL <hl7PSUMWL>`",boolean,"Specifies if the Status of MWL Items in the DB is updated to COMPLETED for a received study after the configured HL7 Procedure Status Update Delay. Implicitly set to true, if notification to HL7 receivers is configured, triggered by received studies associated with MWL. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUMWL)"
    "
    .. _hl7PSUMWLMatchingKey:

    :ref:`HL7 Procedure Status Update MWL Matching Key <hl7PSUMWLMatchingKey>`",string,"Specifies attribute of received object to lookup MWL Item whose status is to be updated to COMPLETED. Only applicable is 'HL7 Procedure Status Update MWL' is configured as or implicitly set to true. May be overwritten by configured values for particular Archive Network AEs.

    Enumerated values:

    AccessionNumber

    StudyInstanceUID

    (hl7PSUMWLMatchingKey)"
    "
    .. _hl7TrackChangedPatientID:

    :ref:`HL7 Track Changed Patient ID <hl7TrackChangedPatientID>`",boolean,"Enable to keep track of the prior Patient ID on a change of the Patient ID by HL7 ADT^A47 or by the RESTful Patient Update Service.

    (hl7TrackChangedPatientID)"
    "
    .. _hl7UseNullValue:

    :ref:`Use HL7 Null Value <hl7UseNullValue>`",boolean,"Specifies if HL7 v2 null values (specified in segment field as `|""""|`) are used in sent HL7 messages for not present or empty entity attributes. Required to unset entity attributes at the remote HL7 Application. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7UseNullValue)"
    "
    .. _hl7VeterinaryUsePatientName:

    :ref:`HL7 Veterinary use Patient Name <hl7VeterinaryUsePatientName>`",boolean,"Indicates to force veterinary use of Patient Names on mapping HL7 PID fields to DICOM attributes: only use the first two components of PID.5 as DICOM Patient Name; if PID.5 only contains one component, use that value as given name, and the first component of PID.9 as family name of the DICOM Patient Name. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7VeterinaryUsePatientName)"
    "
    .. _hl7PrimaryAssigningAuthorityOfPatientID:

    :ref:`HL7 Primary Assigning Authority of Patient ID <hl7PrimaryAssigningAuthorityOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search primary qualified patient identifier in the list of identifiers in PID-3 / MRG.1. This qualified patient identifier shall be used on the root dataset. If absent, by default the first patient identifier pair in PID-3 / MRG.1 shall be used as primary patient identifier on root dataset. If none of the qualified patient identifiers in the list match with the configured issuer, archive server log shall contain a log INFO message and by default the first qualified patient identifier in PID-3 / MRG.1 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}]. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7PrimaryAssigningAuthorityOfPatientID)"
    "
    .. _hl7OtherPatientIDs:

    :ref:`HL7 Other Patient IDs <hl7OtherPatientIDs>`",string,"Specifies inclusion policy for patient identifiers in PID-3 / MRG-1 of HL7 message in Other Patient IDs Sequence (0010,1002). May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ALL

    NONE

    OTHER

    (hl7OtherPatientIDs)"
    "
    .. _hl7OrderMissingStudyIUIDPolicy:

    :ref:`HL7 Order Missing Study Instance UID Policy <hl7OrderMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Order messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    REJECT

    GENERATE

    ACCESSION_BASED

    (hl7OrderMissingStudyIUIDPolicy)"
    "
    .. _hl7OrderMissingAdmissionIDPolicy:

    :ref:`HL7 Order Missing Admission ID Policy <hl7OrderMissingAdmissionIDPolicy>`",string,"Specifies policy on incoming HL7 Order messages without a value for PID-18 Patient Account Number nor field PV1-19 Visit Number. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ACCEPT

    REJECT

    ACCESSION_AS_ADMISSION

    (hl7OrderMissingAdmissionIDPolicy)"
    "
    .. _hl7ImportReportMissingStudyIUIDPolicy:

    :ref:`HL7 Import Report Missing Study Instance UID Policy <hl7ImportReportMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Import Report (ORU) messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    REJECT

    GENERATE

    ACCESSION_BASED

    (hl7ImportReportMissingStudyIUIDPolicy)"
    "
    .. _hl7ImportReportMissingAdmissionIDPolicy:

    :ref:`HL7 Import Report Missing Admission ID Policy <hl7ImportReportMissingAdmissionIDPolicy>`",string,"Specifies policy on incoming HL7 ImportReport (ORU) messages without a value for PID-18 Patient Account Number nor field PV1-19 Visit Number. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    ACCEPT

    REJECT

    ACCESSION_AS_ADMISSION

    (hl7ImportReportMissingAdmissionIDPolicy)"
    "
    .. _hl7ImportReportMissingStudyIUIDCFindSCP:

    :ref:`HL7 Import Report Missing Study Instance UID C-FIND SCP <hl7ImportReportMissingStudyIUIDCFindSCP>`",string,"AE Title of external C-FIND SCP to query for missing Study Instance UID in incoming HL7 Import Report (ORU) messages by given Accession Number. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7ImportReportMissingStudyIUIDCFindSCP)"
    "
    .. _hl7ImportReportAdjustIUID:

    :ref:`HL7 Import Report Adjust Instance UID <hl7ImportReportAdjustIUID>`",string,"Specifies adjustment of Series and SOP Instances UIDs returned by XSLT on incoming HL7 Import Report (ORU) messages. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    NONE

    APPEND_HASH_OF_STUDY_INSTANCE_UID

    (hl7ImportReportAdjustIUID)"
    "
    .. _hl7ReferredMergedPatientPolicy:

    :ref:`HL7 Referred Merged Patient Policy <hl7ReferredMergedPatientPolicy>`",string,"Specifies policy on incoming HL7 messages referring an already merged Patient. Refer `HL7 Referred Merged Patient Policy <https://github.com/dcm4che/dcm4chee-arc-light/wiki/HL7-Referred-Merged-Patient-Policy>`_ meanings. May be overwritten by configured values for particular Archive HL7 Application.

    Enumerated values:

    REJECT

    IGNORE

    IGNORE_DUPLICATE_MERGE

    ACCEPT_INVERSE_MERGE

    (hl7ReferredMergedPatientPolicy)"
    "
    .. _hl7DicomCharacterSet:

    :ref:`HL7 Dicom Character Set <hl7DicomCharacterSet>`",string,"Indicates to use specified Value of Specific Character Set (0008,0005) in Data Sets transcoded from received HL7 messages. Use Value corresponding to Character Set of the HL7 message specified by MSH-18 if absent.

    (hl7DicomCharacterSet)"
    "
    .. _dcmRejectionNoteStorageAET:

    :ref:`Rejection Note Storage AE title <dcmRejectionNoteStorageAET>`",string,"Title of Archive Application Entity, of which first configured Object Storage will be used for storing Rejection Notes generated either by IOCM-RS services or by Delete Expired Studies Scheduler. If absent, for IOCM services the Object Storage configured for Archive AE referred in the IOCM-RS request will be used, or for Delete Expired Studies Scheduler the Object Storage configured for Reject Expired Studies AE will be used.

    (dcmRejectionNoteStorageAET)"
    "
    .. _dcmUIConfigurationDeviceName:

    :ref:`UI Configuration Device Name <dcmUIConfigurationDeviceName>`",string,"Specifies the device name containing the Archive UI Configuration.

    (dcmUIConfigurationDeviceName)"
    "
    .. _dcmCSVUploadChunkSize:

    :ref:`CSV Upload Chunk Size <dcmCSVUploadChunkSize>`",integer,"Number of CSV file upload tasks to be processed in one chunk.

    (dcmCSVUploadChunkSize)"
    "
    .. _dcmValidateUID:

    :ref:`Validate UID <dcmValidateUID>`",boolean,"Indicates if UIDs shall be validated or not.

    (dcmValidateUID)"
    "
    .. _dcmRelationalQueryNegotiationLenient:

    :ref:`Relational Query Negotiation Lenient <dcmRelationalQueryNegotiationLenient>`",boolean,"Indicates to accept C-FIND RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRelationalQueryNegotiationLenient)"
    "
    .. _dcmRelationalRetrieveNegotiationLenient:

    :ref:`Relational Retrieve Negotiation Lenient <dcmRelationalRetrieveNegotiationLenient>`",boolean,"Indicates to accept C-MOVE and C-GET RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRelationalRetrieveNegotiationLenient)"
    "
    .. _dcmRestrictRetrieveSilently:

    :ref:`Restrict Retrieve Silently <dcmRestrictRetrieveSilently>`",boolean,"Indicates if the set of requested objects to retrieve shall be silently (=without counting not transferred object as failures) restricted according the Transfer Capabilities of the Retrieve Destination. Otherwise the number of requested objects for which no Transfer Capability is configured for the Retrieve Destination and therefore are not retrieved is counted as failures. Only effective, if the Retrieve Destination has configured at least one Transfer Capability with SCP role. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRestrictRetrieveSilently)"
    "
    .. _dcmSchedulerMinStartDelay:

    :ref:`Scheduler Minimum Start Delay <dcmSchedulerMinStartDelay>`",integer,"Minimal delay in s to start schedulers on system start up.

    (dcmSchedulerMinStartDelay)"
    "
    .. _dcmRejectConflictingPatientAttribute:

    :ref:`Reject Conflicting Patient Attribute(s) <dcmRejectConflictingPatientAttribute>`",string,"DICOM Tag of Patient Attribute which have to match in received objects with the value in previous received objects with equal Patient ID to be accepted. May be overwritten by configured value for particular Archive Network AEs.

    (dcmRejectConflictingPatientAttribute)"
    "
    .. _dcmStowRetiredTransferSyntax:

    :ref:`STOW Retired Transfer Syntax <dcmStowRetiredTransferSyntax>`",boolean,"Store received JPEG Full Progression, Non-Hierarchical JPEG images in DICOM images with corresponding (retired) Transfer Syntax UID 1.2.840.10008.1.2.4.55. Otherwise set 1.2.840.10008.1.2.4.50 (= JPEG Baseline) or 1.2.840.10008.1.2.4.51 (= JPEG Extended) as Transfer Syntax UID of the stored DICOM image, without transcoding to JPEG Baseline or JPEG Extended, but including the JPEG image as received. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowRetiredTransferSyntax)"
    "
    .. _dcmStowExcludeAPPMarkers:

    :ref:`STOW Exclude Application Markers <dcmStowExcludeAPPMarkers>`",boolean,"Indicates if APP markers in JPEG images received in STOW-RS Metadata and Bulkdata requests shall be excluded from the JPEG bit streams encapsulated in created DICOM instances. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowExcludeAPPMarkers)"
    "
    .. _dcmStowQuicktime2MP4:

    :ref:`STOW Quicktime to MP4 <dcmStowQuicktime2MP4>`",boolean,"Indicates if QuickTime containers received in STOW-RS Metadata and Bulkdata requests shall be converted to MP4 containers encapsulated in created DICOM instances. The conversion requires that ffmpeg is installed and the ffmpeg CLI utility is available in the PATH. Otherwise Quicktime containers will get encapsulated in the stored DICOM object verbatim, with a declared DICOM MPEG-4 Transfer Syntax which reflects the encoding of the video stream in the container, but contradicts the actual container format. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowQuicktime2MP4)"
    "
    .. _dcmStowMaxFragmentLength:

    :ref:`STOW Maximum Fragment Length <dcmStowMaxFragmentLength>`",integer,"Maximum length of data fragments of encapsulated JPEG/MPEG stream in stored DICOM object. If the received JPEG/MPEG stream exceeds that value, it will be split into several fragments, using a Fragmentable Encapsulated Transfer Syntax. Valid range: 1024..4294967294. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStowMaxFragmentLength)"
    "
    .. _dcmChangeRequesterAET:

    :ref:`Change Requester AET <dcmChangeRequesterAET>`",string,"Indicates change requester AET in rejections triggered by archive. May be overwritten by configured values for particular Archive Network AEs.

    (dcmChangeRequesterAET)"
    "
    .. _dcmFilterByIssuerOfPatientID:

    :ref:`Filter by Issuer of Patient ID <dcmFilterByIssuerOfPatientID>`",boolean,"Filter by Issuer of Patient ID even if no matching key for Patient ID is specified. May be overwritten by configured value for particular Archive Network AEs.

    (dcmFilterByIssuerOfPatientID)"
    "
    .. _dcmMatchSOPClassOnInstanceLevel:

    :ref:`Match SOP Class on Instance level <dcmMatchSOPClassOnInstanceLevel>`",boolean,"Indicates to consider the SOP Class UID on Instance level for calculation of matches with SOP Classes in Study (0008,0062); otherwise rely on stored SOP Class UID on Series level, which may result in missing matches if one Series includes Instances of different SOP Classes. May be overwritten by configured value for particular Archive Network AEs.

    (dcmMatchSOPClassOnInstanceLevel)"
    "
    .. _dcmKeyValueRetentionPollingInterval:

    :ref:`Key Value Retention Polling Interval <dcmKeyValueRetentionPollingInterval>`",string,"Polling Interval for Key Value pairs which retention period expired in ISO-8601 duration format PnDTnHnMnS. If absent, Key Value pairs will not get deleted automatically.

    (dcmKeyValueRetentionPollingInterval)"
    "
    .. _dcmKeyValueRetentionFetchSize:

    :ref:`Key Value Retention Fetch Size <dcmKeyValueRetentionFetchSize>`",integer,"Limit result set of DB query for Key Value pairs which retention period expired; 100 if absent

    (dcmKeyValueRetentionFetchSize)"
    "
    .. _dcmKeyValueRetentionPeriod:

    :ref:`Key Value Retention Period <dcmKeyValueRetentionPeriod>`",string,"Retention period in ISO-8601 duration format PnDTnHnMn.nS of stored Key Value pairs. If absent, Key Value pairs will not get deleted automatically.

    (dcmKeyValueRetentionPeriod)"
    "
    .. _dcmUPSUpdateWithoutTransactionUID:

    :ref:`UPS Update Without Transaction UID <dcmUPSUpdateWithoutTransactionUID>`",boolean,"Indicates to permit an UPS Pull SCU or UPS-RS Web client to update or change the state of an UPS workitem in state IN PROCESS without specifying a Transaction UID. May be overwritten by configured value for particular Archive Network AEs.

    (dcmUPSUpdateWithoutTransactionUID)"
    "
    .. _dcmUPS2MWLCFindSCP:

    :ref:`UPS 2 MWL C-Find SCP <dcmUPS2MWLCFindSCP>`",boolean,"Indicates to feed Modality Worklist C-FIND SCP service from managed list of Unified Procedure Step (UPS) instances mapped to MWL items. May be overwritten by configured value for particular Archive Network AEs.

    (dcmUPS2MWLCFindSCP)"
    "
    .. _dcmUPS2MWLScheduledStationNameCode:

    :ref:`UPS 2 MWL Scheduled Station Name Code(s) <dcmUPS2MWLScheduledStationNameCode>`",string,"Defines list of Station Name Codes in format (CV, CSD, ""CM"") used to map Scheduled Station AE Titles (0040,0001) in MWL C-FIND RQ/RSPs to Station Name Code Sequence (0040,4025) items of Unified Procedure Step (UPS) instances.

    (dcmUPS2MWLScheduledStationNameCode)"
    "
    .. _dcmUPS2MWLScheduledStationNameCodeValueAsAET:

    :ref:`UPS 2 MWL Scheduled Station Name Code Value as AE Title <dcmUPS2MWLScheduledStationNameCodeValueAsAET>`",boolean,"Indicates to map Code Value (0008,0101) - instead Code Meaning (0008,0104) - of Scheduled Station Name Code Sequence (0040,4025) items of Unified Procedure Step (UPS) instances to Scheduled Station AE Titles (0040,0001) of MWL C-FIND RQ/RSPs.

    (dcmUPS2MWLScheduledStationNameCodeValueAsAET)"
    "
    .. _dcmQStarVerificationStorageID:

    :ref:`QStar Verification Storage ID <dcmQStarVerificationStorageID>`",string,"ID of QStar Tape File System to which objects were stored which Access State shall be verified. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationStorageID)"
    "
    .. _dcmQStarVerificationPollingInterval:

    :ref:`QStar Verification Polling Interval <dcmQStarVerificationPollingInterval>`",string,"Polling Interval for Verification of Access State of objects stored on QStar Tape File System in ISO-8601 duration format PnDTnHnMnS. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationPollingInterval)"
    "
    .. _dcmQStarVerificationFetchSize:

    :ref:`QStar Verification Fetch Size <dcmQStarVerificationFetchSize>`",integer,"Limit result set of DB query for Verification of Access State of objects stored on QStar Tape File System; 100 if absent.

    (dcmQStarVerificationFetchSize)"
    "
    .. _dcmQStarVerificationDelay:

    :ref:`QStar Verification Delay <dcmQStarVerificationDelay>`",string,"Delay for Verification of Access State after objects stored on QStar Tape File System in ISO-8601 duration format PnDTnHnMnS. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationDelay)"
    "
    .. _dcmQStarVerificationURL:

    :ref:`QStar Verification URL <dcmQStarVerificationURL>`",string,"URL of QStar Archive Storage Manager WEB Services - including username and password (http://username:password@qstar.host:port/) - invoked for Verification of Access State after objects stored on QStar Tape File System. If absent, Access State of objects stored on QStar Tape File System will not be verified.

    (dcmQStarVerificationURL)"
    "
    .. _dcmQStarVerificationMockAccessState:

    :ref:`QStar Verification Mock Access State <dcmQStarVerificationMockAccessState>`",integer,"Indicates to mock invoke of QStar Archive Storage Manager (ASM) WEB Services by return of specified Access State (0 - ACCESS_STATE_NONE, 1 - ACCESS_STATE_EMPTY, 2 - ACCESS_STATE_UNSTABLE, 3 - ACCESS_STATE_STABLE, 4 - ACCESS_STATE_OUT_OF_CACHE, 5 - ACCESS_STATE_OFFLINE, -1 - simulate error response) for testing.

    Enumerated values:

    0

    1

    2

    3

    4

    5

    -1

    (dcmQStarVerificationMockAccessState)"
    "
    .. _dcmTrustedPatientIDPattern:

    :ref:`Trusted Patient ID Pattern(s) <dcmTrustedPatientIDPattern>`",string,"Regular Expression identifying trusted Patient IDs in HL7 v2 CX format: {Patient ID}^^^{Issuer of Patient ID}&{Universal Entity ID}&{Universal Entity ID Type} in received DICOM objects and HL7 messages. Only Patient IDs matching one of the specified patterns or Patient IDs qualified by an Assigning Authority matching one of the configured 'Trusted Issuers of Patient IDs' will be used for identifying the Patient. If neither this attribute nor any 'Trusted Issuers of Patient ID' is configured, all Patient IDs in received DICOM Objects and HL7 messages will be used for identifying the Patient.

    (dcmTrustedPatientIDPattern)"
    "
    .. _dcmTrustedIssuerOfPatientID:

    :ref:`Trusted Issuer of Patient ID(s) <dcmTrustedIssuerOfPatientID>`",string,"Trusted Assigning Authority of Patient IDs in received DICOM objects and HL7 messages. Only Patient IDs qualified by an Assigning Authority matching one of the specified values or Patient IDs matching one of the configured 'Trusted Patient ID Patterns' will be used for identifying the Patient. If neither this attribute nor dcmTrustedPatientIDPattern is configured, all Patient IDs in received DICOM Objects and HL7 messages will be used for identifying the Patient. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}].

    (dcmTrustedIssuerOfPatientID)"
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
    ":doc:`upsOnUPSCompleted` (s)",object,"UPS on UPS Completed Rules applied to UPS managed by any AE. May be supplemented by configured UPS on Store Rules for particular Archive Network AEs."
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

    :ref:`X-Road Property(s) <dcmXRoadProperty>`",string,"Properties for accessing Estonian National Patient Registry in format {name}={value}

    (dcmXRoadProperty)"
    "
    .. _dcmImpaxReportProperty:

    :ref:`Impax Report Property(s) <dcmImpaxReportProperty>`",string,"Properties for accessing Agfa Impax Report Service in format {name}={value}

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
