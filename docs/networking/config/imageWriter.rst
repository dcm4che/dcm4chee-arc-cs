Image Writer
============
Specifies Java Image IO Image Writer and Write Parameter used for compressing DICOM images

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Image Writer Attributes (LDAP Object: dcmImageWriter)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Transfer Syntax",string,"Transfer Syntax to which to compress the DICOM image","
    .. _dicomTransferSyntax:

    dicomTransferSyntax_"
    "Image IO Writer Format Name",string,"Image IO Writer Format Name","
    .. _dcmIIOFormatName:

    dcmIIOFormatName_"
    "Java Class Name",string,"Fully qualified Java class of Image IO Writer. If absent, use any Image Writer found for specified Format Name","
    .. _dcmJavaClassName:

    dcmJavaClassName_"
    "Patch JPEG-LS",string,"Patch JPEG-LS after compressing: JAI2ISO, ISO2JAI or ISO2JAI_IF_APP_OR_COM Enumerated values: JAI2ISO, ISO2JAI or ISO2JAI_IF_APP_OR_COM","
    .. _dcmPatchJPEGLS:

    dcmPatchJPEGLS_"
    "Image Write Param(s)",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression","
    .. _dcmImageWriteParam:

    dcmImageWriteParam_"
