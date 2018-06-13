Queue
=====
Managed JMS Queue

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Queue Attributes (LDAP Object: dcmQueue)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmQueueName:

    :ref:`Queue Name (dcmQueueName) <dcmQueueName>`",string,"JMS Queue Name"
    "
    .. _dcmJndiName:

    :ref:`JNDI Name (dcmJndiName) <dcmJndiName>`",string,"JNDI Name"
    "
    .. _dicomDescription:

    :ref:`DICOM Description (dicomDescription) <dicomDescription>`",string,"Textual description of the DICOM entity"
    "
    .. _dcmMaxRetries:

    :ref:`Maximum Number of Retries (dcmMaxRetries) <dcmMaxRetries>`",integer,"Maximal number of retries to process tasks scheduled in a specific queue."
    "
    .. _dcmRetryDelay:

    :ref:`Retry Delay (dcmRetryDelay) <dcmRetryDelay>`",string,"Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS."
    "
    .. _dcmMaxRetryDelay:

    :ref:`Maximum Retry Delay (dcmMaxRetryDelay) <dcmMaxRetryDelay>`",string,"Maximal Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS. Infinite if absent."
    "
    .. _dcmRetryDelayMultiplier:

    :ref:`Retry Delay Multiplier (dcmRetryDelayMultiplier) <dcmRetryDelayMultiplier>`",integer,"Multiplier in % that will take effect on top of dcmRetryDelay with dcmMaxRetryDelay to be taken into account."
    "
    .. _dcmRetryOnWarning:

    :ref:`Retry on Warning (dcmRetryOnWarning) <dcmRetryOnWarning>`",boolean,"Enables retries to process tasks not only on failure but also on a warning outcome status in a specific queue."
    "
    .. _dcmPurgeQueueMessageCompletedDelay:

    :ref:`Delay for purging completed queue messages (dcmPurgeQueueMessageCompletedDelay) <dcmPurgeQueueMessageCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which completed queue messages are purged. If absent, there is no deletion for that particular queue"
    "
    .. _dcmMaxQueueSize:

    :ref:`Maximum Queue Size (dcmMaxQueueSize) <dcmMaxQueueSize>`",integer,"Maximal number of scheduled tasks in the queue. If the number of scheduled tasks reaches the limit, an attempt to schedule another tasks will fail. 0 = no limitation."
