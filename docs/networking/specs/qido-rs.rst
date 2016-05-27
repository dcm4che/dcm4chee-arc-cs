QIDO-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _qido-rs-search-for-studies

QIDO-RS Search For Studies
""""""""""""""""""""""""""

.. csv-table:: Table 4.2.7.1-1.: QIDO-RS Search for Studies Specification
   :header: "Parameter", "Restrictions"
   :file: qido-rs-search-for-studies.csv


.. csv-table:: Table 4.2.7.1-1a.: QIDO-RS Study Attribute Matching
   :header: "Keyword", "Tag", "Types of Matching"
   :file: qido-rs-study-attribute-matching.csv

Types of Matching:
''''''''''''''''''
"S" indicates the identifier attribute uses Single Value Matching
"L" indicates UID List Matching
"U" indicates Universal Matching.
Note : If only Universal Matching is supported for an attribute then that attribute can only be passed as an "includefield" query key
"*" indicates wild card matching
"R" indicates Range Matching
"SEQUENCE" indicates Sequence Matching
"NONE" indicates that no matching is supported, but that values for this Element requested will be returned with all requests
"UNIQUE" indicates that this is the Unique Key for that query level, in which case Universal Matching or Single Value Matching is used depending on the query level (see Section C.2.2.1.1 “Unique Keys” in PS3.4 ).

Section 1b : Extended Negotiation
'''''''''''''''''''''''''''''''''
DCM4CHEE-QIDO-SERVICE does not support the "fuzzymatching" query key.
DCM4CHEE-QIDO-SERVICE will perform case insensitive matching for PN VR attributes but will not perform other forms of fuzzy matching. This applies to the following attributes:
    > Referring Physician's Name (0008,0090)
    > Physician(s) of Record (0008,1048)
    > Patient's Name (0010,0010)

.. _qido-rs-search-for-series

QIDO-RS Search For Series
"""""""""""""""""""""""""

.. csv-table:: Table 4.2.7.2-1.: QIDO-RS Search for Series Specification
   :header: "Parameter", "Restrictions"
   :file: qido-rs-search-for-series.csv


.. csv-table:: Table 4.2.7.2-1a.: QIDO-RS Series Attribute Matching
   :header: "Keyword", "Tag", "Types of Matching"
   :file: qido-rs-series-attribute-matching.csv

Types of Matching: As explained above in QIDO-RS Search For Studies

.. _qido-rs-search-for-instances

QIDO-RS Search For Instances
""""""""""""""""""""""""""""

.. csv-table:: Table 4.2.7.3-1.: QIDO-RS Search for Instances Specification
   :header: "Parameter", "Restrictions"
   :file: qido-rs-search-for-instances.csv


.. csv-table:: Table 4.2.7.3-1a.: QIDO-RS Instance Attribute Matching
   :header: "Keyword", "Tag", "Types of Matching"
   :file: qido-rs-instances-attribute-matching.csv

Types of Matching: As explained above in QIDO-RS Search For Studies

.. _qido-rs-connection-policies

QIDO-RS Connection Policies
""""""""""""""""""""""""""""

.. _qido-rs-general

General
'''''''
All standard RS connection policies apply. There are no extensions for RS options.

.. _qido-rs-number-of-connections:

Number Of Connections
'''''''''''''''''''''
DCM4CHEE-QIDO-SERVICE limits the number of simultaneous RS requests. Additional requests will be queued after the HTTP connection is accepted. When an earlier request completes, a pending request will proceed.

.. csv-table:: Table 4.2.7.4-1.: Number of HTTP Requests Supported
   :file: qido-rs-stow-rs-wado-uri-wado-rs-number-of-connections.csv

.. _qido-rs-asynchronous-nature:

Asynchronous Nature
'''''''''''''''''''
DCM4CHEE-QIDO-SERVICE does not support RS asynchronous response.

.. _qido-rs-response-status:

Response Status
'''''''''''''''
DCM4CHEE-QIDO-SERVICE shall provide a response message header containing the appropriate status code indicating success, warning, or failure as shown below

.. csv-table:: Table 4.2.7.4-2.: HTTP Standard Response Codes
   :header: "Code", "Name", "Description"
   :file: qido-rs-http-standard-response-codes.csv
