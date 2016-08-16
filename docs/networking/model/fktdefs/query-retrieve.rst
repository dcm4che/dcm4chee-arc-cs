Query/Retrieve Application Entity
"""""""""""""""""""""""""""""""""

The Query/Retrieve Application Entity processes queries for Patient, Study, Series, and Instance information of
received DICOM objects invoked by remote AEs. Attributes of requested entities are fetched from the database.
The objects on the storage backend are not accessed. Therefore, only the configurable sub-set of attributes which
were extracted from the received objects and stored in the data base is provided.

In addition, the Query/Retrieve Application Entity provides the ability to retrieve/transfer received DICOM objects to
remote AEs. The transfer may be originated by a retrieve request from the same or from another remote AE, it may be
caused by a configured Export Rule for received objects, or it may be triggered by the Archive Web UI, which itself
uses a RESTful service to schedule the transfer, which may be also used by other web clients.

The Query/Retrieve Application Entity may forward retrieve requests for which no matching objects were found in the
data base to a configured other DICOM Archive. Two configuration options are available:

1. Preserve the original Move Destination AE Title in the forwarded retrieve request, so the other DICOM Archive
   will directly send the requested objects to the destination AE.
2. Replace the original Move Destination AE Title in the forwarded retrieve request with the AE Title of the/a
   :doc:`storage`, so the other DICOM Archive will send the requested objects to the Storage AE and the
   Query/Retrieve AE will forward the received objects to the original Move Destination AE. If the other DICOM
   Archive signals that not all requested objects could be transfered to the Storage AE successfully, the Study and
   Series of the received objects are marked as incomplete in the data base and following retrieve request for that
   Study or Series will trigger to retry to retrieve the Study or Series from the other DICOM Archive.
