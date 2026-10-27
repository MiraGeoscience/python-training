# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime
from importlib.metadata import version

from packaging.version import Version


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "python-training"

# The full version, including alpha/beta/rc tags.
release = version("python-training")
# drop the post segment if any for release
pep_version = Version(release)
if pep_version.is_postrelease:
    release = pep_version.base_version

# The short X.Y.Z version.
version = Version(release).base_version

project_copyright = "%Y, Mira Geoscience Ltd"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
templates_path = ["_templates"]
todo_include_todos = True


# -- Options for auto-doc ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc

autodoc_typehints = "signature"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_theme_options = {
    "description": f"version {release}",
}

# Enable numref
numfig = True


def get_copyright_notice():
    return f"Copyright {datetime.now().strftime(project_copyright)}"


rst_epilog = f"""
.. |copyright_notice| replace:: {get_copyright_notice()}.
"""
