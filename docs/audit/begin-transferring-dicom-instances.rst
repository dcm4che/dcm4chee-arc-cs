Begin Transferring DICOM Instances
==================================
This message describes the event of a system beginning to transfer a set of DICOM instances from one node to another node
within control of the system's security domain. This message may only include information about a single patient.

Trigger Events
--------------

This message is emitted by the archive in following cases :
- Q/R Move : Objects of a study are retrieved using query/retrieve service and stored to external destination
- Q/R Get : Objects of a study are retrieved using query/retrieve service and stored to the destination which is same as source
- Export : Objects of a study are exported by scheduler or synchronously or by queuing
- WADO RS : Objects of a study are retrieved using WADO RESTful service
- XDSI Retrieve Imaging Document Set RAD-69

Message Structure
-----------------

- :ref:`audit-begin-transferring-event`
- :ref:`audit-begin-transferring-active-participant-app` (1)
- :ref:`audit-begin-transferring-active-participant-destination` (1)
- :ref:`audit-begin-transferring-active-participant-other` (1) - This active participant is present only in the Q/R Move case.
- :ref:`audit-general-message-audit-source`
- :ref:`audit-begin-transferring-participant-object-study` (0..1)
- :ref:`audit-begin-transferring-participant-object-patient` (1)

.. csv-table:: Event: Begin Transferring DICOM Instances
   :name: audit-begin-transferring-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "EV (110100, DCM, 'Begin Transferring DICOM Instances')"
         "EventActionCode", "M", "Enumerated Value E = Execute"
         "EventDateTime", "M", "The time at which the event occurred"
         "EventOutcomeIndicator", "M", "'0'⇒'Success', '4'⇒'Minor failure'"
         "EventOutcomeDescription", "M", "Error/Exception message when 'EventOutcomeIndicator'⇒'4'"


.. csv-table:: Active Participant: Archive application
   :name: audit-begin-transferring-active-participant-app
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Q/R Move case ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Q/R Get case ⇒ 'Application entity title of Archive Device used in the association'"
         "", "", "Export case triggered by scheduler ⇒ 'dicomAETitle configured in the Exporter of archive'"
         "", "", "Export case triggered from UI ⇒ 'Invoked URL'"
         "", "", "WADO RS case ⇒ 'Invoked URL'"
         "", "", "XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'Invoked URL'"
         "UserIDTypeCode", "U", "Q/R Move case : EV ("110118","DCM","Archive Device AE Titles")"
         "", "", "Q/R Get case : EV ("110118","DCM","Archive Device AE Titles")"
         "", "", "Export case triggered by scheduler : EV ("110118","DCM","Archive Device AE Titles")"
         "", "", "Export case triggered from UI : EV ("12", "RFC-3881", "URI")"
         "", "", "WADO RS case : EV ("12", "RFC-3881", "URI")"
         "", "", "XDSI Retrieve Imaging Document Set RAD-69 case : EV ("12", "RFC-3881", "URI")"
         "UserTypeCode", "U", "'System' : '5'"
         "AlternativeUserID", "MC", "Process ID of Audit logger"
         "UserIsRequestor", "M", "false"
         "RoleIDCode", "M", "EV (110153, DCM, 'Source')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of the connection referenced by Audit logger"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Destination
   :name: audit-begin-transferring-active-participant-destination
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Q/R Move case ⇒ 'Application entity title of destination system'"
         "", "", "Q/R Get case ⇒ 'Application entity title of initiating system'"
         "", "", "Export case ⇒ 'dicomAETitle of destination'"
         "", "", "WADO RS case ⇒ 'Remote IP address' or 'User name of logged in user'"
         "", "", "XDSI Retrieve Imaging Document Set RAD-69 case ⇒ 'Remote IP address' or 'User name of logged in user'"
         "UserIsRequestor", "M", "Q/R Move case ⇒ 'false'"
         "", "", "Q/R Get case ⇒ 'true'"
         "", "", "Export case ⇒ 'true'"
         "", "", "WADO RS case ⇒ 'true'"
         "UserIDTypeCode", "U", "Q/R Move case : EV ("110119","DCM","Station AE Title")"
         "", "", "Q/R Get case : EV ("110119","DCM","Station AE Title")"
         "", "", "Export case : EV ("110119","DCM","Station AE Title")"
         "", "", "WADO RS case secured archive : EV ("Cp1640-1","DCM","Local User ID")"
         "", "", "WADO RS case unsecured archive : EV ("110182","DCM","Node ID")"
         "UserTypeCode", "U", "WADO RS case'Person' : '1'"
         "", "", "For all other cases : 'System' : '5'"
         "RoleIDCode", "M", "EV (110152, DCM, 'Destination')"
         "NetworkAccessPointID", "U", "Hostname/IP Address of calling host"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Active Participant: Other
   :name: audit-begin-transferring-active-participant-other
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "UserID", "M", "Application entity title of initiating system"
         "UserIDTypeCode", "U", "EV ("110119","DCM","Station AE Title")"
         "UserTypeCode", "U", "'System' : '5'"
         "UserIsRequestor", "M", "true"
         "NetworkAccessPointID", "U", "Hostname/IP Address of initiating system"
         "NetworkAccessPointTypeCode", "U", "'1'⇒'NetworkAccessPointID is host name', '2'⇒'NetworkAccessPointID is an IP address'"

.. csv-table:: Participant Object Identification: Study
   :name: audit-begin-transferring-participant-object-study
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
   :name: audit-begin-transferring-participant-object-patient
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "ParticipantObjectID", "M", "Patient ID"
         "ParticipantObjectTypeCode", "M", "'1' ⇒ 'Person'"
         "ParticipantObjectTypeCodeRole", "M", "'1' ⇒ 'Patient'"
         "ParticipantObjectIDTypeCode", "M", "EV (2, RFC-3881, 'Patient Number')"
         "ParticipantObjectName", "U", "Patient Name"


Sample XML Message
------------------

.. include:: begin-transferring-dicom-instances.xml
   :code: xml