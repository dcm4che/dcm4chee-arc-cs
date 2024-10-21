DICOM Instances Transferred
===========================

Trigger Events
--------------

This message is emitted by the archive in following cases :

- Query/Retrieve of objects using `RAD-16 <http://ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf#page=206>`_
    - C-Move : Objects of a study are retrieved using query/retrieve service and stored to external destination
    - C-Get : Objects of a study are retrieved using query/retrieve service and stored to the destination which is same as source
- Export : Objects of a study are exported to a destination
- Invoking `WADO-RS <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/WADO-RS>`_
  or `WADO URI <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/WADO-URI>`_
  services
- Objects of a study are stored to the archive by DICOM C-STORE / `Web services <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/STOW-RS>`_
- Assume responsibility for reliable storage of received objects according IHE Transaction `Storage Commitment RAD-10 <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf#page=177>`_
- Verify reliable storage of received objects triggered by `Storage Verification RESTful services <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/STGVER-RS>`_ - typically invoked by the Archive UI - or scheduler triggered periodical storage verification <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Storage-Verification>`_.
- Storage Verification of objects of study using UI / scheduler
- XDSI Retrieve Imaging Document Set `RAD-69 <http://ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol3.pdf#page=185>`_ transaction.
- `Import instances on Storage <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IMPORT-RS/ImportInstances>`_
- `Study is re-imported <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IOCM-RS/ReimportStudy>`_

Message Structure
-----------------

