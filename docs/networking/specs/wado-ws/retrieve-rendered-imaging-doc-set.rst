WADO-WS Retrieve Rendered Imaging Document Set Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _specification:

Specification
"""""""""""""

.. csv-table:: WADO-WS Retrieve Rendered Imaging Document Set Specification
   :header: "Parameter", "Support", "Restrictions"
   :widths: 15, 7, 30

   "SOP Class", "YES", "See *Image Storage SOP Classes* in :ref:`SOPClasses`"
   "Rows", "YES", "Must be greater than 0"
   "Columns", "YES", "Must be greater than 0"
   "Region", "NO",
   "Window Center", "YES", "None"
   "Window Width", "YES", "None"
   "Image Quality", "YES", "None"
   "Content Type", "YES", "image/jpeg"
   "Annotation", "NO",
   "Presentation UID", "NO",
   "Presentation Series UID", "NO",
   "Anonymize", "NO",


.. _endpoint-url:

Web Service Endpoint URL
""""""""""""""""""""""""

*http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource*


.. _request-response:

Retrieve Rendered Imaging Document Set Example
""""""""""""""""""""""""""""""""""""""""""""""

Sample Request
''''''''''''''

.. literalinclude:: retrieve-rendered-imaging-doc-set-request.txt

Sample Response
'''''''''''''''

.. literalinclude:: retrieve-rendered-imaging-doc-set-response.txt


.. _error-codes:

Error Codes
"""""""""""

The following errorCodes are used to report any of the associated error and warning situations.

.. csv-table:: Error Codes
   :header: "Error Code", "Error Situation"
   :widths: 20, 35
   :file: error-codes.csv

