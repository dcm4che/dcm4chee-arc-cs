Archive Device
==============
DICOM Archive Device related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Device Attributes (LDAP Object: dcmArchiveDevice)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmFuzzyAlgorithmClass:

    :ref:`Fuzzy Algorithm Class <dcmFuzzyAlgorithmClass>`",string,"Specifies Fuzzy Algorithm Implementation Class. Enumerated values: org.dcm4che3.soundex.Soundex, org.dcm4che3.soundex.ESoundex, org.dcm4che3.soundex.ESoundex9, org.dcm4che3.soundex.Metaphone, org.dcm4che3.soundex.KPhonetik or org.dcm4che3.soundex.Phonem.

    (dcmFuzzyAlgorithmClass)"
    "
    .. _dcmBulkDataDescriptorID:

    :ref:`Bulk Data Descriptor ID <dcmBulkDataDescriptorID>`",string,"ID of Bulk Data Descriptor applied by all services providing Metadata of archived instances. If absent, only Attributes specified by the Composite Instance Retrieve Without Bulk Data Service Class are treated as Bulk Data. May be overwritten by configured values for particular Archive Network AEs.

    (dcmBulkDataDescriptorID)"
    "
    .. _dcmSeriesMetadataStorageID:

    :ref:`Series Metadata Storage ID(s) <dcmSeriesMetadataStorageID>`",string,"ID of Storage on which ZIP archives with aggregated Metadata of all instances of a Series is stored. Multiple Storage Systems may be configured. If absent, no aggregated Series Metadata will be stored.

    (dcmSeriesMetadataStorageID)"
    "
    .. _dcmSeriesMetadataDelay:

    :ref:`Aggregate Series Metadata Delay <dcmSeriesMetadataDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS for storing aggregated Series Metadata on storage. If absent, no aggregated Series Metadata will be stored. May be overwritten by configured values for particular Archive Network AEs.

    (dcmSeriesMetadataDelay)"
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

    :ref:`Purge Instance Records <dcmPurgeInstanceRecords>`",boolean,"Indicates that Instance Records may be purged from the DB.

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
    .. _dcmOverwritePolicy:

    :ref:`Overwrite Policy <dcmOverwritePolicy>`",string,"Overwrite Policy. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: NEVER, ALWAYS, SAME_SOURCE, SAME_SERIES or SAME_SOURCE_AND_SERIES.

    (dcmOverwritePolicy)"
    "
    .. _dcmAcceptMissingPatientID:

    :ref:`Accept Missing Patient ID <dcmAcceptMissingPatientID>`",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: YES, NO or CREATE.

    (dcmAcceptMissingPatientID)"
    "
    .. _dcmAcceptConflictingPatientID:

    :ref:`Accept Conflicting Patient ID <dcmAcceptConflictingPatientID>`",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: YES, NO or MERGED.

    (dcmAcceptConflictingPatientID)"
    "
    .. _dcmBulkDataSpoolDirectory:

    :ref:`Bulk Data Spool Directory <dcmBulkDataSpoolDirectory>`",string,"Path to Bulk Data Spool Directory. May be overwritten by configured values for particular Archive Network AEs.

    (dcmBulkDataSpoolDirectory)"
    "
    .. _dcmHideSPSWithStatusFromMWL:

    :ref:`Hide SPS with Status(s) <dcmHideSPSWithStatusFromMWL>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: SCHEDULED, ARRIVED, READY, STARTED, DEPARTED, CANCELLED, DISCONTINUED or COMPLETED.

    (dcmHideSPSWithStatusFromMWL)"
    "
    .. _dcmValidateCallingAEHostname:

    :ref:`Validate Calling AE Hostname <dcmValidateCallingAEHostname>`",boolean,"Validate Calling AE Hostname or IP Address of Association requestors. May be overwritten by configured values for particular Archive Network AEs.

    (dcmValidateCallingAEHostname)"
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
    .. _dcmWadoZIPEntryNameFormat:

    :ref:`Wado ZIP Entry Name Format <dcmWadoZIPEntryNameFormat>`",string,"Format of entry names in ZIP archive returned by WADO-RS. May be overwritten by configured value for particular Archive Network AEs.

    (dcmWadoZIPEntryNameFormat)"
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

    :ref:`Qido Max Number Of Results <dcmQidoMaxNumberOfResults>`",integer,"Maximal number of return results by QIDO-RS Service. 0 = no limitation. May be overwritten by configured values for particular Archive Network AEs.

    (dcmQidoMaxNumberOfResults)"
    "
    .. _dcmFwdMppsDestination:

    :ref:`Mpps Forward Destination(s) <dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ. May be overwritten by configured values for particular Archive Network AEs.

    (dcmFwdMppsDestination)"
    "
    .. _dcmIanDestination:

    :ref:`Ian Destination(s) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanDestination)"
    "
    .. _dcmIanDelay:

    :ref:`IAN Delay <dcmIanDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which an IAN for a received study is sent to configured IAN destinations. If absent, IANs are triggered by received MPPS. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanDelay)"
    "
    .. _dcmIanTimeout:

    :ref:`IAN Timeout <dcmIanTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMnS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanTimeout)"
    "
    .. _dcmIanOnTimeout:

    :ref:`IAN On Timeout <dcmIanOnTimeout>`",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced is exceeded. May be overwritten by configured values for particular Archive Network AEs.

    (dcmIanOnTimeout)"
    "
    .. _dcmIanTaskPollingInterval:

    :ref:`IAN Task Polling Interval <dcmIanTaskPollingInterval>`",string,"Polling Interval for IAN Tasks in ISO-8601 duration format PnDTnHnMnS. IAN disabled, if absent

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

    :ref:`Spanning C-Find SCP Policy <dcmSpanningCFindSCPPolicy>`",string,"Specifies policy for combining matches returned from configured Spanning C-Find SCP with matching entries from the archive DB. SUPPLEMENT (= returns local matches before additional matches from Spanning C-Find SCP ), MERGE (= returns matches from Spanning C-Find SCP before additional local matches), REPLACE (= returns only matches from Spanning C-Find SCP). May be overwritten by configured values for particular Archive Network AEs. Enumerated values: SUPPLEMENT, MERGE or REPLACE.

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
    .. _dcmAltCMoveSCP:

    :ref:`Alternative C-Move SCP <dcmAltCMoveSCP>`",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage

    (dcmAltCMoveSCP)"
    "
    .. _dcmExportTaskPollingInterval:

    :ref:`Export Task Polling Interval <dcmExportTaskPollingInterval>`",string,"Export Task Polling Interval in ISO-8601 duration format PnDTnHnMnS.

    (dcmExportTaskPollingInterval)"
    "
    .. _dcmExportTaskFetchSize:

    :ref:`Export Task Fetch Size <dcmExportTaskFetchSize>`",integer,"Maximal number of Export Tasks scheduled in one transaction.

    (dcmExportTaskFetchSize)"
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

    :ref:`Delete Study Batch Size <dcmDeleteStudyBatchSize>`",integer,"number of studies to delete from the Storage System, if the usable space fall below configured Usable Space, before checking the usable space again.

    (dcmDeleteStudyBatchSize)"
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
    .. _dcmShowPatientInfoInSystemLog:

    :ref:`Show Patient Info In System Log <dcmShowPatientInfoInSystemLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in system logs. Enumerated values: PLAIN_TEXT, HASH_NAME or HASH_NAME_AND_ID.

    (dcmShowPatientInfoInSystemLog)"
    "
    .. _dcmShowPatientInfoInAuditLog:

    :ref:`Show Patient Info In Audit Log <dcmShowPatientInfoInAuditLog>`",string,"Specifies if Patient Information is shown as plain text or hashed in emitted audit messages. Enumerated values: PLAIN_TEXT, HASH_NAME or HASH_NAME_AND_ID.

    (dcmShowPatientInfoInAuditLog)"
    "
    .. _dcmStowSpoolDirectory:

    :ref:`STOW-RS Spool Directory <dcmStowSpoolDirectory>`",string,"Path to Directory used by STOW-RS Service to spool Bulkdata of XML/JSON Metadata and Bulk Data Request Messages.

    (dcmStowSpoolDirectory)"
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

    :ref:`HL7 Schedule Protocol Code in Order <hl7ScheduledProtocolCodeInOrder>`",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. May be overwritten by configured values for particular Archive HL7 Application. Enumerated values: OBR_4_1 or OBR_4_4.

    (hl7ScheduledProtocolCodeInOrder)"
    "
    .. _hl7ScheduledStationAETInOrder:

    :ref:`HL7 Schedule Station AET in Order <hl7ScheduledStationAETInOrder>`",string,"Specifies location of Scheduled Station AE Title in received HL7 Order message. Should not be configured for HL7 v2.5.1 OMI^O23 with IPC segment. If absent or no value is provided in the configured field, the Scheduled Station AE Title is selected according configured rules. May be overwritten by configured values for particular Archive HL7 Application. Enumerated values: ORC_18.

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
    .. _hl7NoPatientCreateMessageType:

    :ref:`HL7 No Patient Create Message Type(s) <hl7NoPatientCreateMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of HL7 messages which are only processed, if there is already a Patient record in the database, which Patient ID matches the Patient ID in the PID or MRG segment of the message. Thus no new Patient record will be created by messages of the specified types. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7NoPatientCreateMessageType)"
    "
    .. _dcmUnzipVendorDataToURI:

    :ref:`Unzip Vendor Data To URI <dcmUnzipVendorDataToURI>`",string,"Specifies URI of directory into which ZIP stream in Device Vendor Data attribute will be extracted

    (dcmUnzipVendorDataToURI)"
    "
    .. _dcmPurgeQueueMessagePollingInterval:

    :ref:`Purge Queue Messages Polling Interval <dcmPurgeQueueMessagePollingInterval>`",string,"Polling Interval for purging queue messages in ISO-8601 duration format PnDTnHnMnS. If absent, there is no deletion

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

    :ref:`Store Permission Service URL <dcmStorePermissionServiceURL>`",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study by any AE. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http://host.name/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030,urlencoded}. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceURL)"
    "
    .. _dcmStorePermissionServiceResponsePattern:

    :ref:`Store Permission Service Response Pattern <dcmStorePermissionServiceResponsePattern>`",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" . If absent, every success response will be treated as agreement for storage. May be overwritten by configured value for particular Archive Network AEs.

    (dcmStorePermissionServiceResponsePattern)"
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

    :ref:`Allow Rejection For Data Retention Policy Expired <dcmAllowRejectionForDataRetentionPolicyExpired>`",string,"Allow Rejection For Data Retention Policy Expired. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: NEVER, ALWAYS, EXPIRED_UNSET or ONLY_EXPIRED.

    (dcmAllowRejectionForDataRetentionPolicyExpired)"
    "
    .. _dcmAllowDeleteStudyPermanently:

    :ref:`Allow Delete Study permanently <dcmAllowDeleteStudyPermanently>`",string,"Allow to delete Study permanently. REJECTED = only already rejected Studies. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: ALWAYS or REJECTED.

    (dcmAllowDeleteStudyPermanently)"
    "
    .. _dcmAllowDeletePatient:

    :ref:`Allow Delete Patient <dcmAllowDeletePatient>`",string,"Allow permanent deletion of Patients. Enumerated values: NEVER, ALWAYS, WITHOUT_STUDIES. If absent, WITHOUT_STUDIES will be applied. Enumerated values: NEVER, ALWAYS or WITHOUT_STUDIES.

    (dcmAllowDeletePatient)"
    "
    .. _dcmStorePermissionServiceExpirationDatePattern:

    :ref:`Store Permission Service Expiration Date Pattern <dcmStorePermissionServiceExpirationDatePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". If absent, locally configured Study Retention Policy Rules will be applied. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceExpirationDatePattern)"
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
    .. _dcmStorePermissionServiceErrorCommentPattern:

    :ref:`Store Permission Service Error Comment Pattern <dcmStorePermissionServiceErrorCommentPattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". If absent, ""Storage denied."" will be used as Error Comment. May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceErrorCommentPattern)"
    "
    .. _dcmStorePermissionServiceErrorCodePattern:

    :ref:`Store Permission Service Error Code Pattern <dcmStorePermissionServiceErrorCodePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". If absent, the Error Code will be 0124H (Not Authorized). May be overwritten by configured values for particular Archive Network AEs.

    (dcmStorePermissionServiceErrorCodePattern)"
    "
    .. _dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) <dcmRetrieveAET>`",string,"Specifies Retrieve AE Titles associated with received DICOM objects. If absent, the Called AE Title of the receiving AE will be used. May be overwritten by configured values for particular Archive Network AEs.

    (dcmRetrieveAET)"
    "
    .. _dcmReturnRetrieveAET:

    :ref:`Return Retrieve AE Title(s) <dcmReturnRetrieveAET>`",string,"Retrieve AE Title returned in C-FIND and QIDO responses. If absent, the Retrieve AET associated with the archived entity will be returned. May be overwritten by configured values for particular Archive Network AEs.

    (dcmReturnRetrieveAET)"
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
    .. _dcmAuditRecordRepositoryURL:

    :ref:`Audit Record Repository URL <dcmAuditRecordRepositoryURL>`",string,"Access URL of Audit Record Repository. E.g. http://kibana:5601

    (dcmAuditRecordRepositoryURL)"
    "
    .. _dcmAudit2JsonFhirTemplateURI:

    :ref:`Audit to json+fhir Template URI <dcmAudit2JsonFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR JSON Resource Audit Event

    (dcmAudit2JsonFhirTemplateURI)"
    "
    .. _dcmAudit2XmlFhirTemplateURI:

    :ref:`Audit to xml+fhir Template URI <dcmAudit2XmlFhirTemplateURI>`",string,"Specifies URI for the style sheet to transcode Audit Message to a FHIR XML Resource Audit Event

    (dcmAudit2XmlFhirTemplateURI)"
    "
    .. _dcmInvokeImageDisplayPatientURL:

    :ref:`Invoke Image Display Patient URL <dcmInvokeImageDisplayPatientURL>`",string,"URL to launch external Image Display for a Patient. {} will be replaced by the Patient ID formatted as HL7 CX data type. E.g.: http://display:8080/IHEInvokeImageDisplay?requestType=PATIENT&patientID={}. May be overwritten by configured value for particular Archive Network AEs.

    (dcmInvokeImageDisplayPatientURL)"
    "
    .. _dcmInvokeImageDisplayStudyURL:

    :ref:`Invoke Image Display Study URL <dcmInvokeImageDisplayStudyURL>`",string,"URL to launch external Image Display for a Study. {} will be replaced by the Study Instance UID. E.g.: http://display:8080/IHEInvokeImageDisplay?requestType=STUDY&studyUID={}. May be overwritten by configured value for particular Archive Network AEs.

    (dcmInvokeImageDisplayStudyURL)"
    "
    .. _dcmCopyMoveUpdatePolicy:

    :ref:`Copy Move Update Policy <dcmCopyMoveUpdatePolicy>`",string,"Specifies update policy for attributes of the destination Study on Copy/Move of Instances from another Study. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: PRESERVE, SUPPLEMENT, MERGE, OVERWRITE or REPLACE.

    (dcmCopyMoveUpdatePolicy)"
    "
    .. _dcmLinkMWLEntryUpdatePolicy:

    :ref:`Link MWL Entry Update Policy <dcmLinkMWLEntryUpdatePolicy>`",string,"Specifies update policy for Study attributes on Link of Instances of another Study with a MWL Entry referring an existing Study. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: PRESERVE, SUPPLEMENT, MERGE, OVERWRITE or REPLACE.

    (dcmLinkMWLEntryUpdatePolicy)"
    "
    .. _dcmStorageVerificationPolicy:

    :ref:`Storage Verification Policy <dcmStorageVerificationPolicy>`",string,"DB_RECORD_EXISTS: only check for existence of DB records, OBJECT_EXISTS: check if object exists on Storage System, OBJECT_SIZE: check size of object on Storage System, OBJECT_FETCH: fetch object from Storage System), OBJECT_CHECKSUM: recalculate checksum of object on Storage System, S3_MD5SUM: check MD5 checksum of object on S3 Storage System. May be overwritten by configured values for particular Archive Network AEs. Enumerated values: DB_RECORD_EXISTS, OBJECT_EXISTS, OBJECT_SIZE, OBJECT_FETCH, OBJECT_CHECKSUM or S3_MD5SUM.

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

    :ref:`Storage Verification Period <dcmStorageVerificationPeriod>`",string,"Period between successive Storage Verifications of one Series.

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
    .. _dcmDiffTaskProgressUpdateInterval:

    :ref:`Diff Task Progress Update Interval <dcmDiffTaskProgressUpdateInterval>`",string,"Interval of updating Diff Tasks in process for progress monitoring; disabled if absent.

    (dcmDiffTaskProgressUpdateInterval)"
    "
    .. _dcmPatientVerificationPDQServiceID:

    :ref:`Patient Verification PDQ Service ID <dcmPatientVerificationPDQServiceID>`",string,"ID of PDQ Service used for Verification of Patient Demographic. If absent, no Patient Verification will be performed.

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

    :ref:`Patient Verification Maximum Staleness <dcmPatientVerificationMaxStaleness>`",string,"Indicates to renew the verification of Patient Demographics on receive of objects for a patient, if previous verification is longer ago as the specified Interval. If absent, Patient Verification on receive of objects is disabled.

    (dcmPatientVerificationMaxStaleness)"
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
    .. _hl7PSUDelay:

    :ref:`HL7 Procedure Status Update Delay <hl7PSUDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMnS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUDelay)"
    "
    .. _hl7PSUMWL:

    :ref:`HL7 Procedure Status Update MWL <hl7PSUMWL>`",boolean,"Specifies if the Status of MWL Items in the DB is updated to COMPLETED for a received study after the configured HL7 Procedure Status Update Delay. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUMWL)"
    "
    .. _hl7PSUTimeout:

    :ref:`HL7 Procedure Status Update Timeout <hl7PSUTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMnS for waiting on receive of instances referenced in MPPS; check for completeness forever if absent. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUTimeout)"
    "
    .. _hl7PSUOnTimeout:

    :ref:`HL7 Procedure Status Update On Timeout <hl7PSUOnTimeout>`",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded. May be overwritten by configured values for particular Archive Network AEs.

    (hl7PSUOnTimeout)"
    "
    .. _hl7PSUTaskPollingInterval:

    :ref:`HL7 Procedure Status Update Task Polling Interval <hl7PSUTaskPollingInterval>`",string,"Polling Interval for HL7 Procedure Status Update Tasks in ISO-8601 duration format PnDTnHnMnS. Disabled, if absent.

    (hl7PSUTaskPollingInterval)"
    "
    .. _hl7PSUTaskFetchSize:

    :ref:`HL7 Procedure Status Update Tasks Fetch Size <hl7PSUTaskFetchSize>`",integer,"Maximal number of HL7 Procedure Status Update Tasks fetched in one query.

    (hl7PSUTaskFetchSize)"
    "
    .. _hl7TrackChangedPatientID:

    :ref:`HL7 Track Changed Patient ID <hl7TrackChangedPatientID>`",boolean,"Enable to keep track of the prior Patient ID on a change of the Patient ID by HL7 ADT^A47 or by the RESTful Patient Update Service.

    (hl7TrackChangedPatientID)"
    "
    .. _dcmAuditSoftwareConfigurationVerbose:

    :ref:`Audit Software Configuration Verbose <dcmAuditSoftwareConfigurationVerbose>`",boolean,"Specifies if Child Objects and Attributes of created Objects should be included in Software Configuration Audit Message.

    (dcmAuditSoftwareConfigurationVerbose)"
    "
    .. _hl7UseNullValue:

    :ref:`Use HL7 Null Value <hl7UseNullValue>`",boolean,"Specifies if HL7 v2 null values `(|""""|)` are used in sent HL7 messages for not present or empty entity attributes. Required to unset entity attributes at the remote HL7 Application. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7UseNullValue)"
    "
    .. _hl7VeterinaryUsePatientName:

    :ref:`HL7 Veterinary use Patient Name <hl7VeterinaryUsePatientName>`",boolean,"Indicates to force veterinary use of Patient Names on mapping HL7 PID fields to DICOM attributes: only use the first two components of PID.5 as DICOM Patient Name; if PID.5 only contains one component, use that value as given name, and the first component of PID.9 as family name of the DICOM Patient Name. May be overwritten by configured values for particular Archive HL7 Application.

    (hl7VeterinaryUsePatientName)"
    "
    .. _hl7OrderMissingStudyIUIDPolicy:

    :ref:`HL7 Order Missing Study Instance UID Policy <hl7OrderMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Order messages. Enumerated values: REJECT, GENERATE or ACCESSION_BASED.

    (hl7OrderMissingStudyIUIDPolicy)"
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

    :ref:`CSV Upload Chunk Size <dcmCSVUploadChunkSize>`",integer,"Number of CSV file upload tasks to be processed in one transaction.

    (dcmCSVUploadChunkSize)"
    "
    .. _dcmValidateUID:

    :ref:`Validate UID <dcmValidateUID>`",boolean,"Indicates if UIDs shall be validated or not.

    (dcmValidateUID)"
    "
    .. _dcmRelationalQueryNegotiationLenient:

    :ref:`Relational Query Negotiation Lenient <dcmRelationalQueryNegotiationLenient>`",boolean,"Indicates to accept C-FIND RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated.

    (dcmRelationalQueryNegotiationLenient)"
    "
    .. _dcmRelationalRetrieveNegotiationLenient:

    :ref:`Relational Retrieve Negotiation Lenient <dcmRelationalRetrieveNegotiationLenient>`",boolean,"Indicates to accept C-MOVE and C-GET RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated.

    (dcmRelationalRetrieveNegotiationLenient)"
    "
    .. _dcmSchedulerMinStartDelay:

    :ref:`Scheduler Minimum Start Delay <dcmSchedulerMinStartDelay>`",integer,"Minimal delay in s to start schedulers on system start up.

    (dcmSchedulerMinStartDelay)"
    "
    .. _dcmRejectConflictingPatientAttribute:

    :ref:`Reject Conflicting Patient Attribute(s) <dcmRejectConflictingPatientAttribute>`",string,"DICOM Tag of Patient Attribute which have to match in received objects with the value in previous received objects with equal Patient ID to be accepted.

    (dcmRejectConflictingPatientAttribute)"
    "
    .. _dcmStowRetiredTransferSyntax:

    :ref:`STOW Retired Transfer Syntax <dcmStowRetiredTransferSyntax>`",boolean,"Store received JPEG Full Progression, Non-Hierarchical JPEG images in DICOM images with corresponding (retired) Transfer Syntax UID 1.2.840.10008.1.2.4.55. Otherwise set 1.2.840.10008.1.2.4.50 (= JPEG Baseline) or 1.2.840.10008.1.2.4.51 (= JPEG Extended) as Transfer Syntax UID of the stored DICOM image, without transcoding to JPEG Baseline or JPEG Extended, but including the JPEG image as received.

    (dcmStowRetiredTransferSyntax)"
    ":doc:`attributeFilter` (s)",object,"Specifies Attributes stored in the database"
    ":doc:`attributeSet` (s)",object,"Named Attribute Set for Query Parameter 'includefields' of QIDO-RS and WADO-RS Metadata or by Query Parameter 'comparefield' of DIFF-RS requests."
    ":doc:`bulkData` (s)",object,"Specifies Bulk Data Descriptors applied by services providing Metadata of archived instances."
    ":doc:`storage` (s)",object,"Specifies Storage System"
    ":doc:`queryRetrieveView` (s)",object,"Specifies behavior on Rejection Note Stored"
    ":doc:`queue` (s)",object,"Managed JMS Queue"
    ":doc:`metrics` (s)",object,"Activated Metrics"
    ":doc:`pdqService` (s)",object,"PDQ Service Descriptor"
    ":doc:`exporter` (s)",object,"Exporter Descriptor"
    ":doc:`exportRule` (s)",object,"Export Rules applied to DICOM objects received by any AE. May be supplemented by configured Export Rules for particular Archive Network AEs."
    ":doc:`exportPriorsRule` (s)",object,"Export Priors Rules applied to DICOM objects received by any AE. May be supplemented by configured Export Priors Rules for particular Archive Network AEs."
    ":doc:`rsForwardRule` (s)",object,"RESTful Forward Rules. May be supplemented by configured RESTful Forward Rules for particular Archive Network AEs."
    ":doc:`keycloakServer` (s)",object,"Keycloak Server"
    ":doc:`archiveCompressionRule` (s)",object,"Compression rules applied to DICOM objects received by any AE. May be supplemented by configured Compression Rules for particular Archive Network AEs."
    ":doc:`delayedCompressionRule` (s)",object,"Rules for compression of stored images after a particular delay. May be supplemented by configured Compression Rules for particular Archive Network AEs."
    ":doc:`archiveAttributeCoercion` (s)",object,"Attribute Coercion applied to DIMSE received/sent by any AE. May be supplemented by configured Attribute Coercions for particular Archive Network AEs."
    ":doc:`rejectionNote` (s)",object,"Specifies behavior on Rejection Note Stored"
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policies applied to Studies received by any AE. May be supplemented by configured Study Retention Policies for particular Archive Network AEs."
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by any AE. May be supplemented by configured Store Access Control Rules for particular Archive Network AEs."
    ":doc:`idGenerator` (s)",object,"ID Generator"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rules for HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Forward Rules for particular HL7 Applications."
    ":doc:`hl7ExportRule` (s)",object,"Export Rules applied to HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Export Rules for particular HL7 Application."
    ":doc:`hl7PrefetchRule` (s)",object,"HL7 Prefetch Rules applied to HL7 messages received by any HL7 Application. May be supplemented by configured HL7 Prefetch Rules for particular HL7 Application."
    ":doc:`hl7StudyRetentionPolicy` (s)",object,"HL7 Study Retention Policies triggered by HL7 messages received by any HL7 Application. May be supplemented by configured Study Retention Policies for particular HL7 Applications."
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed received by any HL7 Application. May be supplemented by configured values for particular HL7 Applications."
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages. May be overwritten by configured values for particular Archive HL7 Application."
    "
    .. _dcmXRoadProperty:

    :ref:`X-Road Property(s) <dcmXRoadProperty>`",string,"Properties for accessing Estonian National Patient Registry in format <name>=<value>

    (dcmXRoadProperty)"
    "
    .. _dcmImpaxReportProperty:

    :ref:`Impax Report Property(s) <dcmImpaxReportProperty>`",string,"Properties for accessing Agfa Impax Report Service in format <name>=<value>

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
    rsForwardRule
    keycloakServer
    archiveCompressionRule
    delayedCompressionRule
    archiveAttributeCoercion
    rejectionNote
    studyRetentionPolicy
    storeAccessControlIDRule
    idGenerator
    hl7ForwardRule
    hl7ExportRule
    hl7PrefetchRule
    hl7StudyRetentionPolicy
    hl7OrderScheduledStation
    hl7OrderSPSStatus
