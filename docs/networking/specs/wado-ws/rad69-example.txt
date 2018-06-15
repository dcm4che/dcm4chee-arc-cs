Sample Request
--------------

.. code-block:: xml

POST http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource \
-H 'Content-Type: multipart/related; boundary="MIMEBoundary_4693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca"; type="application/xop+xml"; start="<0.5693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca@apache.org>"; start-info="application/soap+xml"; action="urn:ihe:rad:2009:RetrieveImagingDocumentSet"' \
--data-binary '--MIMEBoundary_4693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca
Content-Type: application/xop+xml; charset=UTF-8; type="application/soap+xml"
Content-Transfer-Encoding: binary
Content-ID: <0.5693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca@apache.org>

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
<soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:To soapenv:mustUnderstand="true">http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource</wsa:To>
<wsa:MessageID soapenv:mustUnderstand="true">urn:uuid:3FC3AA9541DB19A2CA1509719154150</wsa:MessageID>
<wsa:Action soapenv:mustUnderstand="true">urn:ihe:rad:2009:RetrieveImagingDocumentSet</wsa:Action></soapenv:Header>
<soapenv:Body><xdsiB:RetrieveImagingDocumentSetRequest xmlns:xdsiB="urn:ihe:rad:xdsi-b:2009">
   <xdsiB:StudyRequest studyInstanceUID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569">
      <xdsiB:SeriesRequest seriesInstanceUID="1.3.12.2.1107.5.8.1.12345678.199508041416590860429">
         <xdsb:DocumentRequest xmlns:xdsb="urn:ihe:iti:xds-b:2007">
            <xdsb:RepositoryUniqueId>1.3.6.1.4.1.21367.13.80.110</xdsb:RepositoryUniqueId>
            <xdsb:DocumentUniqueId>1.3.12.2.1107.5.8.1.12345678.199508041416590861483</xdsb:DocumentUniqueId>
         </xdsb:DocumentRequest>
      </xdsiB:SeriesRequest>
   </xdsiB:StudyRequest>
   <xdsiB:TransferSyntaxUIDList>
      <xdsiB:TransferSyntaxUID>1.2.840.10008.1.2</xdsiB:TransferSyntaxUID>
   </xdsiB:TransferSyntaxUIDList>
</xdsiB:RetrieveImagingDocumentSetRequest></soapenv:Body></soapenv:Envelope>
--MIMEBoundary_4693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca--'


Sample Response
---------------

.. code-block:: xml


HTTP/1.1 200 OK
Connection: keep-alive
X-Powered-By: Undertow/1
Server: WildFly/11
Transfer-Encoding: chunked
Content-Type: multipart/related; type="application/xop+xml"; boundary="uuid:f693220a-ef9b-4e62-8d02-f8ea7918b7d9";
    start="<root.message@cxf.apache.org>"; start-info="application/soap+xml"
Date: Fri, 15 Jun 2018 10:16:08 GMT

--uuid:f693220a-ef9b-4e62-8d02-f8ea7918b7d9
Content-Type: application/xop+xml; charset=UTF-8; type="application/soap+xml"
Content-Transfer-Encoding: binary
Content-ID: <root.message@cxf.apache.org>

<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Header>
        <Action xmlns="http://www.w3.org/2005/08/addressing">
            urn:ihe:iti:2007:RetrieveDocumentSetResponse
        </Action>
        <MessageID xmlns="http://www.w3.org/2005/08/addressing">
            urn:uuid:5d716edf-91d0-46a3-8b70-46dd54d8c7c3
        </MessageID>
        <To xmlns="http://www.w3.org/2005/08/addressing">
            http://www.w3.org/2005/08/addressing/anonymous
        </To>
        <RelatesTo xmlns="http://www.w3.org/2005/08/addressing">
            urn:uuid:3FC3AA9541DB19A2CA1509719154150
        </RelatesTo>
    </soap:Header>
    <soap:Body>
        <RetrieveDocumentSetResponse
            xmlns="urn:ihe:iti:xds-b:2007"
            xmlns:ns2="urn:ihe:rad:xdsi-b:2009"
            xmlns:ns3="urn:oasis:names:tc:ebxml-regrep:xsd:rim:3.0"
            xmlns:ns4="urn:oasis:names:tc:ebxml-regrep:xsd:rs:3.0"
            xmlns:ns5="urn:oasis:names:tc:ebxml-regrep:xsd:query:3.0"
            xmlns:ns6="urn:oasis:names:tc:ebxml-regrep:xsd:lcm:3.0"
            xmlns:ns7="urn:dicom:wado:ws:2011">
          <ns4:RegistryResponse status="urn:oasis:names:tc:ebxml-regrep:ResponseStatusType:Success"/>
          <DocumentResponse>
            <RepositoryUniqueId>1.3.6.1.4.1.21367.13.80.110</RepositoryUniqueId>
            <DocumentUniqueId>1.3.12.2.1107.5.8.1.12345678.199508041416590861483<DocumentUniqueId>
            <mimeType>application/dicom</mimeType>
            <Document>
              <xop:Include xmlns:xop="http://www.w3.org/2004/08/xop/include"
              href="cid:0d4519bd-32df-4294-aaea-02decb2fb40b-4@urn%3Aihe%3Aiti%3Axds-b%3A2007"/>
            </Document>
          </DocumentResponse>
        </RetrieveDocumentSetResponse>
    </soap:Body>
</soap:Envelope>

--uuid:f693220a-ef9b-4e62-8d02-f8ea7918b7d9
Content-Type: application/dicom
Content-Transfer-Encoding: binary
Content-ID: <0d4519bd-32df-4294-aaea-02decb2fb40b-4@urn:ihe:iti:xds-b:2007>

This is the binary data of the DICOM object.