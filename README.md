# Mira Geoscience - Python Training

This repository contains tutorials to learn Python and the creation of custom applications with Geoscience ANALYST.

## Getting setup

Building and running the content of the tutorial requires some dependencies that can be installed with Conda.

- Install Conda for Python 3.8 or higher. Two recommended options:
    - [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links): ~400 MB of disk space
    - [Anaconda](https://www.anaconda.com/download/): ~3 GB of disk space
- Run the `setup.bat` provided. This will download and install all dependencies under the `python-training` environment.

**_NOTE:_** The assumption is made that Conda has been installed in one
   of the default directories:

    - %USERPROFILE%\\ana[mini]conda3\\
    - %LOCALAPPDATA%\\Continuum\\ana[mini]conda3\\
    - C:\\ProgramData\\ana[mini]conda3\\

   If Conda gets installed in a different directory, users will need to add/edit the
   ``get_custom_conda.bat`` file to add their custom path to the ``conda.bat`` file.

## Updating content

The official content that is versioned controlled and tested is stored as `py` files under `content/`.
Meanwhile, the web documentation and blank forms for training rely on jupyter-book (`ipynb`), and we therefore need to
synchronize the files. The script `devtools\update_tutorials.py` can do the update in both direction.

### Edits from jupyter-notebook
If edits are done in the jupyter-notebook, then `py` files can be updated with

- `conda activate mira-training`
- `python devtools\update_tutorials.py py`

### Generating HTML

 Before building the HTML, the notebook (`ipynb`) files must be updated. Run the following

- `conda activate mira-training`
- `python devtools\update_tutorials.py ipynb`
- `jupyter-book build training/`

The content of the tutorial can then be viewed under `_build/html/index.html`

### Generating blank forms

It is the plan to provide trainees with blank jupyter notebooks with only instructions. To generate those forms run

- `conda activate mira-training`
- `python devtools\update_tutorials.py forms`


#  Copyright (c) 2022 Mira Geoscience Ltd.
