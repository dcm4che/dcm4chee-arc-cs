DICOM Instances Transferred
===========================

Trigger Events
--------------

This message is emitted by the archive in following cases :
- Q/R Move : Objects of a study are retrieved using query/retrieve service and stored to external destination
- Q/R Get : Objects of a study are retrieved using query/retrieve service and stored to the destination which is same as source
- Export : Objects of a study are exported
- WADO RS : Objects of a study are retrieved using WADO RESTful service
- Store : Objects of a study are being stored to the archive
- Storage Commitment of objects of study
- XDSI Retrieve Imaging Document Set RAD-69

Message Structure
-----------------

.. csv-table:: Supported Entities in DICOM Instances Transferred Audit Message

    :ref:`event-identification-instances-transferred`
    :ref:`active-participant-archive-instances-transferred`
    :ref:`active-participant-destination-instances-transferred`
    :ref:`active-participant-other-instances-transferred`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-instances-transferred`
    :ref:`participant-object-patient-instances-transferred`

.. csv-table:: Event Identification
   :name: event-identification-instances-transferred
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110104, DCM, 'DICOM Instances Transferred')"
         "EventActionCode", "M", "Store case : 'C' ⇒ 'Create' or 'U' ⇒ 'Update'"
         "", "", "For all other cases : 'R' ⇒ 'Read'"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0'⇒'Success', '4'⇒'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator'⇒'4'"


.. csv-table:: Active Participant: Archive application
   :name: active-participant-archive-instances-transferred
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Q/R Move case ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Q/R Get case ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Store case ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Storage Commitment case ⇒ 'Application entity title of Archive Device used in the association' or 'Invoked URL'"
         "", "", "Export case ⇒ 'dicomAETitle configured in the Exporter of archive'"
         "", "", "Export case triggered by scheduler ⇒ 'Archive device name'"
         "", "", "WADO RS case ⇒ 'Invoked URL'"
         "", "", "XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'Invoked URL'"
         "UserIDTypeCode", "U", "Q/R Move case : EV (110119, DCM, 'Station AE Title')"
         "", "", "Q/R Get case : EV (110119, DCM, 'Station AE Title')"
         "", "", "Export case triggered by scheduler : EV (113877, DCM, 'Device Name')"
         "", "", "Export case triggered from UI : EV (12, RFC-3881, 'URI')"
         "", "", "WADO RS case : EV (12, RFC-3881, 'URI')"
         "", "", "XDSI Retrieve Imaging Document Set RAD-69 case : EV (12, RFC-3881, 'URI')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Destination
   :name: active-participant-destination-instances-transferred
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Q/R Move case ⇒ 'Application entity title of destination system'"
         "", "", "Q/R Get case ⇒ 'Application entity title of initiating system'"
         "", "", "Store case ⇒ 'Application entity title of Device storing the study objects to archive'"
         "", "", "Storage Commitment case ⇒ 'Remote IP address' or 'User name of logged in user'"
         "", "", "Export case ⇒ 'dicomAETitle of destination'"
         "", "", "WADO RS case ⇒ 'Remote IP address' or 'User name of logged in user'"
         "", "", "XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'Remote IP address' or 'User name of logged in user'"
         "UserIDTypeCode", "U", "Q/R Move case : EV (110119, DCM, 'Station AE Title')"
         "", "", "Q/R Get case : EV (110119, DCM, 'Station AE Title')"
         "", "", "Export case : EV (110119, DCM, 'Station AE Title')"
         "", "", "WADO RS case secured archive : EV (113871, DCM, 'Person ID')"
         "", "", "WADO RS case unsecured archive : EV (110182, DCM, 'Node ID')"
         "UserTypeCode", "U", "WADO RS case : 'Person' : '1'"
         "", "", "For all other cases : 'Application' : '2'"
         "UserIsRequestor", "M", "'true' for all cases except Q/R Move case"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Other
   :description: This active participant is present only in Q/R Move case
   :name: active-participant-other-instances-transferred
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Application entity title of initiating system"
         "UserIDTypeCode", "U", "EV (110119, DCM, 'Station AE Title')"
         "UserTypeCode", "U", "'Application' : '2'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of initiating system"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Study
   :name: participant-object-study-instances-transferred
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
   :name: participant-object-patient-instances-transferred
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