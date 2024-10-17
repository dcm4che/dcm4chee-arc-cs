Query
=====

Trigger Events
--------------

This message is emitted by the archive for queries triggered by archive UI / REST APIs or by C-FIND on following levels :

- Patient
- Study
- Series
- Instance
- Modality Worklist Entry
- Modality Performed Procedure Step
- Unified Worklist

Additionally, this message is also emitted if a Patient Demographics Query is invoked by the archive acting as a Patient
Demographics Consumer to a Patient Demographics Supplier supporting patient demographics query, like

- HL7 Patient Demographics Supplier supporting `Patient Demographics Query [ITI-21] - QBP^Q22 HL7 messages <https://profiles.ihe.net/ITI/TF/Volume2/ITI-21.html>`_
- FHIR Patient Demographics Supplier supporting `Mobile Patient Demographics Query [ITI-78] <https://profiles.ihe.net/ITI/PDQm/ITI-78.html>`_

Message Structure
-----------------

.. csv-table:: Query Message
   :name: query
   :widths: 15, 15, 2, 45, 15
   :header: Real World Entities, Field Name, Opt, Value Constraints, Note

   Event, Event ID, M, "| EV (110112, DCM, 'Query')",
   , Event Action Code, M, E (= Execute),
   , Event Date Time, M, , The time at which the event occurred
   , Event Outcome Indicator, M, "| 0 (= Success)
   | OR
   | 4 (= Minor Failure)", "| - Default indicator for DICOM C-FIND / REST triggered DICOM entities' queries or if patient demographics were not found at HL7 PDQ / FHIR PDQ suppliers
   |
   | - Only applicable for HL7 PDQ or FHIR PDQ queries, if patient demographics were not found at PDQ supplier"
   , Event Outcome Description, U, Querying the PDQ Service for patient identifier was unsuccessful, Applicable only in HL7 PDQ or FHIR PDQ queries, if patient demographics were not found at PDQ supplier
   , Event Type Code, U, "| DT ('ITI-21', 'IHE Transactions', 'Patient Demographics Query')
   | OR
   | DT ('ITI-78', 'urn:ihe:event-type-code', 'Mobile Patient Demographics Query')", "| - Only applicable for HL7 PDQ queries
   |
   | - Only applicable for FHIR PDQ queries"
   Participating Object - Query, Participating Object ID, U, "| SearchForStudies (See [#Note1]_)
   | OR
   | 1.2.840.10008.5.1.4.1.2.2.1 (See [#Note2]_)
   | OR
   | PatientVerificationScheduler
   | OR
   | QueryPatientDemographics", "| - Only applicable for REST triggered DICOM entities' queries (See [#Note1]_)
   |
   | - Only applicable for DICOM C-FIND queries (See [#Note2]_)
   |
   | - Only applicable for scheduler triggered HL7 PDQ or FHIR PDQ queries
   |
   | - Only applicable for REST triggered HL7 PDQ or FHIR PDQ queries"
   , Participant Object Type Code, M, 2 (= System Object),
   , Participant Object Type Code Role, M, "| 3 (= Report)
   | OR
   | 24 (= Query)","| - Only applicable for DICOM C-FIND queries
   |
   | - Only applicable for REST triggered DICOM entities' queries or HL7 PDQ / FHIR PDQ queries"
   , Participant Object ID Type Code, U, "| EV ('REST', '99DCM4CHEE', 'RESTful Web Service')
   | OR
   | EV ('110181', 'DCM', 'SOP Class UID')
   | OR
   | EV ('ITI-21', 'IHE Transactions', 'Patient Demographics Query')
   | OR
   | EV ('ITI-78', 'IHE Transactions', 'Mobile Patient Demographics Query')", "| - Only applicable for REST triggered DICOM entities' queries
   |
   | - Only applicable for DICOM C-FIND queries
   |
   | - Only applicable for HL7 PDQ queries
   |
   | - Only applicable for FHIR PDQ queries"
   , Participant Object Detail, MC, "| Base64 encoded value for 'UTF-8' ⇒ 'type=QueryEncoding value=VVRGLTg='
   | OR
   | Base64 encoded value for 'ImplicitVRLittleEndian' ⇒ 'type=TransferSyntax value=MS4yLjg0MC4xMDAwOC4xLjI='", "| - Only applicable for REST triggered DICOM entities' / HL7 PDQ / FHIR PDQ queries
   |
   | - Only applicable for DICOM C-FIND queries"
   , Participant Object Detail, MC, Base64 encoded value of MSH-10 value sent in QBP^Q22 message to supplier, Only applicable for HL7 PDQ queries
   Participating Object - Patient, Participating Object ID, U, Patient identifier, Only applicable for HL7 PDQ or FHIR PDQ queries
   , Participant Object Type Code, M, 1 (= Person),
   , Participant Object Type Code Role, M, 1 (= Patient),
   , Participant Object ID Type Code, M, "| EV (2, RFC-3881, 'Patient Number')",
   , Participant Object Name, U, The patient name,
   , Participant Object Detail, MC, Base64 encoded value of HL7v2 Message sent as QBP^Q22 message to supplier, Only applicable for HL7 PDQ queries
   , Participant Object Detail, MC, Base64 encoded value of MSH-9 value sent in QBP^Q22 message request to supplier, Only applicable for HL7 PDQ queries
   , Participant Object Detail, MC, Base64 encoded value of MSH-10 value sent in QBP^Q22 message request to supplier, Only applicable for HL7 PDQ queries
   , Participant Object Detail, MC, Base64 encoded value of HL7v2 Message received as RSP^K22 response from supplier, Only applicable for HL7 PDQ queries
   , Participant Object Detail, MC, Base64 encoded value of MSH-9 value received in RSP^K22 message response from supplier, Only applicable for HL7 PDQ queries
   , Participant Object Detail, MC, Base64 encoded value of MSH-10 value sent in QBP^Q22 message response from supplier, Only applicable for HL7 PDQ queries

.. [#Note1] Depending on the query level triggered by :
   - `QIDO-RS REST APIs <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/QIDO-RS>`_
   - Search / Count Modality Worklists in `MWL-RS REST APIs <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MWL-RS>`_
   - `MPPS-RS REST APIs <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/MPPS-RS>`_
   - Search / Count Workitems in `UPS-RS REST APIs <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/UPS-RS>`_
   may contain either of the following values :
   - **SearchForPatients**
   - **SearchForStudies**
   - **SearchForSeries**
   - **SearchForStudySeries**
   - **SearchForInstances**
   - **SearchForStudyInstances**
   - **SearchForStudySeriesInstances**
   - **SearchForSPS** (applicable for MWLs - Modality Worklists)
   - **SearchForMPPS**
   - **SearchForUPS** (applicable for UWLs - Unified Worklists)

.. [#Note2] May contain either of the following values depending on the DICOM C-FIND query level -
   **1.2.840.10008.5.1.4.1.2.1.1** : Patient Root Query/Retrieve Information Model - FIND, SOPClass
   **1.2.840.10008.5.1.4.1.2.3.1** : Patient/Study Only Query/Retrieve Information Model - FIND (Retired), SOPClass
   **1.2.840.10008.5.1.4.1.2.2.1** : Study Root Query/Retrieve Information Model - FIND, SOPClass
   **1.2.840.10008.5.1.4.31** : Modality Worklist Information Model - FIND, SOPClass

.. csv-table:: Entities in Query Audit Message

    :ref:`event-identification-query`
    :ref:`active-participant-initiator-query`, Not present in Patient Demographics Query triggered by scheduler case
    :ref:`active-participant-archive-query`, Not present in Patient Demographics Query triggered by scheduler case
    :ref:`active-participant-pdq-consumer-query`, Present only in Patient Demographics Query case
    :ref:`active-participant-pdq-supplier-query`, Present only in Patient Demographics Query case
    :ref:`active-participant-fhir-pdq-user-query`, Present only in FHIR Patient Demographics Query case
    :ref:`active-participant-fhir-pdq-consumer-query`, Present only in FHIR Patient Demographics Query case
    :ref:`active-participant-fhir-pdq-supplier-query`, Present only in FHIR Patient Demographics Query case
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-c-find-query`, Present only in Query by C-FIND
    :ref:`participant-object-qido-query`, Present only in QIDO Query
    :ref:`participant-object-pdq-query`, Present only in Patient Demographics Query case
    :ref:`participant-object-pdq-patient-query`, Present only in HL7 Patient Demographics Query case
    :ref:`participant-object-fhir-pdq-patient-query`, Present only in FHIR HL7 Patient Demographics Query case

.. csv-table:: Event Identification
   :name: event-identification-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "EV (110112, DCM, 'Query')"
   EventActionCode, M, Execute ⇒ 'E'
   EventDateTime, M, The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, Error/Exception message when EventOutcomeIndicator ⇒ '4'
   EventTypeCode, C, "| HL7v2 Patient Demographics Query case ⇒ EV (ITI-21, IHE Transactions, 'Patient Demographics Query')
   | HL7 FHIR R4 Patient Demographics Query case ⇒ EV (ITI-78, urn:ihe:event-type-code, 'Mobile Patient Demographics Query')"

.. csv-table:: Active Participant : Initiator
   :name: active-participant-initiator-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Query triggered by C-FIND ⇒ 'Calling AE title in association'
   | QIDO or Patient Demographics query triggered by REST services : Secured Archive ⇒ 'User name of logged in user'
   | QIDO or Patient Demographics query triggered by REST services : Unsecured Archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Query triggered by C-FIND ⇒ EV (110119, DCM, 'Station AE Title')
   | QIDO or Patient Demographics query triggered by REST services : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | QIDO or Patient Demographics query triggered by REST services : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, "| Query triggered by C-FIND : Application ⇒ '2'
   | QIDO or Patient Demographics query triggered by REST services : Person ⇒ '1'"
   UserIsRequestor, M, | true
   RoleIDCode, M, "| EV (110153, DCM, 'Source Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Query triggered by C-FIND ⇒ 'Called AE title in association'
   | QIDO or Patient Demographics query triggered by REST services ⇒ 'Request URI'"
   UserIDTypeCode, U, "| Triggered by C-FIND ⇒ EV (110119, DCM, 'Station AE Title')
   | Triggered from UI ⇒ EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, | false
   RoleIDCode, M, "| EV (110152, DCM, 'Destination Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Patient Demographics Consumer
   :name: active-participant-pdq-consumer-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| 'Sending Application and Facility Name'"
   UserIDTypeCode, U, "| EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
   UserTypeCode, U, | 2
   UserIsRequestor, M, "| Patient Demographics query triggered by scheduler ⇒ true
   | Patient Demographics query triggered by REST services ⇒ false"
   RoleIDCode, M, "| EV (110153, DCM, 'Source Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Patient Demographics Supplier
   :name: active-participant-pdq-supplier-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| 'Receiving Application and Facility Name'"
   UserIDTypeCode, U, "| EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
   UserTypeCode, U, | 2
   UserIsRequestor, M, | false
   RoleIDCode, M, "| EV (110152, DCM, 'Destination Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : FHIR Patient Demographics User
   :name: active-participant-fhir-pdq-user-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| For secured archive ⇒ 'User name of logged in user'
   | For unsecured archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| For secured archive ⇒ EV (113871, DCM, 'Person ID')
   | For unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, | Person ⇒ '1'
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : FHIR Patient Demographics Consumer
   :name: active-participant-fhir-pdq-consumer-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| For scheduler triggered PDQ ⇒ 'Archive Device Name'
   | For REST triggered PDQ ⇒ 'Invoked URL of archive's PDQ REST service'"
   UserIDTypeCode, U, "| For scheduler triggered PDQ ⇒ 'EV (113877, DCM, 'Device Name')''
   | For REST triggered PDQ ⇒ 'EV (12, RFC-3881, 'URI')'"
   UserTypeCode, U, | 2
   UserIsRequestor, M, "| For scheduler triggered PDQ ⇒ true
   | For REST triggered PDQ ⇒ false"
   RoleIDCode, M, "| EV (110153, DCM, 'Source Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : FHIR Patient Demographics Supplier
   :name: active-participant-fhir-pdq-supplier-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| 'Service URL of HL7 FHIR R4 PDQ Service Provider'"
   UserIDTypeCode, U, "| EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | 2
   UserIsRequestor, M, | false
   RoleIDCode, M, "| EV (110152, DCM, 'Destination Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of HL7 FHIR R4 PDQ Service Provider host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification : C-FIND Query
   :name: participant-object-c-find-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, "| For patient query ⇒ '1.2.840.10008.5.1.4.1.2.1.1'
   | For study/series/instance query ⇒ '1.2.840.10008.5.1.4.1.2.2.1'
   | For MWL query ⇒ '1.2.840.10008.5.1.4.31'"
   ParticipantObjectTypeCode, M, | SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, | Report ⇒ '3'
   ParticipantObjectIDTypeCode, M, "| EV (110181, DCM, 'SOP Class UID')"
   ParticipantObjectQuery, M, | Base64 encoded value of Query keys
   ParticipantObjectDetail, MC, | Base64 encoded value for ImplicitVRLittleEndian '1.2.840.10008.1.2' ⇒ 'type=TransferSyntax value=MS4yLjg0MC4xMDAwOC4xLjI='"

.. csv-table:: Participant Object Identification : QIDO Query
   :name: participant-object-qido-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, "| For patient query ⇒ 'SearchForPatients'
   | For study query ⇒ 'SearchForStudies'
   | For series query ⇒ 'SearchForStudySeries' or 'SearchForSeries'
   | For Instance query ⇒ 'SearchForInstances' or 'SearchForStudyInstances' or 'SearchForStudySeriesInstances'
   | For MWL query ⇒ 'SearchForSPS'"
   ParticipantObjectTypeCode, M, | SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, | Query ⇒ '24'
   ParticipantObjectIDTypeCode, M,  "| EV (QIDO, 99DCM4CHEE, 'QIDO_Query')"
   ParticipantObjectQuery, M, | Base64 encoded value of Request URI plus the Query String
   ParticipantObjectDetail, MC, | Base64 encoded value for 'UTF-8' ⇒ 'type=QueryEncoding value=VVRGLTg='

.. csv-table:: Participant Object Identification : Patient Demographics Query
   :name: participant-object-pdq-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, "| Patient Demographics Query triggered by scheduler ⇒ 'PatientVerificationScheduler'
   | Patient Demographics Query triggered by Compare Patient Demographics service ⇒ 'DiffPatientDemographics'
   | Patient Demographics Query triggered by Update Patient Demographics service ⇒ 'UpdatePatientDemographics'
   | Patient Demographics Query triggered by Query Patient Demographics service ⇒ 'QueryPatientDemographics'"
   ParticipantObjectTypeCode, M, | SystemObject ⇒ '2'
   ParticipantObjectTypeCodeRole, M, | Query ⇒ '24'
   ParticipantObjectIDTypeCode, M,  "| For HL7v2 PDQ Service Provider ⇒ EV (ITI-21, IHE Transactions, 'Patient Demographics Query')
   | For HL7 FHIR R4 PDQ Service Provider ⇒ EV (ITI-78, IHE Transactions, 'Mobile Patient Demographics Query')"
   ParticipantObjectQuery, M,  "| For HL7v2 PDQ Service Provider ⇒ Base64 encoded value of complete QBP^Q22 query message
   | For HL7 FHIR R4 PDQ Service Provider ⇒ Base64 encoded value of query params passed to HL7 FHIR R4 Service Provider"

.. csv-table:: Participant Object Identification : Patient Demographics Query - Patient
   :name: participant-object-pdq-patient-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown
   ParticipantObjectTypeCode, M, Person : '1'
   ParticipantObjectTypeCodeRole, M, Patient : '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name
   ParticipantObjectDetail, U, 'type=HL7v2 Message value=<Base-64 encoded QBP^Q22 HL7 message>'
   ParticipantObjectDetail, U, 'type=HL7v2 Message value=<Base-64 encoded RSP^K22 HL7 response>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 message control ID>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 response message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 response message control ID>'

.. csv-table:: Participant Object Identification : FHIR Patient Demographics Query - Patient
   :name: participant-object-fhir-pdq-patient-query
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown
   ParticipantObjectTypeCode, M, Person : '1'
   ParticipantObjectTypeCodeRole, M, Patient : '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name

Sample Messages
---------------

Query triggered using QIDO-RS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2024-05-06T13:13:44.343+02:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="16153" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="SearchForStudies" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
    		<ParticipantObjectIDTypeCode csd-code="REST" originalText="RESTful Web Service" codeSystemName="99DCM4CHEE"/>
    		<ParticipantObjectQuery>bGltaXQ9MjEmaW5jbHVkZWZpZWxkPWFsbCZvZmZzZXQ9MA==</ParticipantObjectQuery>
    		<ParticipantObjectDetail type="QueryEncoding" value="VVRGLTg="/>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Query triggered using C-FIND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2024-05-06T13:17:34.441+02:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="16153" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="FINDSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.10008.5.1.4.1.2.2.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110181" originalText="SOP Class UID" codeSystemName="DCM"/>
    		<ParticipantObjectQuery>CAAgAAoAAAAyMDIwMDEwMS0gCABQAAAAAAAIAFIABgAAAFNUVURZIAgAYQACAAAAQ1QQABAAAAAAABAAIAAAAAAAIAANAAAAAAA=</ParticipantObjectQuery>
    		<ParticipantObjectDetail type="TransferSyntax" value="MS4yLjg0MC4xMDAwOC4xLjI="/>
    	</ParticipantObjectIdentification>
    </AuditMessage>

HL7 Patient Demographics Query - REST triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Query Patient Demographics <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/PDQ-RS/queryPatientDemographics>`_
REST Service triggered HL7 Patient Demographics Query audit.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventOutcomeIndicator="0">
    	    <EventTypeCode csd-code="ITI-21" codeSystemName="IHE Transactions" originalText="Patient Demographics Query"/>
    		<EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="HL7SND|DCM4CHEE" AlternativeUserID="16153" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/pdq/HL7PatientDemographicsQuery-to-PatientDemographicsSupplier/patients/PDQ-4713455" AlternativeUserID="16153" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="admin" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="PDQ-4713455" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>DOE^JOHN</ParticipantObjectName>
    		<ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDUwNjEzMzgyNC4yOTh8fFFCUF5RMjJeUUJQX1EyMXwxNjk3OTc4MTkzfFB8Mi41fHx8fHx8VU5JQ09ERSBVVEYtOHx8fA1RUER8SUhFIFBEUSBRdWVyeXxRUlkxNjk3OTc4MTkzfEBQSUQuMy4xXlBEUS00NzEzNDU1fA1SQ1B8SXx8fHx8fA0="/>
    		<ParticipantObjectDetail type="MSH-9" value="UUJQXlEyMg=="/>
    		<ParticipantObjectDetail type="MSH-10" value="MTY5Nzk3ODE5Mw=="/>
    		<ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDUwNjEzMzgyNC4zOTV8fFJTUF5LMjJeUlNQX0syMXwyMDk2NzI2NjkwfFB8Mi41fHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTY5Nzk3ODE5M3wNUUFLfFFSWTE2OTc5NzgxOTN8T0sNUVBEfElIRSBQRFEgUXVlcnl8UVJZMTY5Nzk3ODE5M3xAUElELjMuMV5QRFEtNDcxMzQ1NXwNUElEfHx8Xl5eJiZ8fERPRV5KT0hOfHwxOTQ3MTExMXxNfHx8U1RSRUVUXl5DSVRZXl40NzExfHx8fHx8fEFDQy00NzExXl5eRENNNENIRS1URVNUJjEuMi40MC4wLjEzLjEuMS45OTkmSVNP"/>
    		<ParticipantObjectDetail type="MSH-9" value="UlNQXksyMg=="/>
    		<ParticipantObjectDetail type="MSH-10" value="MjA5NjcyNjY5MA=="/>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="QueryPatientDemographics" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
    		<ParticipantObjectIDTypeCode csd-code="ITI-21" originalText="Patient Demographics Query" codeSystemName="IHE Transactions"/>
    		<ParticipantObjectQuery>TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDUwNjEzMzgyNC4yOTh8fFFCUF5RMjJeUUJQX1EyMXwxNjk3OTc4MTkzfFB8Mi41fHx8fHx8VU5JQ09ERSBVVEYtOHx8fA1RUER8SUhFIFBEUSBRdWVyeXxRUlkxNjk3OTc4MTkzfEBQSUQuMy4xXlBEUS00NzEzNDU1fA1SQ1B8SXx8fHx8fA0=</ParticipantObjectQuery>
    		<ParticipantObjectDetail type="MSH-10" value="MTY5Nzk3ODE5Mw=="/>
    	</ParticipantObjectIdentification>
    </AuditMessage>

HL7 Patient Demographics Query - Scheduler triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Patient Verification Scheduler triggered HL7 Patient Demographics Query audit.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventOutcomeIndicator="0">
    	    <EventTypeCode csd-code="ITI-21" codeSystemName="IHE Transactions" originalText="Patient Demographics Query"/>
    		<EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="HL7SND|DCM4CHEE" AlternativeUserID="16153" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="HL7RCV|DCM4CHEE" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="16153" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="PDQ-4713455" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>DOE^JOHN</ParticipantObjectName>
    		<ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDUwNjEzNDQyNS4yNjZ8fFFCUF5RMjJeUUJQX1EyMXwxNjk3OTc4MTk0fFB8Mi41fHx8fHx8VU5JQ09ERSBVVEYtOHx8fA1RUER8SUhFIFBEUSBRdWVyeXxRUlkxNjk3OTc4MTk0fEBQSUQuMy4xXlBEUS00NzEzNDU1fA1SQ1B8SXx8fHx8fA0="/>
    		<ParticipantObjectDetail type="MSH-9" value="UUJQXlEyMg=="/>
    		<ParticipantObjectDetail type="MSH-10" value="MTY5Nzk3ODE5NA=="/>
    		<ParticipantObjectDetail type="HL7v2 Message" value="TVNIfF5+XCZ8SEw3UkNWfERDTTRDSEVFfEhMN1NORHxEQ000Q0hFRXwyMDI0MDUwNjEzNDQyNS4yNzF8fFJTUF5LMjJeUlNQX0syMXwyMDk2NzI2NjkxfFB8Mi41fHx8fHx8VU5JQ09ERSBVVEYtOA1NU0F8QUF8MTY5Nzk3ODE5NHwNUUFLfFFSWTE2OTc5NzgxOTR8T0sNUVBEfElIRSBQRFEgUXVlcnl8UVJZMTY5Nzk3ODE5NHxAUElELjMuMV5QRFEtNDcxMzQ1NXwNUElEfHx8Xl5eJiZ8fERPRV5KT0hOfHwxOTQ3MTExMXxNfHx8U1RSRUVUXl5DSVRZXl40NzExfHx8fHx8fEFDQy00NzExXl5eRENNNENIRS1URVNUJjEuMi40MC4wLjEzLjEuMS45OTkmSVNP"/>
    		<ParticipantObjectDetail type="MSH-9" value="UlNQXksyMg=="/>
    		<ParticipantObjectDetail type="MSH-10" value="MjA5NjcyNjY5MQ=="/>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="PatientVerificationScheduler" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
    		<ParticipantObjectIDTypeCode csd-code="ITI-21" originalText="Patient Demographics Query" codeSystemName="IHE Transactions"/>
    		<ParticipantObjectQuery>TVNIfF5+XCZ8SEw3U05EfERDTTRDSEVFfEhMN1JDVnxEQ000Q0hFRXwyMDI0MDUwNjEzNDQyNS4yNjZ8fFFCUF5RMjJeUUJQX1EyMXwxNjk3OTc4MTk0fFB8Mi41fHx8fHx8VU5JQ09ERSBVVEYtOHx8fA1RUER8SUhFIFBEUSBRdWVyeXxRUlkxNjk3OTc4MTk0fEBQSUQuMy4xXlBEUS00NzEzNDU1fA1SQ1B8SXx8fHx8fA0=</ParticipantObjectQuery>
    		<ParticipantObjectDetail type="MSH-10" value="MTY5Nzk3ODE5NA=="/>
    	</ParticipantObjectIdentification>
    </AuditMessage>

FHIR Patient Demographics Query - REST triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Query Patient Demographics <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/PDQ-RS/queryPatientDemographics>`_
REST Service triggered FHIR Patient Demographics Query audit.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="E" EventDateTime="2022-07-18T13:20:56.601+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
            <EventTypeCode csd-code="ITI-78" codeSystemName="urn:ihe:event-type-code" originalText="Mobile Patient Demographics Query"/>
            <EventOutcomeDescription>Mobile Patient Demographics Query</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8080/hapi-fhir-jpaserver/fhir/Patient" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="admin" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/pdq/testHAPI/patients/e925b0f3%2D8006%2D43f6%2Daa31%2D94bd215e55e7%5E%5E%5Ehttps%3A%2F%2Fgithub%2Ecom%2Fsynthetichealth%2Fsynthea" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="QueryPatientDemographics" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
            <ParticipantObjectIDTypeCode csd-code="ITI-78" originalText="Mobile Patient Demographics Query" codeSystemName="IHE Transactions"/>
            <ParticipantObjectQuery>aWRlbnRpZmllcj1odHRwcyUzQSUyRiUyRmdpdGh1Yi5jb20lMkZzeW50aGV0aWNoZWFsdGglMkZzeW50aGVhJTdDZTkyNWIwZjMtODAwNi00M2Y2LWFhMzEtOTRiZDIxNWU1NWU3Jl9mb3JtYXQ9eG1s</ParticipantObjectQuery>
            <ParticipantObjectDetail type="QueryEncoding" value="VVRGLTg="/>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="e925b0f3-8006-43f6-aa31-94bd215e55e7^^^https://github.com/synthetichealth/synthea" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Koepp^Abdul^^Mr.</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

FHIR Patient Demographics Query - Scheduler triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Patient Verification Scheduler triggered FHIR Patient Demographics Query audit.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="E" EventDateTime="2022-07-18T13:20:56.601+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110112" codeSystemName="DCM" originalText="Query"/>
            <EventTypeCode csd-code="ITI-78" codeSystemName="urn:ihe:event-type-code" originalText="Mobile Patient Demographics Query"/>
            <EventOutcomeDescription>Mobile Patient Demographics Query</EventOutcomeDescription>
        </EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8080/hapi-fhir-jpaserver/fhir" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost">
    		<RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="43631" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="e925b0f3-8006-43f6-aa31-94bd215e55e7^^^https://github.com/synthetichealth/synthea" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Koepp^Abdul^^Mr.</ParticipantObjectName>
        </ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="PatientVerificationScheduler" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="24">
    		<ParticipantObjectIDTypeCode csd-code="ITI-78" originalText="Mobile Patient Demographics Query" codeSystemName="IHE Transactions"/>
    		<ParticipantObjectQuery>aWRlbnRpZmllcj1lOTI1YjBmMy04MDA2LTQzZjYtYWEzMS05NGJkMjE1ZTU1ZTcmX2Zvcm1hdD14bWw=</ParticipantObjectQuery>
    		<ParticipantObjectDetail type="QueryEncoding" value="VVRGLTg="/>
    	</ParticipantObjectIdentification>
    </AuditMessage>