.. csv-table:: Entities in DICOM Instances Transferred Audit Message

    :ref:`event-identification-instances-transferred`
    :ref:`active-participant-archive-instances-transferred`
    :ref:`active-participant-destination-instances-transferred`, Not present in Store objects and storage commitment cases
    :ref:`active-participant-other-instances-transferred`, Present only in Query/Retrieve C-Move case
    :ref:`active-participant-user-instances-transferred`, Present only in Export case triggered from UI
    :ref:`active-participant-source-instances-transferred`, Present only in Store objects and Storage commitment cases
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-instances-transferred`
    :ref:`participant-object-patient-instances-transferred`

.. csv-table:: Event Identification
   :name: event-identification-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110104, DCM, 'DICOM Instances Transferred')"
   EventActionCode, M, "| Store objects case : Create ⇒ 'C' or Update ⇒ 'U'
   | For all other cases : Read ⇒ 'R'"
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Q/R Move case ⇒ 'Application entity title of Archive Device used in the association'
   | Q/R Get case ⇒ 'Application entity title of Archive Device used in the association'
   | Store objects case : Triggered by Association ⇒ 'Application entity title of Archive Device used in the association'
   | Store objects case : Triggered from UI ⇒ 'Invoked URL'
   | Storage Commitment case : Triggered by Association ⇒ 'Application entity title of Archive Device used in the association'
   | Storage Commitment case : Triggered from UI ⇒ 'Invoked URL'
   | Export case : Triggered by scheduler ⇒ 'Archive device name'
   | Export case : Triggered from UI ⇒ 'Invoked URL'
   | WADO RS case ⇒ 'Invoked URL'
   | XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'Invoked URL'"
   UserIDTypeCode, U, "| Q/R Move case ⇒ EV (110119, DCM, 'Station AE Title')
   | Q/R Get case ⇒ EV (110119, DCM, 'Station AE Title')
   | Store objects case : Triggered by Association ⇒ EV (110119, DCM, 'Station AE Title')
   | Store objects case : Triggered from UI ⇒ EV (12, RFC-3881, 'URI')
   | Storage Commitment case : Triggered by Association ⇒ EV (110119, DCM, 'Station AE Title')
   | Storage Commitment case : Triggered from UI ⇒ EV (12, RFC-3881, 'URI')
   | Export case triggered by scheduler ⇒ EV (113877, DCM, 'Device Name')
   | Export case triggered from UI ⇒ EV (12, RFC-3881, 'URI')
   | WADO RS case ⇒ EV (12, RFC-3881, 'URI')
   | XDSI Retrieve Imaging Document Set RAD-69 case ⇒ EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, "| Export case : Triggered by scheduler ⇒ 'true'
   | All other cases ⇒ 'false'"
   RoleIDCode, M, "| Store objects case ⇒ EV (110152, DCM, 'Destination')
   | Store Commitment Case ⇒ EV (110152, DCM, 'Destination')
   | All other cases ⇒ EV (110153, DCM, 'Source')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Destination
   :name: active-participant-destination-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Q/R Move case ⇒ 'Application entity title of destination system'
   | Q/R Get case ⇒ 'Application entity title of association initiating system'
   | Export case ⇒ 'dicomAETitle of destination'
   | WADO-RS case : Secured archive ⇒ 'User name of logged in user'
   | WADO-RS case : Unsecured archive ⇒ 'Remote IP address'
   | XDSI Retrieve Imaging Document Set RAD-69 case : Secured archive ⇒ 'User name of logged in user'
   | XDSI Retrieve Imaging Document Set RAD-69 case : Unsecured archive ⇒ 'Remote IP address'"
   UserIsRequestor, M, "| Q/R Move case ⇒ 'false'
   | Q/R Get case ⇒ 'true'
   | Export case ⇒ 'false'
   | WADO RS case ⇒ 'true'
   | XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'false'"
   UserIDTypeCode, U, "| Q/R Move case ⇒ EV (110119, DCM, 'Station AE Title')
   | Q/R Get case ⇒ EV (110119, DCM, 'Station AE Title')
   | Export case ⇒ EV (110119, DCM, 'Station AE Title')
   | WADO RS case : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | WADO RS case : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')
   | XDSI Retrieve Imaging Document Set RAD-69 case : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | XDSI Retrieve Imaging Document Set RAD-69 case : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, "| WADO RS case : Person ⇒ '1'
   | XDSI Retrieve Imaging Document Set RAD-69 case : Person ⇒ '1'
   | For all other cases : Application ⇒ '2'"
   RoleIDCode, M, "| EV (110152, DCM, 'Destination Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Other
   :name: active-participant-other-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, | Application entity title of association initiating system
   UserIDTypeCode, U, "| EV (110119, DCM, 'Station AE Title')"
   UserTypeCode, U, | Application ⇒ '2'
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of initiating system
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : User
   :name: active-participant-user-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Export case triggered from UI : Secured archive ⇒ 'User name of logged in user'
   | Export case triggered from UI : Unsecured archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, | Person ⇒ '1'
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of initiating system
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Source
   :name: active-participant-source-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Store object case : Triggered by association ⇒ 'Application entity title of system storing study objects to archive'
   | Triggered by HL7 ORU ⇒ 'HL7 Sending Application and Facility'
   | Store object case : Triggered from UI : Secured Archive ⇒ 'User name of logged in user'
   | Store object case : Triggered from UI : Unsecured Archive ⇒ 'Remote IP address'
   | Storage Commitment case : Triggered by association ⇒ 'Application entity title of association initiating system'
   | Store object case : Triggered from UI : Secured Archive ⇒ 'User name of logged in user'
   | Store object case : Triggered from UI : Unsecured Archive ⇒ 'Remote IP address'"
   UserIDTypeCode, U, "| Triggered by association ⇒ EV (110119, DCM, 'Station AE Title')
   | Triggered by HL7 ORU ⇒ EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI : Secured archive ⇒ EV (113871, DCM, 'Person ID')
   | Triggered from UI : Unsecured archive ⇒ EV (110182, DCM, 'Node ID')"
   UserTypeCode, U, "| Triggered from UI : Person ⇒ '1'
   | Triggered by association : Application ⇒ '2'"
   UserIsRequestor, M, | true
   RoleIDCode, M, "| EV (110153, DCM, 'Source Role ID')"
   NetworkAccessPointID, U, | Hostname/IP Address of initiating system
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Participant Object Identification : Study
   :name: participant-object-study-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Study Instance UID or 1.2.40.0.13.1.15.110.3.165.1 if unknown
   ParticipantObjectTypeCode, M, System ⇒ '2'
   ParticipantObjectTypeCodeRole, M, Report ⇒ '3'
   ParticipantObjectIDTypeCode, M, "EV (110180, DCM, 'Study Instance UID')"
   ParticipantObjectDetail, U, "Base-64 encoded study date if Study has StudyDate(0008,0020) attribute"
   ParticipantObjectDataLifeCycle, U, "| Store object case : OriginationCreation ⇒ '1'
   | Storage Commitment case : Verification ⇒ '4'
   | For all other cases ⇒ This field is not present"
   ParticipantObjectDescription, U
   SOPClass, MC, Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>
   Accession, U, Accession Number

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-instances-transferred
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID or <none> if unknown
   ParticipantObjectTypeCode, M, Person ⇒ '1'
   ParticipantObjectTypeCodeRole, M, Patient ⇒ '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name

Sample Messages
---------------

Studies Stored to archive
.........................

Using DICOM C-STORE
^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2023-11-28T15:16:32.025+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="27558" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
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

Error case

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2023-11-29T13:54:16.349+01:00" EventOutcomeIndicator="4">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
            <EventTypeCode csd-code="A777" codeSystemName="99DCM4CHEE" originalText="Patient ID missing in object"/>
            <EventOutcomeDescription>No Patient ID from trusted Assigning Authority in object.</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="37716" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MTk5NTA2MDI="/>
            <ParticipantObjectDescription>
                <Accession Number="SMS000018"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.2" NumberOfInstances="9"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>COTTA^ANNA</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Using HL7 ORU
^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2023-11-28T15:16:03.985+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="CENTRAL|HOSP1" AlternativeUserID="27558" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="MESA_RPT_MGR|EAST_RADIOLOGY" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="2.25.59010335110574257331553683944760036216" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="ACC1"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.104.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="PID1^^^JMS" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Berger^Oliver</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Using HTTP STOW
^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2023-11-28T15:16:38.793+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="27558" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
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

Study Reimport
..............

Applicable for `Import Instances <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IMPORT-RS/ImportInstances>`_ REST API

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2023-12-04T10:35:25.128+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113674.1118.54.200/reimport" AlternativeUserID="10469" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
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

Retrieve Entities
.................

Using DICOM C-GET
^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-29T14:28:24.232+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="55989" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="GETSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="12345-HD11" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>OBSR^WITH MEAS^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113543.6.6.4.1.61567187113131110962211582791512183929288" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwNTEyMDU="/>
            <ParticipantObjectDescription>
                <Accession Number="OB SR EXAM"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.6.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Using DICOM C-MOVE
^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-29T14:19:27.920+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="MOVESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="55989" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="12345-HD11" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>OBSR^WITH MEAS^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113543.6.6.4.1.61567187113131110962211582791512183929288" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwNTEyMDU="/>
            <ParticipantObjectDescription>
                <Accession Number="OB SR EXAM"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.6.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Error Case

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="E" EventDateTime="2024-08-30T09:06:02.676+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110102" codeSystemName="DCM" originalText="Begin Transferring DICOM Instances"/>
            <EventOutcomeDescription>org.dcm4che3.net.service.DicomServiceException: java.net.ConnectException: Connection refused</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="MOVESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="5908" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="I2EXAMPLE" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Hong^Gildong=洪^吉洞=홍^길동</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwMjA0MjY="/>
            <ParticipantObjectDescription>
                <Accession Number="ACCESSION01"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1">
                    <Instance UID="1.1.1.1"/>
                </SOPClass>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Export Study using REST API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-29T15:15:52.806+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.840.113543.6.6.4.1.61567187113131110962211582791512183929288/export/dicom:STORESCP" AlternativeUserID="82158" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="82158" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="12345-HD11" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>OBSR^WITH MEAS^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113543.6.6.4.1.61567187113131110962211582791512183929288" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwNTEyMDU="/>
            <ParticipantObjectDescription>
                <Accession Number="OB SR EXAM"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.6.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Export Study by Scheduler
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-29T15:41:35.495+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="82158" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="I2EXAMPLE" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Hong^Gildong=洪^吉洞=홍^길동</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.6.1.4.1.5962.1.2.0.1175775771.5708.0" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.7" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Retrieve Study Metadata by WADO-RS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-29T16:01:26.672+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.3.6.1.4.1.5962.1.2.0.1175775771.5708.0/metadata" AlternativeUserID="82158" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="I2EXAMPLE" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Hong^Gildong=洪^吉洞=홍^길동</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.6.1.4.1.5962.1.2.0.1175775771.5708.0" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.7" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Retrieve Multiple Studies of Patient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applicable for DICOM C-MOVE on PATIENT level

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-30T09:09:39.539+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="MOVESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="view-localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="5908" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="I2EXAMPLE" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>Hong^Gildong=洪^吉洞=홍^길동</ParticipantObjectName>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.6.1.4.1.5962.1.2.0.1175775771.5708.0" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.7" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="ACCESSION01"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    </AuditMessage>

Retrieve Instance using WADO-URI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-23T18:52:35.938+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/wado?requestType=WADO&amp;studyUID=2.16.376.1.1.511752826.1.2.21313.5230164&amp;seriesUID=2.16.376.1.1.511752826.1.2.21459.3526228&amp;objectUID=1.2.840.113704.7.7.1.1762134868.1376.807377234.26&amp;contentType=image/jpeg&amp;frameNumber=1" AlternativeUserID="39607" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.21313.5230164" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="ALGO00000"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.2" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="ALGO00001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>PROBST^KATHY</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Storage Commitment
..................

Using REST API
^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-22T12:50:22.215+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.1/stgver" AlternativeUserID="14940" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Scheduler Triggered
^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-22T12:36:35.874+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" AlternativeUserID="14940" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1"/>
                <ParticipantObjectContainsStudy>
                    <StudyIDs UID="1.1"/>
                </ParticipantObjectContainsStudy>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Storage Commitment SCU triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-22T12:55:44.325+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="STGCMTSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="14940" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Storage Commitment referencing Instances of Multiple Studies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-22T13:09:52.670+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="STGCMTSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="14940" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113619.2.216.2.1.2642006103252234.10589" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1">
                    <Instance UID="1.1.1.1"/>
                </SOPClass>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.20" NumberOfInstances="1">
                    <Instance UID="1.2.840.113619.2.216.2.1.2642006103434968.10942"/>
                </SOPClass>
                <ParticipantObjectContainsStudy>
                    <StudyIDs UID="1.2.840.113619.2.216.2.1.2642006103252234.10589"/>
                    <StudyIDs UID="1.1"/>
                </ParticipantObjectContainsStudy>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="MGID001" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>MAMMOGRAPHY^TEST1</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

Storage Commitment Failure
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2024-08-22T12:47:39.998+02:00" EventOutcomeIndicator="4">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
            <EventOutcomeDescription>NoSuchObjectInstance</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="STGCMTSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="14940" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.40.0.13.1.15.110.3.165.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1.2.1" NumberOfInstances="1">
                    <Instance UID="1.1.1.1"/>
                </SOPClass>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

Storage Verification
....................

Using REST API
^^^^^^^^^^^^^^

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-06T17:10:14+01:00" EventOutcomeIndicator="0">
           <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/stgver/studies" AlternativeUserID="16541" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
           <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
           <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
       </ActiveParticipant>
       <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
           <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
           <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
           <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.113654.1.2001.30" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
           <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
           <ParticipantObjectDescription>
               <SOPClass UID="1.2.840.10008.5.1.4.1.1.88.11" NumberOfInstances="1" />
           </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="CR3" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
           <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
           <ParticipantObjectName>CRTHREE^PAUL</ParticipantObjectName>
       </ParticipantObjectIdentification>
   </AuditMessage>

Scheduler Triggered
^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-15T13:04:52+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="27673" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.4.0.13.1.432252867.1552647.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="M4001^^^ADT1" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>Fengler^Klaus</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

Import Reports from AGFA IMPAX
..............................

Applicable for `Import Reports of Study from AGFA IMPAX <https://petstore.swagger.io/index.html?url=https://dcm4che.github.io/dcm4chee-arc-light/swagger/openapi.json#/IMPAX-REPORT-RS/importReportsOfStudy>`_ REST API

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2023-12-01T14:46:45.164+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="http://localhost:8880/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="16659" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="http://impax-host:8780/import-sr" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="impax-host:8780" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113543.6.6.4.1.623691791684870846611353555872217279695" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwNTEyMDU="/>
            <ParticipantObjectDescription>
                <Accession/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.6.1" NumberOfInstances="5"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="54321^^^pdgen-7EF143F2-null" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>HD11^SAMPLE IMAGES^^^</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

