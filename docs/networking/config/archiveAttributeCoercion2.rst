Archive Attribute Coercion - New
================================
Archive Attribute Coercion of received/sent DIMSE

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Archive Attribute Coercion - New Attributes (LDAP Object: dcmArchiveAttributeCoercion2)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _archiveAttributeCoercion2-cn:

    :ref:`Name <archiveAttributeCoercion2-cn>`",string,"Arbitrary/Meaningful name of the Archive Attribute Coercion

    (cn)"
    "
    .. _dicomDescription:
    .. _archiveAttributeCoercion2-dicomDescription:

    :ref:`Attribute Coercion Description <archiveAttributeCoercion2-dicomDescription>`",string,"Unconstrained text description of the Attribute Coercion

    (dicomDescription)"
    "
    .. _dcmURI:
    .. _archiveAttributeCoercion2-dcmURI:

    :ref:`Attribute Coercion URI <archiveAttributeCoercion2-dcmURI>`",string,"Identifies Attribute Coercion by Uniform Resource Identifier. Refer values you can set for `Attribute Coercion URI <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#attribute-coercion-uri>`_ field depending on the coercion type.

    (dcmURI)"
    "
    .. _dcmCoercionSufficient:
    .. _archiveAttributeCoercion2-dcmCoercionSufficient:

    :ref:`Attribute Coercion Sufficient <archiveAttributeCoercion2-dcmCoercionSufficient>`",boolean,"Do not apply other matching Attribute Coercions of lesser priority, if this Attribute Coercion was applied effectively.

    (dcmCoercionSufficient)"
    "
    .. _dcmCoercionOnFailure:
    .. _archiveAttributeCoercion2-dcmCoercionOnFailure:

    :ref:`Attribute Coercion on Failure <archiveAttributeCoercion2-dcmCoercionOnFailure>`",string,"Behavior on failure applying this Attribute Coercion. Refer `Attribute Coercion on Failure meanings. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#attribute-coercion-on-failure>`_

    Enumerated values:

    RETHROW (= Propagates failure to operation which applied this (current) Attribute Coercion)

    CONTINUE (= Continues applying other matching attribute coercions of lesser priority)

    SUFFICIENT (= Does not apply other matching attribute coercions of lesser priority)

    (dcmCoercionOnFailure)"
    "
    .. _dcmRulePriority:
    .. _archiveAttributeCoercion2-dcmRulePriority:

    :ref:`Attribute Coercion Priority <archiveAttributeCoercion2-dcmRulePriority>`",integer,"If the condition of several archive attribute coercion (new) matches for a received image, higher priority coercion takes precedence. If there are several matching coercions with equal priority, it is undefined which coercion takes precedence.

    (dcmRulePriority)"
    "
    .. _dcmDIMSE:
    .. _archiveAttributeCoercion2-dcmDIMSE:

    :ref:`DIMSE <archiveAttributeCoercion2-dcmDIMSE>`",string,"DICOM Message Element on which this Attribute Coercion shall be applied. Also `applicable if the requests are received over web. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#dimse>`_

    Enumerated values:

    N_CREATE_RQ (= Applicable to MPPS N-CREATE request datasets)

    C_STORE_RQ (= Applicable to objects stored / retrieved using C_STORE / C-MOVE / STOW / WADO-RS)

    C_FIND_RQ (= Applicable to C-FIND / QIDO request datasets)

    C_FIND_RSP (= Applicable to C-FIND / QIDO response datasets)

    (dcmDIMSE)"
    "
    .. _dicomTransferRole:
    .. _archiveAttributeCoercion2-dicomTransferRole:

    :ref:`DICOM Transfer Role <archiveAttributeCoercion2-dicomTransferRole>`",string,"DICOM Transfer Role of peer DICOM AE.

    Enumerated values:

    SCU (= Service Class User)

    SCP (= Service Class Provider)

    (dicomTransferRole)"
    "
    .. _dcmSOPClass:
    .. _archiveAttributeCoercion2-dcmSOPClass:

    :ref:`SOP Class UID(s) <archiveAttributeCoercion2-dcmSOPClass>`",string,"UID of SOP Class for which this Attribute Coercion shall be applied. Apply on any if absent.

    (dcmSOPClass)"
    "
    .. _dcmProperty:
    .. _archiveAttributeCoercion2-dcmProperty:

    :ref:`Condition(s) <archiveAttributeCoercion2-dcmProperty>`",string,"Conditions in format {key}[!]={value}. Refer `applicability, format and some examples. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Conditions>`_

    (dcmProperty)"
    "
    .. _dcmAttributeUpdatePolicy:
    .. _archiveAttributeCoercion2-dcmAttributeUpdatePolicy:

    :ref:`Attribute Update Policy <archiveAttributeCoercion2-dcmAttributeUpdatePolicy>`",string,"Applied Attribute Update Policy. Only effective for coerce from Leading C-FIND SCP coercion type. Refer `Attribute Update Policies' meanings. <https://github.com/dcm4che/dcm4chee-arc-light/wiki/Attribute-Update-Policy>`_

    Enumerated values:

    PRESERVE (= The attributes will be preserved. Nullify attributes in the new dataset which are not present in the original dataset. Any extra attributes will be nullified)

    SUPPLEMENT (= The attributes will be overwritten. Attributes not present in original dataset will be supplemented. Any extra attributes with not null values will be added)

    MERGE (= The attributes will be overwritten. Attribute values will be written from new dataset. Any attributes with not null values, shall not be overwritten by attributes with null values)

    OVERWRITE (= The attributes will be overwritten. Attribute values if null in new dataset, will be nullified in original dataset. Any attributes with not null values, shall be overwritten by attributes with null values)

    (dcmAttributeUpdatePolicy)"
    "
    .. _dcmSupplementFromDeviceReference:
    .. _archiveAttributeCoercion2-dcmSupplementFromDeviceReference:

    :ref:`Device Name Coercion Parameter <archiveAttributeCoercion2-dcmSupplementFromDeviceReference>`",string,"Device Name Coercion Parameter. Only effective for supplementing from device coercion type.

    (dcmSupplementFromDeviceReference)"
    "
    .. _dcmMergeAttribute:
    .. _archiveAttributeCoercion2-dcmMergeAttribute:

    :ref:`DICOM Attribute Coercion Parameters(s) <archiveAttributeCoercion2-dcmMergeAttribute>`",string,"DICOM Attribute Coercion Parameters in format {attributeID}={value}. {attributeID} inside of {value} may be replaced by the value of that attribute in the original dataset. Only effective for merging attributes coercion type. Refer `DICOM Attribute Coercion Parameters <https://github.com/dcm4che/dcm4chee-arc-light/wiki/DICOM-Attribute-Coercion-Parameters>`_ for formatting options and examples.

    (dcmMergeAttribute)"
    "
    .. _dcmCoercionParam:
    .. _archiveAttributeCoercion2-dcmCoercionParam:

    :ref:`Other Coercion Parameters(s) <archiveAttributeCoercion2-dcmCoercionParam>`",string,"Refer applicability to coercion types and examples in `Other Attribute Coercion specific Parameters <https://github.com/dcm4che/dcm4chee-arc-light/wiki/New-Archive-Attribute-Coercion---Application-of-multiple-coercions-for-one-use-case-using-multiple-rules#other-coercion-parameters>`_

    (dcmCoercionParam)"
