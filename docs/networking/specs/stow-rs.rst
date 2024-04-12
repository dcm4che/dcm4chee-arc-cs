STOW-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _stow-rs-store-instances:

STOW-RS Store Instance
""""""""""""""""""""""

.. csv-table:: STOW-RS Store Instances Specification
   :header: "Category", "Restrictions"
   :widths: 15, 30

   "Media Types Supported (Accept header)", "Restricted to application/dicom or application/dicom+xml"
   "Transfer Syntaxes Supported (Media Type parameter)", "See - :ref:`SCPImageTS`, :ref:`SCPVideoTS`, :ref:`SCPStructuredReportTS` and :ref:`SCPOtherTS`"
   "SOP Class Restrictions", "See - :ref:`SOPClasses`"

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
   :widths: 10, 15, 30

   "Failure", "400 - Bad Request", "This indicates that the STOW-RS Service was unable to store any instances due to bad syntax."
   "", "401 - Unauthorized", "This indicates that the STOW-RS Service refused to create or append any instances because the client is not authenticated."
   "", "403 - Forbidden", "This indicates that the STOW-RS Service understood the request, but is refusing to fulfill it (e.g., an authenticated user with insufficient privileges)."
   "", "409 - Conflict", "This indicates that the STOW-RS Service request was formed correctly but the service was unable to store any instances due to a conflict in the request (e.g., unsupported SOP Class or Study Instance UID mismatch). This may also be used to indicate that a STOW-RS Service was unable to store any instances for a mixture of reasons. Additional information regarding the instance errors can be found in the XML response message body."
   "", "503 - Busy", "This indicates that the STOW-RS Service was unable to store any instances because it was out of resources."
   "Warning", "202 - Accepted", "This indicates that the STOW-RS Service stored some of the instances but warnings or failures exist for others. Additional information regarding this error can be found in the XML response message body."
   "Success", "200 - OK", "This indicates that the STOW-RS Service successfully stored all the instances."

The following table indicates the meaning of values returned in **FailureReason (0008,1197)** tag in any of the above STOW-RS error responses

.. csv-table:: STOW-RS Error Response Status Return Reasons
    :header-rows: 1
    :widths: 10, 15, 5, 20, 20
    :file: stow-rs-error-response-status-return-reasons.csv


Web Service Endpoint URL
''''''''''''''''''''''''

*http[s]://<host>:<port>/dcm4chee-arc/aets/{AETitle}/rs*

Replace *{AETitle}* in the URL with the configured AE title.