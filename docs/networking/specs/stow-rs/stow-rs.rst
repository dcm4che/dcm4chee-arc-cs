STOW-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _stow-rs-store-instances:

STOW-RS Store Instance
""""""""""""""""""""""

.. csv-table:: Table 4.2.4.1-1.: STOW-RS Store Instances Specification
   :header: "Category", "Restrictions"
   :file: store-instances-specs.csv

.. _stow-rs-connection-policies:

Connection Policies
"""""""""""""""""""

.. _stow-rs-general:

General
'''''''
All standard RS connection policies apply. There are no extensions for RS options.

.. _stow-rs-number-of-connections:

Number Of Connections
'''''''''''''''''''''
DCM4CHEE-STOW-SERVICE limits the number of simultaneous RS requests. Additional requests will be queued after the HTTP connection is accepted. When an earlier request completes, a pending request will proceed.

.. csv-table:: Table 4.2.4.2-1.: Number of HTTP Requests Supported
   :file: common/qido-rs-stow-rs-wado-uri-wado-rs-number-of-connections.csv

.. _stow-rs-asynchronous-nature:

Asynchronous Nature
'''''''''''''''''''
DCM4CHEE-STOW-SERVICE does not support RS asynchronous response.

.. _stow-rs-sop-specific-conformance-for-sop-classes:

SOP Specific Conformance for SOP Class(es)
''''''''''''''''''''''''''''''''''''''''''
The DCM4CHEE-STOW-SERVICE response message header contains status codes indicating success, warning, or failure as shown in the "HTTP Standard Response Codes" below. No additional status codes are used.

.. csv-table:: Table 4.2.4.2-2.: HTTP Standard Response Codes
   :header: "Service Status", "HTTP Status Code", "STOW-RS Description"
   :file: http-standard-response-codes.csv