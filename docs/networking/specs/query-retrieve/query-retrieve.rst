Query/Retrieve Application Entity Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _query-retrieve-sop-classes:

SOP Classes
"""""""""""

The Query/Retrieve Application Entity provides Standard Conformance to the following SOP Classes:

.. csv-table:: SOP Classes for Query/Retrieve Application Entity
   :name: SOPClasses2
   :header: "SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: sop-classes.csv

These are the default SOP Classes supported. By altering the configuration it is possible to support additional or fewer SOP Classes.

.. _association-policies:

Association Policies
""""""""""""""""""""

.. _general:

General
'''''''

The DICOM standard Application Context Name for DICOM 3.0 is always accepted and proposed:

.. csv-table:: DICOM Application Context for Storage Application Entity

  "Application Context Name", "1.2.840.10008.3.1.1.1"

.. _number-of-associations:

Number Of Associations
''''''''''''''''''''''

The Query/Retrieve Application Entity can support multiple simultaneous Associations requested by peer AEs.
The maximum total number of simultaneous Associations accepted from peer AEs is configurable. It is unlimited by default.

The Query/Retrieve Application Entity initiates multiple simultaneous Associations to peer AEs. Particularly for
each simultaneous processed MOVE Retrieve request, a new Association to the specified Move Destination is initiated.

.. csv-table:: Number of Simultaneous Associations as an SCP for the Storage Application Entity

   "Maximum number of simultaneous Associations requested by peer AEs", "No Maximum Limit (Configurable)"
   "Maximum number of simultaneous Associations initiated by the Query/Retrieve Application Application Entity", "No Maximum Limit"

.. _asynchronous-nature:

Asynchronous Nature
'''''''''''''''''''

The Query/Retrieve Application Entity supports asynchronous communication (multiple outstanding transactions over a single Association).
The maximum number of outstanding asynchronous transactions is configurable. It is unlimited by default.

.. csv-table:: Asynchronous Nature for the Query/Retrieve Application Entity

   "Maximum number of outstanding asynchronous transactions", "No Maximum Limit (Configurable)"

.. _storage-scu-implementation-identifying-info:

Implementation Identifying Information
''''''''''''''''''''''''''''''''''''''

The implementation information for the Query/Retrieve Application Entity is:

.. csv-table:: DICOM Implementation Class and Version for the Query/Retrieve Application Entity

   "Implementation Class UID", "1.2.40.0.13.1.3"
   "Implementation Version Name", "dcm4che-5.xx.yy"

All Application Entities of |product| use the same Implementation Version Name. This Version Name is updated with each
new release of the product software.

.. _association-initiation-policy:

Association Initiation Policy
"""""""""""""""""""""""""""""

.. _activity:

Activity - Send Images Requested By an External Peer AE
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. _description:

Description and Sequencing of Activity
......................................

<TODO>

.. _proposed_presentation_contexts:

Proposed Presentation Contexts
..............................

The Query/Retrieve Application Entity will propose Presentation Contexts for Verification, Study Root Query/Retrieve Information Model - FIND,
Study Root Query/Retrieve Information Model - MOVE and of supported Storage SOP Classes.

