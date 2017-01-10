HL7 Application
===============
HL7 Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: HL7 Application Attributes (LDAP Object: hl7Application)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "**HL7 Application name**",string,"HL7 Application and Facility name (Application|Facility)","
    .. _hl7ApplicationName:

    hl7ApplicationName_"
    "**Network Connection Reference(s)**",string,"The JSON Pointers to the Network Connection objects for this HL7 Application","
    .. _dicomNetworkConnectionReference:

    dicomNetworkConnectionReference_"
    "Accepted Sending Application(s)",string,"Application|Facility name of accepted Sending Application(s); any if absent","
    .. _hl7AcceptedSendingApplication:

    hl7AcceptedSendingApplication_"
    "Accepted Message Type(s)",string,"Message Type(s) (MessageType^TriggerEvent) of accepted messages","
    .. _hl7AcceptedMessageType:

    hl7AcceptedMessageType_"
    "Default Character Set",string,"Character Set used to decode received messages if not specified by MSH-18, ASCII if absent","
    .. _hl7DefaultCharacterSet:

    hl7DefaultCharacterSet_"
    "installed",boolean,"True if the HL7 Application is installed on network. If not present, information about the installed status of the HL7 Application is inherited from the device","
    .. _dicomInstalled:

    dicomInstalled_"
    ":doc:`archiveHL7Application` ",object,"DICOM Archive HL7 Application related information","
    .. _dcmArchiveHL7Application:

    dcmArchiveHL7Application_"

.. toctree::

    archiveHL7Application
