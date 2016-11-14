Query Retrieve View
===================
Specifies behavior on Rejection Note Stored

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Query Retrieve View Attributes (LDAP Object: dcmQueryRetrieveView)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Query/Retrieve View ID**",string,"Query/Retrieve View Identifier","
    .. _dcmQueryRetrieveViewID:

    dcmQueryRetrieveViewID_"
    "Show Instances Rejected By Code(s)",string,"Indicates if the Q/R Services shall show instances rejected by the specified code in format (CV, CSD, 'CM'')","
    .. _dcmShowInstancesRejectedByCode:

    dcmShowInstancesRejectedByCode_"
    "Hide Rejection Note With Code(s)",string,"Indicates if the Q/R Services shall hide Rejection Notes with the specified code in format (CV, CSD, 'CM'')","
    .. _dcmHideRejectionNoteWithCode:

    dcmHideRejectionNoteWithCode_"
    "Hide Not Rejected Instances",boolean,"Indicates if the Q/R Services shall hide instances not rejected by any reason; disabled if absent","
    .. _dcmHideNotRejectedInstances:

    dcmHideNotRejectedInstances_"
