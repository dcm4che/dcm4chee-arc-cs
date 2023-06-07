Patient Record
==============

Trigger Events
--------------

This message is emitted by the archive whenever :

- Patient is created by UI / HL7 messages / object storage
- Patient record is updated by UI / HL7 message / PDQ Service
- Patient records are deleted by UI / scheduler
- One or more patients are merged by UI / HL7 messages
- HL7 messages (ADT/Order/ORU) accepted (= also not processed) or processed by archive
- HL7 messages (ADT/Order/ORU) forwarded by archive to external HL7 receivers
- Patient created / updated / merged / changePatientID on external archive
- Patient record updated by `Supplement Issuer of PatientID <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/PAM-RS/SupplementIssuerOfPatientID>`_ service.
- Patient record created / updated by `Change Patient associated to Study <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IOCM-RS/MoveStudyToPatient>`_ service.

Message Structure
-----------------

.. csv-table:: Entities in Patient Record Audit Message

    :ref:`event-identification-patient-record`
    :ref:`active-participant-initiator-patient-record`, Not present when patient is deleted by the scheduler
    :ref:`active-participant-archive-patient-record`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-patient-patient-record`

.. csv-table:: Event: Patient Record
   :name: event-identification-patient-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110110, DCM, 'Patient Record')"
   EventActionCode, M, "| Create : 'C'
   | Update : 'U'
   | Delete : 'D'"
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success : '0'
   | Minor failure : '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator : '4'

.. csv-table:: Active Participant : Initiator
   :name: active-participant-initiator-patient-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| HL7 messages : 'Sending Application and Facility'
   | Triggered from UI : 'Remote IP address' or 'User name of logged in user'
   | Triggered by object storage : 'Calling AE title in association'"
   UserIDTypeCode, U, "| HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI (secured archive) : EV (113871, DCM, 'Person ID')
   | Triggered from UI (unsecured archive) : EV (110182, DCM, 'Node ID')
   | Triggered by object storage : EV (110119, DCM, 'Station AE Title')"
   UserTypeCode, U, "| Triggered from UI : Person : '1'
   | All other cases : Application : '2'"
   UserIsRequestor, M, | true
   RoleIDCode, M, "| EV (110153, DCM, 'Source')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-patient-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| HL7 messages : 'Receiving Application and Facility'
   | Triggered from UI : 'Request URI'
   | Triggered by object storage : 'Called AE title in association'
   | Triggered by scheduler : 'Archive device name'"
   UserIDTypeCode, U, "| HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI : EV (12, RFC-3881, 'URI')
   | Triggered by object storage : EV (110119, DCM, 'Station AE Title')
   | Triggered by scheduler : EV (113877, DCM, 'Device Name')"
   UserTypeCode, U, | Application : '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, "| Patient deletion triggered by scheduler : 'true'
   | All other cases : 'false'"
   RoleIDCode, M, "| EV (110152, DCM, 'Destination')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-patient-record
   :widths: 30, 5, 65, 10
   :header: Field Name, Opt, Description, Note

   ParticipantObjectID, M, Patient ID or <none> if unknown,
   ParticipantObjectTypeCode, M, Person : '1',
   ParticipantObjectTypeCodeRole, M, Patient : '1',
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')",
   ParticipantObjectName, U, Patient Name,
   ParticipantObjectDataLifeCycle, U, Verification ⇒ '4', Present only for audits triggered by PDQ Service
   ParticipantObjectDetail, U, If Patient record created/updated/deleted by HL7 messages : 'type=HL7v2 Message value=<Base-64 encoded HL7 message>'
   ParticipantObjectDetail, U, If Patient record created/updated/deleted by HL7 messages : 'type=HL7v2 Message value=<Base-64 encoded HL7 response>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 message control ID>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 response message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 response message control ID>'


Sample Message
--------------

Patient created by HL7 ADT message

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2018-09-11T11:43:05.007+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" AlternativeUserID="9132" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MM2^^^JMS~MM2^^^JMS1&1.2.3&ISO~MM2^^^JMS2~MM2^^^&1.2.3.4.5.6.7&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0Mjg1Nnx8QURUXkEyOF5BRFRfQTA1fDIwMTYwNjAyMTQyODU2fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQyODU2DQpQSUR8fHxNRUU0LTU0Nzk4Xl5eTUVFNCYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjQuMS4yJklTT15QSXx8QmVyZ2VyXk9saXZlcl5eXl5eTHxTY2h1c3Rlcl5eXl5eXk18MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHxeUFJOXlBIfHx8fENBVHwxMTIyOV5eXklIRVBBTSYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjIuMi41JklTT15BTnx8fHx8fHx8fHx8fHxOW0NSXQ0KUFYxfHxO"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDE4MDkxMTExNDMwNC4yNzR8fEFDS15BMjheQUNLfDE2OTE3ODcwNTN8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQyODU2fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEyOA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDI4NTY="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEyOA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTY5MTc4NzA1Mw=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient created on study stored to archive using C-STORE

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2019-02-05T18:16:46+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record" />
          <EventOutcomeDescription>UNVERIFIED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="CR3" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>CRTHREE^PAUL</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

Patient created on study stored to archive using STOW-RS

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2019-02-05T18:20:00+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record" />
          <EventOutcomeDescription>UNVERIFIED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
       </ActiveParticipant>
       <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="4785133^^^UKL" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>Fengler^Klaus</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

Patient created using UI

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2019-02-05T18:07:26+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record" />
          <EventOutcomeDescription>UNVERIFIED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/patients/" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
       </ActiveParticipant>
       <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="P-00000001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
       </ParticipantObjectIdentification>
    </AuditMessage>