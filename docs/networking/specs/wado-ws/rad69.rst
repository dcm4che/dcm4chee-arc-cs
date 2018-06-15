WADO-WS Retrieve Imaging Document Set Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: WADO-WS Retrieve Imaging Document Set Specification
   :header: "Parameter", "Restrictions"
   :widths: 15, 30

   "Transfer Syntaxes Supported", "See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`, :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS`"
   "SOP Class Restrictions", "See - :ref:`SOPClasses`"


.. _endpoint-url:

Web Service Endpoint URL
""""""""""""""""""""""""

*http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource*


.. _request-response:

Sample Request Response Example
"""""""""""""""""""""""""""""""

.. literalinclude:: rad69-example.txt


Error Codes
"""""""""""

The following errorCodes are used to report any of the associated error and warning situations.

.. csv-table:: Error Codes
   :header: "Error Code", "Error Situation"
   :widths: 20, 35
   :file: error-codes.csv
