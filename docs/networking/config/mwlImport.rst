MWL Import
==========
Specifies import of Scheduled Procedure Step from external MWL SCP

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: MWL Import Attributes (LDAP Object: dcmMwlImport)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmMWLImportID:
    .. _mwlImport-dcmMWLImportID:

    :ref:`MWL Import ID <mwlImport-dcmMWLImportID>`",string,"ID of MWL Import

    (dcmMWLImportID)"
    "
    .. _dicomAETitle:
    .. _mwlImport-dicomAETitle:

    :ref:`Calling AE Title <mwlImport-dicomAETitle>`",string,"Calling AE Title used in A-ASSOCIATE-RQ to external MWL SCP

    (dicomAETitle)"
    "
    .. _dcmMergeMWLSCP:
    .. _mwlImport-dcmMergeMWLSCP:

    :ref:`Source MWL SCP <mwlImport-dcmMergeMWLSCP>`",string,"AE Title of external MWL SCP to query for Scheduled Procedure Step to import.

    (dcmMergeMWLSCP)"
    "
    .. _dcmMWLWorklistLabel:
    .. _mwlImport-dcmMWLWorklistLabel:

    :ref:`MWL Worklist Label <mwlImport-dcmMWLWorklistLabel>`",string,"Value of Worklist Label (0074,1202) of imported MWL items fetched from Source MWL SCP. If absent, imported MWL items are provided by all MWL SCP Archive Network AEs.

    (dcmMWLWorklistLabel)"
    "
    .. _dcmDuration:
    .. _mwlImport-dcmDuration:

    :ref:`Import not before <mwlImport-dcmDuration>`",string,"Import Scheduled Procedure Steps from external MWL SCP to Scheduled Procedure Steps scheduled earlier in the future than the specified Time interval in ISO-8601 duration format PnDTnHnMn.nS; if absent, import all Scheduled Procedure Steps which are scheduled in the future.

    (dcmDuration)"
    "
    .. _dcmMWLImportNotOlder:
    .. _mwlImport-dcmMWLImportNotOlder:

    :ref:`Import not older than <mwlImport-dcmMWLImportNotOlder>`",string,"Import Scheduled Procedure Steps from external MWL SCP to Scheduled Procedure Steps scheduled later in the past than the specified Time interval in ISO-8601 duration format PnDTnHnMn.nS; if absent, import all Scheduled Procedure Steps which are scheduled in the past.

    (dcmMWLImportNotOlder)"
    "
    .. _dcmMWLImportFilterBySCU:
    .. _mwlImport-dcmMWLImportFilterBySCU:

    :ref:`Filter by SCU <mwlImport-dcmMWLImportFilterBySCU>`",boolean,"Indicates to apply specified filter on matches returned by external MWL SCP.

    (dcmMWLImportFilterBySCU)"
    "
    .. _dcmMWLImportDeleteNotFound:
    .. _mwlImport-dcmMWLImportDeleteNotFound:

    :ref:`Delete not found <mwlImport-dcmMWLImportDeleteNotFound>`",boolean,"Indicates to delete Scheduled Procedure Steps from local MWL not returned by external MWL SCP.

    (dcmMWLImportDeleteNotFound)"
    "
    .. _dcmProperty:
    .. _mwlImport-dcmProperty:

    :ref:`Matching Keys(s) <mwlImport-dcmProperty>`",string,"Filter Attributes in format ({AttributeTagOrKeyword}|{SequenceTagOrKeyword.AttributeTagOrKeyword})={value}. Eg: ScheduledProcedureStepSequence.ScheduledStationAETitle=MODALITY_XY

    (dcmProperty)"
    "
    .. _dcmIncludeField:
    .. _mwlImport-dcmIncludeField:

    :ref:`Return Keys(s) <mwlImport-dcmIncludeField>`",string,"Attributes in format (all|{AttributeTagOrKeyword}|{SequenceTagOrKeyword.AttributeTagOrKeyword}) requested from the external MWL SCP additional to attributes required to be supported by MWL SCPs according DICOM. 'all' requests all attributes configured by the Patient and the MWL Attribute Filter of the Archive.

    (dcmIncludeField)"
