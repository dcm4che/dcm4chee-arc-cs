Query/Retrieve Application Entity Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

QUERY-RETRIEVE-SERVER is configured so that the QUERY-RETRIEVE-SCP AE and STORAGE-SCU AE share the same Application Entity Title.

STORAGE-SCU Application Entity Specification
""""""""""""""""""""""""""""""""""""""""""""

.. _storage-scu-sop-classes:

SOP Classes
'''''''''''

The STORAGE-SCU AE provides Standard Conformance to the following DICOM V3.0 SOP Classes:

.. csv-table:: Table 4.2.2.1.1-1.: SOP Classes for STORAGE-SCU AE
   :header: "SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: storage-scu-sop-classes.csv

STORAGE-SCU AE can be configured to use the retired US Image objects (US Image Storage, 1.2.840.10008.5.1.4.1.1.6, and US Multi-frame Storage, 1.2.840.10008.5.1.4.1.1.3) rather than the current US SOP Classes for ultrasound images or vice-versa, making any necessary changes to make the transformed image objects conformant to the corresponding SOP Class. This is only done if the external Storage SCP AE does not support the SOP Instance's original SOP Class.
By altering the configuration it is possible to support additional or fewer SOP Classes.

.. _storage-scu-association-establishment-policies:

Association Establishment Policies
''''''''''''''''''''''''''''''''''

.. _storage-scu-general:

General
.......

The STORAGE-SCU AE can only form Associations when requested to do so by the QUERY-RETRIEVE-SCP AE. The STORAGE-SCU AE can only request the opening of an Association. It cannot accept requests to open Associations from external Application Entities.
The DICOM standard Application Context Name for DICOM is always proposed:

.. csv-table:: Table 4.2.2.1.2-1.: DICOM Application Context for STORAGE-SCU AE
   :file: common/storage-query-retrieve-workflow-general.csv

.. _storage-scu-number-of-associations:

Number Of Associations
......................

The maximum number of simultaneous Associations is configurable, but is usually limited to a maximum of 10. This configuration largely depends on whether relatively quick response to multiple simultaneous C-MOVE Destination AEs is required or maximum throughput performance is required. If the latter is the case, then no simultaneous Associations are permitted, in order to reduce disk thrashing and thus maximize throughput. The STORAGE-SCU AE can initiate simultaneous Associations to a given external C-MOVE Destination AE up to the maximum number configured. There is no separate limit on the maximum number permitted to the same C-MOVE Destination AE.
If the first attempt to open an Association fails then the STORAGE-SCU AE will reschedule the task to attempt it again after a configurable time delay. The number of times to reattempt Association establishment is configurable, with the default being zero.

.. csv-table:: Table 4.2.2.1.2-2.: Number of Associations as a SCU for STORAGE-SCU AE
   :file: storage-scu-query-retrieve-scp-number-of-associations.csv

.. _storage-scu-asynchronous-nature:

Asynchronous Nature
...................

The STORAGE-SCU AE does not support asynchronous communication (multiple outstanding transactions over a single Association). All Association requests must be completed and acknowledged before a new operation can be initiated.

.. csv-table:: Table 4.2.2.1.2-3.: Asynchronous Nature as a SCU for STORAGE-SCU AE
   :file: query-retrieve-asynchronous-nature.csv

.. _storage-scu-implementation-identifying-info:

Implementation Identifying Information
......................................

.. csv-table:: Table 4.2.2.1.2-4.: DICOM Implementation Class and Version for STORAGE-SCU AE
   :file: common/storage-query-retrieve-implementation-identifying-information.csv

Note that the STORAGE-SCU AE and QUERY-RETRIEVE-SCP AE use the same Implementation Class UID. All QUERY-RETRIEVE-SERVER AEs use the same Implementation Version Name. This Version Name is updated with each new release of the product software, as the different AE versions are never released independently.

.. _storage-scu-association-initiation-policy:

