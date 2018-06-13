Query Retrieve View
===================
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Query Retrieve View Attributes (LDAP Object: dcmQueryRetrieveView)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmQueryRetrieveViewID:

    :ref:`Query/Retrieve View ID (dcmQueryRetrieveViewID) <dcmQueryRetrieveViewID>`",string,"Query/Retrieve View Identifier"
    "
    .. _dcmShowInstancesRejectedByCode:

    :ref:`Show Instances Rejected By Code(s) (dcmShowInstancesRejectedByCode) <dcmShowInstancesRejectedByCode>`",string,"Indicates if the Q/R Services shall show instances rejected by the specified code in format (CV, CSD, 'CM'')"
    "
    .. _dcmHideRejectionNoteWithCode:

    :ref:`Hide Rejection Note With Code(s) (dcmHideRejectionNoteWithCode) <dcmHideRejectionNoteWithCode>`",string,"Indicates if the Q/R Services shall hide Rejection Notes with the specified code in format (CV, CSD, 'CM'')"
    "
    .. _dcmHideNotRejectedInstances:

    :ref:`Hide Not Rejected Instances (dcmHideNotRejectedInstances) <dcmHideNotRejectedInstances>`",boolean,"Indicates if the Q/R Services shall hide instances not rejected by any reason."
