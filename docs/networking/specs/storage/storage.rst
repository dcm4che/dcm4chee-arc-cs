Storage Application Entity Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _storage-sop-classes:

SOP Classes
"""""""""""

The Storage Application Entity provides Standard Conformance to the following SOP Class(es) :

.. csv-table:: Table 4.2.1.1-1.: SOP Classes for Storage Application Entity (SCP)
   :header: "SOP Class Group / SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: sop-classes.csv

These are the default SOP Classes supported. By altering the configuration it is possible to support additional or fewer SOP Classes.

.. _storage-association-policies:

Association Policies
""""""""""""""""""""

.. _storage-general:

General
'''''''
The STORAGE-SCP AE can both accept and propose Association Requests. The STORAGE-SCP AE will accept Association Requests for the Verification, Storage, and Storage Commitment Push Model Services. It will propose Associations only for the Storage Commitment Push Model Service.
The DICOM standard Application Context Name for DICOM 3.0 is always accepted and proposed:

.. csv-table:: Table 4.2.1.2-1.: DICOM Application Context for STORAGE-SCP AE
   :file: common/storage-query-retrieve-workflow-general.csv

.. _storage-number-of-associations:

Number of Associations
''''''''''''''''''''''

The STORAGE-SCP AE can support multiple simultaneous Associations requested by peer AEs. Each time the STORAGE-SCP AE receives an Association, a child process will be spawned to process the Verification, Storage, or Storage Commitment Push Model Service requests. The maximum number of child processes, and thus the maximum number of simultaneous Associations that can be processed, is set by configuration. The default maximum number is 10 in total. This maximum number of simultaneous Associations can be either an absolute number or a maximum number for each requesting external Application Entity. The latter flexibility can be useful if communication with one external AE is unreliable and one does not wish 'hung' connections with this AE to prevent Associations with other client AEs.
The STORAGE-SCP AE initiates one Association at a time for sending Storage Commitment Push Model N-EVENT-REPORTs to peer AEs.

.. csv-table:: Table 4.2.1.2-2.: Number of Simultaneous Associations as an SCP for STORAGE-SCP AE
   :file: number-of-associations.csv

.. _storage-asynchrounous-nature:

Asynchronous Nature
'''''''''''''''''''

The STORAGE-SCP AE does not support asynchronous communication (multiple outstanding transactions over a single Association). The STORAGE-SCP AE does permit an SCU to send multiple Storage Commitment Push Model Requests before it has sent back any N-EVENT-REPORT Notifications. However, the STORAGE-SCP AE must send an N-ACTION Response before permitting another N-ACTION Request to be received so the DICOM communication itself is not truly asynchronous.

.. csv-table:: Table 4.2.1.2-3.: Asynchronous Nature as a SCP for STORAGE-SCP AE
   :file: asynchronous-nature.csv

There is no limit on the number of outstanding Storage Commitment Push Model Requests that can be received and acknowledged before the STORAGE-SCP AE has responded with the corresponding N-EVENT-REPORT Notifications.

.. csv-table:: Table 4.2.1.2-4.: Outstanding Storage Commitment Push Model Requests for STORAGE-SCP AE
   :file: outstanding-stgcmt-push-model-req.csv

.. _storage-implementation-class-uid:

Implementation Identifying Information
''''''''''''''''''''''''''''''''''''''

The implementation information for this Application Entity is:

.. csv-table:: Table 4.2.1.2-5.: DICOM Implementation Class and Version for STORAGE-SCP AE
   :file: common/storage-query-retrieve-implementation-identifying-information.csv

Note that the STORAGE-SCP AE specifies a different Implementation Class UID than that used by the other Application Entities. All QUERY-RETRIEVE-SERVER AEs use the same Implementation Version Name. This Version Name is updated with each new release of the product software, as the different AE versions are never released independently.

.. _storage-association-initiation:

Association Initiation Policies
"""""""""""""""""""""""""""""""

.. _send-stgcmt-result:

Activity - Send Storage Commitment Notification Over New Association
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. _send-stgcmt-result-seq:

Description and Sequencing of Activity
......................................

The STORAGE-SCP AE will initiate a new Association if a Storage Commitment Push Model Notification (N-EVENT-REPORT) cannot be sent back over the original Association used to send the corresponding request. A new Association will always be requested by the STORAGE-SCP AE in such cases even if the peer AE requests another Association after the original has been closed (i.e., A peer AE opens an Association and sends some Storage requests and a Storage Commitment Push Model request. Before the STORAGE-SCP AE can send the Storage Commitment Push Model N-EVEN-REPORT the Association is closed. The peer AE then opens another Association and begins to send Storage requests. In such a case the STORAGE-SCP AE will always initiate a new Association to send the N-EVENT-REPORT even though it could send the N-EVENT-REPORT over the new Association opened by the peer AE).
An Association Request is sent to the peer AE that sent the Storage Commitment Push Model request and upon successful negotiation of the required Presentation Context the outstanding N-EVENT-REPORT is sent. If there are multiple outstanding N-EVENT-REPORTs to be sent to a single peer AE then the STORAGE-SCP AE will attempt to send them all over a single Association rather than requesting a new Association for each one. The Association will be released when all the N-EVENT-REPORTs for the peer AE have been sent. If any type of error occurs during transmission (either a communication failure or indicated by a Status Code returned by the peer AE) over an open Association then the transfer of N-EVENT-REPORTs is halted. A new Association will be opened to retry sending outstanding N-EVENT-REPORTs. The maximum number of times the STORAGE-SCP AE will attempt to resend an N-EVENT-REPORT is configurable, along with the amount of time to wait between attempts to resend.
If the STORAGE-SCP AE sends a Notification request (N-EVENT-REPORT-RQ) over the original Association opened by the peer AE but receives a request to close the Association rather than a response to the Notification (N-EVENT-REPORT-RSP) then this is handled in the same way as if the request to close the Association had been received before trying to send the Notification request. Thus, the STORAGE-SCP AE will then open a new Association to resend the Notification request.
The STORAGE-SCP AE can be configured to always open a new Association before sending a Storage Commitment Push Model Notifications (N-EVENT-REPORT), in which case the sequencing illustrated in figure below will always be followed.

.. figure:: sequencing-of-activity-send-storage-commitment-notification-over-new-association.svg

   Figure : Sequencing of Activity - Send Storage Commitment Notification Over New Association

The following sequencing constraints illustrated in figure above apply to the STORAGE-SCP AE for handling Storage Commitment Push Model Requests using a new Association:

1. Peer AE opens an Association with the STORAGE-SCP AE.
2. Peer AE requests Storage Commitment of Composite SOP Instance(s) (peer sends N-ACTION-RQ and STORAGE-SCP AE responds with N-ACTION-RSP to indicate that it received the request).
3. Peer AE closes the Association before the STORAGE-SCP AE can successfully send the Storage Commitment Push Model Notification (N-EVENT-REPORT-RQ).
4. STORAGE-SCP AE opens an Association with the peer AE.
5. STORAGE-SCP AE sends Storage Commitment Push Model Notification (N-EVENT-REPORT). More than one can be sent over a single Association if multiple Notifications are outstanding.
6. STORAGE-SCP AE closes the Association with the peer AE.

The Verification Service as an SCU is only supported as a utility function for Service staff. It is used only as a diagnostic tool when the STORAGE-SCP AE is failing to open new Associations to send N-EVENT-REPORTs to peer AEs.


.. _send-stgcmt-result-proposed-pcs:

Proposed Presentation Contexts
..............................

STORAGE-SCP AE will propose Presentation Contexts as shown in the following table:

.. csv-table:: Table 4.2.1.3-1.: Proposed Presentation Contexts By the STORAGE-SCP AE
   :header: "Abstract Syntax Name", "Abstract Syntax UID", "Transfer Syntax Name", "Transfer Syntax UID", "Role", "Extended Negotiation"
   :file: proposed-presentation-contexts.csv

.. _stgcmt-conformance:

SOP Specific Conformance for Storage Commitment Push Model SOP Class
....................................................................

The associated Activity with the Storage Commitment Push Model service is the communication by the STORAGE-SCP AE to peer AEs that it has committed to permanently store Composite SOP Instances that have been sent to it. It thus allows peer AEs to determine whether the QUERY-RETRIEVE-SERVER has taken responsibility for the archiving of specific SOP Instances so that they can be flushed from the peer AE system.

The STORAGE-SCP AE will initiate a new Association to a peer AE that sent a Storage Commitment Push Model request if the original Association over which this was sent is no longer open. For a detailed explanation of the SOP specific Behavior of the STORAGE-SCP AE in this case please refer to 4.2.4.4.1.3.3, Storage Commitment Push Model as an SCP.

.. _stgcmt-conformance-verification:

SOP Specific Conformance for Storage Commitment Verification SOP Class
......................................................................

Standard conformance is provided to the DICOM Verification Service Class as an SCU. The Verification Service as an SCU is actually only supported as a diagnostic service tool for network communication issues. It can be used to test whether Associations can actually be opened with a peer AE that is issuing Storage Commitment Push Model requests (i.e., to test whether the indicated TCP/IP port and AE Title for sending N-EVENT-REPORT Requests to the peer AE are truly functional).

.. _storage-association-acceptance:

Association Acceptance Policy
"""""""""""""""""""""""""""""

