# 3D Segmenation workshop

## Setting up conda environment

We will be using a yml file to setup our conda environment.  Yml files (Yet another Markup Language) files are a quick and easy way to share reproducible environments between image analysts. Remember
**REPRODUCIBILTY IS KEY IN IMAGE ANALYSIS**

We will be using the **Crick_IA.yml** file to create our segmentation conda installation. The file automatically installs StarDist and CellPose. We will also be using Jupyter Notebooks as our coding environment, so we need to set that up as well. 


Let's get started by installing the yml file first

  Open up the Anaconda Prompt and navigate to where the environment file (in this case, Crick_IA.yml) is
  Then, enter this command in the Anaconda prompt:
```
conda env create -f Crick_IA.yml
```

  Once the environment is created, we need to activate it

```
conda activate Crick_IA
```

  Now to install remote_ikernel, the kernel manager

```
pip install remote_ikernel
```

  Once the remote_ikernel is installed, we can link the kernel to jupyter notebooks easily using this command

```
python -m remote_ikernel manage --add --kernel_cmd="conda activate Crick_IA && ipython3 kernel -f {connection_file}" --name="Crick_IA" --interface=local --workdir="~/" --language=python3
```

  Now we can open jupyter notebook from the Anaconda prompt using this command:

```
jupyter notebook
```

  When Jupyter notebooks opens, open a new notebook, and try:

```
import stardist
import cellpose
```

    If these work, we're doing great!
