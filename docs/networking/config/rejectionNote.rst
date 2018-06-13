Rejection Note
==============
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Rejection Note Attributes (LDAP Object: dcmRejectionNote)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmRejectionNoteLabel:

    :ref:`Rejection Note Label (dcmRejectionNoteLabel) <dcmRejectionNoteLabel>`",string,"Rejection Note Label"
    "
    .. _dcmRejectionNoteType:

    :ref:`Rejection Note Type (dcmRejectionNoteType) <dcmRejectionNoteType>`",string,"Type of Rejection Note. Enumerated values: REJECTED_FOR_QUALITY_REASONS, REJECTED_FOR_PATIENT_SAFETY_REASONS, INCORRECT_MODALITY_WORKLIST_ENTRY, DATA_RETENTION_POLICY_EXPIRED or REVOKE_REJECTION"
    "
    .. _dcmRejectionNoteCode:

    :ref:`Rejection Note Code (dcmRejectionNoteCode) <dcmRejectionNoteCode>`",string,"Specifies Document Title of Rejection Note in format (CV, CSD, 'CM')"
    "
    .. _dcmAcceptPreviousRejectedInstance:

    :ref:`Accept Previous Rejected Instance (dcmAcceptPreviousRejectedInstance) <dcmAcceptPreviousRejectedInstance>`",string,"Specifies behavior on subsequent occurrence of instances rejected by a particular Rejection Note. Enumerated values: REJECT, RESTORE or IGNORE"
    "
    .. _dcmOverwritePreviousRejection:

    :ref:`Overwrite Previous Rejection(s) (dcmOverwritePreviousRejection) <dcmOverwritePreviousRejection>`",string,"Specifies Document Title of previous Rejection Note in format (CV, CSD, 'CM') which may be overwritten by that Rejection Note"
    "
    .. _dcmDeleteRejectedInstanceDelay:

    :ref:`Delete Rejected Instance Delay (dcmDeleteRejectedInstanceDelay) <dcmDeleteRejectedInstanceDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which instances rejected by a particular Rejection Note are deleted. Infinite if absent."
    "
    .. _dcmDeleteRejectionNoteDelay:

    :ref:`Delete Rejection Note Delay (dcmDeleteRejectionNoteDelay) <dcmDeleteRejectionNoteDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which particular Rejection Notes are deleted. Infinite if absent."
