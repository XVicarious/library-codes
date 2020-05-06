# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

from calibre.constants import DEBUG, iswindows
from calibre.db.legacy import LibraryDatabase
from calibre.utils.config import prefs

from polyglot.builtins import as_unicode

#-----------------------------------------------------------------------------------------
def lc_cli_add_custom_column(guidb,param, dbpath):

    #~ param = --is-multiple + '|||' + label + '|||' + name + '|||' +  datatype
    #~ param = label + '|||' + name + '|||' +  datatype

    if "is-multiple" in param:
        is_multiple = True
        param = param.replace("--is-multiple|||","")
    else:
        is_multiple = False

    if DEBUG: print("final param:", param)

    param = param.strip()
    args = param.split("|||")
    args_list = []
    for row in args:
        s = row.strip()
        if s > " ":
            s = s.replace('"','')
            args_list.append(s)
            if DEBUG: print("arg: ", as_unicode(s))
    #END FOR

    label = args_list[0]
    name = args_list[1]
    datatype = args_list[2]

    display  = {}

    db = LibraryDatabase(dbpath)

    db.create_custom_column(label, name, datatype, is_multiple, display=display)

    if DEBUG: print("Custom column created:  ", label, "  ", name, "  ", datatype)

    # Re-open the DB so that  field_metadata reflects the column changes
    guidb.prefs['field_metadata'] = db.field_metadata.all_metadata()

    #~ if DEBUG:
        #~ s = guidb.prefs['field_metadata']
        #~ print("new guidb field_metadata: ", as_unicode(s))

    send_rc_message('')

#-----------------------------------------------------------------------------------------
def send_rc_message(msg):

    from calibre.utils.ipc import RC
    t = RC(print_error=False)
    t.start()
    t.join(3)
    if t.done:
        t.conn.send('refreshdb:'+msg)
        t.conn.close()

    if DEBUG: print('Calibre has been notified of the change...')
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
#END of lc_cli.py
