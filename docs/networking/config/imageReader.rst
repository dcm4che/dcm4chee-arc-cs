Image Reader
============
Specifies Java Image IO Image Readers used for decompressing compressed DICOM images

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Image Reader Attributes (LDAP Object: dcmImageReader)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dicomTransferSyntax:

    :ref:`Transfer Syntax (dicomTransferSyntax) <dicomTransferSyntax>`",string,"Transfer Syntax of compressed DICOM image"
    "
    .. _dcmIIOFormatName:

    :ref:`Image IO Reader Format Name (dcmIIOFormatName) <dcmIIOFormatName>`",string,"Image IO Reader Format Name"
    "
    .. _dcmJavaClassName:

    :ref:`Java Class Name (dcmJavaClassName) <dcmJavaClassName>`",string,"Fully qualified Java class of Image IO Reader. If absent, use any Image Reader found for specified Format Name"
    "
    .. _dcmPatchJPEGLS:

    :ref:`Patch JPEG-LS (dcmPatchJPEGLS) <dcmPatchJPEGLS>`",string,"Patch JPEG-LS before decompressing Enumerated values: JAI2ISO, ISO2JAI or ISO2JAI_IF_APP_OR_COM"
