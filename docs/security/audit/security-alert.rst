Security Alert
==============

Trigger Events
--------------

This message is emitted by the archive in following cases :
- Node authentication failure when establishing a secure communications channel.
- Software Configuration changes done over the UI.

Message Structure
-----------------

.. csv-table:: Entities in Security Alert Audit Message

    :ref:`event-identification-security-alert`
    :ref:`active-participant-initiator-security-alert`
    :ref:`active-participant-archive-security-alert`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-node-security-alert`, Present only in Node authentication failure case
    :ref:`participant-object-ldap-security-alert`, Present only in Software Configuration changes case

.. csv-table:: Event Identification
   :name: event-identification-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110113, DCM, 'Security Alert')"
   EventActionCode, M, | Execute ⇒ 'E'
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'
   EventTypeCode, M, "| Node authentication failure case ⇒ DT (110126, DCM, 'Node Authentication')
   | Software Configuration Changes case ⇒ DT (110131, DCM, 'Software Configuration')"

.. csv-table:: Active Participant: Source
   :name: active-participant-initiator-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Node authentication failure case ⇒ Remote socket address of calling host
   | Software configuration changes done over UI : Secured archive ⇒ 'User name of logged in user'
   | Software configuration changes done over UI : Unsecured archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Node authentication failure case ⇒ EV (110182, DCM, 'Node ID')
   | Software configuration changes done over UI : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Software configuration changes done over UI : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, | Person ⇒ '1'
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, | Archive device name
   UserIDTypeCode, U, "| EV (113877, DCM, 'Device Name')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification
   :name: participant-object-node-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Remote socket address of calling host
   ParticipantObjectTypeCode, M, SystemObject ⇒ '2'
   ParticipantObjectIDTypeCode, M, "EV (110182, DCM, 'Node ID')"

.. csv-table:: Participant Object Identification
   :name: participant-object-ldap-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Name of device being created/updated/deleted
   ParticipantObjectTypeCode, M, SystemObject ⇒ '2'
   ParticipantObjectIDTypeCode, M, "EV (113877, DCM, 'Device Name')"
   ParticipantObjectDetail, M, 'type=Alert Description value=<Base-64 encoded software configuration changes>'

Sample Message
--------------

Node Authentication Failure

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    
        <EventIdentification EventActionCode="E" EventDateTime="2016-06-17T10:35:49.560+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Node Authentication"/>
            <EventOutcomeDescription>null cert chain</EventOutcomeDescription>
        </EventIdentification>
    
        <ActiveParticipant UserID="/127.0.0.1:54404" UserTypeCode="1" UserIsRequestor="true" NetworkAccessPointID="/127.0.0.1:54404" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
    
        <ActiveParticipant UserID="dcm4chee-arc" UserTypeCode="2" AlternativeUserID="3390" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
    
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
    
        <ParticipantObjectIdentification ParticipantObjectID="/127.0.0.1:54404" ParticipantObjectTypeCode="2">
            <ParticipantObjectIDTypeCode csd-code="110182" originalText="Node ID" codeSystemName="DCM"/>
        </ParticipantObjectIdentification>
    
    </AuditMessage>


Software Configuration Changes

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2017-09-22T10:35:49+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="110131" codeSystemName="DCM" originalText="Software Configuration"/>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="dcm4chee-arc" ParticipantObjectTypeCode="2">
            <ParticipantObjectIDTypeCode csd-code="113877" originalText="Device Name" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="Alert Description" value="VSBkaWNvbURldmljZU5hbWU9ZGNtNGNoZWUtYXJjLGNuPURldmljZXMsY249RElDT00gQ29uZmlndXJhdGlvbixkYz1kY200Y2hlLGRjPW9yZwogIGRjbVNlcmllc01ldGFkYXRhUG9sbGluZ0ludGVydmFsOiBbXT0+W1BUMU1dCiAgZGNtQUVDYWNoZVN0YWxlVGltZW91dDogW1BUNU1dPT5bXQogIGRjbUFjY2VwdE1pc3NpbmdQYXRpZW50SUQ6IFtDUkVBVEVdPT5bWUVTXQ=="/>
        </ParticipantObjectIdentification>

    </AuditMessage>