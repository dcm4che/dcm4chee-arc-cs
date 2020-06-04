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
            <ParticipantObjectDescription>
                <Accession Number="$ACCESSION_NUMBER$"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="M4001^^^ADT1" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>KING^MARTIN</ParticipantObjectName>
        </ParticipantObjectIdentification>

    </AuditMessage>