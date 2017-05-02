General Message Format Conventions
==================================

Message Structure
-----------------

- :ref:`audit-general-message-event`
- :ref:`audit-general-message-active-participant` (1..N)
- :ref:`audit-general-message-audit-source`
- :ref:`audit-general-message-participant-object` (0..N)

.. csv-table:: Event
   :name: audit-general-message-event
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "EventID", "M", "The identifier for the family of event. E.g., 'User Authentication'"
         "<TODO>",,

.. csv-table:: Active Participant
   :name: audit-general-message-active-participant
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "<TODO>",,

.. csv-table:: Audit Source
   :name: audit-general-message-audit-source
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "<TODO>",,

.. csv-table:: Participant Object
   :name: audit-general-message-participant-object
   :widths: 30, 5, 65
   :header: "Field Name", "Opt", "Description"

         "<TODO>",,
