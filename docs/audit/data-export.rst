Data Export
===========

Trigger Events
--------------

This message is emitted by archive for XDSI `RAD-68 <http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol3.pdf#page=163>`_ transactions.

Message Structure
-----------------

- :ref:`audit-data-export-event`
- :ref:`audit-data-export-active-participant-user` (1) - This active participant is present only if export is triggered by UI.
- :ref:`audit-data-export-active-participant-source` (1)
- :ref:`audit-data-export-active-participant-destination` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-data-export-participant-object-patient` (1)
- :ref:`audit-data-export-participant-object-submission-set` (1)

.. csv-table:: Event: Data Export
   :name: audit-data-export-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110106, DCM, 'Export')"
         "EventActionCode", "M", "Enumerated Value R = Read"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant: Archive application
   :name: audit-data-export-active-participant-user
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Secured archive : User name for secured version of archive"
         "", "", "Unsecured archive : Remote IP address for unsecured version of archive"
         "UserIDTypeCode", "U", "Secured archive : EV ("Cp1640-1","DCM","Local User ID")"
         "", "", "Unsecured archive : ("110182","DCM","Node ID")"
         "UserTypeCode", "U", "'Person' : '1'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Archive application
   :name: audit-data-export-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Triggered by scheduler : Semicolon separated Application Entity Titles of the device"
         "", "", "Triggered from UI : Invoked URL"
         "UserIDTypeCode", "U", "Triggered by scheduler : EV ("110118","DCM","Archive Device AE Titles")"
         "", "", "Triggered from UI : EV ("12", "RFC-3881", "URI")"
         "UserTypeCode", "U", "'System' : '5'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "Triggered by scheduler : 'true'"
         "", "", "Triggered by UI : 'false'"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Destination
   :name: audit-data-export-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "The URI configured in XDSI Exporter in archive configuration"
         "UserIDTypeCode", "U", "EV ("12", "RFC-3881", "URI")"
         "UserTypeCode", "U", "'System' : '5'"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address present in the URI configured in XDSI Exporter in archive configuration"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Patient
   :name: audit-data-export-participant-object-patient
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' : 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' : 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"

.. csv-table:: Participant Object Identification: Submission Set
   :name: audit-data-export-participant-object-submission-set
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "System generated UID created for the submission set"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectTypeCodeRole", "M", "'20' : 'Job'"
         "ParticipantObjectIDTypeCode", "M", "EV (urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd, IHE XDS Metadata, 'submission set classificationNode')"

Sample Message
--------------

.. include:: data-export.xml
   :code: xml