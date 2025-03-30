# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Why Neovim"
copyright = "2025, Jiandong Qiu"
author = "Jiandong Qiu"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
    # "sphinx.ext.graphviz",
]

html_theme = "sphinx_rtd_theme"

locale_dirs = ["locale/"]
gettest_compact = False
gettext_uuid = True

language = "en"