.. _storage-receive-stgcmt-rq:

Activity - Receive Images and Storage Commitment Requests
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. _storage-receive-stgcmt-rq-seq:

Description and Sequencing of Activities
........................................

The STORAGE-SCP AE accepts Associations only if they have valid Presentation Contexts. If none of the requested Presentation Contexts are accepted then the Association Request itself is rejected. It can be configured to only accept Associations with certain hosts (using TCP/IP address) and/or Application Entity Titles.
The default behavior of the STORAGE-SCP AE is to always attempt to send a Storage Commitment Push Model Notification (N-EVENT-REPORT) over the same Association opened by the peer AE to send the request (N-ACTION). If the STORAGE-SCP AE receives a request to close the Association either before sending the Notification or before receiving the corresponding N-EVENT-REPORT-RSP then it will open a new Association to send the Notification. Refer to Section F.4.2.3.4.1.5 for the details.

.. figure:: sequencing-of-activity-receive-images-and-storage-commitment-requests.svg

   Figure : Sequencing of Activity - Receive Images and Storage Commitment Requests

The following sequencing constraints illustrated in figure above apply to the STORAGE-SCP AE for handling Storage Commitment Push Model Requests over the original Association:

1. Peer AE opens an Association with the STORAGE-SCP AE.
2. Peer AE sends zero or more Composite SOP Instances.
3. Peer AE requests Storage Commitment of Composite SOP Instance(s) (peer sends N-ACTION-RQ and STORAGE-SCP AE responds with N-ACTION-RSP to indicate that it received the request).
4. STORAGE-SCP AE sends Storage Commitment Push Model Notification request (N-EVENT-REPORT-RQ) and successfully receives Notification response (N-EVENT-REPORT-RSP) from peer AE.
5. Peer AE closes the Association.

