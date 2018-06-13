HL7 Application
===============
HL7 Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Application Attributes (LDAP Object: hl7Application)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _hl7ApplicationName:

    :ref:`HL7 Application name (hl7ApplicationName) <hl7ApplicationName>`",string,"HL7 Application and Facility name (Application|Facility)"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) (dicomNetworkConnectionReference) <dicomNetworkConnectionReference>`",string,"The JSON Pointers to the Network Connection objects for this HL7 Application"
    "
    .. _hl7AcceptedSendingApplication:

    :ref:`Accepted Sending Application(s) (hl7AcceptedSendingApplication) <hl7AcceptedSendingApplication>`",string,"Application|Facility name of accepted Sending Application(s); any if absent"
    "
    .. _hl7OtherApplicationName:

    :ref:`Other HL7 Application Name(s) (hl7OtherApplicationName) <hl7OtherApplicationName>`",string,"Additional HL7 Application and Facility name (Application|Facility) - will also accept HL7 messages with such Receiving Application and Facility name"
    "
    .. _hl7AcceptedMessageType:

    :ref:`Accepted Message Type(s) (hl7AcceptedMessageType) <hl7AcceptedMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of accepted messages"
    "
    .. _hl7DefaultCharacterSet:

    :ref:`Default Character Set (hl7DefaultCharacterSet) <hl7DefaultCharacterSet>`",string,"Character Set used to decode received messages if not specified by MSH-18."
    "
    .. _hl7SendingCharacterSet:

    :ref:`Sending Character Set (hl7SendingCharacterSet) <hl7SendingCharacterSet>`",string,"Character Set used to encode HL7 messages sent from archive."
    "
    .. _dicomDescription:

    :ref:`HL7 Description (dicomDescription) <dicomDescription>`",string,"Unconstrained text description of the HL7 Application"
    "
    .. _dicomApplicationCluster:

    :ref:`Application Cluster(s) (dicomApplicationCluster) <dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications"
    "
    .. _dicomInstalled:

    :ref:`installed (dicomInstalled) <dicomInstalled>`",boolean,"True if the HL7 Application is installed on network. If not present, information about the installed status of the HL7 Application is inherited from the device"
    ":doc:`archiveHL7Application` ",object,"DICOM Archive HL7 Application related information"

.. toctree::

    archiveHL7Application
