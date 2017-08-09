User Authentication
===================

Trigger Events
--------------

This message is sent if the archive is secured with Keycloak. The trigger events for this message are :
- Login
- Login Error
- Logout
- Logout Error

Message Structure
-----------------

- :ref:`audit-user-authentication-event`
- :ref:`audit-user-authentication-active-participant-source` (1)
- :ref:`audit-user-authentication-active-participant-destination` (1)

.. csv-table:: Event: User Authentication
   :name: audit-user-authentication-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "For LOGIN events : EV (110122, DCM, 'Login')"
         "", "", "For LOGOUT events : EV (110123, DCM, 'Logout')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant: Source
   :name: audit-user-authentication-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "User name of logged in user"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "IP address of calling user"
         "NetworkAccessPointTypeCode", "U", "2"

.. csv-table:: Active Participant: Archive application
   :name: audit-user-authentication-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Device name of the archive device"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"


Sample Message
--------------

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2017-01-26T17:28:59.553+01:00" EventOutcomeIndicator="0">

            <EventID csd-code="110122" codeSystemName="DCM" originalText="Login"/>

        </EventIdentification>

        <ActiveParticipant UserID="admin" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2" />

        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="3390" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1" />

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">

            <AuditSourceTypeCode csd-code="4"/>

        </AuditSourceIdentification>

    </AuditMessage>