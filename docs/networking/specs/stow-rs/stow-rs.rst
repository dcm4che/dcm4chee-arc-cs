STOW-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _stow-rs-store-instances:

STOW-RS Store Instance
""""""""""""""""""""""

.. csv-table:: STOW-RS Store Instances Specification
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
The maximal number of simultaneous HTTP Requests is configurable. It is unlimited by default.

.. csv-table:: Number of HTTP Requests Supported

   "Maximum number of simultaneous HTTP requests", "No Maximum Limit (Configurable)"

.. _stow-rs-sop-specific-conformance-for-sop-classes:

SOP Specific Conformance for SOP Class(es)
''''''''''''''''''''''''''''''''''''''''''
The DCM4CHEE-STOW-SERVICE response message header contains status codes indicating success, warning, or failure as shown in the "HTTP Standard Response Codes" below. No additional status codes are used.

.. csv-table:: HTTP Standard Response Codes
   :header: "Service Status", "HTTP Status Code", "STOW-RS Description"
   :file: http-standard-response-codes.csv