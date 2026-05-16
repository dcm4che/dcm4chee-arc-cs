RESTful Forward Rule
====================
RESTful Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: RESTful Forward Rule Attributes (LDAP Object: dcmRsForwardRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:
    .. _rsForwardRule-cn:

    :ref:`Name <rsForwardRule-cn>`",string,"Arbitrary/Meaningful name of the RESTful Forward Rule

    (cn)"
    "
    .. _dcmWebAppName:
    .. _rsForwardRule-dcmWebAppName:

    :ref:`Web Application name <rsForwardRule-dcmWebAppName>`",string,"Name of the Web Application

    (dcmWebAppName)"
    "
    .. _dcmURIPattern:
    .. _rsForwardRule-dcmURIPattern:

    :ref:`Request URL Pattern <rsForwardRule-dcmURIPattern>`",string,"Only forward requests which match the given Regular Expression. If prefixed with !, only forward requests which does not match the given Regular Expression.

    (dcmURIPattern)"
    "
    .. _dcmHostnamePattern:
    .. _rsForwardRule-dcmHostnamePattern:

    :ref:`Hostname Pattern <rsForwardRule-dcmHostnamePattern>`",string,"Only forward requests received from clients which hostname match the given Regular Expression. If prefixed with !, only forward requests from clients which hostname does not match the given Regular Expression.

    (dcmHostnamePattern)"
    "
    .. _dcmIPAddressPattern:
    .. _rsForwardRule-dcmIPAddressPattern:

    :ref:`IP Address Pattern <rsForwardRule-dcmIPAddressPattern>`",string,"Only forward requests received from clients which match the given Regular Expression. If prefixed with !, only forward requests from clients which IP address does not match the given Regular Expression.

    (dcmIPAddressPattern)"
    "
    .. _dcmRSOperation:
    .. _rsForwardRule-dcmRSOperation:

    :ref:`RESTful Operation(s) <rsForwardRule-dcmRSOperation>`",string,"Name of RESTful Operation which shall be forwarded to another archive instance.

    Enumerated values:

    CreatePatient

    UpdatePatient

    UpdatePatientByPID

    DeletePatient

    DeletePatientByPID

    ChangePatientID

    ChangePatientID2

    ChangePatientIDByPID

    MergePatient

    MergePatient2

    MergePatientByPID

    UnmergePatient

    UnmergePatientByPID

    SupplementIssuer

    UpdateCharset

    UpdateStudy

    UpdateStudyRequest

    UpdateSeries

    UpdateSeriesRequest

    DeleteStudy

    RejectStudy

    RejectSeries

    RejectInstance

    ApplyRetentionPolicy

    ReimportStudy

    UpdateStudyExpirationDate

    UpdateSeriesExpirationDate

    UpdateStudyAccessControlID

    UpdateSeriesAccessControlID

    MoveStudyToPatient

    LinkStudyToMWLMerge

    CreateMWL

    UpdateMWL

    UpdateMWLStatus

    DeleteMWL

    (dcmRSOperation)"
