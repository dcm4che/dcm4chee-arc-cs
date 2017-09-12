Audit Log Used
==============

Trigger Events
--------------

This message is emitted by the archive when the audit record repository is accessed over archive proxy.

Message Structure
-----------------

- :ref:`audit-audit-log-used-event`
- :ref:`audit-audit-log-used-active-participant-source` (1)
- :ref:`audit-audit-log-used-participant-object` (1)

.. csv-table:: Event: Audit Log Used
   :name: audit-audit-log-used-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110101, DCM, 'Audit Log Used')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success'"

.. csv-table:: Active Participant: Source
   :name: audit-audit-log-used-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Remote IP Address or User name of logged in user"
         "UserIDTypeCode", "U", "Secured Archive : EV ("113871","DCM","Person ID")"
         "", "", "Unsecured Archive : EV ("110182","DCM","Node ID")"
         "UserTypeCode", "U", "'Person' : '1'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification
   :name: audit-audit-log-used-participant-object
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Audit Record Repository URL configured on archive device level"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectTypeCodeRole", "M", "'13' : 'SecurityResource'"
         "ParticipantObjectIDTypeCode", "M", "EV (12, RFC-3881, 'URI')"
         "ParticipantObjectName", "U", "Security Audit Log"

Sample Message
--------------

.. include:: audit-log-used.xml
   :code: xml