Workflow Application Entity Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _workflow-sop-classes

SOP Classes
"""""""""""

The Workflow Application Entity provides Standard Conformance to the following SOP Class(es) :

.. csv-table:: Table 4.2.3.1-1.: SOP Classes for Workflow Application Entity (SCP)
   :header: "SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: workflow-sop-classes.csv

.. _workflow-association-establishment:

Association Policies
""""""""""""""""""""

.. _workflow-general:

General
'''''''
The DICOM standard application context name for DICOM 3.0 is always proposed:

.. csv-table:: Table 4.2.3.1-2.: DICOM Application Context for AE Workflow
   :file: storage-general.csv

.. _workflow-number-of-associations:

Number of Associations
''''''''''''''''''''''
The Workflow Application Entity initiates one Association at a time for a Worklist request.

.. csv-table:: Table 4.2.3.1-3.: Number of Associations Initiated for AE Workflow
   :file: workflow-number-of-associations.csv

.. _workflow-asynchrounous-nature:

Asynchronous Nature
'''''''''''''''''''

The Workflow AE does not support asynchronous communication (multiple outstanding transactions over a single Association).

.. csv-table:: Table 4.2.3.1-4.: Asynchronous Nature as a SCU for STORAGE-SCU AE
   :file: workflow-asynchronous-nature.csv

.. _workflow-implementation-class-uid:

Implementation Identifying Information
''''''''''''''''''''''''''''''''''''''
The implementation information for this Application Entity is:

.. csv-table:: Table 4.2.3.1-5.: DICOM Implementation Class and Version for AE Workflow
   :file: workflow-implementation-identifying-information.csv

.. _workflow-association-initiation:

Association Initiation Policies
"""""""""""""""""""""""""""""""

.. _worklist-worklist-update

Activity - Worklist Update
''''''''''''''''''''''''''

.. _worklist-worklist-update-seq

Description and Sequencing of Activities
........................................

The request for a Worklist Update is initiated by user interaction, i.e., pressing the buttons "Worklist Update"/"Patient Worklist Query"
or automatically at specific time intervals, configurable by the user. With "Worklist Update" the automated query mechanism is performed
immediately on request, while with "Patient Worklist Query" a dialog to enter search criteria is opened and an interactive query can
be performed.
The interactive Patient Worklist Query will display a dialog for entering data as search criteria. When the Query is started on user request,
only the data from the dialog will be inserted as matching keys into the query.
With automated worklist queries (including "Worklist Update") the Worklist Application Entity always requests all items
for a Scheduled Procedure Step Start Date (actual date), Modality (RF) and Scheduled Station AE Title. Query for the Scheduled
Station AE Title is configurable by a Service Engineer.
Upon initiation of the request, the Worklist Application Entity will build an Identifier for the C-FIND request, will initiate an
Association to send the request and will wait for Worklist responses. After retrieval of all responses, Worklist Application Entity
will access the local database to add or update patient demographic data. To protect the system from overflow, the Worklist Application Entity will limit the number of processed worklist responses to a configurable maximum. During receiving
the worklist response items are counted and the query processing is canceled by issuing a C-FIND-CANCEL if the configurable limit
of items is reached. The results will be displayed in a separate list, which will be cleared with the next worklist update.
Worklist Application Entity will initiate an Association in order to issue a C-FIND request according to the Modality
Worklist Information Model.

.. figure:: worklist-sequencing-of-activities-worklist-update.svg

   Figure : Sequencing of Activity - Worklist Update

A possible sequence of interactions between the Workflow AE and a Departmental Scheduler (e.g., a device such as a RIS or HIS
that supports the Modality Worklist SOP Class as an SCP) is illustrated in the Figure above:
1. The Worklist AE opens an association with the Departmental Scheduler
2. The Worklist AE sends a C-FIND request to the Departmental Scheduler containing the Worklist Query attributes.
3. The Departmental Scheduler returns a C-FIND response containing the requested attributes of the first matching Worklist Item.
4. The Departmental Scheduler returns another C-FIND response containing the requested attributes of the second matching
Worklist Item.
5. The Departmental Scheduler returns another C-FIND response with status Success indicating that no further matching Worklist
Items exist. This example assumes that only 2 Worklist items match the Worklist Query.
6. The Worklist AE closes the association with the Departmental Scheduler.

