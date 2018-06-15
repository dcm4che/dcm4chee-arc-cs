WADO-WS Retrieve Imaging Document Set Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: WADO-WS Retrieve Imaging Document Set Specification
   :header: "Parameter", "Restrictions"

   "Transfer Syntaxes Supported", "Same as Transfer Syntaxes listed in - :ref:`SCUImageTS`, :ref:`SCUVideoTS`, :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS`"
   "SOP Class Restrictions", "Same as - :ref:`SOPClasses2`"


.. _endpoint-url:

Web Service Endpoint URL
""""""""""""""""""""""""

_**http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource**_


.. _request-response:

Sample Request Response Example
"""""""""""""""""""""""""""""""

.. toctree::

   rad69-example

Error Codes
"""""""""""

The following errorCodes are used to report any of the associated error and warning situations.

.. csv-table:: Error Codes
   :header: "Error Code", "Error Situation"
   :widths: 20, 35
   :file: error-codes.csv
