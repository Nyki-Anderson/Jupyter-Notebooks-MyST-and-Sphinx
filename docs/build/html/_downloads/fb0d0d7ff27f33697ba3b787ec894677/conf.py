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
    "nbsphinx",
    "jupyter_sphinx",
    "myst_nb"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [
    '_templates'
]

# The suffix(es) of source filenames.
source_suffix = [
    '.rst',
    '.ipynb',
    '.myst',
    '.md'
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
pygements_style = 'style.NordStyle'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_pdj_theme'
html_static_path = ['./_static']
# html_logo = 'path/to/logo.svg'
html_favicon = './favicon.ico'
html_theme_options = {}

myst_html_meta = {
    "description lang=en": "The purpose of this project is to streamline the publishing process for professional-quality scientific reports, books, and documentation. For these purposes, we will be using Jupyter Notebook, MyST Markdown, and Sphinx Documentation. These tools will serve as the backbone to our metadata-rich content, bringing depth and accessibility to the final products (a static HTML site and accompanying PDF book).",
    "keywords": "Sphinx, MyST, Jupyter Notebook, HTML, PDF",
    "property=og:locale":  "en_US"
}

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt',
}