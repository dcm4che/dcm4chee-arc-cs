Query Retrieve View
===================
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Query Retrieve View Attributes (LDAP Object: dcmQueryRetrieveView)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmQueryRetrieveViewID:

    :ref:`Query/Retrieve View ID <dcmQueryRetrieveViewID>`",string,"Query/Retrieve View Identifier

    (dcmQueryRetrieveViewID)"
    "
    .. _dcmShowInstancesRejectedByCode:

    :ref:`Show Instances Rejected By Code(s) <dcmShowInstancesRejectedByCode>`",string,"Indicates if the Q/R Services shall show instances rejected by the specified code in format (CV, CSD, 'CM'')

    (dcmShowInstancesRejectedByCode)"
    "
    .. _dcmHideRejectionNoteWithCode:

    :ref:`Hide Rejection Note With Code(s) <dcmHideRejectionNoteWithCode>`",string,"Indicates if the Q/R Services shall hide Rejection Notes with the specified code in format (CV, CSD, 'CM'')

    (dcmHideRejectionNoteWithCode)"
    "
    .. _dcmHideNotRejectedInstances:

    :ref:`Hide Not Rejected Instances <dcmHideNotRejectedInstances>`",boolean,"Indicates if the Q/R Services shall hide instances not rejected by any reason.

    (dcmHideNotRejectedInstances)"
