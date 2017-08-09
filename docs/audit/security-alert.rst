Security Alert
==============

Trigger Events
--------------

This message describes any event for which a node needs to report a security alert, e.g., a node authentication failure
when establishing a secure communications channel.

Message Structure
-----------------

- :ref:`audit-security-alert-event`
- :ref:`audit-security-alert-active-participant-source` (1)
- :ref:`audit-security-alert-active-participant-destination` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-security-alert-participant-object` (1)

.. csv-table:: Event: Security Alert
   :name: audit-security-alert-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110113, DCM, 'Node Authentication')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message"

.. csv-table:: Active Participant: Source
   :name: audit-security-alert-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Remote socket address of calling host"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Remote socket address of calling host"
         "NetworkAccessPointTypeCode", "U", "2"

.. csv-table:: Active Participant: Archive application
   :name: audit-security-alert-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Semicolon separated Application Entity Titles of the device"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification
   :name: audit-security-alert-participant-object
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Remote socket address of calling host"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectIDTypeCode", "M", "EV (110182, DCM, 'Node ID')"

Sample Message
--------------

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2016-06-17T10:35:49.560+02:00" EventOutcomeIndicator="4">

            <EventID csd-code="110113" codeSystemName="DCM" originalText="Node Authentication"/>

            <EventOutcomeDescription>null cert chain</EventOutcomeDescription>

        </EventIdentification>

        <ActiveParticipant UserID="/127.0.0.1:54404" UserIsRequestor="true" NetworkAccessPointID="/127.0.0.1:54404" NetworkAccessPointTypeCode="2" />

        <ActiveParticipant UserID="DCM4CHEE;DCM4CHEE_ADMIN;DCM4CHEE_TRASH" AlternativeUserID="3390" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1" />

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">

            <AuditSourceTypeCode csd-code="4"/>

        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="/127.0.0.1:54404" ParticipantObjectTypeCode="2">

            <ParticipantObjectIDTypeCode csd-code="110182" originalText="Node ID" codeSystemName="DCM"/>

        </ParticipantObjectIdentification>

    </AuditMessage>