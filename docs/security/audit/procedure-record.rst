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

MWL created by HL7 Order message

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2018-09-12T12:48:59+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
        <ActiveParticipant UserID="MESA_OF|XYZ_RADIOLOGY" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="MESA_IM|XYZ_IMAGE_MANAGER" AlternativeUserID="18494" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.4.0.13.1.432252867.1552647.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8TUVTQV9PRnxYWVpfUkFESU9MT0dZfE1FU0FfSU18WFlaX0lNQUdFX01BTkFHRVJ8MjAxNjA1MTExNTEyfHxPUk1eTzAxfDEwMDExMnxQfDIuMy4xfHx8fHx8IHx8DVBJRHx8fE00MDAxXl5eQURUMXx8S0lOR15NQVJUSU58fDE5NDUwODA0fE18fFdIfDgyMCBKT1JJRSBCTFZEXl5DSElDQUdPXklMXjYwNTIzfHx8fHx8fDIwLTk4LTQwMDB8fHx8fHx8fHx8fHx8fHx8fHx8fHwNUFYxfHxFfEVEfHx8fDEyMzReV0VBVkVSXlRJTU9USFleUF5eRFJ8NTEwMV5ORUxMXkZSRURFUklDS15QXl5EUnwwMDAwXkNvbnN1bHRpbmdeRG9jdG9yXlBeXkRSfEhTUnx8fHx8QVN8fDAwMDBeQWRtaXR0aW5nXkRvY3Rvcl5QXl5EUnx8VjEwMF5eXkFEVDF8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8MjAwMDA4MjAxMTAwfHx8fHx8fFZ8DU9SQ3xOV3xBMTAwWl5NRVNBX09SRFBMQ3xCMTAwWl5NRVNBX09SREZJTHx8U0N8fDFeb25jZV5eXl5TfHwyMDAwMDgxNjE1MTB8XlJPU0VXT09EXlJBTkRPTFBIfHw3MTAxXkVTVFJBREFeSkFJTUVeUF5eRFJ8RW50ZXJlcl5eTG9jYXRpb25eRUxeMDAwMDB8KDMxNCk1NTUtMTIxMnwyMDAwMDgxNjE1MTB8fDkyMjIyOS0xMF5JSEUtUkFEXklIRS1DT0RFLTIzMXxTU0FFVDJ8DU9CUnwxfEExMDBaXk1FU0FfT1JEUExDfEIxMDBaXk1FU0FfT1JERklMfFAxXlByb2NlZHVyZSAxXkVSTF9NRVNBXlgxX0ExXlNQIEFjdGlvbiBJdGVtIFgxX0ExXkRTU19NRVNBfHx8fHx8fHx8eHh4fHxSYWRpb2xvZ3leXl5eUnw3MTAxXkVTVFJBREFeSkFJTUVeUF5eRFJ8fCRBQ0NFU1NJT05fTlVNQkVSJHwkUkVRVUVTVEVEX1BST0NFRFVSRV9JRCR8JFNDSEVEVUxFRF9QUk9DRURVUkVfU1RFUF9JRCR8fHx8TVJ8fHwxXm9uY2VeXl5eU3x8fFdBTEt8fHx8fHx8fHx8fEF8fHwkUFJPQ0VEVVJFX0NPREUkDVpEU3wxLjIuNC4wLjEzLjEuNDMyMjUyODY3LjE1NTI2NDcuMV4xMDBeQXBwbGljYXRpb25eRElDT00N"/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8TUVTQV9JTXxYWVpfSU1BR0VfTUFOQUdFUnxNRVNBX09GfFhZWl9SQURJT0xPR1l8MjAxODA5MTIxMjQ4NTguMDMzfHxBQ0teTzAxXkFDS3wxOTU5MTEzMjl8UHwyLjMuMXx8fHx8fCB8fA1NU0F8QUF8MTAwMTEyfA=="/>
            <ParticipantObjectDetail type="MSH-9" value="T1JNXk8wMQ=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTAwMTEy"/>
            <ParticipantObjectDetail type="MSH2-9" value="QUNLXk8wMQ=="/>
            <ParticipantObjectDetail type="MSH2-10" value="MTk1OTExMzI5"/>
            <ParticipantObjectDescription>
                <Accession Number="$ACCESSION_NUMBER$"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MM2^^^JMS~MM2^^^JMS1&1.2.3&ISO~MM2^^^JMS2~MM2^^^&1.2.3.4.5.6.7&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>KING^MARTIN</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

MWL created using archive UI / REST service

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2019-02-05T18:23:08+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
       </EventIdentification>
       <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
          <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID" />
       </ActiveParticipant>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/mwlitems" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="2.25.236495948151023012026390020924423660325" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <Accession Number="A-00000001" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="3850402XXXX" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>KASMANN^VARMO</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MWL SPS Status updated from SCHEDULED to ARRIVED on receive of ADT^A10

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-06-17T15:35:57.431+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
       </EventIdentification>
       <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" AlternativeUserID="21263" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.4.0.13.1.432252867.1552647.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription />
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="M40011^^^ADT11" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>KING1^MARTIN1</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MPPS In-Progress received by archive

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2020-05-04T17:06:04.303+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
          <EventOutcomeDescription>IN PROGRESS</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="11475" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <MPPS UID="2.25.167652009927391867209751951017387655636" />
             <Accession Number="SMS000018" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MPPS Completed received by archive

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-05-04T17:06:04+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
          <EventOutcomeDescription>COMPLETED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="11475" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <MPPS UID="2.25.167652009927391867209751951017387655636" />
             <Accession Number="SMS000018" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MPPS In-Progress forwarded by archive

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2020-05-08T12:44:45+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
          <EventOutcomeDescription>IN PROGRESS</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="test-ng" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="TEST" AlternativeUserID="8959" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <MPPS UID="2.25.124456130015603657296934039173159643921" />
             <Accession Number="SMS000018" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MPPS Completed forwarded by archive

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-05-08T12:44:55+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
          <EventOutcomeDescription>COMPLETED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="test-ng" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="TEST" AlternativeUserID="8959" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <MPPS UID="2.25.124456130015603657296934039173159643921" />
             <Accession Number="SMS000018" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MWL status changed from SCHEDULED to STARTED triggered by MPPS In-Progress received by archive

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-05-04T16:24:13+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
          <EventOutcomeDescription>STARTED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="26364" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <MPPS UID="2.25.309202333051991089433393223932804305160" />
             <Accession Number="SMS000018" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

MWL status changed from STARTED to COMPLETED triggered by MPPS Completed received by archive

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-05-04T16:24:13+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record" />
          <EventOutcomeDescription>COMPLETED</EventOutcomeDescription>
       </EventIdentification>
       <ActiveParticipant UserID="MPPSSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="26364" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <MPPS UID="2.25.309202333051991089433393223932804305160" />
             <Accession Number="SMS000018" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>
