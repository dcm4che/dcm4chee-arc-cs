Data Export
===========

Trigger Events
--------------

This message is emitted by archive for XDSI `RAD-68 <http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol3.pdf#page=163>`_ transactions.

Message Structure
-----------------

.. csv-table:: Entities in Data Export Audit Message

    :ref:`event-identification-data-export`
    :ref:`active-participant-user-data-export`
    :ref:`active-participant-archive-data-export`
    :ref:`active-participant-destination-data-export`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-patient-data-export`
    :ref:`participant-object-submission-set-data-export`

.. csv-table:: Event Identification
   :name: event-identification-data-export
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110106, DCM, 'Export')"
   EventActionCode, M, | Read : 'R'
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success : '0'
   | Minor failure : '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator : '4'

.. csv-table:: Active Participant: User
   :name: active-participant-user-data-export
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Secured archive : 'User name of logged in user'
   | Unsecured archive : 'Remote IP address'"
   UserIDTypeCode, U, "| Secured archive : EV (113871, DCM, 'Person ID')
   | Unsecured archive : (110182, DCM, 'Node ID')"
   UserTypeCode, U, | Person : '1'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-data-export
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Triggered by scheduler : 'Archive device name'
   | Triggered from UI : 'Invoked URL'"
   UserIDTypeCode, U, "| Triggered by scheduler : EV (113877, DCM, 'Device Name')
   | Triggered from UI : EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | Application : '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, "| Triggered by scheduler : 'true'
   | Triggered by UI : 'false'"
   RoleIDCode, M, "| EV (110153, DCM, 'Source')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Active Participant: Destination
   :name: active-participant-destination-data-export
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, | The URI configured in XDSI Exporter in archive configuration
   UserIDTypeCode, U, "| EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | Application : '2'
   UserIsRequestor, M, | false
   RoleIDCode, M, "| EV (110152, DCM, 'Destination')"
   NetworkAccessPointID, U, | Hostname/IP Address present in the URI configured in XDSI Exporter in archive configuration
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Participant Object Identification: Patient
   :name: participant-object-patient-data-export
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown
   ParticipantObjectTypeCode, M, Person : '1'
   ParticipantObjectTypeCodeRole, M, Patient : '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name

.. csv-table:: Participant Object Identification: Submission Set
   :name: participant-object-submission-set-data-export
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, System generated UID created for the submission set
   ParticipantObjectTypeCode, M, SystemObject : '2'
   ParticipantObjectTypeCodeRole, M, Job : '20'
   ParticipantObjectIDTypeCode, M,  "EV (urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd, IHE XDS Metadata, 'submission set classificationNode')"

Sample Messages
---------------

Scheduler Triggered
^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="R" EventDateTime="2024-08-21T15:23:47.566+02:00" EventOutcomeIndicator="4">
    		<EventID csd-code="110106" codeSystemName="DCM" originalText="Export"/>
    		<EventTypeCode csd-code="ITI-41" codeSystemName="IHE Transactions" originalText="Provide and Register Document Set-b"/>
    		<EventOutcomeDescription>Connection refused</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="xds-i:https://localhost:9443/xdstools4/sim/default__rr/rep/prb" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="55482" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="2.25.223365721262548008523597544488332490265" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="20">
    		<ParticipantObjectIDTypeCode csd-code="urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd" originalText="submission set classificationNode" codeSystemName="IHE XDS Metadata"/>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="MGID001^^^&amp;1.3.6.1.4.1.21367.2005.13.20.1000&amp;ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

REST API Triggered
^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="R" EventDateTime="2024-08-21T15:16:17.167+02:00" EventOutcomeIndicator="4">
    		<EventID csd-code="110106" codeSystemName="DCM" originalText="Export"/>
    		<EventTypeCode csd-code="ITI-41" codeSystemName="IHE Transactions" originalText="Provide and Register Document Set-b"/>
    		<EventOutcomeDescription>Connection refused</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="xds-i:https://localhost:9443/xdstools4/sim/default__rr/rep/prb" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.113654.1.2001.30/export/Export%20to%20XDS" AlternativeUserID="30068" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="2.25.90506177536913613461428105264555596916" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="20">
    		<ParticipantObjectIDTypeCode csd-code="urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd" originalText="submission set classificationNode" codeSystemName="IHE XDS Metadata"/>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="CR3^^^&amp;1.3.6.1.4.1.21367.2005.13.20.1000&amp;ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>CRTHREE^PAUL</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>