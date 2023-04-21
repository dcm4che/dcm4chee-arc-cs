HL7 Application
===============
HL7 Application information

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: HL7 Application Attributes (LDAP Object: hl7Application)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _hl7ApplicationName:

    :ref:`HL7 Application name <hl7ApplicationName>`",string,"HL7 Application and Facility name (Application|Facility)

    (hl7ApplicationName)"
    "
    .. _dicomNetworkConnectionReference:

    :ref:`Network Connection Reference(s) <dicomNetworkConnectionReference>`",string,"The JSON Pointers to the Network Connection objects for this HL7 Application

    (dicomNetworkConnectionReference)"
    "
    .. _hl7AcceptedSendingApplication:

    :ref:`Accepted Sending Application(s) <hl7AcceptedSendingApplication>`",string,"Application|Facility name of accepted Sending Application(s); any if absent

    (hl7AcceptedSendingApplication)"
    "
    .. _hl7OtherApplicationName:

    :ref:`Other HL7 Application Name(s) <hl7OtherApplicationName>`",string,"Additional HL7 Application and Facility name (Application|Facility) - will also accept HL7 messages with such Receiving Application and Facility name

    (hl7OtherApplicationName)"
    "
    .. _hl7AcceptedMessageType:

    :ref:`Accepted Message Type(s) <hl7AcceptedMessageType>`",string,"Message Type(s) (MessageType^TriggerEvent) of accepted messages

    (hl7AcceptedMessageType)"
    "
    .. _hl7DefaultCharacterSet:

    :ref:`Default Character Set <hl7DefaultCharacterSet>`",string,"Character Set used to decode received messages if not specified by MSH-18.

    (hl7DefaultCharacterSet)"
    "
    .. _hl7SendingCharacterSet:

    :ref:`Sending Character Set <hl7SendingCharacterSet>`",string,"Character Set used to encode HL7 messages sent from archive.

    (hl7SendingCharacterSet)"
    "
    .. _hl7RequiredMSHField:

    :ref:`HL7 Required MSH Fields(s) <hl7RequiredMSHField>`",integer,"MSH fields to be validated if missing or not, according to `IHE RAD TF Vol 2 Message Control requirements <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf#page=43>`_. If absent, `previous default checks in dcm4che library <https://dcm4chee-arc-hl7cs.readthedocs.io/en/latest/hl7-impl-notes.html#error-codes-mapping>`_ are applied.

    (hl7RequiredMSHField)"
    "
    .. _dicomDescription:

    :ref:`HL7 Description <dicomDescription>`",string,"Unconstrained text description of the HL7 Application

    (dicomDescription)"
    "
    .. _dicomApplicationCluster:

    :ref:`Application Cluster(s) <dicomApplicationCluster>`",string,"Locally defined names for a subset of related applications

    (dicomApplicationCluster)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"True if the HL7 Application is installed on network. If not present, information about the installed status of the HL7 Application is inherited from the device

    (dicomInstalled)"
    ":doc:`archiveHL7Application` ",object,"DICOM Archive HL7 Application related information"

.. toctree::

    archiveHL7Application
