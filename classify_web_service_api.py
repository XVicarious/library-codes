# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

#~ ---------------------------
#~ original OCLC api.py heavily modified by DaltonST in 2015 (and for FAST in 2018) (and for Python 3 in 2019) for use in Calibre's 'Library Codes' plugin...
#~ ---------------------------
#~ FAST added 2018-10 by DaltonST
#~ ---------------------------

#~ py2:   import sys, BaseHTTPServer, urllib, urlparse, xml.dom.pulldom, xml.dom.minidom, cgi, socket, xml.sax.saxutils, StringIO, string, codecs, time, datetime, os
#~ py2:   from urllib import urlencode
#~ py3:   urlencode, urlopen changed

import sys, os
import xml.dom.pulldom, xml.dom.minidom, xml.sax.saxutils     # supposedly portable between Python 2 and Python 3
import time, datetime
from time import sleep        # Added by DaltonST
import socket                       # Added by DaltonST
timeout = 5.0                        # Added by DaltonST
socket.setdefaulttimeout(timeout)        # Added by DaltonST, since default is 'no timeout'...

from calibre.constants import DEBUG  # Added by DaltonST

from polyglot.builtins import is_py3, unicode_type     # Added by DaltonST
from polyglot.io import PolyglotStringIO                    # Added by DaltonST
if is_py3:
    from urllib.request import urlopen
    from urllib.parse import urlencode  #, urlparse
else:
    from urllib import urlencode
    from urllib2 import urlopen

myurlencode = urlencode
myurlopen = urlopen

