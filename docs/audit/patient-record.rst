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

.. csv-table:: Supported Entities in Patient Record Audit Message

    :ref:`event-identification-patient-record`
    :ref:`active-participant-initiator-patient-record`
    :ref:`active-participant-archive-patient-record`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-patient-patient-record`

.. csv-table:: Event: Patient Record
   :name: event-identification-patient-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110110, DCM, 'Patient Record')"
         "EventActionCode", "M", "Enumerated Value C = Create"
         "", "", "U = Update"
         "", "", "D = Delete"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant : Initiator
   :description: This active participant is not present when patient is deleted by the scheduler
   :name: active-participant-initiator-patient-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Sending Application and Facility'"
         "", "", "Triggered from UI : 'Remote IP address' or 'User name of logged in user'"
         "", "", "Triggered by object storage : 'Calling AE title in association'"
         "UserIDTypeCode", "U", "HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
         "", "", "Triggered from UI (secured archive) : EV (113871, DCM, 'Person ID')"
         "", "", "Triggered from UI (unsecured archive) : EV (110182, DCM, 'Node ID')"
         "", "", "Triggered by object storage : EV (110119, DCM, 'Station AE Title')"
         "UserTypeCode", "U", "Triggered from UI : 'Person' : '1'"
         "", "", "All other cases : 'Application' : '2'"
         "UserIsRequestor", "M", "true"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-patient-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Receiving Application and Facility'"
         "", "", "Triggered from UI : 'Request URI'"
         "", "", "Triggered by object storage : 'Called AE title in association'"
         "", "", "Triggered by scheduler : 'Archive device name'"
         "UserIDTypeCode", "U", "HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
         "", "", "Triggered from UI : EV (12, RFC-3881, 'URI')"
         "", "", "Triggered by object storage : EV (110119, DCM, 'Station AE Title')"
         "", "", "Triggered by scheduler : EV (113877, DCM, 'Device Name')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "Patient deletion triggered by scheduler : 'true'"
         "", "", "All other cases : 'false'"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-patient-record
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

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="C" EventDateTime="2017-08-08T14:57:08.813+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>

        <ActiveParticipant UserID="MESA_OF|XYZ_RADIOLOGY" UserTypeCode="2" UserIsRequestor="true" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="MESA_IM|XYZ_IMAGE_MANAGER" UserTypeCode="2" AlternativeUserID="16577" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="PID1^^^Site A&1.2.40.0.13.1.1.999.111.1111&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TEST^Name</ParticipantObjectName>
        </ParticipantObjectIdentification>

    </AuditMessage>