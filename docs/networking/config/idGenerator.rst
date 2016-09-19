ID Generator
============
ID Generator

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: ID Generator Attributes (LDAP Object: dcmIDGenerator)
    :header: Name ( :sup:`*` = required ), Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "ID Generator Name\ :sup:`*` ",string,"ID Generator Name. Enumerated values: PatientID, AccessionNumber, RequestedProcedureID, ScheduledProcedureStepID","
    .. _dcmIDGeneratorName:

    dcmIDGeneratorName_"
    "ID Generator Format\ :sup:`*` ",string,"Format string used by this ID Generator. %0<width>d will be replaced by a sequential number with leading zeros according the given width","
    .. _dcmIDGeneratorFormat:

    dcmIDGeneratorFormat_"
    "ID Generator Initial Value",integer,"Initial value for sequence used by this ID Generator; 1 if absent","
    .. _dcmIDGeneratorInitialValue:

    dcmIDGeneratorInitialValue_"
