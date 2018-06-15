Sample Request
--------------

.. code-block:: xml


POST http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource \
-H 'Content-Type: multipart/related; boundary="MIMEBoundary_4693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca"; type="application/xop+xml"; start="<0.5693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca@apache.org>"; start-info="application/soap+xml"; action="urn:dicom:ws:wado:2011:RetrieveRenderedImagingDocumentSet"' \
--data-binary '--MIMEBoundary_4693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca
Content-Type: application/xop+xml; charset=UTF-8; type="application/soap+xml"
Content-Transfer-Encoding: binary
Content-ID: <0.5693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca@apache.org>

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
  <soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
    <wsa:To soapenv:mustUnderstand="true">http://localhost:8080/dcm4chee-arc/xdsi/ImagingDocumentSource</wsa:To>
    <wsa:MessageID soapenv:mustUnderstand="true">urn:uuid:3FC3AA9541DB19A2CA1509719154150</wsa:MessageID>
    <wsa:Action soapenv:mustUnderstand="true">urn:dicom:ws:wado:2011:RetrieveRenderedImagingDocumentSet</wsa:Action>
  </soapenv:Header>
  <soapenv:Body>
    <wado:RetrieveRenderedImagingDocumentSetRequest xmlns:wado="urn:dicom:wado:ws:2011" xmlns:xdsb="urn:ihe:iti:xds-b:2007">
      <wado:StudyRequest studyInstanceUID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569">
        <wado:SeriesRequest seriesInstanceUID="1.3.12.2.1107.5.8.1.12345678.199508041416590859569.0">
          <wado:RenderedDocumentRequest>
            <xdsb:RepositoryUniqueId>1.3.6.1.4.1.21367.13.80.110</xdsb:RepositoryUniqueId>
            <xdsb:DocumentUniqueId>1.3.12.2.1107.5.8.1.12345678.199508041416590859569.0.1</xdsb:DocumentUniqueId>
            <wado:Rows>64</wado:Rows>
            <wado:Columns>64</wado:Columns>
            <wado:WindowWidth>2000</wado:WindowWidth>
            <wado:WindowCenter>1000</wado:WindowCenter>
            <wado:ImageQuality>50</wado:ImageQuality>
            <wado:FrameNumber>1</wado:FrameNumber>
            <wado:ContentTypeList>
              <wado:ContentType>image/jpeg</wado:ContentType>
            </wado:ContentTypeList>
          </wado:RenderedDocumentRequest>
        </wado:SeriesRequest>
      </wado:StudyRequest>
    </wado:RetrieveRenderedImagingDocumentSetRequest>
  </soapenv:Body>
</soapenv:Envelope>
--MIMEBoundary_4693e5ce87c3f1a8a06ebc9bbc9911b2e46e1863a7ac87ca--'


Sample Response
---------------

.. code-block:: xml


HTTP/1.1 200 OK
Connection: keep-alive
X-Powered-By: Undertow/1
Server: WildFly/11
Content-Type: multipart/related; type="application/xop+xml"; boundary="uuid:87b1feb2-f5b3-4ecf-a2bc-0c709dcd7900";
    start="<root.message@cxf.apache.org>"; start-info="application/soap+xml"
Content-Length: 3479
Date: Fri, 15 Jun 2018 10:00:46 GMT

--uuid:87b1feb2-f5b3-4ecf-a2bc-0c709dcd7900
Content-Type: application/xop+xml; charset=UTF-8; type="application/soap+xml"
Content-Transfer-Encoding: binary
Content-ID: <root.message@cxf.apache.org>

<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Header>
        <Action xmlns="http://www.w3.org/2005/08/addressing">
            urn:dicom:ws:wado:2011:RetrieveRenderedImagingDocumentSetResponse
        </Action>
        <MessageID xmlns="http://www.w3.org/2005/08/addressing">
            urn:uuid:99e92a47-7d59-407f-a5e2-408cb76559c3
        </MessageID>
        <To xmlns="http://www.w3.org/2005/08/addressing">
            http://www.w3.org/2005/08/addressing/anonymous
        </To>
        <RelatesTo xmlns="http://www.w3.org/2005/08/addressing">
            urn:uuid:3FC3AA9541DB19A2CA1509719154150
        </RelatesTo>
    </soap:Header>
    <soap:Body>
        <ns7:RetrieveRenderedImagingDocumentSetResponse
            xmlns="urn:ihe:iti:xds-b:2007"
            xmlns:ns2="urn:ihe:rad:xdsi-b:2009"
            xmlns:ns3="urn:oasis:names:tc:ebxml-regrep:xsd:rim:3.0"
            xmlns:ns4="urn:oasis:names:tc:ebxml-regrep:xsd:rs:3.0"
            xmlns:ns5="urn:oasis:names:tc:ebxml-regrep:xsd:query:3.0"
            xmlns:ns6="urn:oasis:names:tc:ebxml-regrep:xsd:lcm:3.0"
            xmlns:ns7="urn:dicom:wado:ws:2011">
          <ns7:RegistryResponse status="urn:oasis:names:tc:ebxml-regrep:ResponseStatusType:Success"/>
          <ns7:RenderedDocumentResponse>
            <RepositoryUniqueId>1.3.6.1.4.1.21367.13.80.110</RepositoryUniqueId>
            <ns7:SourceDocumentUniqueId>1.3.12.2.1107.5.8.1.12345678.199508041416590859569.0.1</ns7:SourceDocumentUniqueId>
            <ns7:Rows>64</ns7:Rows>
            <ns7:Columns>64</ns7:Columns>
            <ns7:WindowWidth>2000</ns7:WindowWidth>
            <ns7:WindowCenter>1000</ns7:WindowCenter>
            <ns7:ImageQuality>50</ns7:ImageQuality>
            <ns7:FrameNumber>1</ns7:FrameNumber>
            <mimeType>image/jpeg</mimeType>
            <Document>
                <xop:Include xmlns:xop="http://www.w3.org/2004/08/xop/include"
                    href="cid:0d4519bd-32df-4294-aaea-02decb2fb40b-2@urn%3Aihe%3Aiti%3Axds-b%3A2007"/>
            </Document>
          </ns7:RenderedDocumentResponse>
        </ns7:RetrieveRenderedImagingDocumentSetResponse>
    </soap:Body>
</soap:Envelope>

--uuid:87b1feb2-f5b3-4ecf-a2bc-0c709dcd7900
Content-Type: image/jpeg
Content-Transfer-Encoding: binary
Content-ID: <0d4519bd-32df-4294-aaea-02decb2fb40b-2@urn:ihe:iti:xds-b:2007>

This is the binary JPEG payload of the image.

--uuid:87b1feb2-f5b3-4ecf-a2bc-0c709dcd7900--