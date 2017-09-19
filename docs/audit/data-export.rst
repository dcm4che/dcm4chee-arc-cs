Data Export
===========

Trigger Events
--------------

This message is emitted by archive for XDSI `RAD-68 <http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol3.pdf#page=163>`_ transactions.

Message Structure
-----------------

.. csv-table:: Supported Entities in Data Export Audit Message

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
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110106, DCM, 'Export')"
         "EventActionCode", "M", "Enumerated Value R = Read"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant: Archive application
   :name: active-participant-user-data-export
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Secured archive : User name for secured version of archive"
         "", "", "Unsecured archive : Remote IP address for unsecured version of archive"
         "UserIDTypeCode", "U", "Secured archive : EV (113871, DCM, 'Person ID')"
         "", "", "Unsecured archive : (110182, DCM, 'Node ID')"
         "UserTypeCode", "U", "'Person' : '1'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-data-export
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Triggered by scheduler : Archive device name"
         "", "", "Triggered from UI : Invoked URL"
         "UserIDTypeCode", "U", "Triggered by scheduler : EV (113877, DCM, 'Device Name')"
         "", "", "Triggered from UI : EV (12, RFC-3881, 'URI')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "Triggered by scheduler : 'true'"
         "", "", "Triggered by UI : 'false'"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Destination
   :name: active-participant-destination-data-export
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "The URI configured in XDSI Exporter in archive configuration"
         "UserIDTypeCode", "U", "EV (12, RFC-3881, 'URI')"
         "UserTypeCode", "U", "'Application' : '2'"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address present in the URI configured in XDSI Exporter in archive configuration"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Patient
   :name: participant-object-patient-data-export
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' : 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' : 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"

.. csv-table:: Participant Object Identification: Submission Set
   :name: participant-object-submission-set-data-export
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "System generated UID created for the submission set"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectTypeCodeRole", "M", "'20' : 'Job'"
         "ParticipantObjectIDTypeCode", "M", "EV (urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd, IHE XDS Metadata, 'submission set classificationNode')"

Sample Message
--------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    
        <EventIdentification EventActionCode="R" EventDateTime="2017-03-20T14:17:40.947+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110106" codeSystemName="DCM" originalText="Export"/>
            <EventTypeCode csd-code="ITI-41" codeSystemName="IHE Transactions" originalText="Provide and Register Document Set-b"/>
        </EventIdentification>
    
        <ActiveParticipant UserID="dcm4chee-arc" UserTypeCode="2" AlternativeUserID="60928" UserIsRequestor="true" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source"/>
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
    
        <ActiveParticipant UserID="xds-i:http://localhost:8081/xdstools4/sim/pacs__rr/rep/prb" UserTypeCode="2" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
    
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
    
        <ParticipantObjectIdentification ParticipantObjectID="IDS-AD001-a^^^&1.3.6.1.4.1.21367.2005.13.20.1000&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
        </ParticipantObjectIdentification>
    
        <ParticipantObjectIdentification ParticipantObjectID="2.25.177992962309009308855419466022084866557" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="20">
            <ParticipantObjectIDTypeCode csd-code="urn:uuid:a54d6aa5-d40d-43f9-88c5-b4633d873bdd" originalText="submission set classificationNode" codeSystemName="IHE XDS Metadata"/>
        </ParticipantObjectIdentification>
    
    </AuditMessage>