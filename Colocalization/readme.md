# Co-localisation

In this module, we will cover how to use [CellProfiler](https://cellprofiler.org/). We will first learn how to perform simple quantifications of objects of interest in an image. Next, we are going to look at two different approaches to measure co-localisation. Finally, we will have some time to explore the data acquired during the practical session.

## Download slides (Optional)

All the slides that will be used in this session are [here](https://www.dropbox.com/scl/fi/ybdnchdhwis8mjvm3h4e7/20250908_CellProfiler.pptx?rlkey=hfjwk6g9keihoty8f1b4me6yv&st=pmndhzhr&dl=0).

## Download demo data

We're going to be working with some example datasets, which you can download from [here](https://www.dropbox.com/scl/fo/0vj6sbdxlxto4eqpz51ig/APm69Lc2tieTkY3gES9Pk1U?rlkey=b2189k2ohbi18wsvf908sgimk&st=olkuhtj0&dl=0).


## Fiji macro

* [SplitChannels.ijm](./SplitChannels.ijm) - [Fiji](https://imagej.net/software/fiji/) macro for splitting all the multi channel z-stacks in a folder into individual tif images. Takes as input a folder containing the images you want to split, a folder to save the output and the required file extension (e.g., .tif). It requires the [Bio-Formats](https://imagej.net/formats/bio-formats) plugin in Fiji.

## CellProfiler pipelines

* [01_identify_objects.cppipe](./01_identify_objects.cppipe) - CellProfiler pipeline to perform simple quantifications of objects of interest in an image
* [02_colocalisation.cppipe](./02_colocalisation.cppipe) - CellProfiler pipeline to measure co-localisation with two different approaches

