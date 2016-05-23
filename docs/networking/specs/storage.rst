Storage Application Entity Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _storage-sop-classes:

SOP Classes
"""""""""""

The Storage Application Entity provides Standard Conformance to the following SOP Class(es) :

.. csv-table:: Table 4.2.1.1-1.: SOP Classes for Storage Application Entity (SCP)
   :header: "SOP Class Name", "SOP Class UID", "SCU", "SCP"
   :file: storage-sop-classes.csv

.. _storage-association-establishment:

Association Establishment Policies
""""""""""""""""""""""""""""""""""

.. _storage-general:

General
'''''''
The STORAGE-SCU AE can only form Associations when requested to do so by the QUERY-RETRIEVE-SCP AE. The STORAGE-SCU AE can only request the opening of an Association. It cannot accept requests to open Associations from external Application Entities.

The DICOM standard Application Context Name for DICOM is always proposed:

        "Application Context Name", "1.2.840.10008.3.1.1.1"

.. _storage-number-of-associations:

Number of Associations
''''''''''''''''''''''

.. _storage-asynchrounous-nature:

Asynchronous Nature
'''''''''''''''''''

.. _storage-implementation-class-uid:

Implementation Identifying Information
''''''''''''''''''''''''''''''''''''''

.. _storage-association-initiation:

Association Initiation Policies
"""""""""""""""""""""""""""""""

.. _send-stgcmt-result:

Activity - Send Storage Commitment Result
'''''''''''''''''''''''''''''''''''''''''

.. _send-stgcmt-result-seq:

Description and Sequencing of Activity
......................................

.. _send-stgcmt-result-proposed-pcs:

Proposed Presentation Contexts
..............................

.. _stgcmt-conformance:

SOP Specific Conformance for Storage Commitment Push Model SOP Class
....................................................................

.. _storage-association-acceptance:

Association Acceptance Policy
"""""""""""""""""""""""""""""

.. _receive-instance:

Activity - Received Storage Request
'''''''''''''''''''''''''''''''''''

.. _receive-instance-seq:

Description and Sequencing of Activities
........................................

.. _receive-instance-accepted-pcs:

Accepted Presentation Contexts
..............................

.. _receive-stgcmt-rq:

Activity - Receive Storage Commitment Request
'''''''''''''''''''''''''''''''''''''''''''''

.. _receive-stgcmt-rq-seq:

Description and Sequencing of Activities
........................................

.. _receive-stgcmt-rq-accepted-pcs:

Accepted Presentation Contexts
..............................

