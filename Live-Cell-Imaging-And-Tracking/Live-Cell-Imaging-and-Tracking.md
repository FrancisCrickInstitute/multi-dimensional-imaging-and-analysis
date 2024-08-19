# Cell Tracking

<p align="center">
  <img width="90%" src="./../assets/Tracking_Vis.png" alt="Tracking Visualisation">
</p>

For this module, you need to set up a conda environment to analyse tracking data in Jupyter notebooks.

1. Make sure you first installed conda properly by following [these instructions](./../Pages/Installation-Instructions.md#installing-conda).
2. Open Anaconda Prompt and type the following to create a new environment:
    ```
    conda create --name cell-tracking
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
    python -m pip install matplotlib pandas numpy seaborn jupyter
    ```

For more information on using conda, see [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).
