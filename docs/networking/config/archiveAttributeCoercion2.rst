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

    :ref:`Attribute Coercion on Failure <dcmCoercionOnFailure>`",string,"Behavior on failure applying this Attribute Coercion. Refer `Attribute Coercion on Failure meanings. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#attribute-coercion-on-failure>`_

    Enumerated values:

    RETHROW

    CONTINUE

    SUFFICIENT

    (dcmCoercionOnFailure)"
    "
    .. _dcmRulePriority:

    :ref:`Attribute Coercion Priority <dcmRulePriority>`",integer,"If the condition of several archive attribute coercion (new) matches for a received image, higher priority coercion takes precedence. If there are several matching coercions with equal priority, it is undefined which coercion takes precedence.

    (dcmRulePriority)"
    "
    .. _dcmDIMSE:

    :ref:`DIMSE <dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied. Also `applicable if the requests are received over web. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#dimse>`_

    Enumerated values:

    N_CREATE_RQ

    C_STORE_RQ

    C_FIND_RQ

    C_FIND_RSP

    (dcmDIMSE)"
    "
    .. _dicomTransferRole:

    :ref:`DICOM Transfer Role <dicomTransferRole>`",string,"DICOM Transfer Role of peer DICOM AE.

    Enumerated values:

    SCU

    SCP

    (dicomTransferRole)"
    "
    .. _dcmSOPClass:

    :ref:`SOP Class UID(s) <dcmSOPClass>`",string,"UID of SOP Class for which this Attribute Coercion shall be applied. Apply on any if absent.

    (dcmSOPClass)"
    "
    .. _dcmProperty:

    :ref:`Condition(s) <dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy <dcmAttributeUpdatePolicy>`",string,"Applied Attribute Update Policy. Only effective for coerce from Leading C-FIND SCP coercion type. Refer `Attribute Update Policies' meanings. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Attribute-Update-Policy>`_

    Enumerated values:

    PRESERVE

    SUPPLEMENT

    MERGE

    OVERWRITE

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
