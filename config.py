# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

from PyQt5.Qt import (Qt, QDialog, QFont, QIcon, QGridLayout, QGroupBox, QLabel, QMargins, QVBoxLayout, QWidget)

from calibre.utils.config import JSONConfig

from polyglot.builtins import unicode_type

S_FALSE = unicode_type("False")
S_TRUE = unicode_type("True")

# This is where all preferences for this plugin are stored
prefs = JSONConfig('plugins/Library Codes')

# Set defaults
prefs.defaults['DDC'] = unicode_type("#ddc")
prefs.defaults['LCC'] = unicode_type("#lcc")
prefs.defaults['FAST'] = unicode_type("#fast")
prefs.defaults['OCLC'] = unicode_type("#oclc_owi")
prefs.defaults['DDC_IS_ACTIVE'] = unicode_type(S_FALSE)
prefs.defaults['LCC_IS_ACTIVE'] = unicode_type(S_FALSE)
prefs.defaults['FAST_IS_ACTIVE'] = unicode_type(S_FALSE)
prefs.defaults['FAST_PREFIX'] = unicode_type("")  #deprecated--to be removed in the next release
prefs.defaults['OCLC_IS_ACTIVE'] = unicode_type(S_FALSE)
prefs.defaults['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)
prefs.defaults['EXTRA_AUTHOR_DETAILS'] = unicode_type('#lcead')
prefs.defaults['EXTRA_AUTHOR_DETAILS_IS_ACTIVE'] = unicode_type(S_TRUE)
prefs.defaults['EXTRA_AUTHOR_DETAILS_PREFIX'] = unicode_type("")  #deprecated--to be removed in the next release
prefs.defaults['GENRE'] = unicode_type("#lc_genre")
prefs.defaults['GENRE_DDC_IS_ACTIVE'] = unicode_type(S_FALSE)
prefs.defaults['GENRE_LCC_IS_ACTIVE'] = unicode_type(S_FALSE)
prefs.defaults['GENRE_IS_INACTIVE'] = unicode_type(S_TRUE)
prefs.defaults['GENRE_EXACT_MATCH'] = unicode_type(S_TRUE)
prefs.defaults['GENRE_LCC_MATCH_LENGTH'] = 2

class ConfigWidget(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.layout_1 = QVBoxLayout()
        self.setLayout(self.layout_1)

        self.layout_1.setSpacing(0)
        self.layout_1.setContentsMargins(QMargins(0,0,0,0));

        self.paths_groupbox = QGroupBox('Preferences')
        self.layout_1.addWidget(self.paths_groupbox)

        self.paths_layout = QGridLayout()
        self.paths_groupbox.setLayout(self.paths_layout)

        font = QFont()

        font.setBold(False)
        font.setPointSize(10)

        self.label1 = QLabel()
        self.label1.setTextFormat(1)
        self.label1.setText("<center><font color='#0404B4'>               Please Customize Directly Within Library Codes             </font></center>")
        self.label1.setFont(font)
        self.paths_layout.addWidget(self.label1)

        self.resize(self.sizeHint())

    def save_settings(self):
        return
    def validate(self):
        return False
#END of config.py

