WADO-URI
""""""""

The reception of a WADO request will activate the AE. An internal request is sent to the search capabilities of the DCM4CHEE-WADO-SERVICE. This request is based upon the request parameters or the URL resource end point from the WADO request. The response is a list of all SOP instances stored on the DCM4CHEE-PACS-ARCHIVE that match the request parameters. If there are no matching instances, the AE will indicate this in the WADO response. For all matching instances, the AE will utilize the internal image transfer request to obtain a copy of each instance. If the request was for retrieval of instances, these instances will be returned. If the request was for retrieval of rendered instances, then the AE will render each instance and return the rendered results.
