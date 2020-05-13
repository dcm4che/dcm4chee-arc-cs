Begin Transferring DICOM Instances
==================================
This message describes the event of a system beginning to transfer a set of DICOM instances from one node to another node
within control of the system's security domain. This message may only include information about a single patient.

Trigger Events
--------------

This message is emitted by the archive in following cases :

- Query/Retrieve of objects using `RAD-16 <http://ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf#page=204>`_
    - C-Move : Objects of a study are retrieved using query/retrieve service and stored to external destination
    - C-Get : Objects of a study are retrieved using query/retrieve service and stored to the destination which is same as source
- Export : Objects of a study are exported to a destination
- Invoking `WADO-RS <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/WADO-RS>`_
  or `WADO URI <http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/openapi.json#/WADO-URI>`_
  services
- XDSI Retrieve Imaging Document Set `RAD-69 <http://ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol3.pdf#page=184>`_ transaction

Message Structure
-----------------

.. csv-table:: Entities in Begin Transferring DICOM Instances Audit Message

    :ref:`event-identification-begin-transferring`
    :ref:`active-participant-archive-begin-transferring`
    :ref:`active-participant-destination-begin-transferring`
    :ref:`active-participant-other-begin-transferring`, Present only in Query/Retrieve C-Move case
    :ref:`active-participant-user-begin-transferring`, Present only in Export case triggered from UI
    :ref:`audit-general-message-audit-source`
    :ref:`participant-object-study-begin-transferring`
    :ref:`participant-object-patient-begin-transferring`

.. csv-table:: Event Identification
   :name: event-identification-begin-transferring
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   EventID, M, "| EV (110100, DCM, 'Begin Transferring DICOM Instances')"
   EventActionCode, M, | Execute ⇒ 'E'
   EventDateTime, M, | The time at which the event occurred
   EventOutcomeIndicator, M, "| Success ⇒ '0'
   | Minor failure ⇒ '4'"
   EventOutcomeDescription, M, | Error/Exception message when EventOutcomeIndicator ⇒ '4'


.. csv-table:: Active Participant : Archive application
   :name: active-participant-archive-begin-transferring
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Q/R Move case ⇒ 'Application entity title of Archive Device used in the association'
   | Q/R Get case ⇒ 'Application entity title of Archive Device used in the association'
   | Export case triggered by scheduler ⇒ 'Archive device name'
   | Export case triggered from UI ⇒ 'Invoked URL'
   | WADO RS case ⇒ 'Invoked URL'
   | XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'Invoked URL'"
   UserIDTypeCode, U, "| Q/R Move case ⇒ EV (110119, DCM, 'Station AE Title')
   | Q/R Get case ⇒ EV (110119, DCM, 'Station AE Title')
   | Export case triggered by scheduler ⇒ EV (113877, DCM, 'Device Name')
   | Export case triggered from UI ⇒ EV (12, RFC-3881, 'URI')
   | WADO RS case ⇒ EV (12, RFC-3881, 'URI')
   | XDSI Retrieve Imaging Document Set RAD-69 case ⇒ EV (12, RFC-3881, 'URI')"
   UserTypeCode, U, | Application ⇒ '2'
   AlternativeUserID, MC, | Process ID of Audit logger
   UserIsRequestor, M, "| Export case : Triggered by scheduler ⇒ 'true'
   | All other cases ⇒ 'false'"
   RoleIDCode, M, "| EV (110153, DCM, 'Source')"
   NetworkAccessPointID, U, | Hostname/IP Address of the connection referenced by Audit logger
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Destination
   :name: active-participant-destination-begin-transferring
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, "| Q/R Move case ⇒ 'Application entity title of destination system'
   | Q/R Get case ⇒ 'Application entity title of initiating system'
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
   RoleIDCode, M, "| EV (110152, DCM, 'Destination')"
   NetworkAccessPointID, U, | Hostname/IP Address of calling host
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : Other
   :name: active-participant-other-begin-transferring
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   UserID, M, | Application entity title of initiating system
   UserIDTypeCode, U, "| EV (110119, DCM, 'Station AE Title')"
   UserTypeCode, U, | Application ⇒ '2'
   UserIsRequestor, M, | true
   NetworkAccessPointID, U, | Hostname/IP Address of initiating system
   NetworkAccessPointTypeCode, U, "| NetworkAccessPointID is host name ⇒ '1'
   | NetworkAccessPointID is an IP address ⇒ '2'"

.. csv-table:: Active Participant : User
   :name: active-participant-user-begin-transferring
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

.. csv-table:: Participant Object Identification : Study
   :name: participant-object-study-begin-transferring
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Study Instance UID
   ParticipantObjectTypeCode, M, System ⇒ '2'
   ParticipantObjectTypeCodeRole, M, Report ⇒ '3'
   ParticipantObjectIDTypeCode, M, "EV (110180, DCM, 'Study Instance UID')"
   ParticipantObjectDetail, U, "Base-64 encoded study date if Study has StudyDate(0008,0020) attribute"
   ParticipantObjectDescription, U
   SOPClass, MC, Sop Class UID and Number of instances with this sop class. eg. <SOPClass UID='1.2.840.10008.5.1.4.1.1.88.22' NumberOfInstances='4'/>
   Accession, U, Accession Number

.. csv-table:: Participant Object Identification : Patient
   :name: participant-object-patient-begin-transferring
   :widths: 30, 5, 65
   :header: Field Name, Opt, Description

   ParticipantObjectID, M, Patient ID
   ParticipantObjectTypeCode, M, Person ⇒ '1'
   ParticipantObjectTypeCodeRole, M, Patient ⇒ '1'
   ParticipantObjectIDTypeCode, M,  "EV (2, RFC-3881, 'Patient Number')"
   ParticipantObjectName, U, Patient Name


Sample Message
--------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AuditMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.dcm4che.org/DICOM/audit-message.rnc">
    
        <EventIdentification EventActionCode="E" EventDateTime="2016-06-21T10:22:00.634+02:00" EventOutcomeIndicator="0">
            <EventID csd-code="110102" codeSystemName="DCM" originalText="Begin Transferring DICOM Instances"/>
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
