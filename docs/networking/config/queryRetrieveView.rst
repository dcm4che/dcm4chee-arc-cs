Query Retrieve View
===================
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Query Retrieve View Attributes (LDAP Object: dcmQueryRetrieveView)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmQueryRetrieveViewID:
    .. _queryRetrieveView-dcmQueryRetrieveViewID:

    :ref:`Query/Retrieve View ID <queryRetrieveView-dcmQueryRetrieveViewID>`",string,"Query/Retrieve View Identifier

    (dcmQueryRetrieveViewID)"
    "
    .. _dcmShowInstancesRejectedByCode:
    .. _queryRetrieveView-dcmShowInstancesRejectedByCode:

    :ref:`Show Instances Rejected By Code(s) <queryRetrieveView-dcmShowInstancesRejectedByCode>`",string,"Indicates if the Q/R Services shall show instances rejected by the specified code in format (CV, CSD, 'CM')

    (dcmShowInstancesRejectedByCode)"
    "
    .. _dcmHideRejectionNoteWithCode:
    .. _queryRetrieveView-dcmHideRejectionNoteWithCode:

    :ref:`Hide Rejection Note With Code(s) <queryRetrieveView-dcmHideRejectionNoteWithCode>`",string,"Indicates if the Q/R Services shall hide Rejection Notes with the specified code in format (CV, CSD, 'CM')

    (dcmHideRejectionNoteWithCode)"
    "
    .. _dcmHideNotRejectedInstances:
    .. _queryRetrieveView-dcmHideNotRejectedInstances:

    :ref:`Hide Not Rejected Instances <queryRetrieveView-dcmHideNotRejectedInstances>`",boolean,"Indicates if the Q/R Services shall hide instances not rejected by any reason.

    (dcmHideNotRejectedInstances)"