QStar
.....

Applicable for `Verify Access State of objects stored on QStar Tape File System <https://github.com/dcm4che/dcm4chee-arc-light/issues/4131>`_

.. csv-table:: QStar Access State - Event Outcome Mapping
   :name: qstar-access-state-event-outcome-mapping
   :widths: 30, 5, 65
   :header: fetched Access State, Outcome Indicator, Outcome Description

   0 - ACCESS_STATE_NONE, 8, QStar Access State: Not present
   1 - ACCESS_STATE_EMPTY, 8, QStar Access State: Created but no data written
   2 - ACCESS_STATE_UNSTABLE, 4, QStar Access State: Created - primary only
   3 - ACCESS_STATE_STABLE, 0,
   4 - ACCESS_STATE_OUT_OF_CACHE, 4, QStar Access State: Fully migrated - out of cache
   5 - ACCESS_STATE_OFFLINE, 4, QStar Access State: Offline
   ASM WEB Service returns error status, 4, Failed to get QStar Access State

See `EventOutcomeIndicator meaning in General Message Format <https://dicom.nema.org/medical/dicom/current/output/html/part15.html#table_A.5.2-1>`_

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2023-11-06T16:58:37.650+01:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" UserIsRequestor="true" UserTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="file:/home/vrinda/work/archive/wildfly-29.0.1.Final/standalone/data/fs1/2023/11/06/6B4ACE22/E6A508C7/373EA166" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="http://username:password@qstar.host:port/" NetworkAccessPointTypeCode="5">
            <RoleIDCode csd-code="110154" codeSystemName="DCM" originalText="Destination Media"/>
            <MediaType csd-code="QSTAR" codeSystemName="99DCM4CHEE" originalText="QSTAR"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2023-11-06T16:53:37.481+01:00" EventOutcomeIndicator="4">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
            <EventOutcomeDescription>QStar Access State: Created, primary only</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" UserIsRequestor="true" UserTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="file:/home/vrinda/work/archive/wildfly-29.0.1.Final/standalone/data/fs1/2023/11/06/6B4ACE22/E6A508C7/373EA166" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="http://username:password@qstar.host:port/" NetworkAccessPointTypeCode="5">
            <RoleIDCode csd-code="110154" codeSystemName="DCM" originalText="Destination Media"/>
            <MediaType csd-code="QSTAR" codeSystemName="99DCM4CHEE" originalText="QSTAR"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9">
                    <Instance UID="1.2.840.113674.950809133402066.100"/>
                    <Instance UID="1.2.840.113674.950809133408113.100"/>
                    <Instance UID="1.2.840.113674.950809133406100.100"/>
                    <Instance UID="1.2.840.113674.950809133401055.100"/>
                    <Instance UID="1.2.840.113674.950809133405086.100"/>
                    <Instance UID="1.2.840.113674.950809133409128.100"/>
                    <Instance UID="1.2.840.113674.950809133359043.100"/>
                    <Instance UID="1.2.840.113674.950809133404076.100"/>
                    <Instance UID="1.2.840.113674.950809133358028.100"/>
                </SOPClass>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="R" EventDateTime="2023-11-06T16:48:37.297+01:00" EventOutcomeIndicator="8">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
            <EventOutcomeDescription>QStar Access State: Created but no data written</EventOutcomeDescription>
        </EventIdentification>
        <ActiveParticipant UserID="dcm4chee-arc" UserIsRequestor="true" UserTypeCode="2">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID"/>
            <UserIDTypeCode csd-code="113877" codeSystemName="DCM" originalText="Device Name"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="file:/home/vrinda/work/archive/wildfly-29.0.1.Final/standalone/data/fs1/2023/11/06/6B4ACE22/E6A508C7/373EA166" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="http://username:password@qstar.host:port/" NetworkAccessPointTypeCode="5">
            <RoleIDCode csd-code="110154" codeSystemName="DCM" originalText="Destination Media"/>
            <MediaType csd-code="QSTAR" codeSystemName="99DCM4CHEE" originalText="QSTAR"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1115.261.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="9">
                    <Instance UID="1.2.840.113674.950809133402066.100"/>
                    <Instance UID="1.2.840.113674.950809133408113.100"/>
                    <Instance UID="1.2.840.113674.950809133406100.100"/>
                    <Instance UID="1.2.840.113674.950809133401055.100"/>
                    <Instance UID="1.2.840.113674.950809133405086.100"/>
                    <Instance UID="1.2.840.113674.950809133409128.100"/>
                    <Instance UID="1.2.840.113674.950809133359043.100"/>
                    <Instance UID="1.2.840.113674.950809133404076.100"/>
                    <Instance UID="1.2.840.113674.950809133358028.100"/>
                </SOPClass>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="&lt;none&gt;" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
        </ParticipantObjectIdentification>
    </AuditMessage>

XDSI Retrieve Imaging Document Set RAD-69 transaction
.....................................................

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-08T15:06:59+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/xdsi/ImagingDocumentSource" AlternativeUserID="8368" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
       </ActiveParticipant>
       <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="1.2.276.0.24.438.38523304.4.0.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDetail type="StudyDate" value="Mzg1MjMzMDQ=" />
          <ParticipantObjectDescription>
             <Accession Number="38523304" />
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="4785133^^^UKL" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>Fengler^Klaus</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>