Archive Attribute Coercion
==========================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Attribute Coercion Attributes (LDAP Object: dcmArchiveAttributeCoercion2)
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

    :ref:`Attribute Coercion URI <dcmURI>`",string,"Identifies Attribute Coercion by Uniform Resource Identifier (e.g. 'merge-mwl:${jboss.server.temp.url}/dcm4chee-arc/mwl2series.xsl')

    (dcmURI)"
    "
    .. _dcmCoercionSufficient:

    :ref:`Attribute Coercion Sufficient <dcmCoercionSufficient>`",boolean,"Do not apply other matching Attribute Coercions of lesser priority, if this Attribute Coercion was applied effectively.

    (dcmCoercionSufficient)"
    "
    .. _dcmCoercionOnFailure:

    :ref:`Attribute Coercion on Failure <dcmCoercionOnFailure>`",string,"Behavior on failure applying this Attribute Coercion. RETHROW (= propagate failure to operation applying this Attribute Coercion), CONTINUE (= continue to apply other matching Attribute Coercions of lesser priority) or SUFFICIENT (= do not apply other matching Attribute Coercions of lesser priority). Enumerated values: RETHROW, CONTINUE or SUFFICIENT.

    (dcmCoercionOnFailure)"
    "
    .. _dcmRulePriority:

    :ref:`Attribute Coercion Priority <dcmRulePriority>`",integer,"Rule Priority. Higher priority rule takes precedence.

    (dcmRulePriority)"
    "
    .. _dcmDIMSE:

    :ref:`DIMSE <dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied Enumerated values: N_CREATE_RQ, C_STORE_RQ, C_FIND_RQ or C_FIND_RSP.

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

    :ref:`Attribute Update Policy <dcmAttributeUpdatePolicy>`",string,"Applied Attribute Update Policy. PRESERVE (= nullify attributes in the new dataset which are not present in the original dataset), SUPPLEMENT (= attributes not present in original dataset will be supplemented), MERGE (= attribute values will be written from new dataset), OVERWRITE (= attribute values if null in new dataset, will be nullified in original dataset). Only effective for particular Attribute Coercions. Enumerated values: PRESERVE, SUPPLEMENT, MERGE or OVERWRITE.

    (dcmAttributeUpdatePolicy)"
    "
    .. _dicomDeviceName:

    :ref:`Device Name Coercion Parameter <dicomDeviceName>`",string,"Device Name Coercion Parameter. Only effective for particular Attribute Coercions.

    (dicomDeviceName)"
    "
    .. _dcmMergeAttribute:

    :ref:`DICOM Attribute Coercion Parameter(s) <dcmMergeAttribute>`",string,"DICOM Attribute Coercion Parameters in format {attributeID}={value}. {attributeID} inside of {value} may be replaced by the value of that attribute in the original dataset. Only effective for particular Attribute Coercions.

    (dcmMergeAttribute)"
    "
    .. _dcmCoercionParam:

    :ref:`Other Coercion Parameter(s) <dcmCoercionParam>`",string,"Other Attribute Coercion specific Parameters.

    (dcmCoercionParam)"
