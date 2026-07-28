# AGENTS.md

## Overview

This is a **workshop teaching repository** for the "Multi-Dimensional Imaging and Analysis" (MDIA) course at the Francis Crick Institute. It is **not a software project** — there are no build, test, lint, or deploy commands. The repo is structured as a GitHub Pages site (Jekyll) containing training materials: Jupyter notebooks, CellProfiler pipelines, ImageJ macros, sample data, and documentation.

## Repository structure

```
├── README.md              # Workshop landing page
├── _config.yml             # GitHub Pages / Jekyll config (theme: jekyll-theme-slate)
├── requirements.txt        # Base Python deps: matplotlib, pandas, numpy, seaborn, jupyter
├── assets/                 # Images used in README and module docs
├── Pages/
│   └── Installation-Instructions.md  # Software install guide (FIJI, QuPath, CellProfiler, conda)
├── Colocalization/         # Co-localisation module
│   ├── *.cppipe            # CellProfiler v5 pipelines (plain text, not JSON)
│   └── SplitChannels.ijm   # ImageJ macro (Bio-Formats required)
├── Live-Cell-Imaging-And-Tracking/  # Cell tracking module
│   ├── *.ipynb             # Jupyter notebooks for TrackMate data analysis
│   ├── tracking_requirements.txt    # Same as root requirements.txt
│   └── TrackMate_Outputs/  # Sample CSV data from TrackMate
├── 3D_Segmentation/        # 3D segmentation module
│   ├── *.ipynb             # Jupyter notebooks (watershed, StarDist, data analysis)
│   ├── calm-3dsegm.yml     # Conda environment spec (includes stardist, napari, tensorflow, scikit-image)
│   ├── conda_env_setup.md  # Conda environment setup instructions
│   └── *.tif               # Sample 2D and 3D microscopy images
└── OMERO/
    └── readme.md           # OMERO image database server links
```

## Key files and their purposes

### CellProfiler pipelines (`.cppipe`)
- Plain text format (not JSON/XML). CellProfiler v5 format.
- Each module starts with `[module_num:N|...]` and has key-value property lines.
- Do not reformat or restructure these files — CellProfiler expects the exact format.

### ImageJ macro (`SplitChannels.ijm`)
- Script parameter annotations (`#@`) use ImageJ's script parameter syntax.
- Requires the **Bio-Formats** plugin installed in FIJI.
- Recursively processes folders, splits multi-channel z-stacks into individual TIFF images.

### Jupyter notebooks (`.ipynb`)
- Designed for workshop participants to run interactively.
- **Live-Cell-Imaging-And-Tracking** notebooks (recommended order: `compare_track_data` → `compare_FUCCI_markers` → `plot_fluorescence_profiles`):
  - `compare_track_data.ipynb` — Simplest notebook. Reads TrackMate tracks CSV, plots a chosen metric (e.g. `TRACK_MEAN_SPEED`) across imaging positions with histogram and swarmplot.
  - `compare_FUCCI_markers.ipynb` — Most complex. Reads TrackMate spots CSV, uses sliding-window thresholding to detect intensity drops in Ch2 (G1 marker) and Ch3 (S/G2/M marker), then measures time between transitions.
  - `plot_fluorescence_profiles.ipynb` — Plots per-track Ch2/Ch3 intensity profiles over time for visual inspection of individual cell behaviour.
- **3D_Segmentation** notebooks:
  - `Watershed_3DSegmentation.ipynb` — Classical watershed segmentation with scikit-image and napari visualization.
  - `StarDist_Demo.ipynb` — Deep learning 3D nucleus segmentation using StarDist + TensorFlow.
  - `Data_Analysis.ipynb` — Post-segmentation analysis: regionprops, intensity measurements, CSV export.

### TrackMate CSV format
- Two-row headers: row 1 = long names, row 2 = short names, row 3 = units.
- Tracks CSV columns: `TRACK_INDEX`, `TRACK_ID`, `TRACK_MEAN_SPEED`, `TRACK_DURATION`, etc.
- Spots CSV contains per-spot fluorescence intensity data for FUCCI analysis.

### Conda environments
- **3D Segmentation**: `calm-3dsegm` environment from `calm-3dsegm.yml` (conda-forge channel, includes stardist, napari, tensorflow via pip).
- **Cell Tracking**: `cell-tracking` environment created manually with `python=3.13`, then pip installs from `tracking_requirements.txt`.

## Conventions and gotchas

- **No automated tooling**: No CI, no Makefile, no pre-commit hooks, no test framework. This is intentional — the repo is workshop materials, not code.
- **Jekyll site**: `_config.yml` uses `jekyll-theme-slate`. The repo is published as a GitHub Pages site. Markdown files use relative image paths (`./../assets/...`).
- **Dropbox links**: Several module READMEs reference Dropbox URLs for downloading slides and demo data. These are external and may expire or change.
- **Sample data files**: `.tif` and `.csv` files in the repo are real microscopy data (can be large). Do not delete or modify them unless explicitly asked.
- **Binder support**: The tracking module includes a Binder badge for running notebooks in the cloud. The binder URL references the `main` branch.
- **`.ipynb_checkpoints/`**: Present in `3D_Segmentation/` — these are Jupyter autosave files, not manual content.
- **Windows paths in docs**: Installation instructions reference Windows-style paths (`C:\users\...`) and Mac paths, reflecting the mixed-OS workshop audience.
- **File encoding**: `.cppipe` and `.ijm` files are plain ASCII/UTF-8. Notebooks are standard JSON.