If the STORAGE-SCP AE receives a request to close the Association from the peer AE before sending the Notification request (N-EVENT-REPORT-RQ) or when expecting to receive a Notification response (N-EVENT-REPORT-RSP) then it will open a new Association to send (or resend) the Notification. Refer to 0 for the details. The STORAGE-SCP AE has a configurable timeout value for the maximum amount of time that it will wait on an open Association for a new request from a peer AE. A peer AE can reset this timer by sending a Verification request (C-ECHO-RQ). This can act as a useful mechanism for a peer AE to maintain an active Association if the length of time between sending Storage or Storage Commitment requests can be long (such as when using a single Association to send images as they are acquired during an ultrasound exam).
The STORAGE-SCP AE may reject Association attempts as shown in the Table below. The Result, Source and Reason/Diag columns represent the values returned in the corresponding fields of an ASSOCIATE-RJ PDU. The following abbreviations are used in the Source column:

a. 1 - DICOM UL service-user
b. 2 - DICOM UL service-provider (ASCE related function)
c. 3 - DICOM UL service-provider (Presentation related function)

.. csv-table:: Table 4.2.1.4.1-1.: Association Rejection Reasons
   :header: "Result", "Source", "Reason-Diag", "Explanation"
   :file: common/storage-query-retrieve-association-rejection-reasons.csv

.. _storage-receive-stgcmt-rq-accepted-pcs:

Accepted Presentation Contexts
..............................

The default Behavior of the STORAGE-SCP AE supports the Implicit VR Little Endian and Explicit VR Little Endian Transfer Syntaxes for all Associations. In addition, explicit JPEG (baseline lossy) compression syntax is supported for the following SOP Classes: US Image, US Multi-frame Image, US Image (retired), US Multi-frame Image (retired), VL Image, VL Multi-frame and Secondary Capture Image Storage.
The STORAGE-SCP AE can be configured to accept a subset of these Transfer Syntaxes, with the inclusion of Implicit VR Little Endian being mandatory.
If multiple Transfer Syntaxes are proposed per Presentation Context then only the most preferable Transfer Syntax is accepted. The order of Transfer Syntax preference for the STORAGE-SCP AE is configurable. The default preference order if multiple Transfer Syntaxes are proposed in a single Presentation Context is: JPEG Baseline1, Little Endian Explicit, Little Endian Implicit (if all these are proposed for a single Presentation Context). This means that if the Implicit VR Little Endian and Explicit VR Little Endian Transfer Syntaxes are proposed in a single Presentation Context then the accepted Transfer Syntax will be Explicit VR Little Endian. This order of preference is configurable.
Any of the Presentation Contexts shown in the following table are acceptable to the STORAGE-SCP AE for receiving images.

