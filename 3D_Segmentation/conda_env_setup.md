# Conda Environment Set-Up Instructions
### 3D Segmentation Workshop (MDIA 2025)

We need to set up a conda environment to run our 3D segmentation and analyse our resulting data using Jupyter notebooks.

#### YAML files
We will be using a .yml file to setup our conda environment.  YAML files (*Yet Another Markup Language*) describe the resources used and the template location to define the environment. It helps us record and share the details of the environment we use.

> Ensure you have the [calm-3dsegm.yml](calm-3dsegm.yml) file downloaded. The file includes the packages we will be using in the notebooks.

1. Make sure you first installed conda properly by following [these instructions](./../Pages/Installation-Instructions.md#installing-conda).

2. Open Anaconda Prompt (use *Terminal* on Macs) and navigate to wherever you saved and unzipped the workshop data.
    ```
    cd <path_to_unzipped_files>/FrancisCrickInstitute-multi-dimensional-imaging-and-analysis-*******/3D_Segmentation
    ```
    You'll need to replace `<path_to_unzipped_files>` with the location of the unzipped folder on your computer.
3. Type the following to create a new environment:
    ```
    conda env create -f calm-3dsegm.yml
    ```
4. Check that the environment was created:
    ```
    conda env list
    ```
5. Activate your new environment so you can use it:
    ```
    conda activate calm-3dsegm
    ```
6. Install the kernel manager, remote_ikernel:
    ```
    pip install remote_ikernel
    ```
7. Once installed, we can link the kernel to Jupyter with the following command:
  ```
  python -m ipykernel install --user --name=calm-3dsegm --display-name "MDIA 3D Segmentation"
  ```
8. Open Jupyter notebooks from the terminal:
    ```
    jupyter notebook
    ```
9. Once it opens, create a new notebook and try running:
  ```
  import stardist
  ```
  If it works, we are on the right track!


For more information on using conda, see [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).

For a detailed explanation on Jupyter Lab, visit the [Jupyter Lab User Documentation](https://jupyterlab.readthedocs.io/en/latest/)

