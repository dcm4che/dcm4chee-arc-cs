Application Data Flow
^^^^^^^^^^^^^^^^^^^^^

The core component of |product| is a Java Enterprise Application which provides DICOM service over the
DICOM Upper Layer protocol (DUL) and HTTP, HL7 v2 services over the Minimal Lower Layer Protocol (MLLP),
various proprietary RESTful services und a Web UI accessable by HTML 5 compliant web browsers.

It uses any LDAP v3 compatible LDAP server as configuration backend and a relational database for supporting
query and data management services.

The received DICOM objects are not stored in the database, but in a separated storage backend - typically any
type of file system, but also direct cloud storage is supported.

System-log and audit messages may stored into the ELK (Elasticsearch, Logstash, and Kibana) Stack.

.. figure:: http://uml.mvnsearch.org/github/dcm4che/dcm4chee-arc-cs/blob/master/docs/networking/model/components.puml

   System components

System components may be distributed over multiple hosts, as multiple instances of the Archive Application may share
one LDAP server and one database.

.. figure:: http://uml.mvnsearch.org/github/dcm4che/dcm4chee-arc-cs/blob/master/docs/networking/model/multihost-deployment.puml

   Multi-host deployment

System components of |product| are also available as Docker images to run within Docker containerns.

.. figure:: http://uml.mvnsearch.org/github/dcm4che/dcm4chee-arc-cs/blob/master/docs/networking/model/docker-deployment.puml

   Docker deployment

Conceptually the network services may be modeled as the following separate AEs, though they may share one
AE Title, or one AE may have multiple instances identified by different AE Title, with different configuration.

.. figure:: application-data-flow-diagram.svg

   Application Data Flow Diagram

.. figure:: wrkflw-application-data-flow-diagram.svg

   Workflow Application Data Flow Diagram

.. figure:: web-application-data-flow-diagram.svg

   Web Application Data Flow Diagram
