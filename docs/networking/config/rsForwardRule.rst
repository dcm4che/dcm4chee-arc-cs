RESTful Forward Rule
====================
RESTful Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: RESTful Forward Rule Attributes (LDAP Object: dcmRsForwardRule)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Name",string,"Arbitrary/Meaningful name of the RESTful Forward Rule","
    .. _cn:

    cn_"
    "Target Base URL",string,"Target URL without operation specific part, eg. http://<host>:<port>/dcm4chee-arc/aets/<aet>/rs/","
    .. _dcmURI:

    dcmURI_"
    "RESTful Operation(s)",string,"Name of RESTful Operation which shall be forwarded to another archive instance. Enumerated values: CreatePatient, UpdatePatient, DeletePatient, ChangePatientID, MergePatient, MergePatients, UpdateStudy, DeleteStudy, CopyInstances, MoveInstances, RejectStudy, RejectSeries, RejectInstance, UpdateStudyExpirationDate, UpdateSeriesExpirationDate, CreateMWL, UpdateMWL or DeleteMWL","
    .. _dcmRSOperation:

    dcmRSOperation_"
