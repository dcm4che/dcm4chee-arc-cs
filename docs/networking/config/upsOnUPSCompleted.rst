UPS on UPS Completed
====================
Create Workitem in unified Worklist on previous UPS Completed

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS on UPS Completed Attributes (LDAP Object: dcmUpsOnUPSCompleted)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmUPSOnUPSCompletedID:
    .. _upsOnUPSCompleted-dcmUPSOnUPSCompletedID:

    :ref:`UPS on UPS Completed Rule ID <upsOnUPSCompleted-dcmUPSOnUPSCompletedID>`",string,"ID of UPS on UPS Completed Rule

    (dcmUPSOnUPSCompletedID)"
    "
    .. _dcmProperty:
    .. _upsOnUPSCompleted-dcmProperty:

    :ref:`Condition(s) <upsOnUPSCompleted-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmRequiresOtherUPSCompleted:
    .. _upsOnUPSCompleted-dcmRequiresOtherUPSCompleted:

    :ref:`Requires other UPS completed(s) <upsOnUPSCompleted-dcmRequiresOtherUPSCompleted>`",string,"Specifies Query Parameters for other UPS referring the same request (= Study Instance UID), which must be already be completed for creating this UPS. Format: {attributeID}={value}[&...]

    (dcmRequiresOtherUPSCompleted)"
    "
    .. _dcmUPSLabel:
    .. _upsOnUPSCompleted-dcmUPSLabel:

    :ref:`Procedure Step Label <upsOnUPSCompleted-dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {StudyDescription}

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:
    .. _upsOnUPSCompleted-dcmUPSWorklistLabel:

    :ref:`Worklist Label <upsOnUPSCompleted-dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {StudyDescription}

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSPriority:
    .. _upsOnUPSCompleted-dcmUPSPriority:

    :ref:`Priority <upsOnUPSCompleted-dcmUPSPriority>`",string,"Value of Scheduled Procedure Step Priority (0074,1200) in created UPS.

    Enumerated values:

    HIGH

    MEDIUM

    LOW

    (dcmUPSPriority)"
    "
    .. _dcmUPSInputReadinessState:
    .. _upsOnUPSCompleted-dcmUPSInputReadinessState:

    :ref:`Input Readiness State <upsOnUPSCompleted-dcmUPSInputReadinessState>`",string,"Value of Input Readiness State (0040,4041) in created UPS

    Enumerated values:

    INCOMPLETE

    UNAVAILABLE

    READY

    (dcmUPSInputReadinessState)"
    "
    .. _dcmUPSStartDateTimeDelay:
    .. _upsOnUPSCompleted-dcmUPSStartDateTimeDelay:

    :ref:`Scheduled Procedure Step Start DateTime Delay <upsOnUPSCompleted-dcmUPSStartDateTimeDelay>`",string,"Delay of Scheduled Procedure Step Start DateTime (0040,4005) in created UPS from receive time in format PnDTnHnMn.nS. No delay if absent.

    (dcmUPSStartDateTimeDelay)"
    "
    .. _dcmUPSCompletionDateTimeDelay:
    .. _upsOnUPSCompleted-dcmUPSCompletionDateTimeDelay:

    :ref:`Expected Completion DateTime Delay <upsOnUPSCompleted-dcmUPSCompletionDateTimeDelay>`",string,"Delay of Expected Completion DateTime (0040,4011) in created UPS from receive time in format PnDTnHnMn.nS. If absent, no Expected Completion Date and Time will be set.

    (dcmUPSCompletionDateTimeDelay)"
    "
    .. _dcmUPSInstanceUIDBasedOnName:
    .. _upsOnUPSCompleted-dcmUPSInstanceUIDBasedOnName:

    :ref:`UPS Instance UID based on name <upsOnUPSCompleted-dcmUPSInstanceUIDBasedOnName>`",string,"Value to generate name based SOP Instance UID (0008,0018) in created UPS. If absent, a random generated SOP Instance UID (0008,0018) will be used.

    (dcmUPSInstanceUIDBasedOnName)"
    "
    .. _dcmUPSIncludeInputInformation:
    .. _upsOnUPSCompleted-dcmUPSIncludeInputInformation:

    :ref:`Include Input Information <upsOnUPSCompleted-dcmUPSIncludeInputInformation>`",string,"Indicates if the Input Information Sequence (0040,4021) or/and the Output Information Sequence (0040,4033) in the Unified Procedure Step Performed Procedure Sequence (0074,1216) of the previous UPS is included in Input Information Sequence (0040,4021) of the in created UPS.

    Enumerated values:

    NO

    COPY_INPUT

    COPY_OUTPUT

    (dcmUPSIncludeInputInformation)"
    "
    .. _dcmUPSIncludePatient:
    .. _upsOnUPSCompleted-dcmUPSIncludePatient:

    :ref:`UPS Include Patient <upsOnUPSCompleted-dcmUPSIncludePatient>`",boolean,"Indicates if patient attributes are copied from the previous UPS.

    (dcmUPSIncludePatient)"
    "
    .. _dcmDestinationAE:
    .. _upsOnUPSCompleted-dcmDestinationAE:

    :ref:`Destination AE <upsOnUPSCompleted-dcmDestinationAE>`",string,"Title of a DICOM Application Entity to which Instances will be stored.

    (dcmDestinationAE)"
    "
    .. _dcmEntity:
    .. _upsOnUPSCompleted-dcmEntity:

    :ref:`Scope of Accumulation <upsOnUPSCompleted-dcmEntity>`",string,"Scope of Accumulation

    Enumerated values:

    Study

    Series

    MPPS

    (dcmEntity)"
    "
    .. _dcmUPSScheduledWorkitemCode:
    .. _upsOnUPSCompleted-dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <upsOnUPSCompleted-dcmUPSScheduledWorkitemCode>`",string,"Item of Scheduled Workitem Code Sequence (0040,4018) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:
    .. _upsOnUPSCompleted-dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code(s) <upsOnUPSCompleted-dcmUPSScheduledStationNameCode>`",string,"Item of Scheduled Station Name Code Sequence (0040,4025) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:
    .. _upsOnUPSCompleted-dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code(s) <upsOnUPSCompleted-dcmUPSScheduledStationClassCode>`",string,"Item of Scheduled Station Class Code Sequence (0040,4026) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:
    .. _upsOnUPSCompleted-dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code(s) <upsOnUPSCompleted-dcmUPSScheduledStationLocationCode>`",string,"Item of Scheduled Station Geographic Location Code Sequence (0040,4027) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSScheduledHumanPerformerCode:
    .. _upsOnUPSCompleted-dcmUPSScheduledHumanPerformerCode:

    :ref:`Scheduled Human Performer Code(s) <upsOnUPSCompleted-dcmUPSScheduledHumanPerformerCode>`",string,"Item of Human Performer Code Sequence (0040,4009) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledHumanPerformerCode)"
    "
    .. _dcmUPSScheduledHumanPerformerName:
    .. _upsOnUPSCompleted-dcmUPSScheduledHumanPerformerName:

    :ref:`Scheduled Human Performer Name <upsOnUPSCompleted-dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {PerformingPhysicianName}

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:
    .. _upsOnUPSCompleted-dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <upsOnUPSCompleted-dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {ResponsibleOrganization}

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmAdmissionID:
    .. _upsOnUPSCompleted-dcmAdmissionID:

    :ref:`Admission Number <upsOnUPSCompleted-dcmAdmissionID>`",string,"Value of Admission ID (0038,0010) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {AdmissionID}

    (dcmAdmissionID)"
    "
    .. _dicomIssuerOfAdmissionID:
    .. _upsOnUPSCompleted-dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID <upsOnUPSCompleted-dicomIssuerOfAdmissionID>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAdmissionID)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:
    .. _upsOnUPSCompleted-dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <upsOnUPSCompleted-dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) of the previous UPS object shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
    "
    .. _dcmUPSIncludeReferencedRequest:
    .. _upsOnUPSCompleted-dcmUPSIncludeReferencedRequest:

    :ref:`Include Referenced Request <upsOnUPSCompleted-dcmUPSIncludeReferencedRequest>`",boolean,"Indicates if the Referenced Request Sequence (0040,A370) of the previous UPS is included in the created UPS. Otherwise an empty Referenced Request Sequence (0040,A370) is included.

    (dcmUPSIncludeReferencedRequest)"
    "
    .. _dcmURI:
    .. _upsOnUPSCompleted-dcmURI:

    :ref:`XSL Stylesheet URI <upsOnUPSCompleted-dcmURI>`",string,"Specifies URI of the XSL style sheet to include additional attributes in created UPS.

    (dcmURI)"
    "
    .. _dcmNoKeywords:
    .. _upsOnUPSCompleted-dcmNoKeywords:

    :ref:`No Attribute Keyword <upsOnUPSCompleted-dcmNoKeywords>`",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT.

    (dcmNoKeywords)"
