WADO-URI Specification
^^^^^^^^^^^^^^^^^^^^^^

.. _wado-uri-retrieve-imaging-document-set:

WADO-URI Retrieve Imaging Document Set
""""""""""""""""""""""""""""""""""""""

.. csv-table:: WADO-URI Retrieve Imaging Documents Specification
   :header: "Parameter", "Restrictions"
   :widths: 15, 30

   "Transfer Syntaxes Supported", "See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`, :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS`"
   "SOP Class Restrictions", "Same as - :ref:`SOPClasses2`"

If the URI Retrieve specifies no transfer syntax that is supported by the archive, the SOP Instance will be returned using the Implicit VR Little Endian Transfer Syntax.

.. _wado-uri-retrieve-rendered-imaging-document-set:

WADO-URI Retrieve Rendered Imaging Document Set
"""""""""""""""""""""""""""""""""""""""""""""""

.. csv-table:: WADO-URI Retrieve Rendered Imaging Documents Specification
   :header: "Parameter", "Restrictions"
   :widths: 15, 30

   "Transfer Syntaxes Supported", "See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`, :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS`"
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Rendered formats available", "Supports JPEG, GIF and PDF for IMAGE IODS, and PDF for non-IMAGE IODS."
   "Rows restrictions", "Must be greater than 0"
   "Columns restrictions", "Must be greater than 0"
   "Region restrictions", "None"
   "Window Center restrictions", "Whole window must be in the range of image pixel values."
   "Window Width restrictions", "Must be greater than 4 and whole window must be in the range of image pixel values."
   "Image Quality restrictions", "None"
   "Annotation Restrictions", "None"
   "Compression available", "JPEG"
   "Other restrictions", "None"

.. _wado-uri-retrieve-imaging-document-set-metadata:

WADO-URI Retrieve Imaging Document Set Metadata
"""""""""""""""""""""""""""""""""""""""""""""""

Not Supported

.. _wado-uri-connection-policies:

WADO-URI Connection Policies
""""""""""""""""""""""""""""

.. _wado-uri-general:

General
'''''''
All URI connections are limited to HTTP GET requests. The DCM4CHEE-WADO-SERVICE ignores all unknown HTTP header parameters.

.. _wado-uri-number-of-connections:

Number Of Connections
'''''''''''''''''''''
The maximal number of simultaneous HTTP Requests is configurable. It is unlimited by default.

.. csv-table:: Number of HTTP Requests Supported

   "Maximum number of simultaneous HTTP requests", "No Maximum Limit (Configurable)"


Web Service Endpoint URL
''''''''''''''''''''''''

*http[s]://<host>:<port>/dcm4chee-arc/aets/{AETitle}/wado*

Replace *{AETitle}* in the URL with the configured AE title.