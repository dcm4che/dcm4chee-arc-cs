Image Reader
============
Specifies Java Image IO Image Readers used for decompressing compressed DICOM images

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Image Reader Attributes (LDAP Object: dcmImageReader)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Transfer Syntax",string,"Transfer Syntax of compressed DICOM image","
    .. _dicomTransferSyntax:

    dicomTransferSyntax_"
    "Image IO Reader Format Name",string,"Image IO Reader Format Name","
    .. _dcmIIOFormatName:

    dcmIIOFormatName_"
    "Java Class Name",string,"Fully qualified Java class of Image IO Reader. If absent, use any Image Reader found for specified Format Name","
    .. _dcmJavaClassName:

    dcmJavaClassName_"
    "Patch JPEG-LS",string,"Patch JPEG-LS before decompressing Enumerated values: JAI2ISO, ISO2JAI or ISO2JAI_IF_APP_OR_COM","
    .. _dcmPatchJPEGLS:

    dcmPatchJPEGLS_"
