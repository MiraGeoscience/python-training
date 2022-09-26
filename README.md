# Mira Geoscience - Python Training

This repository contains tutorials to learn Python and the creation of custom applications with Geoscience ANALYST.

## Getting setup

Building and running the content of the tutorial requires some dependencies that can be installed with Conda.

- Install Conda for Python 3.8 or higher. Two recommended options:
    - [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links): ~400 MB of disk space
    - [Anaconda](https://www.anaconda.com/download/): ~3 GB of disk space
- Run the `setup.bat` provided. This will download and install all dependencies under the `python-training` environment.


## Generating HTML

The documentation relies on jupyter-book to generate HTML files for presentation. After editing any files under `training/`, run the following
- `conda activate mira-training`
- `jupyter-book build training/`

The content of the tutorial can then be viewed under `_build/html/index.html`

