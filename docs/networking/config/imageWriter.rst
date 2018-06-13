Image Writer
============
Specifies Java Image IO Image Writer and Write Parameter used for compressing DICOM images

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Image Writer Attributes (LDAP Object: dcmImageWriter)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dicomTransferSyntax:

    :ref:`Transfer Syntax (dicomTransferSyntax) <dicomTransferSyntax>`",string,"Transfer Syntax to which to compress the DICOM image"
    "
    .. _dcmIIOFormatName:

    :ref:`Image IO Writer Format Name (dcmIIOFormatName) <dcmIIOFormatName>`",string,"Image IO Writer Format Name"
    "
    .. _dcmJavaClassName:

    :ref:`Java Class Name (dcmJavaClassName) <dcmJavaClassName>`",string,"Fully qualified Java class of Image IO Writer. If absent, use any Image Writer found for specified Format Name"
    "
    .. _dcmPatchJPEGLS:

    :ref:`Patch JPEG-LS (dcmPatchJPEGLS) <dcmPatchJPEGLS>`",string,"Patch JPEG-LS after compressing Enumerated values: JAI2ISO, ISO2JAI or ISO2JAI_IF_APP_OR_COM"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) (dcmImageWriteParam) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression"
