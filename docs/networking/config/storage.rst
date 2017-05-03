Storage
=======
Storage Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Storage Attributes (LDAP Object: dcmStorage)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**Storage ID**",string,"Storage ID","
    .. _dcmStorageID:

    dcmStorageID_"
    "**Storage URI**",string,"RFC2079: Uniform Resource Identifier","
    .. _dcmURI:

    dcmURI_"
    "Digest Algorithm",string,"Algorithm for generation of check sums: 'MD5' or 'SHA-1'","
    .. _dcmDigestAlgorithm:

    dcmDigestAlgorithm_"
    "Instance Availability",string,"Instance Availability: ONLINE, NEARLINE or OFFLINE. ONLINE if absent.","
    .. _dcmInstanceAvailability:

    dcmInstanceAvailability_"
    "Read Only",boolean,"Indicates if a Storage System is read only; false if absent.","
    .. _dcmReadOnly:

    dcmReadOnly_"
    "Cache",boolean,"Indicates if a Storage System acts as cache - i.e. least recently used objects will be deleted if the usable space fall below the configured Storage Threshold; false if absent.","
    .. _dcmCache:

    dcmCache_"
    "Storage Threshold(s)",string,"Minimal Usable Space on Storage System. The behavior if the usable space fall below that value, depends if the Storage System is marked as cache. In that case least recently used objects will be deleted. Otherwise the Storage System will be removed from the list of configured Storage Systems of the Network AE requesting that Storage System. Format [nn'['<schedule>']']nnn(MB|GB|MiB|GiB).","
    .. _dcmStorageThreshold:

    dcmStorageThreshold_"
    "Storage Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
    "External Retrieve AET",string,"Constrain deletion of Studies, whose objects are retrievable using this AE from an external C-MOVE SCP, if usable space falls below configured threshold.","
    .. _dcmExternalRetrieveAET:

    dcmExternalRetrieveAET_"
