UI Diff Criteria
================
UI Diff Criteria

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Diff Criteria Attributes (LDAP Object: dcmUiDiffCriteria)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiDiffCriteriaTitle:
    .. _uiDiffCriteria-dcmuiDiffCriteriaTitle:

    :ref:`UI Diff Criteria Title <uiDiffCriteria-dcmuiDiffCriteriaTitle>`",string,"Title of Diff Criteria

    (dcmuiDiffCriteriaTitle)"
    "
    .. _dicomDescription:
    .. _uiDiffCriteria-dicomDescription:

    :ref:`UI Diff Criteria Description <uiDiffCriteria-dicomDescription>`",string,"Unconstrained text description of this UI Diff Criteria

    (dicomDescription)"
    "
    .. _dcmuiDiffCriteriaNumber:
    .. _uiDiffCriteria-dcmuiDiffCriteriaNumber:

    :ref:`UI Diff Criteria Number <uiDiffCriteria-dcmuiDiffCriteriaNumber>`",integer,"Attribute Set Number used to order Attribute Sets.

    (dcmuiDiffCriteriaNumber)"
    "
    .. _dcmuiDiffIncludeMissing:
    .. _uiDiffCriteria-dcmuiDiffIncludeMissing:

    :ref:`UI Including Missing <uiDiffCriteria-dcmuiDiffIncludeMissing>`",boolean,"Indicate if missing Studies shall be included

    (dcmuiDiffIncludeMissing)"
    "
    .. _dcmAttributeSetID:
    .. _uiDiffCriteria-dcmAttributeSetID:

    :ref:`Attribute Set ID <uiDiffCriteria-dcmAttributeSetID>`",string,"ID of Attribute Set specifying compared attributes

    (dcmAttributeSetID)"
    "
    .. _dcmuiDiffGroupButton:
    .. _uiDiffCriteria-dcmuiDiffGroupButton:

    :ref:`UI Diff Group Button(s) <uiDiffCriteria-dcmuiDiffGroupButton>`",string,"UI Diff Group Button

    Enumerated values:

    synchronize

    export

    reject

    (dcmuiDiffGroupButton)"
    "
    .. _dcmuiDiffAction:
    .. _uiDiffCriteria-dcmuiDiffAction:

    :ref:`UI Diff Action(s) <uiDiffCriteria-dcmuiDiffAction>`",string,"UI Diff Action

    Enumerated values:

    patient-update

    study-reject-export

    study-reject

    study-export

    (dcmuiDiffAction)"
