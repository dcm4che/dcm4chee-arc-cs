WADO-RS Specifications
^^^^^^^^^^^^^^^^^^^^^^

.. _wado-rs-retrieve-study:

WADO-RS Retrieve Study
""""""""""""""""""""""

.. table:: WADO-RS Retrieve Study

   +----------------------------------------------------------------+----------------------------------------------------+
   |                     Options                                    |               Restrictions                         |
   +================================================================+====================================================+
   |                                                                | multipart/related;type=application/dicom           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/octet-stream    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/pdf             |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jp2                   |
   |            Data Types Supported (Accept Type)                  |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpx                   |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-dicom+rle           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-jls                 |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=text/xml                    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mp4                   |
   |                                                                |----------------------------------------------------+
   |                                                                | application/zip                                    |
   +----------------------------------------------------------------+----------------------------------------------------+
   | Transfer Syntaxes Supported (transfer-syntax Accept parameter) | See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`,        |
   |                                                                | :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS` |
   +----------------------------------------------------------------+----------------------------------------------------+
   | SOP Class restrictions                                         | See - :ref:`SOPClasses`                            |
   +----------------------------------------------------------------+----------------------------------------------------+

.. _wado-rs-retrieve-series:

WADO-RS Retrieve Series
"""""""""""""""""""""""

.. table:: WADO-RS Retrieve Series

   +----------------------------------------------------------------+----------------------------------------------------+
   |                     Options                                    |               Restrictions                         |
   +================================================================+====================================================+
   |                                                                | multipart/related;type=application/dicom           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/octet-stream    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/pdf             |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jp2                   |
   |            Data Types Supported (Accept Type)                  |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpx                   |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-dicom+rle           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-jls                 |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=text/xml                    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mp4                   |
   |                                                                |----------------------------------------------------+
   |                                                                | application/zip                                    |
   +----------------------------------------------------------------+----------------------------------------------------+
   | Transfer Syntaxes Supported (transfer-syntax Accept parameter) | See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`,        |
   |                                                                | :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS` |
   +----------------------------------------------------------------+----------------------------------------------------+
   | SOP Class restrictions                                         | See - :ref:`SOPClasses`                            |
   +----------------------------------------------------------------+----------------------------------------------------+

.. _wado-rs-retrieve-instance:

WADO-RS Retrieve Instance
"""""""""""""""""""""""""

.. table:: WADO-RS Retrieve Instance

   +----------------------------------------------------------------+----------------------------------------------------+
   |                     Options                                    |               Restrictions                         |
   +================================================================+====================================================+
   |                                                                | multipart/related;type=application/dicom           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/octet-stream    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/pdf             |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jp2                   |
   |            Data Types Supported (Accept Type)                  |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpx                   |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-dicom+rle           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-jls                 |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=text/xml                    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mp4                   |
   |                                                                |----------------------------------------------------+
   |                                                                | application/zip                                    |
   +----------------------------------------------------------------+----------------------------------------------------+
   | Transfer Syntaxes Supported (transfer-syntax Accept parameter) | See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`,        |
   |                                                                | :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS` |
   +----------------------------------------------------------------+----------------------------------------------------+
   | SOP Class restrictions                                         | See - :ref:`SOPClasses`                            |
   +----------------------------------------------------------------+----------------------------------------------------+

.. _wado-rs-retrieve-frames:

WADO-RS Retrieve Frames
"""""""""""""""""""""""

.. table:: WADO-RS Retrieve Frames

   +----------------------------------------------------------------+----------------------------------------------------+
   |                     Options                                    |               Restrictions                         |
   +================================================================+====================================================+
   |                                                                | multipart/related;type=application/octet-stream    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/pdf             |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jp2                   |
   |            Data Types Supported (Accept Type)                  |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpx                   |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-dicom+rle           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-jls                 |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=text/xml                    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mp4                   |
   |                                                                |----------------------------------------------------+
   |                                                                | application/zip                                    |
   +----------------------------------------------------------------+----------------------------------------------------+
   | Transfer Syntaxes Supported (transfer-syntax Accept parameter) | See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`,        |
   |                                                                | :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS` |
   +----------------------------------------------------------------+----------------------------------------------------+
   | SOP Class restrictions                                         | Restricted to Multi-Frame Image Objects            |
   +----------------------------------------------------------------+----------------------------------------------------+

.. _wado-rs-retrieve-bulkdata:

WADO-RS Retrieve Bulk Data
""""""""""""""""""""""""""

.. table:: WADO-RS Retrieve Bulk Data

   +----------------------------------------------------------------+----------------------------------------------------+
   |                     Options                                    |               Restrictions                         |
   +================================================================+====================================================+
   |                                                                | multipart/related;type=application/octet-stream    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=application/pdf             |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jp2                   |
   |            Data Types Supported (Accept Type)                  |----------------------------------------------------+
   |                                                                | multipart/related;type=image/jpx                   |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-dicom+rle           |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=image/x-jls                 |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=text/xml                    |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mpeg                  |
   |                                                                |----------------------------------------------------+
   |                                                                | multipart/related;type=video/mp4                   |
   |                                                                |----------------------------------------------------+
   |                                                                | application/zip                                    |
   +----------------------------------------------------------------+----------------------------------------------------+
   | Transfer Syntaxes Supported (transfer-syntax Accept parameter) | See - :ref:`SCUImageTS`, :ref:`SCUVideoTS`,        |
   |                                                                | :ref:`SCUStructuredReportTS` and :ref:`SCUOtherTS` |
   +----------------------------------------------------------------+----------------------------------------------------+
   | SOP Class restrictions                                         | See - :ref:`SOPClasses`                            |
   +----------------------------------------------------------------+----------------------------------------------------+

.. _wado-rs-retrieve-metadata:

WADO-RS Retrieve Metadata
"""""""""""""""""""""""""

.. table:: WADO-RS Retrieve Metadata for Study or Series or Instance

   +----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
   |                     Options                                    |               Restrictions                                                                              |
   +================================================================+=========================================================================================================+
   |                                                                | multipart/related;type=application/dicom+xml                                                            |
   |                                                                |---------------------------------------------------------------------------------------------------------+
   |            Data Types Supported (Accept Type)                  | application/dicom+json                                                                                  |
   |                                                                |---------------------------------------------------------------------------------------------------------+
   |                                                                | application/json                                                                                        |
   +----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
   |               Accept-Encoding                                  | Restricted to gzip, deflate, or identity (the use                                                       |
   |                                                                | of no transformation whatsoever). See                                                                   |
   |                                                                | `W3C RFC 2616 Protocol Parameters Section 3.5 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html>`_ |
   |                                                                | for more information.                                                                                   |
   +----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
   |              SOP Class restrictions                            | See - :ref:`SOPClasses`                                                                                 |
   +----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

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

Web Service Endpoint URL
''''''''''''''''''''''''

*http[s]://<host>:<port>/dcm4chee-arc/aets/{AETitle}/rs*

Replace *{AETitle}* in the URL with the configured AE title.