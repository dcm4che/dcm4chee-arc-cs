Queue
=====
Managed JMS Queue

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Queue Attributes (LDAP Object: dcmQueue)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmQueueName:

    :ref:`Queue Name <dcmQueueName>`",string,"JMS Queue Name

    (dcmQueueName)"
    "
    .. _dcmJndiName:

    :ref:`JNDI Name <dcmJndiName>`",string,"JNDI Name

    (dcmJndiName)"
    "
    .. _dicomDescription:

    :ref:`DICOM Description <dicomDescription>`",string,"Textual description of the DICOM entity

    (dicomDescription)"
    "
    .. _dcmMaxRetries:

    :ref:`Maximum Number of Retries <dcmMaxRetries>`",integer,"Maximal number of retries to process tasks scheduled in a specific queue.

    (dcmMaxRetries)"
    "
    .. _dcmRetryDelay:

    :ref:`Retry Delay <dcmRetryDelay>`",string,"Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS.

    (dcmRetryDelay)"
    "
    .. _dcmMaxRetryDelay:

    :ref:`Maximum Retry Delay <dcmMaxRetryDelay>`",string,"Maximal Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS. Infinite if absent.

    (dcmMaxRetryDelay)"
    "
    .. _dcmRetryDelayMultiplier:

    :ref:`Retry Delay Multiplier <dcmRetryDelayMultiplier>`",integer,"Multiplier in % that will take effect on top of dcmRetryDelay with dcmMaxRetryDelay to be taken into account.

    (dcmRetryDelayMultiplier)"
    "
    .. _dcmRetryOnWarning:

    :ref:`Retry on Warning <dcmRetryOnWarning>`",boolean,"Enables retries to process tasks not only on failure but also on a warning outcome status in a specific queue.

    (dcmRetryOnWarning)"
    "
    .. _dcmRetryInProcessOnStartup:

    :ref:`Retry IN PROCESS on Startup <dcmRetryInProcessOnStartup>`",boolean,"Indicates to retry tasks left in status IN PROCESS on system start-up.

    (dcmRetryInProcessOnStartup)"
    "
    .. _dcmPurgeQueueMessageCompletedDelay:

    :ref:`Delay for purging completed queue messages <dcmPurgeQueueMessageCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which completed queue messages are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageCompletedDelay)"
    "
    .. _dcmPurgeQueueMessageFailedDelay:

    :ref:`Delay for purging failed queue messages <dcmPurgeQueueMessageFailedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which failed queue messages are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageFailedDelay)"
    "
    .. _dcmPurgeQueueMessageWarningDelay:

    :ref:`Delay for purging warning queue messages <dcmPurgeQueueMessageWarningDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which warning queue messages are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageWarningDelay)"
    "
    .. _dcmPurgeQueueMessageCanceledDelay:

    :ref:`Delay for purging canceled queue messages <dcmPurgeQueueMessageCanceledDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which canceled queue messages are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageCanceledDelay)"
    "
    .. _dcmMaxQueueSize:

    :ref:`Maximum Queue Size <dcmMaxQueueSize>`",integer,"Maximal number of scheduled tasks in the queue. If the number of scheduled tasks reaches the limit, an attempt to schedule another tasks will fail. 0 = no limitation.

    (dcmMaxQueueSize)"
