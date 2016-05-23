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

.. csv-table:: Table 4.2.1.2-1.: DICOM Application Context for STORAGE-SCU AE
   :file: storage-general.csv

.. _storage-number-of-associations:

Number of Associations
''''''''''''''''''''''

.. _storage-asynchrounous-nature:

The maximum number of simultaneous Associations is configurable, but is usually limited to a maximum of 10. This configuration largely depends on whether relatively quick response to multiple simultaneous C-MOVE Destination AEs is required or maximum throughput performance is required. If the latter is the case, then no simultaneous Associations are permitted, in order to reduce disk thrashing and thus maximize throughput. The STORAGE-SCU AE can initiate simultaneous Associations to a given external C-MOVE Destination AE up to the maximum number configured. There is no separate limit on the maximum number permitted to the same C-MOVE Destination AE.

If the first attempt to open an Association fails then the STORAGE-SCU AE will reschedule the task to attempt it again after a configurable time delay. The number of times to reattempt Association establishment is configurable, with the default being zero.

.. csv-table:: Table 4.2.1.2-2.: Number of Associations as a SCU for STORAGE-SCU AE
   :file: storage-number-of-associations.csv

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

