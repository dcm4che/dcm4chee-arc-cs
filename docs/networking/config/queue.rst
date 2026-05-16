Queue
=====
Managed Task Queue

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: Queue Attributes (LDAP Object: dcmQueue)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmQueueName:
    .. _queue-dcmQueueName:

    :ref:`Queue Name <queue-dcmQueueName>`",string,"Task Queue Name

    (dcmQueueName)"
    "
    .. _dicomInstalled:
    .. _queue-dicomInstalled:

    :ref:`installed <queue-dicomInstalled>`",boolean,"If false, processing of tasks in this queue is paused.

    (dicomInstalled)"
    "
    .. _dcmMaxTasksParallel:
    .. _queue-dcmMaxTasksParallel:

    :ref:`Maximum parallel Tasks <queue-dcmMaxTasksParallel>`",integer,"Maximal number of tasks processed in parallel.

    (dcmMaxTasksParallel)"
    "
    .. _dicomDescription:
    .. _queue-dicomDescription:

    :ref:`DICOM Description <queue-dicomDescription>`",string,"Textual description of the DICOM entity

    (dicomDescription)"
    "
    .. _dcmMaxRetries:
    .. _queue-dcmMaxRetries:

    :ref:`Maximum Number of Retries <queue-dcmMaxRetries>`",integer,"Maximal number of retries to process tasks scheduled in a specific queue.

    (dcmMaxRetries)"
    "
    .. _dcmRetryDelay:
    .. _queue-dcmRetryDelay:

    :ref:`Retry Delay <queue-dcmRetryDelay>`",string,"Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS.

    (dcmRetryDelay)"
    "
    .. _dcmMaxRetryDelay:
    .. _queue-dcmMaxRetryDelay:

    :ref:`Maximum Retry Delay <queue-dcmMaxRetryDelay>`",string,"Maximal Delay to retry to process tasks scheduled in a specific queue in ISO-8601 duration format PnDTnHnMn.nS. Infinite if absent.

    (dcmMaxRetryDelay)"
    "
    .. _dcmRetryDelayMultiplier:
    .. _queue-dcmRetryDelayMultiplier:

    :ref:`Retry Delay Multiplier <queue-dcmRetryDelayMultiplier>`",integer,"Multiplier in % that will take effect on top of dcmRetryDelay with dcmMaxRetryDelay to be taken into account.

    (dcmRetryDelayMultiplier)"
    "
    .. _dcmRetryOnWarning:
    .. _queue-dcmRetryOnWarning:

    :ref:`Retry on Warning <queue-dcmRetryOnWarning>`",boolean,"Enables retries to process tasks not only on failure but also on a warning outcome status in a specific queue.

    (dcmRetryOnWarning)"
    "
    .. _dcmPurgeQueueMessageCompletedDelay:
    .. _queue-dcmPurgeQueueMessageCompletedDelay:

    :ref:`Delay for purging completed tasks <queue-dcmPurgeQueueMessageCompletedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which completed tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageCompletedDelay)"
    "
    .. _dcmPurgeQueueMessageFailedDelay:
    .. _queue-dcmPurgeQueueMessageFailedDelay:

    :ref:`Delay for purging failed tasks <queue-dcmPurgeQueueMessageFailedDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which failed tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageFailedDelay)"
    "
    .. _dcmPurgeQueueMessageWarningDelay:
    .. _queue-dcmPurgeQueueMessageWarningDelay:

    :ref:`Delay for purging warning tasks <queue-dcmPurgeQueueMessageWarningDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which warning tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageWarningDelay)"
    "
    .. _dcmPurgeQueueMessageCanceledDelay:
    .. _queue-dcmPurgeQueueMessageCanceledDelay:

    :ref:`Delay for purging canceled tasks <queue-dcmPurgeQueueMessageCanceledDelay>`",string,"Delay in ISO-8601 duration format PnDTnHnMn.nS after which canceled tasks are purged. If absent, there is no deletion for that particular queue

    (dcmPurgeQueueMessageCanceledDelay)"
    "
    .. _dcmSchedule:
    .. _queue-dcmSchedule:

    :ref:`Restrict Scheduling(s) <queue-dcmSchedule>`",string,"Restrict Scheduling to specified time ranges.

    (dcmSchedule)"
