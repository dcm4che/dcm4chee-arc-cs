Archive Device
==============
DICOM Archive Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Device Attributes (LDAP Object: dcmArchiveDevice)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmFuzzyAlgorithmClass:

    :ref:`Fuzzy Algorithm Class (dcmFuzzyAlgorithmClass) <dcmFuzzyAlgorithmClass>`",string,"Specifies Fuzzy Algorithm Implementation Class. Enumerated values: org.dcm4che3.soundex.Soundex, org.dcm4che3.soundex.ESoundex, org.dcm4che3.soundex.ESoundex9, org.dcm4che3.soundex.Metaphone, org.dcm4che3.soundex.KPhonetik or org.dcm4che3.soundex.Phonem"
    "
    .. _dcmSeriesMetadataStorageID:

    :ref:`Series Metadata Storage ID(s) (dcmSeriesMetadataStorageID) <dcmSeriesMetadataStorageID>`",string,"ID of Storage on which ZIP archives with aggregated Metadata of all instances of a Series is stored. Multiple Storage Systems may be configured. If absent, no aggregated Series Metadata will be stored."
    "
    .. _dcmSeriesMetadataDelay:

    :ref:`Aggregate Series Metadata Delay (dcmSeriesMetadataDelay) <dcmSeriesMetadataDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for storing aggregated Series Metadata on storage. If absent, no aggregated Series Metadata will be stored."
    "
    .. _dcmSeriesMetadataPollingInterval:

    :ref:`Update Series Metadata Polling Interval (dcmSeriesMetadataPollingInterval) <dcmSeriesMetadataPollingInterval>`",string,"Polling Interval for Series scheduled for Metadata update in ISO-8601 duration format PnDTnHnMn.nS. If absent, no aggregated Series Metadata will be stored."
    "
    .. _dcmSeriesMetadataFetchSize:

    :ref:`Update Series Metadata Fetch Size (dcmSeriesMetadataFetchSize) <dcmSeriesMetadataFetchSize>`",integer,"Maximal number of Series scheduled for Metadata update fetched by one query."
    "
    .. _dcmPurgeInstanceRecords:

    :ref:`Purge Instance Records (dcmPurgeInstanceRecords) <dcmPurgeInstanceRecords>`",boolean,"Indicates that Instance Records may be purged from the DB."
    "
    .. _dcmPurgeInstanceRecordsDelay:

    :ref:`Purge Instance Records Delay (dcmPurgeInstanceRecordsDelay) <dcmPurgeInstanceRecordsDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for purging Instance Records from the DB. May be overwritten by configured values for particular Archive Network AEs. Only effective, if Purge Instance Records = true."
    "
    .. _dcmPurgeInstanceRecordsPollingInterval:

    :ref:`Purge Instance Records Polling Interval (dcmPurgeInstanceRecordsPollingInterval) <dcmPurgeInstanceRecordsPollingInterval>`",string,"Polling Interval for Series scheduled for purging Instance Records from the DB in ISO-8601 duration format PnDTnHnMn.nS. Only effective, if Purge Instance Records = true."
    "
    .. _dcmPurgeInstanceRecordsFetchSize:

    :ref:`Purge Instance Records Fetch Size (dcmPurgeInstanceRecordsFetchSize) <dcmPurgeInstanceRecordsFetchSize>`",integer,"Maximal number of Series scheduled for purging Instance Records from the DB fetched by one query. Only effective, if Purge Instance Records = true."
    "
    .. _dcmQueryRetrieveViewID:

    :ref:`Query/Retrieve View ID (dcmQueryRetrieveViewID) <dcmQueryRetrieveViewID>`",string,"Query/Retrieve View Identifier. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmOverwritePolicy:

    :ref:`Overwrite Policy (dcmOverwritePolicy) <dcmOverwritePolicy>`",string,"Overwrite Policy. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: NEVER, ALWAYS, SAME_SOURCE, SAME_SERIES or SAME_SOURCE_AND_SERIES"
    "
    .. _dcmAcceptMissingPatientID:

    :ref:`Accept Missing Patient ID (dcmAcceptMissingPatientID) <dcmAcceptMissingPatientID>`",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: YES, NO or CREATE"
    "
    .. _dcmAcceptConflictingPatientID:

    :ref:`Accept Conflicting Patient ID (dcmAcceptConflictingPatientID) <dcmAcceptConflictingPatientID>`",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: YES, NO or MERGED"
    "
    .. _dcmBulkDataSpoolDirectory:

    :ref:`Bulk Data Spool Directory (dcmBulkDataSpoolDirectory) <dcmBulkDataSpoolDirectory>`",string,"Path to Bulk Data Spool Directory. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmHideSPSWithStatusFromMWL:

    :ref:`Hide SPS with Status(s) (dcmHideSPSWithStatusFromMWL) <dcmHideSPSWithStatusFromMWL>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: SCHEDULED, ARRIVED, READY, STARTED, DEPARTED, CANCELLED, DISCONTINUED or COMPLETED"
    "
    .. _dcmValidateCallingAEHostname:

    :ref:`Validate Calling AE Hostname (dcmValidateCallingAEHostname) <dcmValidateCallingAEHostname>`",boolean,"Validate Calling AE Hostname or IP Address of Association requestors. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmPersonNameComponentOrderInsensitiveMatching:

    :ref:`Person Name Component Order Insensitive Matching (dcmPersonNameComponentOrderInsensitiveMatching) <dcmPersonNameComponentOrderInsensitiveMatching>`",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmSendPendingCGet:

    :ref:`Send Pending C-Get (dcmSendPendingCGet) <dcmSendPendingCGet>`",boolean,"Enables pending C-GET responses. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmSendPendingCMoveInterval:

    :ref:`Send Pending C-Move Interval (dcmSendPendingCMoveInterval) <dcmSendPendingCMoveInterval>`",string,"Interval of pending C-MOVE responses in ISO-8601 duration format PnDTnHnMn.nS; disabled if absent. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmWadoSupportedSRClasses:

    :ref:`Wado Supported SR Classes(s) (dcmWadoSupportedSRClasses) <dcmWadoSupportedSRClasses>`",string,"Supported SR SOP classes for WADO retrieval"
    "
    .. _dcmWadoSR2HtmlTemplateURI:

    :ref:`Wado SR2 Html Template URI (dcmWadoSR2HtmlTemplateURI) <dcmWadoSR2HtmlTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to html. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmWadoSR2TextTemplateURI:

    :ref:`Wado SR2 Text Template URI (dcmWadoSR2TextTemplateURI) <dcmWadoSR2TextTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to plain text. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmQueryFetchSize:

    :ref:`Query Fetch Size (dcmQueryFetchSize) <dcmQueryFetchSize>`",integer,"Number of rows fetched from the database at once by the Query Service."
    "
    .. _dcmQueryMaxNumberOfResults:

    :ref:`Query Max Number Of Results (dcmQueryMaxNumberOfResults) <dcmQueryMaxNumberOfResults>`",integer,"Maximal number of return results by C-FIND SCP. If the number of matches extends the limit, the C-FIND request will be refused. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmQidoMaxNumberOfResults:

    :ref:`Qido Max Number Of Results (dcmQidoMaxNumberOfResults) <dcmQidoMaxNumberOfResults>`",integer,"Maximal number of return results by QIDO-RS Service. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmFwdMppsDestination:

    :ref:`Mpps Forward Destination(s) (dcmFwdMppsDestination) <dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmIanDestination:

    :ref:`Ian Destination(s) (dcmIanDestination) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmIanDelay:

    :ref:`IAN Delay (dcmIanDelay) <dcmIanDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an IAN for a received study is sent to configured IAN destinations. If absent, IANs are triggered by received MPPS. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmIanTimeout:

    :ref:`IAN Timeout (dcmIanTimeout) <dcmIanTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmIanOnTimeout:

    :ref:`IAN On Timeout (dcmIanOnTimeout) <dcmIanOnTimeout>`",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced is exceeded. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmIanTaskPollingInterval:

    :ref:`IAN Task Polling Interval (dcmIanTaskPollingInterval) <dcmIanTaskPollingInterval>`",string,"Polling Interval for IAN Tasks in ISO-8601 duration format PnDTnHnMn.nS. IAN disabled, if absent"
    "
    .. _dcmIanTaskFetchSize:

    :ref:`IAN Task Fetch Size (dcmIanTaskFetchSize) <dcmIanTaskFetchSize>`",integer,"Maximal number of IAN Tasks scheduled in one transaction."
    "
    .. _dcmSpanningCFindSCP:

    :ref:`Spanning C-Find SCP (dcmSpanningCFindSCP) <dcmSpanningCFindSCP>`",string,"AE Title of external C-FIND SCP to forward C-FIND RQs and backward responses according configured Spanning C-Find SCP Policy. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmSpanningCFindSCPPolicy:

    :ref:`Spanning C-Find SCP Policy (dcmSpanningCFindSCPPolicy) <dcmSpanningCFindSCPPolicy>`",string,"Specifies policy for combining matches returned from configured Spanning C-Find SCP with matching entries from the archive DB. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: SUPPLEMENT, MERGE or REPLACE"
    "
    .. _dcmSpanningCFindSCPRetrieveAET:

    :ref:`Spanning C-Find SCP Retrieve AE Title(s) (dcmSpanningCFindSCPRetrieveAET) <dcmSpanningCFindSCPRetrieveAET>`",string,"Specifies Retrieve AE Title(s) in returned matches from Spanning C-Find SCP. Keep original Retrieve AE Title(s) returned by Spanning C-Find SCP if absent. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmFallbackCMoveSCP:

    :ref:`Fallback C-Move SCP (dcmFallbackCMoveSCP) <dcmFallbackCMoveSCP>`",string,"AE Title of external C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not managed by this archive. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmFallbackCMoveSCPDestination:

    :ref:`Fallback C-Move SCP Destination (dcmFallbackCMoveSCPDestination) <dcmFallbackCMoveSCPDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to the external C-MOVE SCP specified by dcmFallbackCMoveSCP"
    "
    .. _dcmFallbackCMoveSCPStudyOlderThan:

    :ref:`Fallback C-Move SCP Study Older Than (dcmFallbackCMoveSCPStudyOlderThan) <dcmFallbackCMoveSCPStudyOlderThan>`",string,"Specifies threshold for Study Date in format YYYYMMDD for marking received Studies as (potential) incomplete to enforce the retrieve from configured dcmFallbackCMoveSCP"
    "
    .. _dcmFallbackCMoveSCPLeadingCFindSCP:

    :ref:`Fallback C-Move SCP Leading C-Find SCP (dcmFallbackCMoveSCPLeadingCFindSCP) <dcmFallbackCMoveSCPLeadingCFindSCP>`",string,"AE Title of external C-FIND SCP for Verification of Number of Instances retrieved from external C-MOVE SCP specified by dcmFallbackCMoveSCP."
    "
    .. _dcmFallbackCMoveSCPRetries:

    :ref:`Fallback C-Move SCP Retries (dcmFallbackCMoveSCPRetries) <dcmFallbackCMoveSCPRetries>`",integer,"Maximal number of retries to retrieve not available objects from C-MOVE SCP configured by dcmFallbackCMoveSCP. -1 = forever."
    "
    .. _dcmAltCMoveSCP:

    :ref:`Alternative C-Move SCP (dcmAltCMoveSCP) <dcmAltCMoveSCP>`",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage"
    "
    .. _dcmExportTaskPollingInterval:

    :ref:`Export Task Polling Interval (dcmExportTaskPollingInterval) <dcmExportTaskPollingInterval>`",string,"Export Task Polling Interval in ISO-8601 duration format PnDTnHnMn.nS"
    "
    .. _dcmExportTaskFetchSize:

    :ref:`Export Task Fetch Size (dcmExportTaskFetchSize) <dcmExportTaskFetchSize>`",integer,"Maximal number of Export Tasks scheduled in one transaction."
    "
    .. _dcmPurgeStoragePollingInterval:

    :ref:`Purge Storage Polling Interval (dcmPurgeStoragePollingInterval) <dcmPurgeStoragePollingInterval>`",string,"Polling Interval for deleting objects in ISO-8601 duration format PnDTnHnMn.nS"
    "
    .. _dcmPurgeStorageFetchSize:

    :ref:`Purge Storage Fetch Size (dcmPurgeStorageFetchSize) <dcmPurgeStorageFetchSize>`",integer,"Maximal number of objects to delete in one task."
    "
    .. _dcmDeleteStudyBatchSize:

    :ref:`Delete Study Batch Size (dcmDeleteStudyBatchSize) <dcmDeleteStudyBatchSize>`",integer,"number of studies to delete from the Storage System, if the usable space fall below configured Usable Space, before checking the usable space again."
    "
    .. _dcmDeletePatientOnDeleteLastStudy:

    :ref:`Delete Patient On Delete Last Study (dcmDeletePatientOnDeleteLastStudy) <dcmDeletePatientOnDeleteLastStudy>`",boolean,"Specifies if a Patient shall be deleted on deletion of its last study."
    "
    .. _dcmDeleteRejectedPollingInterval:

    :ref:`Delete Rejected Polling Interval (dcmDeleteRejectedPollingInterval) <dcmDeleteRejectedPollingInterval>`",string,"Polling Interval for deleting rejected instances from the DB in ISO-8601 duration format PnDTnHnMn.nS"
    "
    .. _dcmDeleteRejectedFetchSize:

    :ref:`Delete Rejected Fetch Size (dcmDeleteRejectedFetchSize) <dcmDeleteRejectedFetchSize>`",integer,"Maximal number of rejected instances to delete from the DB in one task."
    "
    .. _dcmMaxAccessTimeStaleness:

    :ref:`Maximum Access Time Staleness (dcmMaxAccessTimeStaleness) <dcmMaxAccessTimeStaleness>`",string,"Maximal staleness of recorded study accession time in ISO-8601 duration format PnDTnHnMn.nS. Update of the access time disabled, if absent."
    "
    .. _dcmAECacheStaleTimeout:

    :ref:`AE Cache Stale Timeout (dcmAECacheStaleTimeout) <dcmAECacheStaleTimeout>`",string,"Maximal staleness of cached AE in ISO-8601 duration format PnDTnHnMn.nS. If absent, cached AE entries will not be refetched from LDAP."
    "
    .. _dcmLeadingCFindSCPQueryCacheStaleTimeout:

    :ref:`Leading C-Find SCP Query Cache Stale Timeout (dcmLeadingCFindSCPQueryCacheStaleTimeout) <dcmLeadingCFindSCPQueryCacheStaleTimeout>`",string,"Maximal staleness of cached Patient and Study attributes fetched from leading C-Find SCP in ISO-8601 duration format PnDTnHnMn.nS. If absent, cache Study attributes are only removed on reaching the maximal cache size."
    "
    .. _dcmLeadingCFindSCPQueryCacheSize:

    :ref:`Leading C-Find SCP Query Cache Size (dcmLeadingCFindSCPQueryCacheSize) <dcmLeadingCFindSCPQueryCacheSize>`",integer,"Maximum number of cached Patient and Study attributes fetched from leading C-Find SCP."
    "
    .. _dcmAuditSpoolDirectory:

    :ref:`Audit Spool Directory (dcmAuditSpoolDirectory) <dcmAuditSpoolDirectory>`",string,"Path to Audit Service Spool Directory."
    "
    .. _dcmAuditPollingInterval:

    :ref:`Audit Polling Interval (dcmAuditPollingInterval) <dcmAuditPollingInterval>`",string,"Polling Interval for aggregating Audit Messages in ISO-8601 duration format PnDTnHnMn.nS. Audit Message aggregation disabled, if absent."
    "
    .. _dcmAuditAggregateDuration:

    :ref:`Audit Aggregate Duration (dcmAuditAggregateDuration) <dcmAuditAggregateDuration>`",string,"Audit Message Aggregation Duration in ISO-8601 duration format PnDTnHnMn.nS. Audit Message aggregation disabled, if absent."
    "
    .. _dcmAuditUnknownStudyInstanceUID:

    :ref:`Audit Unknown Study Instance UID (dcmAuditUnknownStudyInstanceUID) <dcmAuditUnknownStudyInstanceUID>`",string,"Indicates study instance uid value to be sent in audit message when not known."
    "
    .. _dcmAuditUnknownPatientID:

    :ref:`Audit Unknown Patient ID (dcmAuditUnknownPatientID) <dcmAuditUnknownPatientID>`",string,"Indicates patient id value to be sent in audit message when not known."
    "
    .. _dcmShowPatientInfoInSystemLog:

    :ref:`Show Patient Info In System Log (dcmShowPatientInfoInSystemLog) <dcmShowPatientInfoInSystemLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in system logs. Enumerated values: PLAIN_TEXT, HASH_NAME or HASH_NAME_AND_ID"
    "
    .. _dcmShowPatientInfoInAuditLog:

    :ref:`Show Patient Info In Audit Log (dcmShowPatientInfoInAuditLog) <dcmShowPatientInfoInAuditLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in emitted audit messages. Enumerated values: PLAIN_TEXT, HASH_NAME or HASH_NAME_AND_ID"
    "
    .. _dcmStowSpoolDirectory:

    :ref:`STOW-RS Spool Directory (dcmStowSpoolDirectory) <dcmStowSpoolDirectory>`",string,"Path to Directory used by STOW-RS Service to spool Bulkdata of XML/JSON Metadata and Bulk Data Request Messages."
    "
    .. _hl7PatientUpdateTemplateURI:

    :ref:`HL7 Patient Update Template URI (hl7PatientUpdateTemplateURI) <hl7PatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _hl7ImportReportTemplateURI:

    :ref:`HL7 Import Report Template URI (hl7ImportReportTemplateURI) <hl7ImportReportTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _hl7ScheduleProcedureTemplateURI:

    :ref:`HL7 Schedule Procedure Template URI (hl7ScheduleProcedureTemplateURI) <hl7ScheduleProcedureTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _hl7OutgoingPatientUpdateTemplateURI:

    :ref:`HL7 Outgoing Patient Update Template URI (hl7OutgoingPatientUpdateTemplateURI) <hl7OutgoingPatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet to transcode DICOM object patient attributes to HL7 ADT messages."
    "
    .. _hl7ScheduledProtocolCodeInOrder:

    :ref:`HL7 Schedule Protocol Code in Order (hl7ScheduledProtocolCodeInOrder) <hl7ScheduledProtocolCodeInOrder>`",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. May be overwritten by configured values for particular Archive HL7 Application. Enumerated values: OBR_4_1 or OBR_4_4"
    "
    .. _hl7ScheduledStationAETInOrder:

    :ref:`HL7 Schedule Station AET in Order (hl7ScheduledStationAETInOrder) <hl7ScheduledStationAETInOrder>`",string,"Specifies location of Scheduled Station AE Title in received HL7 Order message. Should not be configured for HL7 v2.5.1 OMI^O23 with IPC segment. If absent or no value is provided in the configured field, the Scheduled Station AE Title is selected according configured rules. May be overwritten by configured values for particular Archive HL7 Application. Enumerated values: ORC_18"
    "
    .. _hl7LogFilePattern:

    :ref:`HL7 Log File Pattern (hl7LogFilePattern) <hl7LogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7"
    "
    .. _hl7ErrorLogFilePattern:

    :ref:`HL7 Error Log File Pattern (hl7ErrorLogFilePattern) <hl7ErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7"
    "
    .. _hl7NoPatientCreateMessageType:

    :ref:`HL7 No Patient Create Message Type(s) (hl7NoPatientCreateMessageType) <hl7NoPatientCreateMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of HL7 messages which are only processed, if there is already a Patient record in the database, which Patient ID matches the Patient ID in the PID or MRG segment of the message. Thus no new Patient record will be created by messages of the specified types. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _dcmUnzipVendorDataToURI:

    :ref:`Unzip Vendor Data To URI (dcmUnzipVendorDataToURI) <dcmUnzipVendorDataToURI>`",string,"Specifies URI of directory into which ZIP stream in Device Vendor Data attribute will be extracted"
    "
    .. _dcmPurgeQueueMessagePollingInterval:

    :ref:`Purge Queue Messages Polling Interval (dcmPurgeQueueMessagePollingInterval) <dcmPurgeQueueMessagePollingInterval>`",string,"Polling Interval for purging queue messages in ISO-8601 duration format PnDTnHnMn.nS. If absent, there is no deletion"
    "
    .. _dcmWadoSpoolDirectory:

    :ref:`Wado-RS Spool Directory (dcmWadoSpoolDirectory) <dcmWadoSpoolDirectory>`",string,"Path to Wado-RS spool directory used to aggregate uncompressed frames."
    "
    .. _dcmRejectExpiredStudiesPollingInterval:

    :ref:`Reject Expired Studies Polling Interval (dcmRejectExpiredStudiesPollingInterval) <dcmRejectExpiredStudiesPollingInterval>`",string,"Polling Interval for rejecting expired Studies and Series in ISO-8601 duration format PnDTnHnMn.nS. If absent, neither expired Studies nor Series will be rejected automatically"
    "
    .. _dcmRejectExpiredStudiesPollingStartTime:

    :ref:`Reject Expired Studies Polling Start Time (dcmRejectExpiredStudiesPollingStartTime) <dcmRejectExpiredStudiesPollingStartTime>`",string,"Time when the polling interval for rejecting expired Studies and Series starts in ISO-8601 time format [hh][mm][ss]. Archive start time if absent."
    "
    .. _dcmRejectExpiredStudiesFetchSize:

    :ref:`Reject Expired Studies Fetch Size (dcmRejectExpiredStudiesFetchSize) <dcmRejectExpiredStudiesFetchSize>`",integer,"Maximal number of expired Studies fetched in one query; If absent, expired Studies will not be rejected automatically"
    "
    .. _dcmRejectExpiredSeriesFetchSize:

    :ref:`Reject Expired Series Fetch Size (dcmRejectExpiredSeriesFetchSize) <dcmRejectExpiredSeriesFetchSize>`",integer,"Maximal number of expired Series fetched in one query; If absent, expired Series will not be rejected automatically"
    "
    .. _dcmRejectExpiredStudiesAETitle:

    :ref:`Reject Expired Studies AE Title (dcmRejectExpiredStudiesAETitle) <dcmRejectExpiredStudiesAETitle>`",string,"AE Title of Local Application Entity performing the automatic rejection of expired Studies and Series. If absent, neither expired Studies nor Series will be rejected automatically."
    "
    .. _dcmStorePermissionServiceURL:

    :ref:`Store Permission Service URL (dcmStorePermissionServiceURL) <dcmStorePermissionServiceURL>`",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study by any AE. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http://host.name/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030,urlencoded}. May be overwritten by configured value for particular Archive Network AEs."
    "
    .. _dcmStorePermissionServiceResponsePattern:

    :ref:`Store Permission Service Response Pattern (dcmStorePermissionServiceResponsePattern) <dcmStorePermissionServiceResponsePattern>`",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" . If absent, every success response will be treated as agreement for storage. May be overwritten by configured value for particular Archive Network AEs."
    "
    .. _dcmStorePermissionCacheStaleTimeout:

    :ref:`Store Permission Cache Stale Timeout (dcmStorePermissionCacheStaleTimeout) <dcmStorePermissionCacheStaleTimeout>`",string,"Maximal staleness of cached responses from Storage Permission Service in ISO-8601 duration format PnDTnHnMn.nS. If absent, cached responses are only removed on reaching the maximal cache size."
    "
    .. _dcmStorePermissionCacheSize:

    :ref:`Store Permission Cache Size (dcmStorePermissionCacheSize) <dcmStorePermissionCacheSize>`",integer,"Maximum number of cached responses from Storage Permission Service."
    "
    .. _dcmMergeMWLCacheStaleTimeout:

    :ref:`Merge MWL Cache Stale Timeout (dcmMergeMWLCacheStaleTimeout) <dcmMergeMWLCacheStaleTimeout>`",string,"Maximal staleness of Request Attributes extracted from matching DICOM MWL items in ISO-8601 duration format PnDTnHnMn.nS. If absent, cached Request Attributes are only removed on reaching the maximal cache size."
    "
    .. _dcmMergeMWLCacheSize:

    :ref:`Merge MWL Cache Size (dcmMergeMWLCacheSize) <dcmMergeMWLCacheSize>`",integer,"Maximum number of cached Request Attributes extracted from matching DICOM MWL items."
    "
    .. _dcmStoreUpdateDBMaxRetries:

    :ref:`Store Update DB Maximum Number of Retries (dcmStoreUpdateDBMaxRetries) <dcmStoreUpdateDBMaxRetries>`",integer,"Maximum number of retries to update the database on storage."
    "
    .. _dcmStoreUpdateDBMaxRetryDelay:

    :ref:`Store Update DB Delay of Retry (dcmStoreUpdateDBMaxRetryDelay) <dcmStoreUpdateDBMaxRetryDelay>`",integer,"Delay in ms of retry to update the database on storage."
    "
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:

    :ref:`Allow Rejection For Data Retention Policy Expired (dcmAllowRejectionForDataRetentionPolicyExpired) <dcmAllowRejectionForDataRetentionPolicyExpired>`",string,"Allow Rejection For Data Retention Policy Expired. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: NEVER, ALWAYS, EXPIRED_UNSET or ONLY_EXPIRED"
    "
    .. _dcmAllowDeleteStudyPermanently:

    :ref:`Allow Delete Study permanently (dcmAllowDeleteStudyPermanently) <dcmAllowDeleteStudyPermanently>`",string,"Allow to delete Study permanently. REJECTED = only already rejected Studies. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: ALWAYS or REJECTED"
    "
    .. _dcmStorePermissionServiceExpirationDatePattern:

    :ref:`Store Permission Service Expiration Date Pattern (dcmStorePermissionServiceExpirationDatePattern) <dcmStorePermissionServiceExpirationDatePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". If absent, locally configured Study Retention Policy Rules will be applied. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmPurgeStgCmtCompletedDelay:

    :ref:`Purge Storage Commitment Completed Delay (dcmPurgeStgCmtCompletedDelay) <dcmPurgeStgCmtCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which results of completed Storage Commitment requests are purged. If absent, there is no deletion."
    "
    .. _dcmPurgeStgCmtPollingInterval:

    :ref:`Purge Storage Commitment Polling Interval (dcmPurgeStgCmtPollingInterval) <dcmPurgeStgCmtPollingInterval>`",string,"Polling Interval for purging Storage Commitment Results in ISO-8601 duration format PnDTnHnMn.nS. If absent, there is no deletion"
    "
    .. _dcmDefaultCharacterSet:

    :ref:`Default Character Set (dcmDefaultCharacterSet) <dcmDefaultCharacterSet>`",string,"Value of Specific Character Set (0008,0005) added to Data Sets without Specific Character Set (0008,0005) attribute received by any AE. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmStorePermissionServiceErrorCommentPattern:

    :ref:`Store Permission Service Error Comment Pattern (dcmStorePermissionServiceErrorCommentPattern) <dcmStorePermissionServiceErrorCommentPattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". If absent, ""Storage denied."" will be used as Error Comment. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmStorePermissionServiceErrorCodePattern:

    :ref:`Store Permission Service Error Code Pattern (dcmStorePermissionServiceErrorCodePattern) <dcmStorePermissionServiceErrorCodePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". If absent, the Error Code will be 0124H (Not Authorized). May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) (dcmRetrieveAET) <dcmRetrieveAET>`",string,"Specifies Retrieve AE Titles associated with received DICOM objects. If absent, the Called AE Title of the receiving AE will be used. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmExternalRetrieveAEDestination:

    :ref:`External Retrieve AE Destination (dcmExternalRetrieveAEDestination) <dcmExternalRetrieveAEDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to external retrieve AE. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _dcmXDSiImagingDocumentSourceAETitle:

    :ref:`XDS-I Imaging Document Source AE Title (dcmXDSiImagingDocumentSourceAETitle) <dcmXDSiImagingDocumentSourceAETitle>`",string,"AE Title of local Application Entity associated with XDS-I Imaging Document Source."
    "
    .. _dcmQueueTasksFetchSize:

    :ref:`Queue Tasks Fetch Size (dcmQueueTasksFetchSize) <dcmQueueTasksFetchSize>`",integer,"Maximal number of Tasks rescheduled or deleted or canceled in one transaction."
    ":doc:`attributeFilter` (s)",object,"Specifies Attributes stored in the database"
    ":doc:`attributeSet` (s)",object,"Named Attribute Set for Query Parameter 'comparefield' of DIFF-RS and Query Parameter 'includefields' of WADO-RS Metadata requests."
    "
    .. _dcmRemapRetrieveURL:

    :ref:`Remap Retrieve URL (dcmRemapRetrieveURL) <dcmRemapRetrieveURL>`",string,"Remap Retrieve URL used in QIDO-RS and WADO-RS Metadata responses. Optionally prefixed with ""[<http-client-host>]"". E.g.: ""[cache-proxy]http://cache-proxy:8080"". If absent or if the specified <http-client-host> does not match, scheme and server authority of the QIDO-RS or WADO-RS request URL are used."
    "
    .. _dcmAuditRecordRepositoryURL:

    :ref:`Audit Record Repository URL (dcmAuditRecordRepositoryURL) <dcmAuditRecordRepositoryURL>`",string,"Access URL of Audit Record Repository. E.g. http://kibana:5601"
    "
    .. _dcmAudit2JsonFhirTemplateURI:

    :ref:`Audit to json+fhir Template URI (dcmAudit2JsonFhirTemplateURI) <dcmAudit2JsonFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR JSON Resource Audit Event"
    "
    .. _dcmAudit2XmlFhirTemplateURI:

    :ref:`Audit to xml+fhir Template URI (dcmAudit2XmlFhirTemplateURI) <dcmAudit2XmlFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR XML Resource Audit Event"
    "
    .. _dcmInvokeImageDisplayPatientURL:

    :ref:`Invoke Image Display Patient URL (dcmInvokeImageDisplayPatientURL) <dcmInvokeImageDisplayPatientURL>`",string,"URL to launch external Image Display for a Patient. {} will be replaced by the Patient ID formatted as HL7 CX data type. E.g.: http://display:8080/IHEInvokeImageDisplay?requestType=PATIENT&patientID={}. May be overwritten by configured value for particular Archive Network AEs."
    "
    .. _dcmInvokeImageDisplayStudyURL:

    :ref:`Invoke Image Display Study URL (dcmInvokeImageDisplayStudyURL) <dcmInvokeImageDisplayStudyURL>`",string,"URL to launch external Image Display for a Study. {} will be replaced by the Study Instance UID. E.g.: http://display:8080/IHEInvokeImageDisplay?requestType=STUDY&studyUID={}. May be overwritten by configured value for particular Archive Network AEs."
    "
    .. _dcmCopyMoveUpdatePolicy:

    :ref:`Copy Move Update Policy (dcmCopyMoveUpdatePolicy) <dcmCopyMoveUpdatePolicy>`",string,"Specifies update policy for attributes of the destination Study on Copy/Move of Instances from another Study. If absent, the attributes will not be updated. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: SUPPLEMENT, MERGE, OVERWRITE or REPLACE"
    "
    .. _dcmLinkMWLEntryUpdatePolicy:

    :ref:`Link MWL Entry Update Policy (dcmLinkMWLEntryUpdatePolicy) <dcmLinkMWLEntryUpdatePolicy>`",string,"Specifies update policy for Study attributes on Link of Instances of another Study with a MWL Entry referring an existing Study. If absent, the attributes will not be updated. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: SUPPLEMENT, MERGE, OVERWRITE or REPLACE"
    "
    .. _hl7ADTSendingApplication:

    :ref:`HL7 ADT Sending Application (hl7ADTSendingApplication) <hl7ADTSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 ADT messages to synchronize external systems about performed Patient Information updates. If absent, synchronization of external systems by HL7 ADT messages is disabled."
    "
    .. _hl7ADTReceivingApplication:

    :ref:`HL7 ADT Receiving Application(s) (hl7ADTReceivingApplication) <hl7ADTReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 ADT messages to synchronize external systems about performed Patient Information updates. If absent, synchronization of external systems by HL7 ADT messages is disabled."
    "
    .. _hl7PSUSendingApplication:

    :ref:`HL7 Procedure Status Update Sending Application (hl7PSUSendingApplication) <hl7PSUSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 Procedure Status Update. HL7 Procedure Status Update disabled, if absent. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _hl7PSUReceivingApplication:

    :ref:`HL7 Procedure Status Update Receiving Application(s) (hl7PSUReceivingApplication) <hl7PSUReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 Procedure Status Update. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _hl7PSUDelay:

    :ref:`HL7 Procedure Status Update Delay (hl7PSUDelay) <hl7PSUDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _hl7PSUMWL:

    :ref:`HL7 Procedure Status Update MWL (hl7PSUMWL) <hl7PSUMWL>`",boolean,"Specifies if the Status of MWL Items in the DB is updated to COMPLETED for a received study after the configured HL7 Procedure Status Update Delay. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _hl7PSUTimeout:

    :ref:`HL7 Procedure Status Update Timeout (hl7PSUTimeout) <hl7PSUTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _hl7PSUOnTimeout:

    :ref:`HL7 Procedure Status Update On Timeout (hl7PSUOnTimeout) <hl7PSUOnTimeout>`",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded. May be overwritten by configured values for particular Archive Network AEs."
    "
    .. _hl7PSUTaskPollingInterval:

    :ref:`HL7 Procedure Status Update Task Polling Interval (hl7PSUTaskPollingInterval) <hl7PSUTaskPollingInterval>`",string,"Polling Interval for HL7 Procedure Status Update Tasks in ISO-8601 duration format PnDTnHnMn.nS. Disabled, if absent."
    "
    .. _hl7PSUTaskFetchSize:

    :ref:`HL7 Procedure Status Update Tasks Fetch Size (hl7PSUTaskFetchSize) <hl7PSUTaskFetchSize>`",integer,"Maximal number of HL7 Procedure Status Update Tasks fetched in one query."
    "
    .. _hl7TrackChangedPatientID:

    :ref:`HL7 Track Changed Patient ID (hl7TrackChangedPatientID) <hl7TrackChangedPatientID>`",boolean,"Enable to keep track of the prior Patient ID on a change of the Patient ID by HL7 ADT^A47 or by the RESTful Patient Update Service."
    "
    .. _dcmAuditSoftwareConfigurationVerbose:

    :ref:`Audit Software Configuration Verbose (dcmAuditSoftwareConfigurationVerbose) <dcmAuditSoftwareConfigurationVerbose>`",boolean,"Specifies if Child Objects and Attributes of created Objects should be included in Software Configuration Audit Message."
    "
    .. _hl7UseNullValue:

    :ref:`Use HL7 Null Value (hl7UseNullValue) <hl7UseNullValue>`",boolean,"Specifies if HL7 v2 null values (|""""|) are used in sent HL7 messages for not present or empty entity attributes. Required to unset entity attributes at the remote HL7 Application. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _dcmRejectionNoteStorageAET:

    :ref:`Rejection Note Storage AE title (dcmRejectionNoteStorageAET) <dcmRejectionNoteStorageAET>`",string,"Title of Archive Application Entity, of which first configured Object Storage will be used for storing Rejection Notes generated either by IOCM-RS services or by Delete Expired Studies Scheduler. If absent, for IOCM services the Object Storage configured for Archive AE referred in the IOCM-RS request will be used, or for Delete Expired Studies Scheduler the Object Storage configured for Reject Expired Studies AE will be used."
    "
    .. _dcmUIConfigurationDeviceName:

    :ref:`UI Configuration Device Name (dcmUIConfigurationDeviceName) <dcmUIConfigurationDeviceName>`",string,"Specifies the device name containing the Archive UI Configuration."
    ":doc:`storage` (s)",object,"Specifies Storage System"
    ":doc:`queryRetrieveView` (s)",object,"Specifies behavior on Rejection Note Stored"
    ":doc:`queue` (s)",object,"Managed JMS Queue"
    ":doc:`exporter` (s)",object,"Exporter Descriptor"
    ":doc:`exportRule` (s)",object,"Export Rules applied to DICOM objects received by any AE. May be supplemented by configured Export Rules for particular Archive Network AEs."
    ":doc:`rsForwardRule` (s)",object,"RESTful Forward Rules. May be supplemented by configured RESTful Forward Rules for particular Archive Network AEs."
    ":doc:`keycloakServer` (s)",object,"Keycloak Server"
    ":doc:`archiveCompressionRule` (s)",object,"Compression rules applied to DICOM objects received by any AE. May be supplemented by configured Compression Rules for particular Archive Network AEs."
    ":doc:`archiveAttributeCoercion` (s)",object,"Attribute Coercion applied to DIMSE received/sent by any AE. May be supplemented by configured Attribute Coercions for particular Archive Network AEs."
    ":doc:`rejectionNote` (s)",object,"Specifies behavior on Rejection Note Stored"
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policies applied to Studies received by any AE. May be supplemented by configured Study Retention Policies for particular Archive Network AEs."
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by any AE. May be supplemented by configured Store Access Control Rules for particular Archive Network AEs."
    ":doc:`idGenerator` (s)",object,"ID Generator"
    "
    .. _dcmXRoadProperty:

    :ref:`X-Road Property(s) (dcmXRoadProperty) <dcmXRoadProperty>`",string,"Properties for accessing Estonian National Patient Registry in format <name>=<value>"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rules for HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Forward Rules for particular HL7 Applications."
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed received by any HL7 Application. May be supplemented by configured values for particular HL7 Applications."
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages. May be overwritten by configured values for particular Archive HL7 Application."

.. toctree::

    attributeFilter
    attributeSet
    storage
    queryRetrieveView
    queue
    exporter
    exportRule
    rsForwardRule
    keycloakServer
    archiveCompressionRule
    archiveAttributeCoercion
    rejectionNote
    studyRetentionPolicy
    storeAccessControlIDRule
    idGenerator
    hl7ForwardRule
    hl7OrderScheduledStation
    hl7OrderSPSStatus
