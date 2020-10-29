# -*- coding: utf-8 -*-
import sys
import os


cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.insert(0, parent)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'haralyzer_3'
copyright = u'2020, Justin Crown & Cyb3r Jak3'


version = '1.8'
# The full version, including alpha/beta/rc tags.
release = '1.8.0'


exclude_patterns = ['_build', "tests"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

html_theme = 'default'


# Output file base name for HTML help builder.
htmlhelp_basename = 'haralyzer_3doc'


latex_documents = [
  ('index', 'haralyzer_3.tex', u'haralyzer_3 Documentation',
   u'Justin Crown & Cyb3r Jak3', 'manual'),
]


man_pages = [
    ('index', 'haralyzer_3', u'haralyzer_3 Documentation',
     [u'Justin Crown & Cyb3r Jak3'], 1)
]

texinfo_documents = [
  ('index', 'haralyzer_3', u'haralyzer_3 Documentation',
   u'Justin Crown & Cyb3r Jak3', 'haralyzer', 'One line description of project.',
   'Miscellaneous'),
]