.. csv-table:: Table 4.2.1.4.2-1.: Accepted Presentation Contexts By STORAGE-SCP AE
   :header: "SOP Class Groups", "Transfer Syntax Name", "Transfer Syntax UID", "Role", "Extended Negotiation"
   :file: accepted-presentation-contexts-by-STORAGE-SCP-AE.csv

(*) : Decompression not supported when retrieved from archive again.

Note : Refer Table 4.2.1.1-1. which has SOP Class Names and SOP Class UIDs against each of the SOP Class groups

.. _storage-verification-sop-conformance:

SOP Specific Conformance for Verification SOP Class
...................................................

The STORAGE-SCP AE provides standard conformance to the Verification SOP Class as an SCP.

.. _storage-sop-conformance:

SOP Specific Conformance for Storage SOP Class
..............................................

The associated Activity with the Storage service is the storage of medical image data received over the network on a designated hard disk. The STORAGE-SCP AE will return a failure status if it is unable to store the images on to the hard disk.
The STORAGE-SCP AE does not have any dependencies on the number of Associations used to send images to it. Images belonging to more than one Study or Series can be sent over a single or multiple Associations. Images belonging to a single Study or Series can also be sent over different Associations. There is no limit on either the number of SOP Instances or the maximum amount of total SOP Instance data that can be transferred over a single Association.
The STORAGE-SCP AE is configured to retain the original DICOM data in DICOM Part 10 compliant file format. The STORAGE-SCP AE is Level 2 (Full) conformant as a Storage SCP. In addition, all Private and SOP Class Extended Elements are maintained in the DICOM format files. In addition to saving all Elements in files, a subset of the Elements are stored in the QUERY-RETRIEVE-SERVER database to support query and retrieval requests and also allow updating of Patient, Study, and Series information by user input, or demographic and Study related messages. Refer to the Annex for the list of Elements that are checked and/or processed upon receiving a Composite SOP Instance.
The Behavior for handling duplicate SOP Instances is configurable. The default Behavior is to assign a new SOP Instance UID to a received SOP Instance if it conflicts with an existing SOP Instance UID. An alternative configuration is possible that causes the original object with the conflicting SOP Instance UID to be replaced by the new SOP Instance. This Behavior is most commonly enabled if a Storage SCU re-sends entire Studies or Series if a single failure occurs when sending a group of SOP Instances.
For the purposes of image display the system supports the following photometric interpretations: MONOCHROME1, MONOCHROME2, RGB, PALETTE COLOR, YBR FULL 422, and YBR FULL.
It is expected that optimal Window Center and Width values are specified in the DICOM Image Objects if they have greater than 8 bits of image data stored per sample. If optimal Window Center and Width values are not provided, then the QUERY-RETRIEVE-SERVER is capable of estimating values using histogram analysis.
For multi-frame image SOP Instances sent using JPEG compression Transfer Syntax, sending a fully specified offset table increases performance, because the entire file does not have to be parsed to find the individual frame offsets. However, the inclusion of an offset table is not required for archiving or viewing of such SOP Instances.
Display of information conveyed using the DICOM Curve Module is not supported. Graphic overlay data sent either embedded in the unused image pixel data bits or in the separate Overlay Data Element is supported for display. Region of Interest overlays are not yet supported.
If an image SOP Instance specifies an aspect ratio that is not one-to-one then the image data will be automatically resized when displayed on the system monitor so that they are always displayed in a one-to-one aspect ratio.
The average throughput performance has been determined to be between 2 and 6 Mega Bytes per second on a 100 Megabit Ethernet network. Actual performance will depend greatly on the performance of the C-STORE SCU, the number of simultaneous active Associations, and the underlying network performance.

.. csv-table:: Table 4.2.1.4.4-1.: STORAGE-SCP AE C-STORE Response Status Return Reasons
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: c-store-response-status-return-reasons.csv

Note : If a failure condition does occur when handling an Association then all images previously received successfully over the Association are maintained in the QUERY-RETRIEVE-SERVER database. No previously successfully received images are discarded. Even if an image is successfully received but an error occurs transmitting the C-STORE Response then this final image is maintained rather than discarded. If the loss of an Association is detected then the Association is closed.
The Behavior of STORAGE-SCP AE during communication failure is summarized in the following table:

