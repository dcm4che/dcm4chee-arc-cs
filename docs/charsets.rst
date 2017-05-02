Support of Character Sets
=========================

|product| supports all extended character sets defined in the DICOM 2017 standard, including single-byte and
multi-byte character sets as well as code extension techniques using ISO 2022 escapes in DICOM messages.

Support extends to correctly decoding and displaying the correct symbol for all names and strings found in storage
instances received over the network, and in the local database.

In addition to the default character repertoire, the Defined Terms for Specific Character Set in :numref:`charsets`
are supported:

.. csv-table:: Supported Specific Character Set Defined Terms
   :name: charsets
   :widths: 50, 25, 25
   :header: "Character Set Description", "DICOM attribute: Specific Character Set (0008,0005)", "HL7 field: Character Set MSH 18"

       "Latin alphabet No. 1", "ISO_IR 100", "8859/1"
       "Latin alphabet No. 2", "ISO_IR 101", "8859/2"
       "Latin alphabet No. 3", "ISO_IR 109", "8859/3"
       "Latin alphabet No. 4", "ISO_IR 110", "8859/4"
       "Cyrillic", "ISO_IR 144", "8859/5"
       "Arabic", "ISO_IR 127", "8859/6"
       "Greek", "ISO_IR 126", "8859/7"
       "Hebrew", "ISO_IR 138", "8859/8"
       "Latin alphabet No. 5", "ISO_IR 148", "8859/9"
       "Japanese", "ISO_IR 13", "ISO IR14"
       "Thai", "ISO_IR 166", "CNS 11643-1992"
       "Default repertoire", "ISO 2022 IR 6", "not supported [#hl7cs]_"
       "Latin alphabet No. 1", "ISO 2022 IR 100", "not supported [#hl7cs]_"
       "Latin alphabet No. 2", "ISO 2022 IR 101", "not supported [#hl7cs]_"
       "Latin alphabet No. 3", "ISO 2022 IR 109", "not supported [#hl7cs]_"
       "Latin alphabet No. 4", "ISO 2022 IR 110", "not supported [#hl7cs]_"
       "Cyrillic", "ISO 2022 IR 144", "not supported [#hl7cs]_"
       "Arabic", "ISO 2022 IR 127", "not supported [#hl7cs]_"
       "Greek", "ISO 2022 IR 126", "not supported [#hl7cs]_"
       "Hebrew", "ISO 2022 IR 138", "not supported [#hl7cs]_"
       "Latin alphabet No. 5", "ISO 2022 IR 148", "not supported [#hl7cs]_"
       "Japanese", "ISO 2022 IR 13", "not supported [#hl7cs]_"
       "Thai", "ISO 2022 IR 166", "not supported [#hl7cs]_"
       "Japanese", "ISO 2022 IR 87", "not supported [#hl7cs]_"
       "Japanese", "ISO 2022 IR 159", "not supported [#hl7cs]_"
       "Korean", "ISO 2022 IR 149", "not supported [#hl7cs]_"
       "Simplified Chinese", "ISO 2022 IR 58", "not supported [#hl7cs]_"
       "Unicode in UTF-8", "ISO_IR 192", "UNICODE UTF-8"
       "GB18030", "GB18030", "GB 18030-2000"
       "GBK", "GBK", "GB 18030-2000"

.. [#hl7cs] Escape sequences supporting multiple character sets in HL7 v2 messages are not supported.

