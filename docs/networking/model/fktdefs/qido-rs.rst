QIDO-RS
"""""""

The reception of a QIDO-RS GET request will activate the QIDO-RS Provider. An internal query request is sent to the search capabilities of the associated PACS or Vendor Neutral Archive (VNA). The search result is based upon the URL of the QIDO-RS GET request. The response is a status code indicating the success, warning, or failure of the search along with any matching results stored in the Remote PACS or VNA.