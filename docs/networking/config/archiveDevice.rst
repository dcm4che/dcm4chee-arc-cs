Archive Device
==============
DICOM Archive Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive Device Attributes (LDAP Object: dcmArchiveDevice)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Fuzzy Algorithm Class**",string,"Specifies Fuzzy Algorithm Implementation Class: 'org.dcm4che3.soundex.Soundex', 'org.dcm4che3.soundex.ESoundex', 'org.dcm4che3.soundex.ESoundex9', 'org.dcm4che3.soundex.Metaphone', 'org.dcm4che3.soundex.KPhonetik', 'org.dcm4che3.soundex.Phonem","
    .. _dcmFuzzyAlgorithmClass:

    dcmFuzzyAlgorithmClass_"
    "**Storage ID**",string,"Storage ID","
    .. _dcmStorageID:

    dcmStorageID_"
    "Metadata Storage ID",string,"ID of Storage on which Metadata is stored in JSON format - additionally to the complete DICOM composite object. If absent, metadata is not stored additionally","
    .. _dcmMetadataStorageID:

    dcmMetadataStorageID_"
    "Series Metadata Storage ID",string,"ID of Storage on which ZIP archives with aggregated Metadata of all instances of a Series is stored. If absent, no aggregated Series Metadata will be stored.","
    .. _dcmSeriesMetadataStorageID:

    dcmSeriesMetadataStorageID_"
    "Aggregate Series Metadata Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for storing aggregated Series Metadata on storage. If absent, no aggregated Series Metadata will be stored.","
    .. _dcmSeriesMetadataDelay:

    dcmSeriesMetadataDelay_"
    "Update Series Metadata Polling Interval",string,"Polling Interval for Series scheduled for Metadata update in ISO-8601 duration format PnDTnHnMn.nS. If absent, no aggregated Series Metadata will be stored.","
    .. _dcmSeriesMetadataPollingInterval:

    dcmSeriesMetadataPollingInterval_"
    "Update Series Metadata Fetch Size",integer,"Maximal number of Series scheduled for Metadata update fetched by one query; 100 if absent.","
    .. _dcmSeriesMetadataFetchSize:

    dcmSeriesMetadataFetchSize_"
    "Remove Instance Records Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for purging Instance Records from the DB. If absent, Instance Records will never be purged.","
    .. _dcmPurgeInstanceRecordsDelay:

    dcmPurgeInstanceRecordsDelay_"
    "Remove Instance Records Polling Interval",string,"Polling Interval for Series scheduled for purging Instance Records from the DB in ISO-8601 duration format PnDTnHnMn.nS. If absent, Instance Records will not be purged.","
    .. _dcmPurgeInstanceRecordsPollingInterval:

    dcmPurgeInstanceRecordsPollingInterval_"
    "Remove Instance Records Fetch Size",integer,"Maximal number of Series scheduled for purging Instance Records from the DB fetched by one query; 100 if absent.","
    .. _dcmPurgeInstanceRecordsFetchSize:

    dcmPurgeInstanceRecordsFetchSize_"
    "**Query/Retrieve View ID**",string,"Query/Retrieve View Identifier","
    .. _dcmQueryRetrieveViewID:

    dcmQueryRetrieveViewID_"
    "Overwrite Policy",string,"Overwrite Policy: NEVER, ALWAYS, SAME_SOURCE, SAME_SERIES or SAME_SOURCE_AND_SERIES. NEVER if absent.","
    .. _dcmOverwritePolicy:

    dcmOverwritePolicy_"
    "Accept Missing Patient ID",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. Enumerated values: YES, NO, CREATE. If absent, CREATE will be applied.","
    .. _dcmAcceptMissingPatientID:

    dcmAcceptMissingPatientID_"
    "Accept Conflicting Patient ID",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. Enumerated values: YES, NO, MERGED(= accept prior Patient IDs). If absent, MERGED will be applied.","
    .. _dcmAcceptConflictingPatientID:

    dcmAcceptConflictingPatientID_"
    "Bulk Data Spool Directory",string,"Path to Bulk Data Spool Directory","
    .. _dcmBulkDataSpoolDirectory:

    dcmBulkDataSpoolDirectory_"
    "Hide SPS with Status(s)",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP","
    .. _dcmHideSPSWithStatusFromMWL:

    dcmHideSPSWithStatusFromMWL_"
    "Validate Calling AE Hostname",boolean,"Validate Calling AE Hostname or IP Address of Association requestors; disabled if absent","
    .. _dcmValidateCallingAEHostname:

    dcmValidateCallingAEHostname_"
    "Person Name Component Order Insensitive Matching",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names; disabled if absent","
    .. _dcmPersonNameComponentOrderInsensitiveMatching:

    dcmPersonNameComponentOrderInsensitiveMatching_"
    "Send Pending C-Get",boolean,"Enables pending C-GET responses; disabled if absent","
    .. _dcmSendPendingCGet:

    dcmSendPendingCGet_"
    "Send Pending C-Move Interval",string,"Interval of pending C-MOVE responses in ISO-8601 duration format PnDTnHnMn.nS; disabled if absent","
    .. _dcmSendPendingCMoveInterval:

    dcmSendPendingCMoveInterval_"
    "Wado Supported SR Classes(s)",string,"Supported SR SOP classes for WADO retrieval","
    .. _dcmWadoSupportedSRClasses:

    dcmWadoSupportedSRClasses_"
    "Wado SR2 Html Template URI",string,"Specifies URI for the style sheet used to render structured reports to html","
    .. _dcmWadoSR2HtmlTemplateURI:

    dcmWadoSR2HtmlTemplateURI_"
    "Wado SR2 Text Template URI",string,"Specifies URI for the style sheet used to render structured reports to plain text","
    .. _dcmWadoSR2TextTemplateURI:

    dcmWadoSR2TextTemplateURI_"
    "Qido Max Number Of Results",integer,"Maximal number of return results by QIDO-RS Service. 0 (=unlimited) if absent","
    .. _dcmQidoMaxNumberOfResults:

    dcmQidoMaxNumberOfResults_"
    "Mpps Forward Destination(s)",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ","
    .. _dcmFwdMppsDestination:

    dcmFwdMppsDestination_"
    "Ian Destination(s)",string,"Destination to send IAN N-CREATE RQ","
    .. _dcmIanDestination:

    dcmIanDestination_"
    "IAN Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an IAN for a received study is sent to configured IAN destinations. If absent, IANs are triggered by received MPPS","
    .. _dcmIanDelay:

    dcmIanDelay_"
    "IAN Timeout",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent","
    .. _dcmIanTimeout:

    dcmIanTimeout_"
    "IAN On Timeout",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced is exceeded; just stop check for completeness on timeout if absent","
    .. _dcmIanOnTimeout:

    dcmIanOnTimeout_"
    "IAN Task Polling Interval",string,"Polling Interval for IAN Tasks in ISO-8601 duration format PnDTnHnMn.nS. IAN disabled, if absent","
    .. _dcmIanTaskPollingInterval:

    dcmIanTaskPollingInterval_"
    "IAN Task Fetch Size",integer,"Maximal number of IAN Tasks scheduled in one transaction; 100 if absent","
    .. _dcmIanTaskFetchSize:

    dcmIanTaskFetchSize_"
    "Fallback C-Move SCP",string,"AE Title of external C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not managed by this archive","
    .. _dcmFallbackCMoveSCP:

    dcmFallbackCMoveSCP_"
    "Fallback C-Move SCP Destination",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to the external C-MOVE SCP specified by dcmFallbackCMoveSCP","
    .. _dcmFallbackCMoveSCPDestination:

    dcmFallbackCMoveSCPDestination_"
    "Fallback C-Move SCP Study Older Than",string,"Specifies threshold for Study Date in format YYYYMMDD for marking received Studies as (potential) incomplete to enforce the retrieve from configured dcmFallbackCMoveSCP","
    .. _dcmFallbackCMoveSCPStudyOlderThan:

    dcmFallbackCMoveSCPStudyOlderThan_"
    "Fallback C-Move SCP Leading C-Find SCP",string,"AE Title of external C-FIND SCP for Verification of Number of Instances retrieved from external C-MOVE SCP specified by dcmFallbackCMoveSCP.","
    .. _dcmFallbackCMoveSCPLeadingCFindSCP:

    dcmFallbackCMoveSCPLeadingCFindSCP_"
    "Fallback C-Move SCP Retries",integer,"Maximal number of retries to retrieve not available objects from C-MOVE SCP configured by dcmFallbackCMoveSCP. -1 = forever. 0 if absent","
    .. _dcmFallbackCMoveSCPRetries:

    dcmFallbackCMoveSCPRetries_"
    "Alternative C-Move SCP",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage","
    .. _dcmAltCMoveSCP:

    dcmAltCMoveSCP_"
    "Export Task Polling Interval",string,"Export Task Polling Interval in ISO-8601 duration format PnDTnHnMn.nS","
    .. _dcmExportTaskPollingInterval:

    dcmExportTaskPollingInterval_"
    "Export Task Fetch Size",integer,"Maximal number of Export Tasks scheduled in one transaction; 5 if absent","
    .. _dcmExportTaskFetchSize:

    dcmExportTaskFetchSize_"
    "Purge Storage Polling Interval",string,"Polling Interval for deleting objects in ISO-8601 duration format PnDTnHnMn.nS","
    .. _dcmPurgeStoragePollingInterval:

    dcmPurgeStoragePollingInterval_"
    "Purge Storage Fetch Size",integer,"Maximal number of objects to delete in one task; 100 if absent","
    .. _dcmPurgeStorageFetchSize:

    dcmPurgeStorageFetchSize_"
    "Delete Study Batch Size",integer,"number of studies to delete from the Storage System, if the usable space fall below configured Usable Space, before checking the usable space again; 10 if absent","
    .. _dcmDeleteStudyBatchSize:

    dcmDeleteStudyBatchSize_"
    "Delete Patient On Delete Last Study",boolean,"Specifies if a Patient shall be deleted on deletion of its last study; disabled if absent.","
    .. _dcmDeletePatientOnDeleteLastStudy:

    dcmDeletePatientOnDeleteLastStudy_"
    "Delete Rejected Polling Interval",string,"Polling Interval for deleting rejected instances from the DB in ISO-8601 duration format PnDTnHnMn.nS","
    .. _dcmDeleteRejectedPollingInterval:

    dcmDeleteRejectedPollingInterval_"
    "Delete Rejected Fetch Size",integer,"Maximal number of rejected instances to delete from the DB in one task; 100 if absent","
    .. _dcmDeleteRejectedFetchSize:

    dcmDeleteRejectedFetchSize_"
    "Maximum Access Time Staleness",string,"Maximal staleness of recorded study accession time in ISO-8601 duration format PnDTnHnMn.nS. update of the access time disabled, if absent.","
    .. _dcmMaxAccessTimeStaleness:

    dcmMaxAccessTimeStaleness_"
    "AE Cache Stale Timeout",string,"Maximal staleness of cached AE in ISO-8601 duration format PnDTnHnMn.nS. If absent, cached AE entries will not be refetched from LDAP.","
    .. _dcmAECacheStaleTimeout:

    dcmAECacheStaleTimeout_"
    "Leading C-Find SCP Query Cache Stale Timeout",string,"Maximal staleness of cached Patient and Study attributes fetched from leading C-Find SCP in ISO-8601 duration format PnDTnHnMn.nS. If absent, cache Study attributes are only removed on reaching the maximal cache size.","
    .. _dcmLeadingCFindSCPQueryCacheStaleTimeout:

    dcmLeadingCFindSCPQueryCacheStaleTimeout_"
    "Leading C-Find SCP Query Cache Size",integer,"Maximum number of cached Patient and Study attributes fetched from leading C-Find SCP; 10 if absent","
    .. _dcmLeadingCFindSCPQueryCacheSize:

    dcmLeadingCFindSCPQueryCacheSize_"
    "Audit Spool Directory",string,"Path to Audit Service Spool Directory used to aggregate Audit Messages. If absent, audit messages written to temporary location in server","
    .. _dcmAuditSpoolDirectory:

    dcmAuditSpoolDirectory_"
    "Audit Polling Interval",string,"Polling Interval for aggregating Audit Messages in ISO-8601 duration format PnDTnHnMn.nS. Audit Message aggregation disabled, if absent.","
    .. _dcmAuditPollingInterval:

    dcmAuditPollingInterval_"
    "Audit Aggregate Duration",string,"Audit Message Aggregation Duration in ISO-8601 duration format PnDTnHnMn.nS. Audit Message aggregation disabled, if absent.","
    .. _dcmAuditAggregateDuration:

    dcmAuditAggregateDuration_"
    "STOW-RS Spool Directory",string,"Path to Directory used by STOW-RS Service to spool Bulkdata of XML/JSON Metadata and Bulk Data Request Messages.","
    .. _dcmStowSpoolDirectory:

    dcmStowSpoolDirectory_"
    "HL7 Patient Update Template URI",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service.","
    .. _hl7PatientUpdateTemplateURI:

    hl7PatientUpdateTemplateURI_"
    "HL7 Import Report Template URI",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR.","
    .. _hl7ImportReportTemplateURI:

    hl7ImportReportTemplateURI_"
    "HL7 Schedule Procedure Template URI",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items.","
    .. _hl7ScheduleProcedureTemplateURI:

    hl7ScheduleProcedureTemplateURI_"
    "HL7 Log File Pattern",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging.","
    .. _hl7LogFilePattern:

    hl7LogFilePattern_"
    "HL7 Error Log File Pattern",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging.","
    .. _hl7ErrorLogFilePattern:

    hl7ErrorLogFilePattern_"
    "Unzip Vendor Data To URI",string,"Specifies URI of directory into which ZIP stream in Device Vendor Data attribute will be extracted","
    .. _dcmUnzipVendorDataToURI:

    dcmUnzipVendorDataToURI_"
    "Purge Queue Messages Polling Interval",string,"Polling Interval for purging queue messages in ISO-8601 duration format PnDTnHnMn.nS. If absent, there is no deletion","
    .. _dcmPurgeQueueMessagePollingInterval:

    dcmPurgeQueueMessagePollingInterval_"
    "Wado-RS Spool Directory",string,"Path to Wado-RS spool directory used to aggregate uncompressed frames. If absent, aggregation done in temp directory.","
    .. _dcmWadoSpoolDirectory:

    dcmWadoSpoolDirectory_"
    "Reject Expired Studies Polling Interval",string,"Polling Interval for rejecting expired Studies and Series in ISO-8601 duration format PnDTnHnMn.nS. If absent, neither expired Studies nor Series will be rejected automatically","
    .. _dcmRejectExpiredStudiesPollingInterval:

    dcmRejectExpiredStudiesPollingInterval_"
    "Reject Expired Studies Polling Start Time",string,"Time when the polling interval for rejecting expired Studies and Series starts in ISO-8601 time format [hh][mm][ss]. Archive start time if absent.","
    .. _dcmRejectExpiredStudiesPollingStartTime:

    dcmRejectExpiredStudiesPollingStartTime_"
    "Reject Expired Studies Fetch Size",integer,"Maximal number of expired Studies fetched in one query; If absent, expired Studies will not be rejected automatically","
    .. _dcmRejectExpiredStudiesFetchSize:

    dcmRejectExpiredStudiesFetchSize_"
    "Reject Expired Series Fetch Size",integer,"Maximal number of expired Series fetched in one query; If absent, expired Series will not be rejected automatically","
    .. _dcmRejectExpiredSeriesFetchSize:

    dcmRejectExpiredSeriesFetchSize_"
    "Reject Expired Studies AE Title",string,"AE Title of Local Application Entity performing the automatic rejection of expired Studies and Series. If absent, neither expired Studies nor Series will be rejected automatically.","
    .. _dcmRejectExpiredStudiesAETitle:

    dcmRejectExpiredStudiesAETitle_"
    "Store Permission Service URL",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http://host.name/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030}","
    .. _dcmStorePermissionServiceURL:

    dcmStorePermissionServiceURL_"
    "Store Permission Service Response Pattern",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" . If absent, every success response will be treated as agreement for storage.","
    .. _dcmStorePermissionServiceResponsePattern:

    dcmStorePermissionServiceResponsePattern_"
    "Store Permission Cache Stale Timeout",string,"Maximal staleness of cached responses from Storage Permission Service in ISO-8601 duration format PnDTnHnMn.nS. If absent, cached responses are only removed on reaching the maximal cache size.","
    .. _dcmStorePermissionCacheStaleTimeout:

    dcmStorePermissionCacheStaleTimeout_"
    "Store Permission Cache Size",integer,"Maximum number of cached responses from Storage Permission Service; 10 if absent","
    .. _dcmStorePermissionCacheSize:

    dcmStorePermissionCacheSize_"
    "Merge MWL Cache Stale Timeout",string,"Maximal staleness of Request Attributes extracted from matching DICOM MWL items in ISO-8601 duration format PnDTnHnMn.nS. If absent, cached Request Attributes are only removed on reaching the maximal cache size.","
    .. _dcmMergeMWLCacheStaleTimeout:

    dcmMergeMWLCacheStaleTimeout_"
    "Merge MWL Cache Size",integer,"Maximum number of cached Request Attributes extracted from matching DICOM MWL items; 10 if absent","
    .. _dcmMergeMWLCacheSize:

    dcmMergeMWLCacheSize_"
    "Store Update DB Maximum Number of Retries",integer,"Maximum number of retries to update the database on storage; 1 if absent","
    .. _dcmStoreUpdateDBMaxRetries:

    dcmStoreUpdateDBMaxRetries_"
    "Store Update DB Maximum Delay of Retry",integer,"Maximum delay in ms of retry to update the database on storage; 1000 if absent","
    .. _dcmStoreUpdateDBMaxRetryDelay:

    dcmStoreUpdateDBMaxRetryDelay_"
    "Allow Rejection For Data Retention Policy Expired",string,"Allow Rejection For Data Retention Policy Expired : NEVER, ALWAYS, STUDY_RETENTION_POLICY. If absent, STUDY_RETENTION_POLICY will be applied.","
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:

    dcmAllowRejectionForDataRetentionPolicyExpired_"
    "Allow Delete Study permanently",string,"Allow to delete Study permanently. Enumerated values: ALWAYS, REJECTED (= only already rejected Studies). If absent, REJECTED will be applied.","
    .. _dcmAllowDeleteStudyPermanently:

    dcmAllowDeleteStudyPermanently_"
    "Store Permission Service Expiration Date Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". If absent, locally configured Study Retention Policy Rules will be applied.","
    .. _dcmStorePermissionServiceExpirationDatePattern:

    dcmStorePermissionServiceExpirationDatePattern_"
    "Show Patient Info In System Log",string,"Specifies if Patient Information is shown as plain text or hashed in system logs. Enumerated values. PLAIN_TEXT, HASH_NAME, HASH_NAME_AND_ID. PLAIN_TEXT if absent.","
    .. _dcmShowPatientInfoInSystemLog:

    dcmShowPatientInfoInSystemLog_"
    "Show Patient Info In Audit Log",string,"Specifies if Patient Information is shown as plain text or hashed in emitted audit messages. Enumerated values. PLAIN_TEXT, HASH_NAME, HASH_NAME_AND_ID. PLAIN_TEXT if absent.","
    .. _dcmShowPatientInfoInAuditLog:

    dcmShowPatientInfoInAuditLog_"
    "Purge Storage Commitment Completed Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which results of completed Storage Commitment requests are purged. If absent, there is no deletion.","
    .. _dcmPurgeStgCmtCompletedDelay:

    dcmPurgeStgCmtCompletedDelay_"
    "Purge Storage Commitment Polling Interval",string,"Polling Interval for purging Storage Commitment Results in ISO-8601 duration format PnDTnHnMn.nS. If absent, there is no deletion","
    .. _dcmPurgeStgCmtPollingInterval:

    dcmPurgeStgCmtPollingInterval_"
    "Default Character Set",string,"Value of Specific Character Set (0008,0005) added to Data Sets without Specific Character Set (0008,0005) attribute received by the Network AE.","
    .. _dcmDefaultCharacterSet:

    dcmDefaultCharacterSet_"
    "Store Permission Service Error Comment Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". If absent, the Error Comment will be ""Storage denied"".","
    .. _dcmStorePermissionServiceErrorCommentPattern:

    dcmStorePermissionServiceErrorCommentPattern_"
    "Store Permission Service Error Code Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". If absent, the Error Code will be 0124H (Not Authorized).","
    .. _dcmStorePermissionServiceErrorCodePattern:

    dcmStorePermissionServiceErrorCodePattern_"
    "Retrieve AE Title(s)",string,"AE Title associated with Network AE","
    .. _dcmRetrieveAET:

    dcmRetrieveAET_"
    "External Retrieve AE Destination",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to external retrieve AE.","
    .. _dcmExternalRetrieveAEDestination:

    dcmExternalRetrieveAEDestination_"
    ":doc:`attributeFilter` (s)",object,"Specifies Attributes stored in the database","
    .. _dcmAttributeFilter:

    dcmAttributeFilter_"
    ":doc:`metadataFilter` (s)",object,"Named Attribute Filter for WADO-RS Metadata requests.","
    .. _dcmMetadataFilter:

    dcmMetadataFilter_"
    "Remap Retrieve URL",string,"Remap Retrieve URL used in QIDO-RS and WADO-RS Metadata responses. Optionally prefixed with ""[<http-client-host>]"". E.g.: ""[cache-proxy]http://cache-proxy:8080"". If absent or if the specified <http-client-host> does not match, scheme and server authority of the QIDO-RS or WADO-RS request URL are used.","
    .. _dcmRemapRetrieveURL:

    dcmRemapRetrieveURL_"
    "Audit Record Repository URL",string,"Access URL of Audit Record Repository. E.g. http://kibana:5601","
    .. _dcmAuditRecordRepositoryURL:

    dcmAuditRecordRepositoryURL_"
    "HL7 Procedure Status Update Sending Application",string,"Application|Facility name of Sending Application for HL7 Procedure Status Update. HL7 Procedure Status Update disabled.","
    .. _hl7PSUSendingApplication:

    hl7PSUSendingApplication_"
    "HL7 Procedure Status Update Receiving Application(s)",string,"Application|Facility name of Receiving Application for HL7 Procedure Status Update.","
    .. _hl7PSUReceivingApplication:

    hl7PSUReceivingApplication_"
    "HL7 Procedure Status Update Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS.","
    .. _hl7PSUDelay:

    hl7PSUDelay_"
    "HL7 Procedure Status Update MWL",boolean,"Specifies if the Status of MWL Items in the DB is updated to COMPLETED for a received study after the configured HL7 Procedure Status Update Delay. Disabled, if absent.","
    .. _hl7PSUMWL:

    hl7PSUMWL_"
    "HL7 Procedure Status Update Timeout",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent.","
    .. _hl7PSUTimeout:

    hl7PSUTimeout_"
    "HL7 Procedure Status Update On Timeout",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded; just stop check for completeness on timeout if absent.","
    .. _hl7PSUOnTimeout:

    hl7PSUOnTimeout_"
    "HL7 Procedure Status Update Task Polling Interval",string,"Polling Interval for HL7 Procedure Status Update Tasks in ISO-8601 duration format PnDTnHnMn.nS. Disabled, if absent.","
    .. _hl7PSUTaskPollingInterval:

    hl7PSUTaskPollingInterval_"
    "HL7 Procedure Status Update Tasks Fetch Size",integer,"Maximal number of HL7 Procedure Status Update Tasks fetched in one query; 100 if absent","
    .. _hl7PSUTaskFetchSize:

    hl7PSUTaskFetchSize_"
    ":doc:`storage` (s)",object,"Specifies Storage System","
    .. _dcmStorage:

    dcmStorage_"
    ":doc:`queryRetrieveView` (s)",object,"Specifies behavior on Rejection Note Stored","
    .. _dcmQueryRetrieveView:

    dcmQueryRetrieveView_"
    ":doc:`queue` (s)",object,"Managed JMS Queue","
    .. _dcmQueue:

    dcmQueue_"
    ":doc:`exporter` (s)",object,"Exporter Descriptor","
    .. _dcmExporter:

    dcmExporter_"
    ":doc:`exportRule` (s)",object,"Export Rule","
    .. _dcmExportRule:

    dcmExportRule_"
    ":doc:`rsForwardRule` (s)",object,"RESTful Forward Rule","
    .. _dcmRSForwardRule:

    dcmRSForwardRule_"
    ":doc:`archiveCompressionRule` (s)",object,"Archive Compression rule","
    .. _dcmArchiveCompressionRule:

    dcmArchiveCompressionRule_"
    ":doc:`archiveAttributeCoercion` (s)",object,"Archive Attribute Coercion of received/sent DIMSE","
    .. _dcmArchiveAttributeCoercion:

    dcmArchiveAttributeCoercion_"
    ":doc:`rejectionNote` (s)",object,"Specifies behavior on Rejection Note Stored","
    .. _dcmRejectionNote:

    dcmRejectionNote_"
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policy","
    .. _dcmStudyRetentionPolicy:

    dcmStudyRetentionPolicy_"
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by any AE","
    .. _dcmStoreAccessControlIDRule:

    dcmStoreAccessControlIDRule_"
    ":doc:`idGenerator` (s)",object,"ID Generator","
    .. _dcmIDGenerator:

    dcmIDGenerator_"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rule","
    .. _hl7ForwardRule:

    hl7ForwardRule_"
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed","
    .. _hl7OrderScheduledStation:

    hl7OrderScheduledStation_"
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages","
    .. _hl7OrderSPSStatus:

    hl7OrderSPSStatus_"

.. toctree::

    attributeFilter
    metadataFilter
    storage
    queryRetrieveView
    queue
    exporter
    exportRule
    rsForwardRule
    archiveCompressionRule
    archiveAttributeCoercion
    rejectionNote
    studyRetentionPolicy
    storeAccessControlIDRule
    idGenerator
    hl7ForwardRule
    hl7OrderScheduledStation
    hl7OrderSPSStatus
