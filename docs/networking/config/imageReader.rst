Image Reader
============
Specifies Java Image IO Image Readers used for decompressing compressed DICOM images

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Image Reader Attributes (LDAP Object: dcmImageReader)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dicomTransferSyntax:

    :ref:`Transfer Syntax <dicomTransferSyntax>`",string,"Transfer Syntax of compressed DICOM image

    (dicomTransferSyntax)"
    "
    .. _dcmIIOFormatName:

    :ref:`Image IO Reader Format Name <dcmIIOFormatName>`",string,"Image IO Reader Format Name

    (dcmIIOFormatName)"
    "
    .. _dcmJavaClassName:

    :ref:`Java Class Name <dcmJavaClassName>`",string,"Fully qualified Java class of Image IO Reader. If absent, use any Image Reader found for specified Format Name

    (dcmJavaClassName)"
    "
    .. _dcmPatchJPEGLS:

    :ref:`Patch JPEG-LS <dcmPatchJPEGLS>`",string,"Patch JPEG-LS before decompressing

    Enumerated values:

    JAI2ISO (= Patch faulty JPEG-LS streams created by JAI-ImageIO CLibImageWriter, so the resulting JPEG-LS stream can be decoded by JPEG-LS compliant decoders)

    JAI2ISO_IF_NO_APP_OR_COM (= Amend JPEG-LS Coding parameters actually used by JAI-ImageIO, but only if the stream does NOT contain APPn or COM segments and is therefore more likely to have been actually created by JAI-ImageIO.)

    ISO2JAI (= Patch correct JPEG-LS streams, so they can be decompressed by the faulty JAI-ImageIOCLibImageReader. The resulting stream will still be correct JPEG-LS and can also be decoded by other decoders.)

    ISO2JAI_IF_APP_OR_COM (= Amend default JPEG-LS Coding parameters (for streams that do not contain them yet), but only if the stream contains APPn or COM segments - so it was certainly not created by JAI-ImageIO.)

    (dcmPatchJPEGLS)"
    "
    .. _dcmImageReadParam:

    :ref:`Image Read Param(s) <dcmImageReadParam>`",string,"Image Read Parameter(s) (name=value)

    (dcmImageReadParam)"
