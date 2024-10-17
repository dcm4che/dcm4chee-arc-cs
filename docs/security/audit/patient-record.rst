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


Sample Messages
---------------

Patient Record audits on DICOM transactions
...........................................

Following sample messages show audits emitted on DICOM transactions.

Patient created on receive of studies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T13:03:17.930+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="37097" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="54321" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>HD11^SAMPLE IMAGES^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient created on receive of MPPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T12:54:01.908+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="37097" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="12345-HD11" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>OBSR^WITH MEAS^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Record audits on Incoming HL7 Messages
..............................................

Following sample messages show audits emitted on receive of HL7 messages. Audit messages for Patient Create / Update may be
emitted on receive of any of the following HL7 messages :

- ADT^A01
- ADT^A02
- ADT^A03
- ADT^A04
- ADT^A05
- ADT^A06
- ADT^A07
- ADT^A08
- ADT^A10
- ADT^A11
- ADT^A12
- ADT^A13
- ADT^A28
- ADT^A31
- ADT^A38
- ADT^A40
- ADT^A47

Patient created on receive of HL7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-01T18:43:54.254+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P1^^^SYS&amp;1.2.3&amp;ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxITDdTTkR8RENNNENIRUV8MjAxNjA2MDIxNDI4NTZ8fEFEVF5BMDFeQURUX0EwNXwyMDE2MDYwMjE0Mjg1NnxQfDIuNXx8fHx8fEFTQ0lJW0NSXQ0KRVZOfHwyMDE2MDYwMjE0Mjg1Ng0KUElEfHx8UDFeXl5TWVMmMS4yLjMmSVNPfHxCZXJnZXJeT2xpdmVyXl5eXl5MfFNjaHVzdGVyXl5eXl5eTXwxOTk0MTAyNXxNfHx8R2FzdGVpZ3dlZ15eSGFsbGVpbl5eNTQwMF5BVVR8fF5QUk5eUEh8fHx8Q0FUfDExMjI5Xl5eSUhFUEFNJjEuMy42LjEuNC4xLjEyNTU5LjExLjEuMi4yLjUmSVNPXkFOfHx8fHx8fHx8fHx8fE5bQ1JdDQpQVjF8fE4NCg=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDI4NTY="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfFBBTVNpbXVsYXRvcnxJSEV8MjAyNDA5MDExODQzNTMuNTQ1fHxBQ0teQTAxXkFDS3wxMDQxOTA5MDA5fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDU1TQXxBQXwyMDE2MDYwMjE0Mjg1Nnw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTA0MTkwOTAwOQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patients demographics updated on receive of HL7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-01T18:56:18.476+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1335^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>OBSR^WITH MEASss</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0MzM1M3x8QURUXkEzMV5BRFRfQTA1fDIwMTYwNjAyMTQzMzUzfFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQzMzUzDQpQSUR8fHxHRTEzMzVeXl5KTVN8fE9CU1JeV0lUSCBNRUFTc3N8U2NodXN0ZXJeXl5eXl5NfDE5OTQxMDI1fE18fHxHYXN0ZWlnd2VnXl5IYWxsZWluXl41NDAwXkFVVHx8XlBSTl5QSHx8fHxDQVR8MTEyMjleXl5JSEVQQU0mMS4zLjYuMS40LjEuMTI1NTkuMTEuMS4yLjIuNSZJU09eQU58fHx8fHx8fHx8fHx8TltDUl0NClBWMXx8Tg0K"/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEzMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDMzNTM="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMTE4NTYxOC40NTd8fEFDS15BMzFeQUNLfDMwMTc5Nzg2NXxQfDIuNXx8fHx8fEFTQ0lJW0NSXQ1NU0F8QUF8MjAxNjA2MDIxNDMzNTN8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEzMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MzAxNzk3ODY1"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patients identifier changed
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Applicable for ADT^A47 message.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-02T09:42:02.150+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4NEW-54798^^^MEE4&amp;1.2.3.4.5.6.7&amp;ISO^PI" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0MzcwNHx8QURUXkE0N15BRFRfQTMwfDIwMTYwNjAyMTQzNzA0fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpQSUR8fHxNRUU0TkVXLTU0Nzk4Xl5eTUVFNCYxLjIuMy40LjUuNi43JklTT15QSXx8QmVyZ2VyXk9saXZlcl5eXl5eTHxTY2h1c3Rlcl5eXl5eXk18MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHxeUFJOXlBIfHx8fENBVHwxMTIyOV5eXklIRVBBTSYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjIuMi41JklTT15BTnx8fHx8fHx8fHx8fHxOW0NSXQ0KTVJHfE1FRTRORVctNTQ3OTheXl5NRUU0fHx8fHx8QmVyZ2VyXk9saXZlcl5eXl5eTA0K"/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0Nw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDM3MDQ="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMjA5NDIwMi4wODN8fEFDS15BNDdeQUNLfDEzMjg3MjY5ODl8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQzNzA0fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0Nw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyODcyNjk4OQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-02T09:42:02.150+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4NEW-54798^^^MEE4" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0MzcwNHx8QURUXkE0N15BRFRfQTMwfDIwMTYwNjAyMTQzNzA0fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpQSUR8fHxNRUU0TkVXLTU0Nzk4Xl5eTUVFNCYxLjIuMy40LjUuNi43JklTT15QSXx8QmVyZ2VyXk9saXZlcl5eXl5eTHxTY2h1c3Rlcl5eXl5eXk18MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHxeUFJOXlBIfHx8fENBVHwxMTIyOV5eXklIRVBBTSYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjIuMi41JklTT15BTnx8fHx8fHx8fHx8fHxOW0NSXQ0KTVJHfE1FRTRORVctNTQ3OTheXl5NRUU0fHx8fHx8QmVyZ2VyXk9saXZlcl5eXl5eTA0K"/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0Nw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDM3MDQ="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMjA5NDIwMi4wODN8fEFDS15BNDdeQUNLfDEzMjg3MjY5ODl8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQzNzA0fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0Nw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyODcyNjk4OQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patients merged on receive of HL7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Applicable for ADT^A40 message.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-02T09:22:08.206+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4NEW-54798" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0NDMwOXx8QURUXkE0MF5BRFRfQTM5fDIwMTYwNjAyMTQ0MzA5fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQ0MzA5DQpQSUR8fHxNRUU0TkVXLTU0Nzk4fHxCZXJnZXJeT2xpdmVyXl5eXl5MfFNjaHVzdGVyXl5eXl5eTXwxOTk0MTAyNXxNfHx8R2FzdGVpZ3dlZ15eSGFsbGVpbl5eNTQwMF5BVVR8fF5QUk5eUEh8fHx8Q0FUfDExMjI5Xl5eSUhFUEFNJjEuMy42LjEuNC4xLjEyNTU5LjExLjEuMi4yLjUmSVNPXkFOfHx8fHx8fHx8fHx8fE5bQ1JdDQpNUkd8TUVFNE5FV3x8fHx8fEh1YmVyXkpvaGFubl5eXl5eTA0KUFYxfHxODQo="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDQzMDk="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMjA5MjIwNy43Mjh8fEFDS15BNDBeQUNLfDEzMjg3MjY5ODZ8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQ0MzA5fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyODcyNjk4Ng=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-02T09:22:08.206+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4NEW" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Huber^Johann^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0NDMwOXx8QURUXkE0MF5BRFRfQTM5fDIwMTYwNjAyMTQ0MzA5fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQ0MzA5DQpQSUR8fHxNRUU0TkVXLTU0Nzk4fHxCZXJnZXJeT2xpdmVyXl5eXl5MfFNjaHVzdGVyXl5eXl5eTXwxOTk0MTAyNXxNfHx8R2FzdGVpZ3dlZ15eSGFsbGVpbl5eNTQwMF5BVVR8fF5QUk5eUEh8fHx8Q0FUfDExMjI5Xl5eSUhFUEFNJjEuMy42LjEuNC4xLjEyNTU5LjExLjEuMi4yLjUmSVNPXkFOfHx8fHx8fHx8fHx8fE5bQ1JdDQpNUkd8TUVFNE5FV3x8fHx8fEh1YmVyXkpvaGFubl5eXl5eTA0KUFYxfHxODQo="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDQzMDk="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMjA5MjIwNy43Mjh8fEFDS15BNDBeQUNLfDEzMjg3MjY5ODZ8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQ0MzA5fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjecntObjectDetail type="MSH-10" value="MTMyODcyNjk4Ng=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patients merged on receive of HL7 - Error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable for ADT^A40 message

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-01T18:44:14.068+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>Missing patient identifier</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Hofer^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0NDMwOXx8QURUXkE0MF5BRFRfQTM5fDIwMTYwNjAyMTQ0MzA5fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQ0MzA5DQpQSUR8fHx8fEhvZmVyXk9saXZlcl5eXl5eTHxTY2h1c3Rlcl5eXl5eXk18MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHxeUFJOXlBIfHx8fENBVHwxMTIyOV5eXklIRVBBTSYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjIuMi41JklTT15BTnx8fHx8fHx8fHx8fHxOW0NSXQ0KTVJHfE1FRTQtNTQ3OTReXl5NRUU0JjEuMy42LjEuNC4xLjEyNTU5LjExLjEuNC4xLjImSVNPXlBJfHx8fHx8SHViZXJeSm9oYW5uXl5eXl5MW0NSXQ0KUFYxfHxODQo="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDQzMDk="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMTE4NDQxNC4wNjl8fEFDS15BNDBeQUNLfDEwNDE5MDkwMTF8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFFfDIwMTYwNjAyMTQ0MzA5fE1pc3NpbmcgcGF0aWVudCBpZGVudGlmaWVyDUVSUnx8UElEXjFeM3wxMDFeUmVxdWlyZWQgZmllbGQgbWlzc2luZ15ITDcwMzU3fEV8fHx8TWlzc2luZyBwYXRpZW50IGlkZW50aWZpZXI="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTA0MTkwOTAxMQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-01T18:44:14.068+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>Missing patient identifier</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4-54794^^^MEE4&amp;1.3.6.1.4.1.12559.11.1.4.1.2&amp;ISO^PI" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Huber^Johann^^^^^L[CR]</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxEQ000Q0hFRXxEQ000Q0hFRXwyMDE2MDYwMjE0NDMwOXx8QURUXkE0MF5BRFRfQTM5fDIwMTYwNjAyMTQ0MzA5fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQ0MzA5DQpQSUR8fHx8fEhvZmVyXk9saXZlcl5eXl5eTHxTY2h1c3Rlcl5eXl5eXk18MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHxeUFJOXlBIfHx8fENBVHwxMTIyOV5eXklIRVBBTSYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjIuMi41JklTT15BTnx8fHx8fHx8fHx8fHxOW0NSXQ0KTVJHfE1FRTQtNTQ3OTReXl5NRUU0JjEuMy42LjEuNC4xLjEyNTU5LjExLjEuNC4xLjImSVNPXlBJfHx8fHx8SHViZXJeSm9oYW5uXl5eXl5MW0NSXQ0KUFYxfHxODQo="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDQzMDk="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8UEFNU2ltdWxhdG9yfElIRXwyMDI0MDkwMTE4NDQxNC4wNjl8fEFDS15BNDBeQUNLfDEwNDE5MDkwMTF8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFFfDIwMTYwNjAyMTQ0MzA5fE1pc3NpbmcgcGF0aWVudCBpZGVudGlmaWVyDUVSUnx8UElEXjFeM3wxMDFeUmVxdWlyZWQgZmllbGQgbWlzc2luZ15ITDcwMzU3fEV8fHx8TWlzc2luZyBwYXRpZW50IGlkZW50aWZpZXI="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTA0MTkwOTAxMQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient READ on receive of HL7 Appointments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable for following HL7 messages :

