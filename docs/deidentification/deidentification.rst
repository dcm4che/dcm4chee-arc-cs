Application Level Confidentiality Profile Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _options-supported:

Options Supported
"""""""""""""""""

- Basic Application Confidentiality Profile
- Retain Longitudinal Temporal Information Full Dates Option
- Retain Device Identity Option
- Retain Institution Identity Option
- Retain UIDs Option


.. _attributes-removed-replace-during-protection:

Attributes removed or replaced during protection
""""""""""""""""""""""""""""""""""""""""""""""""

One can directly refer the table `Application Level Confidentiality Profile Attributes <http://dicom.nema.org/medical/dicom/current/output/html/part15.html#table_E.1-1>`_
with different `action codes <http://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_E.1.1>`_ to see
the list of attributes supported as per list of options mentioned in :numref:`options-supported`

In addition to the above list of attributes, below table lists out the private attributes and some more DICOM attributes
which are missing in `Application Level Confidentiality Profile Attributes <http://dicom.nema.org/medical/dicom/current/output/html/part15.html#table_E.1-1>`_
to be removed.

.. csv-table:: Attributes removed during protection
   :header: "Group", "Attributes"
   :file: removed-attributes.csv

.. _dummy-values:

Dummy values
""""""""""""

Following table lists attributes and the dummy values which are used to replace the attributes' values

.. csv-table:: Dummy values used to replace the attributes' values
   :header: "VR", "Dummy Value", "Attributes"
   :file: dummy-values.csv

.. _encrypted-attributes-data-sets:

Encrypted Attributes Data Sets
""""""""""""""""""""""""""""""

Encryption of attributes data sets for later re-identification is currently not supported. This inadvertently means that
keys selection for encryption, restriction on key sizes and transfer syntaxes needed for encoding/decoding of encrypted
attribute data sets are not supported as well.

.. _scope-ensuring-referential-integrity-replacement-instances:

Scope ensuring Referential Integrity of Replacement Values for UIDs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

During de-identification, the UIDs are not randomly generated but there exists a static mapping between the old and new UIDs.
The new UID is generated using `Root UID <http://www.oid-info.com/get/2.25>`_ and
`Algorithm for Creating a Name-Based UUID <https://tools.ietf.org/html/rfc4122#section-4.3>`_

.. _sop-instances-protection:

Insertion of Attributes for SOP Instances Protection
""""""""""""""""""""""""""""""""""""""""""""""""""""

Currently the archive removes or replaces attribute values as mentioned in :numref:`attributes-removed-replace-during-protection`.
It assumes that the object's attributes data set contains the attributes needed for removal/replacement; hence **no** attributes
are inserted for extra protection of SOP instance.