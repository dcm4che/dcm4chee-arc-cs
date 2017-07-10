Application Activity
====================

Trigger Events
--------------
This audit message is emitted when the archive is started or stopped using the archive user interface. Its is also
emitted during archive startup or shutdown.

Message Structure
-----------------

- :ref:`audit-application-activity-event`
- :ref:`audit-application-activity-active-participant-app` (1)
- :ref:`audit-application-activity-active-participant-person` (0..1)
- :ref:`audit-general-message-audit-source`

.. csv-table:: Event: Application Activity
   :name: audit-application-activity-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110100, DCM, 'Application Activity')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "Enumerated Value E = Execute"
         "EventOutcomeIndicator", "M", "'0'⇒'SUCCESS'"
         "EventTypeCode", "M", "DT (110120, DCM, 'Application Start')"
         "", "", "DT (110121, DCM, 'Application Stop')"

.. csv-table:: Active Participant: Application started
   :name: audit-application-activity-active-participant-app
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Application entity titles of Archive Device as ; separated values"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110150, DCM, 'Application')"
         "NetworkAccessPointID", "U", "Hostname of the connection referenced by Audit logger"

.. csv-table:: Active Participant: Person who started the Application
   :name: audit-application-activity-active-participant-person
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Remote IP address for unsecured version of archive; User name for secured version of archive"
         "UserIsRequestor", "M", "true"
         "RoleIDCode", "M", "EV (110151, DCM, 'ApplicationLauncher')"
         "NetworkAccessPointID", "U", "Remote IP address of calling host"

Sample Message
--------------

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2017-07-10T10:30:17.651+02:00" EventOutcomeIndicator="0">

            <EventID csd-code="110100" codeSystemName="DCM" originalText="Application Activity"/>

            <EventTypeCode csd-code="110120" codeSystemName="DCM" originalText="Application Start"/>

        </EventIdentification>

        <ActiveParticipant UserID="DCM4CHEE;DCM4CHEE_ADMIN;DCM4CHEE_TRASH" AlternativeUserID="5289" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">

            <RoleIDCode csd-code="110150" codeSystemName="DCM" originalText="Application"/>

        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">

            <AuditSourceTypeCode csd-code="4"/>

        </AuditSourceIdentification>

    </AuditMessage>

