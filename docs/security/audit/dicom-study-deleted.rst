DICOM Study Deleted
===================

This message describes the event of deletion of one or more studies and all associated SOP Instances in a single action.
and it shall only include information about a single patient.

Trigger Events
--------------

This message is emitted by the archive when :

- Study in a **local archive** is **completely rejected** using :
   - Archive UI : Reject Study function (*Navigation page Studies tab with local archive QIDO_RS web application*)
   - `Reject Study <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IOCM-RS/RejectStudy>`_ REST Service invoked by an external client

- Study in a **local archive** is **completely rejected** on receive of **Rejection Notes Key Objects** using `RAD-66 <http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol1.pdf#page=40>`_ transaction, over :
   - DICOM C-Store
   - `Store over Web of DICOM Objects <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/STOW-RS>`_ REST Services

- Expired study is **completely rejected** by Reject Expired Studies Scheduler
- Previous study is **completely rejected** on subsequent receive of objects having same SOP Instance UID but different Study/Series Instance UIDs
- Study in an **external archive** is **completely rejected** using :
   - Archive UI : Reject Study function (*Navigation page Studies tab with external archive QIDO_RS web application*)
   - `Reject Study from StoreSCP <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IOCM-RS/RejectStudyStoreSCP>`_ and `Query FindSCP Reject Study from StoreSCP <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IOCM-RS/QueryFindSCPRejectStudyStoreSCP>`_ REST Services

- Study in a **local archive** is **completely deleted** by :
   - Purge Storage Scheduler
   - `Delete Study Permanently <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IOCM-RS/DeleteStudy>`_ REST Service invoked by an external client or using archive UI
   - `Delete Patient Permanently <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/PAM-RS/DeletePatient>`_ REST Service invoked by an external client or using archive UI

- Study `deleted on reimport <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IOCM-RS/ReimportStudy>`_

Message Structure
-----------------

