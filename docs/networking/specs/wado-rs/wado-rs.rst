WADO-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _wado-rs-retrieve-study:

WADO-RS Retrieve Study
""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Study
   :header: "Options", "Restrictions"
   :file: retrieve-study-series-instance.csv

.. _wado-rs-retrieve-series:

WADO-RS Retrieve Series
"""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Series
   :header: "Options", "Restrictions"
   :file: retrieve-study-series-instance.csv

.. _wado-rs-retrieve-instance:

WADO-RS Retrieve Instance
"""""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Instance
   :header: "Options", "Restrictions"
   :file: retrieve-study-series-instance.csv

.. _wado-rs-retrieve-frames:

WADO-RS Retrieve Frames
"""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Frames
   :header: "Options", "Restrictions"
   :file: retrieve-frames.csv

.. _wado-rs-retrieve-bulkdata:

WADO-RS Retrieve Bulk Data
""""""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Bulk Data
   :header: "Options", "Restrictions"
   :file: retrieve-bulkdata.csv

.. _wado-rs-retrieve-metadata:

WADO-RS Retrieve Metadata
"""""""""""""""""""""""""

.. csv-table:: WADO-RS Retrieve Metadata
   :header: "Options", "Restrictions"
   :file: retrieve-metadata.csv

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
