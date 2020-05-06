# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

#~ For Calibre 3.41.3 & later, extract_pdf_issn was totally rewritten.

import errno
import os
import re
import shutil
import subprocess
import sys

from calibre import CurrentDir, replace_entities, prints
from calibre.constants import (
    filesystem_encoding, isbsd, islinux, isosx, ispy3, iswindows
)
from calibre.ebooks import ConversionError, DRMError
from calibre.ebooks.chardet import xml_to_unicode
from calibre.ptempfile import PersistentTemporaryFile
from calibre.utils.cleantext import clean_xml_chars
from calibre.utils.ipc import eintr_retry_call

from calibre.constants import DEBUG
from calibre.ebooks.pdf.pdftohtml import PDFTOHTML, popen, pdftohtml, parse_outline, flip_image, flip_images
from calibre.ptempfile import base_dir

def pdftohtml_extract_pdf_issn(pdf_path):
    output_dir= base_dir()
    output_dir = output_dir.replace(os.sep,'/')
    if DEBUG: print("Current output working directory ( output_dir= base_dir() ) for temporary files is: ", output_dir)
    pdftohtml(output_dir, pdf_path, no_images=True, as_xml = False)
    return output_dir
#~ ---------------------------------------------------------------------------------------------------------------------------


