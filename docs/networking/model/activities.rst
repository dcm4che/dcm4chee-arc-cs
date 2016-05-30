Sequencing of Real-World Activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: sequencing_of_real_world_activities.svg

   Figure : Sequencing of Real-World Activities

Under normal scheduled workflow conditions the sequencing constraints illustrated in Figure B.4.1-2 apply:

1. Query Worklist
2. Receive Worklist of Modality Scheduled Procedure Steps (MSPS)
3. Select Workitem (MSPS) from Worklist
4. Start acquisition and create MPPS
5. Acquire Images
6. Complete acquisition and finalize MPPS
7. Print acquired images (optional step)
8. Store acquired images and any associated Grayscale Softcopy Presentation State (GSPS) instances.
9. If the Image Manager is configured as an archive device the Storage AE will request Storage Commitment for the images and associated GSPS instances.

Other workflow situations (e.g., unscheduled procedure steps) will have other sequencing constraints. Printing could equally take place after the acquired images have been stored. Printing could be omitted completely if no printer is connected or hard copies are not required.