.. csv-table:: DICOM Study Deleted Message
   :name: dicom-study-deleted
   :widths: 15, 15, 2, 45, 15
   :header: Real World Entities, Field Name, Opt, Value Constraints, Note

   Event, Event ID, M, "| EV (110105, DCM, 'DICOM Study Deleted')",
   , Event Action Code, M, D (= Delete),
   , Event Date Time, M, , The time at which the event occurred
   , Event Outcome Indicator, M, "| 0 (= Success)
   | OR
   | 4 (= Minor Failure)", "| - Rejection / deletion of study was successful
   |
   | - Applicable if any exception caught on rejection / deletion of study"
   , Event Outcome Description, U, "| Rejection Note Code Meaning
   | OR
   | Rejection Note Code Meaning & Exception Message
   | OR
   | Exception Message
   | OR
   | No value", "| - Applicable only if study is **completely rejected successfully**
   |
   | - Applicable only if study is **completely rejected** and an **exception** is caught
   |
   | - Applicable only if study is **completely deleted** and an **exception** is caught
   |
   | - Applicable only if study is **completely deleted successfully**"
   Active Participant - Archive, User ID, M, "| Device Name of archive
   | OR
   | REST Service Request URL
   | OR
   | AET of archive", "| - Applicable only if study is **completely rejected / deleted** by a *scheduler*
   |
   | - Applicable only if study is **completely rejected / deleted** using *REST services*
   |
   | - Applicable only if (previous) study is **completely rejected / deleted** over *DICOM C-Store*"
   , User ID Type Code, U, "| EV (113877, DCM, 'Device Name')
   | OR
   | EV (12, RFC-3881, 'URI')
   | OR
   | EV (110119, DCM, 'Station AE Title')", "| - Applicable only if study is **completely rejected / deleted** by a *scheduler*
   |
   | - Applicable only if study is **completely rejected / deleted** using *REST services*
   |
   | - Applicable only if (previous) study is **completely rejected / deleted** over *DICOM C-Store*"
   , User Type Code, U, 2 (= Application),
   , Alternative User ID, MC, , Process ID of Audit logger
   , User Is Requestor, M, "| true
   | OR
   | false",  "| - Applicable only if study is **completely rejected / deleted** by a *scheduler*
   |
   | - Applicable only if (previous) study is **completely rejected / deleted** over *DICOM C-Store* / *REST services*"
   , Network Access Point ID, U, , Hostname/IP Address of the connection referenced by Audit logger
   , Network Access Point Type Code, U, "| 1 (= Machine name)
   | OR
   | 2 (= IP Address)", "| - Applicable if NetworkAccessPointID is a **hostname**
   |
   | - Applicable if NetworkAccessPointID is an **IP Address**"
   Active Participant - Requestor, , U, , Available only if study is **completely rejected / deleted** by person or external system
   , User ID, M, "| User Name
   | OR
   | Remote IP Address
   | OR
   | AET of calling system", "| - Applicable only if study is **completely rejected / deleted** using *REST services* of *secured archive*
   |
   | - Applicable only if study is **completely rejected / deleted** using *REST services* of *unsecured archive*
   |
   | - Applicable only if (previous) study is **completely rejected / deleted** over *DICOM C-Store*"
   , User ID Type Code, U, "| EV (113871, DCM, 'Person ID')
   | OR
   | EV (110182, DCM, 'Node ID')
   | OR
   | EV (110119, DCM, 'Station AE Title')", "| - Applicable only if study is **completely rejected / deleted** using *REST services* of *secured archive*
   |
   | - Applicable only if study is **completely rejected / deleted** using *REST services* of *unsecured archive*
   |
   | - Applicable only if (previous) study is **completely rejected / deleted** over *DICOM C-Store*"
   , User Type Code, U, "| 1 (= Person)
   | OR
   | 2 (= Application)", "| - Applicable only if study is **completely rejected / deleted** using *REST services* of *secured archive*
   |
   | - Applicable only if study is **completely rejected / deleted** using *REST services* of *unsecured archive* OR if (previous) study is **completely rejected / deleted** over *DICOM C-Store*"
   , User Is Requestor, M, true,
   , Network Access Point ID, U, , Hostname/IP Address of calling host
   , Network Access Point Type Code, U, "| 1 (= Machine name)
   | OR
   | 2 (= IP Address)", "| - Applicable if NetworkAccessPointID is a **hostname**
   |
   | - Applicable if NetworkAccessPointID is an **IP Address**"
   Active Participant - External Archive, , U, , Available only if study is **completely rejected** in an external archive
   , User ID, M, AET of external archive,
   , User ID Type Code, U, "| EV (110119, DCM, 'Station AE Title')",
   , User Type Code, U, 2 (= Application),
   , User Is Requestor, M, false,
   , Network Access Point ID, U, , Hostname/IP Address of external archive host
   , Network Access Point Type Code, U, "| 1 (= Machine name)
   | OR
   | 2 (= IP Address)", "| - Applicable if NetworkAccessPointID is a **hostname**
   |
   | - Applicable if NetworkAccessPointID is an **IP Address**"
   Participating Object - Study, Participating Object ID, M, The Study Instance UID,
   , Participant Object Type Code, M, 2 (= System Object),
   , Participant Object Type Code Role, M, 3 (= Report),
   , Participant Object ID Type Code, M, "| EV (110180, DCM, 'Study Instance UID')",
   , Participant Object Detail, U, , "| Base64 encoded value of *Study Date (0008,0020)* if available"
   , Participant Object Description, U, ,
   , > Accession, U, , "| Value of *Accession Number (0008,0050)* if available"
   , > SOP Class, MC, ,
   , >> UID, MC, SOP Class UID of DICOM objects,
   , >> Number of Instances, MC, No. of Instances of the SOP Class,
   , >> Instances, U, SOP Instance UIDs of DICOM objects, "| Available only if *Event Outcome Indicator = 4* (i.e. Minor Failure)
   | OR
   | `Include Instance UIDs <https://dcm4chee-arc-cs.readthedocs.io/en/latest/networking/config/auditLogger.html#dcmauditincludeinstanceuid>`_ of Audit Logger is set to *true*"
   Participating Object - Patient, Participating Object ID, M, The patient identifiers, *~* separated list of unique patient identifiers of a patient
   , Participant Object Type Code, M, 1 (= Person),
   , Participant Object Type Code Role, M, 1 (= Patient),
   , Participant Object ID Type Code, M, "| EV (2, RFC-3881, 'Patient Number')",
   , Participant Object Name, U, The patient name,

Sample Messages
---------------

