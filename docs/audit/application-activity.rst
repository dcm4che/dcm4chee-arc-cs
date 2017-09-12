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
- :ref:`audit-application-activity-active-participant-person` (1) - This Active Participant is present only if archive
  was started/stopped from UI.
- :ref:`audit-general-message-audit-source`

.. csv-table:: Event: Application Activity
   :name: audit-application-activity-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110100, DCM, 'Application Activity')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0'⇒'Success'"
         "EventTypeCode", "M", "DT (110120, DCM, 'Application Start')"
         "", "", "DT (110121, DCM, 'Application Stop')"

.. csv-table:: Active Participant: Application started
   :name: audit-application-activity-active-participant-app
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Application entity titles of Archive Device as ; separated values"
         "UserIDTypeCode", "U", "Application startup/shutdown or archive deploy/undeploy : EV ("113877","DCM","Device Name")"
         "", "", "Triggered from UI : EV ("12", "RFC-3881", "URI")"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110150, DCM, 'Application')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Person who started the Application
   :name: audit-application-activity-active-participant-person
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Remote IP address for unsecured version of archive; User name for secured version of archive"
         "UserIDTypeCode", "U", "Secured Archive : EV ("113871","DCM","Person ID")"
         "", "", "Unsecured Archive : EV ("110182","DCM","Node ID")"
         "UserTypeCode", "U", "'Person' : '1'"
         "UserIsRequestor", "M", "true"
         "RoleIDCode", "M", "EV (110151, DCM, 'ApplicationLauncher')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

Sample Message
--------------

.. include:: application-activity.xml
   :code: xml