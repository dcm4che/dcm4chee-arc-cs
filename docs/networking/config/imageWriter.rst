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

    :ref:`Patch JPEG-LS <dcmPatchJPEGLS>`",string,"Patch JPEG-LS after compressing Enumerated values: JAI2ISO, ISO2JAI or ISO2JAI_IF_APP_OR_COM.

    (dcmPatchJPEGLS)"
    "
    .. _dcmImageWriteParam:

    :ref:`Image Write Param(s) <dcmImageWriteParam>`",string,"Image Write Parameter(s) (name=value) set at on Image Writer before compression

    (dcmImageWriteParam)"
