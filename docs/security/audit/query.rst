Query
=====

Trigger Events
--------------

This message is emitted by the archive for queries triggered by UI or by C-FIND on following levels :

- Patient
- Study
- Series
- Instance
- Modality Worklist Entry

Additionally, this message is also emitted if a Patient Demographics Query is invoked by the archive acting as a Patient
Demographics Consumer to any Patient Demographics Supplier.

Message Structure
-----------------

.. csv-table:: Entities in Query Audit Message

    :ref:`event-identification-query`
    :ref:`active-participant-initiator-query`, Not present in Patient Demographics Query triggered by scheduler case
    :ref:`active-participant-archive-query`, Not present in Patient Demographics Query triggered by scheduler case
    :ref:`active-participant-pdq-consumer-query`, Present only in Patient Demographics Query case
    :ref:`active-participant-pdq-supplier-query`, Present only in Patient Demographics Query case
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-c-find-query`, Present only in Query by C-FIND
    :ref:`participant-object-qido-query`, Present only in QIDO Query
    :ref:`participant-object-pdq-query`, Present only in Patient Demographics Query case
    :ref:`participant-object-pdq-patient-query`, Present only in Patient Demographics Query case

.. csv-table:: Event Identification
   :name: event-identification-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110112, DCM, 'Query')"
   EventActionCode, M, | Execute ⇒ 'E'
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'
   EventTypeCode, C, | Patient Demographics Query case ⇒ EV (ITI-21, IHE Transactions, 'Patient Demographics Query')

.. csv-table:: Active Participant : Initiator
   :name: active-participant-initiator-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Query triggered by C-FIND ⇒ 'Calling AE title in association'
   | QIDO or Patient Demographics query triggered by REST services : Secured Archive ⇒ 'User name of logged in user'
   | QIDO or Patient Demographics query triggered by REST services : Unsecured Archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Query triggered by C-FIND ⇒ EV (110119, DCM, 'Station AE Title')
   | QIDO or Patient Demographics query triggered by REST services : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | QIDO or Patient Demographics query triggered by REST services : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, "| Query triggered by C-FIND : Application ⇒ '2'
   | QIDO or Patient Demographics query triggered by REST services : Person ⇒ '1'"
   UserIsRequestor, M, | true
   RoleIDCode, M, "| EV (110153, DCM, 'Source Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Query triggered by C-FIND ⇒ 'Called AE title in association'
   | QIDO or Patient Demographics query triggered by REST services ⇒ 'Request URI'"
   UserIDTypeCode, U, "| Triggered by C-FIND ⇒ EV (110119, DCM, 'Station AE Title')
   | Triggered from UI ⇒ EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   RoleIDCode, M, "| EV (110152, DCM, 'Destination Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Patient Demographics Consumer
   :name: active-participant-pdq-consumer-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| 'Sending Application and Facility Name'"
   UserIDTypeCode, U, "| EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
   UserTypeCode, U, | 2
   UserIsRequestor, M, "| Patient Demographics query triggered by scheduler ⇒ true
   | Patient Demographics query triggered by REST services ⇒ false"
   RoleIDCode, M, "| EV (110153, DCM, 'Source Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Patient Demographics Supplier
   :name: active-participant-pdq-supplier-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| 'Receiving Application and Facility Name'"
   UserIDTypeCode, U, "| EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
   UserTypeCode, U, | 2
   UserIsRequestor, M, | false
   RoleIDCode, M, "| EV (110152, DCM, 'Destination Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification : C-FIND Query
   :name: participant-object-c-find-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, "| For patient query ⇒ '1.2.840.10008.5.1.4.1.2.1.1'
   | For study/series/instance query ⇒ '1.2.840.10008.5.1.4.1.2.2.1'
   | For MWL query ⇒ '1.2.840.10008.5.1.4.31'"
   ParticipantObjectTypeCode, M, | SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, | Report ⇒ '3'
   ParticipantObjectIDTypeCode, M, "| EV (110181, DCM, 'SOP Class UID')"
   ParticipantObjectQuery, M, | Base64 encoded value of Query keys
   ParticipantObjectDetail, MC, | Base64 encoded value for ImplicitVRLittleEndian '1.2.840.10008.1.2' ⇒ 'type=TransferSyntax value=MS4yLjg0MC4xMDAwOC4xLjI='"

.. csv-table:: Participant Object Identification : QIDO Query
   :name: participant-object-qido-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, "| For patient query ⇒ 'SearchForPatients'
   | For study query ⇒ 'SearchForStudies'
   | For series query ⇒ 'SearchForStudySeries' or 'SearchForSeries'
   | For Instance query ⇒ 'SearchForInstances' or 'SearchForStudyInstances' or 'SearchForStudySeriesInstances'
   | For MWL query ⇒ 'SearchForSPS'"
   ParticipantObjectTypeCode, M, | SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, | Query ⇒ '24'
   ParticipantObjectIDTypeCode, M,  "| EV (QIDO, 99DCM4CHEE, 'QIDO_Query')"
   ParticipantObjectQuery, M, | Base64 encoded value of Request URI plus the Query String
   ParticipantObjectDetail, MC, | Base64 encoded value for 'UTF-8' ⇒ 'type=QueryEncoding value=VVRGLTg='

.. csv-table:: Participant Object Identification : Patient Demographics Query
   :name: participant-object-pdq-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, "| Patient Demographics Query triggered by scheduler ⇒ 'PatientVerificationScheduler'
   | Patient Demographics Query triggered by Compare Patient Demographics service ⇒ 'DiffPatientDemographics'
   | Patient Demographics Query triggered by Update Patient Demographics service ⇒ 'UpdatePatientDemographics'
   | Patient Demographics Query triggered by Query Patient Demographics service ⇒ 'QueryPatientDemographics'"
   ParticipantObjectTypeCode, M, | SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, | Query ⇒ '24'
   ParticipantObjectIDTypeCode, M,  "| EV (ITI-21, IHE Transactions, 'Patient Demographics Query')"
   ParticipantObjectQuery, M, | Base64 encoded value of complete QBP^Q22 query message

.. csv-table:: Participant Object Identification : Patient Demographics Query - Patient
   :name: participant-object-pdq-patient-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown,
   ParticipantObjectTypeCode, M, Person : '1',
   ParticipantObjectTypeCodeRole, M, Patient : '1',
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')",
   ParticipantObjectName, U, Patient Name,
   ParticipantObjectDetail, U, 'type=HL7v2 Message value=<Base-64 encoded HL7 message>'
   ParticipantObjectDetail, U, 'type=HL7v2 Message value=<Base-64 encoded HL7 response>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 message control ID>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 response message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 response message control ID>'

Sample Message
--------------

Query triggered using QIDO-RS

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="E" EventDateTime="2017-07-27T09:12:21.331+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserTypeCode="1" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/patients" AlternativeUserID="3390" UserTypeCode="2" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="SearchForPatients" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
            <ParticipantObjectIDTypeCode csd-code="QIDO" originalText="QIDO_Query" codeSystemName="99DCM4CHEE"/>
            <ParticipantObjectQuery>L2RjbTRjaGVlLWFyYy9hZXRzL0RDTTRDSEVFL3JzL3BhdGllbnRzaW5jbHVkZWZpZWxkPWFsbCZvZmZzZXQ9MCZsaW1pdD0yMSZvcmRlcmJ5PVBhdGllbnROYW1l</ParticipantObjectQuery>
            <ParticipantObjectDetail type="QueryEncoding" value="VVRGLTg="/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Query triggered using C-FIND

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="E" EventDateTime="2019-02-05T18:01:25+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110112" codeSystemName="DCM" originalText="Query" />
       </EventIdentification>
       <ActiveParticipant UserID="FINDSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.840.10008.5.1.4.1.2.2.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110181" originalText="SOP Class UID" codeSystemName="DCM" />
          <ParticipantObjectQuery>CABSAAYAAABTVFVEWSAgAA0ALAAAADIuMjUuMjIzNDk1ODQxNjcyNTIzMjI3ODMyMTMzMTUzNTY3ODg2NjU5ODAx</ParticipantObjectQuery>
          <ParticipantObjectDetail type="TransferSyntax" value="MS4yLjg0MC4xMDAwOC4xLjI=" />
       </ParticipantObjectIdentification>
    </AuditMessage>

Patient Demographics Query

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="E" EventDateTime="2021-07-05T09:16:21.400+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
            <EventTypeCode csd-code="ITI-21" codeSystemName="IHE Transactions" originalText="Patient Demographics Query"/>
            <EventOutcomeDescription>Patient Demographics Query</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/pdq/testhl7pdq/patients/PDQ-4711%5E%5E%5EDCM4CHE-TEST%261.2.40.0.13.1.1.999%26ISO" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="QueryPatientDemographics" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
            <ParticipantObjectIDTypeCode csd-code="ITI-21" originalText="Patient Demographics Query" codeSystemName="IHE Transactions"/>
            <ParticipantObjectQuery>
                TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDIxMDcwNTA5MTYyMC43ODd8fFFCUF5RMjJeUUJQX1EyMXwyMTI2MTA5NTkzfFB8Mi41fHx8fHx8ODg1OS8xfHx8DVFQRHxJSEUgUERRIFF1ZXJ5fFFSWTIxMjYxMDk1OTN8QFBJRC4zLjFeUERRLTQ3MTF+QFBJRC4zLjQuMV5EQ000Q0hFLVRFU1R+QFBJRC4zLjQuMl4xLjIuNDAuMC4xMy4xLjEuOTk5fkBQSUQuMy40LjNeSVNPfA1SQ1B8SXx8fHx8fA0=
            </ParticipantObjectQuery>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="PDQ-4711^^^DCM4CHE-TEST&1.2.40.0.13.1.1.999&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>DOE^JOHN</ParticipantObjectName>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDIxMDcwNTA5MTYyMC43ODd8fFFCUF5RMjJeUUJQX1EyMXwyMTI2MTA5NTkzfFB8Mi41fHx8fHx8ODg1OS8xfHx8DVFQRHxJSEUgUERRIFF1ZXJ5fFFSWTIxMjYxMDk1OTN8QFBJRC4zLjFeUERRLTQ3MTF+QFBJRC4zLjQuMV5EQ000Q0hFLVRFU1R+QFBJRC4zLjQuMl4xLjIuNDAuMC4xMy4xLjEuOTk5fkBQSUQuMy40LjNeSVNPfA1SQ1B8SXx8fHx8fA0="/>
            <ParticipantObjectDetail type="MSH-9" value="UUJQXlEyMg=="/>
            <ParticipantObjectDetail type="MSH-10" value="MjEyNjEwOTU5Mw=="/>
            <ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDIxMDcwNTA5MTYyMC44MjB8fFJTUF5LMjJeUlNQX0syMXwxMDY0NjIyMjk0fFB8Mi41fHx8fHx8ODg1OS8xDU1TQXxBQXwyMTI2MTA5NTkzfA1RQUt8UVJZMjEyNjEwOTU5M3xPSw1RUER8SUhFIFBEUSBRdWVyeXxRUlkyMTI2MTA5NTkzfEBQSUQuMy4xXlBEUS00NzExfkBQSUQuMy40LjFeRENNNENIRS1URVNUfkBQSUQuMy40LjJeMS4yLjQwLjAuMTMuMS4xLjk5OX5AUElELjMuNC4zXklTT3wNUElEfHx8UERRLTQ3MTFeXl5EQ000Q0hFLVRFU1QmMS4yLjQwLjAuMTMuMS4xLjk5OSZJU098fERPRV5KT0hOfHwxOTQ3MTExMXxNfHx8U1RSRUVUXl5DSVRZXl40NzExfHx8fHx8fEFDQy00NzExXl5eRENNNENIRS1URVNUJjEuMi40MC4wLjEzLjEuMS45OTkmSVNP"/>
            <ParticipantObjectDetail type="MSH-9" value="UlNQXksyMg=="/>
            <ParticipantObjectDetail type="MSH-10" value="MTA2NDYyMjI5NA=="/>
        </ParticipantObjectIdentification>
    </AuditMessage>