.. table:: Proposed Presentation Contexts by the Query/Retrieve Application Entity
   :name: PresentationContext

   +-----------------------------------------------------------------------------------------------------------------------------------------------+
   | Presentation Context Table                                                                                                                    |
   +-------------------------------------------------------------+--------------------------------------------------------------+------+-----------+
   | | Abstract Syntax                                           | Transfer Syntax                                              | Role | Ext. Neg. |
   +-------------------------------+-----------------------------+------------------------------------+-------------------------+      |           |
   | | Name                        | UID                         | Name                               | UID                     |      |           |
   +===============================+=============================+====================================+=========================+======+===========+
   | | Verification                | 1.2.840.10008.1.1           | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None      |
   +-------------------------------+-----------------------------+------------------------------------+-------------------------+------+-----------+
   | | Study Root Query/Retrieve   | 1.2.840.10008.5.1.4.1.2.2.1 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None      |
   | | Information Model - FIND    |                             |                                    |                         |      |           |
   +-------------------------------+-----------------------------+------------------------------------+-------------------------+------+-----------+
   | | Study Root Query/Retrieve   | 1.2.840.10008.5.1.4.1.2.2.2 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None      |
   | | Information Model - MOVE    |                             |                                    |                         |      |           |
   +-------------------------------+-----------------------------+------------------------------------+-------------------------+------+-----------+
   | | Image Storage SOP Class in :ref:`SOPClasses2`             | s. :ref:`SCUImageTS`                                         | SCU  | None      |
   +-------------------------------------------------------------+--------------------------------------------------------------+------+-----------+
   | | Video Storage SOP Class in :ref:`SOPClasses2`             | s. :ref:`SCUVideoTS`                                         | SCU  | None      |
   +-------------------------------------------------------------+------------------------------------+-------------------------+------+-----------+
   | | SR Storage SOP Class in :ref:`SOPClasses2`                | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None      |
   |                                                             +------------------------------------+-------------------------+      |           |
   |                                                             | Explicit VR Little Endian          | 1.2.840.10008.1.2.1     |      |           |
   |                                                             +------------------------------------+-------------------------+      |           |
   |                                                             | Deflated Explicit VR Little Endian | 1.2.840.10008.1.2.1.99  |      |           |
   +-------------------------------------------------------------+------------------------------------+-------------------------+------+-----------+
   | | Other Storage SOP Class in :ref:`SOPClasses2`             | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None      |
   |                                                             +------------------------------------+-------------------------+      |           |
   |                                                             | Explicit VR Little Endian          | 1.2.840.10008.1.2.1     |      |           |
   +-------------------------------------------------------------+------------------------------------+-------------------------+------+-----------+

.. csv-table:: Transfer Syntaxes for Image Storage SOP Classes
   :name: SCUImageTS
   :header: "Transfer Syntax Name", "UID"

   "Implicit VR Little Endian", "1.2.840.10008.1.2"
   "Explicit VR Little Endian", "1.2.840.10008.1.2.1"
   "JPEG Baseline (Process 1)", "1.2.840.10008.1.2.4.50"
   "JPEG Extended (Process 2 & 4)", "1.2.840.10008.1.2.4.51"
   "JPEG Lossless, Non-Hierarchical (Process 14)", "1.2.840.10008.1.2.4.54"
   "JPEG Lossless, Non-Hierarchical, First-Order Prediction (Process 14 [Selection Value 1])", "1.2.840.10008.1.2.4.70"
   "JPEG-LS Lossless", "1.2.840.10008.1.2.4.80"
   "JPEG-LS Lossy (Near-Lossless)", "1.2.840.10008.1.2.4.81"
   "JPEG 2000 (Lossless Only)", "1.2.840.10008.1.2.4.90"
   "JPEG 2000", "1.2.840.10008.1.2.4.91"
   "RLE Lossless", "1.2.840.10008.1.2.5"

.. csv-table:: Transfer Syntax for Video Storage SOP Classes
   :name: SCUVideoTS
   :header: "Transfer Syntax Name", "UID"

   "JPEG Baseline (Process 1)", "1.2.840.10008.1.2.4.50"
   "MPEG2 Main Profile @ Main Level", "1.2.840.10008.1.2.4.100"
   "MPEG2 Main Profile @ High Level", "1.2.840.10008.1.2.4.101"
   "MPEG-4 AVC/H.264 High Profile / Level 4.1", "1.2.840.10008.1.2.4.102"
   "MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1", "1.2.840.10008.1.2.4.103"
   "MPEG-4 AVC/H.264 High Profile / Level 4.2 For 2D Video", "1.2.840.10008.1.2.4.104"
   "MPEG-4 AVC/H.264 High Profile / Level 4.2 For 3D Video", "1.2.840.10008.1.2.4.105"
   "MPEG-4 AVC/H.264 Stereo High Profile / Level 4.2", "1.2.840.10008.1.2.4.106"


.. _verification_sop_class_conformance:

SOP Specific Conformance for Verification SOP Class
...................................................

Standard conformance is provided to the DICOM Verification Service Class as an SCU. The Verification Service as an SCU is actually only supported as a diagnostic service tool for network communication issues.

.. _image_sop_class_conformance:

SOP Specific Conformance for Image SOP Classes
..............................................

<TODO>

.. csv-table:: STORAGE-SCU AE C-STORE Response Status Handling Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: storage-scu-image-sop-conformance.csv

All Status Codes indicating an error or refusal are treated as a permanent failure. The STORAGE-SCU AE never automatically resends images when an error Status Code is returned in a C-STORE Response. For specific behavior regarding Status Code values returned in C-MOVE Responses, refer to the Services Supported as an SCP by the DCM4CHEE SCP AE.

