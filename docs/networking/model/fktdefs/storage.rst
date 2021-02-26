Storage Application Entity
""""""""""""""""""""""""""

The Storage Application Entity receives images and other Composite Object Instances from remote AEs.

Compressed images and non-image objects are stored as received on the storage backend configured for the Storage AE.
Uncompressed images may be compressed according configurable compression rules before they are stored with all
attributes on the storage backend.

A configurable sub-set of attributes are extracted from the received objects and stored in the data base.
These attributes may be coerced according configurable coercion rules on receive time or by data management
functions at any time after.

If configured, the Storage AE queries an external RESTful service for permission to store a study on receive of the
first object of a study. If the service does not grant the permission to store the study, the object and all
following received objects of that study will be refused.

The behavior on receive of an object which *SOP Instance UID* matches with the *SOP Instance UID* of a previous
received object is configurable: The new received object may overwrite the previous one, be stored additionally or
just be ignored, dependent if it was sent by the same source and/or dependent if it belongs to the same series as the
previous received object. That allows to operate with object sources which does not support use of
`Imaging Object Change Management (IOCM) <http://wiki.ihe.net/index.php/Imaging_Object_Change_Management>`_ services
to correct failures in the originally sent objects, but which just send the objects with corrected attributes but
unchanged *SOP Instance UID* again.

The behavior how to treat differences in Patient, Study or Series attributes in received instances belonging
to the same Patient, Study or Series is also configurable: the attributes of the already existing Patient, Study or
Series record in the data base may

* not be updated at all,
* be supplemented with attributes from the new received object, not included in the existing record,
* be additionally overwritten by different values of the attributes in the new received object,
* be completely replaced by the extracted attributes from the new received object.

The Storage AE may also associate a configured *Access Control ID* to a received study. Query/Retrieve AEs can be
configured to only provide access to data and objects of studies, which associated *Access Control ID* matches one
of the *Access Control IDs* configured for that Query/Retrieve AE.

If configured, the Storage AE will set the *Retention Period* of received studies according a configured
*Study Retention Policy*. Individual series of a study may get a different *Retention Period* than the whole study.
If activated, studies - or individual series - will be deleted automatically after its *Retention Period* expires.
On the other hand, |product| can be configured to prevent manual deletion of objects of studies which
*Retention Period* is not yet expired.

The Storage AE can also be configured to act as a cache archive, which deletes least recent accessed studies
according configured thresholds of the storage backend.

Received objects may be exported according configurable export rules, which are triggered by matching
sending/receiving AE Titles and/or matching object attribute values. Received objects of one series or study may be
accumulated, before all objects of the series or study are exported in one task. Export by DICOM storage is invoked
by the :doc:`query-retrieve`.

Objects may be also received from the Storage AE as result of a forwarded retrieve request to a configured fallback
archive by the :doc:`query-retrieve`. In that case, the received objects will be forwarded immediately to the final
retrieve destination by the :doc:`query-retrieve`.

The receive of objects may trigger the notification of configured remote AEs by the DICOM Instance Available
Notification service invoked by the :doc:`workflow`.

If the Storage AE receives a Key Object Selection (KOS) Document with a Document Title which matches one of the
configured Rejection Note Code Values, the object will be treated as Rejection Note and the instances referenced
by the object will be marked as rejected. The Key Selection Object Document itself is stored on the storage backend
as other objects received from the Storage AE. Further treatment of the rejected instances and the KOS Document is
specific to the particular type of rejection.

By default, the KOS Document Titles specified by `Imaging Object Change Management (IOCM)
<http://wiki.ihe.net/index.php/Imaging_Object_Change_Management>`_ are configured:

- (113001, DCM, "Rejected for Quality Reasons")

  - Hide/Show rejected instances dependend on Query/Retrieve AE
  - Show KOS Document
  - Ignore subsequent occurrence of rejected instances
- (113037, DCM, "Rejected for Patient Safety Reasons")

  - Hide rejected instances
  - Show KOS Document
  - Reject subsequent occurrence of rejected instances
- (113038, DCM, "Incorrect Modality Worklist Entry")

  - Hide rejected instances
  - Show KOS Document
  - Reject subsequent occurrence of rejected instances
- (113039, DCM, "Data Retention Rejected for Quality Reasons")

  - Hide rejected instances and KOS Document
  - Subsequent occurrence of rejected instances reverts the rejection
  - Delete rejected instances and KOS Document after delay

The Storage AE accepts requests for commitment for the storage of previous received instances - including KOS Documents
acting as Rejection Notes. For each object, for which storage commitment is requested, the Storage AE does not only
check the existence of a record for that object in the data base, but actually read the object from the storage backend,
recalculating the checksum and compare it with the checksum stored in the data base. Only for objects which recalulated
checksum matches with that in the data base the commitment to store is accepted.

The amount of time to take responsibility for the safekeeping of an objects is independent of the successful
commitment to store the object, but depends on other configuration options, particularly on the configured
*Study Retention Policy*. It is even possible to accept storage commitment requests when acting as a cache archive,
which deletes least recent accessed studies according configured thresholds of the storage backend.