#------------------------------------------------------------------------------------------------------
def oclc_classify_api(paramtype,paramvalue,param_dict):
    #http://classify.oclc.org/classify2/api_docs/index.html
    #http://classify.oclc.org/classify2/api_docs/classifySample.py
    # Usage: python classifySample.py <param-type> <param-value>
    # or, use stdnbr instead of isbn so it will search for any standard number (isbn, issn, upc, etc.)

    parmType = paramtype
    parmValue = paramvalue
    #~ ---------------------------
    summaryInd = 'false'          #FAST requires detail, not summary.  all else uses summary just fine.
    #~ ---------------------------

    if len(param_dict) > 0:   # Added by DaltonST
        use_dict = True
    else:
        use_dict = False

    ddc_return = "NONE"
    lcc_return = "NONE"
    owi_return = "NONE"                              # Added by DaltonST      oclc-owi
    oclc_other_return  = "NONE"                  # Added by DaltonST
    lc_authority_name_return = "NONE"      # Added by DaltonST
    viaf_author_id_return = "NONE"             # Added by DaltonST
    author_extras_return_list = []                  # Added by DaltonST
    authors_return = "NONE"                       # Added by DaltonST
    #~ ---------------------------
    fast_return_list = []                                 # Added by DaltonST
    #~ ---------------------------

    if DEBUG: print('in api:   Searching for: ' + parmType + '=' + parmValue)

    base = 'http://classify.oclc.org/classify2/Classify?'
    #~ summaryBase = '&summary=true'              # Added by DaltonST
    summaryBase = '&summary=false                   '#FAST requires detail, not summary.  all else uses summary just fine.

    #------------------------------------------
    def getText(nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc
    #------------------------------------------
    def iterate_work_values(xdoc_object):       # Added by DaltonST
        # for Multi-work Responses only; for Books only (not Audiobooks or other media types).
        index = 0
        while True:
            try:
                work = xdoc_object.getElementsByTagName('work')[index]
                if work:
                    format = work.attributes["format"].value
                    if unicode_type(format) == unicode_type("Book"):
                        break
                    else:
                        index = index + 1
                        continue
                else:
                    index = index + 1
                    continue
            except:
                return None
        #END DO
        return work
    #------------------------------------------

    xdoc = ''
    try:       # Modified by DaltonST
        if not use_dict:   # Derive from ISBN
            nextURL = base + myurlencode({parmType:parmValue.encode('utf-8')}) + summaryBase
        else:   # Derive from Author & Title
            nextURL = base + myurlencode(param_dict) + summaryBase
        if DEBUG: print(nextURL)
        #~ urlobj = urllib.urlopen(nextURL)
        urlobj = myurlopen(nextURL)
        response = urlobj.read()
        urlobj.close()
        sleep(0)  # Added by DaltonST
        del urlobj  # Added by DaltonST
        xdoc = xml.dom.minidom.parseString(response)
    #~ except UnicodeDecodeError:          # Modified by DaltonST
        #~ if DEBUG: print('UnicodeDecodeError: ' + nextURL)         # Modified by DaltonST
    #~ except IOError:     # Modified by DaltonST
    except Exception as e:
        if DEBUG: print('Connection Error: ' + unicode_type(e))                                                                                                               # Modified by DaltonST
        if DEBUG: print("Likely inability to connect to the Internet.  Verify network connection and retry.")        # Added by DaltonST
        if DEBUG: print("Error: returning from api:  ", ddc_return, lcc_return, unicode_type(owi_return))     # Added by DaltonST
        return ddc_return, lcc_return, fast_return_list, owi_return, oclc_other_return, lc_authority_name_return, viaf_author_id_return, author_extras_return_list   # Added by DaltonST

    response = xdoc.getElementsByTagName('response')[0]
    respCode = response.attributes["code"].value
    if DEBUG: print('Method response: ' + respCode)
    if DEBUG: print("---------------------------------------------------------------------------------------------------")
    if respCode == '0' or respCode == '2':
        recommendations = xdoc.getElementsByTagName('recommendations')[0]
        if recommendations:
            try:
                #~ ---------------------------
                ddc = recommendations.getElementsByTagName('ddc')[0]
                #~ ---------------------------
                if ddc:
                    for mostPopular in ddc.getElementsByTagName('mostPopular'):
                        holdings = mostPopular.attributes["holdings"].value
                        nsfa = mostPopular.attributes["nsfa"].value
                        sfa = mostPopular.attributes["sfa"].value
                        if DEBUG: print('DDC mostPopular: class=' + sfa + ' normalized=' + nsfa + ' holdings=' + holdings)
                        ddc_return = sfa
                        break
                    del ddc
                    del holdings
            except Exception as e:
                if DEBUG: print("ddc = recommendations.....failure:  ",unicode_type(e))
                pass

            try:
                #~ ---------------------------
                lcc = recommendations.getElementsByTagName('lcc')[0]
                #~ ---------------------------
                if lcc:
                    for mostPopular in lcc.getElementsByTagName('mostPopular'):
                        holdings = mostPopular.attributes["holdings"].value
                        nsfa = mostPopular.attributes["nsfa"].value
                        sfa = mostPopular.attributes["sfa"].value
                        if DEBUG: print('LCC mostPopular: class=' + sfa + ' normalized=' + nsfa + ' holdings=' + holdings)
                        lcc_return = sfa
                        break
                    del lcc
                    del holdings
            except Exception as e:
                if DEBUG: print("lcc = recommendations.....failure:  ",unicode_type(e))
                pass

            try:
                #~ ---------------------------
                fast = recommendations.getElementsByTagName('fast')[0]
                #~ ---------------------------
                if fast:
                    for heading in fast.getElementsByTagName('heading'):
                        #~ <heading heldby="3094" ident="1107958" src="fast">Schools</heading>
                        #~ <heading heldby="3094" ident="1728849" src="fast">Families</heading>
                        for child in heading.childNodes:
                            name = child.nodeValue
                            if DEBUG: print("FAST name: ", name)
                            fast_return_list.append(name)
                    del fast
            except Exception as e:
                if DEBUG: print("fast = recommendations.....failure:  ",unicode_type(e))
                pass

        del recommendations
        #--------------------------------------------------------
        # added by DaltonST so as to return oclc-owi etc.
        #--------------------------------------------------------
        try:
            work = xdoc.getElementsByTagName('work')[0]
            if work:
                try:
                    y = work.childNodes[0];       #http://www.w3schools.com/xml/dom_nodes_get.asp
                    z = y.nodeValue
                    z = unicode_type(z)
                    z = z.strip()
                    if z.isdigit():
                        if len(z) > 5:
                            oclc_other_return = z
                    if DEBUG: print("oclc-other is: ", unicode_type(oclc_other_return))
                except:
                    if DEBUG: print("oclc-other is: ", unicode_type(oclc_other_return))
                    pass
                author = work.attributes["author"].value
                authors_return = author
                author_extras_return_list.append(author)   # this list is added to the proper dict down below; just happens to be available here.
                title = work.attributes["title"].value
                try:
                    if DEBUG: print("author(s): ", unicode_type(author))
                    if DEBUG: print("title: ", unicode_type(title))
                except:
                    pass
                owi = work.attributes["owi"].value
                owi_return = owi
                if DEBUG: print("oclc-owi: ", unicode_type(owi))
                if DEBUG: print("---------------------------------------------------------------------------------------------------")
                del author
                del title
                del work
                del owi
            else:
                pass
        except:
            pass
        #--------------------------------------------------------
        # added by DaltonST so as to return Author Details
            #~ <authors>
                #~ <author lc="n79122680" viaf="56617645">Warhol, Andy, 1928-1987</author>
                #~ <author lc="n79122507" viaf="14896823">Hackett, Pat [Editor; Other; Author of introduction]</author>
            #~ </authors>
        #--------------------------------------------------------
        try:
            authors = xdoc.getElementsByTagName('authors')[0]
            if authors:
                for author in authors.getElementsByTagName('author'):
                    lc_authority_name_return = author.attributes["lc"].value
                    viaf_author_id_return = author.attributes["viaf"].value
                    break
                #END FOR
                del authors
                del author
                if DEBUG: print("Author Details: LOC Authority Name: ", lc_authority_name_return, " VIAF Author ID: ", viaf_author_id_return, "Author: ", authors_return)
                del authors_return
        except Exception as e:
            if DEBUG: print("Author Details Exception: ", unicode_type(e), "  (Index Out Of Range means No Data to be Retrieved)")
        #--------------------------------------------------------
        #--------------------------------------------------------
        #--------------------------------------------------------
        #--------------------------------------------------------
        #--------------------------------------------------------
    else:
        if respCode == '4':    # Multi-work response; should be sorted ascending by holdings per my parameters above.
            if DEBUG: print("Multi-work Response")
            #~ <work author="Asimov, Isaac, 1920-1992" editions="322" format="Book" holdings="7747" hyr="2013" itemtype="itemtype-book" lyr="0954" owi="15633154" title="I, robot" wi="10219687"/>
            #~ <work author="Asimov, Isaac, 1920-1992" editions="351" format="Book" holdings="7304" hyr="2015" itemtype="itemtype-book" lyr="1951" owi="19936192" title="Foundation" wi="10041061"/>
            #~ <work author="Asimov, Isaac, 1920-1992 | Pukallus, Horst, 1949- [Translator]" editions="180" format="Book" holdings="4653" hyr="2015" itemtype="itemtype-book" lyr="1982" owi="21029180" title="Foundation's edge" wi="10217376"/>
            #~ <work author="Asimov, Isaac, 1920-1992" editions="227" format="Book" holdings="4182" hyr="2013" itemtype="itemtype-book" lyr="1952" owi="46661001" title="Foundation and empire" wi="123060114"/>
            #~ <work author="Asimov, Isaac, 1920-1992" editions="228" format="Book" holdings="4035" hyr="2014" itemtype="itemtype-book" lyr="1949" owi="13590044" title="Second foundation." wi="1007020"/>
            try:     # Modified by DaltonST
                #~ work = xdoc.getElementsByTagName('work')[0]
                work = iterate_work_values(xdoc)
                if work:
                    try:
                        y = work.childNodes[0];       #http://www.w3schools.com/xml/dom_nodes_get.asp
                        z = y.nodeValue
                        z = unicode_type(z)
                        z = z.strip()
                        if z.isdigit():
                            if len(z) > 5:
                                oclc_other_return = z
                        if DEBUG: print("oclc-other is: ", unicode_type(oclc_other_return))
                    except:
                        if DEBUG: print("oclc-other is: ", unicode_type(oclc_other_return))
                        pass
                    author = work.attributes["author"].value
                    authors_return = author
                    author_extras_return_list.append(author)
                    title = work.attributes["title"].value
                    try:
                        if DEBUG: print("author(s): ", unicode_type(author))
                        if DEBUG: print("title: ", unicode_type(title))
                    except:
                        pass
                    owi = work.attributes["owi"].value
                    owi_return = owi
                    if DEBUG: print("Multi-work Response:  oclc-owi: ", unicode_type(owi))
                    if DEBUG: print("---------------------------------------------------------------------------------------------------")
                    del work
                    del author
                    del title
                    del owi
                else:
                    pass
            except:
                pass
            #--------------------------------------------------------
            # added by DaltonST so as to return Author Details
                #~ <authors>
                    #~ <author lc="n79122680" viaf="56617645">Warhol, Andy, 1928-1987</author>
                    #~ <author lc="n79122507" viaf="14896823">Hackett, Pat [Editor; Other; Author of introduction]</author>
                #~ </authors>
            #--------------------------------------------------------
            try:
                authors = xdoc.getElementsByTagName('authors')[0]
                if authors:
                    for author in authors.getElementsByTagName('author'):
                        lc_authority_name_return = author.attributes["lc"].value
                        viaf_author_id_return = author.attributes["viaf"].value
                        break
                    #END FOR
                    del authors
                    del author
                    if DEBUG: print("Author Details: LOC Authority Name: ", lc_authority_name_return, " VIAF Author ID: ", viaf_author_id_return, "Author: ", authors_return)
            except Exception as e:
                if DEBUG: print("Author Details Exception: ", unicode_type(e), "  (Index Out Of Range means No Data to be Retrieved)")
                pass
            #--------------------------------------------------------
            #--------------------------------------------------------
        else:  # respCode is an error code...
            pass

    xdoc.unlink()            # Added by DaltonST
    del xdoc                   # Added by DaltonST
    del response            # Added by DaltonST


    if DEBUG: print("returning from api:  ", ddc_return, lcc_return, unicode_type(fast_return_list), unicode_type(owi_return), unicode_type(oclc_other_return), unicode_type(lc_authority_name_return), unicode_type(viaf_author_id_return) )   # Added by DaltonST

    return ddc_return, lcc_return, fast_return_list, owi_return, oclc_other_return, lc_authority_name_return, viaf_author_id_return, author_extras_return_list   # Heavily Modified by DaltonST


#------------------------------------------------------------------------------------------------------
# example results returned and parsed using the api:
#------------------------------------------------------------------------------------------------------
'''
<?xml version="1.0" encoding="UTF-8"?>
<classify xmlns="http://classify.oclc.org">
  <response code="0"/>
  <!--Classify is a product of OCLC Online Computer Library Center: http://classify.oclc.org-->
  <work author="McGee, Harold | McGee, Harold [Author] | Cai, Chengzhi | Lin, Huizhen | Qiu, Wenbao | Ibeas Delgado, Juan Manuel," editions="74" eholdings="6" format="Book" holdings="3460" itemtype="itemtype-book" owi="572969" title="On food and cooking : the science and lore of the kitchen">10711863</work>
  <authors>
    <author lc="null" viaf="211226544">Lin, Huizhen</author>
    <author lc="n83311533" viaf="71503302">McGee, Harold [Author]</author>
    <author lc="no2008059459" viaf="14578435">Cai, Chengzhi</author>
  </authors>
  <orderBy>hold desc</orderBy>
  <input type="isbn">9780684843285</input>
  <recommendations>
    <ddc>
      <mostPopular holdings="3191" nsfa="641.5" sfa="641.5"/>
      <mostRecent holdings="3191" sfa="641.5"/>
      <latestEdition holdings="1" sf2="22" sfa="641"/>
      <latestEdition holdings="1626" sf2="22" sfa="641.5"/>
    </ddc>
    <lcc>
      <mostPopular holdings="3249" nsfa="TX651" sfa="TX651"/>
      <mostRecent holdings="3249" sfa="TX651"/>
    </lcc>
  </recommendations>
</classify>
'''
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#END OF classify_web_service_api.py