UPS on UPS Completed
====================
Create Workitem in unified Worklist on previous UPS Completed

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UPS on UPS Completed Attributes (LDAP Object: dcmUpsOnUPSCompleted)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmUPSOnUPSCompletedID:

    :ref:`UPS on UPS Completed Rule ID <dcmUPSOnUPSCompletedID>`",string,"ID of UPS on UPS Completed Rule

    (dcmUPSOnUPSCompletedID)"
    "
    .. _dcmProperty:

    :ref:`Condition(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmRequiresOtherUPSCompleted:

    :ref:`Requires other UPS completed(s) <dcmRequiresOtherUPSCompleted>`",string,"Specifies Query Parameters for other UPS referring the same request (= Study Instance UID), which must be already be completed for creating this UPS. Format: {attributeID}={value}[&...]

    (dcmRequiresOtherUPSCompleted)"
    "
    .. _dcmUPSLabel:

    :ref:`Procedure Step Label <dcmUPSLabel>`",string,"Value of Procedure Step Label (0074,1204) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {StudyDescription}

    (dcmUPSLabel)"
    "
    .. _dcmUPSWorklistLabel:

    :ref:`Worklist Label <dcmUPSWorklistLabel>`",string,"Value of Worklist Label (0074,1202) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {StudyDescription}

    (dcmUPSWorklistLabel)"
    "
    .. _dcmUPSPriority:

    :ref:`Priority <dcmUPSPriority>`",string,"Value of Scheduled Procedure Step Priority (0074,1200) in created UPS. Enumerated Values: HIGH, MEDIUM, LOW. If absent, MEDIUM will be applied. Enumerated values: HIGH, MEDIUM or LOW.

    (dcmUPSPriority)"
    "
    .. _dcmUPSInputReadinessState:

    :ref:`Input Readiness State <dcmUPSInputReadinessState>`",string,"Value of Input Readiness State (0040,4041) in created UPS Enumerated values: INCOMPLETE, UNAVAILABLE or READY.

    (dcmUPSInputReadinessState)"
    "
    .. _dcmUPSStartDateTimeDelay:

    :ref:`Scheduled Procedure Step Start DateTime Delay <dcmUPSStartDateTimeDelay>`",string,"Delay of Scheduled Procedure Step Start DateTime (0040,4005) in created UPS from receive time in format PnDTnHnMn.nS. No delay if absent.

    (dcmUPSStartDateTimeDelay)"
    "
    .. _dcmUPSCompletionDateTimeDelay:

    :ref:`Expected Completion DateTime Delay <dcmUPSCompletionDateTimeDelay>`",string,"Delay of Expected Completion DateTime (0040,4011) in created UPS from receive time in format PnDTnHnMn.nS. If absent, no Expected Completion Date and Time will be set.

    (dcmUPSCompletionDateTimeDelay)"
    "
    .. _dcmUPSInstanceUIDBasedOnName:

    :ref:`UPS Instance UID based on name <dcmUPSInstanceUIDBasedOnName>`",string,"Value to generate name based SOP Instance UID (0008,0018) in created UPS. If absent, a random generated SOP Instance UID (0008,0018) will be used.

    (dcmUPSInstanceUIDBasedOnName)"
    "
    .. _dcmUPSIncludeInputInformation:

    :ref:`Include Input Information <dcmUPSIncludeInputInformation>`",string,"Indicates if the Input Information Sequence (0040,4021) or/and the Output Information Sequence (0040,4033) in the Unified Procedure Step Performed Procedure Sequence (0074,1216) of the previous UPS is included in Input Information Sequence (0040,4021) of the in created UPS. Enumerated values: NO, COPY_INPUT or COPY_OUTPUT.

    (dcmUPSIncludeInputInformation)"
    "
    .. _dcmUPSIncludePatient:

    :ref:`UPS Include Patient <dcmUPSIncludePatient>`",boolean,"Indicates if patient attributes are copied from the previous UPS.

    (dcmUPSIncludePatient)"
    "
    .. _dcmDestinationAE:

    :ref:`Destination AE <dcmDestinationAE>`",string,"Title of a DICOM Application Entity to which Instances will be stored.

    (dcmDestinationAE)"
    "
    .. _dcmEntity:

    :ref:`Scope of Accumulation <dcmEntity>`",string,"Scope of Accumulation Enumerated values: Study, Series or MPPS.

    (dcmEntity)"
    "
    .. _dcmUPSScheduledWorkitemCode:

    :ref:`Scheduled Workitem Code <dcmUPSScheduledWorkitemCode>`",string,"Item of Scheduled Workitem Code Sequence (0040,4018) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledWorkitemCode)"
    "
    .. _dcmUPSScheduledStationNameCode:

    :ref:`Scheduled Station Name Code(s) <dcmUPSScheduledStationNameCode>`",string,"Item of Scheduled Station Name Code Sequence (0040,4025) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationNameCode)"
    "
    .. _dcmUPSScheduledStationClassCode:

    :ref:`Scheduled Station Class Code(s) <dcmUPSScheduledStationClassCode>`",string,"Item of Scheduled Station Class Code Sequence (0040,4026) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationClassCode)"
    "
    .. _dcmUPSScheduledStationLocationCode:

    :ref:`Scheduled Station Geographic Location Code(s) <dcmUPSScheduledStationLocationCode>`",string,"Item of Scheduled Station Geographic Location Code Sequence (0040,4027) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledStationLocationCode)"
    "
    .. _dcmUPSScheduledHumanPerformerCode:

    :ref:`Scheduled Human Performer Code(s) <dcmUPSScheduledHumanPerformerCode>`",string,"Item of Human Performer Code Sequence (0040,4009) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS in format (CV, CSD, ""CM"").

    (dcmUPSScheduledHumanPerformerCode)"
    "
    .. _dcmUPSScheduledHumanPerformerName:

    :ref:`Scheduled Human Performer Name <dcmUPSScheduledHumanPerformerName>`",string,"Value of Human Performer's Name (0040,4037) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {PerformingPhysicianName}

    (dcmUPSScheduledHumanPerformerName)"
    "
    .. _dcmUPSScheduledHumanPerformerOrganization:

    :ref:`Scheduled Human Performer Organization <dcmUPSScheduledHumanPerformerOrganization>`",string,"Value of Human Performer's Organization (0040,4036) in Item of Scheduled Human Performers Sequence (0040,4034) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {ResponsibleOrganization}

    (dcmUPSScheduledHumanPerformerOrganization)"
    "
    .. _dcmAdmissionID:

    :ref:`Admission Number <dcmAdmissionID>`",string,"Value of Admission ID (0038,0010) in created UPS. {attributeID} will be replaced by the value of that attribute in the previous UPS dataset. Example: {AdmissionID}

    (dcmAdmissionID)"
    "
    .. _dicomIssuerOfAdmissionID:

    :ref:`Issuer of Admission ID <dicomIssuerOfAdmissionID>`",string,"Value of Local Namespace Entity ID (0040,0031), Universal Entity ID (0040,0032) and Universal Entity ID Type (0040,0033) of the Item of the Issuer of Admission ID Sequence (0038,0014) in created UPS. Format: <Local Namespace Entity ID>['&'<Universal Entity ID>'&'<Universal Entity ID Type>]

    (dicomIssuerOfAdmissionID)"
    "
    .. _dcmUPSIncludeStudyInstanceUID:

    :ref:`Include Study Instance UID <dcmUPSIncludeStudyInstanceUID>`",boolean,"Indicates if Study Instance UID (0020,000D) of the previous UPS object shall be included in the created UPS

    (dcmUPSIncludeStudyInstanceUID)"
    "
    .. _dcmUPSIncludeReferencedRequest:

    :ref:`Include Referenced Request <dcmUPSIncludeReferencedRequest>`",boolean,"Indicates if the Referenced Request Sequence (0040,A370) of the previous UPS is included in the created UPS. Otherwise an empty Referenced Request Sequence (0040,A370) is included.

    (dcmUPSIncludeReferencedRequest)"
    "
    .. _dcmURI:

    :ref:`XSL Stylesheet URI <dcmURI>`",string,"Specifies URI of the XSL style sheet to include additional attributes in created UPS.

    (dcmURI)"
    "
    .. _dcmNoKeywords:

    :ref:`No Attribute Keyword <dcmNoKeywords>`",boolean,"Indicates if attribute keywords shall be omitted in DICOM XML passed to XSLT.

    (dcmNoKeywords)"
