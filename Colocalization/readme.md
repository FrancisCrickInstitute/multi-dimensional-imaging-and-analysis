## These are the files used in the Colocalization workshop taught by Todd.
* [Colocalization.pptx](./Colocalization.pptx) - Powerpoint slides given during the lecture
* ExampleSpeckles.zip - CellProfiler example pipeline for relating objects
* split_channel_multiple_series_and_rename.ijm - Fiji macro for splitting all the multi channel z-stacks in a folder into individual tif images
* stardist_process_folder.ijm - Fiji macro for running stardist on a set of images in a folder


For split_channel_multiple_series_and_rename.ijm, run the macro, Select a folder of images that you want to split into channels and z-slices, select and output folder, and the file extension (.tif, .nd2, .czi, etc) and click run to split all the images into individual tif files.

For stardist_process_folder.ijm, select the folder with your images and specify the channel you wish to run stardist on, and click "run" and the macro will run stardist on all the images in that folder with that channel name. 
