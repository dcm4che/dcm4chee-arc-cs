Patient Record
==============

Trigger Events
--------------

This message is emitted by the archive whenever :

- Patient is created by UI or by HL7 messages or by object storage.
- Patient record is updated by UI or by HL7 message.
- Patient records are deleted by UI or by scheduler.
- One or more patients are merged by UI or by HL7 messages.

Message Structure
-----------------

- :ref:`audit-patient-record-event`
- :ref:`audit-patient-record-active-participant-source` (1) - This active participant is not present when patient is deleted by the scheduler
- :ref:`audit-patient-record-active-participant-destination` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-patient-record-participant-object-patient` (1)

.. csv-table:: Event: Patient Record
   :name: audit-patient-record-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110110, DCM, 'Patient Record')"
         "EventActionCode", "M", "Enumerated Value C = Create"
         "", "", "U = Update"
         "", "", "D = Delete"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant: Source
   :name: audit-patient-record-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Sending Application and Facility'"
         "", "", "Triggered from UI : 'Remote IP address' or 'User name of logged in user'"
         "", "", "Triggered by object storage : 'Calling AE title in association'"
         "UserIDTypeCode", "U", "HL7 messages : EV ("HL7APP","99DCM4CHEE","Application and Facility")"
         "", "", "Triggered from UI (secured archive) : EV ("113871","DCM","Person ID")"
         "", "", "Triggered from UI (unsecured archive) : EV ("110182","DCM","Node ID")"
         "", "", "Triggered by object storage : EV ("110119","DCM","Station AE Title")"
         "UserTypeCode", "U", "Triggered from UI : 'Person' : '1'"
         "", "", "All other cases : 'Application' : '2'"
         "UserIsRequestor", "M", "true"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Archive application
   :name: audit-patient-record-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Receiving Application and Facility'"
         "", "", "Triggered from UI : 'Request URI'"
         "", "", "Triggered by object storage : 'Called AE title in association'"
         "", "", "Triggered by scheduler : 'Archive device name'"
         "UserIDTypeCode", "U", "HL7 messages : EV ("HL7APP","99DCM4CHEE","Application and Facility")"
         "", "", "Triggered from UI : EV ("12", "RFC-3881", "URI")"
         "", "", "Triggered by object storage : EV ("110119","DCM","Station AE Title")"
         "", "", "Triggered by scheduler : EV ("113877","DCM","Device Name")"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "Patient deletion triggered by scheduler : 'true'"
         "", "", "All other cases : 'false'"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Patient
   :name: audit-patient-record-participant-object-patient
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' : 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' : 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"
         "ParticipantObjectDetail", "U", "Base-64 encoded HL7 message type if Patient record was created/updated/deleted by HL7 messages."


Sample Message
--------------

.. include:: patient-record.xml
   :code: xml