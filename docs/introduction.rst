Introduction
************

.. _revision:

Revision History
================

.. csv-table:: Revision History
   :header: "Document Version", "Date of Issue", "Author", "Description"

   5.0.0, "Dec 06, 2015", gz, Initial Draft
   5.10.5, "Aug 11, 2017", gz, Correct Asynchronous Nature
   |release|, |today|, Current Draft

.. _audience:

Audience
========
This document is written for the people that need to understand how |product| will integrate into their
healthcare facility. This includes both those responsible for overall imaging network policy and architecture,
as well as integrators who need to have a detailed understanding of the DICOM features of the product. This
document contains some basic DICOM definitions so that any reader may understand how this product implements
DICOM features. However, integrators are expected to fully understand all the DICOM terminology, how the tables
in this document relate to the product's functionality, and how that functionality integrates with other devices
that support compatible DICOM features.

.. _remarks:

Remarks
=======
The scope of this DICOM Conformance Statement is to facilitate integration between |product| and other
DICOM products. The Conformance Statement should be read and understood in conjunction with the DICOM Standard.
DICOM by itself does not guarantee interoperability. The Conformance Statement does, however, facilitate a
first-level comparison for interoperability between different applications supporting compatible DICOM functionality.

This Conformance Statement is not supposed to replace validation with other DICOM equipment to ensure proper exchange
of intended information. In fact, the user should be aware of the following important issues:

* The comparison of different Conformance Statements is just the first step towards assessing interconnectivity and
  interoperability between the product and other DICOM conformant equipment.

* Test procedures should be defined and executed to validate the required level of interoperability with specific
  compatible DICOM equipment, as established by the healthcare facility.

* |product| has participated in an industry-wide testing program sponsored by Integrating the Healthcare
  Enterprise (IHE). The IHE Integration Statement for |product|, together with the IHE Technical Framework,
  may facilitate the process of validation testing.

.. _terms:

Terms and Definitions
=====================
Informal definitions are provided for the following terms used in this Conformance Statement. The DICOM Standard is
the authoritative source for formal definitions of these terms.

.. glossary::

   Abstract Syntax
      The information agreed to be exchanged between applications, generally equivalent to a Service/Object Pair (SOP)
      Class. Examples: Verification SOP Class, Modality Worklist Information Model Find SOP Class, Computed Radiography
      Image Storage SOP Class.

   Application Entity (AE)
      An end point of a DICOM information exchange, including the DICOM network or media interface software; i.e.,
      the software that sends or receives DICOM information objects or messages. A single device may have multiple
      Application Entities.

   Application Entity Title (AET)
      The externally known name of an Application Entity, used to identify a DICOM application to other DICOM
      applications on the network.

   Application Context
      The specification of the type of communication used between Application Entities. Example: DICOM network protocol.

   Association
      A network communication channel set up between Application Entities.

   Attribute
      A unit of information in an object definition; a data element identified by a tag. The information may be a
      complex data structure (Sequence), itself composed of lower level data elements. Examples: Patient ID (0010,0020),
      Accession Number (0008,0050), Photometric Interpretation (0028,0004), Procedure Code Sequence (0008,1032).

   Information Object Definition (IOD)
      The specified set of Attributes that comprise a type of data object; does not represent a specific instance of
      the data object, but rather a class of similar data objects that have the same properties. The Attributes may
      be specified as Mandatory (Type 1), Required but possibly unknown (Type 2), or Optional (Type 3), and there may
      be conditions associated with the use of an Attribute (Types 1C and 2C). Examples: MR Image IOD, CT Image IOD,
      Print Job IOD.

   Joint Photographic Experts Group (JPEG)
      A set of standardized image compression techniques, available for use by DICOM applications.

   Media Application Profile
      The specification of DICOM information objects and encoding exchanged on removable media (e.g., CDs)

   Module
      A set of Attributes within an Information Object Definition that are logically related to each other.
      Example: Patient Module includes Patient Name, Patient ID, Patient Birth Date, and Patient Sex.

   Negotiation
      First phase of Association establishment that allows Application Entities to agree on the types of data to be
      exchanged and how that data will be encoded.

   Presentation Context
      The set of DICOM network services used over an Association, as negotiated between Application Entities; includes
      Abstract Syntaxes and Transfer Syntaxes.

   Protocol Data Unit (PDU)
      A packet (piece) of a DICOM message sent across the network. Devices must specify the maximum size packet they
      can receive for DICOM messages.

   Security Profile
      A set of mechanisms, such as encryption, user authentication, or digital signatures, used by an Application Entity
      to ensure confidentiality, integrity, and/or availability of exchanged DICOM data

   Service Class Provider (SCP)
      Role of an Application Entity that provides a DICOM network service; typically, a server that performs operations
      requested by another Application Entity (Service Class User). Examples: Picture Archiving and Communication System
      (image storage SCP, and image query/retrieve SCP), Radiology Information System (modality worklist SCP).

   Service Class User (SCU)
      Role of an Application Entity that uses a DICOM network service; typically, a client. Examples: imaging modality
      (image storage SCU, and modality worklist SCU), imaging workstation (image query/retrieve SCU)

   Service/Object Pair Class (SOP Class)
      The specification of the network or media transfer (service) of a particular type of data (object); the fundamental
      unit of DICOM interoperability specification. Examples: Ultrasound Image Storage Service, Basic Grayscale Print
      Management.

   Service/Object Pair Instance (SOP Instance)
      An information object; a specific occurrence of information exchanged in a SOP Class. Examples: a specific
      x-ray image.

   Tag
      A 32-bit identifier for a data element, represented as a pair of four digit hexadecimal numbers, the "group"
      and the "element". If the "group" number is odd, the tag is for a private (manufacturer-specific) data element.
      Examples: (0010,0020) [Patient ID], (07FE,0010) [Pixel Data], (0019,0210) [private data element]

   Transfer Syntax
      The encoding used for exchange of DICOM information objects and messages. Examples: JPEG compressed (images),
      little endian explicit value representation.

   Unique Identifier (UID)
      A globally unique "dotted decimal" string that identifies a specific object or a class of objects;
      an ISO-8824 Object Identifier. Examples: Study Instance UID, SOP Class UID, SOP Instance UID.

   Value Representation (VR)
      The format type of an individual DICOM data element, such as text, an integer, a person's name, or a code.
      DICOM information objects can be transmitted with either explicit identification of the type of each data element
      (Explicit VR), or without explicit identification (Implicit VR); with Implicit VR, the receiving application must
      use a DICOM data dictionary to look up the format of each data element.
