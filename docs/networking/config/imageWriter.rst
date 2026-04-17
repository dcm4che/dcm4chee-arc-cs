Image Writer
============
Specifies Java Image IO Image Writer and Write Parameter used for compressing DICOM images

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Image Writer Attributes (LDAP Object: dcmImageWriter)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomTransferSyntax:

    :ref:`Transfer Syntax <dicomTransferSyntax>`",string,"Transfer Syntax to which to compress the DICOM image

    (dicomTransferSyntax)"
    "
    .. _dcmIIOFormatName:

    :ref:`Image IO Writer Format Name <dcmIIOFormatName>`",string,"Image IO Writer Format Name

    (dcmIIOFormatName)"
    "
    .. _dcmJavaClassName:

    :ref:`Java Class Name <dcmJavaClassName>`",string,"Fully qualified Java class of Image IO Writer. If absent, use any Image Writer found for specified Format Name

    (dcmJavaClassName)"
    "
    .. _dcmPatchJPEGLS:

    :ref:`Patch JPEG-LS <dcmPatchJPEGLS>`",string,"Patch JPEG-LS after compressing

    Enumerated values:

    JAI2ISO (= Patch faulty JPEG-LS streams created by JAI-ImageIO CLibImageWriter, so the resulting JPEG-LS stream can be decoded by JPEG-LS compliant decoders)

    JAI2ISO_IF_NO_APP_OR_COM (= Amend JPEG-LS Coding parameters actually used by JAI-ImageIO, but only if the stream does NOT contain APPn or COM segments and is therefore more likely to have been actually created by JAI-ImageIO.)

    ISO2JAI (= Patch correct JPEG-LS streams, so they can be decompressed by the faulty JAI-ImageIOCLibImageReader. The resulting stream will still be correct JPEG-LS and can also be decoded by other decoders.)

    ISO2JAI_IF_APP_OR_COM (= Amend default JPEG-LS Coding parameters (for streams that do not contain them yet), but only if the stream contains APPn or COM segments - so it was certainly not created by JAI-ImageIO.)

    (dcmPatchJPEGLS)"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression

    (dcmImageWriteParam)"
