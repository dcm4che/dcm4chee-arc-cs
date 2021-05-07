MWL Import Rule
===============
Specifies import of Scheduled Procedure Step from external MWL SCP

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: MWL Import Rule Attributes (LDAP Object: dcmMwlImportRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmMWLImportID:

    :ref:`MWL Import Rule ID <dcmMWLImportID>`",string,"ID of MWL Import Rule

    (dcmMWLImportID)"
    "
    .. _dicomAETitle:

    :ref:`Calling AE Title <dicomAETitle>`",string,"Calling AE Title used in A-ASSOCIATE-RQ to external MWL SCP

    (dicomAETitle)"
    "
    .. _dcmMergeMWLSCP:

    :ref:`Source MWL SCP <dcmMergeMWLSCP>`",string,"AE Title of external MWL SCP to query for Scheduled Procedure Step to import.

    (dcmMergeMWLSCP)"
    "
    .. _dcmDestinationAE:

    :ref:`Destination MWL SCP <dcmDestinationAE>`",string,"AE Title of local MWL SCP feeded/updated by Scheduled Procedure Steps returned by external MWL SCP.

    (dcmDestinationAE)"
    "
    .. _dcmDuration:

    :ref:`Import not before <dcmDuration>`",string,"Restrict import of Scheduled Procedure Steps from external MWL SCP to Scheduled Procedure Steps scheduled earlier in the future than the specified Time interval in ISO-8601 duration format PnDTnHnMn.nS; if absent, import all Scheduled Procedure Steps which are scheduled in the future.

    (dcmDuration)"
    "
    .. _dcmMWLImportNotOlder:

    :ref:`Import not older than <dcmMWLImportNotOlder>`",string,"Restrict import of Scheduled Procedure Steps from external MWL SCP to Scheduled Procedure Steps scheduled later in the past than the specified Time interval in ISO-8601 duration format PnDTnHnMn.nS; if absent, import all Scheduled Procedure Steps which are scheduled in the past.

    (dcmMWLImportNotOlder)"
    "
    .. _dcmMWLImportFilterBySCU:

    :ref:`Filter by SCU <dcmMWLImportFilterBySCU>`",boolean,"Indicates to apply specified filter on matches returned by external MWL SCP.

    (dcmMWLImportFilterBySCU)"
    "
    .. _dcmMWLImportDeleteNotFound:

    :ref:`Delete not found <dcmMWLImportDeleteNotFound>`",boolean,"Indicates to delete Scheduled Procedure Steps from local MWL not returned by external MWL SCP.

    (dcmMWLImportDeleteNotFound)"
    "
    .. _dcmProperty:

    :ref:`Matching Keys(s) <dcmProperty>`",string,"Filter Attributes in format ({AttributeTagOrKeyword}|{SequenceTagOrKeyword.AttributeTagOrKeyword})={value}. Eg: ScheduledProcedureStepSequence.ScheduledStationAETitle=MODALITY_XY

    (dcmProperty)"
    "
    .. _dcmIncludeField:

    :ref:`Return Keys(s) <dcmIncludeField>`",string,"Attributes in format (all|{AttributeTagOrKeyword}|{SequenceTagOrKeyword.AttributeTagOrKeyword}) requested from the external MWL SCP additional to attributes required to be supported by MWL SCPs according DICOM. 'all' requests all attributes configured by the Patient and the MWL Attribute Filter of the Archive.

    (dcmIncludeField)"
