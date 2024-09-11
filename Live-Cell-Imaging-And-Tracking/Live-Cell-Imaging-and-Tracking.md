# Cell Tracking

<p align="center">
  <img width="90%" src="./../assets/Tracking_Vis.png" alt="Tracking Visualisation">
</p>

## Download slides (Optional)

All the slides that will be used in this session are [here](https://www.dropbox.com/scl/fi/w2o09kpr3drn4xgf5pbyq/Tracking.pptx?rlkey=d3d1tys47pt14f0i6jxb0htqz&dl=0).

## Download demo data

We're going to be working with some example datasets, which you can download from [here](https://www.dropbox.com/scl/fo/6k0erahv2y6yxa17p2vt2/AJEAOdiRSmFPHP3vF7t_6JI?rlkey=i74r1fqhht0avkys5t0wcyl2t&dl=0).

## Set up conda environment

For this module, you need to set up a conda environment to analyse tracking data in Jupyter notebooks.

1. Make sure you first installed conda properly by following [these instructions](./../Pages/Installation-Instructions.md#installing-conda).
2. Open Anaconda Prompt and type the following to create a new environment:
    ```
    conda create --name cell-tracking python=3.12
    ```
3. Check that the environment was created:
    ```
    conda env list
    ```
4. Activate your new environment so you can use it:
    ```
    conda activate cell-tracking
    ```
5. Install the necessary packages for this session:
    ```
    conda install matplotlib pandas numpy seaborn jupyter
    ```
6. Open Jupyter Notebook and check that the installed packages can be correctly imported.
    ```
    jupyter notebook
    ```
    When Jupyter notebook opens in the web browser, open a new notebook with File/New/Notebook
<p align="center">
  <img width="90%" src="./../assets/Jupyter_notebook_Open_new.png" alt="Tracking Visualisation">
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select a python kernel
<p align="center">
  <img width="90%" src="./../assets/Jupyter_notebook_Select_kernel.png" alt="Tracking Visualisation">
</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type in one cell

  ```
    import numpy as np
  ```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and run
<p align="center">
    <img width="90%" src="./../assets/Jupyter_notebook_Run_cell.png" alt="Tracking Visualisation">
</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If no error is found, it means that the package has been installed correctly.



For more information on using conda, see [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).

For a detailed explanation on Jupyter Notebook, visit the [Jupyter Notebook User Documentation](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html)
