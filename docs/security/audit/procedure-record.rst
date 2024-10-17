Procedure Record
================

Trigger Events
--------------

This message is emitted by the archive whenever :

- Modality worklist entry is created by UI / HL7 Order messages
- Modality worklist entry is updated by UI / HL7 Order messages / incoming MPPS
- Modality worklist entry is deleted by UI
- MPPS received by archive
- MPPS forwarded by archive to external MPPS SCP
- HL7 messages forwarded by archive to external HL7 receivers
- HL7 Order messages accepted (= also not processed) by archive
- Link Instances with MWL Entry using UI
- SPS Status of MWL items of a patient changed from SCHEDULED to ARRIVED on receive of Patient Arrival (ADT^A10) HL7 message.

Message Structure
-----------------

.. csv-table:: Entities in Procedure Record Audit Message

    :ref:`event-identification-procedure-record`
    :ref:`active-participant-initiator-procedure-record`
    :ref:`active-participant-archive-procedure-record`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-procedure-record`
    :ref:`participant-object-patient-procedure-record`

.. csv-table:: Event Identification
   :name: event-identification-procedure-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110111, DCM, 'Procedure Record')"
   EventActionCode, M, "| Create ⇒ 'C'
   | Update ⇒ 'U'
   | Delete ⇒ 'D'"
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'

.. csv-table:: Active Participant : Source
   :name: active-participant-initiator-procedure-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| HL7 messages ⇒ 'Sending Application and Facility'
   | Triggered from UI ⇒ 'Remote IP address' or 'User name of logged in user'
   | Triggered by MPPS ⇒ 'Calling AE title in association'"
   UserIDTypeCode, U, "| HL7 messages ⇒ EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI (secured archive) ⇒ EV (113871, DCM, 'Person ID')
   | Triggered from UI (unsecured archive) ⇒ EV (110182, DCM, 'Node ID')
   | Triggered by MPPS ⇒ EV (110119, DCM, 'Station AE Title')"
   UserTypeCode, U, "| Triggered from UI : Person ⇒ '1'
   | All other cases : Application ⇒ '2'"
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-procedure-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| HL7 messages ⇒ 'Receiving Application and Facility'
   | Triggered from UI ⇒ 'Request URI'
   | Triggered by MPPS ⇒ 'Called AE title in association'"
   UserIDTypeCode, U, "| HL7 messages ⇒ EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI ⇒ EV (12, RFC-3881, 'URI')
   | Triggered by MPPS ⇒ EV (110119, DCM, 'Station AE Title')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification : Study
   :name: participant-object-study-procedure-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Study Instance UID or 1.2.40.0.13.1.15.110.3.165.1 if unknown
   ParticipantObjectTypeCode, M, System ⇒ '2'
   ParticipantObjectTypeCodeRole, M, Report ⇒ '3'
   ParticipantObjectIDTypeCode, M, "EV (110180, DCM, 'Study Instance UID')"
   ParticipantObjectDetail, U, "Base-64 encoded study date if Study has StudyDate(0008,0020) attribute"
   ParticipantObjectDetail, U, If Procedure record created/updated by HL7 messages : 'type=HL7v2 value=<Base-64 encoded HL7 message>'
   ParticipantObjectDetail, U, If Procedure record created/updated by HL7 messages : 'type=HL7v2 value=<Base-64 encoded HL7 response>'
   ParticipantObjectDescription, U
   SOPClass, MC, Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>
   Accession, U, Accession Number

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-procedure-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown
   ParticipantObjectTypeCode, M, Person ⇒ '1'
   ParticipantObjectTypeCodeRole, M, Patient ⇒ '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name

Sample Message
--------------

Procedure Record audits on DICOM transactions
.............................................

Following sample messages show audits emitted on DICOM transactions.

MWL's SPS Status Update on MPPS receive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T12:16:12.769+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
            <EventOutcomeDescription>STARTED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <MPPS UID="2.25.82722780936432637174672388918254928984"/>
                <Accession Number="ACCESSION01"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T12:16:12.817+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
            <EventOutcomeDescription>COMPLETED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <MPPS UID="2.25.82722780936432637174672388918254928984"/>
                <Accession Number="ACCESSION01"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Procedure Record audits on Incoming HL7 Messages
................................................

Following sample messages show audits emitted on receive of HL7 messages. Audit messages for Procedure Create / Update may be
emitted on receive of any of the following HL7 messages :

- ORM^O01
- OMG^O19
- OMI^O23

Procedure created on receive of HL7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-18T15:07:18.581+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="MESA_OF|XYZ_RADIOLOGY" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND2|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.40.0.13.1.15.110.3.165.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8TUVTQV9PRnxYWVpfUkFESU9MT0dZfEhMN1NORDJ8RENNNENIRUV8MjAwMDEyMTIwMTAxMDF8fE9NSV5PMjN8MTAwMTEyfFB8Mi41LjF8fHx8fHwgfHwNUElEfHx8TTQwMDBeXl5BRFQyfHxRVVxSXEVFTl5NQVJUXFJcSEF8fDE5NDUwODA0fE18fFdIfDgyMCBKT1JJRSBCTFZEXl5DSElDQUdPXklMXjYwNTIzfHx8fHx8fDIwLTk4LTQwMDB8fHx8fHx8fHx8fHx8fHx8fHx8fHwNUFYxfHxFfEVEfHx8fDEyMzReV0VBVkVSXlRJTU9USFleUF5eRFJ8NTEwMV5ORUxMXkZSRURFUklDS15QXl5EUnx8SFNSfHx8fHxBU3x8MDAwMF5BZG1pdHRpbmdeRG9jdG9yXlBeXkRSfHxWMTAwXl5eQURUMXx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHwyMDAwMDgyMDExMDB8fHx8fHx8VnwNUk9MfDEuMi4zLjQuNXxBQ3xBVHxBdHRlbmRpbmdEb2N0b3J8DVJPTHwxLjIuMy40LjZ8QUN8UlB8UmVmZXJyaW5nRG9jdG9yfA1ST0x8MS4yLjMuNC43fEFDfEFEfEFkbWl0dGluZ0RvY3RvcnwNUk9MfDEuMi4zLjQuOHxBQ3xDUHxDb25zdWx0aW5nRG9jdG9yfA1PUkN8Tld8QTEwMFpeTUVTQV9PUkRQTEN8QjEwMFpeTUVTQV9PUkRGSUx8fFNDfHx8fDIwMDAwODE2MTUxMHxeUk9TRVdPT0ReUkFORE9MUEh8fDcxMDFeRVNUUkFEQV5KQUlNRV5QXl5EUnxFbnRlcmVyXl5Mb2NhdGlvbl5FTF4wMDAwMHwoMzE0KTU1NS0xMjEyfDIwMDAwODE2MTUxMHx8OTIyMjI5LTEwXklIRS1SQUReSUhFLUNPREUtMjMxfHwNVFExfDF8MXxvbmNlfHx8fDIwMDAwODE2MTUxNTE1fA1PQlJ8MXxBMTAwWl5NRVNBX09SRFBMQ3xCMTAwWl5NRVNBX09SREZJTHx8fHx8fHx8fHx4eHh8fHw3MTAxXkVTVFJBREFeSkFJTUVeUF5eRFJ8fHx8fHx8fHx8fHx8fFdBTEt8fHx8fHx8fHx8fEF8fHwkUFJPQ0VEVVJFX0NPREUkfA1JUEN8QUNDMTIzfFJQSUR8fHxDUnxQcm90b2NvbENvZGVeUHJvdG9jb2xcUlxNZWFuaW5nXlByb3RvY29sU2NoZW1lfE1PRF9DUl9OQU1FXE1PRF9EWF9OQU1FfFNQU0x8TU9EXy4uLg=="/>
            <ParticipantObjectDetail type="MSH-9" value="T01JXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTAwMTEy"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EMnxEQ000Q0hFRXxNRVNBX09GfFhZWl9SQURJT0xPR1l8MjAyNDA5MTgxNTA3MTguMjQ3fHxBQ0teTzIzXkFDS3wxMDc0MzE1ODE3fFB8Mi41LjF8fHx8fHwgfHwNTVNBfEFBfDEwMDExMnw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTA3NDMxNTgxNw=="/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="M4000^^^ADT2" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>QU~EEN^MART~HA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

MWL's SPS Status Update on receive of HL7 ADT^A10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T12:51:08.995+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
            <EventOutcomeDescription>ARRIVED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Procedure Record audits on REST APIs invocation
...............................................

Following sample messages show audits emitted on invocation of REST APIs.

Update MWL
^^^^^^^^^^

Applicable on invocation of `Create / Update Scheduled Procedure Step <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MWL-RS/CreateUpdateSPS>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T12:26:28.983+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/WORKLIST/rs/mwlitems" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="2001C30"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Delete MWL
^^^^^^^^^^

