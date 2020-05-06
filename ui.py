# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.40"  # Python 3 compatibility & Calibre Version 3.41.3 pdftohtml compatibility

from PyQt5.Qt import QMenu, QDialog, QIcon, QAction, QSize, QWidget, QFileDialog, QApplication

import os, sys, subprocess
import apsw
import csv
from functools import partial
import re
import time
from time import sleep

from calibre import isbytestring, force_unicode, prints
from calibre.constants import filesystem_encoding, preferred_encoding, iswindows, DEBUG
from calibre.db.backend import DB
from calibre.db.cache import Cache as dbcache
from calibre.ebooks.metadata.meta import set_metadata
from calibre.ebooks.metadata.book.base import Metadata
from calibre.gui2 import error_dialog, info_dialog, question_dialog, FileDialog, __init__
from calibre.gui2.actions import InterfaceAction
from calibre.utils.config import config_dir, JSONConfig

from polyglot.builtins import as_bytes, as_unicode, iteritems, map, unicode_type

from calibre_plugins.library_codes.config import prefs
from calibre_plugins.library_codes.config import ConfigWidget
from calibre_plugins.library_codes.classify_web_service_api import oclc_classify_api
from calibre_plugins.library_codes.common_utils import set_plugin_icon_resources, get_icon, create_menu_action_unique
from calibre_plugins.library_codes.library_codes_dialog import LibraryCodesDialog
from calibre_plugins.library_codes.library_codes_webscraping_api import library_codes_generic_webscraping_api
from calibre_plugins.library_codes.library_codes_pdftohtml import pdftohtml_extract_pdf_issn

PLUGIN_ICONS = ['images/librarycodesicon.png','images/wrench-hammer.png','images/change.png','images/minus.png','images/plus.png','images/ddclccicon.png','images/swap.png','images/import.png','images/genre.png','images/piechart.png']

S_FALSE = "False"
S_TRUE = "True"

SOURCE_TYPE_VIAF = unicode_type("viaf_author_id")
SOURCE_TYPE_OCLC = unicode_type("www.worldcat.org/oclc")
SOURCE_TYPE_XID_OWI = unicode_type("xisbn.worldcat.org/webservices/xid/owi/")
SOURCE_TYPE_XID_OCLC = unicode_type("xisbn.worldcat.org/webservices/xid/oclcnum/")
SOURCE_TYPE_GOOGLE_BOOK_SEARCH = unicode_type("https://books.google.com/books?isbn=")

