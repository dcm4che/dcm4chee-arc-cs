Audit Log Used
==============

Trigger Events
--------------

This message is emitted by the archive when the audit record repository is accessed over archive proxy.

Message Structure
-----------------

.. csv-table:: Entities in Audit Log Used Audit Message

    :ref:`event-identification-audit-log-used`
    :ref:`active-participant-user-audit-log-used`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-audit-log-used`

.. csv-table:: Event Identification
   :name: event-identification-audit-log-used
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "EV (110101, DCM, 'Audit Log Used')"
   EventActionCode, M, Execute ⇒ 'E'
   EventDateTime, M, The time at which the event occurred
   EventOutcomeIndicator, M, Success ⇒ '0'

.. csv-table:: Active Participant: User
   :name: active-participant-user-audit-log-used
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Secured version of archive ⇒ 'Logged in User name'
   | Unsecured version of archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Secured Archive ⇒ EV (113871, DCM, 'Person ID')
   | Unsecured Archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, | Person ⇒ '1'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification
   :name: participant-object-audit-log-used
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Audit Record Repository URL configured on archive device level
   ParticipantObjectTypeCode, M, SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, SecurityResource ⇒ '13'
   ParticipantObjectIDTypeCode, M,  "EV (12, RFC-3881, 'URI')"
   ParticipantObjectName, U, Security Audit Log

Sample Message
--------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="R" EventDateTime="2017-01-27T14:46:32.670+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110101" codeSystemName="DCM" originalText="Audit Log Used"/>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserTypeCode="1" AlternativeUserID="5312" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="http://archive2:5601" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="13">
            <ParticipantObjectIDTypeCode csd-code="12" originalText="URI" codeSystemName="RFC-3881" />
            <ParticipantObjectName>Security Audit Log</ParticipantObjectName>
        </ParticipantObjectIdentification>

    </AuditMessage>