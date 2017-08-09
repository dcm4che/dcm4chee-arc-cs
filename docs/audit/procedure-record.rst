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

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="C" EventDateTime="2017-08-08T14:57:08.989+02:00" EventOutcomeIndicator="0">

            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>

        </EventIdentification>

        <ActiveParticipant UserID="MESA_OF|XYZ_RADIOLOGY" UserIsRequestor="true" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1" />

        <ActiveParticipant UserID="MESA_IM|XYZ_IMAGE_MANAGER" AlternativeUserID="16577" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1" />

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">

            <AuditSourceTypeCode csd-code="4"/>

        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.199402091242.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">

            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>

            <ParticipantObjectDescription>

                <Accession Number="$ACCESSION_NUMBER$"/>

                <ParticipantObjectContainsStudy>

                    <StudyIDs UID="1.2.392.200036.9125.0.199402091242.1"/>

                </ParticipantObjectContainsStudy>

            </ParticipantObjectDescription>

        </ParticipantObjectIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="PID1^^^Site A&1.2.40.0.13.1.1.999.111.1111&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">

            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>

            <ParticipantObjectName>TEST^Name</ParticipantObjectName>

        </ParticipantObjectIdentification>

    </AuditMessage>