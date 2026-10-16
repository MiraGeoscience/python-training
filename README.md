# Mira Geoscience - Python Training

This repository contains tutorials to learn Python and the creation of custom applications with Geoscience ANALYST.

## Getting setup

Building and running the content of the tutorial requires some dependencies that can be installed with Conda.

- Install Conda for Python 3.12 or higher. We recommend to install **Conda** using [miniforge](https://github.com/conda-forge/miniforge).
- Run the `setup.bat` provided. This will download and install all dependencies under the `python-training` environment.

**_NOTE:_** The assumption is made that Conda has been installed in one
   of the default directories:

    - %USERPROFILE%\\miniforge\\
    - %LOCALAPPDATA%\\miniforge\\
    - C:\\ProgramData\\miniforge\\

   If Conda gets installed in a different directory, users will need to add/edit the
   ``get_custom_conda.bat`` file to add their custom path to the ``conda.bat`` file.

## Updating content

The official content that is versioned controlled and tested relies on jupyter-book (`ipynb`) files that are stored under `content/`.
Meanwhile, the blank notebooks used for training are stored under `./assets/training/`. The two versions can be synchronized with the script `devtools\update_tutorials.py`.

### Generating HTML

Run the following

- `conda activate python-training`
- `jupyter-book build content/`

The content of the tutorial can then be viewed under `_build/html/index.html`

### Generating blank forms

It is the plan to provide trainees with blank jupyter notebooks with only instructions. To generate those forms run

- `conda activate python-training`
- `python devtools\update_tutorials.py forms`


#  Copyright (c) 2026 Mira Geoscience Ltd.