.. csv-table:: STORAGE-SCU AE Communication Failure Behavior
   :header: "Exception", "Behaviour"
   :file: storage-scu-communication-failure-behaviour.csv

.. _association-acceptance-policy:

Association Acceptance Policy
"""""""""""""""""""""""""""""

.. _query-retrieve-activity:

Activity - Handling Query and Retrieval Requests
''''''''''''''''''''''''''''''''''''''''''''''''

.. _query-retrieve-description:

Description and Sequencing of Activity
......................................

<TODO>

.. _accepted-presentation-context:

Accepted Presentation Contexts
..............................

The Query/Retrieve Application Entity will accept Presentation Contexts for all SOP Classes listed in Table 4.2.1.1-1 by default.
The list of accepted Transfer Syntaxes for each accepted Abstract Syntax - as the list of accepted Abstract Syntaxes itselfs - is configurable.

.. table:: Accepted Presentation Contexts of Query/Retrieve Application Entity by default configuration

   +----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Presentation Context Table                                                                                                                         |
   +---------------------------------------------------------------+--------------------------------------------------------------+------+--------------+
   | | Abstract Syntax                                             | Transfer Syntax                                              | Role | Ext. Neg.    |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+      |              |
   | | Name                          | UID                         | Name                               | UID                     |      |              |
   +=================================+=============================+====================================+=========================+======+==============+
   | | Verification                  | 1.2.840.10008.1.1           | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | None         |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Patient Root Query/Retrieve   | 1.2.840.10008.5.1.4.1.2.1.1 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | - Relational |
   | | Information Model - FIND      |                             |                                    |                         |      | - Date Range |
   |                                 |                             |                                    |                         |      | - Fuzzy      |
   |                                 |                             |                                    |                         |      | - Timezone   |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Patient Root Query/Retrieve   | 1.2.840.10008.5.1.4.1.2.1.2 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | - Relational |
   | | Information Model - MOVE      |                             |                                    |                         |      |              |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Patient Root Query/Retrieve   | 1.2.840.10008.5.1.4.1.2.1.3 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | - Relational |
   | | Information Model - GET       |                             |                                    |                         |      |              |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Study Root Query/Retrieve     | 1.2.840.10008.5.1.4.1.2.2.1 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | - Relational |
   | | Information Model - FIND      |                             |                                    |                         |      | - Date Range |
   |                                 |                             |                                    |                         |      | - Fuzzy      |
   |                                 |                             |                                    |                         |      | - Timezone   |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Study Root Query/Retrieve     | 1.2.840.10008.5.1.4.1.2.2.2 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | - Relational |
   | | Information Model - MOVE      |                             |                                    |                         |      |              |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Study Root Query/Retrieve     | 1.2.840.10008.5.1.4.1.2.2.3 | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCP  | - Relational |
   | | Information Model - GET       |                             |                                    |                         |      |              |
   +---------------------------------+-----------------------------+------------------------------------+-------------------------+------+--------------+
   | | Image Storage SOP Class listed in :ref:`SOPClasses2`        | s. :ref:`SCUImageTS`                                         | SCU  | None         |
   +---------------------------------------------------------------+--------------------------------------------------------------+------+--------------+
   | | Any Video Storage SOP Class listed in :ref:`SOPClasses2`    | s. :ref:`SCUVideoTS`                                         | SCU  | None         |
   +---------------------------------------------------------------+------------------------------------+-------------------------+------+--------------+
   | | SR Storage SOP Class listed in :ref:`SOPClasses2`           | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None         |
   |                                                               +------------------------------------+-------------------------+      |              |
   |                                                               | Explicit VR Little Endian          | 1.2.840.10008.1.2.1     |      |              |
   |                                                               +------------------------------------+-------------------------+      |              |
   |                                                               | Deflated Explicit VR               | 1.2.840.10008.1.2.1.99  |      |              |
   |                                                               | Little Endian                      |                         |      |              |
   +---------------------------------------------------------------+------------------------------------+-------------------------+------+--------------+
   | | Other Storage SOP Class listed in :ref:`SOPClasses2`        | Implicit VR Little Endian          | 1.2.840.10008.1.2       | SCU  | None         |
   |                                                               +------------------------------------+-------------------------+      |              |
   |                                                               | Explicit VR Little Endian          | 1.2.840.10008.1.2.1     |      |              |
   +---------------------------------------------------------------+------------------------------------+-------------------------+------+--------------+


.. _query-sop-class-conformance:

SOP Specific Conformance for Query SOP Classes
..............................................

The Query/Retrieve SCP AE supports hierarchical queries and relational queries. There are no attributes always returned by default. Only those attributes requested in the query identifier are returned. Query responses always return values from the DCM4CHEE archive database. Exported SOP Instances are always updated with the latest values in the database prior to export. Thus, a change in Patient demographic information will be contained in both the C-FIND Responses and any Composite SOP Instances exported to a C-MOVE Destination AE.
Patient Root Information Model
All required search keys on each of the four levels (Patient, Study, Series, and Image) are supported. However, the Patient ID (0010,0020) key must have at least a partial value if the Patient's Name (0010,0010) is not present in a Patient Level query.
Study Root Information Model
All the required search keys on each of the three levels (Study, Series, and Image) are supported. If no partial values are specified for Study attributes then either the Patient ID (0010,0020) key or the Patient's Name (0010,0010) must have at least a partial value specified.

.. csv-table:: Patient Root C-FIND SCP Supported Elements
   :header: "Level Name/Attribute Name", "Tag", "VR", "Types of Matching"
   :file: query-retrieve-scp-patient-root-c-find-elements.csv

.. csv-table:: Study Root C-FIND SCP Supported Elements
   :header: "Level Name/Attribute Name", "Tag", "VR", "Types of Matching"
   :file: query-retrieve-study-root-c-find-elements.csv

The tables should be read as follows:

- Attribute Name: Attributes supported for returned C-FIND Responses.
- Tag: Appropriate DICOM tag for this attribute.
- VR: Appropriate DICOM VR for this attribute.
- Types of Matching: The types of Matching supported by the C-FIND SCP.

The values in 'Types of Matching' column mean as follows :

- "S" indicates the identifier attribute can specify Single Value Matching.
- "R" will indicate Range Matching.
- "*" will denote wild card matching.
- "U" will indicate universal matching.
- "L" will indicate that UID lists are supported for matching.
- "NONE" indicates that no matching is supported, but that values for this Element in the database can be returned.

.. csv-table:: Query/Retrieve SCP AE C-FIND Response Status Return Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: query-retrieve-scp-c-find-response-status-behaviour.csv

.. _retrieval-sop-class-conformance:

SOP Specific Conformance for Retrieval SOP Classes
..................................................

The Query/Retrieve SCP AE will convey to the Storage SCU AE that an Association with a DICOM Application Entity named by the external C-MOVE SCU (through a MOVE Destination AE Title) should be established. It will also convey to the Storage SCU AE to perform C-STORE operations on specific images requested by the external C-MOVE SCU. One or more of the Image Storage Presentation Contexts listed in Table 4.2.2.3-1. will be negotiated.
The Query/Retrieve SCP AE can support lists of UIDs in the C-MOVE Request at the Study, Series, and Image Levels. The list of UIDs must be at the Level of the C-MOVE Request however. For example, if the C-MOVE Request is for Series Level retrieval but the identifier contains a list of Study UIDs then the C-MOVE Request will be rejected, and the A900 Failed Status Code will be returned in the C-MOVE Response.
An initial C-MOVE Response is always sent after confirming that the C-MOVE Request itself can be processed. After this, the Query/Retrieve SCP AE will return a response to the C-MOVE SCU after the Storage SCU AE has attempted to send each image. This response reports the number of remaining SOP Instances to transfer, and the number transferred having a successful, failed, or warning status. If the Composite SOP Instances must be retrieved from long-term archive prior to export there may be quite a long delay between the first C-MOVE Response and the next one after the attempt to export the first image. The maximum length of time for this delay will depend on the particular type of archive used but typically varies between 3 and 10 minutes.

.. csv-table:: Query/Retrieve SCP AE C-MOVE Response Status Return Behavior
   :header: "Service Status", "Further Meaning", "Error Code", "Behaviour"
   :file: query-retrieve-scp-c-move-response-status-behaviour.csv

Note that the Warning Status, B000 (Sub-operations complete - One or more Failures) is never returned. If a failure occurs during export to the C-MOVE Destination AE by the STORAGE-SCU AE then the entire task is aborted. Thus any remaining matches are not exported.

.. csv-table:: Query/Retrieve SCP AE Communication Failure Behavior
   :header: "Exception", "Behaviour"
   :file: query-retrieve-scp-communication-failure-behaviour.csv
