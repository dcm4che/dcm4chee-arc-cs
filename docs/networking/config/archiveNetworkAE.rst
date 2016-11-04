Archive Network AE
==================
DICOM Archive Network AE related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Archive Network AE Attributes (LDAP Object: dcmArchiveNetworkAE)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Storage ID",string,"Storage ID","
    .. _dcmStorageID:

    dcmStorageID_"
    "Metadata Storage ID",string,"ID of Storage on which Metadata is stored in JSON format - additionally to the complete DICOM composite object. If absent, metadata is not stored additionally","
    .. _dcmMetadataStorageID:

    dcmMetadataStorageID_"
    "Store Access Control ID",string,"Access Contol ID assigned to Studies received by this AE","
    .. _dcmStoreAccessControlID:

    dcmStoreAccessControlID_"
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by this AE","
    .. _dcmStoreAccessControlIDRule:

    dcmStoreAccessControlIDRule_"
    "Access Control ID(s)",string,"Access Contol IDs assigned to Query/Retrieve requests received by this AE","
    .. _dcmAccessControlID:

    dcmAccessControlID_"
    "Overwrite Policy",string,"Overwrite Policy: NEVER, ALWAYS, SAME_SOURCE, SAME_SERIES or SAME_SOURCE_AND_SERIES. NEVER if absent.","
    .. _dcmOverwritePolicy:

    dcmOverwritePolicy_"
    "Accept Missing Patient ID",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. Enumerated values: YES, NO, CREATE. If absent, CREATE will be applied.","
    .. _dcmAcceptMissingPatientID:

    dcmAcceptMissingPatientID_"
    "Query/Retrieve View ID",string,"Query/Retrieve View Identifier","
    .. _dcmQueryRetrieveViewID:

    dcmQueryRetrieveViewID_"
    "Bulk Data Spool Directory",string,"Path to Bulk Data Spool Directory","
    .. _dcmBulkDataSpoolDirectory:

    dcmBulkDataSpoolDirectory_"
    "Hide SPS with Status(s)",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP","
    .. _dcmHideSPSWithStatusFromMWL:

    dcmHideSPSWithStatusFromMWL_"
    "Person Name Component Order Insensitive Matching",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names; disabled if absent","
    .. _dcmPersonNameComponentOrderInsensitiveMatching:

    dcmPersonNameComponentOrderInsensitiveMatching_"
    "Send Pending C-Get",boolean,"Enables pending C-GET responses; disabled if absent","
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
    "Store Permission Service URL",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http://host.name/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030}","
    .. _dcmStorePermissionServiceURL:

    dcmStorePermissionServiceURL_"
    "Store Permission Service Response Pattern",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" . If absent, every success response will be treated as agreement for storage.","
    .. _dcmStorePermissionServiceResponsePattern:

    dcmStorePermissionServiceResponsePattern_"
    "Allow Rejection For Data Retention Policy Expired",string,"Allow Rejection For Data Retention Policy Expired : NEVER, ALWAYS, STUDY_RETENTION_POLICY. If absent, STUDY_RETENTION_POLICY will be applied.","
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:

    dcmAllowRejectionForDataRetentionPolicyExpired_"
    "Accepted User Role(s)",string,"Roles of users from which web requests are accepted; any if absent.","
    .. _dcmAcceptedUserRole:

    dcmAcceptedUserRole_"
    "Allow Delete Study permanently",string,"Allow to delete Study permanently. Enumerated values: ALWAYS, REJECTED (= only already rejected Studies). If absent, REJECTED will be applied.","
    .. _dcmAllowDeleteStudyPermanently:

    dcmAllowDeleteStudyPermanently_"
    "Store Permission Service Expiration Date Pattern",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". If absent, locally configured Study Retention Policy Rules will be applied.","
    .. _dcmStorePermissionServiceExpirationDatePattern:

    dcmStorePermissionServiceExpirationDatePattern_"
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
    ":doc:`exportRule` (s)",object,"Export Rule","
    .. _dcmExportRule:

    dcmExportRule_"
    ":doc:`archiveCompressionRule` (s)",object,"Archive Compression rule","
    .. _dcmArchiveCompressionRule:

    dcmArchiveCompressionRule_"
    ":doc:`archiveAttributeCoercion` (s)",object,"Archive Attribute Coercion of received/sent DIMSE","
    .. _dcmArchiveAttributeCoercion:

    dcmArchiveAttributeCoercion_"
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policy","
    .. _dcmStudyRetentionPolicy:

    dcmStudyRetentionPolicy_"
