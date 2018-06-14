WADO-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _wado-rs-retrieve-study:

WADO-RS Retrieve Study
""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Study
   :header: "Options", "Restrictions"

   "Data Types Supported (Accept Type)", "Restricted to application/dicom or application/octet-stream"
   "Transfer Syntaxes Supported (transfer-syntax Accept parameter)", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

.. _wado-rs-retrieve-series:

WADO-RS Retrieve Series
"""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Series
   :header: "Options", "Restrictions"

   "Data Types Supported (Accept Type)", "Restricted to application/dicom or application/octet-stream"
   "Transfer Syntaxes Supported (transfer-syntax Accept parameter)", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

.. _wado-rs-retrieve-instance:

WADO-RS Retrieve Instance
"""""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Instance
   :header: "Options", "Restrictions"

   "Data Types Supported (Accept Type)", "Restricted to application/dicom or application/octet-stream"
   "Transfer Syntaxes Supported (transfer-syntax Accept parameter)", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

.. _wado-rs-retrieve-frames:

WADO-RS Retrieve Frames
"""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Frames
   :header: "Options", "Restrictions"

   "Data Types Supported (Accept Type)", "Restricted to application/octet-stream"
   "Transfer Syntaxes Supported (transfer-syntax Accept parameter)", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class restrictions", "Restricted to Multi-Frame Image Objects"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

.. _wado-rs-retrieve-bulkdata:

WADO-RS Retrieve Bulk Data
""""""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Bulk Data
   :header: "Options", "Restrictions"

   "Data Types Supported (Accept Type)", "Restricted to application/octet-stream"
   "Transfer Syntaxes Supported (transfer-syntax Accept parameter)", "Same as Transfer Syntaxes listed in - :ref:`PresentationContext`"
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

.. _wado-rs-retrieve-metadata:

WADO-RS Retrieve Metadata
"""""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Metadata
   :header: "Options", "Restrictions"

   "Data Types Supported (Accept Type)", "Restricted to application/dicom+xml"
   "Accept-Encoding", "Restricted to gzip, deflate, or identity (the use of no transformation whatsoever). See `W3C RFC 2616 Protocol Parameters Section 3.5 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html>`_ for more information."
   "SOP Class restrictions", "Same as - :ref:`SOPClasses2`"
   "Size restriction", "Restricted to size supported by the hosting DCM4CHEE ARCHIVE"

.. _wado-rs-connection-policies:

WADO-RS Connection Policies
"""""""""""""""""""""""""""

.. _wado-rs-general:

General
'''''''
All standard RS connection policies apply. There are no extensions for RS options.

.. _wado-rs-number-of-connections:

Number Of Connections
'''''''''''''''''''''
The maximal number of simultaneous HTTP Requests is configurable. It is unlimited by default.

.. csv-table:: Number of HTTP Requests Supported

   "Maximum number of simultaneous HTTP requests", "No Maximum Limit (Configurable)"
