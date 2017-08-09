Query
=====

Trigger Events
--------------

This message is emitted by the archive for queries triggered by UI or by C-FIND on following levels :

- Patient
- Study
- Series
- Instance
- Modality Worklist Entry

Message Structure
-----------------

- :ref:`audit-query-event`
- :ref:`audit-query-active-participant-source` (1)
- :ref:`audit-query-active-participant-destination` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-query-participant-object-query` (1)

.. csv-table:: Event: Query
   :name: audit-query-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110112, DCM, 'Query')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant: Source
   :name: audit-query-active-participant-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Triggered by C-FIND : 'Calling AE title in association'"
         "", "", "Triggered from UI : 'Remote IP address' or 'User name of logged in user'"
         "UserIsRequestor", "M", "true"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Archive application
   :name: audit-query-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Triggered by C-FIND : 'Called AE title in association'"
         "", "", "Triggered from UI : 'Request URI'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Query (When triggered by C-FIND)
   :name: audit-query-participant-object-query
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "For patient query : '1.2.840.10008.5.1.4.1.2.1.1'"
         "", "", "For study/series/instance query : '1.2.840.10008.5.1.4.1.2.2.1'"
         "", "", "For MWL query : '1.2.840.10008.5.1.4.31'"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectTypeCodeRole", "M", "Enumerated value '3' : 'Report'"
         "ParticipantObjectIDTypeCode", "M", "EV (110181, DCM, 'SOP Class UID')"
         "ParticipantObjectQuery", "M", "Base64 encoded value of Query keys"
         "ParticipantObjectDetail", "MC", "Base64 encoded value for ImplicitVRLittleEndian '1.2.840.10008.1.2' : 'type=TransferSyntax value=MS4yLjg0MC4xMDAwOC4xLjI='"

.. csv-table:: Participant Object Identification: Query (When triggered from UI)
   :name: audit-query-participant-object-query
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "For patient query : 'SearchForPatients'"
         "", "", "For study query : 'SearchForStudies'"
         "", "", "For series query : 'SearchForStudySeries' or 'SearchForSeries'"
         "", "", "For Instance query : 'SearchForInstances' or 'SearchForStudyInstances' or 'SearchForStudySeriesInstances'"
         "", "", "For MWL query : 'SearchForSPS'"
         "ParticipantObjectTypeCode", "M", "'2' : 'SystemObject'"
         "ParticipantObjectTypeCodeRole", "M", "Enumerated value '24' : 'Query'"
         "ParticipantObjectIDTypeCode", "M", "EV (QIDO, 99DCM4CHEE, 'QIDO_Query')"
         "ParticipantObjectQuery", "M", "Base64 encoded value of Request URI plus the Query String"
         "ParticipantObjectDetail", "MC", "Base64 encoded value for 'UTF-8' : 'type=QueryEncoding value=VVRGLTg='"

Sample Message
--------------

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="E" EventDateTime="2017-07-27T09:12:21.331+02:00" EventOutcomeIndicator="0">

            <EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>

        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">

            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source"/>

        </ActiveParticipant>

        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/patients" AlternativeUserID="3390" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">

            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination"/>

        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">

            <AuditSourceTypeCode csd-code="4"/>

        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="SearchForPatients" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
        
            <ParticipantObjectIDTypeCode csd-code="QIDO" originalText="QIDO_Query" codeSystemName="99DCM4CHEE"/>
            
            <ParticipantObjectQuery>L2RjbTRjaGVlLWFyYy9hZXRzL0RDTTRDSEVFL3JzL3BhdGllbnRzaW5jbHVkZWZpZWxkPWFsbCZvZmZzZXQ9MCZsaW1pdD0yMSZvcmRlcmJ5PVBhdGllbnROYW1l</ParticipantObjectQuery>
            
            <ParticipantObjectDetail type="QueryEncoding" value="VVRGLTg="/>
            
        </ParticipantObjectIdentification>

    </AuditMessage>