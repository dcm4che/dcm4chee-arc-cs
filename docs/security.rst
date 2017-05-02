Security
========

.. _security-profiles:

Security Profiles
"""""""""""""""""

.. _secure-transport-connection-profiles:

Secure Transport Connection Profiles
''''''''''''''''''''''''''''''''''''

|product| supports the *Basic TLS Secure Transport Connection Profile* and the
*AES TLS Secure Transport Connection Profile* as specified in
`DICOM Standard, Part 15, Annex B.1 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_B.1.html>`_
and `Annex B.3 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_B.3.html>`_.

By default configuration, TLS 1.0, TLS 1.1 and TLS 1.2 are enabled, use of TLS 1.2 is preferred.

Also other cyphersuite options than the two in compliance with *AES TLS Secure Transport Connection Profile*:

- TLS_RSA_WITH_AES_128_CBC_SHA
- TLS_RSA_WITH_3DES_EDE_CBC_SHA

may be configured.

Beside DICOM DIMSE service connections, also HL7 v2 and HTTP connections can be secured by use of TLS.

IP ports on which an implementation accepts TLS connections are configurable.

The private key and the Certificate used by an instance of |product| to identify itself in the TLS negotiation
with remote applications has to be provided in a local keystore file in PKCS12 or JKS (Java Key Store) format
on the application host. Certficates of Certificate Authorities (CA) to validate Certificates received
from remote applications during the TLS negotiation can also be provided in a local keystore file in JKS format
or at the central LDAP server, used as configuration backend for all instances of |product|.

.. _network-address-management-profiles:

Network Address Management Profiles
'''''''''''''''''''''''''''''''''''

|product| supports the *Basic Network Address Management Profile* as *DHCP Client* and *DNS Client* actor utilizing
network configuration options of the underlying operating system.
S. `DICOM Standard, Part 15, Annex F.1 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_F.html#sect_F.1>`_.

.. _time-synchronization-profiles:

Time Synchronization Profiles
'''''''''''''''''''''''''''''

|product| supports the *Basic Time Synchronization Profile* as *DHCP Client* and *NTP Client* actor utilizing
time synchronization options of the underlying operating system.
S. `DICOM Standard, Part 15, Annex G.1 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_G.html#sect_G.1>`_.

.. _application-configuration-management-profiles:

Application Configuration Management Profiles
'''''''''''''''''''''''''''''''''''''''''''''

|product| supports the *Application Configuration Management Profile* as *LDAP Client* actor. Any LDAP v3 compatible
LDAP server can be used as configuration backend for multiple instances of |product| - and may also be shared with
external DICOM applications which also supports the *Application Configuration Management Profile* as *LDAP Client*
actor.
S. `DICOM Standard, Part 15, Annex H.1 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_H.html#sect_H.1>`_.

.. _audit-trail-profiles:

Audit Trail Profiles
''''''''''''''''''''

Audit Trail Message Format Profile
----------------------------------

|product| supports the *Audit Trail Message Format Profile* as specified in
`DICOM Standard, Part 15, Annex A.5 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_A.5.html>`_.

Audit Messages
..............

.. toctree::

   audit/general-message
   audit/application-activity
   audit/audit-log-used
   audit/begin-transferring-dicom-instances
   audit/data-export
   audit/dicom-instances-accessed
   audit/dicom-instances-transferred
   audit/dicom-study-deleted
   audit/query
   audit/security-alert
   audit/user-authentication
   audit/patient-record
   audit/procedure-record

Audit Trail Message Transmission Profile - SYSLOG-TLS
-----------------------------------------------------

|product| supports the *Audit Trail Message Transmission Profile - SYSLOG-TLS* as specified in
`DICOM Standard, Part 15, Annex A.6 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_A.6.html>`_.

Audit Trail Message Transmission Profile - SYSLOG-UDP
-----------------------------------------------------

|product| supports the *Audit Trail Message Transmission Profile - SYSLOG-UDP* as specified in
`DICOM Standard, Part 15, Annex A.7 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_A.7.html>`_.

.. _security-association-level-security:

Association Level Security
""""""""""""""""""""""""""

|product| checks that the Association requestor specifies the correct Called AE Title. Each AE can be configured to
accept Association Requests from only a limited list of Calling AE Titles. In addition the IP address of the requestor
can be checked. Each AE can be configured to accepted only a limited list of Move Destinations in C-MOVE requests.

Each AE can be configured to associate a particular *Access Control ID* to received Studies - optionally also
dependend on the Sending AE Title or on any DICOM Attribute of the first received object of the Study. Each AE can
also be configured to hide Studies from access by Query/Retrieve services which associated *Access Control ID* does
not match with a list of *Access Control IDs* associated with that AE.

Each AE can be configured to hide objects rejected by
`IHE IOCM Rejection Notes <http://wiki.ihe.net/index.php/Imaging_Object_Change_Management>`_ from access by
Query/Retrieve services dependend on the *Key Object Selection Document Title* of the *Rejection Note*.

|product| can be configured to check the Receiving Application and Facility in received HL7 v2 messages. Each
HL7 Application provided by |product| can be configured to accept HL7 v2 messages from only a limited list of Sending
Application and Facility names.

.. _security-application-level-security:

Application Level Security
""""""""""""""""""""""""""

RESTful services and the Web UI may be secured with `OpenID Connect <http://openid.net/connect/>`_ using
`Keycloak <http://www.keycloak.org>`_ as Authentication Server.
