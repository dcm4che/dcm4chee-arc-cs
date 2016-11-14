Audit Record Repository
=======================
Audit Record Repository related information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Audit Record Repository Attributes (LDAP Object: dcmAuditRecordRepository)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Network Connection Reference(s)**",string,"The JSON Pointers to the Network Connection objects of this Audit Record Repository","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "installed",boolean,"True if the ARR is installed on network. If not present, information about the installed status of the ARR is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
