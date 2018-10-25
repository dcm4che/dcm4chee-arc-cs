Security Alert
==============

Trigger Events
--------------

This message is emitted by the archive in following cases :
- Connection Events Failure : Node authentication failure when establishing a secure communications channel.
- Connection Events Failure : TCP Connection to remote hosts failure.
- Association Events Failure : Associations rejected by Archive.
- Association Events Failure : Association initiation to remote AEs failed.
- Software Configuration changes done over the UI.
- One or more task(s) were canceled, rescheduled or deleted using Monitoring page of Archive UI.
- If a super user logs in or logs out of secured Archive UI.
- If any user updates his/her password using secured Archive UI.

Message Structure
-----------------

.. csv-table:: Entities in Security Alert Audit Message

    :ref:`event-identification-security-alert`
    :ref:`active-participant-initiator-security-alert`
    :ref:`active-participant-archive-security-alert`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-ldap-security-alert`, Present only in Software Configuration changes case
    :ref:`participant-object-task-security-alert`, Present only in Cancel/Reschedule/Delete task case
    :ref:`participant-object-tasks-security-alert`, Present only in Cancel/Reschedule/Delete tasks case

.. csv-table:: Event Identification
   :name: event-identification-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110113, DCM, 'Security Alert')"
   EventActionCode, M, | Execute ⇒ 'E'
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'
   EventTypeCode, M, "| Connection Events Failure case ⇒ DT (110126, DCM, 'Node Authentication')
   | Association Events Failure case ⇒ DT (ASSOCIATION-FAILURE, 99DCM4CHEE, 'Association Failure')
   | Software Configuration Changes case ⇒ DT (110131, DCM, 'Software Configuration')
   | Super User Login case ⇒ DT (110127, DCM, 'Emergency Override Started')
   | Super User Logout case ⇒ DT (110138, DCM, 'Emergency Override Stopped')
   | User Password update case ⇒ DT (110137, DCM, 'User security Attributes Changed')
   | Cancel Task(s) case ⇒ DT (CANCEL, 99DCM4CHEE, 'Cancel Task')
   | Reschedule Task(s) case ⇒ DT (RESCHEDULE, 99DCM4CHEE, 'Reschedule Task')
   | Delete Task(s) case ⇒ DT (DELETE, 99DCM4CHEE, 'Delete Task')"

.. csv-table:: Active Participant: Source
   :name: active-participant-initiator-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Connection Events Failure case ⇒ Remote socket address of calling host
   | Association Events Failure case ⇒ 'AE title of remote side used in association'
   | Super user login or logout using Secured archive ⇒ 'User name of logged in user'
   | Password Update of User using Secured archive ⇒ 'User name of logged in user'
   | Cancel, Reschedule or Delete Task(s) : Secured archive ⇒ 'User name of logged in user'
   | Cancel, Reschedule or Delete Task(s) : Unsecured archive ⇒ 'Remote IP address'
   | Software configuration changes done over UI : Secured archive ⇒ 'User name of logged in user'
   | Software configuration changes done over UI : Unsecured archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Connection Events Failure case ⇒ EV (110182, DCM, 'Node ID')
   | Association Events Failure ⇒ EV (110119, DCM, 'Station AE Title')
   | Super user login or logout using Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Password Update of User using Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Cancel, Reschedule or Delete Task(s) : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Cancel, Reschedule or Delete Task(s) : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')
   | Software configuration changes done over UI : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Software configuration changes done over UI : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, | Person ⇒ '1'
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Association Events Failure case ⇒ AE title of Archive used in Association
   | Cancel, Reschedule or Delete Task(s) and Software Configuration Changes case ⇒ RESTful service invoked of Archive
   | For all other cases ⇒ Archive device name"
   UserIDTypeCode, U, "| Association Events Failure case ⇒ EV (110119, DCM, 'Station AE Title')
   | Cancel, Reschedule or Delete Task(s) and Software Configuration Changes case ⇒ EV (12, RFC-3881, 'URI')
   | For all other cases ⇒ EV (113877, DCM, 'Device Name')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification
   :name: participant-object-ldap-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Name of device being created/updated/deleted
   ParticipantObjectTypeCode, M, SystemObject ⇒ '2'
   ParticipantObjectIDTypeCode, M, "EV (113877, DCM, 'Device Name')"
   ParticipantObjectDetail, M, 'type=Alert Description value=<Base-64 encoded software configuration changes>'

.. csv-table:: Participant Object Identification
   :name: participant-object-task-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Name of device being created/updated/deleted
   ParticipantObjectTypeCode, M, SystemObject ⇒ '2'
   ParticipantObjectIDTypeCode, M, "EV (TASK, 99DCM4CHEE, 'Archive Task')"
   ParticipantObjectDetail, M, 'type=Task value=<Base-64 encoded complete queue message>'

.. csv-table:: Participant Object Identification
   :name: participant-object-tasks-security-alert
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Name of device being created/updated/deleted
   ParticipantObjectTypeCode, M, SystemObject ⇒ '2'
   ParticipantObjectIDTypeCode, M, "EV (TASKS, 99DCM4CHEE, 'Archive Tasks')"
   ParticipantObjectDetail, M, "| 'type=Count value=<Base-64 encoded count of total Canceled/Rescheduled/Deleted tasks>'
   | If filter(s) set on service invoke ⇒ 'type=Filters value=<Base-64 encoded query params used for Cancel/Reschedule/Delete tasks service>'"

Sample Message
--------------

Connection Events Failure

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
    
    </AuditMessage>


Associations Events Failure

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2018-10-23T15:33:19.804+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="ASSOCIATION-FAILURE" codeSystemName="99DCM4CHEE" originalText="Association Failure"/>
            <EventOutcomeDescription>A-ASSOCIATE-RJ[result: 1 - rejected-permanent, source: 1 - service-user, reason: 3 - calling-AE-title-not-recognized]</EventOutcomeDescription>
        </EventIdentification>

        <ActiveParticipant UserID="STGCMTSCU1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

    </AuditMessage>

Software Configuration Changes

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2017-09-22T10:35:49+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="110131" codeSystemName="DCM" originalText="Software Configuration"/>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="dcm4chee-arc" ParticipantObjectTypeCode="2">
            <ParticipantObjectIDTypeCode csd-code="113877" originalText="Device Name" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="Alert Description" value="VSBkaWNvbURldmljZU5hbWU9ZGNtNGNoZWUtYXJjLGNuPURldmljZXMsY249RElDT00gQ29uZmlndXJhdGlvbixkYz1kY200Y2hlLGRjPW9yZwogIGRjbVNlcmllc01ldGFkYXRhUG9sbGluZ0ludGVydmFsOiBbXT0+W1BUMU1dCiAgZGNtQUVDYWNoZVN0YWxlVGltZW91dDogW1BUNU1dPT5bXQogIGRjbUFjY2VwdE1pc3NpbmdQYXRpZW50SUQ6IFtDUkVBVEVdPT5bWUVTXQ=="/>
        </ParticipantObjectIdentification>

    </AuditMessage>


User Password Update

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="U" EventDateTime="2018-09-18T17:42:55.226+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="110137" codeSystemName="DCM" originalText="User security Attributes Changed"/>
        </EventIdentification>

        <ActiveParticipant UserID="admin" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="31064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

    </AuditMessage>


Super User Login

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2018-09-18T17:42:55.226+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="110127" codeSystemName="DCM" originalText="Emergency Override Started"/>
        </EventIdentification>

        <ActiveParticipant UserID="admin" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="31064" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

    </AuditMessage>


Cancel Export Task

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2018-01-29T13:54:56.838+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="CANCEL" codeSystemName="99DCM4CHEE" originalText="Cancel Message"/>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="/dcm4chee-arc/monitor/export/51/cancel" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="ID:fb45eabd-04f2-11e8-8a74-7c5cf82aac4c" ParticipantObjectTypeCode="2">
            <ParticipantObjectIDTypeCode csd-code="TASK" originalText="Archive Task" codeSystemName="99DCM4CHEE"/>
            <ParticipantObjectDetail type="Task" value="eyJpZCI6IklEOmZiNDVlYWJkLTA0ZjItMTFlOC04YTc0LTdjNWNmODJhYWM0YyIsInF1ZXVlIjoiRXhwb3J0MSIsInByaW9yaXR5Ijo0LCJjcmVhdGVkVGltZSI6IjIwMTgtMDEtMjlUMTM6NDg6MDQuNjQ3KzAxMDAiLCJ1cGRhdGVkVGltZSI6IjIwMTgtMDEtMjlUMTM6NTQ6NTYuODM0KzAxMDAiLCJkaWNvbURldmljZU5hbWUiOiJkY200Y2hlZS1hcmMiLCJzdGF0dXMiOiJDQU5DRUxFRCIsImZhaWx1cmVzIjoxLCJzY2hlZHVsZWRUaW1lIjoiMjAxOC0wMS0yOVQxMzo1MDo1Ny45MDYrMDEwMCIsInByb2Nlc3NpbmdTdGFydFRpbWUiOiIyMDE4LTAxLTI5VDEzOjUwOjU3LjkxNSswMTAwIiwicHJvY2Vzc2luZ0VuZFRpbWUiOiIyMDE4LTAxLTI5VDEzOjUwOjU4LjA4NiswMTAwIiwiZXJyb3JNZXNzYWdlIjoiamF2YS5uZXQuQ29ubmVjdEV4Y2VwdGlvbjogQ29ubmVjdGlvbiByZWZ1c2VkIChDb25uZWN0aW9uIHJlZnVzZWQpIiwib3V0Y29tZU1lc3NhZ2UiOiJFeHBvcnQgU3R1ZHlbdWlkPTEuMi44NDAuMTEzNjc0LjExMTguNTQuMjAwXSB0byBBRTogU1RPUkVTQ1AxIC0gY29tcGxldGVkOjE4IiwiQUVUaXRsZSI6IkRDTTRDSEVFIiwiUmVxdWVzdGVySG9zdE5hbWUiOiIxMjcuMC4wLjEiLCJSZXF1ZXN0ZXJVc2VySUQiOiIxMjcuMC4wLjEiLCJSZXF1ZXN0VVJJIjoiL2RjbTRjaGVlLWFyYy9hZXRzL0RDTTRDSEVFL3JzL3N0dWRpZXMvMS4yLjg0MC4xMTM2NzQuMTExOC41NC4yMDAvZXhwb3J0L1NUT1JFU0NQIiwiU3R1ZHlJbnN0YW5jZVVJRCI6IjEuMi44NDAuMTEzNjc0LjExMTguNTQuMjAwIiwiRXhwb3J0ZXJJRCI6IlNUT1JFU0NQMSJ9"/>
        </ParticipantObjectIdentification>

    </AuditMessage>

Delete Export Tasks

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2018-10-24T17:06:24.727+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110113" codeSystemName="DCM" originalText="Security Alert"/>
            <EventTypeCode csd-code="DELETE" codeSystemName="99DCM4CHEE" originalText="Delete Task"/>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="/dcm4chee-arc/monitor/export" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="DeleteTasks" ParticipantObjectTypeCode="2">
            <ParticipantObjectIDTypeCode csd-code="TASKS" originalText="Archive Tasks" codeSystemName="99DCM4CHEE"/>
            <ParticipantObjectDetail type="Filters" value="c3RhdHVzPUNPTVBMRVRFRA=="/>
            <ParticipantObjectDetail type="Count" value="Mg=="/>
        </ParticipantObjectIdentification>

    </AuditMessage>