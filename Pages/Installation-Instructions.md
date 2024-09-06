# Preparation For Introduction to Image Analysis Workshop

Please read the following instructions carefully to prepare for the workshop. Completing these steps prior to the workshop is essential to ensure we stay on schedule. If you are having any trouble with the below instructions, please reach out for help:
* For issues with FIJI or QuPath, contact Dave (David.Barry@crick.ac.uk)
* For issues with CellProfiler or conda, contact Todd (Todd.Fallesen@crick.ac.uk)

## Installing FIJI

1. Download FIJI from [here](https://fiji.sc/).

   ![FIJI Webpage](./../assets/FIJI.png)

2. To avoid any permissions issues, install FIJI is in your home directory:
   * PC: `C:\users\<your user name>`
   * Mac: `/Users/<your user name>`

   > **WARNING: FIJI *must* be installed in a location where it has write permission - otherwise, it cannot update itself**

3. Start FIJI and allow the updater to run:

   ![FIJI Updater](./../assets/Updater.png)

4. (Optional) If the updater does not run automatically, select `Help > Update`:

   ![Run FIJI Updater](./../assets/Run_Updater.png)

5. If FIJI produces any error messages, it is most likely because it does not have the necessary permissions to update itself - return to step #2 and double-check the location of the installation.

## Installing QuPath

~~1. Download QuPath from [here](https://qupath.github.io/).~~

~~2. Follow the installation instructions [here](https://qupath.readthedocs.io/en/0.5/docs/intro/installation.html#installation).~~

1. Download QuPath ver 0.4.3
    - Please go to the download page of QuPath [here](https://github.com/qupath/qupath/releases#0.4.3)
    - Follow the instructions to install QuPath v.4.3 on the platform of your laptop

### Installing QuPath OMERO extension
~~1. Download QuPath OMERO Glencoe OMERO extension version 0.4.3-gs [here](https://github.com/glencoesoftware/qupath-extension-omero-web/releases/download/v0.4.3-gs/qupath-extension-omero-web-0.4.3-gs.jar)~~
1. Download the BIOP QuPath extension ver 0.7.0 [here](https://github.com/BIOP/qupath-extension-biop-omero/releases/download/v0.7.0/qupath-extension-biop-omero-0.7.0.zip)
    - you will need to unzip the content.
2. Start up QuPath and drag the unzipped file onto the main QuPath window.
  - If you haven't installed any extensions before, you'll be prompted to select a QuPath user directory. The extension will then be copied to a location inside that directory.
4. You might then need to restart QuPath (but not your computer).

## Installing CellProfiler

1. Download CellProfiler from [here](https://cellprofiler.org/releases)
2. Get started with CellProfiler by following [these instructions](https://cellprofiler.org/getting-started).

## Installing conda

1. Install Miniconda by following the installation instructions for your operating system at [this page](https://docs.anaconda.com/free/miniconda/miniconda-install/)
2. Please check the installation worked properly by opening the Terminal (MacOS) or Anaconda Prompt (Windows) and typing `conda list`. If conda has been installed correctly, a list of installed packages appears.
3. You can find a conda "cheat sheet" [here](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf), which you may find useful for reference during the workshop. 

FAQ: "What should I do if I already have `conda` installed on my machine?"

Please make sure that your `conda` installation is fully up-to-date. To do so, run the following command:
```
conda update -n base conda
```
