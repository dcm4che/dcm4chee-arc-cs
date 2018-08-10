Delayed Compression Rule
========================
Rules for compression of stored images after a particular delay.

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Delayed Compression Rule Attributes (LDAP Object: dcmDelayedCompressionRule)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _cn:

    :ref:`Name <cn>`",string,"Arbitrary/Meaningful name of the Delayed Compression Rule.

    (cn)"
    "
    .. _dcmSOPClass:

    :ref:`Source SOP Class(s) <dcmSOPClass>`",string,"SOP Classes of stored images to which this rule applies.

    (dcmSOPClass)"
    "
    .. _dicomTransferSyntax:

    :ref:`Source Transfer Syntax(s) <dicomTransferSyntax>`",string,"Transfer Syntaxes of stored images to which this rule applies.

    (dicomTransferSyntax)"
    "
    .. _dcmAETitle:

    :ref:`Source AE Title(s) <dcmAETitle>`",string,"Source AE Titles of Series to which this rule applies or does not apply - dependent on Source AE Title Usage Flag.

    (dcmAETitle)"
    "
    .. _dcmAETitleUsageFlag:

    :ref:`Source AE Title Usage Flag <dcmAETitleUsageFlag>`",string,"Controls if the rules applies to Series which Source AE Title matches one or does not match any of the values specified by Source AE Titles. Enumerated values: MATCH or NO_MATCH.

    (dcmAETitleUsageFlag)"
    "
    .. _dcmStationName:

    :ref:`Station Name(s) <dcmStationName>`",string,"Station Names of Series to which this rule applies or does not apply - dependent on Station Name Usage Flag.

    (dcmStationName)"
    "
    .. _dcmStationNameUsageFlag:

    :ref:`Station Name Usage Flag <dcmStationNameUsageFlag>`",string,"Controls if the rules applies to Series which Station Name matches one or does not match any of the values specified by Station Name. Enumerated values: MATCH or NO_MATCH.

    (dcmStationNameUsageFlag)"
    "
    .. _dicomAETitle:

    :ref:`Archive AE Title <dicomAETitle>`",string,"Title of Archive Application Entity used for storing the compressed object.

    (dicomAETitle)"
    "
    .. _dcmDuration:

    :ref:`Compression Delay <dcmDuration>`",string,"Compression delay in ISO-8601 duration format PnDTnHnMn.nS.

    (dcmDuration)"
    "
    .. _dcmTransferSyntax:

    :ref:`Target Transfer Syntax <dcmTransferSyntax>`",string,"Transfer Syntax to which objects shall be compressed.

    (dcmTransferSyntax)"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression.

    (dcmImageWriteParam)"
