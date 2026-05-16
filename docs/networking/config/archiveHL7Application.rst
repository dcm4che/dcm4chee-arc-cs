Archive HL7 Application
=======================
DICOM Archive HL7 Application related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive HL7 Application Attributes (LDAP Object: dcmArchiveHL7Application)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomAETitle:
    .. _archiveHL7Application-dicomAETitle:

    :ref:`AE Title <archiveHL7Application-dicomAETitle>`",string,"Archive AE Title associated with this HL7 Application.

    (dicomAETitle)"
    "
    .. _dcmRecordAttributeModification:
    .. _archiveHL7Application-dcmRecordAttributeModification:

    :ref:`Record Attribute Modification <archiveHL7Application-dcmRecordAttributeModification>`",boolean,"Indicates if modifications of attributes of stored objects by this HL7 Application are recorded in Items of the Original Attributes Sequence. Overwrites value specified on Device level.

    (dcmRecordAttributeModification)"
    "
    .. _dcmMWLWorklistLabel:
    .. _archiveHL7Application-dcmMWLWorklistLabel:

    :ref:`MWL Worklist Label <archiveHL7Application-dcmMWLWorklistLabel>`",string,"Value of Worklist Label (0074,1202) of created MWL items on receive of HL7 Order messages. If absent, created MWL items are not bound to a particular MWL Worklist and are provided by all Archive AEs with MWL SCP Transfer Capability.

    (dcmMWLWorklistLabel)"
    "
    .. _dcmMWLAccessionNumberGenerator:
    .. _archiveHL7Application-dcmMWLAccessionNumberGenerator:

    :ref:`MWL Accession Number Generator <archiveHL7Application-dcmMWLAccessionNumberGenerator>`",string,"Identifies ID Generator to supplement missing Accession Numbers of Scheduled Procedures Steps created on receive of HL7 Order messages. Overwrites value specified on Device level.

    (dcmMWLAccessionNumberGenerator)"
    "
    .. _dcmMWLRequestedProcedureIDGenerator:
    .. _archiveHL7Application-dcmMWLRequestedProcedureIDGenerator:

    :ref:`MWL Requested Procedure ID Generator <archiveHL7Application-dcmMWLRequestedProcedureIDGenerator>`",string,"Identifies ID Generator to supplement missing Requested Procedure IDs of Scheduled Procedures Steps created on receive of HL7 Order messages. Overwrites value specified on Device level.

    (dcmMWLRequestedProcedureIDGenerator)"
    "
    .. _dcmMWLScheduledProcedureStepIDGenerator:
    .. _archiveHL7Application-dcmMWLScheduledProcedureStepIDGenerator:

    :ref:`MWL Scheduled Procedure Step ID Generator <archiveHL7Application-dcmMWLScheduledProcedureStepIDGenerator>`",string,"Identifies ID Generator to supplement missing Scheduled Procedure Step IDs of Scheduled Procedures Steps created on receive of HL7 Order messages. Overwrites value specified on Device level.

    (dcmMWLScheduledProcedureStepIDGenerator)"
    "
    .. _dcmAuditHL7MsgLimit:
    .. _archiveHL7Application-dcmAuditHL7MsgLimit:

    :ref:`Audit HL7 Message Limit <archiveHL7Application-dcmAuditHL7MsgLimit>`",integer,"Limit length of HL7 messages included in emitted Audit Records. Overwrites value specified on Device level.

    (dcmAuditHL7MsgLimit)"
    "
    .. _hl7ORUAction:
    .. _archiveHL7Application-hl7ORUAction:

    :ref:`HL7 ORU Action(s) <archiveHL7Application-hl7ORUAction>`",string,"Specifies action on receive of HL7 ORU^R01 message. Overwrites value specified on Device level.

    Enumerated values:

    IMPORT_REPORT (= Transcode received HL7 ORU^R01 to DICOM SR or PDF or CDA)

    MWL_COMPLETED (= Set Status of matching MWL items to COMPLETED)

    (hl7ORUAction)"
    "
    .. _hl7PatientUpdateTemplateURI:
    .. _archiveHL7Application-hl7PatientUpdateTemplateURI:

    :ref:`HL7 Patient Update Template URI <archiveHL7Application-hl7PatientUpdateTemplateURI>`",string,"Specifies URI for the style sheet used by HL7v2 Patient Update Service. Overwrites value specified on Device level.

    (hl7PatientUpdateTemplateURI)"
    "
    .. _hl7ImportReportTemplateURI:
    .. _archiveHL7Application-hl7ImportReportTemplateURI:

    :ref:`HL7 Import Report Template URI <archiveHL7Application-hl7ImportReportTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORU^R01 to DICOM SR. Overwrites value specified on Device level.

    (hl7ImportReportTemplateURI)"
    "
    .. _hl7ImportReportTemplateParam:
    .. _archiveHL7Application-hl7ImportReportTemplateParam:

    :ref:`HL7 Import Report Template Parameter(s) <archiveHL7Application-hl7ImportReportTemplateParam>`",string,"XSLT parameters passed to style sheet specified by HL7 Import Report Template URI. Format: {name}={value}. E.g.: 'langCodeValue=et', 'langCodingSchemeDesignator=RFC5646', 'langCodeMeaning=Estonian'. Overwrites value specified on Device level.

    (hl7ImportReportTemplateParam)"
    "
    .. _hl7ScheduleProcedureTemplateURI:
    .. _archiveHL7Application-hl7ScheduleProcedureTemplateURI:

    :ref:`HL7 Schedule Procedure Template URI <archiveHL7Application-hl7ScheduleProcedureTemplateURI>`",string,"Specifies URI for the style sheet to transcode received HL7 ORM^O01, OMI^O23, OMG^O19 to DICOM MWL items. Overwrites value specified on Device level.

    (hl7ScheduleProcedureTemplateURI)"
    "
    .. _hl7ScheduledProtocolCodeInOrder:
    .. _archiveHL7Application-hl7ScheduledProtocolCodeInOrder:

    :ref:`HL7 Schedule Protocol Code in Order <archiveHL7Application-hl7ScheduledProtocolCodeInOrder>`",string,"Specifies location of Scheduled Protocol Code in received HL7 Order message. Overwrites value specified on Device level.

    Enumerated values:

    OBR_4_1 (= HL7 Schedule Protocol Code in Order in OBR.4.1 to OBR.4.3)

    OBR_4_4 (= HL7 Schedule Protocol Code in Order in OBR.4.4 to OBR.4.6)

    (hl7ScheduledProtocolCodeInOrder)"
    "
    .. _hl7ScheduledStationAETInOrder:
    .. _archiveHL7Application-hl7ScheduledStationAETInOrder:

    :ref:`HL7 Schedule Station AET in Order <archiveHL7Application-hl7ScheduledStationAETInOrder>`",string,"Specifies location of Scheduled Station AE Title in received HL7 Order message. Should not be configured for HL7 v2.5.1 OMI^O23 with IPC segment. Overwrites value specified on Device level.

    Enumerated values:

    ORC_18 (= HL7 Schedule Station AET in Order in ORC.18)

    (hl7ScheduledStationAETInOrder)"
    "
    .. _hl7LogFilePattern:
    .. _archiveHL7Application-hl7LogFilePattern:

    :ref:`HL7 Log File Pattern <archiveHL7Application-hl7LogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received. If absent, there is no logging. Overwrites value specified on Device level. eg. ${jboss.server.data.dir}/hl7/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7LogFilePattern)"
    "
    .. _hl7ErrorLogFilePattern:
    .. _archiveHL7Application-hl7ErrorLogFilePattern:

    :ref:`HL7 Error Log File Pattern <archiveHL7Application-hl7ErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as received, when processing of HL7 messages fails. If absent, there is no logging. Overwrites value specified on Device level. eg. ${jboss.server.data.dir}/hl7-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7ErrorLogFilePattern)"
    "
    .. _hl7OutgoingLogFilePattern:
    .. _archiveHL7Application-hl7OutgoingLogFilePattern:

    :ref:`HL7 Outgoing Log File Pattern <archiveHL7Application-hl7OutgoingLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as sent. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-out/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7OutgoingLogFilePattern)"
    "
    .. _hl7OutgoingErrorLogFilePattern:
    .. _archiveHL7Application-hl7OutgoingErrorLogFilePattern:

    :ref:`HL7 Outgoing Error Log File Pattern <archiveHL7Application-hl7OutgoingErrorLogFilePattern>`",string,"Path to HL7 messages which will be captured exactly as sent, when processing of sent HL7 messages fails. If absent, there is no logging. May be overwritten by configured values for particular Archive HL7 Application. eg. ${jboss.server.data.dir}/hl7-out-error/${date,yyyy/MM/dd}/${SerialNo}-${MSH-9}.hl7

    (hl7OutgoingErrorLogFilePattern)"
    "
    .. _hl7NoPatientCreateMessageType:
    .. _archiveHL7Application-hl7NoPatientCreateMessageType:

    :ref:`HL7 No Patient Create Message Type(s) <archiveHL7Application-hl7NoPatientCreateMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of HL7 messages which are only processed, if there is already a Patient record in the database, which Patient ID matches the Patient ID in the PID or MRG segment of the message. Thus no new Patient record will be created by messages of the specified types. Overwrites value specified on Device level.

    (hl7NoPatientCreateMessageType)"
    "
    .. _hl7NoPatientUpdateMessageType:
    .. _archiveHL7Application-hl7NoPatientUpdateMessageType:

    :ref:`HL7 No Patient Update Message Type(s) <archiveHL7Application-hl7NoPatientUpdateMessageType>`",string,"Patient record will be not be updated by HL7 messages of specified Message Type(s) (MessageType^TriggerEvent). Overwrites value specified on Device level.

    (hl7NoPatientUpdateMessageType)"
    "
    .. _hl7PatientArrivalMessageType:
    .. _archiveHL7Application-hl7PatientArrivalMessageType:

    :ref:`HL7 Patient Arrival Message Type <archiveHL7Application-hl7PatientArrivalMessageType>`",string,"Message Type of HL7 messages which triggers the change the status of Scheduled Procedure Steps associated with the Patient from SCHEDULED to ARRIVED. Overwrite value specified on Device level.

    Enumerated values:

    ADT^A10 (= Patient Arriving / Tracking)

    (hl7PatientArrivalMessageType)"
    "
    .. _hl7UseNullValue:
    .. _archiveHL7Application-hl7UseNullValue:

    :ref:`Use HL7 Null Value <archiveHL7Application-hl7UseNullValue>`",boolean,"Specifies if HL7 v2 null values (specified in segment field as `|""""|`) are used in sent HL7 messages for not present or empty entity attributes. Required to unset entity attributes at the remote HL7 Application. Overwrites value specified on Device level.

    (hl7UseNullValue)"
    "
    .. _hl7VeterinaryUsePatientName:
    .. _archiveHL7Application-hl7VeterinaryUsePatientName:

    :ref:`HL7 Veterinary use Patient Name <archiveHL7Application-hl7VeterinaryUsePatientName>`",boolean,"Indicates to force veterinary use of Patient Names on mapping HL7 PID fields to DICOM attributes: only use the first two components of PID.5 as DICOM Patient Name; if PID.5 only contains one component, use that value as given name, and the first component of PID.9 as family name of the DICOM Patient Name. Overwrites value specified on Device level.

    (hl7VeterinaryUsePatientName)"
    "
    .. _hl7PrimaryAssigningAuthorityOfPatientID:
    .. _archiveHL7Application-hl7PrimaryAssigningAuthorityOfPatientID:

    :ref:`HL7 Primary Assigning Authority of Patient ID <archiveHL7Application-hl7PrimaryAssigningAuthorityOfPatientID>`",string,"Assigning Authority of Patient ID in received HL7 message used to search primary qualified patient identifier in the list of identifiers in PID-3 / MRG.1. This qualified patient identifier shall be used on the root dataset. If absent, by default the first patient identifier pair in PID-3 / MRG.1 shall be used as primary patient identifier on root dataset. If none of the qualified patient identifiers in the list match with the configured issuer, archive server log shall contain a log INFO message and by default the first qualified patient identifier in PID-3 / MRG.1 shall be used. Format: {Issuer of Patient ID}[&{UniversalEntityID}&{UniversalEntityIDType}]. Overwrites value specified on Device level.

    (hl7PrimaryAssigningAuthorityOfPatientID)"
    "
    .. _hl7OtherPatientIDs:
    .. _archiveHL7Application-hl7OtherPatientIDs:

    :ref:`HL7 Other Patient IDs <archiveHL7Application-hl7OtherPatientIDs>`",string,"Specifies inclusion policy for patient identifiers in PID-3 / MRG-1 of HL7 message in Other Patient IDs Sequence (0010,1002). Overwrites value specified on Device level.

    Enumerated values:

    ALL (= Include all patient identifiers in PID.3 / MRG.1, including patient identifier on root dataset in Other Patient IDs Sequence (0010,1002))

    NONE (= Include no patient identifiers from PID.3 / MRG.1 in Other Patient IDs Sequence (0010,1002))

    OTHER (= Include all patient identifiers in PID.3 / MRG.1, except patient identifier on root dataset in Other Patient IDs Sequence (0010,1002))

    (hl7OtherPatientIDs)"
    "
    .. _hl7OrderMissingStudyIUIDPolicy:
    .. _archiveHL7Application-hl7OrderMissingStudyIUIDPolicy:

    :ref:`HL7 Order Missing Study Instance UID Policy <archiveHL7Application-hl7OrderMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Order messages. Overwrites value specified on Device level.

    Enumerated values:

    REJECT (= Reject HL7 Order Messages with missing Study Instance UID in ZDS.1 / IPC.3)

    GENERATE (= Generate random Study Instance UID if missing in HL7 Order Messages in ZDS.1 / IPC.3)

    ACCESSION_BASED (= Generate Study Instance UID based on Accession Number present in OBR.18 / IPC.1 if Study Instance UID missing in HL7 Order Messages in ZDS.1 / IPC.3)

    (hl7OrderMissingStudyIUIDPolicy)"
    "
    .. _hl7OrderMissingAdmissionIDPolicy:
    .. _archiveHL7Application-hl7OrderMissingAdmissionIDPolicy:

    :ref:`HL7 Order Missing Admission ID Policy <archiveHL7Application-hl7OrderMissingAdmissionIDPolicy>`",string,"Specifies policy on incoming HL7 Order messages without a value for PID-18 Patient Account Number nor field PV1-19 Visit Number. Overwrites value specified on Device level.

    Enumerated values:

    ACCEPT (= Accept HL7 Order Messages with missing Admission ID in PV1.19 / PID.18)

    REJECT (= Reject HL7 Order Messages with missing Admission ID in PV1.19 / PID.18)

    ACCESSION_AS_ADMISSION (= Use Accession Number present in OBR.18 / IPC.1 as Admission ID if it is missing in HL7 Order Message in PV1.19 / PID.18)

    (hl7OrderMissingAdmissionIDPolicy)"
    "
    .. _hl7ImportReportMissingStudyIUIDPolicy:
    .. _archiveHL7Application-hl7ImportReportMissingStudyIUIDPolicy:

    :ref:`HL7 Import Report Missing Study Instance UID Policy <archiveHL7Application-hl7ImportReportMissingStudyIUIDPolicy>`",string,"Specifies policy for missing Study Instance UID in incoming HL7 Import Report (ORU) messages. Overwrites value specified on Device level.

    Enumerated values:

    REJECT (= Reject HL7 ORU^R01 message with missing Study Instance UID in OBX.5 for OBX segment with OBX.3 as 'Study Instance UID' / 'DICOM Study')

    GENERATE (= Generate random Study Instance UID if it is missing in HL7 ORU^R01 Message in OBX.5 for OBX segment with OBX.3 as 'Study Instance UID' / 'DICOM Study')

    ACCESSION_BASED (= Generate Study Instance UID based on Accession Number present in OBR.18 if Study Instance UID missing in HL7 ORU^R01 Messages in OBX.5 for OBX segment with OBX.3 as 'Study Instance UID' / 'DICOM Study')

    (hl7ImportReportMissingStudyIUIDPolicy)"
    "
    .. _hl7ImportReportMissingAdmissionIDPolicy:
    .. _archiveHL7Application-hl7ImportReportMissingAdmissionIDPolicy:

    :ref:`HL7 Import Report Missing Admission ID Policy <archiveHL7Application-hl7ImportReportMissingAdmissionIDPolicy>`",string,"Specifies policy on incoming HL7 ImportReport (ORU) messages without a value for PID-18 Patient Account Number nor field PV1-19 Visit Number. Overwrites value specified on Device level.

    Enumerated values:

    ACCEPT (= Accept HL7 ORU^R01 Messages with missing Admission ID in PV1.19 / PID.18)

    REJECT (= Reject HL7 ORU^R01 Messages with missing Admission ID in PV1.19 / PID.18)

    ACCESSION_AS_ADMISSION (= Use Accession Number present in OBR.18 as Admission ID if it is missing in HL7 ORU^R01 Message in PV1.19 / PID.18)

    (hl7ImportReportMissingAdmissionIDPolicy)"
    "
    .. _hl7ImportReportMissingStudyIUIDCFindSCP:
    .. _archiveHL7Application-hl7ImportReportMissingStudyIUIDCFindSCP:

    :ref:`HL7 Import Report Missing Study Instance UID C-FIND SCP <archiveHL7Application-hl7ImportReportMissingStudyIUIDCFindSCP>`",string,"AE Title of external C-FIND SCP to query for missing Study Instance UID in incoming HL7 Import Report (ORU) messages by given Accession Number. Overwrites value specified on Device level.

    (hl7ImportReportMissingStudyIUIDCFindSCP)"
    "
    .. _hl7ImportReportAdjustIUID:
    .. _archiveHL7Application-hl7ImportReportAdjustIUID:

    :ref:`HL7 Import Report Adjust Instance UID <archiveHL7Application-hl7ImportReportAdjustIUID>`",string,"Specifies adjustment of Series and SOP Instances UIDs returned by XSLT on incoming HL7 Import Report (ORU) messages. Overwrites value specified on Device level.

    Enumerated values:

    NONE (= No adjustment done to Study / Series / SOP IUIDs)

    APPEND_HASH_OF_STUDY_INSTANCE_UID (= Hash of Study Instance UID appended as suffix to Study / Series / SOP IUIDs)

    (hl7ImportReportAdjustIUID)"
    "
    .. _hl7ReferredMergedPatientPolicy:
    .. _archiveHL7Application-hl7ReferredMergedPatientPolicy:

    :ref:`HL7 Referred Merged Patient Policy <archiveHL7Application-hl7ReferredMergedPatientPolicy>`",string,"Specifies policy on incoming HL7 messages referring an already merged Patient. Refer `HL7 Referred Merged Patient Policy <https://github.com/dcm4che/dcm4chee-arc-light/wiki/HL7-Referred-Merged-Patient-Policy>`_ meanings. Overwrites value specified on Device level.

    Enumerated values:

    REJECT (= Reject any incoming HL7 messages referring an already merged Patient)

    IGNORE (= Ignore any incoming HL7 messages referring an already merged Patient)

    IGNORE_DUPLICATE_MERGE (= Ignore only duplicate incoming HL7 Patient Merge (ADT^A40) messages referring an already merged Patient. Reject any other incoming HL7 messages referring an already merged Patient.)

    ACCEPT_INVERSE_MERGE (= Accept any incoming inverse HL7 Patient Merge (ADT^A40) messages referring an already merged Patient, optionally allowing inverse merging of patient records if clients send duplicated ADT^A40 patient merge messages repeatedly, just reversing the patient identifier values in PID / MRG segments.)

    (hl7ReferredMergedPatientPolicy)"
    "
    .. _hl7DicomCharacterSet:
    .. _archiveHL7Application-hl7DicomCharacterSet:

    :ref:`HL7 Dicom Character Set <archiveHL7Application-hl7DicomCharacterSet>`",string,"Indicates to use specified Value of Specific Character Set (0008,0005) in Data Sets transcoded from received HL7 messages. Use Value corresponding to Character Set of the HL7 message specified by MSH-18 if absent.

    (hl7DicomCharacterSet)"
    ":doc:`hl7ForwardRule` (s)",object,"HL7 Forward Rule. Supplements values specified on Device level."
    ":doc:`hl7ExportRule` (s)",object,"Export Rules applied to HL7 messages received by this HL7 Application. Supplements HL7 Export Rules specified on Device level."
    ":doc:`upsOnHL7` (s)",object,"UPS on HL7 Rules applied to HL7 messages received by any HL7 Application. Supplements UPS on HL7 Rules specified on Device level."
    ":doc:`hl7PrefetchRule` (s)",object,"Prefetch Rules applied to HL7 messages received by this HL7 Application. Supplements HL7 Prefetch Rules specified on Device level."
    ":doc:`hl7StudyRetentionPolicy` (s)",object,"HL7 Study Retention Policies triggered by HL7 messages received by this HL7 Application. Supplements values specified on Device level."
    ":doc:`hl7OrderScheduledStation` (s)",object,"Scheduled Station selected on MWL HL7 Order Feed. Supplements values specified on Device level."
    ":doc:`hl7OrderSPSStatus` (s)",object,"Specifies SPS Status of DICOM MWL items created/updated on received HL7 ORM^O01, OMI^O23, OMG^O19 messages. Overwrites values specified on Device level."

.. toctree::

    hl7ForwardRule
    hl7ExportRule
    upsOnHL7
    hl7PrefetchRule
    hl7StudyRetentionPolicy
    hl7OrderScheduledStation
    hl7OrderSPSStatus
