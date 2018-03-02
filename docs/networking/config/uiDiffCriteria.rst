UI Diff Criteria
================
UI Diff Criteria

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: UI Diff Criteria Attributes (LDAP Object: dcmUiDiffCriteria)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "UI Diff Criteria Title",string,"Title of Diff Criteria","
    .. _dcmuiDiffCriteriaTitle:

    dcmuiDiffCriteriaTitle_"
    "UI Diff Criteria Description",string,"Unconstrained text description of this UI Diff Criteria","
    .. _dicomDescription:

    dicomDescription_"
    "UI Diff Criteria Number",integer,"Attribute Set Number used to order Attribute Sets.","
    .. _dcmuiDiffCriteriaNumber:

    dcmuiDiffCriteriaNumber_"
    "UI Including Missing",boolean,"Indicate if missing Studies shall be included","
    .. _dcmuiDiffIncludeMissing:

    dcmuiDiffIncludeMissing_"
    "Attribute Set ID",string,"ID of Attribute Set specifying compared attributes","
    .. _dcmAttributeSetID:

    dcmAttributeSetID_"
    "UI Diff Group Button(s)",string,"UI Diff Group Button Enumerated values: synchronize, export or reject","
    .. _dcmuiDiffGroupButton:

    dcmuiDiffGroupButton_"
    "UI Diff Action(s)",string,"UI Diff Action Enumerated values: patient-update, study-reject-export, study-reject or study-export","
    .. _dcmuiDiffAction:

    dcmuiDiffAction_"