- SIU^S12
- SIU^S13
- SIU^S15

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-09-01T18:58:02.822+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P11^^^SYS&amp;1.2.3&amp;ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Manuel^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8UEFNU2ltdWxhdG9yfElIRXxITDdTTkR8RENNNENIRUV8MjAxNjA2MDIxNDI4NTZ8fFNJVV5TMTJeU0lVX1MxMnwyMDE2MDYwMjE0Mjg1NnxQfDIuNXx8fHx8fEFTQ0lJW0NSXQ0KRVZOfHwyMDE2MDYwMjE0Mjg1Ng0KUElEfHx8UDExXl5eU1lTJjEuMi4zJklTT3x8TWFudWVsXk9saXZlcl5eXl5eTHxTY2h1c3Rlcl5eXl5eXk18MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHxeUFJOXlBIfHx8fENBVHwxMTIyOV5eXklIRVBBTSYxLjMuNi4xLjQuMS4xMjU1OS4xMS4xLjIuMi41JklTT15BTnx8fHx8fHx8fHx8fHxOW0NSXQ0KUFYxfHxODQo="/>
            <ParticipantObjectDetail type="MSH-9" value="U0lVXlMxMg=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDI4NTY="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfFBBTVNpbXVsYXRvcnxJSEV8MjAyNDA5MDExODU4MDIuODIyfHxBQ0teUzEyXkFDS3wzMDE3OTc4NjZ8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQyODU2fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXlMxMg=="/>
            <ParticipantObjectDetail type="MSH-10" value="MzAxNzk3ODY2"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Record audits on REST APIs invocation
