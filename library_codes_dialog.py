# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import (Qt, QDialog, QFileDialog, QObject, QApplication,
                                        QLabel, QWidget, QPushButton, QSpinBox,
                                        QGridLayout, QTabWidget, QVBoxLayout, QScrollArea, QLayout,
                                        QPalette, QColor, QMargins, QSize, QSizePolicy,
                                        QIcon, QGroupBox, QSpacerItem, QLineEdit, QDialogButtonBox, QProgressBar,
                                        QCheckBox, QButtonGroup, QToolTip, QFont)
import os,sys
import apsw
import codecs
import collections
from contextlib import contextmanager
from copy import deepcopy
import datetime
from datetime import datetime
from functools import partial
import re
import time
from time import sleep
import unicodedata

from calibre import isbytestring, force_unicode, prints
from calibre.constants import filesystem_encoding, DEBUG, iswindows
from calibre.gui2 import error_dialog, info_dialog, gprefs
from calibre.utils.config import JSONConfig

from polyglot.builtins import as_unicode, iteritems, unicode_type

from calibre_plugins.library_codes.config import prefs
from calibre_plugins.library_codes.config import ConfigWidget
from calibre_plugins.library_codes.lc_cli import lc_cli_add_custom_column, send_rc_message

S_FALSE = "False"
S_TRUE = "True"

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
class SizePersistedDialog(QDialog):
    initial_extra_size = QSize(10, 10)

    def __init__(self, parent, unique_pref_name):
        QDialog.__init__(self, parent)
        self.unique_pref_name = unique_pref_name
        self.geom = gprefs.get(unique_pref_name, None)

    def resize_dialog(self):
        if self.geom is None:
            self.resize(self.sizeHint()+self.initial_extra_size)
        else:
            self.restoreGeometry(self.geom)

    def save_dialog_geometry(self):
        geom = bytearray(self.saveGeometry())
        gprefs[self.unique_pref_name] = geom
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
class LibraryCodesDialog(SizePersistedDialog):
    #-----------------------------------------------------------------------------------------
    def __init__(self,gui,icon,guidb,plugin_path,ui_exit,action_type):
        parent = gui
        unique_pref_name = 'library_codes:gui_parameters_dialog'
        SizePersistedDialog.__init__(self, parent, unique_pref_name)
        #-----------------------------------------------------
        self.gui = gui
        self.guidb = guidb
        #-----------------------------------------------------
        self.icon = icon
        #-----------------------------------------------------
        self.plugin_path = plugin_path
        #-----------------------------------------------------
        self.ui_exit = ui_exit
        #-----------------------------------------------------
        self.action_type = action_type
        #-----------------------------------------------------
        self.myparentprefs = collections.OrderedDict([])
        prefsdefaults = deepcopy(prefs.defaults)
        tmp_list = []
        #~ for k,v in prefs.iteritems():
        for k,v in iteritems(prefs):
            tmp_list.append(k)
        #END FOR
        #~ for k,v in prefsdefaults.iteritems():
        for k,v in iteritems(prefsdefaults):
            tmp_list.append(k)
        #END FOR
        tmp_set = set(tmp_list)
        tmp_list = list(tmp_set)  #no duplicates
        del tmp_set
        tmp_list.sort()
        for k in tmp_list:
            self.myparentprefs[k] = " "  # ordered by key
        #END FOR
        del tmp_list
        #~ for k,v in prefs.iteritems():
        for k,v in iteritems(prefs):
            self.myparentprefs[k] = v
        #END FOR
        #~ for k,v in prefsdefaults.iteritems():
        for k,v in iteritems(prefsdefaults):
            if not k in prefs:
                prefs[k] = v
            else:
                if not prefs[k] > " ":
                    prefs[k] = v
            if not k in self.myparentprefs:
                self.myparentprefs[k] = v
            else:
                if not self.myparentprefs[k] > " ":
                    self.myparentprefs[k] = v
        #END FOR
        #~ for k,v in self.myparentprefs.iteritems():
        for k,v in iteritems(self.myparentprefs):
            prefs[k] = v
        #END FOR
        prefs  #prefs now synched
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.param_dict = collections.OrderedDict([])
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.init_tooltips_for_parent()
        self.setToolTip(self.parent_tooltip)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        # Tab 0: LibraryCodesTab
        #-----------------------------------------------------
        #-----------------------------------------------------
        from calibre_plugins.library_codes.library_codes_dialog import LibraryCodesTab
        self.LibraryCodesTab = LibraryCodesTab(self.gui,self.guidb,self.myparentprefs,self.param_dict,self.ui_exit,self.save_dialog_geometry)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #    Parent             LibraryCodesDialog
        #-----------------------------------------------------
        font = QFont()
        font.setBold(False)
        font.setPointSize(10)

        tablabel_font = QFont()
        tablabel_font.setBold(False)
        tablabel_font.setPointSize(10)

        #-----------------------------------------------------
        self.setWindowTitle('Library Codes')
        self.setWindowIcon(icon)
        #-----------------------------------------------------
        self.layout_frame = QVBoxLayout()
        self.layout_frame.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout_frame)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        n_width = 600

        self.LCtabWidget = QTabWidget()
        self.LCtabWidget.setMaximumWidth(n_width)
        self.LCtabWidget.setFont(tablabel_font)

        self.LCtabWidget.addTab(self.LibraryCodesTab,"Derivation from ISBN or ISSN or Author/Title")
        self.LibraryCodesTab.setToolTip("<p style='white-space:wrap'>Derive Library Codes DDC and/or LCC and/or OCLC-OWI from ISBN or ISSN or Author/Title.  Visit: http://classify.oclc.org/classify2/ ")
        self.LibraryCodesTab.setMaximumWidth(n_width)

           #-----------------------------------------------------
        self.layout_frame.addWidget(self.LCtabWidget)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.resize_dialog()      # inherited from SizePersistedDialog
        #-----------------------------------------------------
        self.LCtabWidget.setCurrentIndex(0)
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    # OTHER
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def init_tooltips_for_parent(self):
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        self.parent_tooltip = "<p style='white-space:wrap'>" + \
        '''
            "The 'User Guide' is comprised of the sum of all of the 'ToolTips' and messages.<br><br> If you wish to manually determine any Library Codes, simply visit: http://classify.oclc.org/classify2/"
        '''
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
class LibraryCodesTab(QWidget):
    def __init__(self,mygui,myguidb,mymainprefs,myparam_dict,myuiexit,mysavedialoggeometry):
        super(LibraryCodesTab, self).__init__()
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.gui = mygui
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.guidb = myguidb
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.lib_path = self.gui.library_view.model().db.library_path
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.mytabprefs = mymainprefs
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.param_dict = myparam_dict
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.ui_exit = myuiexit
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.save_dialog_geometry = mysavedialoggeometry
        #-----------------------------------------------------
        #-----------------------------------------------------
        font = QFont()
        font.setBold(False)
        font.setPointSize(10)
        #-----------------------------------------------------
        self.layout_top = QVBoxLayout()
        self.layout_top.setSpacing(0)
        self.layout_top.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout_top)
        #-----------------------------------------------------
        self.scroll_area_frame = QScrollArea()
        self.scroll_area_frame.setAlignment(Qt.AlignLeft)
        self.scroll_area_frame.setWidgetResizable(True)
        self.scroll_area_frame.ensureVisible(400,400)

        self.layout_top.addWidget(self.scroll_area_frame)       # the scroll area is now the child of the parent of self.layout_top

        # NOTE: the self.scroll_area_frame.setWidget(self.scroll_widget) is at the end of the init() AFTER all children have been created and assigned to a layout...

        #-----------------------------------------------------
        self.scroll_widget = QWidget()
        self.layout_top.addWidget(self.scroll_widget)           # causes automatic reparenting of QWidget to the parent of self.layout_top, which is:  self .
        #-----------------------------------------------------
        self.layout_frame = QVBoxLayout()
        self.layout_frame.setSpacing(0)
        self.layout_frame.setAlignment(Qt.AlignLeft)

        self.scroll_widget.setLayout(self.layout_frame)        # causes automatic reparenting of any widget later added to self.layout_frame to the parent of self.layout_frame, which is:  QWidget .

        #-----------------------------------------------------
        self.lc_groupbox = QGroupBox('Settings:')
        self.lc_groupbox.setMaximumWidth(400)
        self.lc_groupbox.setToolTip("<p style='white-space:wrap'>The settings that control 'Library Codes'.  Using only ISBN or ISSN or Author/Title, Library Codes for selected books will be derived using the Current Settings.")
        self.layout_frame.addWidget(self.lc_groupbox)

        self.lc_layout = QGridLayout()
        self.lc_groupbox.setLayout(self.lc_layout)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.spacing0 = QLabel()
        self.layout_frame.addWidget(self.spacing0)
        self.spacing0.setMaximumHeight(20)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.button_box = QDialogButtonBox()
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setCenterButtons(True)

        self.layout_frame.addWidget(self.button_box)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.push_button_save_only = QPushButton("Save")
        self.push_button_save_only.clicked.connect(self.save_settings)
        self.push_button_save_only.setDefault(True)
        self.push_button_save_only.setFont(font)
        self.push_button_save_only.setToolTip("<p style='white-space:wrap'>Save all user settings.")
        self.button_box.addButton(self.push_button_save_only,0)

        self.push_button_exit_only = QPushButton("Exit")
        self.push_button_exit_only.clicked.connect(self.exit_only)
        self.push_button_exit_only.setDefault(False)
        self.push_button_exit_only.setFont(font)
        self.push_button_exit_only.setToolTip("<p style='white-space:wrap'>Exit immediately without saving anything.")
        self.button_box.addButton(self.push_button_exit_only,0)
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------

        r = 4

        self.ddc_labelname = QLineEdit(self)
        self.ddc_labelname.setText(self.mytabprefs['DDC'])
        self.ddc_labelname.setFont(font)
        self.ddc_labelname.setToolTip("<p style='white-space:wrap'>Custom Column Search/Lookup #name for DDC.<br><br>See:  https://www.oclc.org/dewey/features/summaries.en.html")
        self.ddc_labelname.setMaximumWidth(100)
        self.lc_layout.addWidget(self.ddc_labelname,r,0)

        self.ddc_activate_checkbox = QCheckBox("Activate 'Dewey Decimal Code' Classification?")
        self.ddc_activate_checkbox.setToolTip("<p style='white-space:wrap'>Do you want to derive DDC?")
        r = r+1
        self.lc_layout.addWidget(self.ddc_activate_checkbox,r,0)
        if prefs['DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.ddc_activate_checkbox.setChecked(True)
        else:
            self.ddc_activate_checkbox.setChecked(False)
        #-----------------------------------------------------
        self.spacing1 = QLabel()
        r = r+1
        self.lc_layout.addWidget(self.spacing1,r,0)
        self.spacing1.setMaximumHeight(10)
        #-----------------------------------------------------
        self.lcc_labelname = QLineEdit(self)
        self.lcc_labelname.setText(self.mytabprefs['LCC'])
        self.lcc_labelname.setFont(font)
        self.lcc_labelname.setToolTip("<p style='white-space:wrap'>Custom Column Search/Lookup #name for LCC.<br><br>See: http://www.loc.gov/catdir/cpso/lcco/ ")
        self.lcc_labelname.setMaximumWidth(100)
        r = r+4
        self.lc_layout.addWidget(self.lcc_labelname,r,0)

        self.lcc_activate_checkbox = QCheckBox("Activate 'Library of Congress Code' Classification?")
        self.lcc_activate_checkbox.setToolTip("<p style='white-space:wrap'>Do you want to derive LCC?")
        r = r+1
        self.lc_layout.addWidget(self.lcc_activate_checkbox,r,0)
        if prefs['LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.lcc_activate_checkbox.setChecked(True)
        else:
            self.lcc_activate_checkbox.setChecked(False)
        #-----------------------------------------------------
        self.spacing2 = QLabel("")
        r = r+1
        self.lc_layout.addWidget(self.spacing2,r,0)
        self.spacing2.setMaximumHeight(10)
        #-----------------------------------------------------

        self.fast_labelname = QLineEdit(self)
        self.fast_labelname.setText(self.mytabprefs['FAST'])
        self.fast_labelname.setFont(font)
        self.fast_labelname.setToolTip("<p style='white-space:wrap'>Custom Column Search/Lookup #name for FAST Tag Values. ")
        self.fast_labelname.setMinimumWidth(100)
        self.fast_labelname.setMaximumWidth(100)
        r = r+4
        self.lc_layout.addWidget(self.fast_labelname,r,0)

        self.fast_activate_checkbox = QCheckBox("Activate 'FAST' Tags?")
        self.fast_activate_checkbox.setToolTip("<p style='white-space:wrap'>Do you want to derive FAST Tags?\
                                                                                                                    <br><br>Text.  Behaves like Tags. Not Names.<br><br>")
        r = r+1
        self.lc_layout.addWidget(self.fast_activate_checkbox,r,0)
        if prefs['FAST_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.fast_activate_checkbox.setChecked(True)
        else:
            self.fast_activate_checkbox.setChecked(False)

        #-----------------------------------------------------
        self.spacing6 = QLabel("")
        r = r+1
        self.lc_layout.addWidget(self.spacing6,r,0)
        self.spacing6.setMaximumHeight(10)
        #-----------------------------------------------------

        self.oclc_labelname = QLineEdit(self)
        self.oclc_labelname.setText(self.mytabprefs['OCLC'])
        self.oclc_labelname.setFont(font)
        self.oclc_labelname.setToolTip("<p style='white-space:wrap'>Custom Column Search/Lookup #name for OCLC-OWI.<br><br>See: #http://classify.oclc.org/classify2/   ")
        self.oclc_labelname.setMaximumWidth(100)
        r = r+4
        self.lc_layout.addWidget(self.oclc_labelname,r,0)

        self.oclc_activate_checkbox = QCheckBox("Activate 'Online Computer Library Center' Work ID Code?")
        self.oclc_activate_checkbox.setToolTip("<p style='white-space:wrap'>Do you want to derive OCLC-OWI?")
        r = r+1
        self.lc_layout.addWidget(self.oclc_activate_checkbox,r,0)
        if self.mytabprefs['OCLC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.oclc_activate_checkbox.setChecked(True)
        else:
            self.oclc_activate_checkbox.setChecked(False)
        #-----------------------------------------------------
        self.spacing5 = QLabel("")
        r = r+1
        self.lc_layout.addWidget(self.spacing5,r,0)
        self.spacing5.setMaximumHeight(10)
        #-----------------------------------------------------
        self.lc_author_details_labelname = QLineEdit(self)
        self.lc_author_details_labelname.setText(self.mytabprefs['EXTRA_AUTHOR_DETAILS'])
        self.lc_author_details_labelname.setFont(font)
        self.lc_author_details_labelname.setToolTip("<p style='white-space:wrap'>Custom Column Search/Lookup #name for 'LC Extra Author Details'.\
                                                                                                                              <br><br>Text.  Behaves like Tags. Not Names.<br><br>")
        self.lc_author_details_labelname.setMaximumWidth(100)
        r = r+4
        self.lc_layout.addWidget(self.lc_author_details_labelname,r,0)


        self.lc_author_details_checkbox = QCheckBox("Activate 'Library Codes Extra Author Details'?")
        self.lc_author_details_checkbox.setToolTip("<p style='white-space:wrap'>Do you want to add (never delete or replace) any available Tag-like values to this Custom Column if they are associated with the OCLC-OWI Identifier?")
        r = r+1
        self.lc_layout.addWidget(self.lc_author_details_checkbox,r,0)
        if self.mytabprefs['EXTRA_AUTHOR_DETAILS_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.lc_author_details_checkbox.setChecked(True)
        else:
            self.lc_author_details_checkbox.setChecked(False)
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.spacing4 = QLabel()
        r = r+1
        self.lc_layout.addWidget(self.spacing4,r,0)
        self.spacing4.setMaximumHeight(10)
        #-----------------------------------------------------
        font.setBold(False)
        font.setPointSize(7)
        #-----------------------------------------------------
        self.push_button_autoadd_custom_columns = QPushButton("Automatically Add Activated Custom Columns?")
        self.push_button_autoadd_custom_columns.clicked.connect(self.autoadd_custom_columns)
        self.push_button_autoadd_custom_columns.setDefault(False)
        self.push_button_autoadd_custom_columns.setFont(font)
        self.push_button_autoadd_custom_columns.setToolTip("<p style='white-space:wrap'>Do you want to automatically add the Custom Columns selected above?<br><br>If you have any issues, please add them manually.")
        r = r+4
        self.lc_layout.addWidget(self.push_button_autoadd_custom_columns,r,0)
        self.push_button_autoadd_custom_columns.setMaximumWidth(250)
        #-----------------------------------------------------
        self.lc_custom_columns_generation_label = QLabel()
        r = r+1
        self.lc_layout.addWidget(self.lc_custom_columns_generation_label,r,0)
        self.lc_custom_columns_generation_label.setText("                                                              ")
        self.lc_custom_columns_generation_label.setMaximumHeight(10)
        self.lc_custom_columns_generation_label.setFont(font)

        self.oclc_identifier_only_checkbox = QCheckBox("Always Create OCLC-OWI as an 'Identifier' (à la ISBN)?")
        self.oclc_identifier_only_checkbox.setToolTip("<p style='white-space:wrap'>Do you want to update Calibre's Identifiers for an Identifier of 'OCLC-OWI',\
                                                                                                                                 regardless of whether you want its own Custom Column updated?\
                                                                                                                                <br><br>REQUIRED to derive DDC/LCC using Author/Title.")
        r = r+2
        self.lc_layout.addWidget(self.oclc_identifier_only_checkbox,r,0)
        if prefs['OCLC_IDENTIFIER'] == unicode_type(S_TRUE):
            self.oclc_identifier_only_checkbox.setChecked(True)
        else:
            self.oclc_identifier_only_checkbox.setChecked(False)

        #-----------------------------------------------------
        self.spacing3 = QLabel("")
        r = r+1
        self.lc_layout.addWidget(self.spacing3,r,0)
        self.spacing3.setMaximumHeight(10)
        #-----------------------------------------------------
        font.setBold(False)
        font.setPointSize(10)
        #-----------------------------------------------------
        self.lc_genre_labelname = QLineEdit(self)
        self.lc_genre_labelname.setText(self.mytabprefs['GENRE'])
        self.lc_genre_labelname.setFont(font)
        self.lc_genre_labelname.setToolTip("<p style='white-space:wrap'>Custom Column Search/Lookup #name for 'Genre'.\
                                                                                                                              <br><br>Text.  Behaves like Tags.<br><br>")
        self.lc_genre_labelname.setMaximumWidth(100)
        r = r+1
        self.lc_layout.addWidget(self.lc_genre_labelname,r,0)

        self.lc_checkbox_buttongroup = QButtonGroup()
        self.lc_checkbox_buttongroup.setExclusive(True)

        self.lc_genre_ddc_checkbox = QCheckBox("Update 'Genre' using DDC-to-Genre Mappings?")
        self.lc_genre_ddc_checkbox.setToolTip("<p style='white-space:wrap'>Do you want LC to update 'Genre' using the DDC-to-Genre mapping in Table _lc_genre_mapping?")
        r = r+1
        self.lc_layout.addWidget(self.lc_genre_ddc_checkbox,r,0)

        self.lc_genre_lcc_checkbox = QCheckBox("Update 'Genre' using LCC-to-Genre Mappings?")
        self.lc_genre_lcc_checkbox.setToolTip("<p style='white-space:wrap'>Do you want LC to update 'Genre' using the LCC-to-Genre mapping in Table _lc_genre_mapping?")
        r = r+1
        self.lc_layout.addWidget(self.lc_genre_lcc_checkbox,r,0)

        self.lc_genre_inactive_checkbox = QCheckBox("Do not update 'Genre' at all")
        self.lc_genre_inactive_checkbox.setToolTip("<p style='white-space:wrap'>Do no 'Genre' processing at all?")
        r = r+1
        self.lc_layout.addWidget(self.lc_genre_inactive_checkbox,r,0)

        self.lc_checkbox_buttongroup.addButton(self.lc_genre_ddc_checkbox)
        self.lc_checkbox_buttongroup.addButton(self.lc_genre_lcc_checkbox)
        self.lc_checkbox_buttongroup.addButton(self.lc_genre_inactive_checkbox)

        if self.mytabprefs['GENRE_DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.lc_genre_ddc_checkbox.setChecked(True)
        elif self.mytabprefs['GENRE_LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.lc_genre_lcc_checkbox.setChecked(True)
        elif self.mytabprefs['GENRE_IS_INACTIVE'] == unicode_type(S_TRUE):
            self.lc_genre_inactive_checkbox.setChecked(True)

        self.lc_exact_match_checkbox = QCheckBox("DDC: Require an 'Exact Match', not a 'Best Match'?")
        self.lc_exact_match_checkbox.setToolTip("<p style='white-space:wrap'>Check this checkbox if you want an exact DDC match to be required in Table _lc_genre_mapping.  Otherwise, a 'best match' will be used via progressive shortening from right to left, but not past any decimal point.  If there is no decimal point in a book's DDC, then no progressive shortening will be performed at all.")
        r = r+1
        self.lc_layout.addWidget(self.lc_exact_match_checkbox,r,0)

        if self.mytabprefs['GENRE_EXACT_MATCH'] == unicode_type(S_TRUE):
            self.lc_exact_match_checkbox.setChecked(True)

        self.spin_lcc = QSpinBox(self)
        self.spin_lcc.setMinimum(1)
        self.spin_lcc.setMaximum(50)
        self.spin_lcc.setProperty('value',prefs['GENRE_LCC_MATCH_LENGTH'])
        self.spin_lcc.setMaximumWidth(250)
        self.spin_lcc.setSuffix("    LCC: Maximum Length to Match")
        self.spin_lcc.setToolTip("<p style='white-space:nowrap'>Maximum number of characters in the LCC that should be used to map to the 'Genre', starting from the left.  A maximum of 1 guarantees a (broad) match.\
                                                                                                   <br><br>LCCs are structured with either 1 or 2 beginning letters, so 2-character LCCs have special matching logic.\
                                                                                                   <br><br>Example:   Assume maximum = 2 for a LCC of 'Q1':  Q1 would be attempted.  If it failed, because the 2nd digit is a number, 'Q' would be attempted.\
                                                                                                   <br><br>Example:   Assume maximum = 2 for a LCC of 'PN1969.C65':  PN would be attempted.  If it failed, nothing else would be attempted.\
                                                                                                   <br><br>Example:   Assume maximum = 4 for a LCC of 'PN1969.C65':  PN19 would be attempted.  If it failed, nothing else would be attempted.\
                                                                                                   <br><br>Example:   Assume maximum = 4 for a LCC of 'Q1':  Q1 would be attempted.  If it failed, because the 2nd digit is a number, 'Q' would be attempted.\
                                                                                                   <br><br>Example:   Assume maximum = 4 for a LCC of 'Q389':  Q389 would be attempted.  If it failed, nothing else would be attempted.")
        r = r+2
        self.lc_layout.addWidget(self.spin_lcc,r,0)

        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.scroll_widget.resize(self.sizeHint())
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.scroll_area_frame.setWidget(self.scroll_widget)    # now that all widgets have been created and assigned to a layout...
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.scroll_area_frame.resize(self.sizeHint())
        #-----------------------------------------------------
        #-----------------------------------------------------
        self.resize(self.sizeHint())
    #-----------------------------------------------------------------------------------------
    def validate(self):
        return True
    #-----------------------------------------------------------------------------------------
    def autoadd_custom_columns(self):
        number_active = self.save_settings()
        if number_active == 0:
            return error_dialog(self.gui, _('Automatically Add Custom Columns'),_('No Activated Library Codes Custom Columns Found.  Nothing to Add.'), show=True)
        self.cli_param_list = self.create_cli_parameters()
        is_valid,restart_required = self.create_new_lc_custom_columns(self.cli_param_list)
        if is_valid:
            if restart_required:
                self.lc_custom_columns_generation_label.setText("Addition of Custom Columns Complete.  Restart Calibre Now.")
                self.repaint()
                info_dialog(self.gui, 'Automatically Add Custom Columns','All Selected Custom Customs Were Added If They Did Not Already Exist.  Please Restart Calibre now.').show()
            else:
                self.lc_custom_columns_generation_label.setText("Selected Custom Columns Already Exist.  Nothing Done.")
                self.repaint()
        else:
            self.lc_custom_columns_generation_label.setText("Not Completed.  Please Restart Calibre, then Add Manually.")
            self.repaint()
            msg = "Fatal error experienced in adding new Custom Columns."
            error_dialog(self.gui, _('Automatically Add Custom Columns'),_(msg), show=True)
    #-----------------------------------------------------------------------------------------
    def create_cli_parameters(self):

        try:
            del self.cli_param_list
        except:
            pass

        self.cli_param_list = []
        temp_list = []
        cc_taglike_list = []
        cc_fast_name = ""

        if self.mytabprefs['DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            cc = self.mytabprefs['DDC']
            if cc > '#':
                cc = cc.replace('#',"").strip()
                cc = unicode_type(cc)
                temp_list.append(cc)
            else:
                error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Illogical DDC Settings.  Please Correct.'), show=True)
                return self.cli_param_list


        if self.mytabprefs['LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
            cc = self.mytabprefs['LCC']
            if cc > '#':
                cc = cc.replace('#',"").strip()
                cc = unicode_type(cc)
                temp_list.append(cc)
            else:
                error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Illogical LCC Settings.  Please Correct.'), show=True)
                return self.cli_param_list


        if self.mytabprefs['FAST_IS_ACTIVE'] == unicode_type(S_TRUE):
            cc = self.mytabprefs['FAST']
            if cc > '#':
                cc = cc.replace('#',"").strip()
                cc = unicode_type(cc)
                temp_list.append(cc)
                cc_taglike_list.append(cc)
                cc_fast_name = cc
            else:
                error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Illogical FAST Settings.  Please Correct.'), show=True)
                return self.cli_param_list


        if self.mytabprefs['OCLC_IS_ACTIVE'] == unicode_type(S_TRUE):
            cc = self.mytabprefs['OCLC']
            if cc > '#':
                cc = cc.replace('#',"").strip()
                cc = unicode_type(cc)
                temp_list.append(cc)
            else:
                error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Illogical OCLC Settings.  Please Correct.'), show=True)
                return self.cli_param_list


        if self.mytabprefs['EXTRA_AUTHOR_DETAILS_IS_ACTIVE'] == unicode_type(S_TRUE):
            cc = self.mytabprefs['EXTRA_AUTHOR_DETAILS']
            if cc > '#':
                cc = cc.replace('#',"").strip()
                cc = unicode_type(cc)
                temp_list.append(cc)
                cc_taglike_list.append(cc)
            else:
                error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Illogical LC Extra Author Details Settings.  Please Correct.'), show=True)
                return self.cli_param_list
        else:
            pass


        if len(temp_list) == 0:
            del temp_list
            error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Nothing to do.  Please Review Settings.'), show=True)
            return self.cli_param_list

        cc_to_add_list = []

        # for each cc currently set to active, create a parameter...but only if the cc does NOT already exist...
        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            error_dialog(self.gui, _('Automatically Add Custom Columns'),_('Database Connection Error.  Restart Calibre.'), show=True)
            return

        self.lc_custom_columns_generation_label.setText("...Adding Custom Columns...")
        self.repaint()

        mysql = "SELECT label,name FROM custom_columns"
        my_cursor.execute(mysql)
        tmp_rows = my_cursor.fetchall()
        if not tmp_rows:
            for cc in temp_list:
                cc_to_add_list.append(cc)
            #END FOR
        else:
            if len(tmp_rows) == 0:
                for cc in temp_list:
                    cc_to_add_list.append(cc)
                #END FOR
            else:
                for cc in temp_list:
                    label_already_exists = False
                    for row in tmp_rows:
                        label,name = row
                        if unicode_type(label) == unicode_type(cc):
                            label_already_exists = True
                            break
                        else:
                            continue
                    #END FOR
                    if not label_already_exists:
                        cc_to_add_list.append(cc)
                #END FOR
                del tmp_rows
                del temp_list

        if len(cc_to_add_list) == 0:
            return self.cli_param_list

        cc_to_add_list.sort()

        for label in cc_to_add_list:
            label = unicodedata.normalize('NFKD', label).encode('ascii','ignore')
            label = unicode_type(label)
            label = label.lower()
            name = label.upper()
            datatype = 'text'
            if label in cc_taglike_list:
                is_multiple = "--is-multiple"
                if label == cc_fast_name:
                    name = "FAST Tags"
                else:
                    name = '"LC Extra Author Details"'
                param = is_multiple + '|||' + label + '|||' + name + '|||' +  datatype
            else:
                param = label + '|||' + name + '|||' +  datatype
            param = param.replace("[LIBRARY]",self.lib_path)
            self.cli_param_list.append(param)
        #END FOR

        del cc_to_add_list

        return self.cli_param_list
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def apsw_connect_to_library(self):

        my_db = self.gui.library_view.model().db

        self.lib_path = my_db.library_path
        self.lib_path = self.lib_path.replace(os.sep, '/')
        if isbytestring(self.lib_path):
            self.lib_path = self.lib_path.decode(filesystem_encoding)

        path = my_db.library_path
        if isbytestring(path):
            path = path.decode(filesystem_encoding)
        path = path.replace(os.sep, '/')
        path = os.path.join(path, 'metadata.db')
        path = path.replace(os.sep, '/')

        if isbytestring(path):
            path = path.decode(filesystem_encoding)

        if path.endswith("/"):
            path = path[0:-1]

        if path.count("metadata.db") == 0:
            path = path + "/metadata.db"

        try:
            my_db =apsw.Connection(path)
            is_valid = True
        except Exception as e:
            if DEBUG: print("path to metadata.db is: ", path)
            if DEBUG: print("error: ", as_unicode(e))
            is_valid = False
            return None,None,is_valid

        my_cursor = my_db.cursor()

        mysql = "PRAGMA main.busy_timeout = 5000;"      #PRAGMA busy_timeout = milliseconds;
        my_cursor.execute(mysql)

        return my_db,my_cursor,is_valid
    #-----------------------------------------------------------------------------------------
    def exit_only(self):
        self.save_dialog_geometry()          #  inherited from SizePersistedDialog
        self.ui_exit()
    #-----------------------------------------------------------------------------------------
    def save_settings(self):

        self.save_dialog_geometry()          #  inherited from SizePersistedDialog

        self.mytabprefs['DDC'] = self.ddc_labelname.text()
        self.mytabprefs['LCC'] = self.lcc_labelname.text()
        self.mytabprefs['FAST'] = self.fast_labelname.text()
        self.mytabprefs['OCLC'] = self.oclc_labelname.text()

        self.mytabprefs['DDC_IS_ACTIVE'] = unicode_type(self.ddc_activate_checkbox.isChecked())
        self.mytabprefs['LCC_IS_ACTIVE'] = unicode_type(self.lcc_activate_checkbox.isChecked())
        self.mytabprefs['FAST_IS_ACTIVE'] = unicode_type(self.fast_activate_checkbox.isChecked())
        self.mytabprefs['OCLC_IS_ACTIVE'] = unicode_type(self.oclc_activate_checkbox.isChecked())
        self.mytabprefs['OCLC_IDENTIFIER'] = unicode_type(self.oclc_identifier_only_checkbox.isChecked())

        label = self.mytabprefs['DDC']
        label = unicode_type(label)
        label = unicodedata.normalize('NFKD', label).encode('ascii','ignore')
        label = label.lower().strip()
        if not label.startswith("#"):
            label = "#" + label
        if label == "#":
            label = ""
            self.ddc_activate_checkbox.setChecked(False)
        self.mytabprefs['DDC'] = unicode_type(label)


        label = self.mytabprefs['LCC']
        label = unicode_type(label)
        label = unicodedata.normalize('NFKD', label).encode('ascii','ignore')
        label = label.lower().strip()
        if not label.startswith("#"):
            label = "#" + label
        if label == "#":
            label = ""
            self.lcc_activate_checkbox.setChecked(False)
        self.mytabprefs['LCC'] = unicode_type(label)


        label = self.mytabprefs['FAST']
        label = unicode_type(label)
        label = unicodedata.normalize('NFKD', label).encode('ascii','ignore')
        label = label.lower().strip()
        if not label.startswith("#"):
            label = "#" + label
        if label == "#":
            label = ""
            self.fast_activate_checkbox.setChecked(False)
        self.mytabprefs['FAST'] = unicode_type(label)


        label = self.mytabprefs['OCLC']
        label = unicode_type(label)
        label = unicodedata.normalize('NFKD', label).encode('ascii','ignore')
        label = label.lower().strip()
        if not label.startswith("#"):
            label = "#" + label
        if label == "#":
            label = ""
            self.oclc_activate_checkbox.setChecked(False)
        self.mytabprefs['OCLC'] = unicode_type(label)

        if self.mytabprefs['DDC'] == unicode_type("") and self.mytabprefs['LCC'] == unicode_type("")  and self.mytabprefs['FAST'] == unicode_type("") and self.mytabprefs['OCLC'] == unicode_type("") :
            self.mytabprefs['DDC'] = unicode_type("#ddc")
            self.mytabprefs['LCC'] = unicode_type("#lcc")
            self.mytabprefs['FAST'] = unicode_type("#fast")
            self.mytabprefs['OCLC'] = unicode_type("#oclc_owi")
        else:
            if self.mytabprefs['DDC'] == unicode_type("") and  self.mytabprefs['LCC'] == unicode_type(""):
                self.oclc_identifier_only_checkbox.setChecked(False)
        #---------------------------------------

        s = unicode_type(self.lc_genre_labelname.text())
        s = s.strip()
        if  s.startswith("#") and len(s) > 1 :
            self.mytabprefs['GENRE'] = unicode_type(s)
            self.mytabprefs['GENRE_DDC_IS_ACTIVE'] = unicode_type(self.lc_genre_ddc_checkbox.isChecked())
            self.mytabprefs['GENRE_LCC_IS_ACTIVE'] = unicode_type(self.lc_genre_lcc_checkbox.isChecked())
            self.mytabprefs['GENRE_IS_INACTIVE'] = unicode_type(self.lc_genre_inactive_checkbox.isChecked())
            self.mytabprefs['GENRE_EXACT_MATCH'] = unicode_type(self.lc_exact_match_checkbox.isChecked())
            self.mytabprefs['GENRE_LCC_MATCH_LENGTH'] = self.spin_lcc.value()
        else:
            self.mytabprefs['GENRE'] = unicode_type("#genre")
            self.lc_genre_labelname.setText(unicode_type("#genre"))
            self.lc_genre_ddc_checkbox.setChecked(False)
            self.lc_genre_lcc_checkbox.setChecked(False)
            self.lc_genre_inactive_checkbox.setChecked(True)
            self.mytabprefs['GENRE_DDC_IS_ACTIVE'] = unicode_type(S_FALSE)
            self.mytabprefs['GENRE_LCC_IS_ACTIVE'] = unicode_type(S_FALSE)
            self.mytabprefs['GENRE_IS_INACTIVE'] = unicode_type(S_TRUE)
            self.mytabprefs['GENRE_EXACT_MATCH'] = unicode_type(S_TRUE)
            self.mytabprefs['GENRE_LCC_MATCH_LENGTH'] = 2
            self.repaint()
            sleep(2)

        #---------------------------------------
        #~ for k,v in self.mytabprefs.iteritems():
        for k,v in iteritems(self.mytabprefs):
            v = unicode_type(v)
            v = v.strip()
            prefs[k] = v
        #END FOR
        prefs

        #---------------------------------------

        self.ddc_labelname.setText(self.mytabprefs['DDC'])
        self.lcc_labelname.setText(self.mytabprefs['LCC'])
        self.fast_labelname.setText(self.mytabprefs['FAST'])
        self.oclc_labelname.setText(self.mytabprefs['OCLC'])
        self.repaint()
        sleep(0)

        #~ for k,v in self.mytabprefs.iteritems():
        for k,v in iteritems(self.mytabprefs):
            self.param_dict[k] = v
        #END FOR

        number_active = 0

        if self.mytabprefs['DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1
        if self.mytabprefs['LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1
        if self.mytabprefs['FAST_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1
        if self.mytabprefs['OCLC_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1

        self.ddc_name = self.mytabprefs['DDC'].replace("#","").strip()
        self.lcc_name = self.mytabprefs['LCC'].replace("#","").strip()
        self.fast_name = self.mytabprefs['FAST'].replace("#","").strip()
        self.oclc_name = self.mytabprefs['OCLC'].replace("#","").strip()

        if self.oclc_identifier_only_checkbox.isChecked():
            self.oclc_identifier_is_desired = True
        else:
            self.oclc_identifier_is_desired = False

        return number_active
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def create_new_lc_custom_columns(self,execution_param_list):

        if len(self.cli_param_list) == 0:
            return True,False    # successful since the labels already exist; no restart is required.

        dbpath = self.lib_path

        was_successful = True
        restart_required = True

        for param in execution_param_list:
            try:
                lc_cli_add_custom_column(self.guidb,param, dbpath)
            except Exception as e:
                if DEBUG: print("Exception: ", as_unicode(e))
                was_successful = False
                break
        #END FOR

        return was_successful, restart_required
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
#END of library_codes_dialog.py