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
    .. _dicomDescription:

    :ref:`Queue Description <dicomDescription>`",string,"Unconstrained text description of the Queue

    (dicomDescription)"
    "
    .. _dicomInstalled:

    :ref:`installed <dicomInstalled>`",boolean,"If false, processing of tasks in this queue is paused.

    (dicomInstalled)"
    "
    .. _dcmMaxTasksParallel:

    :ref:`Maximum parallel Tasks <dcmMaxTasksParallel>`",integer,"Maximal number of tasks processed in parallel.

    (dcmMaxTasksParallel)"
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
    .. _dcmPurgeQueueMessageCompletedDelay:

    :ref:`Delay for purging completed tasks <dcmPurgeQueueMessageCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which completed tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageCompletedDelay)"
    "
    .. _dcmPurgeQueueMessageFailedDelay:

    :ref:`Delay for purging failed tasks <dcmPurgeQueueMessageFailedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which failed tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageFailedDelay)"
    "
    .. _dcmPurgeQueueMessageWarningDelay:

    :ref:`Delay for purging warning tasks <dcmPurgeQueueMessageWarningDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which warning tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageWarningDelay)"
    "
    .. _dcmPurgeQueueMessageCanceledDelay:

    :ref:`Delay for purging canceled tasks <dcmPurgeQueueMessageCanceledDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which canceled tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageCanceledDelay)"
    "
    .. _dcmSchedule:

    :ref:`Restrict Scheduling(s) <dcmSchedule>`",string,"Restrict Scheduling to specified time ranges. Use Maximum Queue Size to control maximal number of Tasks processed between specified time ranges. Only effective for scheduling 'TO SCHEDULE' Retrieve Tasks.

    (dcmSchedule)"