.............................................

Following sample messages show audits emitted on invocation of REST APIs.

Patient Create
^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-01T11:55:36.260+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients" AlternativeUserID="34796" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">e
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P123^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>ANA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Create - On Study Stored
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Patient Update - Error
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-01T18:12:16.095+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>Patient[pk=12, id=[P888^^^JMS], name=P888Name] merged with Patient[pk=13, id=[P999^^^JMS], name=P999Name]</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients" AlternativeUserID="55041" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P888^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P888Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patients identifier changed
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-02T11:43:23.828+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/PID-NEW" AlternativeUserID="21064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="PID-NEW" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PID-NEW-Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-02T11:43:23.829+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/PID-NEW" AlternativeUserID="21064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="PID-OLD" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PID-OLD-Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patients Merged
^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-01T18:00:56.637+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P111%5E%5E%5EJMS?merge=true" AlternativeUserID="55041" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P222^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P222Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-01T18:00:56.637+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P111%5E%5E%5EJMS?merge=true" AlternativeUserID="55041" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P111^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P111Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Delete
^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-02T11:23:03.966+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P888%5E%5E%5EJMS" AlternativeUserID="21064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P888^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P888Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Delete on Delete Last Study
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of `Delete Study Permanently <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IOCM-RS/DeleteStudy>`_
and if `Delete Patient On Delete Last Study <https://dcm4chee-arc-cs.readthedocs.io/en/latest/networking/config/archiveDevice.html#dcmdeletepatientondeletelaststudy>`_ configuration is set to true.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-02T13:24:58.150+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.514.212.200" AlternativeUserID="35197" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE0514" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>WILKINS^CHARLES</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Create on imported MWL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of `Import matching Scheduled Procedure Steps from external MWL SCP <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MWL-RS/ImportMatchingSPS>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-02T14:02:15.030+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/dimse/CENTRAL/mwlitems/import/FOUNDA" AlternativeUserID="35197" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="CENTRAL" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="demo2.j4care.com" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="SMA001^^^SMA&amp;SM_EPI&amp;L" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Beckett^Noah</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Record audits on scheduler functions
............................................

Following sample messages show audits emitted on trigger of scheduler functions.

Patient Delete on Delete Last Study
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of studies deletion by purge storage scheduler and if `Delete Patient On Delete Last Study <https://dcm4chee-arc-cs.readthedocs.io/en/latest/networking/config/archiveDevice.html#dcmdeletepatientondeletelaststudy>`_ configuration is set to true.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-02T13:44:04.397+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="35197" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Create on imported MWL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of importing matching Scheduled Procedure Steps from external MWL SCP triggered by scheduler

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-02T13:55:57.243+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="35197" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="CENTRAL" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="demo2.j4care.com" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="HN-P3^^^HEALNET" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>DOE^JOHN</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Record audits on Patient Demographics Query
...................................................

