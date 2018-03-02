UI Permission
=============
UI Permission

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: UI Permission Attributes (LDAP Object: dcmUiPermission)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "UI Permission Name",string,"Name of Permission for UI Action","
    .. _dcmuiPermissionName:

    dcmuiPermissionName_"
    "UI Action",string,"UI Action Enumerated values: menu-studies, menu-dashboard, menu-correct_data, menu-lifecycle_management, menu-audit_record_repository, menu-configuration, menu-move_data, menu-statistics, menu-monitoring, tab-monitoring->queues, tab-monitoring->export, tab-monitoring->external_retrieve, tab-monitoring->control, tab-monitoring->associations, tab-monitoring->storage_commitments, tab-monitoring->storage_systems, tab-statistics->statistics, tab-configuration->devices, tab-configuration->ae_list, tab-configuration->hl7_applications, tab-move_data->retrieve, tab-move_data->export, action-devicelist-device_configuration, action-studies-patient, action-studies-mwl, action-studies-studie, action-studies-serie, action-studies-instance, action-studies-copy_merge_move, action-studies-more_function, action-studies-diff, action-studies-count, action-studies-size, action-studies-viewer, action-studies-verify_storage_commitment, action-studies-download, action-monitoring->queues-all_action, action-monitoring->export-all_action, action-monitoring->external_retrieve-all_action, action-monitoring->queues-single_action, action-monitoring->export-single_action or action-monitoring->external_retrieve-single_action","
    .. _dcmuiAction:

    dcmuiAction_"
    "UI Action Parameter(s)",string,"UI Action Parameter Enumerated values: edit, create, delete, export, accessible, visible, merge, upload, reject or restore","
    .. _dcmuiActionParam:

    dcmuiActionParam_"
    "Accepted User Role(s)",string,"Accepted User Role","
    .. _dcmAcceptedUserRole:

    dcmAcceptedUserRole_"
