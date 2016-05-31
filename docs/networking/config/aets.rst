AE Title/Presentation Address Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _aets-local-aets:

Local AE Titles
"""""""""""""""

The mapping from AE Title to TCP/IP addresses and ports is configurable and set at the time of installation by Installation Personnel.

.. csv-table:: Table 4.4.1-1.: Default Application Entity Characteristics
   :header: "Application Entity", "Role", "Default AE Title", "Default TCP/IP Port"
   :file: default-ae-characteristics.csv

The STORAGE-SCU and QUERY-RETRIEVE-SCP Application Entities can be configured to have the same AE Title. The STORAGE-SCP Application Entity must not have the same AE Title as the other two.

Remote AE Title/Presentation Address Mapping
""""""""""""""""""""""""""""""""""""""""""""

The mapping of external AE Titles to TCP/IP addresses and ports is configurable and set at the time of installation by Installation Personnel. This mapping is necessary for resolving the IP address and port of C-MOVE Destination Application Entities and must be correctly configured for the QUERY-RETRIEVE-SCP AE to correctly function as a C-MOVE SCP.