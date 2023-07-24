Rejection Note
==============
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Rejection Note Attributes (LDAP Object: dcmRejectionNote)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmRejectionNoteLabel:

    :ref:`Rejection Note Label <dcmRejectionNoteLabel>`",string,"Rejection Note Label

    (dcmRejectionNoteLabel)"
    "
    .. _dcmRejectionNoteType:

    :ref:`Rejection Note Type <dcmRejectionNoteType>`",string,"Type of Rejection Note.

    Enumerated values:

    REJECTED_FOR_QUALITY_REASONS

    REJECTED_FOR_PATIENT_SAFETY_REASONS

    INCORRECT_MODALITY_WORKLIST_ENTRY

    DATA_RETENTION_POLICY_EXPIRED

    REVOKE_REJECTION

    (dcmRejectionNoteType)"
    "
    .. _dcmRejectionNoteCode:

    :ref:`Rejection Note Code <dcmRejectionNoteCode>`",string,"Specifies Document Title of Rejection Note in format (CV, CSD, 'CM')

    (dcmRejectionNoteCode)"
    "
    .. _dcmAcceptPreviousRejectedInstance:

    :ref:`Accept Previous Rejected Instance <dcmAcceptPreviousRejectedInstance>`",string,"Specifies behavior on subsequent occurrence of instances rejected by a particular Rejection Note.

    Enumerated values:

    REJECT

    RESTORE

    IGNORE

    (dcmAcceptPreviousRejectedInstance)"
    "
    .. _dcmOverwritePreviousRejection:

    :ref:`Overwrite Previous Rejection(s) <dcmOverwritePreviousRejection>`",string,"Specifies Document Title of previous Rejection Note in format (CV, CSD, 'CM') which may be overwritten by that Rejection Note

    (dcmOverwritePreviousRejection)"
    "
    .. _dcmAcceptRejectionBeforeStorage:

    :ref:`Accept Rejection before Storage <dcmAcceptRejectionBeforeStorage>`",string,"Time interval in ISO-8601 duration format PnDTnHnMn.nS after receive of a Rejection Note, in which received object referenced by this Rejection Note are treated as rejected. Referenced objects received afterwards are treated as subsequent occurrence of an already rejected instance. If not present, Rejection Notes which refers not yet received objects will not be accepted.

    (dcmAcceptRejectionBeforeStorage)"
    "
    .. _dcmDeleteRejectedInstanceDelay:

    :ref:`Delete Rejected Instance Delay <dcmDeleteRejectedInstanceDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which instances rejected by a particular Rejection Note are deleted. Infinite if absent.

    (dcmDeleteRejectedInstanceDelay)"
    "
    .. _dcmDeleteRejectionNoteDelay:

    :ref:`Delete Rejection Note Delay <dcmDeleteRejectionNoteDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which particular Rejection Notes are deleted. Infinite if absent.

    (dcmDeleteRejectionNoteDelay)"
