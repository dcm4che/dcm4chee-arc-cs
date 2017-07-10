General Message Format Conventions
==================================

Message Structure
-----------------

- :ref:`audit-general-message-event`
- :ref:`audit-general-message-active-participant` (1..N)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-general-message-participant-object` (0..N)

.. csv-table:: Event
   :name: audit-general-message-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description", "Additional Conditions on Field Format/Value"

   "EventID", "M", "Identifier for a specific audited event.", "The identifier for the family of event. E.g., 'User Authentication'"
   "EventActionCode", "M", "Indicator for type of action performed during the event that generated the audit.", "'C'⇒'Create a new database object, such as Placing an Order'"
   "", "", "", "'R'⇒'Read/View/Print/Query Display or print data, such as a Doctor Census'"
   "", "", "", "'U'⇒'Update data, such as Revise Patient Information'"
   "", "", "", "'D'⇒'Delete items, such as a master file record'"
   "", "", "", "'E'⇒'Perform a system or application function such as log-on, program execution, or use of an object's method'"
   "EventDateTime", "M", "Universal coordinated time (UTC), i.e., a date/time specification that is unambiguous as to local time zones.", "The time at which the audited event occurred"
   "EventOutcomeIndicator", "M", "Indicates whether the event succeeded or failed.", "'0'⇒'SUCCESS', '4'⇒'Minor failure'"
   "EventOutcomeDescription", "U", "In failure cases, indicates the exception or error message."
   "EventTypeCode", "M", "Identifier for the category of event.", "The specific type(s) within the family applicable to the event, e.g., "User Login"."


.. csv-table:: Active Participant
   :name: audit-general-message-active-participant
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

   "UserID", "M", "Unique identifier for the user actively participating in the event."
   "AlternativeUserID", "U", "Alternative unique identifier for the user."
   "UserName", "U", "The human-meaningful name for the user."
   "UserIsRequestor", "M", "Indicator that the user is or is not the requestor, or initiator, for the event being audited."
   "RoleIDCode", "U", "Specification of the role(s) the user plays when performing the event, as assigned in role-based access control security."
   "NetworkAccessPointTypeCode", "U", "An identifier for the type of network access point."
   "NetworkAccessPointID", "M", "An identifier for the network access point of the user device This could be a device id, IP address, or some other identifier associated with a device."


.. csv-table:: Audit Source
   :name: audit-general-message-audit-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

   "AuditEnterpriseSiteID", "U", "Logical source location within the healthcare enterprise network, e.g., a hospital or other provider location within a multi-entity provider group."
   "AuditSourceID", "M", "Identifier of the source."
   "AuditSourceTypeCode", "M", "Code specifying the type of source."

.. csv-table:: Participant Object
   :name: audit-general-message-participant-object
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description", "Additional Conditions on Field Format/Value"

   "ParticipantObjectTypeCode", "U", "Code for the participant object type being audited. This value is distinct from the user's role or any user relationship to the participant object.", "'1'⇒'Person'"
   "", "", "", "'2'⇒'System Object'"
   "", "", "", "'3'⇒'Organization'"
   "", "", "", "'4'⇒'Other'"
   "ParticipantObjectTypeCode", "U", "Code representing the functional application role of Participant Object being audited."
   "ParticipantObjectDataLifeCycle", "U", "Identifier for the data life-cycle stage for the participant object. This can be used to provide an audit trail for data, over time, as it passes through the system."
   "ParticipantObjectIDTypeCode", "M", "Describes the identifier that is contained in Participant Object ID."
   "ParticipantObjectSensitivity", "U", "Denotes policy-defined sensitivity for the Participant Object ID such as VIP, HIV status, mental health status, or similar topics."
   "ParticipantObjectID", "M", "Identifies a specific instance of the participant object."
   "ParticipantObjectName", "U", "An instance-specific descriptor of the Participant Object ID audited, such as a person's name."
   "ParticipantObjectQuery", "U", "The actual query for a query-type participant object."
   "ParticipantObjectDetail", "U", "Implementation-defined data about specific details of the object accessed or used.", "This element is a Type-value pair. The "type" attribute is an implementation-defined text string. The "value" attribute is base 64 encoded data. The value is suitable for conveying binary data."
   "SOPClass", "MC", "", "The UIDs of SOP classes referred to in this participant object. Required if ParticipantObjectIDTypeCode is (110180, DCM, 'Study Instance UID') and any of the optional fields (AccessionNumber, ContainsMPPS, NumberOfInstances, ContainsSOPInstances,Encrypted,Anonymized) are present in this Participant Object. May be present if ParticipantObjectIDTypeCode is (110180, DCM, 'Study Instance UID') even though none of the optional fields are present."
   "Accession", "U", "", "An Accession Number(s) associated with this participant object."
   "MPPS", "U", "", "An MPPS Instance UID(s) associated with this participant object."
   "NumberOfInstances", "U", "", "The number of SOP Instances referred to by this participant object."
   "Instance", "U", "", "SOP Instance UID value(s)"
   "Encrypted", "U", "", "A single value of True or False indicating whether or not the data was encrypted."
   "Anonymized", "U", "", "A single value of True or False indicating whether or not all patient identifying information was removed from the data"
   "ParticipantObjectContainsStudy", "U", "", "A Study Instance UID, which may be used when the ParticipantObjectIDTypeCode is not (110180, DCM, "Study Instance UID")."