Study completely rejected using unsecured archive UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-21T06:48:44.512+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    		<EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1118.54.200/reject/113039%5EDCM" AlternativeUserID="10296" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU="/>
    		<ParticipantObjectDescription>
    			<Accession Number="GE0002"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="18"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="GE1118^^^DCM4CHEE.C920706B.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>BUXTON^STEVEN</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study completely rejected on store of rejection note by STOW-RS REST Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Store over Web of DICOM Objects <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/STOW-RS>`_ REST Services

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-12-04T09:50:08.500+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    		<EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="10469" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113543.6.6.4.1.623691791684870846611353555872217279695" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MjAwNTEyMDU="/>
    		<ParticipantObjectDescription>
    			<Accession/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.6.1" NumberOfInstances="5"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="54321^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>HD11^SAMPLE IMAGES^^^</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study completely rejected on store of rejection note over DICOM C-Store
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-22T12:42:06.445+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    		<EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="39489" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
    		<ParticipantObjectDescription>
    			<Accession Number="GE0005"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="10"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study permanently deleted using unsecured archive UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-14T19:35:08.600+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.3.12.2.1107.5.8.1.12345678.199508041416590859569" AlternativeUserID="40918" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDI="/>
    		<ParticipantObjectDescription>
    			<Accession Number="SMS000018"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.2" NumberOfInstances="9"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="SMS530102^^^DCM4CHEE.95FB6349.06B2DF89" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study permanently deleted on deletion of patient using unsecured archive UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-14T19:43:44.555+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/patients/ALGO00001%5E%5E%5EDCM4CHEE.6347B1A7.FE005DEA" AlternativeUserID="40918" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.21313.5230164" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDescription>
    			<Accession Number="ALGO00000"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.7" NumberOfInstances="5"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.2" NumberOfInstances="14"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="ALGO00001^^^DCM4CHEE.6347B1A7.FE005DEA" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>PROBST^KATHY</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study deleted on reimporting a study using unsecured archive UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-12-04T10:35:24.488+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1118.54.200/reimport" AlternativeUserID="10469" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU="/>
    		<ParticipantObjectDescription>
    			<Accession Number="GE0002"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="18"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="GE1118^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>BUXTON^STEVEN</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Expired study completely rejected by Reject Expired Studies Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-22T09:51:09.577+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    		<EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="12384" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
    		<ParticipantObjectDescription>
    			<Accession Number="GE0005"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="10"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study completely deleted by Purge Storage Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-14T20:57:03.604+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="54573" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDescription>
    			<Accession Number="ALGO00002"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.7" NumberOfInstances="5"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.2" NumberOfInstances="4"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="ALGO00003^^^DCM4CHEE.A2100E2B.FFEDA3D5" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Previous study completely rejected on subsequent receive of objects with same SOP Instance UID but different Study/Series Instance UIDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-22T11:36:47.213+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    	</EventIdentification>
    	<ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="12384" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDg="/>
    		<ParticipantObjectDescription>
    			<Accession Number="GE0005"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="10"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="GE1115^^^DCM4CHEE.A0DE4BE6.null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>DAVIDSON^JOSHUA</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>

Study completely rejected in external archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    	<EventIdentification EventActionCode="D" EventDateTime="2023-11-22T08:48:23.410+01:00" EventOutcomeIndicator="0">
    		<EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
    		<EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
    	</EventIdentification>
    	<ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/dimse/DCM4CHEE2/studies/1.2.392.200036.9125.0.199402091242.1/reject/113039%5EDCM" AlternativeUserID="9174" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
    		<UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
    	</ActiveParticipant>
    	<ActiveParticipant UserID="DCM4CHEE2" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
    		<UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
    	</ActiveParticipant>
    	<AuditSourceIdentification AuditSourceID="dcm4chee-arc">
    		<AuditSourceTypeCode csd-code="4"/>
    	</AuditSourceIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.199402091242.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
    		<ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
    		<ParticipantObjectDescription>
    			<Accession Number="FUJI95707"/>
    			<SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1"/>
    		</ParticipantObjectDescription>
    	</ParticipantObjectIdentification>
    	<ParticipantObjectIdentification ParticipantObjectID="FUJI00007" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
    		<ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
    		<ParticipantObjectName>ITO^TOSHIAKI</ParticipantObjectName>
    	</ParticipantObjectIdentification>
    </AuditMessage>