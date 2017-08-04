Archive Network AE
==================
DICOM Archive Network AE related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive Network AE Attributes (LDAP Object: dcmArchiveNetworkAE)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Object Storage ID(s)",string,"ID of Storage System on which received DICOM composite objects are stored. Multiple Storage Systems may be configured.","
    .. _dcmObjectStorageID:

    dcmObjectStorageID_"
    "Object Storage Count",integer,"Number of Storage Systems which are filled in parallel.","
    .. _dcmObjectStorageCount:

    dcmObjectStorageCount_"
    "Metadata Storage ID(s)",string,"ID of Storage on which Metadata is stored in JSON format - additionally to the complete DICOM composite object. Multiple Storage Systems may be configured. If absent, metadata is not stored additionally.","
    .. _dcmMetadataStorageID:

    dcmMetadataStorageID_"
    "Aggregate Series Metadata Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for storing aggregated Series Metadata on storage of objects received by this AE. Overwrites value specified on Device level.","
    .. _dcmSeriesMetadataDelay:

    dcmSeriesMetadataDelay_"
    "Purge Instance Records Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for purging Instance Records from the DB received by this AE. Overwrites value specified on Device level.","
    .. _dcmPurgeInstanceRecordsDelay:

    dcmPurgeInstanceRecordsDelay_"
    "Store Access Control ID",string,"Access Control ID assigned to Studies received by this AE","
    .. _dcmStoreAccessControlID:

    dcmStoreAccessControlID_"
    "Access Control ID(s)",string,"Access Control IDs assigned to Query/Retrieve requests received by this AE","
    .. _dcmAccessControlID:

    dcmAccessControlID_"
    "Accepted Move Destination(s)",string,"Accepted Move Destination in C-MOVE requests; any if absent.","
    .. _dcmAcceptedMoveDestination:

    dcmAcceptedMoveDestination_"
    "Overwrite Policy",string,"Overwrite Policy for Objects received by this AE. Overwrites value specified on Device level. Enumerated values: NEVER, ALWAYS, SAME_SOURCE, SAME_SERIES or SAME_SOURCE_AND_SERIES","
    .. _dcmOverwritePolicy:

    dcmOverwritePolicy_"
    "Accept Missing Patient ID",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. Overwrites value specified on Device level. Enumerated values: YES, NO or CREATE","
    .. _dcmAcceptMissingPatientID:

    dcmAcceptMissingPatientID_"
    "Accept Conflicting Patient ID",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. Overwrites value specified on Device level. Enumerated values: YES, NO or MERGED","
    .. _dcmAcceptConflictingPatientID:

    dcmAcceptConflictingPatientID_"
    "Query/Retrieve View ID",string,"Query/Retrieve View Identifier","
    .. _dcmQueryRetrieveViewID:

    dcmQueryRetrieveViewID_"
    "Bulk Data Spool Directory",string,"Path to Bulk Data Spool Directory. Overwrites value specified on Device level.","
    .. _dcmBulkDataSpoolDirectory:

    dcmBulkDataSpoolDirectory_"
    "Hide SPS with Status(s)",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP Enumerated values: SCHEDULED, ARRIVED, READY, STARTED, DEPARTED, CANCELLED, DISCONTINUED or COMPLETED","
    .. _dcmHideSPSWithStatusFromMWL:

    dcmHideSPSWithStatusFromMWL_"
    "Validate Calling AE Hostname",boolean,"Validate Calling AE Hostname or IP Address of Association requestors for this AE. Overwrites value specified on Device level.","
    .. _dcmValidateCallingAEHostname:

    dcmValidateCallingAEHostname_"
    "Person Name Component Order Insensitive Matching",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names by this AE. Overwrites value specified on Device level.","
    .. _dcmPersonNameComponentOrderInsensitiveMatching:

    dcmPersonNameComponentOrderInsensitiveMatching_"
    "Send Pending C-Get",boolean,"Enables pending C-GET responses. Overwrites value specified on Device level.","
    .. _dcmSendPendingCGet:

    dcmSendPendingCGet_"
    "Send Pending C-Move Interval",string,"Interval of pending C-MOVE responses in ISO-8601 duration format PnDTnHnMn.nS; disabled if absent","
    .. _dcmSendPendingCMoveInterval:

    dcmSendPendingCMoveInterval_"
    "Wado SR2 Html Template URI",string,"Specifies URI for the style sheet used to render structured reports to html","
    .. _dcmWadoSR2HtmlTemplateURI:

    dcmWadoSR2HtmlTemplateURI_"
    "Wado SR2 Text Template URI",string,"Specifies URI for the style sheet used to render structured reports to plain text","
    .. _dcmWadoSR2TextTemplateURI:

    dcmWadoSR2TextTemplateURI_"
    "Query Max Number Of Results",integer,"Maximal number of return results by C-FIND SCP. If the number of matches extends the limit, the C-FIND request will be refused. 0 = no limitation. Overwrites value specified on Device level.","
    .. _dcmQueryMaxNumberOfResults:

    dcmQueryMaxNumberOfResults_"
    "Qido Max Number Of Results",integer,"Maximal number of return results by QIDO-RS Service. 0 = unlimited. Overwrites value specified on Device level.","
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
    "IAN On Timeout",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced is exceeded. Overwrites value specified on Device level.","
    .. _dcmIanOnTimeout:

    dcmIanOnTimeout_"
    "Fallback C-Move SCP",string,"AE Title of external C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not managed by this archive","
    .. _dcmFallbackCMoveSCP:

    dcmFallbackCMoveSCP_"
    "Fallback C-Move SCP Study Older Than",string,"Specifies threshold for Study Date in format YYYYMMDD for marking received Studies as (potential) incomplete to enforce the retrieve from configured dcmFallbackCMoveSCP","
    .. _dcmFallbackCMoveSCPStudyOlderThan:

    dcmFallbackCMoveSCPStudyOlderThan_"
    "Fallback C-Move SCP Destination",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to the external C-MOVE SCP specified by dcmFallbackCMoveSCP","
    .. _dcmFallbackCMoveSCPDestination:

    dcmFallbackCMoveSCPDestination_"
    "Fallback C-Move SCP Leading C-Find SCP",string,"AE Title of external C-FIND SCP for Verification of Number of Instances retrieved from external C-MOVE SCP specified by dcmFallbackCMoveSCP.","
    .. _dcmFallbackCMoveSCPLeadingCFindSCP:

    dcmFallbackCMoveSCPLeadingCFindSCP_"
    "Fallback C-Move SCP Retries",integer,"Maximal number of retries to retrieve not available objects from C-MOVE SCP configured by dcmFallbackCMoveSCP. -1 = forever. Use value configured on Device level, if absent","
    .. _dcmFallbackCMoveSCPRetries:

    dcmFallbackCMoveSCPRetries_"
    "Alternative C-Move SCP",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage","
    .. _dcmAltCMoveSCP:

    dcmAltCMoveSCP_"
    "Store Permission Service URL",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http://host.name/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030,urlencoded}. Overwrites value specified on Device level.","
    .. _dcmStorePermissionServiceURL:

    dcmStorePermissionServiceURL_"
    "Store Permission Service Response Pattern",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"". Overwrites value specified on Device level.","
    .. _dcmStorePermissionServiceResponsePattern:

    dcmStorePermissionServiceResponsePattern_"
    "Store Permission Service Expiration Date Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". Overwrites value specified on Device level.","
    .. _dcmStorePermissionServiceExpirationDatePattern:

    dcmStorePermissionServiceExpirationDatePattern_"
    "Store Permission Service Error Comment Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". Overwrites value specified on Device level.","
    .. _dcmStorePermissionServiceErrorCommentPattern:

    dcmStorePermissionServiceErrorCommentPattern_"
    "Store Permission Service Error Code Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". Overwrites value specified on Device level.","
    .. _dcmStorePermissionServiceErrorCodePattern:

    dcmStorePermissionServiceErrorCodePattern_"
    "Allow Rejection For Data Retention Policy Expired",string,"Allow Rejection For Data Retention Policy Expired. Overwrites value specified on Device level. Enumerated values: NEVER, ALWAYS or STUDY_RETENTION_POLICY","
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:

    dcmAllowRejectionForDataRetentionPolicyExpired_"
    "Accepted User Role(s)",string,"Roles of users from which web requests are accepted; any if absent.","
    .. _dcmAcceptedUserRole:

    dcmAcceptedUserRole_"
    "Allow Delete Study permanently",string,"Allow to delete Study permanently. REJECTED = only already rejected Studies. Overwrites value specified on Device level. Enumerated values: ALWAYS or REJECTED","
    .. _dcmAllowDeleteStudyPermanently:

    dcmAllowDeleteStudyPermanently_"
    "Default Character Set",string,"Value of Specific Character Set (0008,0005) added to Data Sets without Specific Character Set (0008,0005) attribute received by this Network AE. Overwrites value specified on Device level.","
    .. _dcmDefaultCharacterSet:

    dcmDefaultCharacterSet_"
    "Retrieve AE Title(s)",string,"Specifies Retrieve AE Titles associated with DICOM objects received by this Network AE. Overwrites value specified on Device level.","
    .. _dcmRetrieveAET:

    dcmRetrieveAET_"
    "External Retrieve AE Destination",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to external retrieve AE. Overwrites value specified on Device level.","
    .. _dcmExternalRetrieveAEDestination:

    dcmExternalRetrieveAEDestination_"
    "Invoke Image Display Patient URL",string,"URL to launch external Image Display for a Patient. {} will be replaced by the Patient ID formatted as HL7 CX data type. E.g.: http://display:8080/IHEInvokeImageDisplay?requestType=PATIENT&patientID={}. Overwrites value specified on Device level.","
    .. _dcmInvokeImageDisplayPatientURL:

    dcmInvokeImageDisplayPatientURL_"
    "Invoke Image Display Study URL",string,"URL to launch external Image Display for a Study. {} will be replaced by the Study Instance UID. E.g.: http://display:8080/IHEInvokeImageDisplay?requestType=STUDY&studyUID={}. Overwrites value specified on Device level.","
    .. _dcmInvokeImageDisplayStudyURL:

    dcmInvokeImageDisplayStudyURL_"
    "Copy Move Update Policy",string,"Specifies update policy for attributes of the destination Study on Copy/Move of Instances from another Study. If absent, the attributes will not be updated. Overwrites value specified on Device level. Enumerated values: SUPPLEMENT, OVERWRITE, MERGED or REPLACE","
    .. _dcmCopyMoveUpdatePolicy:

    dcmCopyMoveUpdatePolicy_"
    "HL7 Procedure Status Update Sending Application",string,"Application|Facility name of Sending Application for HL7 Procedure Status Update. Overwrites value specified on Device level.","
    .. _hl7PSUSendingApplication:

    hl7PSUSendingApplication_"
    "HL7 Procedure Status Update Receiving Application(s)",string,"Application|Facility name of Receiving Application for HL7 Procedure Status Update. Overwrites value specified on Device level.","
    .. _hl7PSUReceivingApplication:

    hl7PSUReceivingApplication_"
    "HL7 Procedure Status Update Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS. Overwrites value specified on Device level.","
    .. _hl7PSUDelay:

    hl7PSUDelay_"
    "HL7 Procedure Status Update MWL",boolean,"Specifies if the Status of MWL Items in the DB is updated to COMPLETED for a received study after the configured HL7 Procedure Status Update Delay. Overwrites value specified on Device level.","
    .. _hl7PSUMWL:

    hl7PSUMWL_"
    "HL7 Procedure Status Update Timeout",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS. Overwrites value specified on Device level.","
    .. _hl7PSUTimeout:

    hl7PSUTimeout_"
    "HL7 Procedure Status Update On Timeout",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded. Overwrites value specified on Device level.","
    .. _hl7PSUOnTimeout:

    hl7PSUOnTimeout_"
    ":doc:`exportRule` (s)",object,"Export Rules. Supplements Export Rules specified on Device level.","
    .. _dcmExportRule:

    dcmExportRule_"
    ":doc:`rsForwardRule` (s)",object,"RESTful Forward Rules. Supplements RESTful Forward rules specified on Device level.","
    .. _dcmRSForwardRule:

    dcmRSForwardRule_"
    ":doc:`archiveCompressionRule` (s)",object,"Compression rules. Supplements Compression rules specified on Device level.","
    .. _dcmArchiveCompressionRule:

    dcmArchiveCompressionRule_"
    ":doc:`archiveAttributeCoercion` (s)",object,"Attribute Coercion of received/sent DIMSE. Supplements Attribute Coercions specified on Device level.","
    .. _dcmArchiveAttributeCoercion:

    dcmArchiveAttributeCoercion_"
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policies. Supplements Study Retention Policies specified on Device level.","
    .. _dcmStudyRetentionPolicy:

    dcmStudyRetentionPolicy_"
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by this AE. Supplements Store Access Control Rules specified on Device level","
    .. _dcmStoreAccessControlIDRule:

    dcmStoreAccessControlIDRule_"
