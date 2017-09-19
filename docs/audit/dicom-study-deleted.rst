DICOM Study Deleted
===================

Trigger Events
--------------

This message is emitted by the archive when :
- All Instances of a Study are rejected using RESTful service
  `Reject Study <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/IOCM-RS/RejectStudy>`_
  or `Reject Study External <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/DIMSE-RS/RejectStudyExternal>`_
- This message is also sent when Rejection Notes are stored to the archive using `RAD-66 <http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol1.pdf#page=234>`_ transaction.
- The whole study is deleted by the scheduler.
- The whole study is permanently deleted using `Delete Study Permanently <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/IOCM-RS/DeleteStudy>`_ RESTful service.

Message Structure
-----------------

.. csv-table:: Supported Entities in DICOM Study Deleted Audit Message

    :ref:`event-identification-study-deleted`
    :ref:`active-participant-archive-study-deleted`
    :ref:`active-participant-initiator-study-deleted`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-study-deleted`
    :ref:`participant-object-patient-study-deleted`

.. csv-table:: Event Identification
   :name: audit-study-deleted-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110105, DCM, 'DICOM Study Deleted')"
         "EventActionCode", "M", "'D' ⇒ 'Delete'"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0'⇒'SUCCESS', '4'⇒'Minor failure'"
         "EventOutcomeDescription", "M", "Type of Rejection"

.. csv-table:: Active Participant: Archive application
   :name: audit-study-deleted-active-participant-app
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "All Rejected using association ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "All Rejected using archive UI ⇒ 'Invoked URL'"
         "", "", "Deletion by Scheduler case ⇒ 'Archive device name'"
         "UserIDTypeCode", "U", "Deletion triggered by scheduler : EV (113877, DCM, 'Device Name')"
         "", "", "Deletion triggered using RESTful service : EV (12, RFC-3881, 'URI')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "All Rejected case ⇒ 'false'"
         "", "", "Deletion by Scheduler case ⇒ 'true'"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Destination
   :name: audit-study-deleted-active-participant-user
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "All Rejected using association ⇒ 'Application entity title of initiating system'"
         "", "", "All Rejected using archive UI ⇒ 'Remote IP address' or 'User name of logged in user'"
         "UserIDTypeCode", "U", "Deletion triggered using archive UI (Secured archive) : EV (113871, DCM, 'Person ID')"
         "", "", "Deletion triggered using archive UI (Unsecured archive) : EV (110182, DCM, 'Node ID')"
         "", "", "Deletion triggered using association : EV (110119, DCM, 'Station AE Title')"
         "UserTypeCode", "U", "Deletion triggered using archive UI : 'Person' : '1'"
         "", "", "Deletion triggered using association : 'Application' : '2'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Study
   :name: audit-study-deleted-participant-object-study
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Study Instance UID"
         "ParticipantObjectTypeCode", "M", "'2' ⇒ 'System'"
         "ParticipantObjectTypeCodeRole", "M", "'3' ⇒ 'Report'"
         "ParticipantObjectIDTypeCode", "M", "EV (110180, DCM, 'Study Instance UID')"
         "ParticipantObjectDetail", "U", "Base-64 encoded study date if Study has StudyDate(0008,0020) attribute"
         "ParticipantObjectDescription", "U"
         "SOPClass", "MC", "Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>"
         "Accession", "U", "Accession Number"

.. csv-table:: Participant Object Identification: Patient
   :name: audit-study-deleted-participant-object-patient
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' ⇒ 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' ⇒ 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"


Sample Message
--------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">

        <EventIdentification EventActionCode="D" EventDateTime="2017-07-17T12:17:44.888+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110105" codeSystemName="DCM" originalText="DICOM Study Deleted"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserTypeCode="1" UserIsRequestor="true" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies/2.25.118006535449293656175716160619600634776/reject/113039%5EDCM"
                           AlternativeUserID="2716" UserIsRequestor="false" NetworkAccessPointID="localhost" UserTypeCode="2" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="2.25.118006535449293656175716160619600634776"
             ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="2008/004113"/>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="P5^^^ISSUER" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TEST^Name</ParticipantObjectName>
        </ParticipantObjectIdentification>

    </AuditMessage>