# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

from calibre.customize import InterfaceActionBase

class ActionBaseLibraryCodes(InterfaceActionBase):

    name                    = 'Library Codes'
    description           = "Derive Library of Congress Codes, Dewey Decimal Codes, and/or OCLC-OWI plus Other Identifiers for Selected Books Using ISBN or ISSN or Author/Title"
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = 'DaltonST'
    version                 = (1, 0, 42)
    minimum_calibre_version = (4, 6, 0)

    actual_plugin           = 'calibre_plugins.library_codes.ui:ActionLibraryCodes'

    gui_name = 'Library Codes'

    #--------------------------------------------------------------------------------------------------------------------------
    def initialize(self):
        pass
    #--------------------------------------------------------------------------------------------------------------------------
    def is_customizable(self):
        return True
    #--------------------------------------------------------------------------------------------------------------------------
    def config_widget(self):
        from calibre_plugins.library_codes.config import ConfigWidget
        return ConfigWidget()
    #--------------------------------------------------------------------------------------------------------------------------
    def save_settings(self, ConfigWidget):
        ConfigWidget.save_settings()
        # Apply the changes
        ac = self.actual_plugin_
        if ac is not None:
            ac.apply_settings()
    #-------------------------------------------
#END of __init__py