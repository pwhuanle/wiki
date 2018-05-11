import sys, os, subprocess
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer


project = u'Tron Protocol'
copyright = u'2017-2018, TRON Foundation'
master_doc = 'index'
templates_path = ['_templates']
extensions = []
source_suffix = '.rst'
version = '1.0'
exclude_patterns = ['_build']

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = False
html_sidebars = {
    '**': ['logo-text.html',
           'globaltoc.html',
           'localtoc.html',
           'searchbox.html']
}

import guzzle_sphinx_theme

extensions.append("guzzle_sphinx_theme")
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "https://tron.network/"
}