Applicable on invocation of `Delete Scheduled Procedure Step <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MWL-RS/DeleteSPS>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2024-09-19T12:43:46.399+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/WORKLIST/rs/mwlitems/2.16.376.1.1.511752826.1.2.3390529.6263391/zxcv413248526348" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="2001C30"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Change MWL's SPS state
^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of `Change Status of Scheduled Procedure Step <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MWL-RS/ChangeStatusSPS>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T12:54:20.670+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
            <EventOutcomeDescription>CANCELED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/WORKLIST/rs/mwlitems/2.16.376.1.1.511752826.1.2.3390529.6263391/zxcv413248526348/status/CANCELED" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Update Study / Series attributes - Link Study with MWL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of `Link Instances with MWL Entry <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IOCM-RS/LinkInstancesWithMWLEntry>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T13:09:45.613+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/WORKLIST/rs/mwlitems/2.16.376.1.1.511752826.1.2.3390529.6263391/zxcv413248526348/move/113038%5EDCM" AlternativeUserID="49993" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="2001C30"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Procedure Create on imported MWL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of `Import matching Scheduled Procedure Steps from external MWL SCP <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MWL-RS/ImportMatchingSPS>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-19T13:17:31.435+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/dimse/CENTRAL/mwlitems/import/FACET" AlternativeUserID="49993" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="2.25.242213583753504953302127718937265097861" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="CD-SELMED-00000037"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="SMA001^^^SMA&amp;SM_EPI&amp;L" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Beckett^Noah</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Procedure Record audits on scheduler functions
..............................................

Following sample messages show audits emitted on trigger of scheduler functions.

Procedure Create on imported MWL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable on invocation of importing matching Scheduled Procedure Steps from external MWL SCP triggered by scheduler

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-19T13:39:46.068+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="49993" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="1.2.276.0.7230010.3.1.2.895706167.1.1681304884.578782" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="1820Z"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MH11^^^MANAGEH" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Moser^Paul</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Procedure Record audits on MPPS Forwarding
..........................................

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-19T11:35:26.182+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
            <EventOutcomeDescription>IN PROGRESS</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="demo2.j4care.com" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="CENTRAL" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <MPPS UID="2.25.166255563418865932941909299757043562240"/>
                <Accession Number="ACCESSION01"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-19T11:35:26.360+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
            <EventOutcomeDescription>COMPLETED</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="demo2.j4care.com" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="CENTRAL" AlternativeUserID="36354" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <MPPS UID="2.25.166255563418865932941909299757043562240"/>
                <Accession Number="ACCESSION01"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Procedure Record audits on Outgoing HL7 Messages
................................................

Following sample messages show audits emitted on HL7 Messages sent from archive to external HL7 receivers.

HL7 Forwarding
^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2024-09-18T15:15:34.440+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="HL7SND2|DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="1.2.40.0.13.1.15.110.3.165.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EMnxEQ000Q0hFRXxITDdSQ1Z8RENNNENIRUV8MjAwMDEyMTIwMTAxMDF8fE9NSV5PMjN8MTAwMTEyfFB8Mi41LjF8fHx8fHwgfHwNUElEfHx8TTQwMDBeXl5BRFQyfHxRVVxSXEVFTl5NQVJUXFJcSEF8fDE5NDUwODA0fE18fFdIfDgyMCBKT1JJRSBCTFZEXl5DSElDQUdPXklMXjYwNTIzfHx8fHx8fDIwLTk4LTQwMDB8fHx8fHx8fHx8fHx8fHx8fHx8fHwNUFYxfHxFfEVEfHx8fDEyMzReV0VBVkVSXlRJTU9USFleUF5eRFJ8NTEwMV5ORUxMXkZSRURFUklDS15QXl5EUnx8SFNSfHx8fHxBU3x8MDAwMF5BZG1pdHRpbmdeRG9jdG9yXlBeXkRSfHxWMTAwXl5eQURUMXx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHwyMDAwMDgyMDExMDB8fHx8fHx8VnwNUk9MfDEuMi4zLjQuNXxBQ3xBVHxBdHRlbmRpbmdEb2N0b3J8DVJPTHwxLjIuMy40LjZ8QUN8UlB8UmVmZXJyaW5nRG9jdG9yfA1ST0x8MS4yLjMuNC43fEFDfEFEfEFkbWl0dGluZ0RvY3RvcnwNUk9MfDEuMi4zLjQuOHxBQ3xDUHxDb25zdWx0aW5nRG9jdG9yfA1PUkN8Tld8QTEwMFpeTUVTQV9PUkRQTEN8QjEwMFpeTUVTQV9PUkRGSUx8fFNDfHx8fDIwMDAwODE2MTUxMHxeUk9TRVdPT0ReUkFORE9MUEh8fDcxMDFeRVNUUkFEQV5KQUlNRV5QXl5EUnxFbnRlcmVyXl5Mb2NhdGlvbl5FTF4wMDAwMHwoMzE0KTU1NS0xMjEyfDIwMDAwODE2MTUxMHx8OTIyMjI5LTEwXklIRS1SQUReSUhFLUNPREUtMjMxfHwNVFExfDF8MXxvbmNlfHx8fDIwMDAwODE2MTUxNTE1fA1PQlJ8MXxBMTAwWl5NRVNBX09SRFBMQ3xCMTAwWl5NRVNBX09SREZJTHx8fHx8fHx8fHx4eHh8fHw3MTAxXkVTVFJBREFeSkFJTUVeUF5eRFJ8fHx8fHx8fHx8fHx8fFdBTEt8fHx8fHx8fHx8fEF8fHwkUFJPQ0VEVVJFX0NPREUkfA1JUEN8QUNDMTIzfFJQSUR8fHxDUnxQcm90b2NvbENvZGVeUHJvdG9jb2xcUlxNZWFuaW5nXlByb3RvY29sU2NoZW1lfE1PRF9DUl9OQU1FXE1PRF9EWF9OQU1FfFNQU0x8TU9EX0NSMDFcTS4uLg=="/>
            <ParticipantObjectDetail type="MSH-9" value="T01JXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTAwMTEy"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORDJ8RENNNENIRUV8MjAyNDA5MTgxNTE1MzQuMzkzfHxBQ0teTzIzXkFDS3wxNDI0NzE2NzI3fFB8Mi41LjF8fHx8fHwgfHwNTVNBfEFBfDEwMDExMnw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTQyNDcxNjcyNw=="/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="M4000^^^ADT2" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>QU~EEN^MART~HA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of MPPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-18T17:11:48.962+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
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
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkxODE3MTE0OC44NTV8fE9NSV5PMjNeT01JX08yM3wxOTczMjM5MTkxfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fE1HSUQwMDF8fE1BTU1PR1JBUEhZXlRFU1QxXl5eXnx8MTk1MDAxMDJ8Rnx8fHx8fHxeXnx8fHx8fHx8fHx8fHx8fHx8fHx8fA1QVjF8fFV8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8Vg1PUkN8U0N8MDAwMEJEQjR8MDAwMEJEQjR8fENNDU9CUnx8MDAwMEJEQjR8MDAwMEJEQjR8fHx8MjAwMjA0MjYxMjAwfHx8fHx8fHx8fHwwMDAwQkRCNHwwMDAwQkRCNHx8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8fHx8fHx8fHx8fHx8DVRRMXx8fHx8fHwyMDAyMDQyNjEyMDB8fFJeUm91dGluZV5ITDcwMDc4DUlQQ3xBQ0NFU1NJT04wMXx8MS4xfHxNR3x8fHxNUFBTU0NVDQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="T01JXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTk3MzIzOTE5MQ=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkxODE3MTE0OC45MTd8fEFDS15PMjNeQUNLfDI3OTE1MTc5MHxQfDIuNS4xfHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTk3MzIzOTE5MXw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="Mjc5MTUxNzkw"/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1^^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of Study - Triggered by HL7 Procedure Status Update Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-18T17:06:02.443+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
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
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkxODE3MDU0OC41MzF8fE9NSV5PMjNeT01JX08yM3wxOTczMjM5MTkwfFB8Mi41LjF8fHx8fHxVTklDT0RFIFVURi04DVBJRHx8fE1BRFRQSUQzNTk3fHxWRU5UUkleVEVTVF5eXl58fDE5NzYwMjA1fE18fHx8fHx8Xl58fHx8fHx8fHx8fHx8fHx8fHx8fHwNUFYxfHxVfHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fFYNT1JDfFNDfEREM0IwMkE5fEREM0IwMkE5fHxDTQ1PQlJ8fEREM0IwMkE5fEREM0IwMkE5fHx8fDIwMDYwNDI2MTIzMjUyfHx8fHx8fHx8fHxERDNCMDJBOXxERDNCMDJBOXx8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8fHx8fHx8fHx8fHx8DVRRMXx8fHx8fHwyMDI0MDkxODE3MDU0OC41MzF8fFJeUm91dGluZV5ITDcwMDc4DUlQQ3x8fDEuMi44NDAuMTEzNjE5LjIuMjE2LjIuMS4yNjQyMDA2MTAzMjUyMjM0LjEwNTg5fHxOTXx8fHwN"/>
            <ParticipantObjectDetail type="MSH-9" value="T01JXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTk3MzIzOTE5MA=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkxODE3MDYwMi4zNDd8fEFDS15PMjNeQUNLfDcyNjU0NjQ5NXxQfDIuNS4xfHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTk3MzIzOTE5MHw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="NzI2NTQ2NDk1"/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MADTPID3597" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>VENTRI^TEST^^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of Study - Using DCM2HL7Exporter triggered by REST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-18T16:35:57.387+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.392.200036.9125.0.198811291108.7/export/DcM2HL7PSU-Exporter" AlternativeUserID="13561" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
        <ParticipantObjectIdentification ParticipantObjectID="2.25.8306615672720099948502801105922467113" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkxODE2MzU1Ny4yNzJ8fE9NSV5PMjNeT01JX08yM3w3MTg3MzczMTd8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNUElEfHx8RlVKSTAwMDAxXl5eSk1TfHxUQU5BS0FeSEFOQUtPXl5eXnx8MTkyNTA4MjR8Rnx8fHx8fHxeXnx8fHx8fHx8fHx8fHx8fHx8fHx8fA1QVjF8fFV8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8Vg1PUkN8U0N8QTM0QzIyOUZ8QTM0QzIyOUZ8fENNDU9CUnx8QTM0QzIyOUZ8QTM0QzIyOUZ8fHx8fHx8fHx8fHx8fHxGVUpJOTU3MDF8QTM0QzIyOUZ8fHx8fFJBRHxSfHxeXl5eXlJ8fHx8fHx8fHx8fHx8fHx8fA1UUTF8fHx8fHx8MjAyNDA5MTgxNjM1NTcuMjcyfHxSXlJvdXRpbmVeSEw3MDA3OA1PQlh8MXxTVHwxMTMwMTReRElDT00gU3R1ZHleRENNfHwxLjIuMzkyLjIwMDAzNi45MTI1LjAuMTk4ODExMjkxMTA4Ljd8fHx8fHxPfHx8fHx8fHx8fHx8fA1PQlh8MnxTVHxeU2VyaWVzIEluc3RhbmNlIFVJRHx8MS4yLjM5Mi4yMDAwMzYuOTEyNS4wLjE5ODgxMTI5MTEwOC43fHx8fHx8Rnx8fHx8fHx8fHx8fEtBTkFHQVdBIEMuQy58DU9CWHwzfFNUfF5TT1AgSW5zdGFuY2UgVUlEfHwxLjIuMzkyLjIwMDAzNi45MTI1LjAuMTk5NTA3MjAwOTM1MDl8fHx8fHxGfHx8fHx8fHx8fHx8fA1PQlh8NHxTVHxeU09QIENsYXNzIFVJRHx8MS4yLjg0MC4xMDAwOC41LjEuNC4xLjEuMXx8fHx8fEZ8fHx8fHx8fHx8fHx8DU9CWHw1fENFfF5eDQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="T01JXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="NzE4NzM3MzE3"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkxODE2MzU1Ny4zNTB8fEFDS15PMjNeQUNLfDEzMTQ3MzUxNDN8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDcxODczNzMxN3w="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTMxNDczNTE0Mw=="/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="FUJI00001^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TANAKA^HANAKO^^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Notify HL7 Receivers on receive of Study - Using DCM2HL7Exporter triggered by Export Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-09-18T16:47:46.425+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
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
        <ParticipantObjectIdentification ParticipantObjectID="2.25.294012187024780465613920798759483465568" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDkxODE2NDc0Ni4zNTN8fE9NSV5PMjNeT01JX08yM3w3MTg3MzczMTh8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNUElEfHx8Q1IzfHxDUlRIUkVFXlBBVUxeXl5efHwxOTUwMDQwM3xNfHx8fHx8fF5efHx8fHx8fHx8fHx8fHx8fHx8fHx8DVBWMXx8VXx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHxWDU9SQ3xTQ3wzREM4NDRDMHwzREM4NDRDMHx8Q00NT0JSfHwzREM4NDRDMHwzREM4NDRDMHx8fHwyMDAxMDQzMHx8fHx8fHx8fHx8MjAwMUMzMHwzREM4NDRDMHx8fHx8UkFEfFJ8fF5eXl5eUnx8fHx8NjA2MF5eXl5eXk1pZHdlc3QgQXZpYXRvcnN8fHx8fHx8fHx8fHwNVFExfHx8fHx8fDIwMjQwOTE4MTY0NzQ2LjM1M3x8Ul5Sb3V0aW5lXkhMNzAwNzgNT0JYfDF8U1R8MTEzMDE0XkRJQ09NIFN0dWR5XkRDTXx8MS4xMTM2NTQuMS4yMDAxLjMwfHx8fHx8T3x8fDIwMDEwNDMwfHx8fHx8fHx8fA1PQlh8MnxTVHxeU2VyaWVzIEluc3RhbmNlIFVJRHx8MS4xMTM2NTQuMS4yMDAxLjMwLjMuNjAxfHx8fHx8Rnx8fHx8fHx8fHx8fHwNT0JYfDN8U1R8XlNPUCBJbnN0YW5jZSBVSUR8fDEuMTEzNjU0LjEuMjAwMS4zMC4zLjF8fHx8fHxGfHx8MjAwMTA1MDExNDE1MDAuMDAwMHx8fHx8fHx8fHwNT0JYfDR8U1R8XlNPUCBDbGFzcyBVSUR8fDEuMi44NDAuMTAwMDguNS4xLjQuMS4xLjg4LjExfHx8fHx8Rnx8fHx8fHx8fHx8fHwNT0JYfDV8Q0V8MTE1MjgtN15SYWRpb2xvZ3kgUmVwb3J0XkxODQ=="/>
            <ParticipantObjectDetail type="MSH-9" value="T01JXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="NzE4NzM3MzE4"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDkxODE2NDc0Ni4zNzh8fEFDS15PMjNeQUNLfDE4MzUxOTI2OTJ8UHwyLjUuMXx8fHx8fFVOSUNPREUgVVRGLTgNTVNBfEFBfDcxODczNzMxOHw="/>
            <ParticipantObjectDetail type="MSH-9" value="QUNLXk8yMw=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTgzNTE5MjY5Mg=="/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="CR3" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>CRTHREE^PAUL^^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>