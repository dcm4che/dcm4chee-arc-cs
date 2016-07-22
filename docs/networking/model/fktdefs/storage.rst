Storage Application Entity
""""""""""""""""""""""""""

The existence of a send-job queue entry with associated network destination will activate the Storage AE. An association request is sent to the destination AE and upon successful negotiation of a Presentation Context the image transfer is started. If the association cannot be opened, the related send-job is set to an error state and can be restarted by the user via job control interface. By default, the Storage AE will not try to initiate another association for this send-job automatically. However, an automatic retry (retry-timer, retry­count) can be configured by a CSE.
