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

Sample Message
--------------

Study stored using C-STORE

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
      <EventIdentification EventActionCode="C" EventDateTime="2019-02-05T18:16:46+01:00" EventOutcomeIndicator="0">
         <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
      </EventIdentification>
      <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
         <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
         <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
      </ActiveParticipant>
      <ActiveParticipant UserID="STORESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
         <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
         <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
      </ActiveParticipant>
      <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
         <AuditSourceTypeCode csd-code="4" />
      </AuditSourceIdentification>
      <ParticipantObjectIdentification ParticipantObjectID="1.113654.1.2001.30" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
         <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
         <ParticipantObjectDetail type="StudyDate" value="MjAwMTA0MzA=" />
         <ParticipantObjectDescription>
            <Accession Number="2001C30" />
            <SOPClass UID="1.2.840.10008.5.1.4.1.1.88.11" NumberOfInstances="1" />
         </ParticipantObjectDescription>
      </ParticipantObjectIdentification>
      <ParticipantObjectIdentification ParticipantObjectID="CR3" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
         <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
         <ParticipantObjectName>CRTHREE^PAUL</ParticipantObjectName>
      </ParticipantObjectIdentification>
   </AuditMessage>

Study stored using STOW-RS

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2019-02-05T18:20:00+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies" AlternativeUserID="5726" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
       <ParticipantObjectIdentification ParticipantObjectID="1.2.276.0.24.438.38523304.4.0.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDetail type="StudyDate" value="MjAxODEyMjg=" />
          <ParticipantObjectDescription>
             <MPPS UID="1.3.46.670589.30.1.6.1.963335255131.1545983251893.1" />
             <Accession Number="38523304" />
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="4785133^^^UKL" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>Fengler^Klaus</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

Reports stored using HL7 ORU^R01

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="C" EventDateTime="2019-02-15T17:05:47+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="27673" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="MESA_RPT_MGR|EAST_RADIOLOGY" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="2.25.185448987116626056864758237726880870790" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <Accession Number="ACC1" />
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.88.11" NumberOfInstances="1" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="MM2^^^JMS~MM2^^^JMS1&1.2.3&ISO~MM2^^^JMS2~MM2^^^&1.2.3.4.5.6.7&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>Miller^John</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

Export study triggered from UI

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
      <EventIdentification EventActionCode="R" EventDateTime="2019-02-08T13:49:24+01:00" EventOutcomeIndicator="0">
         <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
      </EventIdentification>
      <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
         <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
         <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
      </ActiveParticipant>
      <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.276.0.24.438.38523304.4.0.1/export/dicom:STORESCP" AlternativeUserID="9694" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
         <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
         <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI" />
      </ActiveParticipant>
      <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
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

Export study triggered by scheduler

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-08T15:14:37+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="8368" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
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

Storage Verification triggered from UI

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

Storage Verification triggered by scheduler

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

Storage Commitment triggered over DICOM association

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-06T17:20:37+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="16541" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="STGCMTSCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
          <AuditSourceTypeCode csd-code="4" />
       </AuditSourceIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="2.16.376.1.1.511752826.1.2.3390529.6263391" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="4">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDescription>
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.7" NumberOfInstances="5" />
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.2" NumberOfInstances="4" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="ALGO00003" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>PRITCHET^LAURIE</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

WADO-URI Retrieve Instance

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-06T17:04:33+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/wado" AlternativeUserID="16541" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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
       <ParticipantObjectIdentification ParticipantObjectID="1.2.840.113674.1118.54.200" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
          <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM" />
          <ParticipantObjectDetail type="StudyDate" value="MTk5NTA3MjU=" />
          <ParticipantObjectDescription>
             <Accession Number="GE0002" />
             <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="1" />
          </ParticipantObjectDescription>
       </ParticipantObjectIdentification>
       <ParticipantObjectIdentification ParticipantObjectID="GE1118" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
          <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881" />
          <ParticipantObjectName>BUXTON^STEVEN</ParticipantObjectName>
       </ParticipantObjectIdentification>
    </AuditMessage>

WADO-RS Retrieve Study

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-08T13:54:34+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.276.0.24.438.38523304.4.0.1" AlternativeUserID="9694" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
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

Retrieve study triggered using C-MOVE

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
       <EventIdentification EventActionCode="R" EventDateTime="2019-02-08T13:43:07+01:00" EventOutcomeIndicator="0">
          <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred" />
       </EventIdentification>
       <ActiveParticipant UserID="DCM4CHEE" AlternativeUserID="9694" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="STORESCP" UserIsRequestor="false" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination Role ID" />
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
       </ActiveParticipant>
       <ActiveParticipant UserID="MOVESCU" UserIsRequestor="true" UserTypeCode="2" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
          <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title" />
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

Retrieve study triggered using C-GET

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="E" EventDateTime="2017-07-10T12:22:29.457+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="DCM4CHEE" UserTypeCode="2" AlternativeUserID="60928" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="GETSCU" UserTypeCode="2" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination"/>
            <UserIDTypeCode csd-code="110119" codeSystemName="DCM" originalText="Station AE Title"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.3.12.2.1107.5.2.33.37113.30000008060311320917100000013" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwODA3MTY="/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.88.22" NumberOfInstances="4"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.4" NumberOfInstances="2"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="P5^^^ISSUER" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TEST^Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>


IMPAX Reports Import Service

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
        <EventIdentification EventActionCode="C" EventDateTime="2018-10-22T12:51:49.332+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110104" codeSystemName="DCM" originalText="DICOM Instances Transferred"/>
        </EventIdentification>
        <ActiveParticipant UserID="testuser" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="113871" codeSystemName="DCM" originalText="Person"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="https://aps1tln.pacs.ee/AgfaHC.Connectivity.Web.Services/ReportServiceCM.asmx" UserTypeCode="1" UserIsRequestor="true" NetworkAccessPointID="agfa-host" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110153" codeSystemName="DCM" originalText="Source"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.113654.1.2001.30/impax/reports" UserTypeCode="2" AlternativeUserID="5373" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <RoleIDCode csd-code="110152" codeSystemName="DCM" originalText="Destination"/>
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="1.113654.1.2001.30" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3" ParticipantObjectDataLifeCycle="1">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDetail type="StudyDate" value="MjAwMTA0MzA="/>
            <ParticipantObjectDescription>
                <Accession Number="2001C30"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.88.11" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
        <ParticipantObjectIdentification ParticipantObjectID="CR3^^^SiteA" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>CRTHREE^PAUL</ParticipantObjectName>
        </ParticipantObjectIdentification>
    </AuditMessage>

XDSI Retrieve Imaging Document Set RAD-69 transaction

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