Following sample messages show audits emitted on trigger of Patient Demographics Query from a patient demographics supplier.

DICOM PDQ Supplier
^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-02T11:57:16.399+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>NOT_FOUND</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P888New2/pdq/pdq-dicom" AlternativeUserID="21064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="pdq-dicom:CENTRAL" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="demo2.j4care.com" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectDetail type="PatientVerificationStatus" value="Tk9UX0ZPVU5E"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

FHIR PDQ Supplier
^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-02T12:14:16.383+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>NOT_FOUND</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P888New2/pdq/fhir-patient-source-hapi" AlternativeUserID="21064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="pdq-fhir:FHIR_HAPI" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectDetail type="PatientVerificationStatus" value="Tk9UX0ZPVU5E"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

HL7 PDQ Supplier
^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-02T12:24:39.083+02:00" EventOutcomeIndicator="8">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>VERIFICATION_FAILED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P888New2/pdq/HL7PatientDemographicsQuery-to-PatientDemographicsSupplier" AlternativeUserID="35197" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="pdq-hl7:HL7SND/DCM4CHEE:HL7RCV/DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectDetail type="PatientVerificationStatus" value="VkVSSUZJQ0FUSU9OX0ZBSUxFRA=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

HL7 PDQ Supplier - Triggered by Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-02T13:20:23.090+02:00" EventOutcomeIndicator="8">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
            <EventOutcomeDescription>VERIFICATION_FAILED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="35197" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="pdq-hl7:HL7SND/DCM4CHEE:HL7RCV/DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectDetail type="PatientVerificationStatus" value="VkVSSUZJQ0FUSU9OX0ZBSUxFRA=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Patient Record audits on Outgoing HL7 Messages
..............................................

Following sample messages show audits emitted on HL7 Messages sent from archive to external HL7 receivers.

HL7 Forwarding
^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-03T09:33:02.524+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P1^^^SYS&amp;1.2.3&amp;ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDE2MDYwMjE0Mjg1Nnx8QURUXkEwMV5BRFRfQTA1fDIwMTYwNjAyMTQyODU2fFB8Mi41fHx8fHx8QVNDSUlbQ1JdDQpFVk58fDIwMTYwNjAyMTQyODU2DQpQSUR8fHxQMV5eXlNZUyYxLjIuMyZJU098fEJlcmdlcl5PbGl2ZXJeXl5eXkx8U2NodXN0ZXJeXl5eXl5NfDE5OTQxMDI1fE18fHxHYXN0ZWlnd2VnXl5IYWxsZWluXl41NDAwXkFVVHx8XlBSTl5QSHx8fHxDQVR8MTEyMjleXl5JSEVQQU0mMS4zLjYuMS40LjEuMTI1NTkuMTEuMS4yLjIuNSZJU09eQU58fHx8fHx8fHx8fHx8TltDUl0NClBWMXx8Tg0K"/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDI4NTY="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzA5MzMwMi40OTB8fEFDS15BMDFeQUNLfDE5MDc0MTQwMzl8UHwyLjV8fHx8fHxBU0NJSVtDUl0NTVNBfEFBfDIwMTYwNjAyMTQyODU2fA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTkwNzQxNDAzOQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

