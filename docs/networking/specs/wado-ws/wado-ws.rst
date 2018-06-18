WADO-WS Specifications
======================

WADO-WS Retrieve Imaging Document Set Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: WADO-WS Retrieve Imaging Document Set Specification
   :header: "Parameter", "Restrictions"
   :widths: 15, 30

   "Transfer Syntaxes Supported", "See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`, :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS`"
   "SOP Class Restrictions", "See - :ref:`SOPClasses`"

Web Service Endpoint URL
""""""""""""""""""""""""

*http[s]://<host>:<port>/dcm4chee-arc/xdsi/ImagingDocumentSource*

Retrieve Imaging Document Set Example
"""""""""""""""""""""""""""""""""""""

Sample Request
''''''''''''''

.. literalinclude:: rad69-request.txt

Sample Response
'''''''''''''''

.. literalinclude:: rad69-response.txt

Error Codes
"""""""""""

The following errorCodes are used to report any of the associated error and warning situations.

.. csv-table:: Error Codes
   :header: "Error Code", "Error Situation"
   :widths: 20, 35
   :file: error-codes.csv

WADO-WS Retrieve Rendered Imaging Document Set Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Specification
"""""""""""""

.. csv-table:: WADO-WS Retrieve Rendered Imaging Document Set Specification
   :header: "Parameter", "Support", "Restrictions"
   :widths: 15, 7, 30

   "SOP Class", "✓", "See *Image Storage SOP Classes* in :ref:`SOPClasses`"
   "Rows", "✓", "None"
   "Columns", "✓", "None"
   "Region", "✗",
   "Window Center", "✓", "None"
   "Window Width", "✓", "None"
   "Image Quality", "✓", "None"
   "Content Type", "✓", "`image/jpeg`"
   "Annotation", "✗",
   "Presentation UID", "✗",
   "Presentation Series UID", "✗",
   "Anonymize", "✗",


Web Service Endpoint URL
""""""""""""""""""""""""

*http[s]://<host>:<port>/dcm4chee-arc/xdsi/ImagingDocumentSource*


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

