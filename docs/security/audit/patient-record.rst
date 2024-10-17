Patient Record
==============

Trigger Events
--------------

This message is emitted by the archive whenever :

- Patient is created by UI / HL7 messages / object storage
- Patient record is updated by UI / HL7 message / PDQ Service
- Patient records are deleted by UI / scheduler
- One or more patients are merged by UI / HL7 messages
- HL7 messages (ADT/Order/ORU) accepted (= also not processed) or processed by archive
- HL7 messages (ADT/Order/ORU) forwarded by archive to external HL7 receivers
- Patient created / updated / merged / changePatientID on external archive
- Patient record updated by `Supplement Issuer of PatientID <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/PAM-RS/SupplementIssuerOfPatientID>`_ service.
- Patient record created / updated by `Change Patient associated to Study <https://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/IOCM-RS/MoveStudyToPatient>`_ service.

Message Structure
-----------------

.. csv-table:: Entities in Patient Record Audit Message

    :ref:`event-identification-patient-record`
    :ref:`active-participant-initiator-patient-record`, Not present when patient is deleted by the scheduler
    :ref:`active-participant-archive-patient-record`
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-patient-patient-record`

.. csv-table:: Event: Patient Record
   :name: event-identification-patient-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110110, DCM, 'Patient Record')"
   EventActionCode, M, "| Create : 'C'
   | Update : 'U'
   | Delete : 'D'"
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success : '0'
   | Minor failure : '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator : '4'

.. csv-table:: Active Participant : Initiator
   :name: active-participant-initiator-patient-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| HL7 messages : 'Sending Application and Facility'
   | Triggered from UI : 'Remote IP address' or 'User name of logged in user'
   | Triggered by object storage : 'Calling AE title in association'"
   UserIDTypeCode, U, "| HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI (secured archive) : EV (113871, DCM, 'Person ID')
   | Triggered from UI (unsecured archive) : EV (110182, DCM, 'Node ID')
   | Triggered by object storage : EV (110119, DCM, 'Station AE Title')"
   UserTypeCode, U, "| Triggered from UI : Person : '1'
   | All other cases : Application : '2'"
   UserIsRequestor, M, | true
   RoleIDCode, M, "| EV (110153, DCM, 'Source')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-patient-record
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| HL7 messages : 'Receiving Application and Facility'
   | Triggered from UI : 'Request URI'
   | Triggered by object storage : 'Called AE title in association'
   | Triggered by scheduler : 'Archive device name'"
   UserIDTypeCode, U, "| HL7 messages : EV (HL7APP, 99DCM4CHEE, 'Application and Facility')
   | Triggered from UI : EV (12, RFC-3881, 'URI')
   | Triggered by object storage : EV (110119, DCM, 'Station AE Title')
   | Triggered by scheduler : EV (113877, DCM, 'Device Name')"
   UserTypeCode, U, | Application : '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, "| Patient deletion triggered by scheduler : 'true'
   | All other cases : 'false'"
   RoleIDCode, M, "| EV (110152, DCM, 'Destination')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name : '1'
   | NetworkAccessPointID is an IP address : '2'"

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-patient-record
   :widths: 30, 5, 65, 10
   :header: Field Name, Opt, Description, Note

   ParticipantObjectID, M, Patient ID or <none> if unknown,
   ParticipantObjectTypeCode, M, Person : '1',
   ParticipantObjectTypeCodeRole, M, Patient : '1',
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')",
   ParticipantObjectName, U, Patient Name,
   ParticipantObjectDataLifeCycle, U, Verification ⇒ '4', Present only for audits triggered by PDQ Service
   ParticipantObjectDetail, U, If Patient record created/updated/deleted by HL7 messages : 'type=HL7v2 Message value=<Base-64 encoded HL7 message>'
   ParticipantObjectDetail, U, If Patient record created/updated/deleted by HL7 messages : 'type=HL7v2 Message value=<Base-64 encoded HL7 response>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 message control ID>'
   ParticipantObjectDetail, U, 'type=MSH-9 value=<Base-64 encoded HL7 response message type>'
   ParticipantObjectDetail, U, 'type=MSH-10 value=<Base-64 encoded HL7 response message control ID>'


Sample Messages
---------------

.. toctree::

   patient-record-sample-messages