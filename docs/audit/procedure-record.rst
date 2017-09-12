Procedure Record
================

Trigger Events
--------------

This message is emitted by the archive whenever :

- Modality worklist entry is created by UI or by HL7 messages.
- Modality worklist entry is updated by UI or by HL7 message or by incoming MPPS.
- Modality worklist entry is deleted by UI.
- Study attributes are updated from UI.
- Expiration date is set to study/series from UI.

Message Structure
-----------------

- :ref:`audit-procedure-record-event`
- :ref:`audit-procedure-record-active-participant-source` (1)
- :ref:`audit-procedure-record-active-participant-destination` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-procedure-record-participant-object-study` (1)
- :ref:`audit-procedure-record-participant-object-patient` (1)

.. csv-table:: Event: Procedure Record
   :name: audit-procedure-record-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110111, DCM, 'Procedure Record')"
         "EventActionCode", "M", "Enumerated Value C = Create"
         "", "", "U = Update"
         "", "", "D = Delete"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant: Source
   :name: audit-procedure-record-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Sending Application and Facility'"
         "", "", "Triggered from UI : 'Remote IP address' or 'User name of logged in user'"
         "", "", "Triggered by MPPS : 'Calling AE title in association'"
         "UserIDTypeCode", "U", "HL7 messages : EV ("110116","DCM","Application and Facility")"
         "", "", "Triggered from UI (secured archive) : EV ("Cp1640-1","DCM","Local User ID")"
         "", "", "Triggered from UI (unsecured archive) : EV ("110182","DCM","Node ID")"
         "", "", "Triggered by MPPS : EV ("110119","DCM","Station AE Title")"
         "UserTypeCode", "U", "HL7 messages : 'Organization' : '3'"
         "", "", "Triggered from UI : 'Person' : '1'"
         "", "", "Triggered by MPPS : 'System' : '5'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Archive application
   :name: audit-procedure-record-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Receiving Application and Facility'"
         "", "", "Triggered from UI : 'Request URI'"
         "", "", "Triggered by MPPS : 'Called AE title in association'"
         "UserIDTypeCode", "U", "HL7 messages : EV ("110116","DCM","Application and Facility")"
         "", "", "Triggered from UI : EV ("12", "RFC-3881", "URI")"
         "", "", "Triggered by MPPS : EV ("110118","DCM","Archive Device AE Titles")"
         "UserTypeCode", "U", "HL7 messages : 'Organization' : '3'"
         "", "", "All other cases : 'System' : '5'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Study
   :name: audit-procedure-record-participant-object-study
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Study Instance UID"
         "ParticipantObjectTypeCode", "M", "'2' : 'System'"
         "ParticipantObjectTypeCodeRole", "M", "'3' : 'Report'"
         "ParticipantObjectIDTypeCode", "M", "EV (110180, DCM, 'Study Instance UID')"
         "ParticipantObjectDetail", "U", "Base-64 encoded study date if Study has StudyDate(0008,0020) attribute"
         "ParticipantObjectDescription", "U"
         "SOPClass", "MC", "Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>"
         "Accession", "U", "Accession Number"
         "ParticipantObjectContainsStudy", "U"
         "StudyIDs", "M", "Study Instance UID"

.. csv-table:: Participant Object Identification: Patient
   :name: audit-procedure-record-participant-object-patient
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

.. include:: procedure-record.xml
   :code: xml