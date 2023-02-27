Archive Attribute Coercion - New
================================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Attribute Coercion - New Attributes (LDAP Object: dcmArchiveAttributeCoercion2)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Archive Attribute Coercion

    (cn)"
    "
    .. _dicomDescription:

    :ref:`Attribute Coercion Description <dicomDescription>`",string,"Unconstrained text description of the Attribute Coercion

    (dicomDescription)"
    "
    .. _dcmURI:

    :ref:`Attribute Coercion URI <dcmURI>`",string,"Identifies Attribute Coercion by Uniform Resource Identifier. Refer values you can set for `Attribute Coercion URI <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#attribute-coercion-uri>`_ field depending on the coercion type.

    (dcmURI)"
    "
    .. _dcmCoercionSufficient:

    :ref:`Attribute Coercion Sufficient <dcmCoercionSufficient>`",boolean,"Do not apply other matching Attribute Coercions of lesser priority, if this Attribute Coercion was applied effectively.

    (dcmCoercionSufficient)"
    "
    .. _dcmCoercionOnFailure:

    :ref:`Attribute Coercion on Failure <dcmCoercionOnFailure>`",string,"Behavior on failure applying this Attribute Coercion. Refer `Attribute Coercion on Failure meanings. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#attribute-coercion-on-failure>`_ Enumerated values: RETHROW, CONTINUE or SUFFICIENT.

    (dcmCoercionOnFailure)"
    "
    .. _dcmRulePriority:

    :ref:`Attribute Coercion Priority <dcmRulePriority>`",integer,"Rule Priority. Higher priority rule takes precedence.

    (dcmRulePriority)"
    "
    .. _dcmDIMSE:

    :ref:`DIMSE <dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied. Also `applicable if the requests are received over web <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#dimse>`_ Enumerated values: N_CREATE_RQ, C_STORE_RQ, C_FIND_RQ or C_FIND_RSP.

    (dcmDIMSE)"
    "
    .. _dicomTransferRole:

    :ref:`DICOM Transfer Role <dicomTransferRole>`",string,"DICOM Transfer Role of peer DICOM AE. Enumerated values: SCU or SCP.

    (dicomTransferRole)"
    "
    .. _dcmSOPClass:

    :ref:`SOP Class UID(s) <dcmSOPClass>`",string,"UID of SOP Class for which this Attribute Coercion shall be applied. Apply on any if absent.

    (dcmSOPClass)"
    "
    .. _dcmProperty:

    :ref:`Condition(s) <dcmProperty>`",string,"Conditions in format (SendingHostname|SendingApplicationEntityTitle|ReceivingHostname|ReceivingApplicationEntityTitle|{AttributeTagOrKeyword[number]}|{SequenceTagOrKeyword.AttributeTagOrKeyword})[!]={regEx}. More than one value can be specified for a given attribute by separating them with a | symbol. Examples: SendingApplicationEntityTitle=FORWARD or Modality=MR|CT or ProcedureCodeSequence.CodeValue=MRProcedure or 00180015=KNEE or 00321034.00080100=RequestingServiceCode or ImageType[3]=LOCALIZER

    (dcmProperty)"
    "
    .. _dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy <dcmAttributeUpdatePolicy>`",string,"Applied Attribute Update Policy. Only effective for coerce from Leading C-FIND SCP coercion type. Refer `Attribute Update Policies' meanings <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Attribute-Update-Policy>`_ Enumerated values: PRESERVE, SUPPLEMENT, MERGE or OVERWRITE.

    (dcmAttributeUpdatePolicy)"
    "
    .. _dcmSupplementFromDeviceReference:

    :ref:`Device Name Coercion Parameter <dcmSupplementFromDeviceReference>`",string,"Device Name Coercion Parameter. Only effective for supplementing from device coercion type.

    (dcmSupplementFromDeviceReference)"
    "
    .. _dcmMergeAttribute:

    :ref:`DICOM Attribute Coercion Parameters(s) <dcmMergeAttribute>`",string,"DICOM Attribute Coercion Parameters in format {attributeID}={value}. {attributeID} inside of {value} may be replaced by the value of that attribute in the original dataset. Only effective for merging attributes coercion type. Refer `formatting options and examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#dicom-attribute-coercion-parameters>`_

    (dcmMergeAttribute)"
    "
    .. _dcmCoercionParam:

    :ref:`Other Coercion Parameters(s) <dcmCoercionParam>`",string,"Refer applicability to coercion types and examples in `Other Attribute Coercion specific Parameters <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#other-coercion-parameters>`_

    (dcmCoercionParam)"