HL7 Forwarding - Merge
^^^^^^^^^^^^^^^^^^^^^^

Applicable similarly for Change Patient Identifier.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-03T14:50:51.765+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4NEW-54798" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8SEw3UkNWfERDTTRDSEVFfDIwMTYwNjAyMTQ0MzA5fHxBRFReQTQwXkFEVF9BMzl8MjAxNjA2MDIxNDQzMDl8UHwyLjV8fHx8fHxBU0NJSVtDUl0NCkVWTnx8MjAxNjA2MDIxNDQzMDkNClBJRHx8fE1FRTRORVctNTQ3OTh8fEJlcmdlcl5PbGl2ZXJeXl5eXkx8U2NodXN0ZXJeXl5eXl5NfDE5OTQxMDI1fE18fHxHYXN0ZWlnd2VnXl5IYWxsZWluXl41NDAwXkFVVHx8XlBSTl5QSHx8fHxDQVR8MTEyMjleXl5JSEVQQU0mMS4zLjYuMS40LjEuMTI1NTkuMTEuMS4yLjIuNSZJU09eQU58fHx8fHx8fHx8fHx8TltDUl0NCk1SR3xNRUU0TkVXfHx8fHx8SHViZXJeSm9oYW5uXl5eXl5MDQpQVjF8fE4NCg=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDQzMDk="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfERDTTRDSEVFfERDTTRDSEVFfDIwMjQwOTAzMTQ1MDUxLjczMHx8QUNLXkE0MF5BQ0t8MzA3OTk4OTYxfFB8Mi41fHx8fHx8QVNDSUlbQ1JdDU1TQXxBQXwyMDE2MDYwMjE0NDMwOXw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MzA3OTk4OTYx"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-03T14:50:51.766+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MEE4NEW" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Huber^Johann^^^^^L</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8RENNNENIRUV8RENNNENIRUV8SEw3UkNWfERDTTRDSEVFfDIwMTYwNjAyMTQ0MzA5fHxBRFReQTQwXkFEVF9BMzl8MjAxNjA2MDIxNDQzMDl8UHwyLjV8fHx8fHxBU0NJSVtDUl0NCkVWTnx8MjAxNjA2MDIxNDQzMDkNClBJRHx8fE1FRTRORVctNTQ3OTh8fEJlcmdlcl5PbGl2ZXJeXl5eXkx8U2NodXN0ZXJeXl5eXl5NfDE5OTQxMDI1fE18fHxHYXN0ZWlnd2VnXl5IYWxsZWluXl41NDAwXkFVVHx8XlBSTl5QSHx8fHxDQVR8MTEyMjleXl5JSEVQQU0mMS4zLjYuMS40LjEuMTI1NTkuMTEuMS4yLjIuNSZJU09eQU58fHx8fHx8fHx8fHx8TltDUl0NCk1SR3xNRUU0TkVXfHx8fHx8SHViZXJeSm9oYW5uXl5eXl5MDQpQVjF8fE4NCg=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjAxNjA2MDIxNDQzMDk="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfERDTTRDSEVFfERDTTRDSEVFfDIwMjQwOTAzMTQ1MDUxLjczMHx8QUNLXkE0MF5BQ0t8MzA3OTk4OTYxfFB8Mi41fHx8fHx8QVNDSUlbQ1JdDU1TQXxBQXwyMDE2MDYwMjE0NDMwOXw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MzA3OTk4OTYx"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on PAM-RS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T10:08:53.247+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients" AlternativeUserID="6365" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P888^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P888Name^^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzEwMDg1My4xMDN8fEFEVF5BMjheQURUX0EwNXwxNjE4ODk5NDQ4fFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA4ODheXl5KTVN8fFA4ODhOYW1lXl5eXl58fDE5NjcxMjEyfEZ8fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwN"/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEyOA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTYxODg5OTQ0OA=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzEwMDg1My4xNjJ8fEFDS15BMjheQUNLfDMwMDA0OTk4MHxQfDIuNS4xfHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTYxODg5OTQ0OHw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEyOA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MzAwMDQ5OTgw"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on PAM-RS - Merge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable similarly for Change Patient Identifier.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-03T11:29:48.481+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P666%5E%5E%5EJMS?merge=true" AlternativeUserID="18887" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P777^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P777Name^^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzExMjk0OC40NDB8fEFEVF5BNDBeQURUX0EzOXwxMzIzNzQwNjQyfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA3NzdeXl5KTVN8fFA3NzdOYW1lXl5eXl58fHx8fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwNTVJHfFA2NjZeXl5KTVN8fHx8fHxQNjY2TmFtZV5eXl5eDQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyMzc0MDY0Mg=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzExMjk0OC40ODB8fEFDS15BNDBeQUNLfDYyODg4MTYzM3xQfDIuNS4xfHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTMyMzc0MDY0Mnw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="NjI4ODgxNjMz"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-03T11:29:48.481+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients/P666%5E%5E%5EJMS?merge=true" AlternativeUserID="18887" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P666^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P666Name^^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzExMjk0OC40NDB8fEFEVF5BNDBeQURUX0EzOXwxMzIzNzQwNjQyfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA3NzdeXl5KTVN8fFA3NzdOYW1lXl5eXl58fHx8fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwNTVJHfFA2NjZeXl5KTVN8fHx8fHxQNjY2TmFtZV5eXl5eDQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyMzc0MDY0Mg=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzExMjk0OC40ODB8fEFDS15BNDBeQUNLfDYyODg4MTYzM3xQfDIuNS4xfHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTMyMzc0MDY0Mnw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="NjI4ODgxNjMz"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Create Patient In External Archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T12:22:01.743+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/hl7apps/HL7SND%7CDCM4CHEE/hl7/HL7RCV%7CDCM4CHEE/patients" AlternativeUserID="18887" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P888^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P888Name^^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzEyMjIwMS42ODh8fEFEVF5BMjheQURUX0EwNXwxMzIzNzQwNjUxfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA4ODheXl5KTVN8fFA4ODhOYW1lXl5eXl58fDE5NjcxMjEyfEZ8fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwN"/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEyOA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyMzc0MDY1MQ=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzEyMjIwMS42OTh8fEFDS15BMjheQUNLfDIwNTY3Mjk0Mjl8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDEzMjM3NDA2NTF8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEyOA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjA1NjcyOTQyOQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Update Patient In External Archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-03T12:28:25.279+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/hl7apps/HL7SND%7CDCM4CHEE/hl7/HL7RCV%7CDCM4CHEE/patients/P888%5E%5E%5EJMS" AlternativeUserID="18887" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P888^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P888Name2^^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzEyMjgyNS4yNzN8fEFEVF5BMzFeQURUX0EwNXwxMzIzNzQwNjUzfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA4ODheXl5KTVN8fFA4ODhOYW1lMl5eXl5efHwxOTY3MTIxMnxGfHx8fHx8fF5efHx8fHx8fHx8fHx8fHx8fHx8fHx8DQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkEzMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyMzc0MDY1Mw=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzEyMjgyNS4yNzh8fEFDS15BMzFeQUNLfDIwNTY3Mjk0MzF8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDEzMjM3NDA2NTN8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkEzMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjA1NjcyOTQzMQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Merge Patients In External Archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-03T12:44:34.381+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/hl7apps/HL7SND%7CDCM4CHEE/hl7/HL7RCV%7CDCM4CHEE/patients/P8889%5E%5E%5EJMS/merge" AlternativeUserID="18887" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P888^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>P888Name^^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzEyNDQzNC4zNzJ8fEFEVF5BNDBeQURUX0EzOXwxMzIzNzQwNjU2fFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA4ODheXl5KTVN8fFA4ODhOYW1lXl5eXl58fDE5NjcxMjEyfEZ8fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwNTVJHfFA4ODg5Xl5eSk1TfHx8fHx8DQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyMzc0MDY1Ng=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzEyNDQzNC4zNzZ8fEFDS15BNDBeQUNLfDIwNTY3Mjk0MzR8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDEzMjM3NDA2NTZ8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjA1NjcyOTQzNA=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-03T12:44:34.382+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/hl7apps/HL7SND%7CDCM4CHEE/hl7/HL7RCV%7CDCM4CHEE/patients/P8889%5E%5E%5EJMS/merge" AlternativeUserID="18887" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P8889^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzEyNDQzNC4zNzJ8fEFEVF5BNDBeQURUX0EzOXwxMzIzNzQwNjU2fFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFA4ODheXl5KTVN8fFA4ODhOYW1lXl5eXl58fDE5NjcxMjEyfEZ8fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwNTVJHfFA4ODg5Xl5eSk1TfHx8fHx8DQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="QURUXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMyMzc0MDY1Ng=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzEyNDQzNC4zNzZ8fEFDS15BNDBeQUNLfDIwNTY3Mjk0MzR8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDEzMjM3NDA2NTZ8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXkE0MA=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjA1NjcyOTQzNA=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of MPPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T14:21:02.354+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="12345-HD11" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>OBSR^WITH MEAS^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzE0MjEwMi4yNTh8fE9SVV5SMDFeT1JVX1IwMXwxNjM5OTQ0MTYxfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fDEyMzQ1LUhEMTF8fE9CU1JeV0lUSCBNRUFTXl5eXnx8MTk4NjA1MDZ8Rnx8fHx8fHxeXnx8fHx8fHx8fHx8fHx8fHx8fHx8fA1QVjF8fFV8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8Vg1PUkN8U0N8NDIxMEMyQTN8NDIxMEMyQTN8fElQDU9CUnx8NDIxMEMyQTN8NDIxMEMyQTN8fHx8MjAwNTEyMDUxNjQxNTIuMDAwMDAwfHx8fHx8fHx8fHw0MjEwQzJBM3w0MjEwQzJBM3x8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8fHx8fHx8fHx8fHx8DVRRMXx8fHx8fHwyMDA1MTIwNTE2NDE1Mi4wMDAwMDB8fFJeUm91dGluZV5ITDcwMDc4DUlQQ3xPQiBTUiBFWEFNfHwxLjIuODQwLjExMzU0My42LjYuNC4xLjYxNTY3MTg3MTEzMTMxMTEwOTYyMjExNTgyNzkxNTEyMTgzOTI5Mjg4fHxVU3x8fHxNUFBTU0NVDQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="T1JVXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTYzOTk0NDE2MQ=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzE0MjEwMi4zMTN8fEFDS15SMDFeQUNLfDEzMTk5MTA5Nzl8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDE2Mzk5NDQxNjF8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMxOTkxMDk3OQ=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of Study - Triggered by HL7 Procedure Status Update Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T13:48:10.858+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzEzNDcxMy41MTR8fE9SVV5SMDFeT1JVX1IwMXwxNjM5OTQ0MTU3fFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fE1HSUQwMDF8fE1BTU1PR1JBUEhZXlRFU1QxXl5eXnx8MTk1MDAxMDJ8Rnx8fHx8fHxeXnx8fHx8fHx8fHx8fHx8fHx8fHx8fA1QVjF8fFV8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8Vg1PUkN8U0N8MDAwMEJEQjR8MDAwMEJEQjR8fENNDU9CUnx8MDAwMEJEQjR8MDAwMEJEQjR8fHx8MjAwMjA0MjYxMjAwfHx8fHx8fHx8fHwwMDAwQkRCNHwwMDAwQkRCNHx8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8fHx8fHx8fHx8fHx8DVRRMXx8fHx8fHwyMDI0MDkwMzEzNDcxMy41MTR8fFJeUm91dGluZV5ITDcwMDc4DUlQQ3xBQ0NFU1NJT04wMXx8MS4xfHxNR3x8fHwN"/>
            <ParticipantObjectDetail type="MSH-9" value="T1JVXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTYzOTk0NDE1Nw=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzEzNDgxMC44MTN8fEFDS15SMDFeQUNLfDk0NTY4NDgyM3xQfDIuNS4xfHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTYzOTk0NDE1N3w="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="OTQ1Njg0ODIz"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of Study - Using DCM2HL7Exporter triggered by REST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T14:26:32.243+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113619.2.216.2.1.2642006103252234.10589/export/DcM2HL7PSU-Exporter" AlternativeUserID="37097" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MADTPID3597" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>VENTRI^TEST^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzE0MjYzMi4xMjh8fE9SVV5SMDFeT1JVX1IwMXwxNjM5OTQ0MTYyfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fE1BRFRQSUQzNTk3fHxWRU5UUkleVEVTVF5eXl58fDE5NzYwMjA1fE18fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwNUFYxfHxVfHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fFYNT1JDfFNDfEREM0IwMkE5fEREM0IwMkE5fHxDTQ1PQlJ8fEREM0IwMkE5fEREM0IwMkE5fHx8fDIwMDYwNDI2MTIzMjUyfHx8fHx8fHx8fHxERDNCMDJBOXxERDNCMDJBOXx8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8fHx8fHx8fHx8fHx8DVRRMXx8fHx8fHwyMDI0MDkwMzE0MjYzMi4xMjh8fFJeUm91dGluZV5ITDcwMDc4DU9CWHwxfFNUfDExMzAxNF5ESUNPTSBTdHVkeV5EQ018fDEuMi44NDAuMTEzNjE5LjIuMjE2LjIuMS4yNjQyMDA2MTAzMjUyMjM0LjEwNTg5fHx8fHx8T3x8fDIwMDYwNDI2MTIzMjUyfHx8fHx8fHx8fA1PQlh8MnxTVHxeU2VyaWVzIEluc3RhbmNlIFVJRHx8MS4yLjg0MC4xMTM2MTkuMi4yMTYuMi4xLjI2NDIwMDYxMDM0MzYyODEuMTA3MTZ8fHx8fHxGfHx8fHx8fHx8fHx8SW5zdGl0dXRpb24gbmFtZXxJbnN0aXR1dGlvbiBhZGRyZXNzDU9CWHwzfFNUfF5TT1AgSW5zdGFuY2UgVUlEfHwxLjIuODQwLjExMzYxOS4yLjIxNi4yLjEuMjY0MjAwNjEwMzQzNDk2OC4xMDk0Mnx8fHx8fEZ8fHwyMDA2MDQyNjEyMzQ0N3x8fHx8fHx8fHwNT0JYfDR8U1R8XlNPUCBDbGFzcyBVSUR8fDEuMi44NDAuMTAwMDguNS4xLjQuMS4xLjIwfHx8fHx8Rnx8fHx8fHx8fHx8fHwNT0JYfDV8Q0V8Xl4NT0JYfDZ8U1R8NTk3NzYtNV5Qcm9jZWR1cmUgRmluZGluZ3NeTE58fFN0dWR5IERlc2NyaXB0aW9uIDogRmFjdG9yeVxUXENhcmRpb2xvZ3lcVFxEdWFsIElzb3RvcGUNT0JYfDd8U1R8NTk3NzYtNV5Qcm9jZWR1cmUgRmluZGluZ3NeTE58fFNlcmllcyBEZXNjcmlwdGlvbiA6IFJFU1QN"/>
            <ParticipantObjectDetail type="MSH-9" value="T1JVXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTYzOTk0NDE2Mg=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzE0MjYzMi4xNTV8fEFDS15SMDFeQUNLfDcxNTk4OTI0fFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DU1TQXxBQXwxNjM5OTQ0MTYyfA=="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="NzE1OTg5MjQ="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of Study - Using DCM2HL7Exporter triggered by Export Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-03T14:34:10.877+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110110" codeSystemName="DCM" originalText="Patient Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="PID1123^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver^^^^</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkwMzE0MzQxMC44Mjl8fE9SVV5SMDFeT1JVX1IwMXwxNjM5OTQ0MTY1fFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fFBJRDExMjNeXl5KTVN8fEJlcmdlcl5PbGl2ZXJeXl5efFNjaHVzdGVyXl5eXl58MTk5NDEwMjV8TXx8fEdhc3RlaWd3ZWdeXkhhbGxlaW5eXjU0MDBeQVVUfHx8fF5efHx8fHx8fHx8fHx8Xkdhc3RlaWd3ZWdcU1xcU1xIYWxsZWluXFNcXFNcNTQwMFxTXEFVVHx8fHx8fHx8fA1QVjF8fFV8fHx8fHx8fHx8fHx8fHx8fDAwNjM2MTIwNDEyNTY5NDY2ODk4fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHxWDU9SQ3xTQ3xIQ0lTMjAyNDE0MzUyNnxFODY5OTU0Rnx8Q00NT0JSfHxIQ0lTMjAyNDE0MzUyNnxFODY5OTU0Rnx8fHwyMDI0MDQxMjA4NDYzNXx8fHx8fHx8fHx8QUNDMXxFODY5OTU0Rnx8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8fHx8fHx8fHx8fHx8DVRRMXx8fHx8fHwyMDI0MDkwMzE0MzQxMC44Mjl8fFJeUm91dGluZV5ITDcwMDc4DU9CWHwxfFNUfDExMzAxNF5ESUNPTSBTdHVkeV5EQ018fDEuMi42MjAuMzc4NzMuMS4yLjg0MC4xMTM1NDMuNi42LjQuMS42MTU2NzE4NzExMzEzMTExMDk2MjIxMTU4Mjc5MTUuMS4xfHx8fHx8T3x8fHx8fHx8fHx8fHwNT0JYfDJ8U1R8XlNlcmllcyBJbnN0YW5jZSBVSUR8fDEuMi44NDAuMTEzNTQzLjYuNi40LjEuNjE1NjcxODcxMTMxMzExMTA5NjIyMTE1ODI3OTE1LjEuMS4zODk5MjMzNjE1fHx8fHx8Rnx8fHx8fHx8fHx8fENVRiBFQVNUX1JBRElPTE9HWXwNT0JYfDN8U1R8XlNPUCBJbnN0YW5jZSBVSUR8fDEuMi44NDAuMTEzNTQzLjYuNi40LjEuNjE1NjcxODcxMTMxMzExMTA5NjIyMTE1ODI3OTE1LjEuMS40LjM4OTkyMzM2MTV8fHx8fHxGfHx8MjAyNDA0MTIwODQ2MzV8fHx8fHx8fHx8DU9CWHw0fFNUfF5TT1AgQ2xhc3MgVUlEfHwxLjIuODQwLjEwMDA4LjUuMS40LjEuMS4xMDQuMXx8fHx8fEZ8fHx8fHx8fHx8fHx8DU9CWHw1fENFfDE4NzQ4LTReU1IgSW5zdGFuY2UgVUlEXkxODU9CWHw2fFNUfDU5Nzc2LTVeUHJvY2VkdXJlIEZpbmRpbmdzXkxOfHxTZXJpZXMgRGVzY3JpcHRpb24gOiBBRE1JTklTVFJBVElWT1NfUFJFU0NSSUNBT19QcmVzY3Jpw6fDtWVzDQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="T1JVXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTYzOTk0NDE2NQ=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkwMzE0MzQxMC44NDN8fEFDS15SMDFeQUNLfDEwNjk4NzYxODh8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDE2Mzk5NDQxNjV8"/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXlIwMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTA2OTg3NjE4OA=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>