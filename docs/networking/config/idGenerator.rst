ID Generator
============
ID Generator

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: ID Generator Attributes (LDAP Object: dcmIDGenerator)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmIDGeneratorName:

    :ref:`ID Generator Name (dcmIDGeneratorName) <dcmIDGeneratorName>`",string,"ID Generator Name. Enumerated values: PatientID, AccessionNumber, RequestedProcedureID or ScheduledProcedureStepID"
    "
    .. _dcmIDGeneratorFormat:

    :ref:`ID Generator Format (dcmIDGeneratorFormat) <dcmIDGeneratorFormat>`",string,"Format string used by this ID Generator. %0<width>d will be replaced by a sequential number with leading zeros according the given width"
    "
    .. _dcmIDGeneratorInitialValue:

    :ref:`ID Generator Initial Value (dcmIDGeneratorInitialValue) <dcmIDGeneratorInitialValue>`",integer,"Initial value for sequence used by this ID Generator."
