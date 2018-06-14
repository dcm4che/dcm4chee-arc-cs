WADO-URI Specification
^^^^^^^^^^^^^^^^^^^^^^

.. _wado-uri-retrieve-imaging-document-set:

WADO-URI Retrieve Imaging Document Set
""""""""""""""""""""""""""""""""""""""

.. csv-table:: WADO-URI Retrieve Imaging Documents Specification
   :header: "Parameter", "Restrictions"

   "Transfer Syntaxes Supported", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class Restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

If the URI Retrieve specifies no transfer syntax that is supported by the archive, the SOP Instance will be returned using the Implicit VR Little Endian Transfer Syntax.

.. _wado-uri-retrieve-rendered-imaging-document-set:

WADO-URI Retrieve Rendered Imaging Document Set
"""""""""""""""""""""""""""""""""""""""""""""""

.. csv-table:: WADO-URI Retrieve Rendered Imaging Documents Specification
   :header: "Parameter", "Restrictions"

   "Transfer Syntaxes Supported", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to sizes supported by the hosting DCM4CHEE ARCHIVE"
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
