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

.. _attribute-confidentiality-profiles:

Attribute Confidentiality Profiles
''''''''''''''''''''''''''''''''''

Basic Application Level Confidentiality Profile
-----------------------------------------------
|product| supports the *Basic Application Level Confidentiality Profile* as specified in
`DICOM Standard, Part 15, Annex E.2 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.2.html>`_
with the *Basic Application Level Confidentiality Options*:

- *Retain Longitudinal Temporal Information Full Dates Option* as specified in
  `DICOM Standard, Part 15, Annex E.3.6 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.6.html>`_
- *Retain Device Identity Option* as specified in
  `DICOM Standard, Part 15, Annex E.3.8 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.8.html>`_
- *Retain UIDs Option* as specified in
  `DICOM Standard, Part 15, Annex E.3.9 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.9.html>`_
- *Retain Institution Identity Option* as specified in
  `DICOM Standard, Part 15, Annex E.3.11 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.11.html>`_

Attributes removed or replaced
..............................

One can directly refer the table `Application Level Confidentiality Profile Attributes <http://dicom.nema.org/medical/dicom/current/output/html/part15.html#table_E.1-1>`_
with different `action codes <http://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_E.1.1>`_ to see
the list of attributes supported dependent on the applied *Basic Application Level Confidentiality Option*.

In addition to the above list of attributes, below table lists out the private attributes and some more DICOM attributes
which are missing in `Application Level Confidentiality Profile Attributes <http://dicom.nema.org/medical/dicom/current/output/html/part15.html#table_E.1-1>`_
to be removed.

.. csv-table:: Attributes removed during protection
   :header: "Attributes"
   :widths: 30
   :file: removed-attributes.csv

Inserted dummy values
.....................

Following table lists attributes and the dummy values which are used to replace the attributes' values

.. csv-table:: Dummy values used to replace the attributes' values
   :header: "VR", "Dummy Value", "Attributes"
   :widths: 4, 15, 30
   :file: dummy-values.csv

Encrypted Attributes Data Sets
..............................

Encryption of attributes data sets for later re-identification is not supported.

Scope of Referential Integrity of Replacement Values for UIDs
.............................................................

Replacement UIDs are derived from the original UID by using the algorithm for Creating Name-Based UUIDs as specified in
`RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace <https://tools.ietf.org/html/rfc4122#section-4.3>`_,
encoded as UID according `Object Identifier (OID) Repository <http://oid-info.com/get/2.25>`_. Therefore equal original
UIDs in different DICOM objects also accross Studies or Patients are replaced by equal new UIDs in resulting objects.
