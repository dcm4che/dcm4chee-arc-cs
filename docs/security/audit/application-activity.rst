Application Activity
====================

This audit message describes the event of an archive application starting or stopping.

Trigger Events
--------------
This audit message is emitted when the archive is started or stopped using the archive user interface. It is also
emitted during archive startup or shutdown.

Message Structure
-----------------

.. csv-table:: Application Activity Message
   :name: application-activity
   :widths: 15, 15, 2, 45, 15
   :header: Real World Entities, Field Name, Opt, Value Constraints, Note

   Event, Event ID, M, "| EV (110100, DCM, 'Application Activity')",
   , Event Action Code, M, E (= Execute),
   , Event Date Time, M, , The time at which the event occurred
   , Event Outcome Indicator, M, 0 (= Success),
   , Event Type Code, M, "| DT (110120, DCM, 'Application Start')
   | OR
   | DT (110121, DCM, 'Application Stop')", "| - Applicable on **startup** of archive.
   |
   | - Applicable on **shutdown** of archive"
   "| Active Participant:
   | Application started (1)", User ID, M, "| Device Name of archive
   | OR
   | `Start Archive <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/CTRL-RS/start>`_ request URL
   | OR
   | `Stop Archive <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/CTRL-RS/stop>`_ request URL", "| - Applicable on **startup / shutdown** of archive by a **process**
   |
   | - Applicable on **startup** of archive using **REST service**
   |
   | - Applicable on **shutdown** of archive using **REST service**"
   , User ID Type Code, U, "| EV (113877, DCM, 'Device Name')
   | OR
   | EV (12, RFC-3881, 'URI')", "| - Application startup/shutdown of archive by a process
   |
   | - Applicable on startup / shutdown of archive using REST service"
   , User Type Code, U, 2 (= Application),
   , Alternative User ID, MC, , Process ID of Audit logger
   , User Is Requestor, M, "| true
   | OR
   | false",  "| - Application **startup / shutdown** of archive by a **process**
   |
   | - Applicable on **startup / shutdown** of archive using **REST service**"
   , Role ID Code, M, "| EV (110150, DCM, 'Application')",
   , Network Access Point ID, U, , Hostname/IP Address of the connection referenced by Audit logger
   , Network Access Point Type Code, U, "| 1 (= Machine name)
   | OR
   | 2 (= IP Address)", "| - Applicable if NetworkAccessPointID is a **hostname**
   |
   | - Applicable if NetworkAccessPointID is an **IP Address**"
   "| Active Participant:
   | Persons and or processes that started the Application (0..N)
   |
   | Applicable only if archive **startup / shutdown** done using **REST service**", User ID, M, "| User Name
   | Remote IP Address", "| - Applicable for **Secured version of archive**
   |
   | - Applicable for **Unsecured version of archive**"
   , User ID Type Code, U, "| EV (113871, DCM, 'Person ID')
   | EV (110182, DCM, 'Node ID')", "| - Applicable for **Secured version of archive**
   |
   | - Applicable for **Unsecured version of archive**"
   , User Type Code, U, "| 1 (= Person)
   | OR
   | 2 (= Application)", "| - Applicable for **Secured version of archive**
   |
   | - Applicable for **Unsecured version of archive**"
   , User Is Requestor, M, true,
   , RoleIDCode, M, "| EV (110151, DCM, 'Application Launcher')",
   , Network Access Point ID, U, , Hostname/IP Address of calling host
   , Network Access Point Type Code, U, "| 1 (= Machine name)
   | OR
   | 2 (= IP Address)", "| - Applicable if NetworkAccessPointID is a **hostname**
   |
   | - Applicable if NetworkAccessPointID is an **IP Address**"

Sample Messages
---------------

Application Activity Message - Application Start
................................................

Startup of archive / Deploy archive ear file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2023-11-14T17:06:12.209+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110100" codeSystemName="DCM" originalText="Application Activity"/>
    		<EventTypeCode csd-code="110120" codeSystemName="DCM" originalText="Application Start"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="38551" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110150" codeSystemName="DCM" originalText="Application"/>
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>

Archive Startup by REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Triggered by external client or user logged in to archive UI

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2023-11-14T17:14:44.048+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110100" codeSystemName="DCM" originalText="Application Activity"/>
    		<EventTypeCode csd-code="110120" codeSystemName="DCM" originalText="Application Start"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="/dcm4chee-arc/ctrl/start" AlternativeUserID="40918" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110150" codeSystemName="DCM" originalText="Application"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<RoleIDCode csd-code="110151" codeSystemName="DCM" originalText="Application Launcher"/>
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>

Application Activity Message - Application Stop
...............................................

Shutdown of archive / Undeploy archive ear file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2023-11-14T17:08:46.221+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110100" codeSystemName="DCM" originalText="Application Activity"/>
    		<EventTypeCode csd-code="110121" codeSystemName="DCM" originalText="Application Stop"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110150" codeSystemName="DCM" originalText="Application"/>
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>

Archive Stop using REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Triggered by external client or user logged in to archive UI

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2023-11-14T17:14:42.628+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110100" codeSystemName="DCM" originalText="Application Activity"/>
    		<EventTypeCode csd-code="110121" codeSystemName="DCM" originalText="Application Stop"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="/dcm4chee-arc/ctrl/stop" AlternativeUserID="40918" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110150" codeSystemName="DCM" originalText="Application"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<RoleIDCode csd-code="110151" codeSystemName="DCM" originalText="Application Launcher"/>
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>