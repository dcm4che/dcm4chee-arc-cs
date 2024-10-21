DICOM Instances Accessed
========================

Trigger Events
--------------

This message is emitted by the archive in following cases :

- Some objects / series of study are rejected using UI
- Some objects / series of study are rejected in an external archive using UI
- Rejection Notes for some objects of a study are stored to the archive using `RAD-66 <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf#page=455>`_ transaction.
- Objects are retrieved from an external archive by HL7 Prefetch Scheduler
- Update study/series expiration date using UI / Study Retention Policy / HL7 Study Retention Policy.
- Update study attributes using UI.
- Previous series/instances of a study are deleted on subsequent receive of objects having same SOP IUID but different Series IUID
- Scheduler triggered study size & query attributes calculation
- Retrieve of objects from fallback C-MOVE SCP

Message Structure
-----------------

.. csv-table:: Entities in DICOM Instances Accessed Audit Message

    :ref:`event-identification-instances-accessed`
    :ref:`active-participant-archive-instances-accessed`, Not present in scheduler triggered study size & query attributes calculation
    :ref:`active-participant-initiator-instances-accessed`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-instances-accessed`
    :ref:`participant-object-patient-instances-accessed`

.. csv-table:: Event Identification
   :name: event-identification-instances-accessed
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110103, DCM, 'DICOM Instances Accessed')"
   EventActionCode, M, "| Rejection / Deletion case : Delete ⇒ 'D'
   | Update study attributes / expiration date case : Update ⇒ 'U'
   | Scheduler triggered study size & query attributes calculation case : Read ⇒ 'R'
   | Update expiration date for frozen study / series case : Read ⇒ 'R'"
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, "| Rejection / Deletion case : Success ⇒ 'Rejection Code Meaning'
   | Rejection / Deletion case : Minor failure ⇒ 'Rejection Code Meaning + Error/Exception message'
   | All other cases case : Minor failure ⇒ 'Error/Exception message'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-instances-accessed
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Action triggered using association ⇒ 'Application entity title of Archive Device used in the association'
   | Action triggered using archive UI ⇒ 'Invoked URL'
   | Action triggered using HL7 messages ⇒ 'Receiving Application and Facility'"
   UserIDTypeCode, U, "| Action triggered using association ⇒ EV (110119, DCM, 'Station AE Title')
   | Action triggered from UI ⇒ EV (12, RFC-3881, 'URI')
   | Action triggered using HL7 messages ⇒ EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Initiator
   :name: active-participant-initiator-instances-accessed
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Action triggered using association ⇒ 'Application entity title of initiating system'
   | Action triggered using UI : Secured Archive ⇒ 'User name of logged in user'
   | Action triggered using UI : Unsecured archive ⇒ 'Remote IP address'
   | Action triggered using HL7 messages ⇒ 'Sending Application and Facility'
   | Scheduler triggered study size & query attributes calculation ⇒ 'Archive Device Name'"
   UserIDTypeCode, U, "| Action triggered using archive UI (Secured archive) ⇒ EV (113871, DCM, 'Person ID')
   | Action triggered using archive UI (Unsecured archive) ⇒ EV (110182, DCM, 'Node ID')
   | Action triggered using association ⇒ EV (110119, DCM, 'Station AE Title')
   | Action triggered using HL7 messages ⇒ EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Scheduler triggered study size & query attributes calculation case ⇒ EV (113877, DCM, 'Device Name')"
   UserTypeCode, U, "| Action triggered using archive UI : Person ⇒ '1'
   | Action triggered using association or by device : Application ⇒ '2'"
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification : Study
   :name: participant-object-study-instances-accessed
   :widths: 30, 5, 65, 20
   :header: Field Name, Opt, Description, Notes

   ParticipantObjectID, M, Study Instance UID or 1.2.40.0.13.1.15.110.3.165.1 if unknown,
   ParticipantObjectTypeCode, M, System ⇒ '2',
   ParticipantObjectTypeCodeRole, M, Report ⇒ '3',
   ParticipantObjectIDTypeCode, M, "EV (110180, DCM, 'Study Instance UID')",
   ParticipantObjectDetail, U, "| All cases ⇒ 'Base-64 encoded study date if Study has StudyDate(0008,0020) attribute', Not present for scheduler triggered study size & query attributes calculation
   | Update study / series expiration date ⇒ 'Base-64 encoded expiration date (7777,1023)'",
   ParticipantObjectDescription, U, , Not present for scheduler triggered study size & query attributes calculation
   SOPClass, MC, Rejection / Deletion case ⇒ Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>, Not present for scheduler triggered study size & query attributes calculation
   Accession, U, Accession Number, Not present for scheduler triggered study size & query attributes calculation
   ParticipantObjectDataLifeCycle, U, Scheduler triggered study size & query attributes calculation case : AggregationSummarizationDerivation ⇒ '8'

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-instances-accessed
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown
   ParticipantObjectTypeCode, M, Person ⇒ '1'
   ParticipantObjectTypeCodeRole, M, Patient ⇒ '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name


Sample Messages
---------------

Update Entities
...............

Update Study
^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T11:07:29.705+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1118.54.200" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU="/>
            <ParticipantObjectDescription>
                <Accession Number="GE000257"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1118" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>BUXTON^STEVEN</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Update Series
^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T11:00:28.710+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.3.12.2.1107.5.8.1.12345678.199508041416590859569/series/1.3.12.2.1107.5.8.1.12345678.199508041416590860429" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDI="/>
            <ParticipantObjectDescription>
                <Accession Number="SMS000018"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Expiration Date Update
......................

Update Study Expiration Date - Triggered by HL7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T11:41:03.356+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="TQADK|TQA" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="HL7SND|DCM4CHEE" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="ExpirationDate" value="MjAyNC0wOC0yOQ=="/>
            <ParticipantObjectDescription>
                <Accession Number="2001C30"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Update Study Expiration Date - Triggered by REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T10:14:07.276+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1118.54.200/expire/20240828" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU="/>
            <ParticipantObjectDetail type="ExpirationDate" value="MjAyNC0wOC0yOA=="/>
            <ParticipantObjectDescription>
                <Accession Number="GE000257"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1118" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>BUXTON^STEVEN</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Update Series Expiration Date - Triggered by REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T10:55:29.264+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.3.12.2.1107.5.8.1.12345678.199508041416590859569/series/1.3.12.2.1107.5.8.1.12345678.199508041416590860429/expire/20240828" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDI="/>
            <ParticipantObjectDetail type="ExpirationDate" value="MjAyNC0wOC0yOA=="/>
            <ParticipantObjectDescription>
                <Accession Number="SMS000018"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="SMS530102" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Access Control ID Update
........................

Applicable for `Study Access Control Services <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/ACCESS-RS>`_

Update Study Access Control ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T11:24:38.233+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1115.261.200/access/access1" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
            <ParticipantObjectDescription>
                <Accession Number="GE0005"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1115" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Update Access Control ID of Matching Studies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="U" EventDateTime="2024-08-28T11:33:40.253+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/access/access3?ModalitiesInStudy=MG" AlternativeUserID="8804" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwMjA0MjY="/>
            <ParticipantObjectDescription>
                <Accession Number="ACCESSION01"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Retrieve Entities from external archive
.......................................

Applicable for `Invoke C-MOVE requests on external C-MOVE SCP <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MOVE-RS>`_ REST APIs

Retrieve matching studies from external archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-19T15:31:07.880+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/dimse/DCM4CHEE/studies/export/dicom:STORESCP?ModalitiesInStudy=NM" AlternativeUserID="54270" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Error Case

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-20T10:58:57.794+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventTypeCode csd-code="A702" codeSystemName="99DCM4CHEE" originalText="Refused: Out Of Resources - Unable to perform sub-operations"/>
            <EventOutcomeDescription>Number Of Failed Sub operations : 1</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/dimse/DCM4CHEE/query:DCM4CHEE/studies/export/dicom:STORESCP?ModalitiesInStudy=NM" AlternativeUserID="24025" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Retrieve study from external archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-19T15:58:57.929+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/dimse/DCM4CHEE/studies/1.2.840.113619.2.216.2.1.2642006103252234.10589/export/dicom:STORESCP" AlternativeUserID="54270" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Error Case

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-19T16:14:17.756+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>java.net.ConnectException: Connection refused</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/dimse/DCM4CHEE/studies/1.2.840.113619.2.216.2.1.2642006103252234.10589/export/dicom:STORESCP" AlternativeUserID="54270" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

HL7 triggered Prefetch Studies
..............................

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-20T11:40:11.928+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="24025" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.113654.1.2001.30" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Error Case

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-20T11:47:11.594+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventTypeCode csd-code="A702" codeSystemName="99DCM4CHEE" originalText="Refused: Out Of Resources - Unable to perform sub-operations"/>
            <EventOutcomeDescription>Number Of Failed Sub operations : 1</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="24025" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Study Size Calculation
......................

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-07-29T09:34:13.294+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="5518" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113543.6.6.4.1.623691791684870846611353555872217279695" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="8">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="54321" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>HD11^SAMPLE IMAGES^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Partial Rejection of Studies
............................

Using REST API
^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2023-11-21T06:43:48.442+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1115.261.200/series/1.2.840.113674.1115.261.178.300/reject/113039%5EDCM" AlternativeUserID="10296" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
            <ParticipantObjectDescription>
                <Accession Number="GE0005"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

On store of rejection note over DICOM C-Store
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-22T12:45:53.042+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
    		<EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="39489" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
    		<ParticipantObjectDescription>
    			<Accession Number="GE0005"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

On store of rejection note by STOW-RS REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2023-12-04T09:55:28.062+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="10469" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU="/>
            <ParticipantObjectDescription>
                <Accession Number="GE0002"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1118^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>BUXTON^STEVEN</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

In external archive
^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2023-11-22T08:54:02.312+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/dimse/DCM4CHEE2/studies/1.2.392.200036.9125.0.198811291108.7/series/1.2.392.200036.9125.0.198811291108.7/reject/113039%5EDCM" AlternativeUserID="9174" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE2" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.198811291108.7" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="FUJI95701"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="FUJI00001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TANAKA^HANAKO</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Expired study partially rejected by Reject Expired Studies Scheduler
....................................................................

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2023-11-22T09:59:09.996+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="12384" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
            <ParticipantObjectDescription>
                <Accession Number="GE0005"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Previous study partially rejected on subsequent receive of objects with same SOP Instance UID but different Study/Series Instance UIDs
......................................................................................................................................

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="D" EventDateTime="2023-11-22T11:41:27.611+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="12384" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
            <ParticipantObjectDescription>
                <Accession Number="GE0005"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Lifecycle Management
....................

Apply Retention Policy REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable for expiration of studies by `Apply Retention Policy REST Service <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IOCM-RS/applyRetentionPolicy>`_ REST API

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-05-18T17:34:53.967+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed" />
       </EventIdentification>
       <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
          <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID" />
       </ActiveParticipant>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/expire/series" AlternativeUserID="23592" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.199302241758.16" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDetail type="Expiration Date" value="MjAyMC0wNS0xOQ==" />
          <ParticipantObjectDescription>
             <Accession Number="FUJI95714" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="FUJI00014" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>NAGASHIMA^TAKANORI</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

Apply Retention Policy by HL7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable for expiration of studies by `HL7 Study Retention Policy <https://dcm4chee-arc-cs.readthedocs.io/en/latest/networking/config/hl7StudyRetentionPolicy.html>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="U" EventDateTime="2020-05-19T11:30:12.309+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed" />
       </EventIdentification>
       <ActiveParticipant UserID="PAMSimulator|IHE" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE|DCM4CHEE" AlternativeUserID="4544" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDetail type="ExpirationDate" value="MjAyMC0wNS0yMA==" />
          <ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU=" />
          <ParticipantObjectDescription>
             <Accession Number="GE0002" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="GE1118" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>Berger1^Oliver1</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>


Retrieve of objects from fallback C-MOVE SCP
............................................

Applicable only if `Fallback C-MOVE SCP <https://dcm4chee-arc-cs.readthedocs.io/en/latest/networking/config/archiveDevice.html#dcmfallbackcmovescp>`_ is configured

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2021-04-07T12:23:11.084+02:00" EventOutcomeIndicator="0">
          <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed" />
       </EventIdentification>
       <ActiveParticipant UserID="MOVESCU" AlternativeUserID="129898" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE2" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.514.212.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
       </ParticipantObjectIdentification>
    </AuditMessage>
