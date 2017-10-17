Queue
=====
Managed JMS Queue

.. tabularcolumns:: |p{4cm}|l|p{8cm}|l|
.. csv-table:: Queue Attributes (LDAP Object: dcmQueue)
    :header: Name, Type, Description, LDAP Attribute
    :widths: 20, 7, 60, 13

    "Queue Name",string,"JMS Queue Name","
    .. _dcmQueueName:

    dcmQueueName_"
    "JNDI Name",string,"JNDI Name","
    .. _dcmJndiName:

    dcmJndiName_"
    "DICOM Description",string,"Textual description of the DICOM entity","
    .. _dicomDescription:

    dicomDescription_"
    "Maximum Number of Retries",integer,"Maximal number of retries to process tasks scheduled in a specific queue.","
    .. _dcmMaxRetries:

    dcmMaxRetries_"
    "Retry Delay",string,"Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS.","
    .. _dcmRetryDelay:

    dcmRetryDelay_"
    "Maximum Retry Delay",string,"Maximal Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS. Infinite if absent.","
    .. _dcmMaxRetryDelay:

    dcmMaxRetryDelay_"
    "Retry Delay Multiplier",integer,"Multiplier in % that will take effect on top of dcmRetryDelay with dcmMaxRetryDelay to be taken into account.","
    .. _dcmRetryDelayMultiplier:

    dcmRetryDelayMultiplier_"
    "Retry on Warning",boolean,"Enables retries to process tasks not only on failure but also on a warning outcome status in a specific queue.","
    .. _dcmRetryOnWarning:

    dcmRetryOnWarning_"
    "Delay for purging completed queue messages",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which completed queue messages are purged. If absent, there is no deletion for that particular queue","
    .. _dcmPurgeQueueMessageCompletedDelay:

    dcmPurgeQueueMessageCompletedDelay_"
    "Maximum Queue Size",integer,"Maximal number of scheduled tasks in the queue. If the number of scheduled tasks reaches the limit, an attempt to schedule another tasks will fail. 0 = no limitation.","
    .. _dcmMaxQueueSize:

    dcmMaxQueueSize_"
