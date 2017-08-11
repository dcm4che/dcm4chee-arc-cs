Workflow Application Entity Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _workflow-sop-classes:

SOP Classes
"""""""""""

The Workflow Application Entity provides Standard Conformance to the following SOP Class(es) :

.. csv-table:: SOP Classes for Workflow Application Entity (SCP)
   :header: "SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: sop-classes.csv

.. _workflow-association-establishment:

Association Policies
""""""""""""""""""""

.. _workflow-general:

General
'''''''
The DICOM standard Application Context Name for DICOM 3.0 is always accepted and proposed:

.. csv-table:: DICOM Application Context for Storage Application Entity

  "Application Context Name", "1.2.840.10008.3.1.1.1"

.. _workflow-number-of-associations:

Number of Associations
''''''''''''''''''''''
The Workflow Application Entity can support multiple simultaneous Associations requested by peer AEs.
The maximum total number of simultaneous Associations accepted from peer AEs is configurable. It is unlimited by default.

The Workflow Application Entity initiates one Association at a time to send Modality Performed Procedure Step N-CREATE
and N-SET request and one Association at a time to send Instance Availability Notifications to peer AEs.

.. csv-table:: Number of Simultaneous Associations for the Workflow Application Entity

   "Maximum number of simultaneous Associations requested by peer AEs", "No Maximum Limit (Configurable)"
   "Maximum number of simultaneous Associations initiated by the Workflow Application Entity to peer Modality Performed Procedure Step SCPs", "1"
   "Maximum number of simultaneous Associations initiated by the Workflow Application Entity to peer Instance Availability Notification SCPs", "1"

.. _workflow-asynchrounous-nature:

Asynchronous Nature
'''''''''''''''''''

The Workflow Application Entity supports asynchronous communication (multiple outstanding transactions over a single Association).
The maximum number of outstanding asynchronous transactions is configurable. It is unlimited by default.

.. csv-table:: Asynchronous Nature for the Workflow Application Entity

   "Maximum number of outstanding asynchronous transactions", "No Maximum Limit (Configurable)"

.. _workflow-implementation-class-uid:

Implementation Identifying Information
''''''''''''''''''''''''''''''''''''''

The implementation information for the Workflow Application Entity is:

.. csv-table:: DICOM Implementation Class and Version for the Workflow Application Entity

   "Implementation Class UID", "1.2.40.0.13.1.3"
   "Implementation Version Name", "dcm4che-5.xx.yy"

All Application Entities of |product| use the same Implementation Version Name. This Version Name is updated with each
new release of the product software.

.. _workflow-association-initiation:

Association Initiation Policies
"""""""""""""""""""""""""""""""

Activity - Forward Modality Performed Procedure
'''''''''''''''''''''''''''''''''''''''''''''''

Description and Sequencing of Activities
........................................

<TODO>

Proposed Presentation Contexts
..............................

The Workflow AE will propose Presentation Contexts as shown in the following table:

.. table:: Proposed Presentation Contexts for Real-World Activity Forward Modality Performed Procedure

   +----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Presentation Context Table                                                                                                                         |
   +--------------------------------------------------------------+-------------------------------------------------------+------+----------------------+
   | Abstract Syntax                                              | Transfer Syntax                                       | Role | Extended Negotiation |
   +------------------------------------+-------------------------+---------------------------------+---------------------+      +                      +
   | Name                               | UID                     | Name                            | UID                 |      |                      |
   +====================================+=========================+=================================+=====================+======+======================+
   | Modality Performed Procedure Step  | 1.2.840.10008.3.1.2.3.3 | DICOM Implicit VR Little Endian | 1.2.840.10008.1.2   | SCU  | None                 |
   +                                    +                         +---------------------------------+---------------------+      +                      +
   |                                    |                         | DICOM Explicit VR Little Endian | 1.2.840.10008.1.2.1 | SCP  |                     +------------------------------------+-------------------------+---------------------------------+---------------------+------+----------------------+
   +------------------------------------+-------------------------+---------------------------------+---------------------+------+----------------------+

SOP Specific Conformance
........................

<TODO>

Activity - Send Instance Available Notification
'''''''''''''''''''''''''''''''''''''''''''''''

Description and Sequencing of Activities
........................................

<TODO>

Proposed Presentation Contexts
..............................

The Workflow AE will propose Presentation Contexts as shown in the following table:

.. table:: Proposed Presentation Contexts for Real-World Activity Send Instance Available Notification

   +----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Presentation Context Table                                                                                                                         |
   +--------------------------------------------------------------+-------------------------------------------------------+------+----------------------+
   | Abstract Syntax                                              | Transfer Syntax                                       | Role | Extended Negotiation |
   +------------------------------------+-------------------------+---------------------------------+---------------------+      +                      +
   | Name                               | UID                     | Name                            | UID                 |      |                      |
   +====================================+=========================+=================================+=====================+======+======================+
   | Instance Availability Notification | 1.2.840.10008.5.1.4.33  | DICOM Implicit VR Little Endian | 1.2.840.10008.1.2   | SCU  | None                 |
   +                                    +                         +---------------------------------+---------------------+      +                      +
   |                                    |                         | DICOM Explicit VR Little Endian | 1.2.840.10008.1.2.1 |      |                      |
   +------------------------------------+-------------------------+---------------------------------+---------------------+------+----------------------+

SOP Specific Conformance
........................

<TODO>

.. _workflow-association-acceptance:

Association Acceptance Policies
"""""""""""""""""""""""""""""""

<TODO>
