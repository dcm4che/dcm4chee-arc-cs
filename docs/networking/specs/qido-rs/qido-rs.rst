QIDO-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _qido-rs-search-for-studies:

QIDO-RS Search For Studies
""""""""""""""""""""""""""

.. csv-table:: QIDO-RS Search for Studies Specification
   :header: "Parameter", "Restrictions"
   :file: search-for-studies.csv

Extended Negotiation :

DCM4CHEE-QIDO-SERVICE does not support the "fuzzymatching" query key.
DCM4CHEE-QIDO-SERVICE will perform case insensitive matching for PN VR attributes but will not perform other forms of fuzzy matching. This applies to the following attributes:

1. Referring Physician's Name (0008,0090).
2. Physician(s) of Record (0008,1048).
3. Patient's Name (0010,0010).

.. csv-table:: QIDO-RS Study Attribute Matching
   :header: "Keyword", "Tag", "Types of Matching"
   :file: study-attribute-matching.csv

Types of Matching :

1. "S" indicates the identifier attribute uses Single Value Matching.
2. "L" indicates UID List Matching.
3. "U" indicates Universal Matching.

Note : If only Universal Matching is supported for an attribute then that attribute can only be passed as an "includefield" query key.
4. "*" indicates wild card matching.
5. "R" indicates Range Matching.
6. "SEQUENCE" indicates Sequence Matching.
7. "NONE" indicates that no matching is supported, but that values for this Element requested will be returned with all requests.
8. "UNIQUE" indicates that this is the Unique Key for that query level, in which case Universal Matching or Single Value Matching is used depending on the query level.

.. _qido-rs-search-for-series:

QIDO-RS Search For Series
"""""""""""""""""""""""""

.. csv-table:: QIDO-RS Search for Series Specification
   :header: "Parameter", "Restrictions"
   :file: search-for-series.csv

Types of Matching: As explained above in QIDO-RS Search For Studies

.. csv-table:: QIDO-RS Series Attribute Matching
   :header: "Keyword", "Tag", "Types of Matching"
   :file: series-attribute-matching.csv

.. _qido-rs-search-for-instances:

QIDO-RS Search For Instances
""""""""""""""""""""""""""""

.. csv-table:: QIDO-RS Search for Instances Specification
   :header: "Parameter", "Restrictions"
   :file: search-for-instances.csv

Types of Matching: As explained above in QIDO-RS Search For Studies

.. csv-table:: QIDO-RS Instance Attribute Matching
   :header: "Keyword", "Tag", "Types of Matching"
   :file: instance-attribute-matching.csv

.. _qido-rs-connection-policies:

QIDO-RS Connection Policies
"""""""""""""""""""""""""""

.. _qido-rs-general:

General
'''''''
All standard RS connection policies apply. There are no extensions for RS options.

.. _qido-rs-number-of-connections:

Number Of Connections
'''''''''''''''''''''
DCM4CHEE-QIDO-SERVICE limits the number of simultaneous RS requests. Additional requests will be queued after the HTTP connection is accepted. When an earlier request completes, a pending request will proceed.

.. csv-table:: Number of HTTP Requests Supported
   :file: common/qido-rs-stow-rs-wado-uri-wado-rs-number-of-connections.csv

.. _qido-rs-asynchronous-nature:

Asynchronous Nature
'''''''''''''''''''
DCM4CHEE-QIDO-SERVICE does not support RS asynchronous response.

.. _qido-rs-response-status:

Response Status
'''''''''''''''
DCM4CHEE-QIDO-SERVICE shall provide a response message header containing the appropriate status code indicating success, warning, or failure as shown below

.. csv-table:: HTTP Standard Response Codes
   :header: "Code", "Name", "Description"
   :file: http-standard-response-codes.csv
