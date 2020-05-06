# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

import re
import socket
socket.setdefaulttimeout(15)

#~ from calibre_plugins.library_codes.beautifulsoup3 import BeautifulSoup     #v1.0.39 bs3 method names do not have the bs4 '_' in the middle:  findAll  instead of find_all
from calibre.ebooks.BeautifulSoup import BeautifulSoup                                # v1.0.39  based on bs attributes, use Standard Calibre's bs3 .findAll or bs4 .find_all
from calibre.constants import DEBUG

from polyglot.builtins import is_py3, iteritems, unicode_type

#~ import urllib
if is_py3:
    from urllib.request import urlopen
    #~ urlopen = urllib.request.urlopen
else:
    from urllib2 import urlopen
myurlopen = urlopen

SOURCE_TYPE_VIAF = unicode_type("viaf_author_id")
SOURCE_TYPE_OCLC = unicode_type("www.worldcat.org/oclc")
SOURCE_TYPE_XID_OWI = unicode_type("xisbn.worldcat.org/webservices/xid/owi/")
SOURCE_TYPE_XID_OCLC = unicode_type("xisbn.worldcat.org/webservices/xid/oclcnum/")

#--------------------------------------------------------------------------------------------
def library_codes_generic_webscraping_api(source_type,source_dict,another_dict):

    source_type = unicode_type(source_type)

    if source_type == SOURCE_TYPE_VIAF:
        active_target_url = "http://viaf.org/viaf/[REFERENCENUMBER]/"
    elif source_type == SOURCE_TYPE_OCLC:
        active_target_url = "https://www.worldcat.org/oclc/[REFERENCENUMBER]/"
    elif source_type == SOURCE_TYPE_XID_OWI:
        active_target_url = "http://xisbn.worldcat.org/webservices/xid/owi/owi[REFERENCENUMBER]?method=getEditions&format=xml&fl=isbn,lccn"
    elif source_type == SOURCE_TYPE_XID_OCLC:
        active_target_url = "http://xisbn.worldcat.org/webservices/xid/oclcnum/[REFERENCENUMBER]?method=getEditions&format=xml&fl=lccn"
    else:
        results_dict = {}
        return results_dict

    # another_dict is currently only possibly equal to:   isbn_dict

    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    def download_html(target_url):
        soup = ""
        html_page = ""
        html_raw = ""
        try:
            #~ connection = urllib2.urlopen(target_url)
            connection = myurlopen(target_url)
            html_raw = connection.read()
            soup = BeautifulSoup(html_raw)
            if hasattr(soup,"findAll"):
                if DEBUG: print("BeautifulSoup3 is being used in download_html")
            elif hasattr(soup,"find_all"):
                if DEBUG: print("BeautifulSoup4 is being used in download_html")
            else:
                if DEBUG: print("BeautifulSoup???? is being used in download_html")
            connection.close()
            del connection
            html_page = soup.prettify()    # take note...
        except Exception as e:
            if DEBUG: print(unicode_type(e))
            pass

        if not soup:
            if DEBUG: print("not soup")
            soup = ""
        if not html_page:
            html_page = ""
        if not html_raw:
            html_raw = ""



        return html_page,soup,html_raw
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    def parse_html_viaf(v,html_page,html_raw):

        # v = viaf

        new_row1 = None
        new_row2 = None

        try:
            html_page = unicode_type(html_page)
            text_list = html_page.split("source nsid")
            #~ if DEBUG: print("# rows: ", unicode_type(len(text_list)))
            for row in text_list:
                s = unicode_type(row)
                t = unicode_type("ISNI|")
                if s.count(t) > 0:  #  <a href="/viaf/sourceID/ISNI|0000000121340483">ISNI|0000000121340483</a>
                    s = s.strip()
                    s_split = s.split('|')
                    if s_split:
                        if len(s_split) > 0:
                            s = s_split[1]
                            myre = '[0-9]+'
                            match1 = re.match(myre,s)
                            if match1:
                                isni = match1.group(0)
                                isni = isni.strip()
                                if DEBUG: print("isni is: ", unicode_type(isni))
                                new_row1 = "isni",v,isni
                                break
            #END FOR
            del text_list

            #  <a href="http://www.worldcat.org/identities/lccn-n2001-90808">WorldCat Identities</a>
            #~ <ns2:source nsid="n50012900">LC|n  50012900</ns2:source>
            #~  LC|n  50012900
            contents = unicode_type(html_raw)
            tmp_list = contents.split("<ns2:")
            if tmp_list:
                #~ if DEBUG: print("length of tmp_list: ", unicode_type(len(tmp_list)))
                for row in tmp_list:
                    s = unicode_type(row)
                    if unicode_type('LC|n') in s:
                        s_split = s.split('LC|n')
                        if s_split:
                            if len(s_split) > 0:
                                lccn = s_split[1]
                                lccn = lccn.strip()
                                lccn = "lccn-n" + lccn
                                lccn = lccn.replace(" ","")
                                n = lccn.find("<")
                                if n > 0:
                                    lccn = lccn[0:n]
                                n = lccn.find('"')
                                if n > 0:
                                    lccn = lccn[0:n]
                                if DEBUG: print("lccn is: ", unicode_type(lccn))
                                new_row2 = "lccn",v,lccn
                                break
                    else:
                        continue
                #END FOR
            else:
                if DEBUG: print("no data for lccn")
                pass
        except Exception as e:
            if DEBUG: print(unicode_type(e))
            pass

        return new_row1,new_row2
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    def parse_html_oclc(v,soup):

        # v = oclc

        #~ <head>
            #~ <meta http-equiv="X-UA-Compatible" content="IE=edge">
            #~ <title>The Andy Warhol diaries (Book, 2014) [WorldCat.org]</title>
            #~ <meta name="description" content="Get this from a library! The Andy Warhol diaries. [Andy Warhol; Pat Hackett] -- Spanning the mid-1970s until just a few days before his death in 1987, THE ANDY WARHOL DIARIES is a compendium of the more than twenty thousand pages of the artist&#039;s diary that he dictated daily to ..." />
            #~ <link rel="canonical" href="//www.worldcat.org/title/andy-warhol-diaries/oclc/881024850" />
            #~ <link rel="meta" type="application/rdf+xml" href="http://www.worldcat.org/oclc/881024850.rdf" />
            #~ <link rel="meta" type="application/ld+json" href="http://www.worldcat.org/oclc/881024850.jsonld" />
            #~ <link rel="meta" type="text/turtle" href="http://www.worldcat.org/oclc/881024850.ttl" />
            #~ <link rel="meta" type="text/plain" href="http://www.worldcat.org/oclc/881024850.nt" />
            #~ <meta name="keywords" content="Warhol, Andy, 1928-1987 Diaries, Artists United States Diaries, Artists United States Biography, Warhol, Andy, 1928-1987, Artists, United States." />
        #~ </head>
        new_row1 = None
        new_row2 = None
        new_row3 = None
        new_row4 = None
        new_row5 = None
        try:
            if soup == "":
                if DEBUG: print("not soup.........")
                return new_row1,new_row2,new_row3,new_row4,new_row5
            head = soup.head
            if head:
                ttitle = head.find('title')
                title = ttitle.string
                title = title.replace("[WorldCat.org]","")
                if DEBUG: print("https://www.worldcat.org/oclc/  --  title is: ", title)
                if hasattr(soup,"findAll"):
                    mydata = head.findAll(True)       # bs3
                    if DEBUG: print("BeautifulSoup3 is being used in parse_html_oclc")
                elif hasattr(soup,"find_all"):
                    mydata = head.find_all(True)       # bs4
                    if DEBUG: print("BeautifulSoup4 is being used in parse_html_oclc")
                else:
                    mydata = None
                    if DEBUG: print("BeautifulSoup???? is being used in parse_html_oclc")
                if mydata:
                    for item in mydata:
                        if item:
                            s = unicode_type(item)
                            if s.count("<meta") > 0:
                                if s.count('name="keywords"') > 0:     #  <meta name="keywords" content="Warhol, Andy, 1928-1987 Diaries, Artists United States Diaries, Artists United States Biography, Warhol, Andy, 1928-1987, Artists, United States." />
                                    s = s.strip()
                                    s_split = s.split('content=')
                                    if s_split:
                                        if len(s_split) > 0:
                                            long_string = s_split[1]
                                            del s_split
                                            long_string = long_string.replace('"','')   # e.g.  arts."   or    "Warhol
                                            long_string = long_string.replace('.','')   # e.g.  arts.  which is now identical to another value = arts; no duplicates.
                                            long_string = long_string.replace('/>','')
                                            tmp_list = long_string.split(",")
                                            tmp_set = set(tmp_list)
                                            tmp_list = list(tmp_set)   # now no duplicates
                                            del tmp_set
                                            tmp_list.sort()
                                            for row in tmp_list:
                                                row = row.strip()
                                                if title.count(row) > 0:   # e.g. Warhol is in the title...
                                                    continue
                                                else:
                                                    pass
                                                try:
                                                    if DEBUG: print("keyword: ", row)
                                                except:
                                                    pass
                                                if not new_row1:
                                                    new_row1 = "lcead",v,row
                                                elif not new_row2:
                                                    new_row2 = "lcead",v,row
                                                elif not new_row3:
                                                    new_row3 = "lcead",v,row
                                                elif not new_row4:
                                                    new_row4 = "lcead",v,row
                                                elif not new_row5:
                                                    new_row5 = "lcead",v,row
                                                else:
                                                    continue
                                            #END FOR
                    #END FOR
                    del mydata
                else:
                    if DEBUG: print("no lcead keywords were found for url...")
        except Exception as e:
            if DEBUG: print(unicode_type(e))
            pass

        #~ if DEBUG: print("new rows 1-5: ", new_row1,new_row2,new_row3,new_row4,new_row5)

        return new_row1,new_row2,new_row3,new_row4,new_row5
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    def parse_html_xid(v,html_page,call_type,isbn):

        #---------------------------------------------------------------------------
        #   OCLC           v = oclc (other)     purpose:  retrieve lccn for oclc (specifically here for lccn)
        #---------------------------------------------------------------------------
        #~ <?xml version="1.0" encoding="UTF-8"?>
        #~ <rsp xmlns="http://worldcat.org/xid/oclcnum/" stat="ok">
        #~ <oclcnum    lccn="2001044026"     >47254275</oclcnum>
        #~ <oclcnum    lccn="2001044026"     >490898930</oclcnum>
        #~ </rsp>
        #---------------------------------------------------------------------------
        #  OWI              v = oclc-owi         purpose:  retrieve oclc for isbn (specifically here for oclc)  (may or may not also retrieve lccn simultaneously)
        #---------------------------------------------------------------------------
        #~ http://xisbn.worldcat.org/webservices/xid/owi/owi718389?method=getEditions&format=xml&fl=lccn,isbn
        #~ <?xml version="1.0" encoding="UTF-8"?>
        #~ <rsp xmlns="http://worldcat.org/xid/oclcnum/" stat="ok">
        #~ <oclcnum   isbn="9781565924642"  lccn="00267609"     >41259934</oclcnum>
        #~ <oclcnum   isbn="9781565924642 9781565928930"      >44960325</oclcnum>
        #~ <oclcnum   isbn="9781565924642 9781565928930"      >54116262</oclcnum>
        #~ <oclcnum   isbn="9780596513986"      >156890981</oclcnum>
        #~ <oclcnum   isbn="9780596513986"      >182576260</oclcnum>
        #~ <oclcnum   isbn="9781565924642"  lccn="00267609"     >41466161</oclcnum>
        #~ <oclcnum   isbn="9781565924642"  lccn="00267609"     >491122358</oclcnum>
        #---------------------------------------------------------------------------

        if DEBUG: print("parse_html_xid:  source_type is: ", call_type, "  of:  ", v, "  with an isbn of: ", unicode_type(isbn))
        #~ if DEBUG: print("=============================================")
        #~ if DEBUG: print(unicode_type(html_page))
        #~ if DEBUG: print("=============================================")

        new_row1 = None

        try:
            html_page = unicode_type(html_page)
            oclcnums = html_page.split("<oclcnum")              #  <oclcnum    lccn="88040565"     >19326769</oclcnum>
            if oclcnums:
                if len(oclcnums) > 1:
                    if call_type == "oclc":
                        for oclcnum in oclcnums:
                            if oclcnum:
                                s = unicode_type(oclcnum)
                                if s.count("lccn=") > 0:               #  lccn="88040565"     >19326769</oclcnum>
                                    s = s.strip()
                                    s_split = s.split('lccn="')
                                    if s_split:
                                        if len(s_split) > 0:
                                            lccn = s_split[1]
                                            lccn = lccn.strip()
                                            n = lccn.find('"')   #        88040565"     >19326769</oclcnum>
                                            if n > 5:
                                                lccn = lccn[0:n+1]
                                                lccn = lccn.replace('"','')
                                                lccn = lccn.strip()          #   88040565
                                                if DEBUG: print("loc lccn is: ", unicode_type(lccn))
                                                if lccn.isdigit():
                                                    new_row1 = "loc_lccn",v,lccn
                                                    break
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        #END FOR
                    else:
                        pass
                    if call_type == "owi":
                        if isbn:
                            foundit = False
                            for oclcnum in oclcnums:
                                if oclcnum:
                                    s = unicode_type(oclcnum)
                                    if s.count("isbn=") > 0:         #~ <oclcnum   isbn="9781565924642 9781565928930"      >44960325</oclcnum>
                                        if s.count(isbn) > 0:
                                            s = s.strip()
                                            n = len(s) - 22
                                            oclc = s[n: ]
                                            oclc = oclc.strip()
                                            oclc = oclc.replace("</oclcnum>","")
                                            oclc = oclc.replace(">","")
                                            oclc = oclc.replace('"',"")
                                            oclc = oclc.strip()
                                            if len(oclc) > 5:
                                                if oclc.isdigit():
                                                    if DEBUG: print("oclc (other) is: ", unicode_type(oclc))
                                                    new_row1 = "oclc",v,oclc
                                                    foundit = True
                                                    break
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    continue
                            #END FOR
                            if not foundit:
                                # default to the best one available...since the book's isbn may not be 'good'...just require that a recent isbn exists in the results for the oclc-owi...and use its oclc (other)...
                               for oclcnum in oclcnums:
                                    if oclcnum:
                                        s = unicode_type(oclcnum)
                                        if s.count('isbn="9') > 0:         #~ <oclcnum   isbn="9781565924642 9781565928930"      >44960325</oclcnum>
                                            s = s.strip()
                                            n = len(s) - 22
                                            oclc = s[n: ]
                                            oclc = oclc.strip()
                                            oclc = oclc.replace("</oclcnum>","")
                                            oclc = oclc.replace(">","")
                                            oclc = oclc.replace('"',"")
                                            oclc = oclc.strip()
                                            if len(oclc) > 5:
                                                if oclc.isdigit():
                                                    if DEBUG: print("oclc (other) (the best available given the book's current isbn) is: ", unicode_type(oclc))
                                                    new_row1 = "oclc",v,oclc
                                                    foundit = True
                                                    break
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                                    else:
                                        continue
                                #END FOR
                            else:
                                pass
                            if not foundit:
                                # default to the best one available...any oclc is better than no oclc as long as it is an oclc for this book's specific oclc-owi...
                               for oclcnum in oclcnums:
                                    if oclcnum:
                                        s = unicode_type(oclcnum)
                                        if s.count('oclcnum') > 0:         #~ <oclcnum   ..............      >44960325</oclcnum>
                                            s = s.strip()
                                            n = len(s) - 22
                                            oclc = s[n: ]
                                            oclc = oclc.strip()
                                            oclc = oclc.replace("</oclcnum>","")
                                            oclc = oclc.replace(">","")
                                            oclc = oclc.replace('"',"")
                                            oclc = oclc.strip()
                                            if len(oclc) > 5:
                                                if oclc.isdigit():
                                                    if DEBUG: print("oclc (other) (the only value available at this time) is: ", unicode_type(oclc))
                                                    new_row1 = "oclc",v,oclc
                                                    foundit = True
                                                    break
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                                    else:
                                        continue
                                #END FOR
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except Exception as e:
            if DEBUG: print("Exception: ", unicode_type(e))
            pass

        if DEBUG: print("new_row1: ", unicode_type(new_row1))

        return new_row1
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------
    #-----------------------------------------------

    #-----------------------------------------------
    # MAIN FUNCTION
    #-----------------------------------------------

    final_results_dict = {}

    already_retrieved_list = []

    if DEBUG: print(" ")

    #~ for k,v in source_dict.iteritems():
    for k,v in iteritems(source_dict):
        results_list = []
        v = unicode_type(v)
        target_url = active_target_url
        isbn = None
        if another_dict:
            if source_type == SOURCE_TYPE_XID_OWI:
                if k in another_dict:
                    isbn = another_dict[k]
                    isbn = unicode_type(isbn)
                else:
                    pass
        else:
            pass
        target_url = target_url.replace("[REFERENCENUMBER]",v)
        if DEBUG: print("-----------------------------------------------")
        try:
            if DEBUG: print("current target_url is: ", target_url)
        except:
            pass
        if not v in already_retrieved_list:
            if source_type == SOURCE_TYPE_VIAF:
                html_page,soup,html_raw = download_html(target_url)
                new_row1,new_row2 = parse_html_viaf(v,html_page,html_raw)
                already_retrieved_list.append(v)
            elif source_type == SOURCE_TYPE_OCLC:
                html_page,soup,html_raw = download_html(target_url)
                new_row1,new_row2,new_row3,new_row4,new_row5 = parse_html_oclc(v,soup)        # returns multiple LC Extra Author Detail rows
                already_retrieved_list.append(v)
            elif source_type == SOURCE_TYPE_XID_OWI:
                html_page,soup,html_raw = download_html(target_url)
                new_row1 = parse_html_xid(v,html_page,"owi",isbn)     #call_type = "owi"  returns oclc for isbn/owi combination
            elif source_type == SOURCE_TYPE_XID_OCLC:
                html_page,soup,html_raw = download_html(target_url)
                new_row1 = parse_html_xid(v,html_page,"oclc",None)   #call_type = "oclc"  returns loc_lccn for oclc
            else:
                continue

            try:
                if new_row1:
                    results_list.append(new_row1)
                if new_row2:
                    results_list.append(new_row2)
                if new_row3:
                    results_list.append(new_row3)
                if new_row4:
                    results_list.append(new_row4)
                if new_row5:
                    results_list.append(new_row5)
            except:
                pass
            if len(results_list) > 0:
                    final_results_dict[v] = results_list
            try:
                del new_row1
                del new_row2
                del new_row3
                del new_row4
                del new_row5
            except:
                pass
            try:
                del results_list
            except:
                pass
        else:
            if DEBUG: print("reference number was already processed; skipping... ", unicode_type(v))
            continue
    #END FOR
    if DEBUG: print("-----------------------------------------------")

    try:
        del soup
        del html_page
        del html_raw
        del source_dict
        del another_dict
        del already_retrieved_list
    except:
        pass

    return final_results_dict

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#END OF library_codes_webscraping_api
