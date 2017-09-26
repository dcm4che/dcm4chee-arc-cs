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

.. csv-table:: Entities in User Authentication Audit Message

    :ref:`event-identification-user-authentication`
    :ref:`active-participant-initiator-user-authentication`
    :ref:`active-participant-archive-user-authentication`
    :ref:`audit-general-message-audit-source`

.. csv-table:: Event Identification
   :name: event-identification-user-authentication
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| For LOGIN events ⇒ EV (110122, DCM, 'Login')
   | For LOGOUT events ⇒ EV (110123, DCM, 'Logout')"
   EventActionCode, M, | Execute ⇒ 'E'
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'

.. csv-table:: Active Participant: Source
   :name: active-participant-initiator-user-authentication
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, User name of logged in user
   UserIDTypeCode, U, "EV (113871, DCM, 'Person ID')"
   UserTypeCode, U, Person ⇒ '1'
   UserIsRequestor, M, true
   NetworkAccessPointID, U, IP address of calling user
   NetworkAccessPointTypeCode, U, 2

.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-user-authentication
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, | Device name of the archive device
   UserIDTypeCode, U, "| EV (113877, DCM, 'Device Name')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

Sample Message
--------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    
        <EventIdentification EventActionCode="E" EventDateTime="2017-01-26T17:28:59.553+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110122" codeSystemName="DCM" originalText="Login"/>
        </EventIdentification>
    
        <ActiveParticipant UserID="admin" UserTypeCode="1" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person ID"/>
        </ActiveParticipant>
    
        <ActiveParticipant UserID="dcm4chee-arc" UserTypeCode="2" AlternativeUserID="3390" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
    
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
    
    </AuditMessage>