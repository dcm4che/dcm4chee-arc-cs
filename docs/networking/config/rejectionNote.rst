Rejection Note
==============
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Rejection Note Attributes (LDAP Object: dcmRejectionNote)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Rejection Note Label\ :sup:`*` ",string,"Rejection Note Label","
    .. _dcmRejectionNoteLabel:

    dcmRejectionNoteLabel_"
    "Rejection Note Type",string,"Type of Rejection Note. Enumerated values: REJECTED_FOR_QUALITY_REASONS, REJECTED_FOR_PATIENT_SAFETY_REASONS, INCORRECT_MODALITY_WORKLIST_ENTRY, DATA_RETENTION_POLICY_EXPIRED, REVOKE_REJECTION.","
    .. _dcmRejectionNoteType:

    dcmRejectionNoteType_"
    "Rejection Note Code\ :sup:`*` ",string,"Specifies Document Title of Rejection Note in format (CV, CSD, 'CM')","
    .. _dcmRejectionNoteCode:

    dcmRejectionNoteCode_"
    "Accept Previous Rejected Instance",string,"Specifies behavior on subsequent occurrence of instances rejected by a particular Rejection Note. Enumerated values: REJECT, RESTORE, IGNORE. REJECT if absent.","
    .. _dcmAcceptPreviousRejectedInstance:

    dcmAcceptPreviousRejectedInstance_"
    "Overwrite Previous Rejection(s)",string,"Specifies Document Title of previous Rejection Note in format (CV, CSD, 'CM') which may be overwritten by that Rejection Note","
    .. _dcmOverwritePreviousRejection:

    dcmOverwritePreviousRejection_"
    "Delete Rejected Instance Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which instances rejected by a particular Rejection Note are deleted. Infinite if absent.","
    .. _dcmDeleteRejectedInstanceDelay:

    dcmDeleteRejectedInstanceDelay_"
    "Delete Rejection Note Delay",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which particular Rejection Notes are deleted. Infinite if absent.","
    .. _dcmDeleteRejectionNoteDelay:

    dcmDeleteRejectionNoteDelay_"