Association Initiation Policy
'''''''''''''''''''''''''''''

.. _storage-scu-activity:

Activity - Send Images Requested By an External Peer AE
.......................................................

Description and Sequencing of Activity
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

The STORAGE-SCU AE will initiate a new Association when the QUERY-RETRIEVE-SCP AE invokes the STORAGE-SCU AE to transmit images. The QUERY-RETRIEVE-SCP AE will issue such a command whenever it receives a valid C-MOVE Request. An Association Request is sent to the specified C-MOVE Destination AE and upon successful negotiation of the required Presentation Context the image transfer is started. In all cases an attempt will be made to transmit all the indicated images in a single Association, but this may not always be possible. The Association will be released when all the images have been sent. If an error occurs during transmission over an open Association then the image transfer is halted. The STORAGE-SCU AE will not attempt to independently retry the image export.
Note that the STORAGE-SCU AE does not support the unsolicited sending of SOP Instances using the DICOM Storage Service Class. It will only send SOP Instances in response to a C-MOVE Request from a peer AE.

.. figure:: sequencing-of-activity-storage-scu.svg

   Figure : Sequencing of Activity - Send Images Requested By an External Peer AE

The following sequencing constraints illustrated in figure above apply to the STORAGE-SCU AE:

1. Peer AE requests retrieval of Study, Series, or Images from QUERY-RETRIEVE-SCP AE (C-MOVE-RQ).
2. QUERY-RETRIEVE-SCP AE signals STORAGE-SCU AE to send the image Composite SOP Instances indicated in the C-MOVE-RQ to the C-MOVE Destination AE.
3. STORAGE-SCU AE opens a new Association with the indicated C-MOVE Destination AE.
4. STORAGE-SCU AE sends the indicated Composite SOP Instances.
5. STORAGE-SCU AE closes the Association.
6. The Verification Service is only supported as a utility function for Service staff. It is used only as a diagnostic tool.

Proposed Presentation Contexts
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

STORAGE-SCU AE will propose Presentation Contexts as shown in the following table:

.. csv-table:: Table 4.2.2.1.3-1.: Proposed Presentation Contexts By the STORAGE-SCU AE
   :header: "Abstract Syntax Name", "Abstract Syntax UID", "Transfer Syntax Name", "Transfer Syntax UID", "Role", "Extended Negotiation"
   :file: storage-scu-presentation-contexts.csv

Note
The SOP Classes and Transfer Syntaxes that the STORAGE-SCU AE proposes, as listed above, represent the default behavior. The STORAGE-SCU AE can be configured to propose a subset of these contexts or additional Presentation Contexts. Also, the default Behavior is to propose just a single Transfer Syntax per Presentation Context. However, this can be altered so that every proposed Presentation Context has a unique SOP Class and one or more Transfer Syntaxes. That is, the default behavior is to determine the Transfer Syntaxes the SCP can accept as opposed to which it prefers.

SOP Specific Conformance for Verification SOP Class
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Standard conformance is provided to the DICOM Verification Service Class as an SCU. The Verification Service as an SCU is actually only supported as a diagnostic service tool for network communication issues.

SOP Specific Conformance for Image SOP Classes
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Composite DICOM SOP Instances are maintained as DICOM Part 10 compliant files in the QUERY-RETRIEVE-SERVER database. The entire set of tags received with the image will be saved in QUERY-RETRIEVE-SERVER; this includes all Private and SOP Extended Elements. When a SOP Instance is selected for export from QUERY-RETRIEVE-SERVER, its content will be exported as it was originally received except for a few possible exceptions. Some of the Patient demographic and Study information Elements whose values can have been altered due to changes administered on QUERY-RETRIEVE-SERVER or changes to the state of the image data due to compression can be altered when the SOP Instance is exported.
The Patient demographic and Study information can be entered or altered by several means: manually, or from HL7 messaging,. The replacement behavior depends on which specific DICOM and HL7 services are supported. Also, this behavior is configurable. Values can be altered without changing the SOP Instance UID unless otherwise noted. Refer to the Annex for the specific details of which Elements can have their values altered at time of export.
The QUERY-RETRIEVE-SERVER creates files called Service Logs that can be used to monitor their status and diagnose any problems that may arise. If any error occurs during DICOM communication then appropriate messages are always output to these Service Logs. In addition, error messages may be output as alerts to the User Interface in certain cases.
The STORAGE-SCU AE will exhibit the following Behavior according to the Status Code value returned in a C-STORE Response from a destination C-STORE SCP:

.. csv-table:: Table 4.2.2.1.3-2.: STORAGE-SCU AE C-STORE Response Status Handling Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: storage-scu-image-sop-conformance.csv

All Status Codes indicating an error or refusal are treated as a permanent failure. The STORAGE-SCU AE never automatically resends images when an error Status Code is returned in a C-STORE Response. For specific behavior regarding Status Code values returned in C-MOVE Responses, refer to the Services Supported as an SCP by the QUERY-RETRIEVE-SCP AE.

.. csv-table:: Table 4.2.2.1.3-3.: STORAGE-SCU AE Communication Failure Behavior
   :header: "Exception", "Behaviour"
   :file: storage-scu-communication-failure-behaviour.csv

.. _storage-scu-association-acceptance-policy:

Association Acceptance Policy
'''''''''''''''''''''''''''''

