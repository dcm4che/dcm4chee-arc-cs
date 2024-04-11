Archive Network AE
==================
DICOM Archive Network AE related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Network AE Attributes (LDAP Object: dcmArchiveNetworkAE)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmObjectStorageID:

    :ref:`Object Storage ID(s) <dcmObjectStorageID>`",string,"ID of Storage System on which received DICOM composite objects are stored. Multiple Storage Systems may be configured.

    (dcmObjectStorageID)"
    "
    .. _dcmObjectStorageCount:

    :ref:`Object Storage Count <dcmObjectStorageCount>`",integer,"Number of Storage Systems which are filled in parallel.

    (dcmObjectStorageCount)"
    "
    .. _dcmMetadataStorageID:

    :ref:`Metadata Storage ID(s) <dcmMetadataStorageID>`",string,"ID of Storage on which Metadata is stored in JSON format - additionally to the complete DICOM composite object. Multiple Storage Systems may be configured. If absent, metadata is not stored additionally.

    (dcmMetadataStorageID)"
    "
    .. _dcmBulkDataDescriptorID:

    :ref:`Bulk Data Descriptor ID <dcmBulkDataDescriptorID>`",string,"ID of Bulk Data Descriptor applied by all services of this Archive Network AE providing Metadata of archived instances. Overwrites value specified on Device level.

    (dcmBulkDataDescriptorID)"
    "
    .. _dcmSeriesMetadataDelay:

    :ref:`Aggregate Series Metadata Delay <dcmSeriesMetadataDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for storing aggregated Series Metadata on storage of objects received by this AE. Overwrites value specified on Device level.

    (dcmSeriesMetadataDelay)"
    "
    .. _dcmPurgeInstanceRecordsDelay:

    :ref:`Purge Instance Records Delay <dcmPurgeInstanceRecordsDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS for purging Instance Records from the DB received by this AE. Overwrites value specified on Device level. Only effective, if Purge Instance Records on Device Level = true.

    (dcmPurgeInstanceRecordsDelay)"
    "
    .. _dcmStoreAccessControlID:

    :ref:`Store Access Control ID <dcmStoreAccessControlID>`",string,"Access Control ID assigned to Studies received by this AE

    (dcmStoreAccessControlID)"
    "
    .. _dcmAccessControlID:

    :ref:`Access Control ID(s) <dcmAccessControlID>`",string,"Access Control IDs assigned to Query/Retrieve requests received by this AE.

    (dcmAccessControlID)"
    "
    .. _dcmAcceptedMoveDestination:

    :ref:`Accepted Move Destination(s) <dcmAcceptedMoveDestination>`",string,"Accepted Move Destination in C-MOVE requests; any if absent.

    (dcmAcceptedMoveDestination)"
    "
    .. _dcmOverwritePolicy:

    :ref:`Overwrite Policy <dcmOverwritePolicy>`",string,"Overwrite Policy for Objects received by this AE. Overwrites value specified on Device level.

    Enumerated values:

    NEVER

    ALWAYS

    SAME_SOURCE

    SAME_SERIES

    SAME_SOURCE_AND_SERIES

    EVEN_WITH_EQUAL_DIGEST

    (dcmOverwritePolicy)"
    "
    .. _dcmRecordAttributeModification:

    :ref:`Record Attribute Modification <dcmRecordAttributeModification>`",boolean,"Indicates if modifications of attributes of stored objects by this AE are recorded in Items of the Original Attributes Sequence. Overwrites value specified on Device level.

    (dcmRecordAttributeModification)"
    "
    .. _dcmAcceptMissingPatientID:

    :ref:`Accept Missing Patient ID <dcmAcceptMissingPatientID>`",string,"Indicates if objects without Patient IDs shall be accepted and if a Patient ID shall be created. Overwrites value specified on Device level.

    Enumerated values:

    YES

    NO

    CREATE

    (dcmAcceptMissingPatientID)"
    "
    .. _dcmAcceptConflictingPatientID:

    :ref:`Accept Conflicting Patient ID <dcmAcceptConflictingPatientID>`",string,"Indicates if objects with a Patient IDs which differs from the Patient ID in previous received objects of the Study shall be accepted. Overwrites value specified on Device level.

    Enumerated values:

    YES

    NO

    MERGED

    (dcmAcceptConflictingPatientID)"
    "
    .. _dcmQueryRetrieveViewID:

    :ref:`Query/Retrieve View ID <dcmQueryRetrieveViewID>`",string,"Query/Retrieve View Identifier.

    (dcmQueryRetrieveViewID)"
    "
    .. _dcmBulkDataSpoolDirectory:

    :ref:`Bulk Data Spool Directory <dcmBulkDataSpoolDirectory>`",string,"Path to Bulk Data Spool Directory. Overwrites value specified on Device level.

    (dcmBulkDataSpoolDirectory)"
    "
    .. _dcmHideSPSWithStatusFromMWL:

    :ref:`Hide SPS with Status by MWL SCP(s) <dcmHideSPSWithStatusFromMWL>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL SCP. Overwrites value specified on Device level.

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

    :ref:`Hide SPS with Status by MWL RS(s) <dcmHideSPSWithStatusFromMWLRS>`",string,"Scheduled Procedure Step Status codes of MWL items which shall not be returned by the MWL RS. Overwrites value specified on Device level.

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
    .. _dcmMWLAccessionNumberGenerator:

    :ref:`MWL Accession Number Generator <dcmMWLAccessionNumberGenerator>`",string,"Identifies ID Generator to supplement missing Accession Numbers of Scheduled Procedures Steps created by RESTful service. Overwrites value specified on Device level.

    (dcmMWLAccessionNumberGenerator)"
    "
    .. _dcmMWLRequestedProcedureIDGenerator:

    :ref:`MWL Requested Procedure ID Generator <dcmMWLRequestedProcedureIDGenerator>`",string,"Identifies ID Generator to supplement missing Requested Procedure IDs of Scheduled Procedures Steps created by RESTful service. Overwrites value specified on Device level.

    (dcmMWLRequestedProcedureIDGenerator)"
    "
    .. _dcmMWLScheduledProcedureStepIDGenerator:

    :ref:`MWL Scheduled Procedure Step ID Generator <dcmMWLScheduledProcedureStepIDGenerator>`",string,"Identifies ID Generator to supplement missing Scheduled Procedure Step IDs of Scheduled Procedures Steps created by RESTful service. Overwrites value specified on Device level.

    (dcmMWLScheduledProcedureStepIDGenerator)"
    "
    .. _dcmEncodeAsJSONNumber:

    :ref:`Encode as JSON Number(s) <dcmEncodeAsJSONNumber>`",string,"VR encoded as JSON Number. If not listed, IS, DS, SV and UV values are encoded as JSON Strings. Supplements values specified on Device level.

    Enumerated values:

    DS

    IS

    SV

    UV

    (dcmEncodeAsJSONNumber)"
    "
    .. _dcmValidateCallingAEHostname:

    :ref:`Validate Calling AE Hostname <dcmValidateCallingAEHostname>`",boolean,"Validate Calling AE Hostname or IP Address of Association requestors for this AE. Overwrites value specified on Device level.

    (dcmValidateCallingAEHostname)"
    "
    .. _dcmUserIdentityNegotiation:

    :ref:`User Identity Negotiation <dcmUserIdentityNegotiation>`",string,"Specifies to ignore User Identity Negotiation Sub-Item in Association requests (=NOT_SUPPORTED), to verify passed Username and password or JSON Web Token are against a Keycloak server (=SUPPORTS), or to reject Association requests without a valid Username and password or JSON Web Token in its Identity Negotiation Sub-Item (=REQUIRED). Overwrites value specified on Device level.

    Enumerated values:

    NOT_SUPPORTED

    SUPPORTS

    REQUIRED

    (dcmUserIdentityNegotiation)"
    "
    .. _dcmUserIdentityNegotiationRole:

    :ref:`User Identity Negotiation Role <dcmUserIdentityNegotiationRole>`",string,"Constrain accepted User Identity Negotiation requests to users with specified role. Overwrites value specified on Device level.

    (dcmUserIdentityNegotiationRole)"
    "
    .. _dcmUserIdentityNegotiationKeycloakClientID:

    :ref:`User Identity Negotiation Keycloak Client ID <dcmUserIdentityNegotiationKeycloakClientID>`",string,"Keycloak Client ID referring Keycloak connection configuration for verifying passed username and password or JSON Web Token. Overwrites value specified on Device level.

    (dcmUserIdentityNegotiationKeycloakClientID)"
    "
    .. _dcmPersonNameComponentOrderInsensitiveMatching:

    :ref:`Person Name Component Order Insensitive Matching <dcmPersonNameComponentOrderInsensitiveMatching>`",boolean,"Indicates if name component order insensitive matching is performed on fuzzy semantic matching of person names by this AE. Overwrites value specified on Device level.

    (dcmPersonNameComponentOrderInsensitiveMatching)"
    "
    .. _dcmSendPendingCGet:

    :ref:`Send Pending C-Get <dcmSendPendingCGet>`",boolean,"Enables pending C-GET responses. Overwrites value specified on Device level.

    (dcmSendPendingCGet)"
    "
    .. _dcmSendPendingCMoveInterval:

    :ref:`Send Pending C-Move Interval <dcmSendPendingCMoveInterval>`",string,"Interval of pending C-MOVE responses in ISO-8601 duration format PnDTnHnMn.nS. Overwrites value specified on Device level.

    (dcmSendPendingCMoveInterval)"
    "
    .. _dcmWadoSR2HtmlTemplateURI:

    :ref:`Wado SR2Html Template URI <dcmWadoSR2HtmlTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to html. Overwrites value specified on Device level.

    (dcmWadoSR2HtmlTemplateURI)"
    "
    .. _dcmWadoSR2TextTemplateURI:

    :ref:`Wado SR2Text Template URI <dcmWadoSR2TextTemplateURI>`",string,"Specifies URI for the style sheet used to render structured reports to plain text. Overwrites value specified on Device level.

    (dcmWadoSR2TextTemplateURI)"
    "
    .. _dcmWadoCDA2HtmlTemplateURI:

    :ref:`Wado CDA to HTML Template URI <dcmWadoCDA2HtmlTemplateURI>`",string,"URL to XSL style sheet inserted as <?xml-stylesheet type=""text/xsl"" href=""<url>"" > in CDA documents returned by WADO-URI service. If absent, the embedded CDI document is returned verbatim. Overwrites value specified on Device level.

    (dcmWadoCDA2HtmlTemplateURI)"
    "
    .. _dcmWadoThumbnailViewport:

    :ref:`Wado Thumbnail Viewport <dcmWadoThumbnailViewport>`",string,"Dimension of Thumbnails returned by WADO retrieve of Instance Thumbnails, if no Viewport is specified in the request. Format: <width>,<height>. Overwrites value specified on Device level.

    (dcmWadoThumbnailViewport)"
    "
    .. _dcmWadoZIPEntryNameFormat:

    :ref:`Wado ZIP Entry Name Format <dcmWadoZIPEntryNameFormat>`",string,"Format of entry names in ZIP archive returned by WADO-RS. Overwrites value specified on Device level.

    (dcmWadoZIPEntryNameFormat)"
    "
    .. _dcmWadoIgnorePresentationLUTShape:

    :ref:`Wado Ignore Presentation LUT Shape <dcmWadoIgnorePresentationLUTShape>`",boolean,"Indicates to ignore (2050,0020) Presentation LUT Shape, but prioritize value of (0028,0004) Photometric Interpretation to determine if minimum sample value is intended to be displayed as white (=MONCHROME1) or as black (=MONCHROME2) on retrieve of rendered DICOM images by WADO-RS or WADO-URI services. Overwrites value specified on Device level.

    (dcmWadoIgnorePresentationLUTShape)"
    "
    .. _dcmWadoMetadataExcludePrivate:

    :ref:`Wado Metadata Exclude Private <dcmWadoMetadataExcludePrivate>`",boolean,"Indicates to exclude Private Data Elements from Metadata returned by WADO-RS Retrieve Transaction. Overwrites value specified on Device level.

    (dcmWadoMetadataExcludePrivate)"
    "
    .. _dcmQueryMaxNumberOfResults:

    :ref:`Query Max Number Of Results <dcmQueryMaxNumberOfResults>`",integer,"Maximal number of return results by C-FIND SCP. If the number of matches extends the limit, the C-FIND request will be refused. 0 = no limitation. Overwrites value specified on Device level.

    (dcmQueryMaxNumberOfResults)"
    "
    .. _dcmQidoMaxNumberOfResults:

    :ref:`Qido Max Number Of Results <dcmQidoMaxNumberOfResults>`",integer,"Maximal number of return results by QIDO-RS Service. 0 = unlimited. Overwrites value specified on Device level.

    (dcmQidoMaxNumberOfResults)"
    "
    .. _dcmQidoETag:

    :ref:`Qido ETag <dcmQidoETag>`",boolean,"Indicates to return Last-Modified and ETag for Search Series or Instances of a Study. Overwrites value specified on Device level.

    (dcmQidoETag)"
    "
    .. _dcmFwdMppsDestination:

    :ref:`Mpps Forward Destination(s) <dcmFwdMppsDestination>`",string,"Destination to forward MPPS N-CREATE RQ and N-SET RQ. Overwrites value specified on Device level.

    (dcmFwdMppsDestination)"
    "
    .. _dcmIanDestination:

    :ref:`Ian Destination(s) <dcmIanDestination>`",string,"Destination to send IAN N-CREATE RQ. Overwrites value specified on Device level.

    (dcmIanDestination)"
    "
    .. _dcmIanDelay:

    :ref:`IAN Delay <dcmIanDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an IAN for a received study is sent to configured IAN destinations. Overwrites value specified on Device level.

    (dcmIanDelay)"
    "
    .. _dcmIanTimeout:

    :ref:`IAN Timeout <dcmIanTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS. Overwrites value specified on Device level.

    (dcmIanTimeout)"
    "
    .. _dcmIanOnTimeout:

    :ref:`IAN On Timeout <dcmIanOnTimeout>`",boolean,"Specifies if the IAN is sent if the timeout for waiting on receive of instances referenced is exceeded. Overwrites value specified on Device level.

    (dcmIanOnTimeout)"
    "
    .. _dcmSpanningCFindSCP:

    :ref:`Spanning C-Find SCP <dcmSpanningCFindSCP>`",string,"AE Title of external C-FIND SCP to forward C-FIND RQs and backward responses according configured Spanning C-Find SCP Policy. Overwrites value specified on Device level.

    (dcmSpanningCFindSCP)"
    "
    .. _dcmSpanningCFindSCPPolicy:

    :ref:`Spanning C-Find SCP Policy <dcmSpanningCFindSCPPolicy>`",string,"Specifies policy for combining matches returned from configured Spanning C-Find SCP with matching entries from the archive DB. SUPPLEMENT (= returns local matches before additional matches from Spanning C-Find SCP ), MERGE (= returns matches from Spanning C-Find SCP before additional local matches), REPLACE (= returns only matches from Spanning C-Find SCP). Overwrites value specified on Device level.

    Enumerated values:

    SUPPLEMENT

    MERGE

    REPLACE

    (dcmSpanningCFindSCPPolicy)"
    "
    .. _dcmSpanningCFindSCPRetrieveAET:

    :ref:`Spanning C-Find SCP Retrieve AE Title(s) <dcmSpanningCFindSCPRetrieveAET>`",string,"Specifies Retrieve AE Title(s) in returned matches from Spanning C-Find SCP. Overwrites value specified on Device level.

    (dcmSpanningCFindSCPRetrieveAET)"
    "
    .. _dcmFallbackCMoveSCP:

    :ref:`Fallback C-Move SCP <dcmFallbackCMoveSCP>`",string,"AE Title of external C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not managed by this archive. Overwrites value specified on Device level.

    (dcmFallbackCMoveSCP)"
    "
    .. _dcmFallbackCMoveSCPStudyOlderThan:

    :ref:`Fallback C-Move SCP Study Older Than <dcmFallbackCMoveSCPStudyOlderThan>`",string,"Specifies threshold for Study Date in format YYYYMMDD for marking received Studies as (potential) incomplete to enforce the retrieve from configured dcmFallbackCMoveSCP. Overwrites value specified on Device level.

    (dcmFallbackCMoveSCPStudyOlderThan)"
    "
    .. _dcmFallbackCMoveSCPDestination:

    :ref:`Fallback C-Move SCP Destination <dcmFallbackCMoveSCPDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to the external C-MOVE SCP specified by dcmFallbackCMoveSCP. Overwrites value specified on Device level.

    (dcmFallbackCMoveSCPDestination)"
    "
    .. _dcmFallbackCMoveSCPLeadingCFindSCP:

    :ref:`Fallback C-Move SCP Leading C-Find SCP <dcmFallbackCMoveSCPLeadingCFindSCP>`",string,"AE Title of external C-FIND SCP for Verification of Number of Instances retrieved from external C-MOVE SCP specified by dcmFallbackCMoveSCP. Overwrites value specified on Device level.

    (dcmFallbackCMoveSCPLeadingCFindSCP)"
    "
    .. _dcmFallbackCMoveSCPRetries:

    :ref:`Fallback C-Move SCP Retries <dcmFallbackCMoveSCPRetries>`",integer,"Maximal number of retries to retrieve not available objects from C-MOVE SCP configured by dcmFallbackCMoveSCP. -1 = forever. Overwrites value specified on Device level.

    (dcmFallbackCMoveSCPRetries)"
    "
    .. _dcmFallbackWadoURIWebAppName:

    :ref:`Fallback WADO-URI Web Application Name <dcmFallbackWadoURIWebAppName>`",string,"Name of external Web Application to redirect WADO-URI requests if the requested Object is not available by this archive. Overwrites value specified on Device level.

    (dcmFallbackWadoURIWebAppName)"
    "
    .. _dcmFallbackWadoURIHttpStatusCode:

    :ref:`Fallback WADO-URI HTTP Status Code <dcmFallbackWadoURIHttpStatusCode>`",integer,"HTTP Status code of Redirect Response configured by Fallback WADO-URI Web Application Name. Overwrites value specified on Device level.

    Enumerated values:

    301

    302

    303

    307

    (dcmFallbackWadoURIHttpStatusCode)"
    "
    .. _dcmFallbackWadoURIRedirectOnNotFound:

    :ref:`Fallback WADO-URI Redirect On Not Found <dcmFallbackWadoURIRedirectOnNotFound>`",boolean,"Indicates if WADO-URI requests are redirected to configured Fallback WADO-URI Web Application Name even if the object was not found or - if set to false - only if the object is no longer accessible on this archive. Overwrites value specified on Device level.

    (dcmFallbackWadoURIRedirectOnNotFound)"
    "
    .. _dcmExternalWadoRSWebAppName:

    :ref:`External WADO-RS Web Application Name <dcmExternalWadoRSWebAppName>`",string,"Name of external Web Application to redirect WADO-RS requests if the requested Object is not available by this archive. Overwrites value specified on Device level.

    (dcmExternalWadoRSWebAppName)"
    "
    .. _dcmExternalWadoRSHttpStatusCode:

    :ref:`External WADO-RS HTTP Status Code <dcmExternalWadoRSHttpStatusCode>`",integer,"HTTP Status code of Redirect Response configured by External WADO-RS Web Application Name. Overwrites value specified on Device level.

    Enumerated values:

    301

    302

    303

    307

    (dcmExternalWadoRSHttpStatusCode)"
    "
    .. _dcmExternalWadoRSRedirectOnNotFound:

    :ref:`External WADO-RS Redirect On Not Found <dcmExternalWadoRSRedirectOnNotFound>`",boolean,"Indicates if WADO-RS requests are redirected to configured External WADO-RS Web Application Name even if the requested objects were not found or - if set to false - only if some of the requested objects are no longer accessible on this archive. Overwrites value specified on Device level.

    (dcmExternalWadoRSRedirectOnNotFound)"
    "
    .. _dcmFallbackCMoveSCPCallingAET:

    :ref:`Fallback C-Move SCP Calling AE title <dcmFallbackCMoveSCPCallingAET>`",string,"Calling AE Title used in A-ASSOCIATE-RQ to configured Fallback C-MOVE SCP. If absent, the AE Title of the external C-MOVE SCU is used. Overwrites value specified on Device level.

    (dcmFallbackCMoveSCPCallingAET)"
    "
    .. _dcmAltCMoveSCP:

    :ref:`Alternative C-Move SCP <dcmAltCMoveSCP>`",string,"AE Title of alternative C-MOVE SCP to forward C-MOVE RQs if the requested Entities are not located on a local attached Storage. Overwrites value specified on Device level.

    (dcmAltCMoveSCP)"
    "
    .. _dcmStorePermissionServiceURL:

    :ref:`Store Permission Service URL <dcmStorePermissionServiceURL>`",string,"URL of Store Permission Service which will be invoked on receive of the first object of a study. {<dicomTag>} will be replaced by the value of the attribute in the object. E.g. http(s)://<store-permission-service-provider-host>:<store-permission-service-provider-port>/storage-permission/study/{0020000D}?patientId={00100020}&patientIdIssuer={00100021}&studyDescription={00081030,urlencoded}. Overwrites value specified on Device level.

    (dcmStorePermissionServiceURL)"
    "
    .. _dcmStorePermissionServiceResponse:

    :ref:`Store Permission Service Response <dcmStorePermissionServiceResponse>`",string,"Emulate Store Permission Service Response on receive of the first object of a study. {<dicomTag>} will be replaced by the value of the attribute in the object. Only effective if no Store Permission Service Response is configured. Example: patientID={00100020},patientName={00100010},errorCode=0110H,errorComment=errorMessage. Overwrites value specified on Device level.

    (dcmStorePermissionServiceResponse)"
    "
    .. _dcmStorePermissionServiceResponsePattern:

    :ref:`Store Permission Service Response Pattern <dcmStorePermissionServiceResponsePattern>`",string,"Regular Expression applied to responses from Store Permission Service to determine agreement for storage. E.g. ""validation""\s*:\s*""true"" or '(?<=patientName=)[^null].*?(?=,)'. Overwrites value specified on Device level.

    (dcmStorePermissionServiceResponsePattern)"
    "
    .. _dcmStorePermissionServiceErrorCommentPattern:

    :ref:`Store Permission Service Error Comment Pattern <dcmStorePermissionServiceErrorCommentPattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Comment. E.g. ""errorcomment""\s*:\s*""(.*)"". Overwrites value specified on Device level.

    (dcmStorePermissionServiceErrorCommentPattern)"
    "
    .. _dcmStorePermissionServiceErrorCodePattern:

    :ref:`Store Permission Service Error Code Pattern <dcmStorePermissionServiceErrorCodePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract Error Code in hexadecimal. E.g. ""errorcode""\s*:\s*""(\p{XDigit}{4})"". Overwrites value specified on Device level.

    (dcmStorePermissionServiceErrorCodePattern)"
    "
    .. _dcmStorePermissionServiceExpirationDatePattern:

    :ref:`Store Permission Service Expiration Date Pattern <dcmStorePermissionServiceExpirationDatePattern>`",string,"Regular Expression applied to responses from Store Permission Service to extract the initial Study Expiration Date. E.g. ""expirationdate""\s*:\s*""([0-9]{8})"". Overwrites value specified on Device level.

    (dcmStorePermissionServiceExpirationDatePattern)"
    "
    .. _dcmAllowRejectionForDataRetentionPolicyExpired:

    :ref:`Allow Rejection For Data Retention Policy Expired <dcmAllowRejectionForDataRetentionPolicyExpired>`",string,"Allow Rejection For Data Retention Policy Expired. Overwrites value specified on Device level.

    Enumerated values:

    NEVER

    ALWAYS

    EXPIRED_UNSET

    ONLY_EXPIRED

    (dcmAllowRejectionForDataRetentionPolicyExpired)"
    "
    .. _dcmAcceptedUserRole:

    :ref:`Accepted User Role(s) <dcmAcceptedUserRole>`",string,"Roles of users from which web requests are accepted; any if absent.

    (dcmAcceptedUserRole)"
    "
    .. _dcmAllowDeleteStudyPermanently:

    :ref:`Allow Delete Study permanently <dcmAllowDeleteStudyPermanently>`",string,"Allow to delete Study permanently. REJECTED = only already rejected Studies. Overwrites value specified on Device level.

    Enumerated values:

    ALWAYS

    REJECTED

    (dcmAllowDeleteStudyPermanently)"
    "
    .. _dcmAllowDeletePatient:

    :ref:`Allow Delete Patient <dcmAllowDeletePatient>`",string,"Allow permanent deletion of Patients. Enumerated values: NEVER, ALWAYS, WITHOUT_STUDIES. Overwrites value specified on Device level.

    Enumerated values:

    NEVER

    ALWAYS

    WITHOUT_STUDIES

    (dcmAllowDeletePatient)"
    "
    .. _dcmDefaultCharacterSet:

    :ref:`Default Character Set <dcmDefaultCharacterSet>`",string,"Value of Specific Character Set (0008,0005) added to Data Sets of C-STORE RQs and pending C-FIND RSPs without Specific Character Set (0008,0005) attribute received by this Network AE. Overwrites value specified on Device level.

    (dcmDefaultCharacterSet)"
    "
    .. _dcmMWLWorklistLabel:

    :ref:`MWL Worklist Label <dcmMWLWorklistLabel>`",string,"Only consider MWL items with this or no Worklist Label (0074,1202) for matching by this Archive AE acting as MWP SCP. If absent, MWL items with any Value of Worklist Label (0074,1202) are considered for matching by this Archive AE acting as MWL SCP.

    (dcmMWLWorklistLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`UPS Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) of created UPS by this Network AE, if the UPS Push SCU or UPS-RS User Agent does not provide a value for this attribute. If absent, the AE Title of the receiving AE will be used. Overwrites value specified on Device level.

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSEventSCU:

    :ref:`UPS Event SCU(s) <dcmUPSEventSCU>`",string,"AE Title of UPS Event SOP Class SCU, to which UPS Event Reports are sent for subscriptions created on this Network AE  - independently if the subscription was created by the N-ACTION DIMSE service, or by a corresponding UPS RESTful service. Overwrites value specified on Device level.

    (dcmUPSEventSCU)"
    "
    .. _dcmUPSEventSCUKeepAlive:

    :ref:`UPS Event SCU Keep Alive <dcmUPSEventSCUKeepAlive>`",integer,"Timeout in ms to keep associations to UPS Event SCUs alive. If absent, associations will not be reused for sending multiple UPS Event Reports to one UPS Event SCU. Overwrites value specified on Device level.

    (dcmUPSEventSCUKeepAlive)"
    "
    .. _dcmRetrieveAET:

    :ref:`Retrieve AE Title(s) <dcmRetrieveAET>`",string,"Specifies Retrieve AE Titles associated with DICOM objects received by this Network AE. Overwrites value specified on Device level.

    (dcmRetrieveAET)"
    "
    .. _dcmReturnRetrieveAET:

    :ref:`Return Retrieve AE Title(s) <dcmReturnRetrieveAET>`",string,"Retrieve AE Title returned in C-FIND and QIDO responses. If absent, the Retrieve AET associated with the archived entity will be returned. Overwrites value specified on Device level.

    (dcmReturnRetrieveAET)"
    "
    .. _dcmMultipleStoreAssociations:

    :ref:`Multiple Store Associations(s) <dcmMultipleStoreAssociations>`",string,"Number of Storage Associations used for retrieve of Composite Objects. C-STORE SCP specific numbers can be specified by prefix '<AETitle>:'. Examples : 2 or STORESCP:3 Supplements Multiple Store Associations specified on Device level.

    (dcmMultipleStoreAssociations)"
    "
    .. _dcmExternalRetrieveAEDestination:

    :ref:`External Retrieve AE Destination <dcmExternalRetrieveAEDestination>`",string,"AE Title of local C-STORE-SCP to be set as Move Destination in C-MOVE RQs forwarded to external retrieve AE. Overwrites value specified on Device level.

    (dcmExternalRetrieveAEDestination)"
    "
    .. _dcmCopyMoveUpdatePolicy:

    :ref:`Copy Move Update Policy <dcmCopyMoveUpdatePolicy>`",string,"Specifies update policy for attributes of the destination Study on Copy/Move of Instances from another Study. If absent, the attributes will not be updated. Overwrites value specified on Device level.

    Enumerated values:

    PRESERVE

    SUPPLEMENT

    MERGE

    OVERWRITE

    REPLACE

    (dcmCopyMoveUpdatePolicy)"
    "
    .. _dcmLinkMWLEntryUpdatePolicy:

    :ref:`Link MWL Entry Update Policy <dcmLinkMWLEntryUpdatePolicy>`",string,"Specifies update policy for Study attributes on Link of Instances of another Study with a MWL Entry referring an existing Study. Overwrites value specified on Device level.

    Enumerated values:

    PRESERVE

    SUPPLEMENT

    MERGE

    OVERWRITE

    REPLACE

    (dcmLinkMWLEntryUpdatePolicy)"
    "
    .. _dcmStorageVerificationPolicy:

    :ref:`Storage Verification Policy <dcmStorageVerificationPolicy>`",string,"DB_RECORD_EXISTS: only check for existence of DB records, OBJECT_EXISTS: check if object exists on Storage System, OBJECT_SIZE: check size of object on Storage System, OBJECT_FETCH: fetch object from Storage System), OBJECT_CHECKSUM: recalculate checksum of object on Storage System, S3_MD5SUM: check MD5 checksum of object on S3 Storage System. Overwrites value specified on Device level.

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

    :ref:`Storage Verification Update Location Status <dcmStorageVerificationUpdateLocationStatus>`",boolean,"Indicates if the Status of the Location DB record shall be updated on Storage Verification accordingly. Not effective with Storage Verification Policy: DB_RECORD_EXISTS. Overwrites value specified on Device level.

    (dcmStorageVerificationUpdateLocationStatus)"
    "
    .. _dcmStorageVerificationStorageID:

    :ref:`Storage Verification Storage IDs(s) <dcmStorageVerificationStorageID>`",string,"Only accept Storage Verification if the validation of the storage of the object on one of the specified Storage Systems is successful. Not effective with Storage Verification Policy: DB_RECORD_EXISTS. Overwrites values specified on Device level.

    (dcmStorageVerificationStorageID)"
    "
    .. _dcmStorageVerificationInitialDelay:

    :ref:`Storage Verification Initial Delay <dcmStorageVerificationInitialDelay>`",string,"Delay in ISO-8601 duration format PnYnMnD or PnW of first Storage Verification of a Series after it was received. Overwrites values specified on Device level.

    (dcmStorageVerificationInitialDelay)"
    "
    .. _dcmUpdateLocationStatusOnRetrieve:

    :ref:`Update Location Status on Retrieve <dcmUpdateLocationStatusOnRetrieve>`",boolean,"Indicates if the Status of the Location DB record shall be updated for objects failed to get fetched from storage on retrieve to MISSING_OBJECT or FAILED_TO_FETCH_OBJECT. Overwrites value specified on Device level.

    (dcmUpdateLocationStatusOnRetrieve)"
    "
    .. _dcmStorageVerificationOnRetrieve:

    :ref:`Storage Verification on Retrieve <dcmStorageVerificationOnRetrieve>`",boolean,"Indicates if failures to fetch an object from Storage on retrieve shall trigger a Storage Verification of the whole Series. Overwrites value specified on Device level.

    (dcmStorageVerificationOnRetrieve)"
    "
    .. _hl7PSUSendingApplication:

    :ref:`HL7 Procedure Status Update Sending Application <hl7PSUSendingApplication>`",string,"Application|Facility name of Sending Application for HL7 Procedure Status Update. Overwrites value specified on Device level.

    (hl7PSUSendingApplication)"
    "
    .. _hl7PSUReceivingApplication:

    :ref:`HL7 Procedure Status Update Receiving Application(s) <hl7PSUReceivingApplication>`",string,"Application|Facility name of Receiving Application for HL7 Procedure Status Update. Overwrites value specified on Device level.

    (hl7PSUReceivingApplication)"
    "
    .. _hl7PSUDelay:

    :ref:`HL7 Procedure Status Update Delay <hl7PSUDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which an HL7 Procedure Status Update for a received study is sent to configured HL7 receivers. If absent, HL7 Procedure Status Update is triggered by received MPPS. Overwrites value specified on Device level.

    (hl7PSUDelay)"
    "
    .. _hl7PSUStudyTemplateURI:

    :ref:`HL7 Procedure Status Update Study Template URI <hl7PSUStudyTemplateURI>`",string,"URL of XSL style sheet to create HL7v2 message to notify configured HL7 receivers about changes of the Status of requested Procedures triggered by received Study. Overwrites value specified on Device level.

    (hl7PSUStudyTemplateURI)"
    "
    .. _hl7PSUTimeout:

    :ref:`HL7 Procedure Status Update Timeout <hl7PSUTimeout>`",string,"Timeout in ISO-8601 duration format PnDTnHnMn.nS for waiting on receive of instances referenced in MPPS. Overwrites value specified on Device level.

    (hl7PSUTimeout)"
    "
    .. _hl7PSUOnTimeout:

    :ref:`HL7 Procedure Status Update On Timeout <hl7PSUOnTimeout>`",boolean,"Specifies if the HL7 Procedure Status Update is sent if the timeout for waiting on receive of instances referenced is exceeded. Overwrites value specified on Device level.

    (hl7PSUOnTimeout)"
    "
    .. _hl7PSUMppsTemplateURI:

    :ref:`HL7 Procedure Status Update MPPS Template URI <hl7PSUMppsTemplateURI>`",string,"URL of XSL style sheet to create HL7v2 message to notify configured HL7 receivers about changes of the Status of requested Procedures triggered by MPPS. Overwrites value specified on Device level.

    (hl7PSUMppsTemplateURI)"
    "
    .. _hl7PSUCondition:

    :ref:`HL7 Procedure Status Update Conditions(s) <hl7PSUCondition>`",string,"Restrict notification of configured HL7 Procedure Status Update Receiving Applications about Procedure Status Update by conditions on attributes of received composite object in format {key}[!]={value}. Refer `applicability, format and some examples <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_. Overwrites value specified on Device level.

    (hl7PSUCondition)"
    "
    .. _hl7PSUForRequestedProcedure:

    :ref:`HL7 Procedure Status Update for Requested Procedure <hl7PSUForRequestedProcedure>`",boolean,"Restrict notification of configured HL7 Procedure Status Update Receiving Applications about Procedure Status Update to existence of Scheduled Procedure Steps of a Requested Procedure (MWL Items in the DB) with matching Study Instance UID. Overwrites value specified on Device level.

    (hl7PSUForRequestedProcedure)"
    "
    .. _hl7PSUTemplateParam:

    :ref:`HL7 Procedure Status Update Template Parameters(s) <hl7PSUTemplateParam>`",string,"XSLT parameters in format {attributeID}={value} passed to style sheet specified by HL7 Procedure Status Update MPPS Template URI or HL7 Procedure Status Update Study Template URI. {attributeID} inside of {value} will be replaced by the value of that attribute in the original dataset. E.g.: 'RequestedProcedureID={StudyInstanceUID,hash}' or 'AccessionNumber={0020000D,hash}'. Overwrites value specified on Device level.

    (hl7PSUTemplateParam)"
    "
    .. _hl7PSUMessageType:

    :ref:`HL7 Procedure Status Update Message Type <hl7PSUMessageType>`",string,"Message Type of HL7 Procedure Status Update message. Overwrites value specified on Device level.

    Enumerated values:

    OMG_O19

    ORU_R01

    OMI_O23

    (hl7PSUMessageType)"
    "
    .. _hl7PSUPIDPV1:

    :ref:`HL7 Procedure Status Update PID PV1 <hl7PSUPIDPV1>`",boolean,"Indicates to include a Patient Identification (PID) and a Patient Visit (PV1) segment in the HL7 Procedure Status Update message. Implicitly set, if HL7 Procedure Status Message Type = ORU_R01. Overwrites value specified on Device level.

    (hl7PSUPIDPV1)"
    "
    .. _hl7PSUMWL:

    :ref:`HL7 Procedure Status Update MWL <hl7PSUMWL>`",boolean,"Specifies if the Status of MWL Items in the DB is updated to COMPLETED for a received study after the configured HL7 Procedure Status Update Delay. Implicitly set to true, if notification to HL7 receivers is configured, triggered by received studies associated with MWL. Overwrites value specified on Device level.

    (hl7PSUMWL)"
    "
    .. _hl7PSUMWLMatchingKey:

    :ref:`HL7 Procedure Status Update MWL Matching Key <hl7PSUMWLMatchingKey>`",string,"Specifies attribute of received object to lookup MWL Item whose status is to be updated to COMPLETED. Only applicable is 'HL7 Procedure Status Update MWL' is configured as or implicitly set to true. Overwrites value specified on Device level.

    Enumerated values:

    AccessionNumber

    StudyInstanceUID

    (hl7PSUMWLMatchingKey)"
    "
    .. _dcmRelationalQueryNegotiationLenient:

    :ref:`Relational Query Negotiation Lenient <dcmRelationalQueryNegotiationLenient>`",boolean,"Indicates to accept C-FIND RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated. Overwrites value specified on Device level.

    (dcmRelationalQueryNegotiationLenient)"
    "
    .. _dcmRelationalRetrieveNegotiationLenient:

    :ref:`Relational Retrieve Negotiation Lenient <dcmRelationalRetrieveNegotiationLenient>`",boolean,"Indicates to accept C-MOVE and C-GET RQs without unique keys for levels above the query level also if support for relational-queries was not negotiated. Overwrites value specified on Device level. Overwrites value specified on Device level.

    (dcmRelationalRetrieveNegotiationLenient)"
    "
    .. _dcmRestrictRetrieveSilently:

    :ref:`Restrict Retrieve Silently <dcmRestrictRetrieveSilently>`",boolean,"Indicates if the set of requested objects to retrieve shall be silently (=without counting not transferred object as failures) restricted according the Transfer Capabilities of the Retrieve Destination. Otherwise the number of requested objects for which no Transfer Capability is configured for the Retrieve Destination and therefore are not retrieved is counted as failures. Only effective, if the Retrieve Destination has configured at least one Transfer Capability with SCP role. Overwrites value specified on Device level.

    (dcmRestrictRetrieveSilently)"
    "
    .. _dcmRejectConflictingPatientAttribute:

    :ref:`Reject Conflicting Patient Attribute(s) <dcmRejectConflictingPatientAttribute>`",string,"DICOM Tag of Patient Attribute which have to match in received objects with the value in previous received objects with equal Patient ID to be accepted. Overwrites value specified on Device level.

    (dcmRejectConflictingPatientAttribute)"
    "
    .. _dcmStowRetiredTransferSyntax:

    :ref:`STOW Retired Transfer Syntax <dcmStowRetiredTransferSyntax>`",boolean,"Store received JPEG Full Progression, Non-Hierarchical JPEG images in DICOM images with corresponding (retired) Transfer Syntax UID 1.2.840.10008.1.2.4.55. Otherwise set 1.2.840.10008.1.2.4.50 (= JPEG Baseline) or 1.2.840.10008.1.2.4.51 (= JPEG Extended) as Transfer Syntax UID of the stored DICOM image, without transcoding to JPEG Baseline or JPEG Extended, but including the JPEG image as received. Overwrites value specified on Device level.

    (dcmStowRetiredTransferSyntax)"
    "
    .. _dcmStowExcludeAPPMarkers:

    :ref:`STOW Exclude Application Markers <dcmStowExcludeAPPMarkers>`",boolean,"Indicates if APP markers in JPEG images received in STOW-RS Metadata and Bulkdata requests shall be excluded from the JPEG bit streams encapsulated in created DICOM instances. Overwrites value specified on Device level.

    (dcmStowExcludeAPPMarkers)"
    "
    .. _dcmStowQuicktime2MP4:

    :ref:`STOW Quicktime to MP4 <dcmStowQuicktime2MP4>`",boolean,"Indicates if QuickTime containers received in STOW-RS Metadata and Bulkdata requests shall be converted to MP4 containers encapsulated in created DICOM instances. The conversion requires that ffmpeg is installed and the ffmpeg CLI utility is available in the PATH. Otherwise Quicktime containers will get encapsulated in the stored DICOM object verbatim, with a declared DICOM MPEG-4 Transfer Syntax which reflects the encoding of the video stream in the container, but contradicts the actual container format. Overwrites value specified on Device level.

    (dcmStowQuicktime2MP4)"
    "
    .. _dcmStowMaxFragmentLength:

    :ref:`STOW Maximum Fragment Length <dcmStowMaxFragmentLength>`",integer,"Maximum length of data fragments of encapsulated JPEG/MPEG stream in stored DICOM object. If the received JPEG/MPEG stream exceeds that value, it will be split into several fragments, using a Fragmentable Encapsulated Transfer Syntax. Valid range: 1024..4294967294. Overwrites value specified on Device level.

    (dcmStowMaxFragmentLength)"
    "
    .. _dcmRetrieveTaskWarningOnNoMatch:

    :ref:`Retrieve Task Warning on no Match <dcmRetrieveTaskWarningOnNoMatch>`",boolean,"Indicates if the result status of Retrieve Tasks shall be set to WARNING if none of the requested objects was found on the C-MOVE SCP. Overwrites value specified on Device level.

    (dcmRetrieveTaskWarningOnNoMatch)"
    "
    .. _dcmRetrieveTaskWarningOnWarnings:

    :ref:`Retrieve Task Warning on Warnings <dcmRetrieveTaskWarningOnWarnings>`",boolean,"Indicates if the result status of Retrieve Tasks shall be set to WARNING if there are Warning Sub-Operations, even if the retrieve of all objects was successful. Overwrites value specified on Device level

    (dcmRetrieveTaskWarningOnWarnings)"
    "
    .. _dcmChangeRequesterAET:

    :ref:`Change Requester AET <dcmChangeRequesterAET>`",string,"Indicates change requester AET in rejections triggered by archive. Overwrites value specified on Device level.

    (dcmChangeRequesterAET)"
    "
    .. _dcmFilterByIssuerOfPatientID:

    :ref:`Filter by Issuer of Patient ID <dcmFilterByIssuerOfPatientID>`",boolean,"Filter by Issuer of Patient ID even if no matching key for Patient ID is specified. Overwrites value specified on Device level.

    (dcmFilterByIssuerOfPatientID)"
    "
    .. _dcmMatchSOPClassOnInstanceLevel:

    :ref:`Match SOP Class on Instance level <dcmMatchSOPClassOnInstanceLevel>`",boolean,"Indicates to consider the SOP Class UID on Instance level for calculation of matches with SOP Classes in Study (0008,0062); otherwise rely on stored SOP Class UID on Series level, which may result in missing matches if one Series includes Instances of different SOP Classes. Overwrites value specified on Device level.

    (dcmMatchSOPClassOnInstanceLevel)"
    "
    .. _dcmUPSUpdateWithoutTransactionUID:

    :ref:`UPS Update Without Transaction UID <dcmUPSUpdateWithoutTransactionUID>`",boolean,"Indicates to permit an UPS Pull SCU or UPS-RS Web client to update or change the state of an UPS workitem in state IN PROCESS without specifying a Transaction UID. Overwrites value specified on Device level.

    (dcmUPSUpdateWithoutTransactionUID)"
    ":doc:`exportRule` (s)",object,"Export Rules applied to DICOM objects received by this AE. Supplements Export Rules specified on Device level."
    ":doc:`exportPriorsRule` (s)",object,"Export Priors Rules applied to DICOM objects received by this AE. Supplements Export Priors Rules specified on Device level."
    ":doc:`mppsForwardRule` (s)",object,"MPPS Forward Rules applied to MPPS received by this AE. Supplements MPPS Forward Rules specified on Device level."
    ":doc:`rsForwardRule` (s)",object,"RESTful Forward Rules. Supplements RESTful Forward rules specified on Device level."
    ":doc:`archiveCompressionRule` (s)",object,"Compression rules. Supplements Compression rules specified on Device level."
    ":doc:`archiveAttributeCoercion` (s)",object,"Attribute Coercion of received/sent DIMSE. Supplements Attribute Coercions specified on Device level."
    ":doc:`archiveAttributeCoercion2` (s)",object,"Attribute Coercion of received/sent DIMSE. Supplements Attribute Coercions specified on Device level."
    ":doc:`studyRetentionPolicy` (s)",object,"Study Retention Policies. Supplements Study Retention Policies specified on Device level."
    ":doc:`storeAccessControlIDRule` (s)",object,"Store Access Control Rules applied to Studies received by this AE. Supplements Store Access Control Rules specified on Device level."
    ":doc:`upsOnStore` (s)",object,"UPS on Store Rules applied to DICOM objects received by this AE. Supplements UPS on Store Rules specified on Device level."
    ":doc:`upsOnUPSCompleted` (s)",object,"UPS on UPS Completed Rules applied to UPS managed by this AE. Supplements UPS on UPS Completed Rules specified on Device level."
