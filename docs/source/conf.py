# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Build & Publish Tutorials Using Jupyter Notebooks, MyST, and Sphinx'
copyright = '2024, Nyki Anderson'
author = 'Nyki Anderson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "colon_fence",
    "sphinx-copybutton",
    "sphinx-autobuild",
    "sphinx-last-updated-by-git",
    "enable-checkboxes",
    "dollarmath",
    "deflist",
    "smartquotes",
    "attrs_inline",
    "sphinx.ext.githubpages"
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

templates_path = ['_templates']
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store'
]

jupyter_execute_notebooks = "cache"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'renku'
html_static_path = ['static']
