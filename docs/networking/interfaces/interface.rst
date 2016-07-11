Network Interfaces
^^^^^^^^^^^^^^^^^^

.. _interface-physical-network-interface:

Physical Network Interface
""""""""""""""""""""""""""

The DCM4CHEE archive supports a single network interface. One of the following physical network interfaces will be available depending on installed hardware options:

.. csv-table:: Supported Physical Network Interfaces
   :file: physical-network-interface.csv

.. _interface-additional-protocols:

Additional Protocols
""""""""""""""""""""

DCM4CHEE archive conforms to the System Management Profiles listed in table below. All requested transactions for the listed profiles and actors are supported. It does not support any optional transactions.

.. csv-table:: Supported Physical Network Interfaces
   :header: "Profile Name", "Actor", "Protocols Used", "Optional Transactions", "Security Support"
   :file: supported-system-management-profiles.csv

DHCP
''''

DHCP can be used to obtain TCP/IP network configuration information. The network parameters obtainable via DHCP are shown in table below. The Default Value column of the table shows the default used if the DHCP server does not provide a value. Values for network parameters set in the Service/Installation tool take precedence over values obtained from the DHCP server. Support for DHCP can be configured via the Service/Installation Tool. The Service/Installation tool can be used to configure the machine name. If DHCP is not in use, TCP/IP network configuration information can be manually configured via the Service/Installation Tool.

.. csv-table:: Supported DHCP Parameters
   :header: "DHCP Parameter", "Default Value"
   :file: supported-dhcp-parameters.csv

If the DHCP server refuses to renew a lease on the assigned IP address all active DICOM Associations will be aborted.


DNS
'''

DNS can be used for address resolution. If DHCP is not in use or the DHCP server does not return any DNS server addresses, the identity of a DNS server can be configured via the Service/Installation Tool. If a DNS server is not in use, local mapping between hostname and IP address can be manually configured via the Service/Installation Tool.

.. _interface-ip-support:

IPv4 and IPv6 Support
"""""""""""""""""""""

This product supports both IPv4 and IPv6. It does not utilize any of the optional configuration identification or security features of IPv6.