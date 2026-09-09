# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UGME'
copyright = '2026, Anthony J Dominic III'
author = 'Anthony J Dominic III'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'nbsphinx',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']
html_theme_options = {
    # Include sub-headers in sidebar TOC (default True)
    'includehidden': True,
    
    # Maximum depth of sidebar navigation tree
    'navigation_depth': 4,
    
    # Collapse unexpanded subtrees
    'collapse_navigation': True,
}
# html_theme_options = {
#     "bgcolor" : "#ecf39e",
#     "sidebarbgcolor" : "#4f772d",
# }
