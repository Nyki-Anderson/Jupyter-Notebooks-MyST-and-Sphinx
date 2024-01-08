# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Using Jupyter Notebooks, MyST Markdown, & Sphinx to Publish Professional Quality HTML & LaTeX Documents'
copyright = '2024, N. L. Dentinger-Anderson, C. L. Dentinger-Valentine'
author = 'N. L. Dentinger-Anderson, C. L. Dentinger-Valentine'
version = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "jupyter_sphinx",
    "myst_nb"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [
    '_templates'
]

# The suffix(es) of source filenames.
source_suffix = [
    '.ipynb',
    '.md',
    '.rst' 
]

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'lib'
]

# The name of hte Pygments (syntax highlighting) style to use.
pygements_style = 'style.StarofficeStyle'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_pdj_theme'
html_static_path = []
# html_logo = 'path/to/logo.svg'
# html_favicon = 'path/to/favicon.ico'
html_theme_options = {}

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt',
}