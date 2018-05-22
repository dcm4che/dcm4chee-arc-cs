Application Level Confidentiality Profile Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _attributes-removed-during-protection:

Attributes removed during protection
""""""""""""""""""""""""""""""""""""

//TODO

.. _attributes-replaced-by-dummy-values:

Attributes replaced by dummy values
"""""""""""""""""""""""""""""""""""

- Acquisition Device Processing Description (0018,1400)
- Contrast Bolus Agent (0018,0010)
- Dose Reference UID (300A,0013)
- Operators Name (0008,1070)
- Person Name (0040,A123)
- Protocol Name (0018,1030)
- Verifying Observer Name (0040,A075)
- Verifying Organization (0040,A027)
- Detector ID (0018,700A)
- Device Serial Number (0018,1000)
- Station Name (0008,1010)
- Institution Name (0008,0080)
- Acquisition Date Time (0008,002A)
- Content Date (0008,0023)
- Content Time (0008,0033)
- Start Acquisition Date Time (0018,9516)
- End Acquisition Date Time (0018,9517)
- Verification Date Time (0040,A030)
- Series Date (0008,0021)
- Series Time (0008,0031)

.. _dummy-values-generation:

Dummy Values Generation
"""""""""""""""""""""""

Following table lists the dummy values which are used to replace the attributes' values

.. table:: Dummy values used for replacement of attributes' values

   +-----------------------------------------------------------------------------+
   | VR | Dummy Value    | Attributes                                            |
   +====+================+=======================================================+
   | DA | 19991111       | Series Date (0008,0021)                               |
   |    |                +-------------------------------------------------------+
   |    |                | Content Date (0008,0023)                              |
   +----+----------------+-------------------------------------------------------+
   | DT | 19991111111111 | Acquisition Date Time (0008,002A)                     |
   |    |                +-------------------------------------------------------+
   |    |                | Start Acquisition Date Time (0018,9516)               |
   |    |                +-------------------------------------------------------+
   |    |                | End Acquisition Date Time (0018,9517)                 |
   |    |                +-------------------------------------------------------+
   |    |                | Verification Date Time (0040,A030)                    |
   +----+----------------+-------------------------------------------------------+
   | TM | 111111         | Series Time (0008,0031)                               |
   |    |                +-------------------------------------------------------+
   |    |                | Content Time (0008,0033)                              |
   +----+----------------+-------------------------------------------------------+
   | IS | 0              |                                                       |
   +----+----------------+-------------------------------------------------------+
   | DS | 0              |                                                       |
   +----+----------------+-------------------------------------------------------+
   | LO | REMOVED        | Acquisition Device Processing Description (0018,1400) |
   |    |                +-------------------------------------------------------+
   |    |                | Contrast Bolus Agent (0018,0010)                      |
   |    |                +-------------------------------------------------------+
   |    |                | Protocol Name (0018,1030)                             |
   |    |                +-------------------------------------------------------+
   |    |                | Verifying Organization (0040,A027)                    |
   |    |                +-------------------------------------------------------+
   |    |                | Device Serial Number (0018,1000)                      |
   |    |                +-------------------------------------------------------+
   |    |                | Institution Name (0008,0080)                          |
   +----+----------------+-------------------------------------------------------+
   | SH | REMOVED        | Detector ID (0018,700A)                               |
   |    |                +-------------------------------------------------------+
   |    |                | Station Name (0008,1010)                              |
   +----+----------------+-------------------------------------------------------+
   | UI | REMOVED        | Dose Reference UID (300A,0013)                        |
   +----+----------------+-------------------------------------------------------+
   | PN | REMOVED        | Operators Name (0008,1070)                            |
   |    |                +-------------------------------------------------------+
   |    |                | Person Name (0040,A123)                               |
   |    |                +-------------------------------------------------------+
   |    |                | Verifying Observer Name (0040,A075)                   |
   +----+----------------+-------------------------------------------------------+

.. _encrypted-attributes-data-sets:

Encrypted Attributes Data Sets
""""""""""""""""""""""""""""""

//TODO

.. _scope-ensuring-referential-integrity-replacement-instances:

Scope ensuring Referential Integrity of Replacement Values
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

//TODO


.. _sop-instances-protection:

SOP Instances Protection
""""""""""""""""""""""""

//TODO


.. _transfer-syntaxes-supported:

Transfer Syntaxes Supported
"""""""""""""""""""""""""""

//TODO

.. _options-supported:

Options Supported
"""""""""""""""""

- Basic Application Confidentiality Profile
- Retain Longitudinal Temporal Information Full Dates Option
- Retain Device Identity Option
- Retain Institution Identity Option
- Retain UIDs Option

.. _additional-restrictions:

Additional Restrictions
"""""""""""""""""""""""

//TODO