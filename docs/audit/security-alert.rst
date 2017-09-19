Security Alert
==============

Trigger Events
--------------

This message describes any event for which a node needs to report a security alert, e.g., a node authentication failure
when establishing a secure communications channel.

Message Structure
-----------------

.. csv-table:: Supported Entities in Security Alert Audit Message

    :ref:`event-identification-security-alert`
    :ref:`active-participant-initiator-security-alert`
    :ref:`active-participant-archive-security-alert`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-security-alert`

.. csv-table:: Event Identification
   :name: event-identification-security-alert
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110113, DCM, 'Node Authentication')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message"

.. csv-table:: Active Participant: Source
   :name: active-participant-initiator-security-alert
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Remote socket address of calling host"
         "UserIDTypeCode", "U", "EV (110182, DCM, 'Node ID')"
         "UserTypeCode", "U", "'Person' : '1'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Remote socket address of calling host"
         "NetworkAccessPointTypeCode", "U", "2"

.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-security-alert
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Archive device name"
         "UserIDTypeCode", "U", "EV (113877, DCM, 'Device Name')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification
   :name: participant-object-security-alert
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Remote socket address of calling host"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectIDTypeCode", "M", "EV (110182, DCM, 'Node ID')"

Sample Message
--------------

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