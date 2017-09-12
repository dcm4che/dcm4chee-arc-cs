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
         "UserIDTypeCode", "U", "EV ("110182","DCM","Node ID")"
         "UserTypeCode", "U", "'Person' : '1'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Remote socket address of calling host"
         "NetworkAccessPointTypeCode", "U", "2"

.. csv-table:: Active Participant: Archive application
   :name: audit-security-alert-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Semicolon separated Application Entity Titles of the device"
         "UserIDTypeCode", "U", "EV ("110118","DCM","Archive Device AE Titles")"
         "UserTypeCode", "U", "'System' : '5'"
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

.. include:: security-alert.xml
   :code: xml