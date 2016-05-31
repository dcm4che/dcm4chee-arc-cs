Functional Definitions of AEs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _storage:

Storage Application Entity
""""""""""""""""""""""""""

The existence of a send-job queue entry with associated network destination will activate the Storage AE. An association request is sent to the destination AE and upon successful negotiation of a Presentation Context the image transfer is started. If the association cannot be opened, the related send-job is set to an error state and can be restarted by the user via job control interface. By default, the Storage AE will not try to initiate another association for this send-job automatically. However, an automatic retry (retry-timer, retry­count) can be configured by a CSE.

.. _query-retrieve:

Query/Retrieve Application Entity
"""""""""""""""""""""""""""""""""

The STORAGE-SCU AE can be invoked by the QUERY-RETRIEVE-SCP AE to trigger the transfer of specific images to a remote destination AE. The STORAGE-SCU AE must be correctly configured with the host and port number of any external DICOM AEs that are to be C-MOVE retrieval destinations. The Presentation Contexts to use are determined from the headers of the DICOM files to be transferred. Some conversion of the DICOM image objects is possible if the original Presentation Context is not supported by the remote destination AE or if compression is preferred.
The QUERY-RETRIEVE-SCP AE waits for another application to connect at the presentation address configured for its Application Entity Title. When another application connects, QUERY-RETRIEVE-SCP AE expects it to be a DICOM application. QUERY-RETRIEVE-SCP AE will accept Associations with Presentation Contexts for SOP Classes of the DICOM Query-Retrieve Service Class, and Verification Service Class. It will handle query and retrieve requests on these Presentation Contexts and respond with data objects with values corresponding to the contents of the EXAMPLE-QUERY-RETRIEVE-SERVER database. For C-MOVE requests the destination for the image objects is determined from the Destination AE Title contained in the C-MOVE request. When a retrieval request is received, the QUERY-RETRIEVE-SCP AE issues a command to the STORAGE-SCU AE to send the specified images to the C-MOVE Destination AE.

.. _workflow:

Workflow Application Entity
"""""""""""""""""""""""""""

Worklist Update attempts to download a Worklist from a remote node. If the Workflow AE establishes an Association to a remote AE, it will transfer all worklist items via the open Association. During receiving the worklist response items are counted and the query processing is canceled if the configurable limit of items is reached. The results will be displayed in a separate list, which will be cleared with the next Worklist Update.
The Workflow AE performs the creation of a MPPS Instance automatically whenever images are acquired. Further updates on the MPPS data can be performed interactively from the related MPPS user interface. The MPPS "Complete" or "Discontinued" states can only be set from the user interface.

.. _stow-rs:

STOW-RS
"""""""

The reception of a STOW-RS POST request will activate the STOW-RS Service. The storage request is based upon the accept headers in the STOW-RS POST request. The response includes an HTTP status line, including a status-code and its associated textual phrase, followed by an XML message indicating success, warning, or failure for each instance stored by the STOW-RS service.

.. _wado-uri-wado-rs:

WADO-URI / WADO-RS
""""""""""""""""""

The reception of a WADO request will activate the AE. An internal request is sent to the search capabilities of the DCM4CHEE-WADO-SERVICE. This request is based upon the request parameters or the URL resource end point from the WADO request. The response is a list of all SOP instances stored on the DCM4CHEE-PACS-ARCHIVE that match the request parameters. If there are no matching instances, the AE will indicate this in the WADO response. For all matching instances, the AE will utilize the internal image transfer request to obtain a copy of each instance. If the request was for retrieval of instances, these instances will be returned. If the request was for retrieval of rendered instances, then the AE will render each instance and return the rendered results.

.. _qido-rs:

QIDO-RS
"""""""

The reception of a QIDO-RS GET request will activate the QIDO-RS Provider. An internal query request is sent to the search capabilities of the associated PACS or Vendor Neutral Archive (VNA). The search result is based upon the URL of the QIDO-RS GET request. The response is a status code indicating the success, warning, or failure of the search along with any matching results stored in the Remote PACS or VNA.