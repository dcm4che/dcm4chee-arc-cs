DICOM Study Deleted
===================

Trigger Events
--------------

This message is emitted by the archive when :
- All Rejected : all objects of a study are rejected using store association or from archive UI.
- Deletion by scheduler : the whole study is deleted by the scheduler.
- Deletion by RESTful service : the whole study is deleted using RESTful service.

Message Structure
-----------------

- :ref:`audit-study-deleted-event`
- :ref:`audit-study-deleted-active-participant-app` (1) - This active participant is present only in Rejection case
- :ref:`audit-study-deleted-active-participant-user` (1)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-study-deleted-participant-object-study` (1)
- :ref:`audit-study-deleted-participant-object-patient` (1)

.. csv-table:: Event: DICOM Study Deleted
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
         "UserIDTypeCode", "U", "Deletion triggered by scheduler : EV ("113877","DCM","Device Name")"
         "", "", "Deletion triggered using RESTful service : EV ("12", "RFC-3881", "URI")"
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
         "UserIDTypeCode", "U", "Deletion triggered using archive UI (Secured archive) : EV ("113871","DCM","Person ID")"
         "", "", "Deletion triggered using archive UI (Unsecured archive) : EV ("110182","DCM","Node ID")"
         "", "", "Deletion triggered using association : EV ("110119","DCM","Station AE Title")"
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
         "ParticipantObjectContainsStudy", "U"
         "StudyIDs", "M", "Study Instance UID"

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

.. include:: dicom-study-deleted.xml
   :code: xml