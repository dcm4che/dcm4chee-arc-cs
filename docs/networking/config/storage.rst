Storage
=======
Storage Descriptor

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Storage Attributes (LDAP Object: dcmStorage)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Storage ID\ :sup:`*` ",string,"Storage ID","
    .. _dcmStorageID:

    dcmStorageID_"
    "Storage URI\ :sup:`*` ",string,"RFC2079: Uniform Resource Identifier","
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
    "Deleter Threshold(s)",string,"Minimal Usable Space on Storage System. If present, studies are deleted from the Storage System, if the usable space fall below that value. Format [nn'['<schedule>']']nnn(MB|GB|MiB|GiB)","
    .. _dcmDeleterThreshold:

    dcmDeleterThreshold_"
    "Storage Property(s)",string,"Property in format <name>=<value>","
    .. _dcmProperty:

    dcmProperty_"
    "External Retrieve AET",string,"Constrain deletion of Studies, whose objects are retrievable using this AE from an external C-MOVE SCP, if usable space falls below configured threshold.","
    .. _dcmExternalRetrieveAET:

    dcmExternalRetrieveAET_"
