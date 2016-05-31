Security
========

.. _security-profiles:

Security Profiles
"""""""""""""""""

The DCM4CHEE archive conforms to the bit preserving Digital Signatures Security Profile, if the STORAGE SCP AE receives a SOP Instance in an Explicit Transfer Syntax and the STORAGE SCU AE can export such SOP Instances using an Explicit Transfer Syntax.

.. _security-association-level-security:

Association Level Security
""""""""""""""""""""""""""

The QUERY-RETRIEVE-SCP AE and the STORAGE-SCP AE can both be configured to check the following DICOM values when determining whether to accept Association Open Requests:

Calling AE Title

Called AE Title

Application Context

Each SCP AE can be configured to accept Association Requests from only a limited list of Calling AE Titles. They SCP AEs can have different lists. Each SCP AE can be configured to check that the Association requester specifies the correct Called AE Title for the SCP.

In addition the IP address of the requester can be checked. The SCP AEs can be constrained to only accept Association Requests from a configured list of IP addresses. The SCP AEs can have different lists.