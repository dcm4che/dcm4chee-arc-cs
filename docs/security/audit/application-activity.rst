Application Activity
====================

Trigger Events
--------------
This audit message is emitted when the archive is started or stopped using the archive user interface. It is also
emitted during archive startup or shutdown.

Message Structure
-----------------

.. csv-table:: Application Activity Message
   :name: application-activity
   :widths: 25, 30, 5, 40, 10
   :header: Real World Entities, Field Name, Opt, Value Constraints, Note

   Event, EventID, M, EV (110100, DCM, 'Application Activity'),
   , EventActionCode, M, E (= Execute),
   , EventDateTime, M, , The time at which the event occurred
   , EventOutcomeIndicator, M, 0 (= Success),
   , EventTypeCode, M, "| DT (110120, DCM, 'Application Start')
   | DT (110121, DCM, 'Application Stop')", "| Applicable on startup of archive
   | Applicable on shutdown of archive"

Sample Message
--------------

Application Activity Message - Application Start - Startup of archive / Deploy archive ear file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2023-11-14T17:09:15.082+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110100" codeSystemName="DCM" originalText="Application Activity"/>
    		<EventTypeCode csd-code="110120" codeSystemName="DCM" originalText="Application Start"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110150" codeSystemName="DCM" originalText="Application"/>
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>

Application Activity Message - Application Start - Using REST service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    	<ActiveParticipant UserID="127.0.0.1" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<RoleIDCode csd-code="110151" codeSystemName="DCM" originalText="Application Launcher"/>
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>

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
    	<ActiveParticipant UserID="admin" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<RoleIDCode csd-code="110151" codeSystemName="DCM" originalText="Application Launcher"/>
    		<UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>

Application Activity Message - Application Stop - Shutdown of archive / Undeploy archive ear file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Application Activity Message - Application Stop - Using REST service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    	<ActiveParticipant UserID="127.0.0.1" AlternativeUserID="40918" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<RoleIDCode csd-code="110151" codeSystemName="DCM" originalText="Application Launcher"/>
    		<UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    </AuditMessage>