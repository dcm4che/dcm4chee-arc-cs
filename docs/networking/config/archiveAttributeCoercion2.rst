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

    RETHROW (= Propagates failure to operation which applied this (current) Attribute Coercion)

    CONTINUE (= Continues applying other matching attribute coercions of lesser priority)

    SUFFICIENT (= Does not apply other matching attribute coercions of lesser priority)

    (dcmCoercionOnFailure)"
    "
    .. _dcmRulePriority:

    :ref:`Attribute Coercion Priority <dcmRulePriority>`",integer,"If the condition of several archive attribute coercion (new) matches for a received image, higher priority coercion takes precedence. If there are several matching coercions with equal priority, it is undefined which coercion takes precedence.

    (dcmRulePriority)"
    "
    .. _dcmDIMSE:

    :ref:`DIMSE <dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied. Also `applicable if the requests are received over web. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#dimse>`_

    Enumerated values:

    N_CREATE_RQ (= Applicable to MPPS N-CREATE request datasets)

    C_STORE_RQ (= Applicable to objects stored / retrieved using C_STORE / C-MOVE / STOW / WADO-RS)

    C_FIND_RQ (= Applicable to C-FIND / QIDO request datasets)

    C_FIND_RSP (= Applicable to C-FIND / QIDO response datasets)

    (dcmDIMSE)"
    "
    .. _dicomTransferRole:

    :ref:`DICOM Transfer Role <dicomTransferRole>`",string,"DICOM Transfer Role of peer DICOM AE.

    Enumerated values:

    SCU (= Service Class User)

    SCP (= Service Class Provider)

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

    PRESERVE (= The attributes will be preserved. Nullify attributes in the new dataset which are not present in the original dataset. Any extra attributes will be nullified)

    SUPPLEMENT (= The attributes will be overwritten. Attributes not present in original dataset will be supplemented. Any extra attributes with not null values will be added)

    MERGE (= The attributes will be overwritten. Attribute values will be written from new dataset. Any attributes with not null values, shall not be overwritten by attributes with null values)

    OVERWRITE (= The attributes will be overwritten. Attribute values if null in new dataset, will be nullified in original dataset. Any attributes with not null values, shall be overwritten by attributes with null values)

    (dcmAttributeUpdatePolicy)"
    "
    .. _dcmSupplementFromDeviceReference:

    :ref:`Device Name Coercion Parameter <dcmSupplementFromDeviceReference>`",string,"Device Name Coercion Parameter. Only effective for supplementing from device coercion type.

    (dcmSupplementFromDeviceReference)"
    "
    .. _dcmMergeAttribute:

    :ref:`DICOM Attribute Coercion Parameters(s) <dcmMergeAttribute>`",string,"DICOM Attribute Coercion Parameters in format {attributeID}={value}. {attributeID} inside of {value} may be replaced by the value of that attribute in the original dataset. Only effective for merging attributes coercion type. Refer `DICOM Attribute Coercion Parameters <https://github.com/dcm4che/dcm4chee-arc-light/wiki/DICOM-Attribute-Coercion-Parameters>`_ for formatting options and examples.

    (dcmMergeAttribute)"
    "
    .. _dcmCoercionParam:

    :ref:`Other Coercion Parameters(s) <dcmCoercionParam>`",string,"Refer applicability to coercion types and examples in `Other Attribute Coercion specific Parameters <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#other-coercion-parameters>`_

    (dcmCoercionParam)"
