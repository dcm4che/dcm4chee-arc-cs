DICOM Instances Accessed
========================

Trigger Events
--------------

- "DICOM Instances Accessed" message is emitted by the archive only when "some" objects of study are rejected using RESTful services
  `Reject Series <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/IOCM-RS/RejectSeries>`_
  or `Reject Instance <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/IOCM-RS/RejectInstance>`_
  or `Reject Series External <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/DIMSE-RS/RejectSeriesExternal>`_
  or `Reject Instance External <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/DIMSE-RS/RejectInstanceExternal>`_
- This message is also sent when Rejection Notes are stored to the archive using `RAD-66 <http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol1.pdf#page=234>`_ transaction.
- "DICOM Study Deleted" message is sent when the whole study is rejected by storing Rejection Notes to the archive as mentioned above
  or using RESTful services `Reject Study <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/IOCM-RS/RejectStudy>`_
  or `Reject Study External <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger.json#/DIMSE-RS/RejectStudyExternal>`_

Message Structure
-----------------

.. csv-table:: Entities in DICOM Instances Accessed Audit Message

    :ref:`event-identification-instances-accessed`
    :ref:`active-participant-archive-instances-accessed`
    :ref:`active-participant-initiator-instances-accessed`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-instances-accessed`
    :ref:`participant-object-patient-instances-accessed`

.. csv-table:: Event Identification
   :name: event-identification-instances-accessed
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110103, DCM, 'DICOM Instances Accessed')"
         "EventActionCode", "M", "'D' ⇒ 'Delete'"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0'⇒'Success', '4'⇒'Minor failure'"
         "EventOutcomeDescription", "M", "Code Meaning of Rejection Note"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-instances-accessed
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Rejection triggered using association ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Rejection triggered using archive UI ⇒ 'Invoked URL'"
         "UserIDTypeCode", "U", "Rejection triggered using association : EV (110119, DCM, 'Station AE Title')"
         "", "", "Rejection triggered from UI : EV (12, RFC-3881, 'URI')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant : Initiator
   :name: active-participant-initiator-instances-accessed
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Rejection triggered using association ⇒ 'Application entity title of initiating system'"
         "", "", "Rejection triggered using archive UI ⇒ 'Remote IP address' or 'User name of logged in user'"
         "UserIDTypeCode", "U", "Rejection triggered using archive UI (Secured archive) : EV (113871, DCM, 'Person ID')"
         "", "", "Rejection triggered using archive UI (Unsecured archive) : EV (110182, DCM, 'Node ID')"
         "", "", "Rejection triggered using association : EV (110119, DCM, 'Station AE Title')"
         "UserTypeCode", "U", "Rejection triggered using archive UI : 'Person' : '1'"
         "", "", "Rejection triggered using association : 'Application' : '2'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification : Study
   :name: participant-object-study-instances-accessed
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

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-instances-accessed
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

        <EventIdentification EventActionCode="D" EventDateTime="2017-07-17T11:24:42.320+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110103" codeSystemName="DCM" originalText="DICOM Instances Accessed"/>
            <EventOutcomeDescription>Data Retention Policy Expired</EventOutcomeDescription>
        </EventIdentification>

        <ActiveParticipant UserID="127.0.0.1" UserIsRequestor="true" UserTypeCode="1" NetworkAccessPointID="127.0.0.1" NetworkAccessPointTypeCode="2">
            <UserIDTypeCode csd-code="110182" codeSystemName="DCM" originalText="Node ID"/>
        </ActiveParticipant>

        <ActiveParticipant UserID="/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.392.200036.9125.0.199402091242.1/series/1.2.392.200036.9125.0.199402091242.1/reject/113039%5EDCM"
           AlternativeUserID="2716" UserIsRequestor="false" NetworkAccessPointID="localhost" UserTypeCode="2" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="12" codeSystemName="RFC-3881" originalText="URI"/>
        </ActiveParticipant>

        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.199402091242.1"
            ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <SOPClass UID="1.2.840.10008.5.1.4.1.1.1" NumberOfInstances="1"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="P5^^^ISSUER" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TEST^Name</ParticipantObjectName>
        </ParticipantObjectIdentification>

    </AuditMessage>