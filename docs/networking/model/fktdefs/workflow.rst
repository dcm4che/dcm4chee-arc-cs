Workflow Application Entity
"""""""""""""""""""""""""""

Worklist Update attempts to download a Worklist from a remote node. If the Workflow AE establishes an Association to a remote AE, it will transfer all worklist items via the open Association. During receiving the worklist response items are counted and the query processing is canceled if the configurable limit of items is reached. The results will be displayed in a separate list, which will be cleared with the next Worklist Update.
The Workflow AE performs the creation of a MPPS Instance automatically whenever images are acquired. Further updates on the MPPS data can be performed interactively from the related MPPS user interface. The MPPS "Complete" or "Discontinued" states can only be set from the user interface.
