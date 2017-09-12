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
         "UserIDTypeCode", "U", "Rejection triggered using association : EV ("110119","DCM","Station AE Title")"
         "", "", "Rejection triggered from UI : EV ("12", "RFC-3881", "URI")"
         "UserTypeCode", "U", "'Application' : '2'"
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
         "UserIDTypeCode", "U", "Rejection triggered using archive UI (Secured archive) : EV ("113871","DCM","Person ID")"
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

.. include:: dicom-instances-accessed.xml
   :code: xml