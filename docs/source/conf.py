# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import revitron_sphinx_theme
sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../revitron'))

master_doc = 'index'

# -- Project information -----------------------------------------------------

project = 'Revitron'
copyright = '2020, Marc Anton Dahmen'
author = 'Marc Anton Dahmen'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

autodoc_mock_imports = ['pyrevit', 'Autodesk', 'clr', 'System', 'Microsoft']

napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['modules.rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

html_theme = 'revitron_sphinx_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
    'github_url': 'https://github.com/revitron/revitron',
    'opengraph_image': 'revitron.png',
    'base_url': 'https://revitron.readthedocs.io/en/latest'
}

html_logo = '_static/revitron.svg'

html_sidebars = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = []

html_js_files = []