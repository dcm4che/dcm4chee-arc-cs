Audit Record Repository
=======================
Audit Record Repository related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Audit Record Repository Attributes (LDAP Object: dcmAuditRecordRepository)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) <dicomNetworkConnectionReference>`",string,"The JSON Pointers to the Network Connection objects of this Audit Record Repository

    (dicomNetworkConnectionReference)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"True if the ARR is installed on network. If not present, information about the installed status of the ARR is inherited from the device

    (dicomInstalled)"