#--------------------------------------------------------------------------------------------
class ActionLibraryCodes(InterfaceAction):

    name = 'Library Codes'
    action_spec = ('LC','images/librarycodesicon.png', "Library Codes:  Derive Library of Congress Codes, Dewey Decimal Codes, and/or OCLC-OWI plus Other Identifiers for Selected Books Using ISBN or ISSN or Author/Title", None)
    action_type = 'global'
    accepts_drops = False
    auto_repeat = False
    priority = 9
    popup_type = 1

    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def genesis(self):

        icon_resources = self.load_resources(PLUGIN_ICONS)
        set_plugin_icon_resources(self.name, icon_resources )

        self.menu = QMenu(self.gui)

        self.build_menus(self.gui)

        # main icon
        self.qaction.setMenu(self.menu)
        self.qaction.setIcon(get_icon(PLUGIN_ICONS[0]))

        self.qaction.triggered.connect(self.derive_from_isbn_issn)
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def initialization_complete(self):

        self.guidb = self.gui.library_view.model().db

        self.selected_books_list = []

        must_save = False
        #~ for k,v in prefs.defaults.iteritems():
        for k,v in iteritems(prefs.defaults):
            if k in prefs:
                pass
            else:
                prefs[k] = v
                must_save = True
        #END FOR
        if must_save:
            prefs
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def library_changed(self,guidb):

        self.guidb = self.gui.library_view.model().db

        self.qaction.setIcon(get_icon(PLUGIN_ICONS[0]))

        try:
            self.librarycodesdialog.close()
        except:
            pass
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def build_menus(self,gui):

        lc_menu = self.menu
        lc_menu.clear()

        lc_menu.setTearOffEnabled(True)
        lc_menu.setWindowTitle('Library Codes Menu')

        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Configuration && ToolTip-Instructions', 'images/wrench-hammer.png',
                              triggered=partial(self.init_librarycodesdialog))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Using ISBN/ISSN:  Derive DDC/LCC/FAST/OCLC-OWI Custom Columns [Selected Books]', 'images/ddclccicon.png',
                              triggered=partial(self.derive_from_isbn_issn))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Using Author/Title:  Derive Incremental OCLC-OWI Identifiers [Selected Books]', 'images/plus.png',
                              triggered=partial(self.derive_incremental_oclc_owi_identifiers))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Using OCLC-OWI Identifier:  Derive DDC/LCC/FAST Custom Columns  [Selected Books]', 'images/ddclccicon.png',
                              triggered=partial(self.derive_from_oclc_owi))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, "Using OCLC-OWI Identifier:  Derive Incremental Identifier 'OCLC' then 'LOC_LCCN' [Selected Books]", 'images/plus.png',
                              triggered=partial(self.derive_incremental_identifiers))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, "Using OCLC-OWI Identifier:  Retrieve Incremental Tag-Like 'Extra Author Details' [Selected Books]", 'images/plus.png',
                              triggered=partial(self.retrieve_incremental_lcead_data))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Find Alternatives for a Non-Responsive ISBN [Selected Single Book]', 'images/swap.png',
                              triggered=partial(self.find_alternatives_for_nonresponsive_isbn))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Scrub ISBNs [Selected Books]', 'images/change.png',
                              triggered=partial(self.scrub_isbn))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Convert ISBN-10 to ISBN-13 [Selected Books]', 'images/change.png',
                              triggered=partial(self.scrub_isbns))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Delete All Non-Library Codes/ZMI/z* Identifiers [Selected Books]', 'images/minus.png',
                              triggered=partial(self.delete_non_lc_identifiers))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Extract ISSNs from Magazine/Periodical PDFs [Selected Books]', 'images/plus.png',
                              triggered=partial(self.extract_issn_from_pdf_control))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        #BEGIN submenu m1 --------------------------------------------------------------------------
        self.m1 = QMenu(_('[Menu] DDC/LCC to Genre Mapping'))
        self.m1_action = lc_menu.addMenu(self.m1)
        self.m1.setIcon(get_icon('images/genre.png'))

        self.m1.setTearOffEnabled(True)
        self.m1.setWindowTitle('DDC/LCC to Custom Column Mapping')

        self.m1.addSeparator()
        create_menu_action_unique(self, self.m1, 'Update Genre using Table _lc_genre_mapping [Selected Books]', 'images/genre.png',
                              triggered=partial(self.update_genre_control))
        self.m1.addSeparator()
        create_menu_action_unique(self, self.m1, ' ', ' ',
                              triggered=None)
        self.m1.addSeparator()
        create_menu_action_unique(self, self.m1, 'Import Add/Change .CSV file to Table _lc_genre_mapping', 'images/import.png',
                              triggered=partial(self.import_csv_mappings))
        self.m1.addSeparator()
        create_menu_action_unique(self, self.m1, ' ', ' ',
                              triggered=None)

        m1tool_tip = "<p style='white-space:wrap'>Update any regular Text custom column, such as #genre, by mapping a DDC or LCC to a value, such as a Genre, in Table _lc_genre_mapping."
        m1tool_tip = m1tool_tip + "<br><br>LC comes pre-loaded with the mapping table.  However, you may add or change (but not delete) as you wish by importing a CSV file.\
                                                     <br><br>The CSV file must be a typical UTF-8 encoded text file that is comma-separated, and with both columns enclosed in quotes.  \
                                                     <br><br>The CSV file must have exactly 2 textual columns.  Column 1 must be a library_code (either DDC or LCC), and Column 2 must be its mapped genre."
        m1tool_tip = m1tool_tip + '<br><br>Example of a CSV row displayed in a text editor to show the comma delimiter and the enclosing quotes: ' + '  "001.944","Monsters (unexplained phenomena)"  '
        m1tool_tip = m1tool_tip + "<br> "
        self.m1.setToolTip(m1tool_tip)
        #END submenu m1 --------------------------------------------------------------------------
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, 'Show DDC Top 20 Pie Chart [NN]', 'images/piechart.png',
                              triggered=partial(self.ddc_pie_chart_1))
        create_menu_action_unique(self, lc_menu, 'Show DDC Top 20 Pie Chart [NNN]', 'images/piechart.png',
                              triggered=partial(self.ddc_pie_chart_2))
        lc_menu.addSeparator()
        create_menu_action_unique(self, lc_menu, ' ', ' ',
                              triggered=None)

        lc_menu.setToolTip("<p style='white-space:wrap'>Usually, DDC/LCC/OCLC-OWI can be derived from an ISBN/ISSN. If so, many other Identifiers can be derived simultaneously.\
                                                                                        <br><br>If ISBN/ISSN fails, DDC/LCC can usually be derived indirectly by using a book's OCLC-OWI, which we must first derive using a book's Author/Title.\
                                                                                        <br><br>OCLC-OWI can usually be used to derive a book's OCLC (Other) and LC 'Extra Author Details'.\
                                                                                        <br><br>OCLC (Other) in combination with ISBN can often be used to retrieve a book's LOC_LCCN. \
                                                                                        <br><br>FAST Tags are derived simultaneously from the identical source as DDC and LCC.  \
                                                                                        <br><br>In summary, both ISBN and OCLC-OWI are critical Identifiers which can be used to derive other Identifiers that then can be used to derive even other Identifiers and/or retrieve other information.\
                                                                                        <br><br>")
                                                                                        #~ <br><br>Extracting ISSNs from non-responsive PDFs is usually successful after re-converting the PDF to PDF first, although that may cause other problems. \
                                                                                        #~ PDFs with images of their ISSN rather than textual ISSNs cannot be processed.")

        self.gui.keyboard.finalize()
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def init_librarycodesdialog(self):

        self.guidb = self.gui.library_view.model().db

        try:
            self.librarycodesdialog.close()
        except:
            pass

        self.qaction.setIcon(get_icon(PLUGIN_ICONS[0]))
        self.librarycodesdialog = LibraryCodesDialog(self.gui,self.qaction.icon(),self.guidb,self.plugin_path,self.ui_exit,self.action_type)
        self.librarycodesdialog.show()

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        self.create_lc_genre_mapping_table(my_db,my_cursor)   # ensures table _lc_genre_mapping exists in current library so user can manually update it in a sqlite tool...
        my_db.close()
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def ui_exit(self):
        self.librarycodesdialog.close()
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def derive_from_isbn_issn(self):

        self.guidb = self.gui.library_view.model().db

        if question_dialog(self.gui, "Library Codes", "Derive Library Codes from ISBN/ISSN for Selected Books?"):
            msg = 'LC is deriving Library Codes from ISBN/ISSN: Wait'
            self.gui.status_bar.show_message(msg)
            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
            source = "ISBN"
            self.derive_all_library_codes_control(source)
        else:
            return
    #-----------------------------------------------------------------------------------------
    def derive_incremental_oclc_owi_identifiers(self):

        self.guidb = self.gui.library_view.model().db

        if question_dialog(self.gui, "Library Codes", "Derive OCLC-OWI Identifier from Author/Title for Selected Books?"):
            msg = 'LC is deriving OCLC-OWI Identifiers from Author/Title: Wait'
            self.gui.status_bar.show_message(msg)
            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
            source = "AUTHOR/TITLE"
            self.derive_all_library_codes_control(source)
        else:
            return
    #-----------------------------------------------------------------------------------------
    def derive_from_oclc_owi(self):

        self.guidb = self.gui.library_view.model().db

        if question_dialog(self.gui, "Library Codes", "Derive DDC/LCC from OCLC-OWI Identifier for Selected Books?"):
            msg = 'LC is deriving DDC/LCC from OCLC-OWI Identifier: Wait'
            self.gui.status_bar.show_message(msg)
            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
            source = "OCLC-OWI"
            self.derive_all_library_codes_control(source)
        else:
            return
    #-----------------------------------------------------------------------------------------
    def derive_incremental_identifiers(self,source):

        self.guidb = self.gui.library_view.model().db

        if question_dialog(self.gui, "Library Codes", "Derive Incremental Identifiers from OCLC-OWI Identifier for Selected Books?"):
            msg = 'LC is deriving Incremental Identifiers from OCLC-OWI Identifier: Wait'
            self.gui.status_bar.show_message(msg)
            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
            if not prefs['OCLC_IDENTIFIER'] == unicode_type(S_TRUE):   #oclc-owi
                prefs['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)
                prefs
            self.oclc_owi_identifier_is_desired = True
            source = "OCLC-OWI_INCREMENTAL_IDENTIFIERS"
            self.derive_all_library_codes_control(source)
        else:
            return
    #-----------------------------------------------------------------------------------------
    def derive_all_library_codes_control(self,source):

        self.guidb = self.gui.library_view.model().db

        number_active = 0

        if prefs['DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1
        if prefs['LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1
        if prefs['FAST_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1
        if prefs['OCLC_IS_ACTIVE'] == unicode_type(S_TRUE):
            number_active = number_active + 1

        if number_active == 0:
            return error_dialog(self.gui, _('Derive Library Codes'),_('No Active Library Codes.'), show=True)

        self.ddc_name = prefs['DDC'].replace("#","").strip()
        self.lcc_name = prefs['LCC'].replace("#","").strip()
        self.fast_name = prefs['FAST'].replace("#","").strip()
        self.oclc_name = prefs['OCLC'].replace("#","").strip()

        if prefs['OCLC_IDENTIFIER'] == unicode_type(S_TRUE):   #oclc-owi
            self.oclc_owi_identifier_is_desired = True
        else:
            self.oclc_owi_identifier_is_desired = False

        #-------------------------------------
        # get selected books
        #-------------------------------------
        self.selected_books_list = self.get_selected_books()
        n_books = len(self.selected_books_list)
        if n_books == 0:
             return error_dialog(self.gui, _('Derive Library Codes'),_('No Books Were Selected.'), show=True)
        self.selected_books_list.sort()
        #-------------------------------------
        # process selected books
        #-------------------------------------
        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
    #-------------------------------------
    #-------------------------------------
        self.populate_ddc_lcc_oclc_using_classify_api(my_db,my_cursor,source)
    #-------------------------------------
    #-------------------------------------
        self.force_refresh_of_cache(self.selected_books_list)
    #-------------------------------------
        self.mark_selected_books()
    #-------------------------------------
        del self.selected_books_list
    #-----------------------------------------------------------------------------------------
    def populate_ddc_lcc_oclc_using_classify_api(self,my_db,my_cursor,source):

        ddc_exists = True
        lcc_exists = True

        n = len(self.ddc_name)
        if self.ddc_name == "none" or self.ddc_name == "":
            ddc_exists = False
        n = len(self.lcc_name)
        if self.lcc_name == "none" or self.lcc_name == "" :
            lcc_exists = False

        if ((not ddc_exists) and (not lcc_exists)):
            self.lc_derivation_messages_label.setText("Cannot Update Library Codes for Selected Books")
            return error_dialog(self.gui, _('Cannot Update Library Codes for Selected Books'),
                                                          _('You Must Configure the Lookup Name for at least one of DDC or LCC.'), show=True)

        # custom column values
        ddc_dict = {}
        lcc_dict = {}
        fast_dict = {}
        oclc_owi_dict = {}

        # extended attributes values
        oclc_other_dict = {}
        lc_authority_name_dict = {}
        viaf_author_id_dict = {}
        authors_additional_details_dict  = {}

        # classify api parameters for Author/Title lookup
        param_dict = {}

        #--------------------------------
        if source == "ISBN":
            self.use_classify_api = True
            isbn_dict = self.get_isbn_identifiers_for_selected_books(my_db,my_cursor)
            my_db.close()
            self.use_isbn = True
            self.use_oclc_owi = False
            if not isbn_dict:
                return error_dialog(self.gui, _('Cannot Update DDC, LCC or OCLC for Selected Books'),
                                                          _('An ISBN/ISSN for at least one of the selected books, plus DDC and/or LCC and/or OCLC-OWI Custom Columns, must exist in this library order to perform this action.'), show=True)
        elif source == "OCLC-OWI":
            self.use_classify_api = True
            self.use_isbn = False
            self.use_oclc_owi = True
            oclc_owi_dict = self.get_oclc_owi_identifiers_for_selected_books(my_db,my_cursor)
            my_db.close()
            if not oclc_owi_dict:
                return error_dialog(self.gui, _('Cannot Update DDC, LCC for Selected Books'),
                                                          _('An OCLC-OWI Identifier for at least one of the selected books, plus DDC and/or LCC Custom Columns, must exist in this library order to perform this action.'), show=True)
        elif source == "OCLC-OWI_INCREMENTAL_IDENTIFIERS":
            self.oclc_owi_identifier_is_desired = True
            self.use_classify_api = False
            isbn_dict = self.get_isbn_identifiers_for_selected_books(my_db,my_cursor)
            self.use_isbn = True
            oclc_owi_dict = self.get_oclc_owi_identifiers_for_selected_books(my_db,my_cursor)
            self.use_oclc_owi = True
            my_db.close()
            if not oclc_owi_dict:
                return error_dialog(self.gui, _('Cannot Update DDC, LCC for Selected Books'),
                                                          _('An OCLC-OWI Identifier for at least one of the selected books, plus DDC and/or LCC Custom Columns, must exist in this library order to perform this action.'), show=True)
        else:  #~ source = "AUTHOR/TITLE"
            self.use_classify_api = True
            self.use_isbn = False
            self.use_oclc_owi = False
            my_db.close()

        #---------------------------------
        #---------------------------------
        book_ids_list = []
        del book_ids_list
        book_ids_list = []

        final_list = []

        self.ddc_name = '#' + self.ddc_name
        self.lcc_name = '#' + self.lcc_name
        self.fast_name = '#' + self.fast_name
        self.oclc_name = '#' + self.oclc_name

        self.guidb = self.gui.library_view.model().db
        db = self.guidb.new_api

        n_total_books = len(self.selected_books_list)
        if n_total_books == 0:
            info_dialog(self.gui, "Library Codes", "No Selected Books.").show()
            return

        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        #---------------------------------------------------------------------------------
        if self.use_classify_api:
        #---------------------------------------------------------------------------------
            n_progress = 0
            n_sleep_counter = 0
            for book in self.selected_books_list:
                s_book = unicode_type(book)
                n_book = int(book)
                #------------------------------------------------------------------
                if self.use_isbn:    # Use ISBN/ISSN to Derive DDC/LCC/OCLC [1-Step]
                #------------------------------------------------------------------
                    try:
                        isbn = isbn_dict[s_book]
                        if isbn:
                            sleep(0)
                            n_progress = n_progress + 1
                            n_sleep_counter = n_sleep_counter + 1
                            if n_sleep_counter == 50:
                                sleep(0.5)
                                n_sleep_counter = 0
                                sleep(0)
                            msg = 'LC is deriving DDC/LCC from ISBN/ISSN:  ' + unicode_type(n_progress)
                            if DEBUG: print(msg)
                            self.gui.status_bar.show_message(msg)
                            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
                            paramtype = "stdnbr"          # "stdnbr"  includes isbn, issn, upc, owi, etc.
                            paramvalue = isbn               # isbn OR issn...
                            sleep(0)
                            ddc, lcc, fast_list, owi, oclc_other, lc_authority_name, viaf_author_id, authors = oclc_classify_api(paramtype,paramvalue,param_dict)        #http://classify.oclc.org/classify2/Classify?stdnbr=0047-2689&summary=true
                            sleep(0)
                            was_found = False
                            if ddc != "NONE":
                                ddc_dict[s_book] = ddc
                                was_found = True
                            if lcc != "NONE":
                                lcc_dict[s_book] = lcc
                                was_found = True
                            if isinstance(fast_list,list):
                                if len(fast_list) > 0:
                                    fast_dict[s_book] = fast_list
                                    was_found = True
                            if owi != "NONE":
                                oclc_owi_dict[s_book] = owi
                                was_found = True
                            if oclc_other != "NONE":
                                oclc_other_dict[s_book] = oclc_other
                                was_found = True
                            if lc_authority_name != "NONE":
                                lc_authority_name_dict[s_book] = lc_authority_name
                                was_found = True
                            if viaf_author_id != "NONE":
                                viaf_author_id_dict[s_book] = viaf_author_id
                                was_found = True
                            if authors != "NONE":
                                authors_additional_details_dict[s_book] = authors
                                was_found = True
                            if was_found:
                                book_ids_list.append(n_book)
                                #~ if DEBUG: print("appending to book_ids_list: ", unicode_type(n_book))
                            del ddc
                            del lcc
                            del owi
                            del oclc_other
                            del lc_authority_name
                            del viaf_author_id
                            del authors
                        else:
                            continue
                    except Exception as e:
                        if DEBUG: print("Exception within the ISBN Route: ", unicode_type(e))
                        continue
                #------------------------------------------------------------------
                elif self.use_oclc_owi:    # Use OCLC-OWI to Derive DDC/LCC [Step 2 of 2 Steps]
                #------------------------------------------------------------------
                    try:
                        n_progress = n_progress + 1
                        msg = 'LC is deriving DDC/LCC from OCLC-OWI [Step 2 of 2]:  ' + unicode_type(n_progress)
                        if DEBUG: print(msg)
                        self.gui.status_bar.show_message(msg)
                        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
                        oclcowi = oclc_owi_dict[s_book]
                        if oclcowi:
                            paramtype = "owi"
                            paramvalue = oclcowi
                            sleep(0)
                            ddc, lcc, fast_list, owi, oclc_other, lc_authority_name, viaf_author_id, authors  = oclc_classify_api(paramtype,paramvalue,param_dict)
                            sleep(0)
                            was_found = False
                            if ddc != "NONE":
                                ddc_dict[s_book] = ddc
                                was_found = True
                            if lcc != "NONE":
                                lcc_dict[s_book] = lcc
                                was_found = True
                            if isinstance(fast_list,list):
                                if len(fast_list) > 0:
                                    fast_dict[s_book] = fast_list
                                    was_found = True
                            if oclc_other != "NONE":
                                oclc_other_dict[s_book] = oclc_other
                                was_found = True
                            if lc_authority_name != "NONE":
                                lc_authority_name_dict[s_book] = lc_authority_name
                                was_found = True
                            if viaf_author_id != "NONE":
                                viaf_author_id_dict[s_book] = viaf_author_id
                                was_found = True
                            if authors != "NONE":
                                authors_additional_details_dict[s_book] = authors
                                was_found = True
                            if was_found:
                                #~ if DEBUG: print("appending to book_ids_list: ", unicode_type(n_book))
                                book_ids_list.append(n_book)
                            del ddc
                            del lcc
                            del owi
                            del oclcowi
                        else:
                            continue
                    except Exception as e:
                        if DEBUG: print("OCLC-OWI Route: ", unicode_type(e))
                        continue
                #------------------------------------------------------------------
                else:   # Use Author/Title to Derive OCLC-OWI [Step 1 of 2 Steps]
                #------------------------------------------------------------------
                    try:
                        n_progress = n_progress + 1
                        msg = 'LC is deriving OCLC-OWI from Author/Title [Step 1 of 2]:  ' + unicode_type(n_progress)
                        if DEBUG: print(msg)
                        self.gui.status_bar.show_message(msg)
                        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
                        book_mi_object = db.get_metadata(n_book, get_cover=False, get_user_categories=False, cover_as_data=False)    # a :class:`Metadata` object.
                        if not book_mi_object:
                            continue
                        colname = 'authors'
                        tmp = book_mi_object.__getattribute__(colname)
                        author = ""
                        for row in tmp:
                            author = row
                            if DEBUG: print("author is: ", author)
                            break
                        #END FOR
                        del tmp
                        colname = 'title'
                        title = book_mi_object.__getattribute__(colname)
                        if DEBUG: print("title is: ", title)
                        if not author:
                            continue
                        if not title:
                            continue
                        paramtype = "author"
                        paramvalue = author
                        param_dict[paramtype] = paramvalue
                        paramtype = "title"
                        paramvalue = title
                        param_dict[paramtype] = paramvalue
                        paramtype = "maxRecs"
                        paramvalue = 25
                        param_dict[paramtype] = paramvalue
                        paramtype = "orderBy"
                        paramvalue = "hold asc"
                        param_dict[paramtype] = paramvalue
                        sleep(0)
                        ddc, lcc, fast_list, owi, oclc_other, lc_authority_name, viaf_author_id, authors  = oclc_classify_api("dummy","dummy",param_dict)
                        sleep(0)
                        was_found = False
                        if owi != "NONE":
                            oclc_owi_dict[s_book] = owi
                            was_found = True
                        if oclc_other != "NONE":
                            oclc_other_dict[s_book] = oclc_other
                            was_found = True
                        if lc_authority_name != "NONE":
                            lc_authority_name_dict[s_book] = lc_authority_name
                            was_found = True
                        if viaf_author_id != "NONE":
                            viaf_author_id_dict[s_book] = viaf_author_id
                            was_found = True
                        if authors != "NONE":
                            authors_additional_details_dict[s_book] = authors
                            was_found = True
                        if was_found:
                            #~ if DEBUG: print("appending to book_ids_list: ", unicode_type(n_book))
                            book_ids_list.append(n_book)     #list of books
                        param_dict.clear()
                        del ddc
                        del lcc
                        del owi
                        del book_mi_object
                    except Exception as e:
                        if DEBUG: print("AUTHOR/TITLE Route: ", unicode_type(e))
                        continue
            #END FOR
            del param_dict

            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

            nd = len(ddc_dict)
            nl = len(lcc_dict)
            noclc = len(oclc_owi_dict)
            if nd == 0 and nl == 0 and noclc == 0:
                info_dialog(self.gui, "Library Codes", "Nothing Found For Any Selected Book.  Visit:  http://classify.oclc.org/classify2/  ").show()
                return

            custom_columns = self.gui.current_db.field_metadata.custom_field_metadata()

            n = len(book_ids_list)
            if n == 0:
                if DEBUG: print("no books in book_ids_list; returning...")
                return

            id_map = {}
            for row in book_ids_list:
                data_changed = False
                s_book = unicode_type(row)
                n_book = int(row)
                mi = Metadata(_('Unknown'))
                if prefs['DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
                    try:
                        custcol1 = custom_columns[self.ddc_name]         #  custcol = custom_columns["#ddc"]
                        custcol1['#value#'] = unicode_type(ddc_dict[s_book])
                        mi.set_user_metadata(self.ddc_name, custcol1)   # class Metadata in  src>calibre>ebooks>metadata>book>base.py
                        data_changed = True
                    except Exception as e:
                        #~ if DEBUG: print("no-data for book in ddc_dict: book id: ", unicode_type(e))
                        pass
                if prefs['LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
                    try:
                        custcol2 = custom_columns[self.lcc_name]
                        custcol2['#value#'] = unicode_type(lcc_dict[s_book])
                        mi.set_user_metadata(self.lcc_name, custcol2)
                        data_changed = True
                    except Exception as e:
                        #~ if DEBUG: print("no-data for book in lcc_dict: book id: ", unicode_type(e))
                        pass

                if prefs['FAST_IS_ACTIVE'] == unicode_type(S_TRUE):
                    try:
                        custcol4 = custom_columns[self.fast_name]
                        fast_list = fast_dict[s_book]
                        tmp_list = []
                        for new_tag in fast_list:
                            if not isinstance(new_tag,unicode_type):
                                new_tag = unicode_type(new_tag)
                            tmp_list.append(new_tag)
                        #END FOR
                        custcol4['#value#'] = tmp_list
                        mi.set_user_metadata(self.fast_name, custcol4)     # class Metadata in  src>calibre>ebooks>metadata>book>base.py
                        data_changed = True
                    except Exception as e:
                        #~ if DEBUG: print("no-data for book in fast_dict: book id: ", unicode_type(e))
                        pass

                if prefs['OCLC_IS_ACTIVE'] == unicode_type(S_TRUE):
                    try:
                        custcol3 = custom_columns[self.oclc_name]
                        custcol3['#value#'] = unicode_type(oclc_owi_dict[s_book])
                        mi.set_user_metadata(self.oclc_name, custcol3)
                        data_changed = True
                    except Exception as e:
                        #~ if DEBUG: print("no-data for book in oclc_owi_dict: book id: ", unicode_type(e))
                        pass
                if data_changed:
                    id_map[n_book] = mi
                    final_list.append(n_book)
                    should_show_message = False
                else:
                    if self.oclc_owi_identifier_is_desired:
                        final_list.append(n_book)
            #END FOR
        #---------------------------------------------------------------------------------
        else:  # NOT self.use_classify_api
        #---------------------------------------------------------------------------------
            self.oclc_owi_identifier_is_desired = True
            for book in self.selected_books_list:
                n_book = int(book)
                final_list.append(n_book)
            #END FOR
        #---------------------------------------------------------------------------------

        if not self.oclc_owi_identifier_is_desired:   # oclc-owi
            if self.use_isbn:
                pass
            else:        # Required to derive via Author/Title
                prefs['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)    # oclc-owi
                prefs
                self.oclc_owi_identifier_is_desired = True

        #~ SOURCE_TYPE_VIAF = unicode_type("viaf_author_id")
        #~ SOURCE_TYPE_OCLC = unicode_type("www.worldcat.org/oclc")
        #~ SOURCE_TYPE_XID_OWI = unicode_type("xisbn.worldcat.org/webservices/xid/owi/")
        #~ SOURCE_TYPE_XID_OCLC = unicode_type("xisbn.worldcat.org/webservices/xid/oclcnum/")

        if self.oclc_owi_identifier_is_desired:
            if len(final_list) > 0:
                msg = 'LC is now adding multiple identifiers for selected books'
                self.gui.status_bar.show_message(msg)
                QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
                try:
                    n = len(oclc_owi_dict)
                except:
                    n = 0
                if n == 0:
                    my_db,my_cursor,is_valid = self.apsw_connect_to_library()
                    if not is_valid:
                        return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
                    oclc_owi_dict = self.get_oclc_owi_identifiers_for_selected_books(my_db,my_cursor)
                    my_db.close()
                else:
                    if self.use_classify_api:  # just downloaded data
                        if oclc_owi_dict:        # just downloaded and the dict was created from that downloaded results data
                            self.add_oclc_owi_identifiers(oclc_owi_dict,final_list)
                if len(oclc_owi_dict) > 0:    # next, need to add oclc (other) using its matching isbn.  this must be done prior to loc_lccn being derived from a book's oclc (other).
                    try:
                        n = len(isbn_dict)
                    except:
                        n = 0
                    if n == 0:
                        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
                        if not is_valid:
                            return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
                        isbn_dict = self.get_isbn_identifiers_for_selected_books(my_db,my_cursor)
                        my_db.close()
                    # a 'better' oclc_other_dict will be created to replace the existing one since the source type is: SOURCE_TYPE_XID_OWI
                    oclc_other_dict = self.call_lc_generic_webscraping_api(SOURCE_TYPE_XID_OWI,oclc_owi_dict,final_list,isbn_dict)    #call_type = "owi"  returns oclc for matching owi/isbn combination
                if len(oclc_other_dict) > 0:
                    self.add_oclc_other_identifiers(oclc_other_dict,final_list)
                if len(viaf_author_id_dict) > 0:
                    if len(lc_authority_name_dict) > 0:
                        self.add_extended_identifiers(lc_authority_name_dict,viaf_author_id_dict,final_list)
                if len(viaf_author_id_dict) > 0:
                    self.call_lc_generic_webscraping_api(SOURCE_TYPE_VIAF,viaf_author_id_dict,final_list,None)
                if len(oclc_other_dict) > 0:
                    if self.use_classify_api:
                        self.call_lc_generic_webscraping_api(SOURCE_TYPE_OCLC,oclc_other_dict,final_list,None)            # returns multiple LC Extra Author Detail rows
                    self.call_lc_generic_webscraping_api(SOURCE_TYPE_XID_OCLC,oclc_other_dict,final_list,None)         #call_type = "oclc"  returns loc_lccn for oclc, and does not use isbn at all
                if len(authors_additional_details_dict) > 0:
                    self.add_additional_attributes(authors_additional_details_dict)
                self.force_refresh_of_cache(final_list)
            else:
                pass
        else:
            pass


        if (not self.use_isbn) and (not self.use_oclc_owi):  # only getting oclc-owi for step 1 of 2 steps via author/title
            if len(oclc_owi_dict) == 0:
                info_dialog(self.gui, "Library Codes", "No OCLC-OWI Identifiers were found for the selected books.  Nothing at all was just updated.").show()
                return

        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        if self.use_classify_api:
            n = len(final_list)
            if n == 0:
                info_dialog(self.gui, "Library Codes", "Nothing Updated For Any Books, But There Were No Errors.  Visit: http://classify.oclc.org/classify2/ ").show()
                return
            msg = "LC is preparing to update its Custom Columns"
            self.gui.status_bar.show_message(msg)
            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
            payload = final_list, oclc_owi_dict
            edit_metadata_action = self.gui.iactions['Edit Metadata']
            edit_metadata_action.apply_metadata_changes(id_map, callback=self.finish_displaying_results_of_ddc_lcc(payload))
        else:
            pass  # no ddc/lcc custom column data was derived...
    #--------------------------------------------------------------------------------------------------------------------------------------
    def finish_displaying_results_of_ddc_lcc(self, payload):
        final_list, oclc_owi_dict = payload
        self.force_refresh_of_cache(final_list)
    #-------------------------------------------------------------------------------------------------------------------------------------
    def get_isbn_identifiers_for_selected_books(self,my_db,my_cursor):

        try:
            del isbn_dict
        except:
            pass

        isbn_dict = {}

        #-----------------------------
        #before anything else, ensure that at least one of the custom columns exists in this library...
        self.ddc_name = self.ddc_name.replace("#","")
        self.lcc_name = self.lcc_name.replace("#","")
        self.oclc_name = self.oclc_name.replace("#","")
        mysql = "SELECT count(*) FROM custom_columns WHERE label = ? OR label = ? OR label = ?"
        my_cursor.execute(mysql,(self.ddc_name,self.lcc_name,self.oclc_name))
        s_count = my_cursor.fetchall()
        for row in s_count:
            for col in row:
                s_count = unicode_type(col)
            #END FOR
        #END FOR
        s_count = unicode_type(s_count)
        s_count = s_count.replace("(","")
        s_count = s_count.replace(")","")
        s_count = s_count.replace(",","")
        s_count = s_count.replace("'","")
        s_count = s_count.strip()
        if not unicode_type(s_count) > unicode_type("0") :
            if DEBUG: print("lcc and ddc and oclc have not been configured as custom columns in this library")
            return isbn_dict

        #-----------------------------

        for book in self.selected_books_list:
            book = unicode_type(book)
            mysql = "SELECT val FROM identifiers WHERE book = [BOOK] AND (type = 'isbn' OR type = 'issn') AND val NOT NULL "
            mysql = mysql.replace("[BOOK]", book)
            my_cursor.execute(mysql)
            tmp_rows = []
            del tmp_rows
            tmp_rows = my_cursor.fetchall()
            if tmp_rows:
                tmp_rows.sort(reverse=True)    #this forces isbn to be used instead of issn if both exist
                for row in tmp_rows:
                    for col in row:
                        isbn_dict[book] = col
                    #END FOR
                    break  #can have BOTH isbn and issn; isbn.  The ISBN identifies the individual book in a series or a specific year for an annual or biennial. The ISSN identifies the ongoing series, or the ongoing annual or biennial serial.
                #END FOR
            else:
                continue
        #END FOR

        return isbn_dict
    #-------------------------------------------------------------------------------------------------------------------------------------
    def get_oclc_owi_identifiers_for_selected_books(self,my_db,my_cursor):

        try:
            del oclc_owi_dict
        except:
            pass

        oclc_owi_dict = {}

        #-----------------------------
        #before anything else, ensure that at least one of the custom columns exists in this library...
        self.ddc_name = self.ddc_name.replace("#","")
        self.lcc_name = self.lcc_name.replace("#","")
        self.oclc_name = self.oclc_name.replace("#","")
        mysql = "SELECT count(*) FROM custom_columns WHERE label = ? OR label = ? OR label = ?"
        my_cursor.execute(mysql,(self.ddc_name,self.lcc_name,self.oclc_name))
        s_count = my_cursor.fetchall()
        for row in s_count:
            for col in row:
                s_count = unicode_type(col)
            #END FOR
        #END FOR
        s_count = unicode_type(s_count)
        s_count = s_count.replace("(","")
        s_count = s_count.replace(")","")
        s_count = s_count.replace(",","")
        s_count = s_count.replace("'","")
        s_count = s_count.strip()
        if not unicode_type(s_count) > unicode_type("0") :
            if DEBUG: print("lcc and ddc and oclc have not been configured as custom columns in this library")
            return isbn_dict

        #-----------------------------

        for book in self.selected_books_list:
            book = unicode_type(book)
            mysql = "SELECT val FROM identifiers WHERE book = [BOOK] AND type = 'oclc-owi' AND val NOT NULL "
            mysql = mysql.replace("[BOOK]", book)
            my_cursor.execute(mysql)
            tmp_rows = []
            del tmp_rows
            tmp_rows = my_cursor.fetchall()
            if tmp_rows:
                for row in tmp_rows:
                    for col in row:
                        oclc_owi_dict[book] = col
                    #END FOR
                    break
                #END FOR
            else:
                continue
        #END FOR

        return oclc_owi_dict
    #-------------------------------------------------------------------------------------------------------------------------------------
    def add_oclc_owi_identifiers(self,oclc_owi_dict,final_list):
        # oclc-owi is an identifier at oclc.org:        http://classify.oclc.org/classify2/api_docs/classify.html

        if not self.oclc_owi_identifier_is_desired:
            if self.use_isbn:
                return
            else:        # Required to derive via Author/Title
                prefs['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)
                prefs
                self.oclc_owi_identifier_is_desired = True

        if len(oclc_owi_dict) == 0:
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
        #-----------------------------
        my_cursor.execute("begin")
        for book in final_list:
            book = unicode_type(book)
            try:
                if book in oclc_owi_dict:
                    owi = oclc_owi_dict[book]
                    if DEBUG: print("Adding 'oclc-owi' identifier: ", unicode_type(owi))
                else:
                    continue
                owi = unicode_type(owi)
                book = int(book)
                mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,'oclc-owi', ?)  "
                my_cursor.execute(mysql,(None,book,owi))
            except Exception as e:
                if DEBUG: print("Exception: ", unicode_type(e))
                continue
        #END FOR
        my_cursor.execute("commit")
        my_db.close()
    #-------------------------------------------------------------------------------------------------------------------------------------
    def add_oclc_other_identifiers(self,oclc_other_dict,final_list):
        # oclc (not oclc-owi) is another identifier at oclc.org:        http://classify.oclc.org/classify2/api_docs/classify.html

        if len(oclc_other_dict) == 0:
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
        #-----------------------------
        my_cursor.execute("begin")
        for book in final_list:
            book = unicode_type(book)
            try:
                if book in oclc_other_dict:
                    oclc = oclc_other_dict[book]
                    oclc = unicode_type(oclc)
                    oclc = oclc.strip()
                else:
                    continue
                book = int(book)
                if DEBUG: print("Adding 'oclc' identifier: ", oclc, "  for book: ", unicode_type(book))
                mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,'oclc', ?)  "
                my_cursor.execute(mysql,(None,book,oclc))
            except Exception as e:
                if DEBUG: print("Exception: ", unicode_type(e))
                continue
        #END FOR
        my_cursor.execute("commit")
        my_db.close()
        del oclc_other_dict
    #-----------------------------------------------------------------------------------------
    def add_extended_identifiers(self,lc_authority_name_dict,viaf_author_id_dict,final_list):
        # add additional book attributes obtained as part of deriving other library codes.

        if not self.oclc_owi_identifier_is_desired:
            if self.use_isbn:
                return
            else:        # Required to derive via Author/Title
                prefs['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)
                prefs

        if len(lc_authority_name_dict) == 0 and len(viaf_author_id_dict) == 0:
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
        #-----------------------------
        my_cursor.execute("begin")
        for book in final_list:
            book = unicode_type(book)
            try:
                if book in lc_authority_name_dict:
                    lc_authority_name = lc_authority_name_dict[book]
                else:
                    continue
                if not lc_authority_name:
                    continue
                lc_authority_name = unicode_type(lc_authority_name)
                lc_authority_name = lc_authority_name.strip()
                if not lc_authority_name > "":
                    continue
                if unicode_type(lc_authority_name) == unicode_type("null"):
                    continue
                book = int(book)
                mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,'lc_authority_name', ?)  "
                my_cursor.execute(mysql,(None,book,lc_authority_name))
            except Exception as e:
                if DEBUG: print("Exception: ", unicode_type(e))
                continue
        #END FOR
        my_cursor.execute("commit")
        #-----------------------------
        my_cursor.execute("begin")
        for book in final_list:
            book = unicode_type(book)
            try:
                if book in viaf_author_id_dict:
                    viaf_author_id = viaf_author_id_dict[book]
                else:
                    continue
                if not viaf_author_id:
                    continue
                viaf_author_id = unicode_type(viaf_author_id)
                viaf_author_id = viaf_author_id.strip()
                if not viaf_author_id > "":
                    continue
                if unicode_type(viaf_author_id) == unicode_type("null"):
                    continue
                book = int(book)
                mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,'viaf_author_id', ?)  "
                my_cursor.execute(mysql,(None,book,viaf_author_id))
            except Exception as e:
                if DEBUG: print("Exception: ", unicode_type(e))
                continue
        #END FOR
        my_cursor.execute("commit")
        #-----------------------------
        my_db.close()

        del lc_authority_name_dict
        del viaf_author_id_dict
    #-----------------------------------------------------------------------------------------
    def add_additional_attributes(self,authors_additional_details_dict):

        if not prefs['EXTRA_AUTHOR_DETAILS_IS_ACTIVE'] == unicode_type(S_TRUE):
            return

        if len(authors_additional_details_dict) == 0:
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
        #-----------------------------

        msg = "LC is now updating the specified 'LC Extra Author Data' custom column..."
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        cc_label = prefs['EXTRA_AUTHOR_DETAILS']
        cc_label = cc_label.replace('#','')
        cc_label = cc_label.strip()

        custom_column_number = None

        mysql = "SELECT id,label FROM custom_columns WHERE label = ? "
        my_cursor.execute(mysql,([cc_label]))
        tmp_rows = my_cursor.fetchall()
        if not tmp_rows:
            return error_dialog(self.gui, _('Derive Library Codes'),_('Specified custom column label does not exist; nothing can be done.'), show=True)
        for row in tmp_rows:
            for col in row:
                custom_column_number = unicode_type(col)
                break
            #END FOR
        #END FOR

        if not custom_column_number:
            return error_dialog(self.gui, _('Derive Library Codes'),_('Specified custom column id does not exist; nothing can be done.'), show=True)

        #~ for k,v in authors_additional_details_dict.iteritems():           #~ authors_additional_details_dict[s_book] = authors additional details
        for k,v in iteritems(authors_additional_details_dict):           #~ authors_additional_details_dict[s_book] = authors additional details
            book = int(k)
            new_tag_list = []
            for row in v:  # v = author_extras_return_list from  classify_web_service_api
                if "|" in row:
                    s_split1 = row.split("|")
                    for item in s_split1:
                        if "--" in item:
                            s_split2 = item.split("--")
                            for line in s_split2:
                                new_tag_list.append(unicode_type(line))
                            #END FOR
                            del s_split2
                        else:
                            new_tag_list.append(unicode_type(item))
                    #END FOR
                    del s_split1
                else:
                    if "--" in row:
                        s_split = row.split("--")
                        for item in s_split:
                            new_tag_list.append(unicode_type(item))
                        #END FOR
                        del s_split
                    else:
                        new_tag_list.append(unicode_type(row))
            #END FOR
            new_tag_list = self.format_new_tag_list(new_tag_list)
            self.add_new_lc_extra_author_details(my_db,my_cursor,custom_column_number,book,new_tag_list)
            del new_tag_list
        #END FOR

        del custom_column_number
        del authors_additional_details_dict
        #-----------------------------
        my_db.close()
        #-----------------------------

        msg = "LC has updated the specified 'LC Extra Author Data' custom column"
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
    #-----------------------------------------------------------------------------------------
    def format_new_tag_list(self,tmp_tag_list):
        #~        ˏ	        719	02CF	 	MODIFIER LETTER LOW ACUTE ACCENT

        s_719 = unicode_type('ˏ')
        s_719 = s_719.strip()

        new_tag_list = []

        for row in tmp_tag_list:
            s = row
            s = unicode_type(s)
            s = s.replace("  "," ")
            s = s.replace(",","/")                   # Shandley, Robert R.                 ==>>  Shandley/ Robert R.
            s = s.replace("/ 1"," : 1")            # Warhol/ Andy/ 1928-1987      ==>>  Warhol/ Andy : 1928-1987
            s = s.replace("/ 2"," : 2")            # Young/ Andy/ 2001-2098       ==>>   Young/ Andy : 2001-2098
            s = s.replace("."," ")                   # Shandley/ Robert R.                ==>>  Shandley/ Robert R        and also dots anywhere else (especially those)
            s = s.replace("'"," ")
            s = s.replace('"','')
            s = s.replace("  "," ")
            if s.endswith("/"):
                s = s[0:-1]
            if s.startswith("/"):
                s = s[1: ]
            s = s.replace("/",s_719)              # Shandley/ Robert R.                 ==>>  Shandleyˏ Robert R.
            s = s.strip()

            s = self.match_regex_new_tag(s)
            if not s:
                continue

            s = s.title()

            if ":" in s or "1" in s or "2" in s or ";" in s or "[" in s or "(" in s:
                new_tag_list.append(s)
            else:
                if s_719 in s:
                    continue   # e.g. Shandleyˏ Robert R.    which is just a plain author name and redundant
                else:
                    if " " in s:
                        new_tag_list.append(s)    # e.g. United States
                    else:
                        continue   # e.g. William or Daughter or London or Kate
            try:
                if DEBUG: print("new value for LC Extra Author Data: ", s)
            except:
                if DEBUG: print("error: unprintable new value for LC Extra Author Data: ", unicode_type(s))
        #END FOR
        del tmp_tag_list

        return new_tag_list
    #-----------------------------------------------------------------------------------------
    def match_regex_new_tag(self,new_tag):
        try:
            re1 = "^[0-9]+[-][0-9]+$|books|^united states$|fictitious|^[(][a-z ]+[)]$|tales|character|stories|paperback|hardback|novel|[-][ ]texts$"      # e.g.  1928-1987   or   contains 'books'   or   equals  'united states'   or like '(howard phillips)'
            p1 = re.compile(re1, re.IGNORECASE)
            match1 = p1.search(new_tag)
            if match1:
                return None
        except:
            pass
        return new_tag
    #-----------------------------------------------------------------------------------------
    def add_new_lc_extra_author_details(self,my_db,my_cursor,custom_column_number,book,new_tag_list):

        #-----------------------------
        mysql = "INSERT OR  IGNORE INTO custom_column_[NN] (id,value) VALUES (?,?)"
        mysql = mysql.replace("[NN]",custom_column_number)

        my_cursor.execute("begin")
        for new_tag in new_tag_list:
            if not isinstance(new_tag,unicode_type):
                new_tag = unicode_type(new_tag)
            my_cursor.execute(mysql,(None,new_tag))
        #END FOR
        my_cursor.execute("commit")
        #-----------------------------
        #-----------------------------
        mysql = "INSERT OR  IGNORE INTO books_custom_column_[NN]_link (id,book,value) \
                                                         VALUES (?,?,\
                                                         (SELECT id FROM custom_column_[NN] WHERE value = ?) )"
        mysql = mysql.replace("[NN]",custom_column_number)

        my_cursor.execute("begin")
        for new_tag in new_tag_list:
            if not isinstance(new_tag,unicode_type):
                new_tag = unicode_type(new_tag)
            my_cursor.execute(mysql,(None,book,new_tag))
        #END FOR
        my_cursor.execute("commit")
        #-----------------------------
        del new_tag_list
    #-----------------------------------------------------------------------------------------
    def mark_selected_books(self):

        found_dict = {}
        s_true = 'true'
        for row in self.selected_books_list:
            key = int(row)
            found_dict[key] = s_true
        #END FOR

        marked_ids = dict.fromkeys(found_dict, s_true)
        self.gui.current_db.set_marked_ids(marked_ids)
        self.gui.search.clear()
        self.gui.search.set_search_string('marked:true')

        del found_dict
    #-----------------------------------------------------------------------------------------
    def get_selected_books(self):

        try:
            del self.selected_books_list
        except:
            pass

        self.selected_books_list = []

        book_ids_list = []

        book_ids_list = list(map(partial(self.convert_id_to_book), self.gui.library_view.get_selected_ids()))  #https://stackoverflow.com/questions/50671360/map-in-python-3-vs-python-2
        n = len(book_ids_list)
        if n == 0:
            del book_ids_list
            return self.selected_books_list
        for item in book_ids_list:
            s = unicode_type(item['calibre_id'])
            self.selected_books_list.append(s)
        #END FOR

        del book_ids_list

        return self.selected_books_list
    #-----------------------------------------------------------------------------------------
    def convert_id_to_book(self, idval):
        book = {}
        book['calibre_id'] = idval
        return book
    #-----------------------------------------------------------------------------------------
    def force_refresh_of_cache(self,selected_book_list):
        backend = self.gui.library_view.model().db.backend
        mydbcache = dbcache(self.gui.library_view.model().db.backend)
        mydbcache.init()
        self.gui.library_view.model().refresh_ids(selected_book_list)
        self.gui.tags_view.recount()
        del selected_book_list
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
            if DEBUG: print("error: ", unicode_type(e))
            is_valid = False
            return None,None,is_valid

        my_cursor = my_db.cursor()

        mysql = "PRAGMA main.busy_timeout = 5000;"      #PRAGMA busy_timeout = milliseconds;
        my_cursor.execute(mysql)

        return my_db,my_cursor,is_valid
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def scrub_isbn(self):
        #~ This menu option is just to encourage users to scrub their ISBNs even if they are already ISBN-13s.
        msg = "ISBNs Scrubbed. 'E'dit to View New Value."
        self.scrub_isbns(msg)
    #-----------------------------------------------------------------------------------------
    def scrub_isbns(self,msg=None):
        #~ This menu option will always convert 10s to 13s, and always does scrubbing too.

        self.selected_books_list = self.get_selected_books()

        self.lc_isbns_scrubbed_books_list = []

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Convert ISBNs'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        self.scrub_isbn_values(my_db,my_cursor)

        self.convert_identifiers_isbn_from_10_to_13(my_db, my_cursor)

        self.detect_isbn_changes_to_refresh(my_db, my_cursor)

        my_db.close()

        self.mark_selected_books()

        del self.selected_books_list

        if not msg:
            msg = "Any ISBN-10s were Converted to ISBN-13s.  'E'dit to View New Value."

        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
    #-----------------------------------------------------------------------------------------
    def convert_identifiers_isbn_from_10_to_13(self,my_db, my_cursor):
        #~ Important: this is alway done for all books, even if they were NOT selected otherwise.

        mysql = "SELECT book, val FROM identifiers WHERE type = 'isbn' \
                       AND val NOT LIKE '977%'  AND val NOT LIKE '978%'  \
                        AND val NOT LIKE '979%'  AND val NOT NULL;"
        my_cursor.execute(mysql)
        tmp_rows = my_cursor.fetchall()
        if not tmp_rows:
            if DEBUG: print("No ISBN 10's Were Found to Convert")
            return
        else:
            n = len(tmp_rows)
            if DEBUG: print("Total Number of ISBN 10s Found: " + unicode_type(n))
            if n == 0 :
                return
            my_counter = 0
            my_total = 0
            my_cursor.execute("begin")  #apsw
            for row in tmp_rows:
                book, old_isbn = row
                book = int(book)
                old_isbn = unicode_type(old_isbn).strip()
                if len(old_isbn) == 10:
                    self.lc_isbns_scrubbed_books_list.append(book)
                    new_isbn = unicode_type(self._convert_isbn_convert_10_to_13(old_isbn))
                    if len(new_isbn) == 13:
                        if isinstance(new_isbn, str):
                            new_isbn = unicode_type(new_isbn)
                        mysql = "UPDATE identifiers SET val = ? WHERE book = ? AND type = 'isbn' "
                        my_cursor.execute(mysql,(new_isbn, book))
                        if DEBUG: print("ISBN10 Converted to ISBN13: " + unicode_type(old_isbn) + " >>> " + unicode_type(new_isbn))
                    else:
                        if isinstance(old_isbn, str):
                            old_isbn = unicode_type(old_isbn)
                        if DEBUG: print("This ISBN10 appears to not really be an ISBN10, and was deleted:  " + unicode_type(old_isbn) )
                        mysql = "DELETE FROM identifiers WHERE val = ? AND book = ? AND type = 'isbn' "
                        my_cursor.execute(mysql,(old_isbn, book))
                    self.lc_isbns_scrubbed_books_list.append(book)
                else:
                    if isinstance(old_isbn, str):
                        old_isbn = unicode_type(old_isbn)
                    if DEBUG: print("This ISBN appears to not really be any kind of ISBN, and was deleted:  " + unicode_type(old_isbn) )
                    mysql = "DELETE FROM identifiers WHERE val = ? AND book = ? AND type = 'isbn' "
                    my_cursor.execute(mysql,(old_isbn, book))
                    self.lc_isbns_scrubbed_books_list.append(book)
            #END FOR
            my_cursor.execute("commit")
    #-----------------------------------------------------------------------------------------
    def _convert_isbn_check_digit_13(self,isbn):
        try:
            assert len(isbn) == 12
            sum = 0
            for i in range(len(isbn)):
                c = int(isbn[i])
                if i % 2: w = 3
                else: w = 1
                sum += w * c
            r = 10 - (sum % 10)
            if r == 10: return '0'
            else: return unicode_type(r)
        except:
            return isbn
    #-----------------------------------------------------------------------------------------
    def _convert_isbn_convert_10_to_13(self,isbn):
        try:
            assert len(isbn) == 10
            prefix = '978' + isbn[:-1]
            check = self._convert_isbn_check_digit_13(prefix)
            return prefix + check
        except:
            return isbn
    #-----------------------------------------------------------------------------------------
    def scrub_isbn_values(self,my_db,my_cursor):
        try:
            #~ ----------
            my_cursor.execute("begin")
            mysql = "UPDATE OR IGNORE identifiers SET type = 'isbn',val=type WHERE type LIKE '%978%' AND val NOT LIKE '%978%'   "    # type 978000123456 value xxxxx  should be:  isbn:978000123456
            my_cursor.execute (mysql)
            mysql = "UPDATE OR IGNORE identifiers SET type = 'isbn',val=type WHERE type LIKE '979%' AND val NOT LIKE '979%'   "          # 979 is reservef for use by the same int'l agency that assigns 978
            my_cursor.execute (mysql)
            mysql = "UPDATE OR IGNORE identifiers SET type = 'isbn',val=type WHERE type LIKE '977%' AND val NOT LIKE '977%'   "          # 977 is reservef for use by the same int'l agency that assigns 978
            my_cursor.execute (mysql)
            my_cursor.execute("commit")
            #~ ----------
            my_cursor.execute("begin")
            mysql = "UPDATE OR IGNORE identifiers SET type = 'isbn' WHERE type LIKE '%isbn%' AND type != 'isbn'   "                               # type urnisbn            value 978000123456   should be:  isbn:978000123456
            my_cursor.execute (mysql)
            my_cursor.execute("commit")
            #~ ----------
            my_cursor.execute("begin")
            mysql = "UPDATE OR IGNORE identifiers SET type = (trim(type)) WHERE type LIKE '%isbn%'  "
            my_cursor.execute (mysql)
            my_cursor.execute("commit")
            #~ ----------
            my_cursor.execute("begin")
            mysql = "UPDATE identifiers SET val = (replace(val,'-','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%-%')"
            my_cursor.execute (mysql)
            mysql = "UPDATE identifiers SET val = (replace(val,' ','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '% %') "
            my_cursor.execute (mysql)
            mysql = "UPDATE identifiers SET val = (replace(val,':','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%:%') "
            my_cursor.execute (mysql)
            mysql = "UPDATE identifiers SET val = (replace(val,'/','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%/%') "
            my_cursor.execute (mysql)
            mysql = "UPDATE identifiers SET val = (trim(val)) WHERE type = 'isbn'  "
            my_cursor.execute (mysql)
            my_cursor.execute("commit")
            #~ ----------
            my_cursor.execute("begin")
            mysql = "UPDATE identifiers SET val = (replace(val,'urn','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%urn%') "
            my_cursor.execute (mysql)
            mysql = "UPDATE identifiers SET val = (replace(val,'ebook','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%ebook%') "
            my_cursor.execute (mysql)
            mysql = "UPDATE identifiers SET val = (replace(val,'eBook','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%eBook%') "
            my_cursor.execute (mysql)
            my_cursor.execute("commit")
            #~ ----------
            my_cursor.execute("begin")
            mysql = "UPDATE identifiers SET val = (replace(val,'isbn','')) WHERE val IN(SELECT val FROM identifiers WHERE type = 'isbn' AND val LIKE '%isbn%') "
            my_cursor.execute (mysql)
            my_cursor.execute("commit")
            #~ ----------
            if DEBUG: print("All ISBN13s have been standardized by removing any dashes, spaces and prefixes.")
        except Exception as e:
            if DEBUG: print(unicode_type(e))
            try:
                my_cursor.execute("commit")
            except:
                pass
    #---------------------------------------------------------------------------------------------------------------------------------------
    def detect_isbn_changes_to_refresh(self,my_db, my_cursor):

        mysql = "SELECT book, val FROM identifiers WHERE type = 'isbn' "
        my_cursor.execute(mysql)
        tmp_rows = my_cursor.fetchall()
        if not tmp_rows:
            return
        if len(tmp_rows) == 0:
            return

        tmp_rows.sort()

        for row in tmp_rows:
            book,val = row
            mi = self.guidb.new_api.get_metadata(book)
            identifiers_dict = mi.get_identifiers()
            if 'isbn' in identifiers_dict:
                cache_val = identifiers_dict['isbn']
            else:
                cache_val = "NONE"
            if val != cache_val:
                self.lc_isbns_scrubbed_books_list.append(book)
                if DEBUG: print("book: ", unicode_type(book), "  db val: ", unicode_type(val), "  cache val: ", unicode_type(cache_val))
        #END FOR

        self.lc_isbns_scrubbed_books_list = list(set(self.lc_isbns_scrubbed_books_list))

        if len(self.lc_isbns_scrubbed_books_list) > 0:
            if DEBUG: print("Cache being refreshed from metadata.db due to ISBN key/value changes")
            self.force_refresh_of_cache(self.lc_isbns_scrubbed_books_list)

        for book in self.lc_isbns_scrubbed_books_list:
            if not book in self.selected_books_list:
                self.selected_books_list.append(book)    #so will get marked as if it were selected, since it was changed although not first selected by the user...
        #END FOR

        del self.lc_isbns_scrubbed_books_list
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def call_lc_generic_webscraping_api(self,source_type,source_dict,final_list,another_dict):
        # actual dict named by source_dict depends on the source_type...
        # e.g. oclc_other_dict[s_book] = oclc_other
        # e.g. viaf_author_id_dict[book] = viaf_author_id
        # e.g. isbn_dict[s_book] = isbn

        # another_dict is currently only used for:   isbn_dict

        msg = 'LC is now downloading requested data for selected books...Wait...'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        final_results_dict = library_codes_generic_webscraping_api(source_type,source_dict,another_dict)

        self.add_additional_webscraped_data(final_results_dict,source_type,source_dict,final_list)

        if another_dict:
            if unicode_type(source_type) == SOURCE_TYPE_XID_OWI:
                new_oclc_other_dict = self.create_new_oclc_other_dict(final_results_dict,source_dict)
                del final_results_dict
                del source_dict
                del final_list
                del another_dict
                return new_oclc_other_dict

        del final_results_dict
        del source_dict
        del final_list
        del another_dict

        none_dict = {}

        return none_dict
    #-----------------------------------------------------------------------------------------
    def create_new_oclc_other_dict(self,final_results_dict,source_dict):
        #~ source_dict == oclc_owi_dict where  oclc_owi_dict[s_book] = oclc-owi
        #~ final_results_dict[oclc-owi] = a list, containing OCLC (other)

        new_oclc_other_dict = {}    #  k = s_book; v = oclc (other)

        #~ for s_book,oclc_owi in source_dict.iteritems():
        for s_book,oclc_owi in iteritems(source_dict):
            if oclc_owi in final_results_dict:
                tmp_list = final_results_dict[oclc_owi]
                results_list_identifier_type = ""
                for item in tmp_list:         # item = "oclc",v,oclc (other)  where v is the book's oclc-owi
                    results_list_identifier_type,dummy,oclc = item
                    if unicode_type(results_list_identifier_type) == unicode_type("oclc"):
                        new_oclc_other_dict[s_book] = oclc
                        #~ if DEBUG: print("book, new oclc: ", s_book, oclc)
                        break
                 #END FOR
            else:
                continue
        #END FOR

        del final_results_dict
        del source_dict

        return new_oclc_other_dict
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def add_additional_webscraped_data(self,final_results_dict,source_type,source_dict,final_list):
        # add additional identifiers or custom column data, depending on source_type

        if not self.oclc_owi_identifier_is_desired:
            if self.use_isbn:
                if unicode_type(source_type) == SOURCE_TYPE_VIAF or unicode_type(source_type) == SOURCE_TYPE_XID_OWI or unicode_type(source_type) == SOURCE_TYPE_XID_OCLC:
                    del final_results_dict
                    return
                else:
                    pass
            else:        # Required to derive via Author/Title
                prefs['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)
                prefs

        if len(final_results_dict) == 0:
            del final_results_dict
            self.was_final_results_dict_empty = True
            return
        else:
            self.was_final_results_dict_empty = False

        if unicode_type(source_type) == SOURCE_TYPE_VIAF:
            self.add_isni_lccn_for_viaf(final_results_dict)
        elif unicode_type(source_type) == SOURCE_TYPE_OCLC:
            self.add_lcead_for_oclc(final_results_dict,final_list,source_dict)
        elif unicode_type(source_type) == SOURCE_TYPE_XID_OWI:
            self.add_oclc_for_xid(final_results_dict,source_dict,'owi')
        elif unicode_type(source_type) == SOURCE_TYPE_XID_OCLC:
            self.add_loc_lccn_for_xid(final_results_dict,source_dict,'oclc')
        elif unicode_type(source_type) == SOURCE_TYPE_GOOGLE_BOOK_SEARCH:
            self.add_isbn_for_book(final_results_dict,source_dict)
        else:
            del final_results_dict
            return
    #-----------------------------------------------------------------------------------------
    def add_isni_lccn_for_viaf(self,final_results_dict):

        msg = 'LC is now adding ISNI and LCCN identifiers for VIAF'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        source_type = SOURCE_TYPE_VIAF

        if DEBUG: print("-------------------------------------------------------------------")
        if DEBUG: print("now adding isni and lccn for books with same viaf_author_id")
        if DEBUG: print("-------------------------------------------------------------------")

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            del final_results_dict
            return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
        #-----------------------------
        mysql = "SELECT book,val FROM identifiers WHERE type = ? "
        my_cursor.execute(mysql,([source_type]))
        book_type_list = my_cursor.fetchall()
        if not book_type_list:
            del final_results_dict
            return
        else:
            if len(book_type_list) == 0:
                del final_results_dict
                return
            else:
                book_type_list.sort()
        #-----------------------------
        my_cursor.execute("begin")
        #~ for k,v in final_results_dict.iteritems():
        for k,v in iteritems(final_results_dict):
            #k is the val for the identifier source_type   e.g.  "123456" for "viaf_author_id"
            #v is the list of other lists of other identifiers by other types to add for books having "123456" as a val for type k: "viaf_author_id":
            #       new_row1 = "isni",v,isni            v = 123456        new_type, key_type_val, new_type_val = new_row
            #       new_row2 = "lccn",v,lccn          v = 123456
            for row in v:
                new_type, key_type_val, new_type_val = row
                for item in book_type_list:   # all key_type_vals are for key_type == source_type per:  mysql = "SELECT book,val FROM identifiers WHERE type = ? "
                    book,val = item
                    if unicode_type(val) == unicode_type(key_type_val):      # if 123456 == 123456:
                        # add a new identifier for the current book with a type of new_type and a val of new_type_val
                        book = int(book)
                        mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,?,?)  "
                        my_cursor.execute(mysql,(None,book,new_type,new_type_val))
                        if DEBUG: print("new: ", new_type, " value: ", unicode_type(new_type_val), " for book: ", unicode_type(book), " with key_type_val of: ", key_type_val, " for key_type: ", source_type)
                    else:
                        continue
                #END FOR
            #END FOR
            msg = 'LC is now adding ISNI and LCCN identifiers for all books with a VIAF of: ' + unicode_type(k)
            self.gui.status_bar.show_message(msg)
            QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
        #END FOR
        my_cursor.execute("commit")
        #-----------------------------
        my_db.close()
        #-----------------------------
        del final_results_dict
    #-----------------------------------------------------------------------------------------
    def add_lcead_for_oclc(self,final_results_dict,final_list,source_dict):
        #~ final_results_dict[OCLC] = results_list
        #~ source_dict == oclc_other_dict where  oclc_other_dict[s_book] = OCLC

        msg = 'LC is now adding LCEAD values for OCLC'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        authors_additional_details_dict = {}

        #~ note:  source_dict is really oclc_other_dict ...
        #~ for k,v in source_dict.iteritems():
        for k,v in iteritems(source_dict):
            s_book = unicode_type(k)
            oclc = unicode_type(v)
            if oclc in final_results_dict:
                details_list = final_results_dict[oclc]  # BUT: details_list is  list, not a string, since is coming from the library codes webscraping api, not the classify_api...
                new_list = []
                for row in details_list:
                    source_literal,oclc,value = row
                    if unicode_type(source_literal) == unicode_type('lcead'):
                        #~ if DEBUG: print(source_literal,oclc,"  value to append: ", value)
                        new_list.append(value)
                #END FOR
                authors_additional_details_dict[s_book] = new_list     #~ authors_additional_details_dict[s_book] = authors additional details list
                del new_list
            else:
                continue
        #END FOR
        del final_results_dict
        del final_list
        del source_dict

        self.add_additional_attributes(authors_additional_details_dict)

        del authors_additional_details_dict
    #-----------------------------------------------------------------------------------------
    def add_loc_lccn_for_xid(self,final_results_dict,source_dict,source_id):
        #~ final_results_dict[oclc] = a list, containing LOC LCCN
        #~ source_dict == oclc_other_dict where  oclc_other_dict[s_book] = oclc (other)

        if not source_id == 'oclc':    #currently, only valid source id...
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            return error_dialog(self.gui, _('Convert ISBNs'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        if DEBUG: print("------------------------------------------------------------------------------------------")
        if DEBUG: print("now adding loc_lccn for each selected book using its oclc (other)")
        if DEBUG: print("------------------------------------------------------------------------------------------")

        msg = 'LC is now adding loc_lccn for each selected book using its oclc (other)'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        try:
            my_cursor.execute("begin")
            #~ for s_book,oclc in source_dict.iteritems():
            for s_book,oclc in iteritems(source_dict):
                if oclc in final_results_dict:
                    tmp_list = final_results_dict[oclc]
                    results_list_identifier_type = ""
                    for item in tmp_list:         # item = "loc_lccn",v,lccn   where v is oclc (other)
                        results_list_identifier_type,dummy,lccn = item
                        if unicode_type(results_list_identifier_type) == unicode_type("loc_lccn"):
                            break
                        else:
                            continue
                    #END FOR
                    if unicode_type(results_list_identifier_type) == "loc_lccn":
                        book = int(s_book)
                        new_type = "loc_lccn"
                        if DEBUG: print("new: ", new_type, " value: ", unicode_type(lccn), " for book: ", unicode_type(book), " with an oclc (other) of: ", unicode_type(oclc))
                        try:
                            mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,?,?)  "
                            my_cursor.execute(mysql,(None,book,new_type,lccn))
                        except:
                            continue
                    else:
                        continue
                else:
                    continue
            #END FOR
            my_cursor.execute("commit")
        except:
            pass

        my_db.close()

        if DEBUG: print("------------------------------------------------------------------------------------------")
    #-----------------------------------------------------------------------------------------
    def add_oclc_for_xid(self,final_results_dict,source_dict,source_id):
        #~ final_results_dict[oclc-owi] = a list, containing OCLC (other)
        #~ source_dict == oclc_owi_dict where  oclc_owi_dict[s_book] = oclc-owi

        if not source_id == 'owi':    #currently, only valid source id...
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            return error_dialog(self.gui, _('Convert ISBNs'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        if DEBUG: print("------------------------------------------------------------------------------------------")
        if DEBUG: print("now adding oclc (other) for each selected book using its isbn via its oclc-owi")
        if DEBUG: print("------------------------------------------------------------------------------------------")

        msg = 'LC is now adding oclc (other) for each selected book using its isbn via its oclc-owi'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
        try:
            my_cursor.execute("begin")
            #~ for s_book,oclc_owi in source_dict.iteritems():
            for s_book,oclc_owi in iteritems(source_dict):
                if oclc_owi in final_results_dict:
                    tmp_list = final_results_dict[oclc_owi]
                    results_list_identifier_type = ""
                    for item in tmp_list:         # item = "oclc",v,oclc (other)  where v is the book's oclc-owi
                        results_list_identifier_type,dummy,oclc = item
                        if unicode_type(results_list_identifier_type) == unicode_type("oclc"):
                            break
                        else:
                            continue
                    #END FOR
                    if unicode_type(results_list_identifier_type) == unicode_type("oclc"):
                        book = int(s_book)
                        new_type = "oclc"
                        if DEBUG: print("new: ", new_type, " value: ", unicode_type(oclc), " for book: ", unicode_type(book), " with an oclc-owi of: ", unicode_type(oclc_owi))
                        try:
                            mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,?,?)  "
                            my_cursor.execute(mysql,(None,book,new_type,oclc))
                        except:
                            continue
                    else:
                        continue
                else:
                    #~ if DEBUG: print("no results were found for book: ", s_book)
                    continue
            #END FOR
            my_cursor.execute("commit")
        except Exception as e:
            if DEBUG: print("Error: ", unicode_type(e))
            pass

        my_db.close()

        if DEBUG: print("------------------------------------------------------------------------------------------")
    #-----------------------------------------------------------------------------------------
    def delete_non_lc_identifiers(self):

        self.selected_books_list = self.get_selected_books()

        n = len(self.selected_books_list)
        if n == 0:
             return error_dialog(self.gui, _('Delete Non-Library Codes Identifiers'),_('You must select at least 1 book to perform this function. '), show=True)

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Delete Non-Library Codes Identifiers'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        #---------------------------------
        my_cursor.execute("begin")
        mysql = "DELETE FROM identifiers \
                                        WHERE (type != 'isbn') \
                                        AND (type != 'oclc-owi') \
                                        AND (type != 'issn') \
                                        AND (type != 'isni') \
                                        AND (type != 'lccn') \
                                        AND (type != 'loc_lccn') \
                                        AND (type != 'viaf_author_id') \
                                        AND (type != 'lc_authority_name') \
                                        AND (type != 'doi') \
                                        AND (type NOT LIKE 'z%') \
                                        AND (type != 'oclc') ;"
        my_cursor.execute(mysql)
        my_cursor.execute("commit")
        #---------------------------------

        my_db.close()

        self.force_refresh_of_cache(self.selected_books_list)

        self.mark_selected_books()

        del self.selected_books_list

        msg = 'LC has finished deleting non-Library Codes Identifiers for the selected books.'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
    #-----------------------------------------------------------------------------------------
    def retrieve_incremental_lcead_data(self):

        self.ddc_name = prefs['DDC'].replace("#","").strip()
        self.lcc_name = prefs['LCC'].replace("#","").strip()
        self.oclc_name = prefs['OCLC'].replace("#","").strip()

        if not prefs['OCLC_IDENTIFIER'] == unicode_type(S_TRUE):
            prefs['OCLC_IDENTIFIER'] = unicode_type(S_TRUE)
            prefs

        self.oclc_owi_identifier_is_desired = True

        #-------------------------------------
        # get selected books
        #-------------------------------------
        self.selected_books_list = self.get_selected_books()
        n_books = len(self.selected_books_list)
        if n_books == 0:
             return error_dialog(self.gui, _('Derive Library Codes'),_('No Books Were Selected.'), show=True)
        self.selected_books_list.sort()
        #-------------------------------------
        # process selected books
        #-------------------------------------
        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
             return error_dialog(self.gui, _('Derive Library Codes'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        oclc_owi_dict = self.get_oclc_owi_identifiers_for_selected_books(my_db,my_cursor)

        my_db.close()

        authors_additional_details_dict = {}
        param_dict = {}

        n_progress = 0
        for book in self.selected_books_list:
            s_book = unicode_type(book)
            n_book = int(book)
            try:
                n_progress = n_progress + 1
                msg = 'LC is Retrieving Incremental Extra Author Details:  ' + unicode_type(n_progress)
                self.gui.status_bar.show_message(msg)
                QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
                oclcowi = oclc_owi_dict[s_book]
                if oclcowi:
                    paramtype = "owi"
                    paramvalue = oclcowi
                    ddc, lcc, fast_list, owi, oclc_other, lc_authority_name, viaf_author_id, authors  = oclc_classify_api(paramtype,paramvalue,param_dict)
                    sleep(0)
                    if authors:
                        if authors != "NONE":
                            authors_additional_details_dict[s_book] = authors
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            except Exception as e:
                if DEBUG: print("Exception - Additional LCEAD: ", unicode_type(e))
                continue
        #END FOR

        if not len(authors_additional_details_dict) > 0:
            info_dialog(self.gui, "Library Codes", "No Incremental Extra Author Details Found for Selected Book(s).").show()
            return

        self.add_additional_attributes(authors_additional_details_dict)

        del authors_additional_details_dict

        self.force_refresh_of_cache(self.selected_books_list)

        self.mark_selected_books()

        del self.selected_books_list

        msg = 'LC: Completed Retrieving Incremental Extra Author Details.'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
    #-------------------------------------------------------------------------------------------------------------------------------------
    def find_alternatives_for_nonresponsive_isbn(self):
        # only a single selected book is allowed...

        self.guidb = self.gui.library_view.model().db

        self.selected_books_list = self.get_selected_books()
        n_books = len(self.selected_books_list)
        if n_books != 1:
             return error_dialog(self.gui, _('Derive Library Codes'),_('One (1) Book Must Be Selected; Cancelled. '), show=True)
        self.selected_books_list.sort()

        book = self.selected_books_list[0]
        book = int(book)

        mi = self.guidb.new_api.get_metadata(book)
        identifiers_dict = mi.get_identifiers()
        if 'isbn' in identifiers_dict:
            isbn_nonresponsive = identifiers_dict['isbn']
        else:
            del mi
            del identifiers_dict
            del self.selected_books_list
            return

        url = "https://books.google.com/books?isbn="

        url = url + isbn_nonresponsive

        if DEBUG: print("nonresponsive isbn url is : ", url)

        msg = "LC opening: " + url + "     Click 'More Editions' to find Alternative ISBNs "
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        try:
            if sys.platform == 'win32':
                os.startfile(url)
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', url])
            else:
                try:
                    subprocess.Popen(['xdg-open', url])
                except Exception as e:
                    if DEBUG: print("Exception opening web browser: ", url, "       ", unicode_type(e))
        except Exception as e:
            if DEBUG: print("Exception opening web browser: ", url, "       ", unicode_type(e))


        del mi
        del identifiers_dict
        del self.selected_books_list
        del url
        del isbn_nonresponsive
    #-------------------------------------------------------------------------------------------------------------------------------------
    def add_isbn_for_book(self,final_results_dict,source_dict):
        # source_dict:  k = n_book    v = "author||title"
        # final_results_dict["author||title"] = a list, containing isbn

        if len(final_results_dict) == 0:
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            return error_dialog(self.gui, _('Convert ISBNs'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        if DEBUG: print("------------------------------------------------------------------------------------------")
        if DEBUG: print("now adding new isbn for each selected book using its author/title")
        if DEBUG: print("------------------------------------------------------------------------------------------")

        msg = 'LC is now adding new isbn for each selected book using its author/title'
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...


        try:
            my_cursor.execute("begin")
            #~ for n_book,author_title in source_dict.iteritems():
            for n_book,author_title in iteritems(source_dict):
                if author_title in final_results_dict:
                    tmp_list = final_results_dict[author_title]
                    results_list_identifier_type = ""
                    for item in tmp_list:         # item = "isbn",v,isbn   where v is author_title
                        results_list_identifier_type,dummy,isbn = item
                        if unicode_type(results_list_identifier_type) == unicode_type("isbn"):
                            break
                        else:
                            continue
                    #END FOR
                    if unicode_type(results_list_identifier_type) == "isbn":
                        book = int(n_book)
                        new_type = "isbn"
                        author_title = author_title.replace("||"," ------ ")
                        if DEBUG: print("new: ", new_type, " value: ", unicode_type(isbn), " for book: ", unicode_type(book), " with an author/title of: ", author_title)
                        try:
                            mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (?,?,?,?)  "
                            my_cursor.execute(mysql,(None,book,new_type,isbn))
                        except:
                            continue
                    else:
                        continue
                else:
                    continue
            #END FOR
            my_cursor.execute("commit")
        except:
            pass

        my_db.close()

        if DEBUG: print("------------------------------------------------------------------------------------------")
    #-------------------------------------------------------------------------------------------------------------------------------------
    def extract_issn_from_pdf_control(self):

        self.selected_book_list = self.get_selected_books()

        if len(self.selected_book_list) == 0:
            return

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            return

        self.issn_results_dict = {}

        for current_book in self.selected_book_list:
            full_book_path = self.build_book_path(my_db,my_cursor,current_book,self.lib_path)
            if not full_book_path == "":
                msg = "Extracting ISSN for: " + full_book_path
                self.gui.status_bar.show_message(msg)
                QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...
                issn = self.pdf_control(full_book_path)
                if unicode_type("-") in unicode_type(issn):
                    self.issn_results_dict[current_book] = unicode_type(issn)
                else:
                    pass
                    #~ if DEBUG: print("issn not found for book: ", unicode_type(current_book))
            else:
                if DEBUG: print("full book path not found for book: ", unicode_type(current_book))
        #END FOR

        new_list = []

        if len(self.issn_results_dict) > 0:
            my_cursor.execute("begin")
            #~ for current_book,issn in self.issn_results_dict.iteritems():
            for current_book,issn in iteritems(self.issn_results_dict):
                current_book = int(current_book)
                mysql = "INSERT OR REPLACE INTO identifiers (id,book,type,val) VALUES (NULL,?,'issn',?)  "
                my_cursor.execute(mysql,(current_book,issn))
                new_list.append(current_book)
                if DEBUG: print("ISSN updated for: ", unicode_type(current_book), "  ", issn)
            #END FOR
            my_cursor.execute("commit")
            self.force_refresh_of_cache(new_list)
        else:
            pass

        my_db.close()

        n = len(self.issn_results_dict)
        msg = "LC: Extracting ISSNs from PDFs has Completed.  Updated: " + unicode_type(n)
        self.gui.status_bar.show_message(msg)
        QApplication.instance().processEvents()  #otherwise, status bar messages will never be shown...

        del self.issn_results_dict
        del self.selected_book_list
        del new_list
    #-------------------------------------------------------------------------------------------------------------------------------------
    def build_book_path(self,my_db,my_cursor,current_book,library_path):

        full_book_path = ""
        path_to_use = ""
        format_to_use = ""
        name = ""

        mysql = 'SELECT path FROM books WHERE id = ?'
        my_cursor.execute(mysql,([current_book]))
        tmp = my_cursor.fetchall()
        if not tmp:
            return full_book_path
        else:
            if len(tmp) == 0:
                return full_book_path
            else:
                for row in tmp:
                    for col in row:
                        path_to_use = col

        mysql = "SELECT format,name FROM data WHERE book = ? AND format = 'PDF' "
        my_cursor.execute(mysql,([current_book]))
        tmp = my_cursor.fetchall()
        if not tmp:
            pass
        else:
            if len(tmp) == 0:
                pass
            else:
                for row in tmp:
                    format_to_use,name = row
                    break
                del tmp

        if not format_to_use == "PDF":
            return full_book_path

        s_lower = format_to_use.lower()

        name = name + "." + s_lower

        path_to_use = os.path.join(path_to_use,name)

        full_book_path = os.path.join(library_path,path_to_use)

        full_book_path = full_book_path.replace(os.sep,"/")

        del path_to_use
        del name
        del s_lower

        return full_book_path
    #-------------------------------------------------------------------------------------------------------------------------------------
    def pdf_control(self,path):

        issn = ""

        path = path.replace(os.sep,"/")
        if isbytestring(path):
            path = path.decode(filesystem_encoding)

        issn = self.extract_pdf_issn(path)

        del path

        return issn
    #-------------------------------------------------------------------------------------------------------------------------------------
    def extract_pdf_issn(self,pdf_path):

        issn = ""
        pdf_html_ugly = []

        try:

            html_dir = pdftohtml_extract_pdf_issn(pdf_path)
            html_path = os.path.join(html_dir, 'index.html')

            with open(html_path, 'rb') as f:
                pdf_html_ugly = f.readlines()
            f.close()

            try:
                if os.isfile(html_path):
                    os.remove(html_path)
            except:
                pass

            try:
                del f
                del html_path
                del html_dir
                del pdf_path
            except:
                pass

            n = len(pdf_html_ugly)
            if DEBUG: print("Extraction of PDF HTML was successful; number of rows of text: ", unicode_type(n))

        except Exception as e:
            if DEBUG: print("Extraction of PDF HTML Failed using 'pdftohtml(os.getcwdu(), stream.name, options.no_images)': " + unicode_type(e))
            return issn

        sleep(0)
        is_in_next_row = False
        re1 = 'ISSN[:]*[ ]*[No.]*[ ]*[0-9][0-9][0-9][0-9][- ][0-9][0-9][0-9][0-9X]'
        p1 = re.compile(re1, re.IGNORECASE)
        re2 = '[0-9][0-9][0-9][0-9][- ][0-9][0-9][0-9][0-9X]'
        p2 = re.compile(re2, re.IGNORECASE)
        for row in pdf_html_ugly:
            r = unicode_type(row)
            if unicode_type("ISSN") in r or unicode_type("issn") in r or unicode_type("Issn") in r or is_in_next_row:
                r = unicode_type(r.replace("&#160;"," "))
                r = unicode_type(r.replace("<br>"," "))
                try:
                    if is_in_next_row:
                        match1 = p2.search(r)
                        is_in_next_row = False
                    else:
                        match1 = p1.search(r)
                    if match1:
                        is_in_next_row = False
                        s = match1.group(0)
                        issn = unicode_type(s)
                        #~ if DEBUG: print(issn)
                        issn = issn.upper()
                        issn = issn.replace("ISSN","")
                        issn = issn.replace(":","")
                        issn = issn.replace(" ","")
                        issn = issn.replace(";","")
                        issn = issn.replace("NO","")
                        issn = issn.replace(".","")
                        issn = issn.strip()
                        if len(issn) == 8:
                            p1 = issn[0:4]
                            p2 = issn[4: ]
                            issn = p1 + "-" + p2
                        break
                    else:
                        is_in_next_row = True
                except Exception as e:
                    if DEBUG: print("regex error: ", unicode_type(e))
                    continue
        #END FOR

        del pdf_html_ugly

        sleep(0)

        return issn
    #---------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------
    def update_genre_control(self):

        #~ for k,v in iteritems(prefs):
            #~ if DEBUG: print(unicode_type(k),unicode_type(v))

        if prefs['GENRE_IS_INACTIVE'] == unicode_type(S_TRUE):
            return
        if prefs['GENRE_DDC_IS_ACTIVE'] == unicode_type(S_FALSE) and prefs['GENRE_LCC_IS_ACTIVE'] == unicode_type(S_FALSE):
            return
        if not prefs['GENRE'].startswith("#"):
            return

        self.genre_label = prefs['GENRE']
        self.genre_label = self.genre_label[1: ]
        self.genre_label = self.genre_label.strip()
        if len(self.genre_label) == 0:
            return

        if prefs['GENRE_DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.lc_label = prefs['DDC']
        else:
            self.lc_label = prefs['LCC']

        if not self.lc_label.startswith("#"):
            return
        else:
            self.lc_label = self.lc_label[1: ]
            self.lc_label = self.lc_label.strip()
            if len(self.lc_label) == 0:
                return

        self.selected_books_list = self.get_selected_books()

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            return error_dialog(self.gui, _('Update Genre'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)

        self.create_lc_genre_mapping_table(my_db,my_cursor)   #only if not exists

        self.custom_column_id_genre,self.custom_column_id_library_code = self.get_custom_column_table(my_db,my_cursor)
        if self.custom_column_id_genre > '0' and self.custom_column_id_library_code > '0':
            self.lc_dict = self.get_library_codes_for_selected_books(my_db,my_cursor)
            if len(self.lc_dict) > 0:
                self.mapping_dict = self.get_mapping_table(my_db,my_cursor)
                if len(self.mapping_dict) > 0:
                    self.update_genres(my_db,my_cursor)
                    self.force_refresh_of_cache(self.selected_books_list)
                    self.mark_selected_books()

        my_db.close()

        del self.custom_column_id_genre
        del self.custom_column_id_library_code
        try:
            del self.lc_dict
            del self.mapping_dict
            del self.genre_dict
            del self.genre_set
        except:
            pass
        del self.selected_books_list
#-------------------------------------------------------------------------------------------------------------------------------------
    def update_genres(self,my_db,my_cursor):

        if prefs['GENRE_DDC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.ddc_match()
        elif prefs['GENRE_LCC_IS_ACTIVE'] == unicode_type(S_TRUE):
            self.lcc_match()
        else:
            return

        mysql = "INSERT OR IGNORE INTO custom_column_[N] (id,value) VALUES (null,?)"
        mysql = mysql.replace("[N]",self.custom_column_id_genre)
        my_cursor.execute("begin")
        for genre in self.genre_set:
            my_cursor.execute(mysql,([genre]))
        #END FOR
        my_cursor.execute("commit")

        mysql = "INSERT OR IGNORE INTO books_custom_column_[N]_link (id,book,value) VALUES (null,?,(SELECT id FROM custom_column_[N] WHERE value = ? AND value NOT NULL) )"
        mysql = mysql.replace("[N]",self.custom_column_id_genre)
        my_cursor.execute("begin")
        #~ for book,genre in self.genre_dict.iteritems():
        for book,genre in iteritems(self.genre_dict):
            my_cursor.execute(mysql,(book,genre))
        #END FOR
        my_cursor.execute("commit")
#-------------------------------------------------------------------------------------------------------------------------------------
    def ddc_match(self):

        self.genre_dict = {}
        self.genre_set = set()

        if prefs['GENRE_EXACT_MATCH'] == unicode_type(S_TRUE):
            use_exact_match = True
        else:
            use_exact_match = False

        #~ for book,lc in self.lc_dict.iteritems():
        for book,lc in iteritems(self.lc_dict):
            #~ if DEBUG: print("book,lc: ", unicode_type(book), lc)
            if lc in self.mapping_dict:
                genre = self.mapping_dict[lc]
                #~ if DEBUG: print("exact match: ", genre)
            else:
                if not use_exact_match:
                    #~ if DEBUG: print("not use_exact_match")
                    if lc.count(".") > 0:
                        do_while = True
                        #~ if DEBUG: print("original lc: ", lc)
                        while do_while:
                            lc = lc[0:-1]
                            if lc in self.mapping_dict:
                                genre = self.mapping_dict[lc]
                                do_while = False
                            else:
                                if lc.count(".") > 0:
                                    #~ if DEBUG: print("iterating: ", lc)
                                    pass
                                else:
                                    #on final shortening (e.g. 050. is now 050), but never shorten 050 to 05
                                    #~ if DEBUG: print("final shortening: ", lc)
                                    if lc in self.mapping_dict:
                                        genre = self.mapping_dict[lc]
                                    else:
                                        genre = ""
                                    do_while = False  #no matter what...
                        #END WHILE
                    else:
                        #~ if DEBUG: print("no decimal found in original lc")
                        genre = ""
                else:
                    #~ if DEBUG: print("exact match specified, so nothing done...")
                    genre = ""
            self.genre_dict[book] = genre
            self.genre_set.add(genre)
        #END FOR
#-------------------------------------------------------------------------------------------------------------------------------------
    def lcc_match(self):

        self.genre_dict = {}
        self.genre_set = set()

        n_max_match_length = int(prefs['GENRE_LCC_MATCH_LENGTH'])

        #~ for book,lc in self.lc_dict.iteritems():
        for book,lc in iteritems(self.lc_dict):
            lc = lc.strip()
            if len(lc) == 0:
                continue
            lc = lc.upper()
            if len(lc) > n_max_match_length:
                lc = lc[0:n_max_match_length]
            #~ if DEBUG: print("book,lc: ", unicode_type(book), lc)
            if lc in self.mapping_dict:
                genre = self.mapping_dict[lc]
                #~ if DEBUG: print("[1] match found: ", genre)
            else:
                if len(lc) == 2:
                    if lc[0].isalpha():
                        if lc[1].isdigit():
                            lc = lc[0]
                            if lc in self.mapping_dict:
                                genre = self.mapping_dict[lc]
                                #~ if DEBUG: print("[2] match found: ", genre)
                            else:
                                genre = ""
                        else:
                            genre = ""
                    else:
                        genre = ""
                else:
                    genre = ""
            self.genre_dict[book] = genre
            self.genre_set.add(genre)
        #END FOR
#-------------------------------------------------------------------------------------------------------------------------------------
    def get_mapping_table(self,my_db,my_cursor):

        self.mapping_dict = {}

        mysql = "SELECT library_code,genre FROM _lc_genre_mapping WHERE genre NOT NULL"
        my_cursor.execute(mysql)
        tmp_rows = my_cursor.fetchall()
        if not tmp_rows:
            tmp_rows = []
        for row in tmp_rows:
            library_code,genre = row
            if library_code:
                if genre:
                    library_code = library_code.upper()
                    self.mapping_dict[library_code] = genre
        #END FOR

        del tmp_rows

        return self.mapping_dict
#-------------------------------------------------------------------------------------------------------------------------------------
    def get_library_codes_for_selected_books(self,my_db,my_cursor):

        self.lc_dict = {}

        mysql = "SELECT id,value FROM custom_column_[N] WHERE id = (SELECT value FROM books_custom_column_[N]_link WHERE book = ?)"
        mysql = mysql.replace("[N]",self.custom_column_id_library_code)
        for book in self.selected_books_list:
            my_cursor.execute(mysql,([book]))
            tmp_rows = my_cursor.fetchall()
            if not tmp_rows:
                tmp_rows = []
            for row in tmp_rows:
                id,value = row
                if id:
                    if value:
                        self.lc_dict[book] = value
            #END FOR
            del tmp_rows
        #END FOR

        return self.lc_dict
#-------------------------------------------------------------------------------------------------------------------------------------
    def get_custom_column_table(self,my_db,my_cursor):

        self.custom_column_id_genre = 0
        self.custom_column_id_library_code = 0

        mysql = "SELECT id,label FROM custom_columns WHERE datatype = 'text' AND normalized = 1"
        my_cursor.execute(mysql)
        tmp_rows = my_cursor.fetchall()
        if not tmp_rows:
            tmp_rows = []
        for row in tmp_rows:
            id,label = row
            if unicode_type(label) == unicode_type(self.genre_label):
                self.custom_column_id_genre = unicode_type(id)
            if unicode_type(label) == unicode_type(self.lc_label):
                self.custom_column_id_library_code = unicode_type(id)
        #END FOR

        del tmp_rows

        return self.custom_column_id_genre,self.custom_column_id_library_code
#-------------------------------------------------------------------------------------------------------------------------------------
    def create_lc_genre_mapping_table(self,my_db,my_cursor):

        try:
            my_cursor.execute("begin")
            mysql = "CREATE TABLE  _lc_genre_mapping (library_code TEXT PRIMARY KEY  NOT NULL  UNIQUE , genre TEXT DEFAULT TBD)"
            my_cursor.execute(mysql)
            my_cursor.execute("commit")
        except Exception as e:
            try:
                my_cursor.execute("commit")
            except Exception as e:
                pass
            #~ if DEBUG: print("[1] already created and seeded; continuing normally: ",unicode_type(e))
            return  # already seeded...

        # seed the table
        from calibre_plugins.library_codes.library_codes_genre_mapping import return_lc_genre_mapping_table_mysql
        mysql = return_lc_genre_mapping_table_mysql()

        try:
            my_cursor.execute(mysql)
        except Exception as e:
            if DEBUG: print("[2]",unicode_type(e))
            try:
                my_cursor.execute("commit")
            except Exception as e:
                pass
#-------------------------------------------------------------------------------------------------------------------------------------
    def import_csv_mappings(self):

        if prefs['GENRE_IS_INACTIVE'] == unicode_type(S_TRUE):
            info_dialog(self.gui, 'ERROR','LC has not (yet) been configured and activated for this function; Execution canceled.').show()
            return

        chosen_files = self.choose_csv_file_to_import()
        if not chosen_files:
            info_dialog(self.gui, 'Canceled','No CSV File was was selected; Execution canceled.').show()
            return
        else:
            csv_path = chosen_files[0]

        csv_mappings_list = self.import_csv_file(csv_path)
        if not len(csv_mappings_list) > 0:
            if DEBUG: print("CSV File was empty.  Nothing done.")
            return
        is_valid,n_total = self.add_csv_mappings(csv_mappings_list)
        if not is_valid:
            info_dialog(self.gui, 'Failed to Import CSV File','Nothing was imported due to errors.').show()
        else:
            msg = 'CSV File rows imported and added to (or changed in) the mapping table: ' + unicode_type(n_total)
            info_dialog(self.gui, 'Success Importing CSV File',msg).show()

        del chosen_files
        del csv_mappings_list
#-------------------------------------------------------------------------------------------------------------------------------------
    def choose_csv_file_to_import(self):

        name = "choose_mappings_csv_file"
        title = "Choose Mapping Table CSV File"
        all_files=True
        select_only_single_file=True
        filters=[]
        window = None   # parent = None

        mode = QFileDialog.ExistingFile if select_only_single_file else QFileDialog.ExistingFiles
        fd = FileDialog(title=title, name=name, filters=filters, parent=window, add_all_files_filter=all_files, mode=mode)
        fd.setParent(None)
        if fd.accepted:
            return fd.get_files()
        return None
#---------------------------------------------------------------------------------------------------------------------------------------------
    def import_csv_file(self,csv_path):

        tmp_list = []
        csv_mappings_list  = []

        if DEBUG: print("CSV File path: " + csv_path)

        if csv_path == unicode_type(""):
            return csv_mappings_list

        try:
            with open (csv_path,'rb') as csvfile:
                lc_csv_reader = csv.reader(csvfile,dialect='excel')
                for row in lc_csv_reader:
                    tmp_list.append(row)
                #END FOR
            csvfile.close()
            del csv_path
            del lc_csv_reader
            for row in tmp_list:
                if isinstance(row,list):
                    csv_mappings_list.append(row)
                elif isinstance(row,unicode_type):
                    pass
        except Exception as e:
            if DEBUG: print("CSV File Error: " + unicode_type(e))
            error_dialog(self.gui, _('CSV File Error'),_(e), show=True)

        return csv_mappings_list
#---------------------------------------------------------------------------------------------------------------------------------------------
    def add_csv_mappings(self,csv_mappings_list):

        is_valid = False

        n_total_csv_mappings_to_add = len(csv_mappings_list)

        if DEBUG: print("Number of mappings in the specified CSV file: " + unicode_type(n_total_csv_mappings_to_add))

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            error_dialog(self.gui, _('Update Genre'),_('Database Connection Error.  Cannot Connect to the Current Library.'), show=True)
            return is_valid,0

        self.create_lc_genre_mapping_table(my_db,my_cursor)

        my_cursor.execute("begin")
        i = 0
        n_total = 0
        for row in csv_mappings_list:        # row = ['"811.56","Fiction - 21st Century"']
            try:
                #~ if DEBUG: print("raw csv row: " + unicode_type(row))
                library_code,genre = row
            except Exception as e:
                if DEBUG: print("library_code,genre = row in csv file error.  invalid csv file format and/or data: " + unicode_type(e))
                msg = "library_code,genre = row in csv file error.  invalid csv file format and/or data: " + unicode_type(e)
                error_dialog(self.gui, _('CSV data error for mapping'),_(msg), show=True)
                break
            try:
                if library_code:
                    library_code = unicode_type(library_code)
                    library_code = library_code.replace('"',"")
                    library_code = library_code.replace("'","")
                    library_code = library_code.strip()
                    if genre:
                        try:
                            genre = as_unicode(genre, encoding='utf-8', errors='replace') # if bytes, decodes, else returns as unique_type, which returns the original if already unicode
                        except Exception as e:
                            if DEBUG: print("utf-8 decode error: ", unicode_type(e))
                        genre = genre.strip()
                        if genre != '':
                            mysql = "INSERT OR REPLACE INTO _lc_genre_mapping (library_code,genre) VALUES (?,?)"
                            my_cursor.execute(mysql,(library_code,genre))
                            #~ if DEBUG: print("added or replaced: " + library_code + "   " + genre)
                            n_total = n_total + 1
                            i = i + 1
                            if i >= 100:
                                my_cursor.execute("commit")
                                my_cursor.execute("begin")
                                i = 0
                            else:
                                continue
            except Exception as e:
                if DEBUG: print("CSV data error for mapping: " + library_code + " --- " + genre + " with the reason: " + unicode_type(e) )
                msg = "CSV data error for mapping: " + library_code + " --- " + genre + " with the reason: " + unicode_type(e)
                error_dialog(self.gui, _('CSV data error for mapping'),_(msg), show=True)
                break
        #END FOR
        try:
            my_cursor.execute("commit")
        except:
            pass

        my_db.close()

        del csv_mappings_list

        is_valid = True

        return is_valid,n_total
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    def ddc_pie_chart_1(self):
        self.show_ddc_pie_chart(1)
    def ddc_pie_chart_2(self):
        self.show_ddc_pie_chart(2)
    def show_ddc_pie_chart(self,type):

        my_db,my_cursor,is_valid = self.apsw_connect_to_library()
        if not is_valid:
            return

        self.ddc_name = prefs['DDC'].replace("#","").strip()

        #-----------------------------
        #before anything else, ensure that the ddc custom column exists in this library...
        self.ddc_name = self.ddc_name.replace("#","")
        mysql = "SELECT id,label FROM custom_columns WHERE label = ? and normalized = 1 and datatype = 'text' "
        my_cursor.execute(mysql,([self.ddc_name]))
        tmp_rows= my_cursor.fetchall()
        if not tmp_rows:
            tmp_rows = []
        if len(tmp_rows) == 0:
            my_db.close()
            if DEBUG: print("ddc has not been configured as a proper custom column in this library")
            return
        for row in tmp_rows:
            id,dummy = row
        #END FOR
        del tmp_rows
        s_id = unicode_type(id)
        s_id = s_id.strip()
        #-----------------------------
        mysql = "SELECT count(book) AS number,(SELECT substr(value,1,[L]) FROM custom_column_[N] WHERE id = books_custom_column_[N]_link.value) AS ddc \
                        FROM books_custom_column_[N]_link  GROUP BY ddc ORDER BY number DESC, ddc ASC "
        if type == 1:
            mysql = mysql.replace("[L]","2")
        else:
            mysql = mysql.replace("[L]","3")
        mysql = mysql.replace("[N]",s_id)
        my_cursor.execute(mysql)
        tmp_rows= my_cursor.fetchall()
        my_db.close()
        if not tmp_rows:
            tmp_rows = []
        if len(tmp_rows) == 0:
            if DEBUG: print("DDC has not been populated in this library.  Nothing to show.")
            return

        from calibre_plugins.library_codes.qpainter_charts import Chart, PieChart, Viewer, DialogViewer, DataTable

        table = DataTable()
        table.addColumn('DDC')
        table.addColumn('Count')
        i = 0
        for row in tmp_rows:
            n_count,ddc = row
            if i < 20:
                table.addRow([ddc,n_count])
                i = i + 1
            else:
                break
        #END FOR
        del tmp_rows
        #-----------------------------

        chart = PieChart(table)

        view = DialogViewer()
        view.setGraph(chart)

        if type == 1:
            view.setWindowTitle('DDC Top 20 [NN]')
        else:
            view.setWindowTitle('DDC Top 20 [NNN]')

        view.resize(480, 360)

        view.exec_()

        try:
            del table
            del chart
            del view
        except:
            pass

    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#END of ui.py