The STORAGE-SCU AE does not accept Associations.


QUERY-RETRIEVE-SCP Application Entity Specification
"""""""""""""""""""""""""""""""""""""""""""""""""""

.. _query-retrieve-scp-sop-classes:

SOP Classes
'''''''''''

The QUERY-RETRIEVE-SCP AE provides Standard Conformance to the following DICOM V3.0 SOP Classes:

.. csv-table:: Table 4.2.2.2.1-1.: SOP Classes for QUERY-RETRIEVE-SCP AE
   :header: "SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: query-retrieve-scp-sop-classes.csv

.. _query-retrieve-association-policies:

Association Policies
''''''''''''''''''''

.. _query-retrieve-scp-general:

General
.......

The QUERY-RETRIEVE-SCP AE will never initiate Associations; it only accepts Association Requests from external DICOM AEs. The QUERY-RETRIEVE-SCP AE will accept Associations for Verification, C-FIND, and C-MOVE requests. In the case of a C-MOVE request, the QUERY-RETRIEVE-SCP AE will issue a command to the STORAGE-SCU AE to initiate an Association with the Destination DICOM AE to send images as specified by the originator of the C-MOVE Request.
The DICOM standard Application Context Name for DICOM 3.0 is always accepted:

.. csv-table:: Table 4.2.2.2.2-1.: DICOM Application Context for QUERY-RETRIEVE-SCP AE
   :file: common/storage-query-retrieve-workflow-general.csv

.. _query-retrieve-scp-number-of-associations:

Number Of Associations
......................

The QUERY-RETRIEVE-SCP AE can support multiple simultaneous Associations. Each time the QUERY-RETRIEVE-SCP AE receives an Association, a child process will be spawned to process the Verification, Query, or Retrieval request. The maximum number of child processes, and thus the maximum number of simultaneous Associations that can be processed, is set by configuration. The default maximum is 10 in total. The maximum number of simultaneous Associations can be either an absolute number or a maximum number for each requesting external Application Entity. The latter flexibility can be useful if communication with one external AE is unreliable and one does not wish 'hung' connections with this AE to prevent Associations with other client AEs.

.. csv-table:: Table 4.2.2.2.2-2.: Number of Associations as a SCP for QUERY-RETRIEVE-SCP AE
   :file: storage-scu-query-retrieve-scp-number-of-associations.csv

.. _query-retrieve-scp-asynchronous-nature:

Asynchronous Nature
...................

The QUERY-RETRIEVE-SCP AE does not support asynchronous communication (multiple outstanding transactions over a single Association). All Association requests must be completed and acknowledged before a new operation can be initiated.

.. csv-table:: Table 4.2.2.2.2-3.: Asynchronous Nature as a SCP for QUERY-RETRIEVE-SCP AE
   :file: query-retrieve-scp-asynchronous-nature.csv

.. _query-retrieve-scp-implementation-identifying-info:

Implementation Identifying Information
......................................

The implementation information for the Application Entity is:

.. csv-table:: Table 4.2.2.2.2-4.: DICOM Implementation Class and Version for QUERY-RETRIEVE-SCP AE
   :file: common/storage-query-retrieve-implementation-identifying-information.csv

Note that the STORAGE-SCU AE, and QUERY-RETRIEVE-SCP AE use the same Implementation Class UID. All QUERY-RETRIEVE-SERVER AEs use the same Implementation Version Name. This Version Name is updated with each new release of the product software, as the different AE versions are never released independently.

.. _query-retrieve-scp-association-initiation-policy:

Association Initiation Policy
'''''''''''''''''''''''''''''

The QUERY-RETRIEVE-SCP AE does not initiate Associations.

.. _query-retrieve-scp-association-acceptance-policy:

Association Acceptance Policy
'''''''''''''''''''''''''''''

.. _query-retrieve-scp-activity:

Activity - Handling Query and Retrieval Requests
................................................

Description and Sequencing of Activity
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

The QUERY-RETRIEVE-SCP AE accepts Associations only if they have valid Presentation Contexts. If none of the requested Presentation Contexts are accepted then the Association Request itself is rejected. It can be configured to only accept Associations with certain hosts (using TCP/IP address) and/or Application Entity Titles.
If QUERY-RETRIEVE-SCP AE receives a query (C-FIND) request then the response(s) will be sent over the same Association used to send the C-FIND-Request.
If QUERY-RETRIEVE-SCP AE receives a retrieval (C-MOVE) request then the responses will be sent over the same Association used to send the C-MOVE-Request. The QUERY-RETRIEVE-SCP AE will notify the STORAGE-SCU to send the requested SOP Instances to the C-MOVE Destination. The STORAGE-SCU AE notifies the QUERY-RETRIEVE-SCP AE of the success or failure of each attempt to send a Composite SOP Instance to the peer C-MOVE Destination AE. The QUERY-RETRIEVE-SCP AE then sends a C-MOVE Response indicating this status after each attempt. Once the STORAGE-SCU AE has finished attempting to transfer all the requested SOP Instances, the QUERY-RETRIEVE-SCP AE sends a final C-MOVE Response indicating the overall status of the attempted retrieval.

.. figure:: sequencing-of-activity-query-retrieve-scp.svg

   Figure : Sequencing of Activity - Handling Query and Retrieval Requests

The following sequencing constraints illustrated in above figure apply to the QUERY-RETRIEVE-SCP AE for handling queries (C-FIND-Requests) :

1. Peer AE opens an Association with the QUERY-RETRIEVE-SCP AE.
2. Peer AE sends a C-FIND-RQ Message
3. QUERY-RETRIEVE-SCP AE returns a C-FIND-RSP Message to the peer AE with matching information. A C-FIND-RSP is sent for each entity matching the identifier specified in the C-FIND-RQ. A final C-FIND-RSP is sent indicating that the matching is complete.
4. Peer AE closes the Association. Note that the peer AE does not have to close the Association immediately. Further C-FIND or C-MOVE Requests can be sent over the Association before it is closed.

The following sequencing constraints illustrated in above figure apply to the QUERY-RETRIEVE-SCP AE for handling retrievals (C-MOVE-Requests) :

1. Peer AE opens an Association with the QUERY-RETRIEVE-SCP AE.
2. Peer AE sends a C-MOVE-RQ Message
3. QUERY-RETRIEVE-SCP AE notifies the STORAGE-SCU AE to send the Composite SOP Instances to the peer C-MOVE Destination AE as indicated in the C-MOVE-RQ.
4. After attempting to send a SOP Instance, the STORAGE-SCU AE indicates to the QUERY-RETRIEVE-SCP AE whether the transfer succeeded or failed. The QUERY-RETRIEVE-SCP AE then returns a C-MOVE-RSP indicating this success or failure.
5. Once the STORAGE-SCU AE has completed all attempts to transfer the SOP Instances to the C-MOVE Destination AE, or the first failure occurred, the QUERY-RETRIEVE-SCP AE sends a final C-MOVE-RSP indicating the overall success or failure of the retrieval.
6. Peer AE closes the Association. Note that the peer AE does not have to close the Association immediately. Further C-FIND or C-MOVE Requests can be sent over the Association before it is closed.

The QUERY-RETRIEVE-SCP AE may reject Association attempts as shown in the table below. The Result, Source and Reason/Diag columns represent the values returned in the corresponding fields of an ASSOCIATE-RJ PDU. The following abbreviations are used in the Source column:

a. 1 - DICOM UL service-user
b. 2 - DICOM UL service-provider (ASCE related function)
c. 3 - DICOM UL service-provider (Presentation related function)

.. csv-table:: Table 4.2.2.2.4-1.: Accepted Presentation Contexts By the QUERY-RETRIEVE-SCP AE
   :header: "Result", "Source", "Reason-Diag", "Explanation"
   :sub-header: "Name", "UID"
   :file: common/storage-query-retrieve-association-rejection-reasons.csv

Accepted Presentation Contexts
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

QUERY-RETRIEVE-SCP AE will accept Presentation Contexts as shown in the following table:

.. csv-table:: Table 4.2.2.2.4-2.: Accepted Presentation Contexts By the QUERY-RETRIEVE-SCP AE
   :header: "Abstract Syntax Name", "Abstract Syntax UID", "Transfer Syntax Name", "Transfer Syntax UID", "Role", "Extended Negotiation"
   :file: query-retrieve-scp-presentation-contexts.csv

SOP Specific Conformance for Query SOP Classes
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

The QUERY-RETRIEVE-SCP AE supports hierarchical queries and not relational queries. There are no attributes always returned by default. Only those attributes requested in the query identifier are returned. Query responses always return values from the QUERY-RETRIEVE-SERVER database. Exported SOP Instances are always updated with the latest values in the database prior to export. Thus, a change in Patient demographic information will be contained in both the C-FIND Responses and any Composite SOP Instances exported to a C-MOVE Destination AE.
Patient Root Information Model
All required search keys on each of the four levels (Patient, Study, Series, and Image) are supported. However, the Patient ID (0010,0020) key must have at least a partial value if the Patient's Name (0010,0010) is not present in a Patient Level query.
Study Root Information Model
All the required search keys on each of the three levels (Study, Series, and Image) are supported. If no partial values are specified for Study attributes then either the Patient ID (0010,0020) key or the Patient's Name (0010,0010) must have at least a partial value specified.

.. csv-table:: Table 4.2.2.2.4-3.: Patient Root C-FIND SCP Supported Elements
   :header: "Level Name    Attribute Name", "Tag", "VR", "Types of Matching"
   :file: query-retrieve-scp-patient-root-c-find-elements.csv

.. csv-table:: Table 4.2.2.2.4-4.: Study Root C-FIND SCP Supported Elements
   :header: "Level Name    Attribute Name", "Tag", "VR", "Types of Matching"
   :file: query-retrieve-scp-study-root-c-find-elements.csv

The tables should be read as follows:
Attribute Name: Attributes supported for returned C-FIND Responses.
Tag: Appropriate DICOM tag for this attribute.
VR: Appropriate DICOM VR for this attribute.
Types of Matching: The types of Matching supported by the C-FIND SCP. A "S" indicates the identifier attribute can specify Single Value Matching, a "R" will indicate Range Matching, a "*" will denote wild card matching, an 'U' will indicate universal matching, and 'L' will indicate that UID lists are supported for matching. "NONE" indicates that no matching is supported, but that values for this Element in the database can be returned.

.. csv-table:: Table 4.2.2.2.4-5.: QUERY-RETRIEVE-SCP AE C-FIND Response Status Return Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: query-retrieve-scp-c-find-response-status-behaviour.csv

SOP Specific Conformance for Retrieval SOP Classes
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

The QUERY-RETRIEVE-SCP AE will convey to the STORAGE-SCU AE that an Association with a DICOM Application Entity named by the external C-MOVE SCU (through a MOVE Destination AE Title) should be established. It will also convey to the STORAGE-SCU AE to perform C-STORE operations on specific images requested by the external C-MOVE SCU. One or more of the Image Storage Presentation Contexts listed in Table 4.2.2.1.3-1. will be negotiated.
The QUERY-RETRIEVE-SCP AE can support lists of UIDs in the C-MOVE Request at the Study, Series, and Image Levels. The list of UIDs must be at the Level of the C-MOVE Request however. For example, if the C-MOVE Request is for Series Level retrieval but the identifier contains a list of Study UIDs then the C-MOVE Request will be rejected, and the A900 Failed Status Code will be returned in the C-MOVE Response.
An initial C-MOVE Response is always sent after confirming that the C-MOVE Request itself can be processed. After this, the QUERY-RETRIEVE-SCP AE will return a response to the C-MOVE SCU after the STORAGE-SCU AE has attempted to send each image. This response reports the number of remaining SOP Instances to transfer, and the number transferred having a successful, failed, or warning status. If the Composite SOP Instances must be retrieved from long-term archive prior to export there may be quite a long delay between the first C-MOVE Response and the next one after the attempt to export the first image. The maximum length of time for this delay will depend on the particular type of archive used but typically varies between 3 and 10 minutes.

.. csv-table:: Table 4.2.2.2.4-6.: QUERY-RETRIEVE-SCP AE C-MOVE Response Status Return Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: query-retrieve-c-move-response-status-behaviour.csv

Note that the Warning Status, B000 (Sub-operations complete - One or more Failures) is never returned. If a failure occurs during export to the C-MOVE Destination AE by the STORAGE-SCU AE then the entire task is aborted. Thus any remaining matches are not exported.

.. csv-table:: Table 4.2.2.2.4-7.: QUERY-RETRIEVE-SCP AE Communication Failure Behavior
   :header: "Exception", "Behaviour"
   :file: query-retrieve-scp-communication-failure-behaviour.csv
