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
   :file: storage-implementation-identifying-information.csv

Note that the STORAGE-SCU AE and QUERY-RETRIEVE-SCP AE use the same Implementation Class UID. All EXAMPLE-QUERY-RETRIEVE-SERVER AEs use the same Implementation Version Name. This Version Name is updated with each new release of the product software, as the different AE versions are never released independently.

.. _storage-association-initiation:


