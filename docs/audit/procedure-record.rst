Procedure Record
================

Trigger Events
--------------

This message is emitted by the archive whenever :

- Modality worklist entry is created by UI or by HL7 messages.
- Modality worklist entry is updated by UI or by HL7 message or by incoming MPPS.
- Modality worklist entry is deleted by UI.
- Study attributes are updated from UI.
- Expiration date is set to study/series from UI.

Message Structure
-----------------

.. csv-table:: Supported Entities in Procedure Record Audit Message

    :ref:`event-identification-procedure-record`
    :ref:`active-participant-initiator-procedure-record`
    :ref:`active-participant-archive-procedure-record`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-procedure-record`
    :ref:`participant-object-patient-procedure-record`

.. csv-table:: Event Identification
   :name: event-identification-procedure-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110111, DCM, 'Procedure Record')"
         "EventActionCode", "M", "Enumerated Value C = Create"
         "", "", "U = Update"
         "", "", "D = Delete"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0':'Success', '4':'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator':'4'"

.. csv-table:: Active Participant : Source
   :name: active-participant-initiator-procedure-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Sending Application and Facility'"
         "", "", "Triggered from UI : 'Remote IP address' or 'User name of logged in user'"
         "", "", "Triggered by MPPS : 'Calling AE title in association'"
         "UserIDTypeCode", "U", "HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
         "", "", "Triggered from UI (secured archive) : EV (113871, DCM, 'Person ID')"
         "", "", "Triggered from UI (unsecured archive) : EV (110182, DCM, 'Node ID')"
         "", "", "Triggered by MPPS : EV (110119, DCM, 'Station AE Title')"
         "UserTypeCode", "U", "Triggered from UI : 'Person' : '1'"
         "", "", "All other cases: 'Application' : '2'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-procedure-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "HL7 messages : 'Receiving Application and Facility'"
         "", "", "Triggered from UI : 'Request URI'"
         "", "", "Triggered by MPPS : 'Called AE title in association'"
         "UserIDTypeCode", "U", "HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')"
         "", "", "Triggered from UI : EV (12, RFC-3881, 'URI')"
         "", "", "Triggered by MPPS : EV (110119, DCM, 'Station AE Title')"
         "UserTypeCode", "U", "'Application' : '2'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1':'NetworkAccessPointID is host name', '2':'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification : Study
   :name: participant-object-study-procedure-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Study Instance UID"
         "ParticipantObjectTypeCode", "M", "'2' : 'System'"
         "ParticipantObjectTypeCodeRole", "M", "'3' : 'Report'"
         "ParticipantObjectIDTypeCode", "M", "EV (110180, DCM, 'Study Instance UID')"
         "ParticipantObjectDetail", "U", "Base-64 encoded study date if Study has StudyDate(0008,0020) attribute"
         "ParticipantObjectDescription", "U"
         "SOPClass", "MC", "Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>"
         "Accession", "U", "Accession Number"

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-procedure-record
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' : 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' : 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"
         "ParticipantObjectDetail", "U", "Base-64 encoded HL7 message type if Patient record was created/updated/deleted by HL7 messages."


Sample Message
--------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    
        <EventIdentification EventActionCode="C" EventDateTime="2017-08-08T14:57:08.989+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110111" codeSystemName="DCM" originalText="Procedure Record"/>
        </EventIdentification>
    
        <ActiveParticipant UserID="MESA_OF|XYZ_RADIOLOGY" UserTypeCode="2" UserIsRequestor="true" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
    
        <ActiveParticipant UserID="MESA_IM|XYZ_IMAGE_MANAGER" UserTypeCode="2" AlternativeUserID="16577" UserIsRequestor="false" NetworkAccessPointID="localhost" NetworkAccessPointTypeCode="1">
            <UserIDTypeCode csd-code="HL7APP" codeSystemName="99DCM4CHEE" originalText="Application and Facility"/>
        </ActiveParticipant>
    
        <AuditSourceIdentification AuditSourceID="dcm4chee-arc">
            <AuditSourceTypeCode csd-code="4"/>
        </AuditSourceIdentification>
    
        <ParticipantObjectIdentification ParticipantObjectID="1.2.392.200036.9125.0.199402091242.1" ParticipantObjectTypeCode="2" ParticipantObjectTypeCodeRole="3">
            <ParticipantObjectIDTypeCode csd-code="110180" originalText="Study Instance UID" codeSystemName="DCM"/>
            <ParticipantObjectDescription>
                <Accession Number="$ACCESSION_NUMBER$"/>
            </ParticipantObjectDescription>
        </ParticipantObjectIdentification>
    
        <ParticipantObjectIdentification ParticipantObjectID="PID1^^^Site A&1.2.40.0.13.1.1.999.111.1111&ISO" ParticipantObjectTypeCode="1" ParticipantObjectTypeCodeRole="1">
            <ParticipantObjectIDTypeCode csd-code="2" originalText="Patient Number" codeSystemName="RFC-3881"/>
            <ParticipantObjectName>TEST^Name</ParticipantObjectName>
        </ParticipantObjectIdentification>
    
    </AuditMessage>