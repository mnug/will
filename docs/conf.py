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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# before any changes, index.rst likely needs moving to root

#root_doc = "docs/index"


# -- Project information -----------------------------------------------------

project = "Basic Sphinx Example Project"
copyright = "2022, Read the Docs core team"
author = "Read the Docs core team"


# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# print("AAAAAAAAAAAAAAAAAAAAAAAAA")
# print("----------- ROOT")

# import os

# # Get the current directory
# current_directory = os.getcwd()

# # List all files in the current directory
# files = os.listdir(current_directory)

# # Print the list of files
# for file in files:
#     print(file)



# print("----------- BUILD")

# os.chdir("build")

# # Get the current directory
# current_directory = os.getcwd()

# # List all files in the 'build' directory
# files = os.listdir(current_directory)

# # Print the list of files
# for file in files:
#     print(file)

# print("----------- DOCS")

# os.chdir("../docs")

# # Get the current directory
# current_directory = os.getcwd()

# # List all files in the 'build' directory
# files = os.listdir(current_directory)

# # Print the list of files
# for file in files:
#     print(file)


# print("CCCCCCCCCCCC")



# print("--------- current directory")

# import os

# # Get the current directory
# current_directory = os.getcwd()

# # List all files in the current directory
# files = os.listdir(current_directory)

# # Print the list of files
# for file in files:
#     print(file)

# import shutil

# # Define the paths
# source_file = "index.rst"  # Path to the index.rst file
# destination_directory = "index.rst"  # Path to the destination directory

# # Move the file
# shutil.move(source_file, destination_directory)




# print("DDDDDDDDDDDD")
