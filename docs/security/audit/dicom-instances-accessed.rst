DICOM Instances Accessed
========================

Trigger Events
--------------

This message is emitted by the archive in following cases :

- Some objects / series of study are rejected using UI
- Some objects / series of study are rejected in an external archive using UI
- Rejection Notes for some objects of a study are stored to the archive using `RAD-66 <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol3.pdf#page=159>`_ transaction.
- Objects are retrieved from an external archive by HL7 Prefetch Scheduler
- Update study/series expiration date using UI / Study Retention Policy / HL7 Study Retention Policy.
- Update study attributes using UI.
- Previous series/instances of a study are deleted on subsequent receive of objects having same SOP IUID but different Series IUID
- Scheduler triggered study size & query attributes calculation

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
   | Update study / series expiration date ⇒ 'Base-64 encoded expiration date (7777,1023)',"
   ParticipantObjectDescription, U, , Not present for scheduler triggered study size & query attributes calculation
   SOPClass, MC, Rejection / Deletion case ⇒ Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>, Not present for scheduler triggered study size & query attributes calculation
   Accession, U, Accession Number, Not present for scheduler triggered study size & query attributes calculation
   ParticipantObjectDataLifeCycle, U, "| Scheduler triggered study size & query attributes calculation case : AggregationSummarizationDerivation ⇒ '8'

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-instances-accessed
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

        <EventIdentification EventActionCode="D" EventDateTime="2017-07-17T11:24:42.320+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.392.200036.9125.0.199402091242.1/series/1.2.392.200036.9125.0.199402091242.1/reject/113039%5EDCM"
           AlternativeUserID="2716" UserIsRequestor="false" NetworkAccessPointID="localhost" UserTypeCode="2" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.199402091242.1"
            ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="P5^^^ISSUER" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TEST^Name</ParticipantObjectName>
        </ParticipantObjectIdentification>

    </AuditMessage>