.. csv-table:: Table 4.2.1.4.4-2.: STORAGE-SCP AE Storage Service Communication Failure Reasons
   :header: "Exception", "Reason"
   :file: storage-scp-communication-failure-reasons.csv

.. _storage-stgcmt-conformance:

SOP Specific Conformance for Storage Commitment SOP Class
.........................................................

The associated Activity with the Storage Commitment Push Model service is the communication by the STORAGE-SCP AE to peer AEs that it has committed to permanently store Composite SOP Instances that have been sent to it. It thus allows peer AEs to determine whether the QUERY-RETRIEVE-SERVER has taken responsibility for the archiving of specific SOP Instances so that they can be flushed from the peer AE system.
The STORAGE-SCP AE takes the list of Composite SOP Instance UIDs specified in a Storage Commitment Push Model N-ACTION Request and checks if they are present in the QUERY-RETRIEVE-SERVER database. As long as the Composite SOP Instance UIDs are present in the database, the STORAGE-SCP AE will consider those Composite SOP Instance UIDs to be successfully archived. The STORAGE-SCP AE does not require the Composite SOP Instances to actually be successfully written to archive media in order to commit to responsibility for maintaining these SOP Instances.
Once the STORAGE-SCP AE has checked for the existence of the specified Composite SOP Instances, it will then attempt to send the Notification request (N-EVENT-REPORT-RQ). The default behavior is to attempt to send this Notification over the same Association that was used by the peer AE to send the original N-ACTION Request. If the Association has already been released or Message transfer fails for some reason then the STORAGE-SCP AE will attempt to send the N-EVENT-REPORT-RQ over a new Association. The STORAGE-SCP AE will request a new Association with the peer AE that made the original N-ACTION Request. The STORAGE-SCP AE can be configured to always open a new Association in order to send the Notification request.
The STORAGE-SCP AE will not cache Storage Commitment Push Model N-ACTION Requests that specify Composite SOP Instances that have not yet been transferred to the QUERY-RETRIEVE-SERVER. If a peer AE sends a Storage Commitment Push Model N-ACTION Request before the specified Composite SOP Instances are later sent over the same Association, the STORAGE-SCP AE will not commit to responsibility for such SOP Instances.
The STORAGE-SCP AE does not support the optional Storage Media File-Set ID & UID attributes in the N-ACTION.
The QUERY-RETRIEVE-SERVER never automatically deletes Composite SOP Instances from the archive. The absolute persistence of SOP Instances and the maximum archiving capacity for such SOP Instances is dependent on the archiving media and capacity used by the QUERY-RETRIEVE-SERVER and is dependent on the actual specifications of the purchased system. It is necessary to check the actual system specifications to determine these characteristics.
The STORAGE-SCP AE will support Storage Commitment Push Model requests for SOP Instances of any of the Storage SOP Classes that are also supported by the STORAGE-SCP AE:

.. csv-table:: Table 4.2.1.4.5-1.: Supported Referenced SOP Classes in Storage Commitment Push Model N-ACTION Requests
   :header: "Supported Referenced SOP Classes"
   :file: supported-sop-classes-stgcmt.csv

The STORAGE-SCP AE will return the following Status Code values in N-ACTION Responses:

.. csv-table:: Table 4.2.1.4.5-2.: STORAGE-SCP AE Storage Commitment Push Model N-ACTION Response Status Return Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: stgcmt-n-action-response-status-return-behaviour.csv

The STORAGE-SCP AE will exhibit the following Behavior according to the Status Code value returned in an N-EVENT-REPORT Response from a destination Storage Commitment Push Model SCU:

.. csv-table:: Table 4.2.1.4.5-3.: STORAGE-SCP AE N-EVENT-REPORT Response Status Handling Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: stgcmt-n-event-response-status-return-behaviour.csv

All Status Codes indicating an error or refusal are treated as a permanent failure. The STORAGE-SCP AE can be configured to automatically reattempt the sending of Storage Commitment Push Model N-EVENT-REPORT Requests if an error Status Code is returned or a communication failure occurs. The maximum number of times to attempt sending as well as the time to wait between attempts is configurable.

.. csv-table:: Table 4.2.1.4.5-4.: STORAGE-SCP AE Storage Commitment Push Model Communication Failure Behavior
   :header: "Exception", "Behaviour"
   :file: stgcmt-communication-failure-behaviour.csv