RESTful Forward Rule
====================
RESTful Forward Rule

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: RESTful Forward Rule Attributes (LDAP Object: dcmRsForwardRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the RESTful Forward Rule

    (cn)"
    "
    .. _dcmWebAppName:

    :ref:`Web Application name <dcmWebAppName>`",string,"Name of the Web Application

    (dcmWebAppName)"
    "
    .. _dcmTLSAllowAnyHostname:

    :ref:`TLS Allow Any Hostname <dcmTLSAllowAnyHostname>`",boolean,"If the other server requires HTTPS and this config option is set to true the other server’s certificate is validated via the truststore, but host name validation is not done.

    (dcmTLSAllowAnyHostname)"
    "
    .. _dcmTLSDisableTrustManager:

    :ref:`TLS Disable Trust Manager <dcmTLSDisableTrustManager>`",boolean,"If the other server requires HTTPS and this config option is set to true you do not have to specify a truststore

    (dcmTLSDisableTrustManager)"
    "
    .. _dcmURIPattern:

    :ref:`Request URL Pattern <dcmURIPattern>`",string,"Only forward requests which match the given Regular Expression. If prefixed with !, only forward requests which does not match the given Regular Expression.

    (dcmURIPattern)"
    "
    .. _dcmRSOperation:

    :ref:`RESTful Operation(s) <dcmRSOperation>`",string,"Name of RESTful Operation which shall be forwarded to another archive instance. Enumerated values: CreatePatient, UpdatePatient, DeletePatient, ChangePatientID, MergePatient, MergePatients, UpdateStudy, DeleteStudy, RejectStudy, RejectSeries, RejectInstance, UpdateStudyExpirationDate, UpdateSeriesExpirationDate, ApplyRetentionPolicy, CreateMWL, UpdateMWL, DeleteMWL or UpdateStudyAccessControlID.

    (dcmRSOperation)"
