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
         "UserIDTypeCode", "U", "EV ("Cp1640-1","DCM","Local User ID")"
         "UserTypeCode", "U", "'Person' : '1'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "IP address of calling user"
         "NetworkAccessPointTypeCode", "U", "2"

.. csv-table:: Active Participant: Archive application
   :name: audit-user-authentication-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Device name of the archive device"
         "UserIDTypeCode", "U", "EV ("110117","DCM","Archive Device")"
         "UserTypeCode", "U", "'System' : '5'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"


Sample Message
--------------

.. include:: user-authentication.xml
   :code: xml