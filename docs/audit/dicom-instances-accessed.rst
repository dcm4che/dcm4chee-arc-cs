DICOM Instances Accessed
========================

Trigger Events
--------------

This message is emitted by the archive when some objects of study are rejected using store association or from archive UI.
If the whole study is rejected then "DICOM Study Deleted" message is sent.

Message Structure
-----------------

- :ref:`audit-instances-accessed-event`
- :ref:`audit-instances-accessed-active-participant-app` (1)
- :ref:`audit-instances-accessed-active-participant-destination` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-instances-accessed-participant-object-study` (1)
- :ref:`audit-instances-accessed-participant-object-patient` (1)

.. csv-table:: Event: DICOM Instances Accessed
   :name: audit-instances-accessed-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110103, DCM, 'DICOM Instances Accessed')"
         "EventActionCode", "M", "'D' ⇒ 'Delete'"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0'⇒'Success', '4'⇒'Minor failure'"
         "EventOutcomeDescription", "M", "Type of Rejection"

.. csv-table:: Active Participant: Archive application
   :name: audit-instances-transferred-active-participant-app
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Rejection triggered using association ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Rejection triggered using archive UI ⇒ 'Invoked URL'"
         "UserIDTypeCode", "U", "Rejection triggered using association : EV ("110118","DCM","Archive Device AE Titles")"
         "", "", "Rejection triggered from UI : EV ("12", "RFC-3881", "URI")"
         "UserTypeCode", "U", "'System' : '5'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Destination
   :name: audit-instances-transferred-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Rejection triggered using association ⇒ 'Application entity title of initiating system'"
         "", "", "Rejection triggered using archive UI ⇒ 'Remote IP address' or 'User name of logged in user'"
         "UserIDTypeCode", "U", "Rejection triggered using archive UI (Secured archive) : EV ("Cp1640-1","DCM","Local User ID")"
         "", "", "Rejection triggered using archive UI (Unsecured archive) : EV ("110182","DCM","Node ID")"
         "", "", "Rejection triggered using association : EV ("110119","DCM","Station AE Title")"
         "UserTypeCode", "U", "'Person' : '1'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Study
   :name: audit-instances-transferred-participant-object-study
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
         "ParticipantObjectContainsStudy", "U"
         "StudyIDs", "M", "Study Instance UID"

.. csv-table:: Participant Object Identification: Patient
   :name: audit-instances-transferred-participant-object-patient
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' ⇒ 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' ⇒ 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"


Sample Message
--------------

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
        AlternativeUserID="2716" UserIsRequestor="false" NetworkAccessPointID="localhost" UserTypeCode="5" NetworkAccessPointTypeCode="1">

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

                <ParticipantObjectContainsStudy>

                    <StudyIDs UID="1.2.392.200036.9125.0.199402091242.1"/>

                </ParticipantObjectContainsStudy>

            </ParticipantObjectDescription>

        </ParticipantObjectIdentification>

        <ParticipantObjectIdentification ParticipantObjectID="P5^^^ISSUER" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">

            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>

            <ParticipantObjectName>TEST^Name</ParticipantObjectName>

        </ParticipantObjectIdentification>

    </AuditMessage>