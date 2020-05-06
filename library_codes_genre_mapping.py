# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2
def return_lc_genre_mapping_table_mysql():
    mysql = ("\
            BEGIN TRANSACTION;\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('0','Information');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('00','Information>Computing And Information');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('000','Information>Computing And Information>Computer science, knowledge & systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001','Information>Computing And Information>Knowledge');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.012','Information>Computing And Information>Knowledge>Classification');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.1','Information>Computing And Information>Knowledge>Intellectual Life');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.2','Information>Computing And Information>Knowledge>Scholarship And Learning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.3','Information>Computing And Information>Knowledge>Humanities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.4','Information>Computing And Information>Knowledge>Research And Data Display');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.433','Information>Computing And Information>Knowledge>Questionnaires');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.5','Information>Computing And Information>Knowledge>Communication');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.6','Information>Computing And Information>Knowledge>Computer Science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.9','Information>Computing And Information>Knowledge>Controversial knowledge');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.942','Information>Computing And Information>Knowledge>UFOs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('001.944','Information>Computing And Information>Knowledge>Monsters (unexplained phenomena)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('002','Information>Computing And Information>History of the Book');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('002.2','Information>Computing And Information>History of the Book>Dictionaries And Encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('003','Information>Computing And Information>Systems Theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('003.2','Information>Computing And Information>Systems Theory>Futuring');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('003.3','Information>Computing And Information>Systems Theory>Computer Simulation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('003.5','Information>Computing And Information>Systems Theory>Communication And Control');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('003.7','Information>Computing And Information>Systems Theory>Kinds Of Systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('003.8','Information>Computing And Information>Systems Theory>Systems And Time');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004','Information>Computing And Information>Computer Hardware');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.1','Information>Computing And Information>Computer Hardware>By Computer Type');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.16','Information>Computing And Information>Computer Hardware>Laptop computers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.3','Information>Computing And Information>Computer Hardware>Modes Of Processing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.5','Information>Computing And Information>Computer Hardware>Memory And Storage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.565','Information>Computing And Information>Computer Hardware>CDROMs (computer memory)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.6','Information>Computing And Information>Computer Hardware>Networking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.64','Information>Computing And Information>Computer Hardware>Opticalfiber cable (computer science)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.678','Information>Computing And Information>Computer Hardware>Internet');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.692','Information>Computing And Information>Computer Hardware>Email');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.693','Information>Computing And Information>Computer Hardware>Mailing lists (computers)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.7','Information>Computing And Information>Computer Hardware>Peripherals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('004.76','Information>Computing And Information>Computer Hardware>Keyboards (computers)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005','Information>Computing And Information>Computer Software');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.1','Information>Computing And Information>Computer Software>Programming');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.13','Information>Computing And Information>Computer Software>Computer languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.2','Information>Computing And Information>Computer Software>Programming For Specific Environments');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.3','Information>Computing And Information>Computer Software>Programs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.4','Information>Computing And Information>Computer Software>Compilers And Operating Systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.435','Information>Computing And Information>Computer Software>Memory management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.5','Information>Computing And Information>Computer Software>Desktop Applications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.7','Information>Computing And Information>Computer Software>Data');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.74','Information>Computing And Information>Computer Software>File managers (computers)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('005.8','Information>Computing And Information>Computer Software>Computer Security');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006','Information>Computing And Information>Special Topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.3','Information>Computing And Information>Special Topics>Artificial Intelligence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.31','Information>Computing And Information>Special Topics>Machine Learning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.32','Information>Computing And Information>Special Topics>Neural Networks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.33','Information>Computing And Information>Special Topics>Knowledge-based Systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.35','Information>Computing And Information>Special Topics>Natural Language Processing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.37','Information>Computing And Information>Special Topics>Machine Vision');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.4','Information>Computing And Information>Special Topics>Pattern And Speech Recognition');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.5','Information>Computing And Information>Special Topics>Audio Tools');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.6','Information>Computing And Information>Special Topics>Computer Graphics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.7','Information>Computing And Information>Special Topics>Web Design');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.74','Information>Computing And Information>Special Topics>Markup Language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('006.8','Information>Computing And Information>Special Topics>Virtual Reality');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('007','Information>Computing And Information>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('008','Information>Computing And Information>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('009','Information>Computing And Information>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('01','Information>Bibliographies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('010','Information>Bibliographies>Bibliography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('011','Information>Bibliographies>General Bibliographies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('012','Information>Bibliographies>Of Individuals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('013','Information>Bibliographies>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('014','Information>Bibliographies>Of anonymous & pseudonymous works');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('015','Information>Bibliographies>Of Special Countries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('016','Information>Bibliographies>Of Special Subjects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('017','Information>Bibliographies>Clast Catalogs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('018','Information>Bibliographies>Author Catalogs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('019','Information>Bibliographies>Dictionary Catalogs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020','Information>Library and Information Sciences');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.1','Information>Library and Information Sciences>Theory and Instruction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.2','Information>Library and Information Sciences>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.3','Information>Library and Information Sciences>Dictionaries And Encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.4','Information>Library and Information Sciences>Essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.5','Information>Library and Information Sciences>Periodicals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.6','Information>Library and Information Sciences>Societies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.7','Information>Library and Information Sciences>Education And Research');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.8','Information>Library and Information Sciences>Culture Studies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('020.9','Information>Library and Information Sciences>Biography And History');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('021','Information>Library and Information Sciences>Library relationships');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('022','Information>Library and Information Sciences>Administration of physical plant');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('023','Information>Library and Information Sciences>Personnel management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('024','Information>Library and Information Sciences>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('025','Information>Library and Information Sciences>Library operations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('025.04','Information>Library and Information Sciences>Databases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('025.3','Information>Library and Information Sciences>Indexing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('025.524','Information>Library and Information Sciences>Information');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('026','Information>Library and Information Sciences>Libraries for specific subjects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('027','Information>Library and Information Sciences>General Libraries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('028','Information>Library and Information Sciences>Reading & use of other information media');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('029','Information>Library and Information Sciences>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('030','Information>Dictionaries and Encyclopedias>General Encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('031','Information>Dictionaries and Encyclopedias>American');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('032','Information>Dictionaries and Encyclopedias>English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('033','Information>Dictionaries and Encyclopedias>German');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('034','Information>Dictionaries and Encyclopedias>French');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('035','Information>Dictionaries and Encyclopedias>Italian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('036','Information>Dictionaries and Encyclopedias>Spanish');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('037','Information>Dictionaries and Encyclopedias>Slavic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('038','Information>Dictionaries and Encyclopedias>Scandinavian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('039','Information>Dictionaries and Encyclopedias>Minor Languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('040','Information>General Collected Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('041','Information>General Collected Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('042','Information>General Collected Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('043','Information>General Collected Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('044','Information>Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('045','Information>Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('046','Information>Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('047','Information>Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('048','Information>Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('049','Information>Essays>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('050','Information>Periodicals>Magazines, journals & serials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('051','Information>Periodicals>Serials in American English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('052','Information>Periodicals>Serials in English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('053','Information>Periodicals>Serials in other Germanic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('054','Information>Periodicals>Serials in French, Occitan & Catalan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('055','Information>Periodicals>In Italian, Romanian & related languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('056','Information>Periodicals>Serials in Spanish & Portuguese');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('057','Information>Periodicals>Serials in Slavic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('057.972','Information>Periodicals>Allergies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('058','Information>Periodicals>Serials in Scandinavian languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('059','Information>Periodicals>Serials in other languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('060','Information>Organizations>Associations, organizations & museums');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('061','Information>Organizations>Organizations in North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('062','Information>Organizations>Organizations in British Isles and in England');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('063','Information>Organizations>Organizations in central Europe and in Germany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('064','Information>Organizations>Organizations in France & Monaco');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('065','Information>Organizations>Organizations in Italy & adjacent islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('066','Information>Organizations>In Iberian Peninsula & adjacent islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('067','Information>Organizations>Organizations in eastern Europe and in Russia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('068','Information>Organizations>Organizations in other geographic areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('069','Information>Organizations>Museums');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('069.4','Information>Organizations>Collecting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('070','Information>Journalism and Publishing>News media, journalism & publishing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('071','Information>Journalism and Publishing>Newspapers in North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('072','Information>Journalism and Publishing>Newspapers in British Isles and in  England');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('073','Information>Journalism and Publishing>Newspapers in central Europe and in  Germany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('074','Information>Journalism and Publishing>Newspapers in France & Monaco');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('075','Information>Journalism and Publishing>Newspapers in Italy & adjacent islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('076','Information>Journalism and Publishing>In Iberian Peninsula & adjacent islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('077','Information>Journalism and Publishing>Newspapers in eastern Europe and in  Russia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('078','Information>Journalism and Publishing>Newspapers in Scandinavia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('079','Information>Journalism and Publishing>Newspapers in other geographic areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('080','Information>Quotations>Quotations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('081','Information>Quotations>Collections in American English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('082','Information>Quotations>Collections in English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('083','Information>Quotations>Collections in other Germanic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('084','Information>Quotations>Collections in French, Occitan & Catalan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('085','Information>Quotations>In Italian, Romanian & related languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('086','Information>Quotations>Collections in Spanish & Portuguese');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('087','Information>Quotations>Collections in Slavic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('088','Information>Quotations>Collections in Scandinavian languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('089','Information>Quotations>Collections in other languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('090','Information>Manuscripts and Rare Books>Manuscripts & rare books');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('091','Information>Manuscripts and Rare Books>Manuscripts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('092','Information>Manuscripts and Rare Books>Block books');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('093','Information>Manuscripts and Rare Books>Incunabula');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('094','Information>Manuscripts and Rare Books>Printed books');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('095','Information>Manuscripts and Rare Books>Books notable for bindings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('096','Information>Manuscripts and Rare Books>Books notable for illustrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('097','Information>Manuscripts and Rare Books>Books notable for ownership or origin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('098','Information>Manuscripts and Rare Books>Prohibited works, forgeries & hoaxes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('099','Information>Manuscripts and Rare Books>Books notable for format');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('1','Philosophy And Psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('10','Philosophy And Psychology>Philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('100','Philosophy And Psychology>Philosophy>Philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('101','Philosophy And Psychology>Philosophy>Theory of philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('102','Philosophy And Psychology>Philosophy>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('103','Philosophy And Psychology>Philosophy>Dictionaries & encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('104','Philosophy And Psychology>Philosophy>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('105','Philosophy And Psychology>Philosophy>Serial publications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('106','Philosophy And Psychology>Philosophy>Organizations & management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('107','Philosophy And Psychology>Philosophy>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('108','Philosophy And Psychology>Philosophy>Kinds of persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('109','Philosophy And Psychology>Philosophy>Historical & collected persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('110','Philosophy And Psychology>Metaphysics>Metaphysics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('111','Philosophy And Psychology>Metaphysics>Ontology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('111.85','Philosophy And Psychology>Metaphysics>Aesthetics--philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('112','Philosophy And Psychology>Metaphysics>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('113','Philosophy And Psychology>Metaphysics>Cosmology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('114','Philosophy And Psychology>Metaphysics>Space');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('115','Philosophy And Psychology>Metaphysics>Time');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('116','Philosophy And Psychology>Metaphysics>Change');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('117','Philosophy And Psychology>Metaphysics>Structure');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('118','Philosophy And Psychology>Metaphysics>Force & energy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('119','Philosophy And Psychology>Metaphysics>Number & quantity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('120','Philosophy And Psychology>Philosophy of Humanity>Epistemology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('121','Philosophy And Psychology>Philosophy of Humanity>Truth');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('121.7','Philosophy And Psychology>Philosophy of Humanity>Faith');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('122','Philosophy And Psychology>Philosophy of Humanity>Causation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('123','Philosophy And Psychology>Philosophy of Humanity>Fate');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('123.5','Philosophy And Psychology>Philosophy of Humanity>Freedom');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('124','Philosophy And Psychology>Philosophy of Humanity>Teleology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('125','Philosophy And Psychology>Philosophy of Humanity>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('126','Philosophy And Psychology>Philosophy of Humanity>The self');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('127','Philosophy And Psychology>Philosophy of Humanity>The unconscious & the subconscious');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('128','Philosophy And Psychology>Philosophy of Humanity>Humankind');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('129','Philosophy And Psychology>Philosophy of Humanity>Immortality (philosophy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('130','Philosophy And Psychology>Parapsychology and Occultism>Parapsychology & occultism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('131','Philosophy And Psychology>Parapsychology and Occultism>Parapsychological & occult methods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('132','Philosophy And Psychology>Parapsychology and Occultism>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133','Philosophy And Psychology>Parapsychology and Occultism>Occult');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.1','Philosophy And Psychology>Parapsychology and Occultism>Ghosts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.3','Philosophy And Psychology>Parapsychology and Occultism>Fortune telling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.333','Philosophy And Psychology>Parapsychology and Occultism>Feng shui');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.334','Philosophy And Psychology>Parapsychology and Occultism>Omens');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.4','Philosophy And Psychology>Parapsychology and Occultism>Witchcraft');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.43','Philosophy And Psychology>Parapsychology and Occultism>Magic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.54','Philosophy And Psychology>Parapsychology and Occultism>Horoscopes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.82','Philosophy And Psychology>Parapsychology and Occultism>Mind reading');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.901','Philosophy And Psychology>Parapsychology and Occultism>Reincarnation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('133.95','Philosophy And Psychology>Parapsychology and Occultism>Outofbody experience');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('134','Philosophy And Psychology>Parapsychology and Occultism>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('135','Philosophy And Psychology>Parapsychology and Occultism>Dreams & mysteries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('135.3','Philosophy And Psychology>Parapsychology and Occultism>Dreams');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('136','Philosophy And Psychology>Parapsychology and Occultism>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('137','Philosophy And Psychology>Parapsychology and Occultism>Divinatory graphology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('138','Philosophy And Psychology>Parapsychology and Occultism>Physiognomy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('139','Philosophy And Psychology>Parapsychology and Occultism>Phrenology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('140','Philosophy And Psychology>Philosophical Systems>Philosophical schools of thought');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('141','Philosophy And Psychology>Philosophical Systems>Idealism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('142','Philosophy And Psychology>Philosophical Systems>Critical philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('142.78','Philosophy And Psychology>Philosophical Systems>Existentialism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('143','Philosophy And Psychology>Philosophical Systems>Bergsonism & intuitionism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('144','Philosophy And Psychology>Philosophical Systems>Humanism & related systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('145','Philosophy And Psychology>Philosophical Systems>Sensationalism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('146','Philosophy And Psychology>Philosophical Systems>Naturalism & related systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('146.3','Philosophy And Psychology>Philosophical Systems>Materialism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('147','Philosophy And Psychology>Philosophical Systems>Pantheism & related systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('148','Philosophy And Psychology>Philosophical Systems>Liberalism (philosophy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('149','Philosophy And Psychology>Philosophical Systems>Other philosophical systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('150','Philosophy And Psychology>Psychology>Psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('151','Philosophy And Psychology>Psychology>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152','Philosophy And Psychology>Psychology>Perception, movement, emotions & drives');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152.1','Philosophy And Psychology>Psychology>Discrimination (psychology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152.4','Philosophy And Psychology>Psychology>Feelings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152.42','Philosophy And Psychology>Psychology>Joy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152.43','Philosophy And Psychology>Psychology>Humor');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152.46','Philosophy And Psychology>Psychology>Fear');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('152.47','Philosophy And Psychology>Psychology>Anger');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('153','Philosophy And Psychology>Psychology>Mental processes & intelligence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('153.15','Philosophy And Psychology>Psychology>Learning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('153.8','Philosophy And Psychology>Psychology>Motivation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('153.9','Philosophy And Psychology>Psychology>Intelligence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('153.93','Philosophy And Psychology>Psychology>IQ tests');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('154','Philosophy And Psychology>Psychology>Subconscious & altered states');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('154.3','Philosophy And Psychology>Psychology>Fantasy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('154.4','Philosophy And Psychology>Psychology>Hallucinations (psychology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('154.7','Philosophy And Psychology>Psychology>Hypnosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('155','Philosophy And Psychology>Psychology>Differential & developmental psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('155.2','Philosophy And Psychology>Psychology>Character');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('155.25','Philosophy And Psychology>Psychology>Maturity (individual psychologycharacterdevelopment)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('155.6','Philosophy And Psychology>Psychology>Maturity (developmental psychologyadulthood)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('155.916','Philosophy And Psychology>Psychology>Deformities (psychological influence)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('155.93','Philosophy And Psychology>Psychology>Death and Dying(psychology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('156','Philosophy And Psychology>Psychology>Comparative psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('157','Philosophy And Psychology>Psychology>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('158','Philosophy And Psychology>Psychology>Applied Psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('158.12','Philosophy And Psychology>Psychology>Meditation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('159','Philosophy And Psychology>Psychology>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('160','Philosophy And Psychology>Logic>Logic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('161','Philosophy And Psychology>Logic>Induction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('162','Philosophy And Psychology>Logic>Deduction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('163','Philosophy And Psychology>Logic>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('164','Philosophy And Psychology>Logic>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('165','Philosophy And Psychology>Logic>Fallacies & sources of error');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('166','Philosophy And Psychology>Logic>Syllogisms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('167','Philosophy And Psychology>Logic>Hypotheses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('168','Philosophy And Psychology>Logic>Argument & persuasion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('169','Philosophy And Psychology>Logic>Analogy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('170','Philosophy And Psychology>Ethics>Ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('171','Philosophy And Psychology>Ethics>Ethical systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('172','Philosophy And Psychology>Ethics>Political ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('172.179','Philosophy And Psychology>Ethics>Ethical problems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('172.2','Philosophy And Psychology>Ethics>Government (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('172.422','Philosophy And Psychology>Ethics>Nuclear  warfare(ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('173','Philosophy And Psychology>Ethics>Divorce (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('174','Philosophy And Psychology>Ethics>Occupational ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('174.2','Philosophy And Psychology>Ethics>Medical ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('174.297','Philosophy And Psychology>Ethics>Organ  transplants(medical ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('174.4','Philosophy And Psychology>Ethics>Business Ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('175','Philosophy And Psychology>Ethics>Gambling (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('176','Philosophy And Psychology>Ethics>Homosexuality (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('177','Philosophy And Psychology>Ethics>Ethics of social relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('177.2','Philosophy And Psychology>Ethics>Gossip (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('177.3','Philosophy And Psychology>Ethics>Lying (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('177.62','Philosophy And Psychology>Ethics>Friendship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('177.7','Philosophy And Psychology>Ethics>Charity (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('178','Philosophy And Psychology>Ethics>Greed');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('178.8','Philosophy And Psychology>Ethics>Narcotics (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('179','Philosophy And Psychology>Ethics>Other ethical norms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('179.6','Philosophy And Psychology>Ethics>Courage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('179.7','Philosophy And Psychology>Ethics>Genocide (ethics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('179.8','Philosophy And Psychology>Ethics>Hate');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('179.9','Philosophy And Psychology>Ethics>Gratitude');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('180','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Ancient, medieval & eastern philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('181','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Eastern philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('182','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Pre-Socratic Greek philosophies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('183','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Socratic & related philosophies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('184','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Platonic philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('185','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Aristotelian philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('186','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Skeptic & Neoplatonic philosophies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('187','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Epicurean philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('188','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Stoic philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('189','Philosophy And Psychology>Ancient, Medieval and Eastern Philosophy>Medieval western philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('190','Philosophy And Psychology>Modern Western Philosophy>Modern western philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('191','Philosophy And Psychology>Modern Western Philosophy>Philosophy of United States & Canada');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('192','Philosophy And Psychology>Modern Western Philosophy>Philosophy of British Isles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('193','Philosophy And Psychology>Modern Western Philosophy>Philosophy of Germany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('194','Philosophy And Psychology>Modern Western Philosophy>Philosophy of France');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('195','Philosophy And Psychology>Modern Western Philosophy>Philosophy of Italy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('196','Philosophy And Psychology>Modern Western Philosophy>Philosophy of Spain & Portugal');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('197','Philosophy And Psychology>Modern Western Philosophy>Philosophy of former Soviet Union');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('198','Philosophy And Psychology>Modern Western Philosophy>Philosophy of Scandinavia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('199','Philosophy And Psychology>Modern Western Philosophy>Philosophy in other geographic areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('2','Religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('200','Religion>Religon>Religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('200.92','Religion>Religon>Saints');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('201','Religion>Religon>Religious mythology & social theology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202','Religion>Religon>Doctrines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202.117','Religion>Religon>Miracles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202.13','Religion>Religon>Heroes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202.18','Religion>Religon>Idols');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202.2','Religion>Religon>Karma');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202.3','Religion>Religon>Heaven');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('202.37','Religion>Religon>Reincarnation (religion)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('203','Religion>Religon>Public worship & other practices');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('203.5','Religion>Religon>Shrines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('203.8','Religion>Religon>Benedictions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('204','Religion>Religon>Religious experience, life & practice');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('204.2','Religion>Religon>Visions (religious experience)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('204.47','Religion>Religon>Fasting (religious practice)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('205','Religion>Religon>Religious ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('206','Religion>Religon>Leaders & organization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('206.1','Religion>Religon>Marriage counseling (pastoraltheology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('207','Religion>Religon>Missions & religious education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('208','Religion>Religon>Sources');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('209','Religion>Religon>Cults');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('210','Religion>Theory>Philosophy & theory of religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('211','Religion>Theory>Concepts of God');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('212','Religion>Theory>Existence, knowability & attributes of God');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('212.1','Religion>Theory>Existence of God');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('213','Religion>Theory>Creation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('214','Religion>Theory>Theodicy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('215','Religion>Theory>Science & religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('216','Religion>Theory>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('217','Religion>Theory>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('218','Religion>Theory>Humankind');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('219','Religion>Theory>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('220','Religion>Bible>The Bible');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('220.95','Religion>Bible>Biblical Events');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('221','Religion>Bible>Old Testament');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('222','Religion>Bible>Historical books of Old Testament');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('223','Religion>Bible>Poetic books of Old Testament');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('224','Religion>Bible>Prophetic books of Old Testament');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('225','Religion>Bible>New Testament');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('226','Religion>Bible>Gospels & Acts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('227','Religion>Bible>Epistles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('228','Religion>Bible>Revelation (Apocalypse)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('229','Religion>Bible>Apocrypha & pseudepigrapha');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('230','Religion>Christianity>Christianity & Christian theology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('231','Religion>Christianity>God');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('232','Religion>Christianity>Jesus Christ & his family');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('233','Religion>Christianity>Humankind');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('233.14','Religion>Christianity>Original sin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('234','Religion>Christianity>Salvation & grace');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('235','Religion>Christianity>Spiritual beings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('236','Religion>Christianity>Eschatology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('237','Religion>Christianity>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('238','Religion>Christianity>Creeds & catechisms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('239','Religion>Christianity>Apologetics & polemics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('240','Religion>Christian Practice and Observance>Christian practice & observance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('241','Religion>Christian Practice and Observance>Christian ethics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('242','Religion>Christian Practice and Observance>Devotionals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('243','Religion>Christian Practice and Observance>Evangelistic writings for individuals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('244','Religion>Christian Practice and Observance>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('245','Religion>Christian Practice and Observance>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('246','Religion>Christian Practice and Observance>Use of art in Christianity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('247','Religion>Christian Practice and Observance>Church furnishings & articles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('248','Religion>Christian Practice and Observance>Christian experience, practice & life');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('249','Religion>Christian Practice and Observance>Christian observances in family life');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('250','Religion>Cristian Pastoral Practice and Religious Orders>Christian pastoral practice & religious orders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('251','Religion>Cristian Pastoral Practice and Religious Orders>Preaching');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('252','Religion>Cristian Pastoral Practice and Religious Orders>Texts of sermons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('253','Religion>Cristian Pastoral Practice and Religious Orders>Pastoral office & work');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('254','Religion>Cristian Pastoral Practice and Religious Orders>Parish administration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('255','Religion>Cristian Pastoral Practice and Religious Orders>Religious congregations & orders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('256','Religion>Cristian Pastoral Practice and Religious Orders>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('257','Religion>Cristian Pastoral Practice and Religious Orders>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('258','Religion>Cristian Pastoral Practice and Religious Orders>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('259','Religion>Cristian Pastoral Practice and Religious Orders>Pastoral care of families & kinds of persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('260','Religion>Christian Organization, Social Work, Worship>Christian organization, social work & worship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('261','Religion>Christian Organization, Social Work, Worship>Social theology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('262','Religion>Christian Organization, Social Work, Worship>Ecclesiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('263','Religion>Christian Organization, Social Work, Worship>Days, times & places of observance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('263.93','Religion>Christian Organization, Social Work, Worship>Easter');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('264','Religion>Christian Organization, Social Work, Worship>Calendars');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('265','Religion>Christian Organization, Social Work, Worship>Sacraments, other rites & acts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('266','Religion>Christian Organization, Social Work, Worship>Missions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('267','Religion>Christian Organization, Social Work, Worship>Associations for religious work');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('268','Religion>Christian Organization, Social Work, Worship>Religious education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('269','Religion>Christian Organization, Social Work, Worship>Spiritual renewal');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('270','Religion>History of Christianity>History of Christianity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('271','Religion>History of Christianity>Religious orders in church history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('272','Religion>History of Christianity>Persecutions in church history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('273','Religion>History of Christianity>Doctrinal controversies & heresies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('274','Religion>History of Christianity>History of Christianity in Europe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('275','Religion>History of Christianity>History of Christianity in Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('276','Religion>History of Christianity>History of Christianity in Africa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('277','Religion>History of Christianity>History of Christianity in North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('278','Religion>History of Christianity>History of Christianity in South America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('279','Religion>History of Christianity>History of Christianity in other areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('280','Religion>Christian Denominations>Christian denominations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('281','Religion>Christian Denominations>Early church & Eastern churches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('282','Religion>Christian Denominations>Catholic Church');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('283','Religion>Christian Denominations>Anglican churches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('284','Religion>Christian Denominations>Protestants of Continental origin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('285','Religion>Christian Denominations>Presbyterian, Reformed & Congregational');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('286','Religion>Christian Denominations>Baptist, Disciples of Christ & Adventist');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('287','Religion>Christian Denominations>Methodist & related churches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('288','Religion>Christian Denominations>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('289','Religion>Christian Denominations>Other denominations & sects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('289.6','Religion>Christian Denominations>Quakers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('290','Religion>Other Religions>Other religions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('291','Religion>Other Religions>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('292','Religion>Other Religions>Greek & Roman religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('293','Religion>Other Religions>Germanic religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('294','Religion>Other Religions>Religions of Indic origin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('294.3','Religion>Other Religions>Buddhism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('295','Religion>Other Religions>Zoroastrianism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('296','Religion>Other Religions>Judaism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('296.43','Religion>Other Religions>Jewish holidays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('296.432','Religion>Other Religions>Yom Kippur');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('297','Religion>Other Religions>Islam');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('297.082','Religion>Other Religions>Muslims');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('297.122','Religion>Other Religions>Koran');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('298','Religion>Other Religions>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('299','Religion>Other Religions>Religions not provided for elsewhere');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('299.7','Religion>Other Religions>Native American religions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('3','Social Sciences');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('30','Social Sciences>Social Sciences, Sociology, Anthropology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('300','Social Sciences>Social Sciences, Sociology, Anthropology>Social sciences, sociology & anthropology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('301','Social Sciences>Social Sciences, Sociology, Anthropology>Mankind');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302','Social Sciences>Social Sciences, Sociology, Anthropology>Interpersonal relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.2','Social Sciences>Social Sciences, Sociology, Anthropology>Communication');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.224','Social Sciences>Social Sciences, Sociology, Anthropology>Listening');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.23','Social Sciences>Social Sciences, Sociology, Anthropology>Mass media');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.24','Social Sciences>Social Sciences, Sociology, Anthropology>Gossip (social psychology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.3','Social Sciences>Social Sciences, Sociology, Anthropology>Bullying');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.34','Social Sciences>Social Sciences, Sociology, Anthropology>Gangs (social psychology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('302.54','Social Sciences>Social Sciences, Sociology, Anthropology>Aggression');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('303','Social Sciences>Social Sciences, Sociology, Anthropology>Social processes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('303.34','Social Sciences>Social Sciences, Sociology, Anthropology>Leadership');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('303.482','Social Sciences>Social Sciences, Sociology, Anthropology>International relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('303.4833','Social Sciences>Social Sciences, Sociology, Anthropology>Information');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('303.61','Social Sciences>Social Sciences, Sociology, Anthropology>Nonviolence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('303.625','Social Sciences>Social Sciences, Sociology, Anthropology>Terrorism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('304','Social Sciences>Social Sciences, Sociology, Anthropology>Factors affecting social behavior');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('304.645','Social Sciences>Social Sciences, Sociology, Anthropology>Life expectancy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305','Social Sciences>Social Sciences, Sociology, Anthropology>Discrimination');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.23','Social Sciences>Social Sciences, Sociology, Anthropology>Boys');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.232','Social Sciences>Social Sciences, Sociology, Anthropology>Infants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.235','Social Sciences>Social Sciences, Sociology, Anthropology>Adolescence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.26','Social Sciences>Social Sciences, Sociology, Anthropology>Elderly persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.31','Social Sciences>Social Sciences, Sociology, Anthropology>Males (human)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.4','Social Sciences>Social Sciences, Sociology, Anthropology>Females (human)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.55','Social Sciences>Social Sciences, Sociology, Anthropology>Middle class');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.56','Social Sciences>Social Sciences, Sociology, Anthropology>Minorities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.569','Social Sciences>Social Sciences, Sociology, Anthropology>Homeless persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.6','Social Sciences>Social Sciences, Sociology, Anthropology>Religious groups');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.8','Social Sciences>Social Sciences, Sociology, Anthropology>Racial groups');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.891497','Social Sciences>Social Sciences, Sociology, Anthropology>Romanies--social aspects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.896','Social Sciences>Social Sciences, Sociology, Anthropology>African Americans (Culture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.896073','Social Sciences>Social Sciences, Sociology, Anthropology>African Americans--social');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.897','Social Sciences>Social Sciences, Sociology, Anthropology>American native');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.897415','Social Sciences>Social Sciences, Sociology, Anthropology>Mayas--social aspects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.89915','Social Sciences>Social Sciences, Sociology, Anthropology>Australian aborigines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.899442','Social Sciences>Social Sciences, Sociology, Anthropology>Maori (New Zealand people)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.906','Social Sciences>Social Sciences, Sociology, Anthropology>Aliens');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('305.908','Social Sciences>Social Sciences, Sociology, Anthropology>Deaf persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306','Social Sciences>Social Sciences, Sociology, Anthropology>Social Sciences, Sociology, Anthropology>Culture and Institutions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.3','Social Sciences>Social Sciences, Sociology, Anthropology>Economic institutions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.3620973','Social Sciences>Social Sciences, Sociology, Anthropology>Slavery--United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.38','Social Sciences>Social Sciences, Sociology, Anthropology>Retirement');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.42','Social Sciences>Social Sciences, Sociology, Anthropology>Knowledge (sociology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.43','Social Sciences>Social Sciences, Sociology, Anthropology>Education--sociology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.482','Social Sciences>Social Sciences, Sociology, Anthropology>Gambling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.7','Social Sciences>Social Sciences, Sociology, Anthropology>Sexuality');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.734','Social Sciences>Social Sciences, Sociology, Anthropology>Courtship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.736','Social Sciences>Social Sciences, Sociology, Anthropology>Extramarital relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.765','Social Sciences>Social Sciences, Sociology, Anthropology>Bisexuality');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.766','Social Sciences>Social Sciences, Sociology, Anthropology>Homosexuality');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.8','Social Sciences>Social Sciences, Sociology, Anthropology>Marriage & family');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.81','Social Sciences>Social Sciences, Sociology, Anthropology>Marriage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.82','Social Sciences>Social Sciences, Sociology, Anthropology>Mate selection (sociology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.83','Social Sciences>Social Sciences, Sociology, Anthropology>Kinship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.84','Social Sciences>Social Sciences, Sociology, Anthropology>Remarriage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.842','Social Sciences>Social Sciences, Sociology, Anthropology>Monogamy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.848','Social Sciences>Social Sciences, Sociology, Anthropology>Gay marriage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.85','Social Sciences>Social Sciences, Sociology, Anthropology>Families');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.856','Social Sciences>Social Sciences, Sociology, Anthropology>Unmarried parents');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.857','Social Sciences>Social Sciences, Sociology, Anthropology>Extended family');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.872','Social Sciences>Social Sciences, Sociology, Anthropology>Married persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.874','Social Sciences>Social Sciences, Sociology, Anthropology>Biological Parents');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.875','Social Sciences>Social Sciences, Sociology, Anthropology>Quintuplets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.877','Social Sciences>Social Sciences, Sociology, Anthropology>Incest');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.883','Social Sciences>Social Sciences, Sociology, Anthropology>Widows');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.89','Social Sciences>Social Sciences, Sociology, Anthropology>Divorce');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('306.9','Social Sciences>Social Sciences, Sociology, Anthropology>Death');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('307','Social Sciences>Social Sciences, Sociology, Anthropology>Communities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('307.76','Social Sciences>Social Sciences, Sociology, Anthropology>Cities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('308','Social Sciences>Social Sciences, Sociology, Anthropology>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('309','Social Sciences>Social Sciences, Sociology, Anthropology>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('310','Social Sciences>Statistics>Statistics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('311','Social Sciences>Statistics>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('312','Social Sciences>Statistics>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('313','Social Sciences>Statistics>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('314','Social Sciences>Statistics>Almanacs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('315','Social Sciences>Statistics>General statistics of Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('316','Social Sciences>Statistics>General statistics of Africa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('317','Social Sciences>Statistics>General statistics of North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('318','Social Sciences>Statistics>General statistics of South America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('319','Social Sciences>Statistics>General statistics of other areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320','Social Sciences>Political Science>Political science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.1','Social Sciences>Political Science>States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.4','Social Sciences>Political Science>Civics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.473','Social Sciences>Political Science>United States (Government)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.51','Social Sciences>Political Science>Liberalism (political ideology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.54','Social Sciences>Political Science>Nationalism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.8','Social Sciences>Political Science>Local government');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('320.854','Social Sciences>Political Science>Mayors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('321','Social Sciences>Political Science>Systems of governments & states');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('321.07','Social Sciences>Political Science>Utopias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('321.8','Social Sciences>Political Science>Democracy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('322','Social Sciences>Political Science>Relation of state to organized groups');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('322.1','Social Sciences>Political Science>Church and state');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323','Social Sciences>Political Science>Civil rights');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323.44','Social Sciences>Political Science>Freedom of expression');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323.442','Social Sciences>Political Science>Freedom of religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323.443','Social Sciences>Political Science>Freedom of speech');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323.445','Social Sciences>Political Science>Freedom of information');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323.47','Social Sciences>Political Science>Freedom of association');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('323.6','Social Sciences>Political Science>Citizenship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('324','Social Sciences>Political Science>Elections');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('324.64','Social Sciences>Political Science>Voter registration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('324.65','Social Sciences>Political Science>Ballots');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('324.9','Social Sciences>Political Science>Campaigns (Politics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('325','Social Sciences>Political Science>International migration & colonization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('325.3','Social Sciences>Political Science>Colonization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('325.373','Social Sciences>Political Science>Colonization by the');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('326','Social Sciences>Political Science>Slavery & emancipation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('326.0973','Social Sciences>Political Science>Slavery and');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('327','Social Sciences>Political Science>Foreign relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('327.12','Social Sciences>Political Science>Intelligence (information)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('327.127','Social Sciences>Political Science>Central Intelligence Agency');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('327.2','Social Sciences>Political Science>Diplomacy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('327.73','Social Sciences>Political Science>Foreign relations—United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('328','Social Sciences>Political Science>Legislative branch');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('328.092','Social Sciences>Political Science>Legislators (biography)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('328.38','Social Sciences>Political Science>Legislative lobbying');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('329','Social Sciences>Political Science>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('330','Social Sciences>Economics>Economics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('330.122','Social Sciences>Economics>Capitalism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('330.16','Social Sciences>Economics>Wealth');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('330.9','Social Sciences>Economics>Economic situation &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331','Social Sciences>Economics>Labor');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.11','Social Sciences>Economics>Employees');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.137','Social Sciences>Economics>Unemployment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.21','Social Sciences>Economics>Wages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.216','Social Sciences>Economics>Tipping (economics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.257','Social Sciences>Economics>Vacations (labor economics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.398','Social Sciences>Economics>Older  workers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.44','Social Sciences>Economics>Maternity leave');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.544','Social Sciences>Economics>Migrant  workers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.7','Social Sciences>Economics>Occupations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.702','Social Sciences>Economics>Career Guidance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.88','Social Sciences>Economics>Labor  unions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.889','Social Sciences>Economics>Labor grievances');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('331.893','Social Sciences>Economics>Labor  violence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332','Social Sciences>Economics>Finance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.024','Social Sciences>Economics>Debt management (personal)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.041','Social Sciences>Economics>Capital');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.1','Social Sciences>Economics>Banking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.4','Social Sciences>Economics>Currency');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.404','Social Sciences>Economics>Gold coins');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.6','Social Sciences>Economics>Investing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.632','Social Sciences>Economics>Mutual funds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.7','Social Sciences>Economics>Loans');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.72','Social Sciences>Economics>Mortgages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.75','Social Sciences>Economics>Bankruptcy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('332.765','Social Sciences>Economics>Credit cards');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333','Social Sciences>Economics>Land');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.338','Social Sciences>Economics>Real Estate');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.7','Social Sciences>Economics>Environment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.74','Social Sciences>Economics>Meadows');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.75','Social Sciences>Economics>Forests');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.782','Social Sciences>Economics>Wilderness areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.79','Social Sciences>Economics>Energy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.792','Social Sciences>Economics>Nuclear energy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.793','Social Sciences>Economics>Electricity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.911','Social Sciences>Economics>Water conservation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.95','Social Sciences>Economics>Biodiversity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('333.954','Social Sciences>Economics>Wildlife management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('334','Social Sciences>Economics>Cooperatives');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('335','Social Sciences>Economics>Socialism & related systems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('335.4','Social Sciences>Economics>Communism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('335.409','Social Sciences>Economics>Marxists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('335.6','Social Sciences>Economics>Fascism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('336','Social Sciences>Economics>Public finance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('336.24','Social Sciences>Economics>Income tax');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('336.271','Social Sciences>Economics>Luxury tax');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('336.276','Social Sciences>Economics>Inheritance tax');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('336.343','Social Sciences>Economics>National debt');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('337','Social Sciences>Economics>International economics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338','Social Sciences>Economics>Industry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.02','Social Sciences>Economics>Commodities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.092','Social Sciences>Economics>Managers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.13','Social Sciences>Economics>Farm costs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.17','Social Sciences>Economics>Farm produce');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.174','Social Sciences>Economics>Timber');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.522','Social Sciences>Economics>Fair  trade');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.604','Social Sciences>Economics>Competition');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.65','Social Sciences>Economics>Factories (organization ofproduction)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('338.83','Social Sciences>Economics>Mergers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('339','Social Sciences>Economics>Macroeconomics & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('339.32','Social Sciences>Economics>Income');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('340','Social Sciences>Law>Law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('340.092','Social Sciences>Law>Attorneys');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('340.11','Social Sciences>Law>Justice (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('341','Social Sciences>Law>Law of nations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('341.353','Social Sciences>Law>Kale');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('341.37','Social Sciences>Law>Treaties');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('341.371','Social Sciences>Law>Yogurt');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('342','Social Sciences>Law>Constitutional & administrative law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('342.05','Social Sciences>Law>Legislative branch (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('342.084','Social Sciences>Law>Marketing (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('342.085','Social Sciences>Law>Fetus (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('343','Social Sciences>Law>Military, tax, trade & industrial law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('343.052','Social Sciences>Law>Taxes (income)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('343.07','Social Sciences>Law>Industrial law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('344','Social Sciences>Law>Labor, social, education & cultural law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('344.01','Social Sciences>Law>Labor (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('344.022','Social Sciences>Law>National health insurance(law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('344.041','Social Sciences>Law>Midwives (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('344.053','Social Sciences>Law>Guns (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('345','Social Sciences>Law>Criminal law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('345.025','Social Sciences>Law>Manslaughter (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('345.052','Social Sciences>Law>Search and seizure(law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346','Social Sciences>Law>Private law');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.013','Social Sciences>Law>Disability (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.017','Social Sciences>Law>Joint custody');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.02','Social Sciences>Law>Contracts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.03','Social Sciences>Law>Torts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.033','Social Sciences>Law>False arrest');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.043','Social Sciences>Law>Water rights');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.066','Social Sciences>Law>Incorporation (law)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.36','Social Sciences>Law>Juvenile justice');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('346.73','Social Sciences>Law>Copyright and Patents');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('347','Social Sciences>Law>Civil procedure & courts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('347.013','Social Sciences>Law>Court records');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('347.014','Social Sciences>Law>Judges');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('347.075','Social Sciences>Law>Juries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('348','Social Sciences>Law>Laws, regulations & cases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('348.044','Social Sciences>Law>Court decisions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('349','Social Sciences>Law>Law of specific jurisdictions & areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('350','Social Sciences>Public Administration and Military Science>Public administration & military science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('351','Social Sciences>Public Administration and Military Science>Civil service');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('352','Social Sciences>Public Administration and Military Science>General considerations of public administration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('352.74','Social Sciences>Public Administration and Military Science>Knowledge (public administrativesupport)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('352.84','Social Sciences>Public Administration and Military Science>Incorporation (public administration)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('353','Social Sciences>Public Administration and Military Science>Specific fields of public administration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('353.53','Social Sciences>Public Administration and Military Science>Equal opportunity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('354','Social Sciences>Public Administration and Military Science>Administration of economy & environment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355','Social Sciences>Public Administration and Military Science>Military');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.02','Social Sciences>Public Administration and Military Science>War');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.021','Social Sciences>Public Administration and Military Science>Nuclear  warfare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.1','Social Sciences>Public Administration and Military Science>Military life & customs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.22','Social Sciences>Public Administration and Military Science>Human resources');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.23','Social Sciences>Public Administration and Military Science>Civilian workers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.33','Social Sciences>Public Administration and Military Science>Personnel & their hierarchy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.34','Social Sciences>Public Administration and Military Science>Noncombat services');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.37','Social Sciences>Public Administration and Military Science>National guards');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.4','Social Sciences>Public Administration and Military Science>Combat');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.5','Social Sciences>Public Administration and Military Science>Military training');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.54','Social Sciences>Public Administration and Military Science>Basic training');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.6','Social Sciences>Public Administration and Military Science>Military administration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.621','Social Sciences>Public Administration and Military Science>Supply administration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.7','Social Sciences>Public Administration and Military Science>Military installations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.8','Social Sciences>Public Administration and Military Science>Military equipment &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.82','Social Sciences>Public Administration and Military Science>Specific kinds of weapons (ordnance)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('355.824','Social Sciences>Public Administration and Military Science>Machine guns');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('356','Social Sciences>Public Administration and Military Science>Infantry forces & warfare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('357','Social Sciences>Public Administration and Military Science>Mounted forces & warfare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358','Social Sciences>Public Administration and Military Science>Air & other specialized forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.1','Social Sciences>Public Administration and Military Science>Missile forces and army artillery & armored forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.12','Social Sciences>Public Administration and Military Science>Army artillery forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.13','Social Sciences>Public Administration and Military Science>Antiaircraft artillery forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.16','Social Sciences>Public Administration and Military Science>Coast artillery forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.17','Social Sciences>Public Administration and Military Science>Guided missile forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.18','Social Sciences>Public Administration and Military Science>Armored forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.2','Social Sciences>Public Administration and Military Science>Army engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.3','Social Sciences>Public Administration and Military Science>Weapons of massdestruction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.38','Social Sciences>Public Administration and Military Science>Germ  warfare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.4','Social Sciences>Public Administration and Military Science>Air forces & warfare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('358.8','Social Sciences>Public Administration and Military Science>Space forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359','Social Sciences>Public Administration and Military Science>Sea forces & warfare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.009','Social Sciences>Public Administration and Military Science>Naval history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.1','Social Sciences>Public Administration and Military Science>Navy life');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.338','Social Sciences>Public Administration and Military Science>Seamen');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.6','Social Sciences>Public Administration and Military Science>Naval administration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.7','Social Sciences>Public Administration and Military Science>Naval installations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.8','Social Sciences>Public Administration and Military Science>Naval equipment & supplies and Naval weapons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.82','Social Sciences>Public Administration and Military Science>Specific kinds of weapons (ordnance)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.83','Social Sciences>Public Administration and Military Science>Transportation equipment & supplies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.93','Social Sciences>Public Administration and Military Science>Submarine forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.938','Social Sciences>Public Administration and Military Science>Submarines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.94','Social Sciences>Public Administration and Military Science>Naval air forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.96','Social Sciences>Public Administration and Military Science>Marine forces');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('359.97','Social Sciences>Public Administration and Military Science>Coast guard');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('360','Social Sciences>Social Problems and Social Services>Social problems & social services');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('361','Social Sciences>Social Problems and Social Services>Social problems & social welfare in general');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('361.05','Social Sciences>Social Problems and Social Services>Financial aid');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('361.06','Social Sciences>Social Problems and Social Services>Counseling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('361.706','Social Sciences>Social Problems and Social Services>Fundraising');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362','Social Sciences>Social Problems and Social Services>Social welfare problems & services');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1','Social Sciences>Social Problems and Social Services>Health care');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1042','Social Sciences>Social Problems and Social Services>Diseases (Human)--social');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.10723','Social Sciences>Social Problems and Social Services>Health');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.108','Social Sciences>Social Problems and Social Services>Services to');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.109','Social Sciences>Social Problems and Social Services>Diseases (Human)--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.11','Social Sciences>Social Problems and Social Services>Hospitals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1109','Social Sciences>Social Problems and Social Services>Hospitals & related');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.16','Social Sciences>Social Problems and Social Services>Extended care facilities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.173','Social Sciences>Social Problems and Social Services>Nurses--health services');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.17309','Social Sciences>Social Problems and Social Services>Nurses--health services--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.178','Social Sciences>Social Problems and Social Services>Rehabilitation (health services)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1783','Social Sciences>Social Problems and Social Services>Organ & tissue banks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.18','Social Sciences>Social Problems and Social Services>Medical emergencies (socialservices)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196','Social Sciences>Social Problems and Social Services>AIDS (disease)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196044','Social Sciences>Social Problems and Social Services>Chronic diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196044009','Social Sciences>Social Problems and Social Services>Chronic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1960754','Social Sciences>Social Problems and Social Services>Physical diagnosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1960757','Social Sciences>Social Problems and Social Services>Radiological diagnosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19607575','Social Sciences>Social Problems and Social Services>Radioisotope scanning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1961','Social Sciences>Social Problems and Social Services>Diseases of cardiovascular system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1961009','Social Sciences>Social Problems and Social Services>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19615','Social Sciences>Social Problems and Social Services>Diseases of blood');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19615009','Social Sciences>Social Problems and Social Services>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1962','Social Sciences>Social Problems and Social Services>Diseases of respiratory system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1962009','Social Sciences>Social Problems and Social Services>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19621','Social Sciences>Social Problems and Social Services>Diseases of nose, larynx,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19622','Social Sciences>Social Problems and Social Services>Diseases of larynx, glottis,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1963','Social Sciences>Social Problems and Social Services>Diseases of digestive system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1963009','Social Sciences>Social Problems and Social Services>Diseases of digestive');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19639','Social Sciences>Social Problems and Social Services>Nutritional & metabolic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1964','Social Sciences>Social Problems and Social Services>Endocrine system--human diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1964009','Social Sciences>Social Problems and Social Services>Endocrine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19642','Social Sciences>Social Problems and Social Services>Diseases of lymphatic system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19642009','Social Sciences>Social Problems and Social Services>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1965','Social Sciences>Social Problems and Social Services>Diseases of integument, hair, nails');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1965009','Social Sciences>Social Problems and Social Services>Diseases of integument,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1966','Social Sciences>Social Problems and Social Services>Diseases of the urogenital system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1966009','Social Sciences>Social Problems and Social Services>Diseases of the');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1967','Social Sciences>Social Problems and Social Services>Diseases of musculoskeletal system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1967009','Social Sciences>Social Problems and Social Services>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19677','Social Sciences>Social Problems and Social Services>Diseases of connective tissues');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1968','Social Sciences>Social Problems and Social Services>Diseases of nervous system & mental');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1968009','Social Sciences>Social Problems and Social Services>Diseases of nervous');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1969','Social Sciences>Social Problems and Social Services>Other diseases;\');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1969009','Social Sciences>Social Problems and Social Services>Other diseases;\');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19692','Social Sciences>Social Problems and Social Services>Bacterial &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196925','Social Sciences>Social Problems and Social Services>Viral diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196951','Social Sciences>Social Problems and Social Services>Sexually');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19696','Social Sciences>Social Problems and Social Services>Parasitic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1969792','Social Sciences>Social Problems and Social Services>Acquired immune deficiency');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196980213','Social Sciences>Social Problems and Social Services>Aviation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196980214','Social Sciences>Social Problems and Social Services>Space medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1969803','Social Sciences>Social Problems and Social Services>Industrial');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1969883','Social Sciences>Social Problems and Social Services>Tropical');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196989','Social Sciences>Social Problems and Social Services>Diseases due to');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.196995','Social Sciences>Social Problems and Social Services>Tuberculosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.197','Social Sciences>Social Problems and Social Services>Surgery & related medical specialties');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.197009','Social Sciences>Social Problems and Social Services>Surgery--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19705','Social Sciences>Social Problems and Social Services>Surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1971','Social Sciences>Social Problems and Social Services>Injuries &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19741','Social Sciences>Social Problems and Social Services>Cardiovascular system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19743','Social Sciences>Social Problems and Social Services>Digestive system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19744','Social Sciences>Social Problems and Social Services>Endocrine system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19746','Social Sciences>Social Problems and Social Services>Urogenital system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19747','Social Sciences>Social Problems and Social Services>Musculoskeletal system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.197477','Social Sciences>Social Problems and Social Services>Skin--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19748','Social Sciences>Social Problems and Social Services>Nervous system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19751','Social Sciences>Social Problems and Social Services>Otorhinolaryngology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.197522','Social Sciences>Social Problems and Social Services>Oral region');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19754','Social Sciences>Social Problems and Social Services>Respiratory system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1976','Social Sciences>Social Problems and Social Services>Dentistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1976009','Social Sciences>Social Problems and Social Services>Dentistry--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1977','Social Sciences>Social Problems and Social Services>Ophthalmology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1977009','Social Sciences>Social Problems and Social Services>Ophthalmology--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1978','Social Sciences>Social Problems and Social Services>Otology & audiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19791','Social Sciences>Social Problems and Social Services>Operative surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19795','Social Sciences>Social Problems and Social Services>Plastic surgery and Organ Transplants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19796','Social Sciences>Social Problems and Social Services>Anesthesiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19797','Social Sciences>Social Problems and Social Services>Geriatric surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19798','Social Sciences>Social Problems and Social Services>Pediatric surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19799','Social Sciences>Social Problems and Social Services>Military');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.198','Social Sciences>Social Problems and Social Services>Geriatric disorders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1981','Social Sciences>Social Problems and Social Services>Gynecology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19814','Social Sciences>Social Problems and Social Services>Diseases of uterus');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19819','Social Sciences>Social Problems and Social Services>Diseases of breast');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1982','Social Sciences>Social Problems and Social Services>Obstetrics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1982009','Social Sciences>Social Problems and Social Services>Obstetrics--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1983','Social Sciences>Social Problems and Social Services>Diseases & complications of pregnancy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1984','Social Sciences>Social Problems and Social Services>Childbirth (Parturition)--Labor');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1985','Social Sciences>Social Problems and Social Services>Complicated labor (Dystocia)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1986','Social Sciences>Social Problems and Social Services>Normal puerperium');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1987','Social Sciences>Social Problems and Social Services>Puerperal diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.1988','Social Sciences>Social Problems and Social Services>Obstetrical surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19892','Social Sciences>Social Problems and Social Services>Pediatrics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.198920009','Social Sciences>Social Problems and Social Services>Pediatrics--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.19897','Social Sciences>Social Problems and Social Services>Geriatric disorders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.2','Social Sciences>Social Problems and Social Services>Mental illness');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.25','Social Sciences>Social Problems and Social Services>Anorexia Nervosa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.26','Social Sciences>Social Problems and Social Services>Psychoses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.28','Social Sciences>Social Problems and Social Services>Suicide');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.29','Social Sciences>Social Problems and Social Services>Addiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.291','Social Sciences>Social Problems and Social Services>Codependency');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.292','Social Sciences>Social Problems and Social Services>Alcoholism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.293','Social Sciences>Social Problems and Social Services>Narcotics abuse');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.296','Social Sciences>Social Problems and Social Services>Tobacco abuse');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.299','Social Sciences>Social Problems and Social Services>Caffeine Abuse');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.3','Social Sciences>Social Problems and Social Services>Mental retardation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.712','Social Sciences>Social Problems and Social Services>Day care');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.734','Social Sciences>Social Problems and Social Services>Adoption');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.76','Social Sciences>Social Problems and Social Services>Child abuse');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.828','Social Sciences>Social Problems and Social Services>Marriage counseling (socialwelfare)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.829','Social Sciences>Social Problems and Social Services>Domestic  violence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('362.86','Social Sciences>Social Problems and Social Services>Veterans');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363','Social Sciences>Social Problems and Social Services>Other social problems & services');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.1','Social Sciences>Social Problems and Social Services>Safety');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.11','Social Sciences>Social Problems and Social Services>Industrial accidents');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.17','Social Sciences>Social Problems and Social Services>Hazardous materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.232','Social Sciences>Social Problems and Social Services>Arrest');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.252','Social Sciences>Social Problems and Social Services>Secret agents');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.31','Social Sciences>Social Problems and Social Services>Censorship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.348','Social Sciences>Social Problems and Social Services>Disaster relief');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.37','Social Sciences>Social Problems and Social Services>Fire safety');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.45','Social Sciences>Social Problems and Social Services>Narcotics  traffic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.46','Social Sciences>Social Problems and Social Services>Abortion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.5','Social Sciences>Social Problems and Social Services>Housing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.583','Social Sciences>Social Problems and Social Services>Home ownership');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.68','Social Sciences>Social Problems and Social Services>National parks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.69','Social Sciences>Social Problems and Social Services>Historic buildings (preservation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.7','Social Sciences>Social Problems and Social Services>Environmental');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.728','Social Sciences>Social Problems and Social Services>Garbage disposal');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.735','Social Sciences>Social Problems and Social Services>Radioactive pollution');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.738','Social Sciences>Social Problems and Social Services>Global  warming');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.739','Social Sciences>Social Problems and Social Services>Air Pollution');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.75','Social Sciences>Social Problems and Social Services>Cemeteries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.8','Social Sciences>Social Problems and Social Services>Nutrition');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('363.96','Social Sciences>Social Problems and Social Services>Family planning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364','Social Sciences>Social Problems and Social Services>Crime');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.106','Social Sciences>Social Problems and Social Services>Gangs (criminology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.131','Social Sciences>Social Problems and Social Services>Treason');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.133','Social Sciences>Social Problems and Social Services>Counterfeiting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.138','Social Sciences>Social Problems and Social Services>War crimes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.151','Social Sciences>Social Problems and Social Services>Genocide');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.152','Social Sciences>Social Problems and Social Services>Manslaughter');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.155','Social Sciences>Social Problems and Social Services>Hijacking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.156','Social Sciences>Social Problems and Social Services>Libel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.162','Social Sciences>Social Problems and Social Services>Shoplifting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.163','Social Sciences>Social Problems and Social Services>Forgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.164','Social Sciences>Social Problems and Social Services>Sabotage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.165','Social Sciences>Social Problems and Social Services>Extortion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.168','Social Sciences>Social Problems and Social Services>Computer crimes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.172','Social Sciences>Social Problems and Social Services>Gambling (criminology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.36','Social Sciences>Social Problems and Social Services>Juvenile delinquency');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('364.66','Social Sciences>Social Problems and Social Services>Death penalty');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('365','Social Sciences>Social Problems and Social Services>Penal & related institutions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('365.34','Social Sciences>Social Problems and Social Services>Jails');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('365.641','Social Sciences>Social Problems and Social Services>Escapes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('366','Social Sciences>Social Problems and Social Services>Associations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('367','Social Sciences>Social Problems and Social Services>Clubs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('368','Social Sciences>Social Problems and Social Services>Insurance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('368.32','Social Sciences>Social Problems and Social Services>Life insurance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('368.382','Social Sciences>Social Problems and Social Services>Health insurance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('368.42','Social Sciences>Social Problems and Social Services>National health insurance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('368.44','Social Sciences>Social Problems and Social Services>Unemployment compensation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('369','Social Sciences>Social Problems and Social Services>Miscellaneous kinds of associations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370','Social Sciences>Education>Education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.1','Social Sciences>Education>Philosophy & theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.11','Social Sciences>Education>Education for specific');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.113','Social Sciences>Education>Career Development');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.15','Social Sciences>Education>Educational psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.3','Social Sciences>Education>Education--Dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.5','Social Sciences>Education>Education--Periodicals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.7','Social Sciences>Education>Education, research, related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.8','Social Sciences>Education>History & description with respect to');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('370.9','Social Sciences>Education>Historical, geographic, persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371','Social Sciences>Education>Schools & their activities and special education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.1','Social Sciences>Education>Faculty');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.302','Social Sciences>Education>Homework');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.32','Social Sciences>Education>Textbooks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.356','Social Sciences>Education>Correspondence courses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.384','Social Sciences>Education>Field  trips');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.394','Social Sciences>Education>Independent study');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.8','Social Sciences>Education>Extracurricular activities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.82','Social Sciences>Education>Specific kinds of students');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('371.926','Social Sciences>Education>Learning Disabilities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372','Social Sciences>Education>Elementary education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.218','Social Sciences>Education>Kindergarten');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.414','Social Sciences>Education>Reading readiness');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.47','Social Sciences>Education>Reading comprehension');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.6','Social Sciences>Education>Language elementary education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.623','Social Sciences>Education>Writing skills');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.634','Social Sciences>Education>Handwriting (elementary education)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('372.66','Social Sciences>Education>Oral presentations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('373','Social Sciences>Education>Secondary education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('374','Social Sciences>Education>Adult education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('375','Social Sciences>Education>Curriculums');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('376','Social Sciences>Education>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('377','Social Sciences>Education>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('378','Social Sciences>Education>Higher education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('378.1','Social Sciences>Education>Organization &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('378.154','Social Sciences>Education>Colleges');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('378.2','Social Sciences>Education>Academic degrees &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('378.3','Social Sciences>Education>Grants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('378.4','Social Sciences>Education>Higher education--Europe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('379','Social Sciences>Education>Public policy issues in education');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('380','Social Sciences>Commerce, Communications and Transportation>Commerce, communications & transportation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381','Social Sciences>Commerce, Communications and Transportation>Commerce');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.12','Social Sciences>Commerce, Communications and Transportation>Chain stores');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.13','Social Sciences>Commerce, Communications and Transportation>Franchises');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.142','Social Sciences>Commerce, Communications and Transportation>Internet shopping');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.15','Social Sciences>Commerce, Communications and Transportation>Outlet stores');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.17','Social Sciences>Commerce, Communications and Transportation>Auctions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.19','Social Sciences>Commerce, Communications and Transportation>Thrift shops');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.195','Social Sciences>Commerce, Communications and Transportation>Garage sales');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('381.33','Social Sciences>Commerce, Communications and Transportation>Consumer information');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('382','Social Sciences>Commerce, Communications and Transportation>Foreign  trade');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('382.7','Social Sciences>Commerce, Communications and Transportation>Export tax');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('383','Social Sciences>Commerce, Communications and Transportation>Postal communication');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('383.122','Social Sciences>Commerce, Communications and Transportation>Correspondence (letters)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('384','Social Sciences>Commerce, Communications and Transportation>Communications and telecommunication');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('384.5','Social Sciences>Commerce, Communications and Transportation>Radio (communication)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('384.54','Social Sciences>Commerce, Communications and Transportation>Amateur Radio');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('384.55','Social Sciences>Commerce, Communications and Transportation>Television');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('384.558','Social Sciences>Commerce, Communications and Transportation>Video recordings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('385','Social Sciences>Commerce, Communications and Transportation>Railroads');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('385.36','Social Sciences>Commerce, Communications and Transportation>Locomotives');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('386','Social Sciences>Commerce, Communications and Transportation>Inland waterway & ferry transportation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('386.229','Social Sciences>Commerce, Communications and Transportation>Canoes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387','Social Sciences>Commerce, Communications and Transportation>Water  transportation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.1','Social Sciences>Commerce, Communications and Transportation>Seaports');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.155','Social Sciences>Commerce, Communications and Transportation>Lighthouses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.2','Social Sciences>Commerce, Communications and Transportation>Ships');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.204','Social Sciences>Commerce, Communications and Transportation>Sailing ships');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.231','Social Sciences>Commerce, Communications and Transportation>Inboardoutboard motorboats');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.232','Social Sciences>Commerce, Communications and Transportation>Tugboats');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.245','Social Sciences>Commerce, Communications and Transportation>Cargo Ships');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.5','Social Sciences>Commerce, Communications and Transportation>Marine  transportation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.7','Social Sciences>Commerce, Communications and Transportation>Aviation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.73','Social Sciences>Commerce, Communications and Transportation>Aircraft');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('387.733','Social Sciences>Commerce, Communications and Transportation>Jet planes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388','Social Sciences>Commerce, Communications and Transportation>Transportation and ground transportation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.04','Social Sciences>Commerce, Communications and Transportation>Vehicles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.042','Social Sciences>Commerce, Communications and Transportation>Mass  transit');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.1','Social Sciences>Commerce, Communications and Transportation>Roads');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.13','Social Sciences>Commerce, Communications and Transportation>Tunnels');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.132','Social Sciences>Commerce, Communications and Transportation>Bridges');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.312','Social Sciences>Commerce, Communications and Transportation>Traffic signs/signals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.321','Social Sciences>Commerce, Communications and Transportation>Limousine service');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.34','Social Sciences>Commerce, Communications and Transportation>Land  vehicles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.342','Social Sciences>Commerce, Communications and Transportation>Cars');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.344','Social Sciences>Commerce, Communications and Transportation>Trucks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.346','Social Sciences>Commerce, Communications and Transportation>Motor homes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('388.347','Social Sciences>Commerce, Communications and Transportation>Motorcycles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('389','Social Sciences>Commerce, Communications and Transportation>Metrology & standardization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('390','Social Sciences>Customs, Etiquette and Folklore>Customs, etiquette & folklore');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391','Social Sciences>Customs, Etiquette and Folklore>Clothing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.1','Social Sciences>Customs, Etiquette and Folklore>Men''s clothing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.2','Social Sciences>Customs, Etiquette and Folklore>Dresses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.41','Social Sciences>Customs, Etiquette and Folklore>Ties (neckwear)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.413','Social Sciences>Customs, Etiquette and Folklore>Footwear');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.42','Social Sciences>Customs, Etiquette and Folklore>Lingerie');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.434','Social Sciences>Customs, Etiquette and Folklore>Masks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.44','Social Sciences>Customs, Etiquette and Folklore>Handbags');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.65','Social Sciences>Customs, Etiquette and Folklore>Tattooing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('391.7','Social Sciences>Customs, Etiquette and Folklore>Jewelry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('392','Social Sciences>Customs, Etiquette and Folklore>Maternity garments');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('392.3','Social Sciences>Customs, Etiquette and Folklore>Family life (customs)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('392.4','Social Sciences>Customs, Etiquette and Folklore>Engagement (betrothal)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('392.5','Social Sciences>Customs, Etiquette and Folklore>Honeymoons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('392.54','Social Sciences>Customs, Etiquette and Folklore>Wedding clothes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('393','Social Sciences>Customs, Etiquette and Folklore>Death customs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('393.3','Social Sciences>Customs, Etiquette and Folklore>Mummies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('393.9','Social Sciences>Customs, Etiquette and Folklore>Funerals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394','Social Sciences>Customs, Etiquette and Folklore>General customs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.1','Social Sciences>Customs, Etiquette and Folklore>Toasts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.14','Social Sciences>Customs, Etiquette and Folklore>Smoking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.2','Social Sciences>Customs, Etiquette and Folklore>Celebrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.25','Social Sciences>Customs, Etiquette and Folklore>Mardi Gras');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.26','Social Sciences>Customs, Etiquette and Folklore>Festivals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.261','Social Sciences>Customs, Etiquette and Folklore>Kwanzaa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.264','Social Sciences>Customs, Etiquette and Folklore>Halloween');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.266','Social Sciences>Customs, Etiquette and Folklore>Christmas (customs)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('394.4','Social Sciences>Customs, Etiquette and Folklore>Memorials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('395','Social Sciences>Customs, Etiquette and Folklore>Etiquette');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('395.22','Social Sciences>Customs, Etiquette and Folklore>Weddings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('395.5','Social Sciences>Customs, Etiquette and Folklore>Tipping (etiquette)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('396','Social Sciences>Customs, Etiquette and Folklore>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('397','Social Sciences>Customs, Etiquette and Folklore>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('398','Social Sciences>Customs, Etiquette and Folklore>Folklore');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('398.2','Social Sciences>Customs, Etiquette and Folklore>Fairy Tales');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('398.24','Social Sciences>Customs, Etiquette and Folklore>Fables');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('398.245','Social Sciences>Customs, Etiquette and Folklore>Dragons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('398.6','Social Sciences>Customs, Etiquette and Folklore>Riddles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('398.8','Social Sciences>Customs, Etiquette and Folklore>Nursery rhymes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('399','Social Sciences>Customs, Etiquette and Folklore>Torture (war customs)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('4','Language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('40','Language>Language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('400','Language>Language>Language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('401','Language>Language>Philosophy & theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('401.4','Language>Language>Vocabulary');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('402','Language>Language>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('403','Language>Language>Dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('404','Language>Language>Special topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('405','Language>Language>Serial publications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('406','Language>Language>Organizations & management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('407','Language>Language>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('408','Language>Language>Kinds of persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('409','Language>Language>Geographic & persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('410','Language>Linguistics>Linguistics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('411','Language>Linguistics>Spelling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('411.7','Language>Linguistics>Paleography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('412','Language>Linguistics>Etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('413','Language>Linguistics>Dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('414','Language>Linguistics>Phonology & phonetics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('415','Language>Linguistics>Grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('415.6','Language>Linguistics>Verbs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('416','Language>Linguistics>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('417','Language>Linguistics>Dialectology & historical linguistics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('418','Language>Linguistics>Language  usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('418.4','Language>Linguistics>Speed reading');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('419','Language>Linguistics>Sign Language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('420','Language>English>English & Old English languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('421','Language>English>English writing system & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('422','Language>English>English etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('423','Language>English>English dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('424','Language>English>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('425','Language>English>English grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('426','Language>English>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('427','Language>English>English language variations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('428','Language>English>Standard English usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('429','Language>English>Old English (Anglo-Saxon)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('430','Language>German>German & related languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('431','Language>German>German writing systems & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('432','Language>German>German etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('433','Language>German>German dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('434','Language>German>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('435','Language>German>German grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('436','Language>German>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('437','Language>German>German language variations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('438','Language>German>Standard German usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('439','Language>German>Other Germanic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('439.9','Language>German>East Germanic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('440','Language>French & related languages>French');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('441','Language>French & related languages>French writing systems & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('442','Language>French & related languages>French etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('443','Language>French & related languages>French dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('444','Language>French & related languages>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('445','Language>French & related languages>French grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('446','Language>French & related languages>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('447','Language>French & related languages>French language variations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('448','Language>French & related languages>Standard French usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('449','Language>French & related languages>Occitan & Catalan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('450','Language>Italian, Romanian & related languages>Italian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('451','Language>Italian, Romanian & related languages>Italian writing systems & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('452','Language>Italian, Romanian & related languages>Italian etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('453','Language>Italian, Romanian & related languages>Italian dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('454','Language>Italian, Romanian & related languages>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('455','Language>Italian, Romanian & related languages>Italian grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('456','Language>Italian, Romanian & related languages>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('457','Language>Italian, Romanian & related languages>Italian language variations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('458','Language>Italian, Romanian & related languages>Standard Italian usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('459','Language>Italian, Romanian & related languages>Romanian & related languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('460','Language>Spanish and Portuguese>Spanish');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('461','Language>Spanish and Portuguese>Spanish writing systems & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('462','Language>Spanish and Portuguese>Spanish etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('463','Language>Spanish and Portuguese>Spanish dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('464','Language>Spanish and Portuguese>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('465','Language>Spanish and Portuguese>Spanish grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('466','Language>Spanish and Portuguese>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('467','Language>Spanish and Portuguese>Spanish language variations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('468','Language>Spanish and Portuguese>Learn Spanish');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('469','Language>Spanish and Portuguese>Portuguese');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('470','Language>Latin>Latin & Italic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('471','Language>Latin>Classical Latin writing & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('472','Language>Latin>Classical Latin etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('473','Language>Latin>Classical Latin dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('474','Language>Latin>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('475','Language>Latin>Classical Latin grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('476','Language>Latin>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('477','Language>Latin>Old, postclassical & Vulgar Latin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('478','Language>Latin>Classical Latin usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('479','Language>Latin>Other Italic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('480','Language>Greek>Classical & modern Greek languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('481','Language>Greek>Classical Greek writing & phonology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('482','Language>Greek>Classical Greek etymology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('483','Language>Greek>Classical Greek dictionaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('484','Language>Greek>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('485','Language>Greek>Classical Greek grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('486','Language>Greek>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('487','Language>Greek>Preclassical & postclassical Greek');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('488','Language>Greek>Classical Greek usage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('489','Language>Greek>Other Hellenic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('490','Language>Other Languages>Other languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('491','Language>Other Languages>East Indo-European & Celtic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('491.6','Language>Other Languages>Celtic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('491.7','Language>Other Languages>East');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('491.8','Language>Other Languages>Slavic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('492','Language>Other Languages>Afro-Asiatic and Semitic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('493','Language>Other Languages>Non-Semitic Afro-Asiatic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('493.1','Language>Other Languages>Hieroglyphics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('494','Language>Other Languages>Altaic, Uralic, Hyperborean & Dravidian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('494.4','Language>Other Languages>Samoyedic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('494.5','Language>Other Languages>Finno-Ugric');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('494.6','Language>Other Languages>Ainu language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('494.8','Language>Other Languages>Dravidian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('495','Language>Other Languages>Languages of East & Southeast Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('496','Language>Other Languages>African languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('497','Language>Other Languages>Native American languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('498','Language>Other Languages>South American native languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('499','Language>Other Languages>Austronesian & other languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('499.92','Language>Other Languages>Basque');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('499.94','Language>Other Languages>Etruscan language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('499.95','Language>Other Languages>Sumerian language');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('499.96','Language>Other Languages>Caucasian languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('499.99','Language>Other Languages>Artificial');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('5','Mathematics and Science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('50','Mathematics and Science>General Science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('500','Mathematics and Science>General Science>Science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('501','Mathematics and Science>General Science>Philosophy & theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('502','Mathematics and Science>General Science>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('503','Mathematics and Science>General Science>Dictionaries & encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('504','Mathematics and Science>General Science>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('505','Mathematics and Science>General Science>Serial publications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('506','Mathematics and Science>General Science>Organizations & management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('507','Mathematics and Science>General Science>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('508','Mathematics and Science>General Science>Nature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('508.2','Mathematics and Science>General Science>Autumn');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('509','Mathematics and Science>General Science>Historical, geographic & persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('509.2','Mathematics and Science>General Science>Scientists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('510','Mathematics and Science>Mathematics>Mathematics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('511','Mathematics and Science>Mathematics>General Math');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('511.32','Mathematics and Science>Mathematics>Sets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('511.5','Mathematics and Science>Mathematics>Graphs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('512','Mathematics and Science>Mathematics>Algebra');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('512.788','Mathematics and Science>Mathematics>Imaginary numbers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('512.922','Mathematics and Science>Mathematics>Exponents');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('512.923','Mathematics and Science>Mathematics>Factors (mathematics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('513','Mathematics and Science>Mathematics>Arithmetic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('513.23','Mathematics and Science>Mathematics>Fractions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('513.5','Mathematics and Science>Mathematics>Number system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('514','Mathematics and Science>Mathematics>Topology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('514.742','Mathematics and Science>Mathematics>Fractals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('515','Mathematics and Science>Mathematics>Calculus');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('516','Mathematics and Science>Mathematics>Geometry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('516.152','Mathematics and Science>Mathematics>Lines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('516.154','Mathematics and Science>Mathematics>Triangles (geometry)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('517','Mathematics and Science>Mathematics>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('518','Mathematics and Science>Mathematics>Numerical analysis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('519','Mathematics and Science>Mathematics>Probabilities & applied mathematics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('520','Mathematics and Science>Astronomy>Astronomy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('521','Mathematics and Science>Astronomy>Celestial mechanics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('521.3','Mathematics and Science>Astronomy>Orbits');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('522','Mathematics and Science>Astronomy>Techniques, equipment & materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523','Mathematics and Science>Astronomy>Specific celestial bodies & phenomena');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.113','Mathematics and Science>Astronomy>Milky  Way');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.3','Mathematics and Science>Astronomy>Moon');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.4','Mathematics and Science>Astronomy>Planets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.42','Mathematics and Science>Astronomy>Venus (planet)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.51','Mathematics and Science>Astronomy>Meteorites');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.6','Mathematics and Science>Astronomy>Comets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.75','Mathematics and Science>Astronomy>Solar flares');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('523.99','Mathematics and Science>Astronomy>Eclipses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('524','Mathematics and Science>Astronomy>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('525','Mathematics and Science>Astronomy>Earth (Astronomical geography)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('526','Mathematics and Science>Astronomy>Map making');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('526.62','Mathematics and Science>Astronomy>Longitude');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('526.9','Mathematics and Science>Astronomy>Surveying');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('527','Mathematics and Science>Astronomy>Celestial navigation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('528','Mathematics and Science>Astronomy>Ephemerides');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('529','Mathematics and Science>Astronomy>Chronology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('529.1','Mathematics and Science>Astronomy>Days');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530','Mathematics and Science>Physics>Physics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530.42','Mathematics and Science>Physics>Liquids (state of matter)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530.425','Mathematics and Science>Physics>Osmosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530.43','Mathematics and Science>Physics>Gases (state of matter)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530.444','Mathematics and Science>Physics>Ionization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530.8','Mathematics and Science>Physics>Measurement');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('530.812','Mathematics and Science>Physics>Metric system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('531','Mathematics and Science>Physics>Classical Mechanics and Solid Mechanics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('531.112','Mathematics and Science>Physics>Velocity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('531.113','Mathematics and Science>Physics>Kinetics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('531.14','Mathematics and Science>Physics>Gravity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('531.6','Mathematics and Science>Physics>Momentum');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('532','Mathematics and Science>Physics>Hydraulics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('533','Mathematics and Science>Physics>Gas mechanics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('533.62','Mathematics and Science>Physics>Aerodynamics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('534','Mathematics and Science>Physics>Sound & related vibrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('535','Mathematics and Science>Physics>Light');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('535.014','Mathematics and Science>Physics>Ultraviolet radiation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('535.6','Mathematics and Science>Physics>Color');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('536','Mathematics and Science>Physics>Heat');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('536.44','Mathematics and Science>Physics>Condensation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('536.5','Mathematics and Science>Physics>Temperature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('536.7','Mathematics and Science>Physics>Thermodynamics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('537','Mathematics and Science>Physics>Electricity & electronics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('537.534','Mathematics and Science>Physics>Microwaves');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('538','Mathematics and Science>Physics>Magnetism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('538.4','Mathematics and Science>Physics>Magnets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('539','Mathematics and Science>Physics>Nuclear Physics and Matter');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('539.2','Mathematics and Science>Physics>Radiation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('539.7','Mathematics and Science>Physics>Nuclear physics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('539.721','Mathematics and Science>Physics>Quarks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('539.722','Mathematics and Science>Physics>Xrays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('539.764','Mathematics and Science>Physics>Nuclear fusion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('540','Mathematics and Science>Chemistry>Chemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('541','Mathematics and Science>Chemistry>Physical chemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('541.22','Mathematics and Science>Chemistry>Molecular structure');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('541.361','Mathematics and Science>Chemistry>Combustion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('541.39','Mathematics and Science>Chemistry>Chemical Reactions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('542','Mathematics and Science>Chemistry>Techniques, equipment & materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('543','Mathematics and Science>Chemistry>Analytical chemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('544','Mathematics and Science>Chemistry>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('545','Mathematics and Science>Chemistry>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('546','Mathematics and Science>Chemistry>Inorganic chemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('546.688','Mathematics and Science>Chemistry>Lead (chemistry)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('547','Mathematics and Science>Chemistry>Organic chemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('548','Mathematics and Science>Chemistry>Crystallography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('549','Mathematics and Science>Chemistry>Mineralogy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('550','Mathematics and Science>Earth Sciences & Geology>Earth sciences & geology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551','Mathematics and Science>Earth Sciences & Geology>Geology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.13','Mathematics and Science>Earth Sciences & Geology>Magma');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.21','Mathematics and Science>Earth Sciences & Geology>Craters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.31','Mathematics and Science>Earth Sciences & Geology>Ice');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.312','Mathematics and Science>Earth Sciences & Geology>Glaciers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.415','Mathematics and Science>Earth Sciences & Geology>Deserts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.42','Mathematics and Science>Earth Sciences & Geology>Islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.447','Mathematics and Science>Earth Sciences & Geology>Caves');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.453','Mathematics and Science>Earth Sciences & Geology>Tundras');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.457','Mathematics and Science>Earth Sciences & Geology>Coasts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.46','Mathematics and Science>Earth Sciences & Geology>Marine science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.461','Mathematics and Science>Earth Sciences & Geology>Lagoons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.463','Mathematics and Science>Earth Sciences & Geology>Tidal  waves');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.482','Mathematics and Science>Earth Sciences & Geology>Lakes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.483','Mathematics and Science>Earth Sciences & Geology>Rivers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.489','Mathematics and Science>Earth Sciences & Geology>Floods (hydrology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.5','Mathematics and Science>Earth Sciences & Geology>Atmosphere');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.552','Mathematics and Science>Earth Sciences & Geology>Hurricanes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.553','Mathematics and Science>Earth Sciences & Geology>Tornadoes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.554','Mathematics and Science>Earth Sciences & Geology>Thunderstorms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.563','Mathematics and Science>Earth Sciences & Geology>Lightning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.565','Mathematics and Science>Earth Sciences & Geology>Mirages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.576','Mathematics and Science>Earth Sciences & Geology>Clouds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.577','Mathematics and Science>Earth Sciences & Geology>Rain');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.578','Mathematics and Science>Earth Sciences & Geology>Snow');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.6','Mathematics and Science>Earth Sciences & Geology>Climate');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.691','Mathematics and Science>Earth Sciences & Geology>Tropical climate');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('551.792','Mathematics and Science>Earth Sciences & Geology>Ice age');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('552','Mathematics and Science>Earth Sciences & Geology>Petrology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553','Mathematics and Science>Earth Sciences & Geology>Minerals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.24','Mathematics and Science>Earth Sciences & Geology>Coal');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.282','Mathematics and Science>Earth Sciences & Geology>Oil (petroleum)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.285','Mathematics and Science>Earth Sciences & Geology>natural gas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.516','Mathematics and Science>Earth Sciences & Geology>Limestone');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.61','Mathematics and Science>Earth Sciences & Geology>Clay');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.632','Mathematics and Science>Earth Sciences & Geology>Salt');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.672','Mathematics and Science>Earth Sciences & Geology>Asbestos');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.68','Mathematics and Science>Earth Sciences & Geology>Chalk');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.7','Mathematics and Science>Earth Sciences & Geology>Water');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.8','Mathematics and Science>Earth Sciences & Geology>Gems');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.82','Mathematics and Science>Earth Sciences & Geology>Diamonds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.876','Mathematics and Science>Earth Sciences & Geology>Jade');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('553.93','Mathematics and Science>Earth Sciences & Geology>Nitrogen');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('554','Mathematics and Science>Earth Sciences & Geology>Earth sciences of Europe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('555','Mathematics and Science>Earth Sciences & Geology>Earth sciences of Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('556','Mathematics and Science>Earth Sciences & Geology>Earth sciences of Africa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('557','Mathematics and Science>Earth Sciences & Geology>Earth sciences of North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('558','Mathematics and Science>Earth Sciences & Geology>Earth sciences of South America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('559','Mathematics and Science>Earth Sciences & Geology>Earth sciences of other areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('560','Mathematics and Science>Fossils & Prehistoric Life>Fossils & prehistoric life');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('561','Mathematics and Science>Fossils & Prehistoric Life>Extinct plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('562','Mathematics and Science>Fossils & Prehistoric Life>Fossil invertebrates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('563','Mathematics and Science>Fossils & Prehistoric Life>Fossil marine & seashore invertebrates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('564','Mathematics and Science>Fossils & Prehistoric Life>Fossil mollusks & molluscoids');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('565','Mathematics and Science>Fossils & Prehistoric Life>Fossil arthropods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('566','Mathematics and Science>Fossils & Prehistoric Life>Fossil chordates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('567','Mathematics and Science>Fossils & Prehistoric Life>Fossil cold-blooded vertebrates and fossil fishes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('567.9','Mathematics and Science>Fossils & Prehistoric Life>Dinosaurs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('568','Mathematics and Science>Fossils & Prehistoric Life>Fossil birds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('569','Mathematics and Science>Fossils & Prehistoric Life>Fossil mammals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('570','Mathematics and Science>Biology>Life sciences and biology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('570.282','Mathematics and Science>Biology>Microscopy (biology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571','Mathematics and Science>Biology>Physiology & related subjects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.3','Mathematics and Science>Biology>Anatomy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.6','Mathematics and Science>Biology>Cells (biology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.74','Mathematics and Science>Biology>Hormones');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.8','Mathematics and Science>Biology>Life cycle');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.847','Mathematics and Science>Biology>Spores');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.864','Mathematics and Science>Biology>Zygote');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.878','Mathematics and Science>Biology>Aging');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.89','Mathematics and Science>Biology>Cloning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.9','Mathematics and Science>Biology>Diseases--Pathology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.948','Mathematics and Science>Biology>Hereditary diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.978','Mathematics and Science>Biology>Cancer');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.98','Mathematics and Science>Biology>Infectious diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('571.992','Mathematics and Science>Biology>Viral diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('572','Mathematics and Science>Biology>Biochemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('572.4','Mathematics and Science>Biology>Metabolism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('572.56','Mathematics and Science>Biology>Carbohydrates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('572.57','Mathematics and Science>Biology>Fats');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('572.7','Mathematics and Science>Biology>Enzymes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573','Mathematics and Science>Biology>Specific physiological systems in animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.1','Mathematics and Science>Biology>Circulatory system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.139','Mathematics and Science>Biology>Cardiovascular Diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.15','Mathematics and Science>Biology>Blood');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.155','Mathematics and Science>Biology>Bone Marrow');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.17','Mathematics and Science>Biology>Heart');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.187','Mathematics and Science>Biology>Capillaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.3','Mathematics and Science>Biology>Digestion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.49','Mathematics and Science>Biology>Bladder (Urinary)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.67','Mathematics and Science>Biology>Birth');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.7','Mathematics and Science>Biology>Movement');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.76','Mathematics and Science>Biology>Skeleton');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.79','Mathematics and Science>Biology>Locomotion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.798','Mathematics and Science>Biology>Flight (animals)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.8','Mathematics and Science>Biology>Nervous system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.853','Mathematics and Science>Biology>Neurons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.86','Mathematics and Science>Biology>Brain');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.88','Mathematics and Science>Biology>Eyes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.883','Mathematics and Science>Biology>Eye diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('573.89','Mathematics and Science>Biology>Hearing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('574','Mathematics and Science>Biology>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('575','Mathematics and Science>Biology>Specific parts of & systems in plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('576','Mathematics and Science>Biology>Genetics & evolution');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('576.5','Mathematics and Science>Biology>Heredity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('576.544','Mathematics and Science>Biology>Inbreeding');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('576.8','Mathematics and Science>Biology>Evolution');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('576.839','Mathematics and Science>Biology>Extraterrestrial life');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('577','Mathematics and Science>Biology>Ecology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('578','Mathematics and Science>Biology>Natural history of organisms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('578.746','Mathematics and Science>Biology>Meadows (biology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('579','Mathematics and Science>Biology>Microbiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('579.2','Mathematics and Science>Biology>Viruses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('579.3','Mathematics and Science>Biology>Bacteria');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('579.53','Mathematics and Science>Biology>Mildew');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('579.6','Mathematics and Science>Biology>Mushrooms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('579.8','Mathematics and Science>Biology>Algae');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('580','Mathematics and Science>Botony>Plants (Botany)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('581','Mathematics and Science>Botony>Specific topics in natural history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('581.464','Mathematics and Science>Botony>Fruit');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('581.467','Mathematics and Science>Botony>Seeds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('581.6','Mathematics and Science>Botony>Miscellaneous nontaxonomic kinds of plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('581.76','Mathematics and Science>Botony>Freshwater plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('582','Mathematics and Science>Botony>Plants noted for characteristics & flowers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('582.13','Mathematics and Science>Botony>Flowers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('582.16','Mathematics and Science>Botony>Trees');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('582.17','Mathematics and Science>Botony>Shrubs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('582.18','Mathematics and Science>Botony>Vines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('583','Mathematics and Science>Botony>Dicotyledons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('583.56','Mathematics and Science>Botony>Cactuses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('583.74','Mathematics and Science>Botony>Kudzu');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('584','Mathematics and Science>Botony>Monocotyledons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('584.4','Mathematics and Science>Botony>Orchids');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('584.9','Mathematics and Science>Botony>Grasses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('585','Mathematics and Science>Botony>Gymnosperms and conifers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('586','Mathematics and Science>Botony>Seedless plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('587','Mathematics and Science>Botony>Vascular seedless plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('588','Mathematics and Science>Botony>Bryophytes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('589','Mathematics and Science>Botony>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('590','Mathematics and Science>Zoology>Animals (Zoology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('590.73','Mathematics and Science>Zoology>Zoos');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591','Mathematics and Science>Zoology>Specific topics in natural history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.177','Mathematics and Science>Zoology>Marine botany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.479','Mathematics and Science>Zoology>Tracks (animals)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.5','Mathematics and Science>Zoology>Animal Behavior');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.565','Mathematics and Science>Zoology>Hibernation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.65','Mathematics and Science>Zoology>Dangerous animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.76','Mathematics and Science>Zoology>Freshwater animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('591.77','Mathematics and Science>Zoology>Marine animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('592','Mathematics and Science>Zoology>Invertebrates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('593','Mathematics and Science>Zoology>Marine & seashore invertebrates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('594','Mathematics and Science>Zoology>Sea shells');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595','Mathematics and Science>Zoology>Arthropods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595.3','Mathematics and Science>Zoology>Crustaceans');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595.44','Mathematics and Science>Zoology>Spiders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595.77','Mathematics and Science>Zoology>Flies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595.781','Mathematics and Science>Zoology>Caterpillars');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595.789','Mathematics and Science>Zoology>Butterflies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('595.79','Mathematics and Science>Zoology>Wasps');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('596','Mathematics and Science>Zoology>Chordates');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597','Mathematics and Science>Zoology>Fishes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.43','Mathematics and Science>Zoology>Eels');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.49','Mathematics and Science>Zoology>Cat fishes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.7','Mathematics and Science>Zoology>Insects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.8','Mathematics and Science>Zoology>Amphibians');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.9','Mathematics and Science>Zoology>Reptiles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.92','Mathematics and Science>Zoology>Turtles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.954','Mathematics and Science>Zoology>Iguanas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('597.96','Mathematics and Science>Zoology>Snakes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('598','Mathematics and Science>Zoology>Birds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('598.8','Mathematics and Science>Zoology>Songbirds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('598.883','Mathematics and Science>Zoology>Sparrows');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599','Mathematics and Science>Zoology>Mammals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.222','Mathematics and Science>Zoology>Kangaroos');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.36','Mathematics and Science>Zoology>Squirrels');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.4','Mathematics and Science>Zoology>Bats');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.5','Mathematics and Science>Zoology>Whales');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.642','Mathematics and Science>Zoology>Yak');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.65','Mathematics and Science>Zoology>Deer');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.665','Mathematics and Science>Zoology>Zebra');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.67','Mathematics and Science>Zoology>Elephants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.78','Mathematics and Science>Zoology>Bears');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('599.9','Mathematics and Science>Zoology>Physical anthropology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('6','Technology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('60','Technology>General Technology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('600','Technology>General Technology>Technology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('601','Technology>General Technology>Philosophy & theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('602','Technology>General Technology>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('603','Technology>General Technology>Dictionaries & encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('604','Technology>General Technology>Special topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('604.2','Technology>General Technology>Technical drawing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('605','Technology>General Technology>Serial publications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('606','Technology>General Technology>Organizations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('607','Technology>General Technology>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('608','Technology>General Technology>Inventions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('609','Technology>General Technology>Historical, geographic & persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610','Technology>Medicine>Medicine & health');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610.619','Technology>Medicine>Medical');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610.73','Technology>Medicine>Nurses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610.7309','Technology>Medicine>Nursing--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610.736','Technology>Medicine>Longterm care nursing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610.9','Technology>Medicine>Medicine--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('610.92','Technology>Medicine>Medical personnel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611','Technology>Medicine>Human anatomy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.018','Technology>Medicine>Gene mapping (human)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.0185','Technology>Medicine>Blood & lymph elements');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.1','Technology>Medicine>Cardiovascular organs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.12','Technology>Medicine>Heart (human anatomy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.2','Technology>Medicine>Respiratory organs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.3','Technology>Medicine>Digestive tract organs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.4','Technology>Medicine>Lymphatic & glandular organs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.42','Technology>Medicine>Lymphatic system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.46','Technology>Medicine>Lymphatic glands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.6','Technology>Medicine>Genital system (humananatomy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.65','Technology>Medicine>Ovaries & fallopian tubes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.7','Technology>Medicine>Musculoskeletal system, integument');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.73','Technology>Medicine>Muscles (human anatomy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.77','Technology>Medicine>Integument');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.8','Technology>Medicine>Nervous system (humananatomy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('611.92','Technology>Medicine>Face (anatomy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612','Technology>Medicine>Human physiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.014','Technology>Medicine>Radiation (humans)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.015','Technology>Medicine>Biochemistry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.1','Technology>Medicine>Cardiovascular system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.11','Technology>Medicine>Blood');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.2','Technology>Medicine>Respiration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.3','Technology>Medicine>Digestion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.39','Technology>Medicine>Metabolism (human physiology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.4','Technology>Medicine>Secretion, excretion, related functions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.405','Technology>Medicine>Hormones (human physiology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.42','Technology>Medicine>Lymph & lymphatics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.46','Technology>Medicine>Excretion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.62','Technology>Medicine>Female');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.63','Technology>Medicine>Pregnancy & childbirth');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.64','Technology>Medicine>Physiology of embryo & fetus');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.647','Technology>Medicine>Fetus (human physiology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.663','Technology>Medicine>Maturity (human physiology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.664','Technology>Medicine>Mammary glands & lactation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.7','Technology>Medicine>Musculoskeletal system, integument');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.79','Technology>Medicine>Integument and Skin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.8','Technology>Medicine>Nervous functions--Sensory functions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.85','Technology>Medicine>Hearing (human physiology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('612.98','Technology>Medicine>Feet');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613','Technology>Medicine>Health');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.042','Technology>Medicine>Females (health)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.2','Technology>Medicine>Diet and Nutrition');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.25','Technology>Medicine>Fasting (health)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.263','Technology>Medicine>Fiber (diet)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.284','Technology>Medicine>Fats (applied nutrition)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.6','Technology>Medicine>Special topics of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.62','Technology>Medicine>Industrial &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.69','Technology>Medicine>Survival skills');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('613.71','Technology>Medicine>Exercise');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614','Technology>Medicine>Incidence & prevention of disease');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614.09','Technology>Medicine>Incidence & prevention of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614.1','Technology>Medicine>Forensic medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614.42','Technology>Medicine>Incidence');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614.47','Technology>Medicine>Vaccination');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614.5','Technology>Medicine>Incidence of & public');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('614.599','Technology>Medicine>HIV infections (incidence)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615','Technology>Medicine>Drugs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.1','Technology>Medicine>Medications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.109','Technology>Medicine>Drugs (Materia medica)--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.2','Technology>Medicine>Inorganic drugs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.3','Technology>Medicine>Organic drugs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.321','Technology>Medicine>Herbs (Medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.4','Technology>Medicine>Practical pharmacy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.5','Technology>Medicine>Therapy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.532','Technology>Medicine>Homeopathy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.534','Technology>Medicine>Chiropractic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.6','Technology>Medicine>Methods of administering medication');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.7','Technology>Medicine>Pharmacodynamics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.8','Technology>Medicine>Specific therapies & kinds of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.842','Technology>Medicine>Radiation therapy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.852','Technology>Medicine>Faith healing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.882','Technology>Medicine>Massage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.9','Technology>Medicine>Toxicology (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.94','Technology>Medicine>Animal poisons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('615.952','Technology>Medicine>Tobacco (human toxicology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616','Technology>Medicine>Diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.01','Technology>Medicine>Medical microbiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.025','Technology>Medicine>Medical emergencies (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.0252','Technology>Medicine>First aid');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.027','Technology>Medicine>Laboratory animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.043','Technology>Medicine>Birth Defects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.044','Technology>Medicine>Chronic diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.04409','Technology>Medicine>Chronic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.047','Technology>Medicine>Pain');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.07','Technology>Medicine>Pathology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.0709','Technology>Medicine>Pathology--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.075','Technology>Medicine>Nuclear medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.0754','Technology>Medicine>Physical diagnosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.075409','Technology>Medicine>Physical');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.0757','Technology>Medicine>Radiological diagnosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.075709','Technology>Medicine>Radiological');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.07575','Technology>Medicine>Radioisotope scanning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.079','Technology>Medicine>Immunity');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.1','Technology>Medicine>Diseases of cardiovascular system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.1009','Technology>Medicine>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.12','Technology>Medicine>Heart (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.123','Technology>Medicine>Cardiac Arrest');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.13','Technology>Medicine>Arterial Diseases (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.15','Technology>Medicine>Diseases of blood');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.15009','Technology>Medicine>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.152','Technology>Medicine>Anemia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.2','Technology>Medicine>Diseases of respiratory system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.2009','Technology>Medicine>Diseases of respiratory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.21','Technology>Medicine>Diseases of nose, larynx, accessory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.22','Technology>Medicine>Diseases of larynx, glottis, vocal');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.234','Technology>Medicine>Bronchitis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.24','Technology>Medicine>Lung diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.3','Technology>Medicine>Diseases of digestive system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.3009','Technology>Medicine>Diseases of digestive');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.39','Technology>Medicine>Nutritional & metabolic diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.398','Technology>Medicine>Obesity (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.4','Technology>Medicine>Endocrine system--human diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.4009','Technology>Medicine>Endocrine system--human');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.42','Technology>Medicine>Diseases of lymphatic system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.42009','Technology>Medicine>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.462','Technology>Medicine>Diabetes (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.5','Technology>Medicine>Diseases of integument, hair, nails');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.5009','Technology>Medicine>Diseases of integument, hair,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.6','Technology>Medicine>Diseases of the urogenital system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.6009','Technology>Medicine>Diseases of the');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.61','Technology>Medicine>Kidney disease');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.7','Technology>Medicine>Diseases of musculoskeletal system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.7009','Technology>Medicine>Diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.722','Technology>Medicine>Arthritis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.77','Technology>Medicine>Diseases of connective tissues');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.8','Technology>Medicine>Diseases of nervous system & mental');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.809','Technology>Medicine>Diseases of nervous system &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.83','Technology>Medicine>Memory disorders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.85','Technology>Medicine>Miscellaneous diseases of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.852','Technology>Medicine>Neuroses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.855','Technology>Medicine>Language disorders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.858','Technology>Medicine>False memory syndrome');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.8588','Technology>Medicine>Mental retardation &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.86','Technology>Medicine>Drug Abuse (Medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.863','Technology>Medicine>Narcotics abuse (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.865','Technology>Medicine>Smoking (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.89','Technology>Medicine>Mental disorders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.89009','Technology>Medicine>Mental disorders--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.89075','Technology>Medicine>Mental');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.891','Technology>Medicine>Marriage counseling (psychotherapy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.9','Technology>Medicine>Other diseases;\');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.909','Technology>Medicine>Other diseases;\');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.92','Technology>Medicine>Bacterial & viral');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.925','Technology>Medicine>Viral diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.951','Technology>Medicine>Sexually');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.96','Technology>Medicine>Parasitic diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.975','Technology>Medicine>Drug allergies (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.979','Technology>Medicine>AIDS (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.9792','Technology>Medicine>Acquired immune deficiency');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.980213','Technology>Medicine>Aviation medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.980214','Technology>Medicine>Space medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.9803','Technology>Medicine>Industrial &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.988','Technology>Medicine>Jungle diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.9883','Technology>Medicine>Tropical diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.989','Technology>Medicine>Diseases due to');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.992','Technology>Medicine>Tumors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.993','Technology>Medicine>Benign tumors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.994','Technology>Medicine>Breast Cancer (Medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.99449','Technology>Medicine>Breast cancer--medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('616.995','Technology>Medicine>Tuberculosis');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617','Technology>Medicine>Surgery & related medical specialties');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.03','Technology>Medicine>Rehabilitation (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.05','Technology>Medicine>Surgery utilizing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.058','Technology>Medicine>Laser surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.09','Technology>Medicine>Surgery--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.1','Technology>Medicine>Injuries & wounds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.10262','Technology>Medicine>First aid');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.1027','Technology>Medicine>Athletic injuries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.41','Technology>Medicine>Cardiovascular system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.43','Technology>Medicine>Digestive system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.44','Technology>Medicine>Endocrine system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.46','Technology>Medicine>Urogenital system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.47','Technology>Medicine>Musculoskeletal system--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.477','Technology>Medicine>Skin--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.48','Technology>Medicine>Nervous system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.51','Technology>Medicine>Head');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.5109','Technology>Medicine>Head--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.522059','Technology>Medicine>Oral region--surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.52205909','Technology>Medicine>Oral');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.54','Technology>Medicine>Thorax (Chest) & respiratory system');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.6','Technology>Medicine>Dental care');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.601','Technology>Medicine>Oral hygiene');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.609','Technology>Medicine>Dentistry--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.7','Technology>Medicine>Ophthalmology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.709','Technology>Medicine>Ophthalmology--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.742','Technology>Medicine>Cataracts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.8','Technology>Medicine>Hearing impairment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.91','Technology>Medicine>Operative surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.95','Technology>Medicine>Plastic surgery and Organ transplants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.954','Technology>Medicine>Organ transplants (surgery)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.96','Technology>Medicine>Anesthesiology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.97','Technology>Medicine>Geriatric surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.98','Technology>Medicine>Pediatric surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('617.99','Technology>Medicine>Military surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618','Technology>Medicine>Pregnancy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.1','Technology>Medicine>Gynecology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.14','Technology>Medicine>Diseases of uterus');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.178','Technology>Medicine>Infertility');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.19','Technology>Medicine>Diseases of breast');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.2','Technology>Medicine>Midwives (medicine)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.2009','Technology>Medicine>Obstetrics--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.24','Technology>Medicine>Childbirth');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.3','Technology>Medicine>Diseases & complications of pregnancy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.4','Technology>Medicine>Labor (obstetrics)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.5','Technology>Medicine>Complicated labor (Dystocia)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.6','Technology>Medicine>Normal puerperium');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.7','Technology>Medicine>Puerperal diseases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.8','Technology>Medicine>Obstetrical surgery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.92','Technology>Medicine>Pediatrics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.920009','Technology>Medicine>Pediatrics--history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('618.97','Technology>Medicine>Geriatric medicine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('619','Technology>Medicine>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('620','Technology>Engineering>Engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('620.004','Technology>Engineering>Repairs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('620.106','Technology>Engineering>Hydraulics (engineering)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('620.112','Technology>Engineering>Corrosion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('620.3','Technology>Engineering>Vibrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('620.8','Technology>Engineering>Human factors & safety engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621','Technology>Engineering>Applied physics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.1','Technology>Engineering>Steam engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.2','Technology>Engineering>Hydraulic-power');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.3','Technology>Engineering>Electronics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.32','Technology>Engineering>Lighting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.323','Technology>Engineering>Kerosene lamps');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.366','Technology>Engineering>Lasers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.367','Technology>Engineering>Technological photography & photo-optics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.384','Technology>Engineering>Ham radio');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.388','Technology>Engineering>HDTV (Highdefinition television)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.398','Technology>Engineering>Opticalfiber cable (engineering)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.4','Technology>Engineering>Engines, power');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.435','Technology>Engineering>Rocket engines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.436','Technology>Engineering>Diesel engines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.483','Technology>Engineering>Nuclear power plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.5','Technology>Engineering>Pneumatic, vacuum,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.56','Technology>Engineering>Refrigeration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.6','Technology>Engineering>Blowers, fans, pumps');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.8','Technology>Engineering>Machinery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.9','Technology>Engineering>Tools');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('621.934','Technology>Engineering>Chain saws');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('622','Technology>Engineering>Mines and mining');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('622.7','Technology>Engineering>Ore processing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623','Technology>Engineering>Military & nautical engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.4','Technology>Engineering>Ordnance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.446','Technology>Engineering>Laser  weapons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.812','Technology>Engineering>Inboardoutboard motorboats (design)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.82','Technology>Engineering>Nautical craft');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.862','Technology>Engineering>Sails');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.88','Technology>Engineering>Seamanship');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('623.89','Technology>Engineering>Navigation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('624','Technology>Engineering>Construction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('624.1','Technology>Engineering>Structural');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('624.152','Technology>Engineering>Excavation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('625','Technology>Engineering>Engineering of railroads & roads');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('625.143','Technology>Engineering>Ties (railroad)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('625.26','Technology>Engineering>Locomotives');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('626','Technology>Engineering>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('627','Technology>Engineering>Hydraulic engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('627.72','Technology>Engineering>Diving');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('627.8','Technology>Engineering>Dams');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('628','Technology>Engineering>Sanitary & municipal engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629','Technology>Engineering>Other branches of engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.04','Technology>Engineering>Transportation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.045','Technology>Engineering>Navigators');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.1','Technology>Engineering>Aerospace');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.13','Technology>Engineering>Flight');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.133','Technology>Engineering>Airplanes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.2','Technology>Engineering>Motor land');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.221','Technology>Engineering>Model cars');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.225','Technology>Engineering>Farm  tractors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.28','Technology>Engineering>Car Repairs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.287','Technology>Engineering>Motorcycles (repair)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.3','Technology>Engineering>Air-cushion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.4','Technology>Engineering>Space exploration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.8','Technology>Engineering>Automatic control');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('629.82','Technology>Engineering>Vending machines');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('630','Technology>Agriculture>Agriculture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('630.92','Technology>Agriculture>Farmers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631','Technology>Agriculture>Techniques, equipment & materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.2','Technology>Agriculture>Farm buildings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.27','Technology>Agriculture>Fences');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.5','Technology>Agriculture>Cultivation & harvesting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.52','Technology>Agriculture>Nurseries (plant culture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.531','Technology>Agriculture>Seeds (sowing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.6','Technology>Agriculture>Clearing, drainage, revegetation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.7','Technology>Agriculture>Water conservation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.8','Technology>Agriculture>Fertilizers, soil conditioners,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('631.875','Technology>Agriculture>Composting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('632','Technology>Agriculture>Plant injuries, diseases & pests');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('632.17','Technology>Agriculture>Floods (crop damage)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('632.5','Technology>Agriculture>Weeds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('632.6','Technology>Agriculture>Farm pests');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('633','Technology>Agriculture>Field crops');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('633.71','Technology>Agriculture>Tobacco (agriculture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('634','Technology>Agriculture>Orchards, fruits & forestry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('634.7','Technology>Agriculture>Berries & herbaceous tropical');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('634.8','Technology>Agriculture>Grapes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('634.9','Technology>Agriculture>Forestry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635','Technology>Agriculture>Gardening');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635.7','Technology>Agriculture>Herbs (gardening)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635.933','Technology>Agriculture>African  Violets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635.962','Technology>Agriculture>Flower beds');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635.965','Technology>Agriculture>House plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635.976','Technology>Agriculture>Hedges');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('635.982','Technology>Agriculture>Terrariums');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636','Technology>Agriculture>Domestic Animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.084','Technology>Agriculture>Feeding animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.085','Technology>Agriculture>Nitrogen (animal husbandry)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.088','Technology>Agriculture>Obedience  training(pets)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.089','Technology>Agriculture>Veterinarians');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.089607','Technology>Agriculture>Veterinary pathology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.1','Technology>Agriculture>Horses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.3','Technology>Agriculture>Sheep');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.5','Technology>Agriculture>Chickens');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.686','Technology>Agriculture>Canaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.7','Technology>Agriculture>Dogs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.737','Technology>Agriculture>Sheep dogs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.753','Technology>Agriculture>Bloodhound');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.755','Technology>Agriculture>Terriers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('636.8','Technology>Agriculture>Cats');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('637','Technology>Agriculture>Processing dairy & related products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('638','Technology>Agriculture>Insect culture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639','Technology>Agriculture>Hunting, fishing & conservation');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.1','Technology>Agriculture>Trapping');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.2','Technology>Agriculture>Commercial fishing,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.3','Technology>Agriculture>Fish farming');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.374','Technology>Agriculture>Goldfish');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.4','Technology>Agriculture>Mollusk fisheries & culture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.5','Technology>Agriculture>Crustacean fisheries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.6','Technology>Agriculture>Crustacean culture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.7','Technology>Agriculture>Harvest & culture of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.8','Technology>Agriculture>Aquaculture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('639.9','Technology>Agriculture>Conservation of biological resources');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('640','Technology>Home Economics>Home & family management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641','Technology>Home Economics>Food & drink');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.222','Technology>Home Economics>Champagne');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.255','Technology>Home Economics>Liqueurs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.3','Technology>Home Economics>Baby Food');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.302','Technology>Home Economics>Lowcalorie food');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.303','Technology>Home Economics>Edible plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.308','Technology>Home Economics>Food additives');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.331','Technology>Home Economics>Wheat');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.337','Technology>Home Economics>Chocolate (food)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.338','Technology>Home Economics>Flavorings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.344','Technology>Home Economics>Kiwi');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.345','Technology>Home Economics>Nuts (food)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.352','Technology>Home Economics>Yams');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.356','Technology>Home Economics>Zucchini');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.357','Technology>Home Economics>Herbs (food)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.358','Technology>Home Economics>Truffles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.37','Technology>Home Economics>Dairy products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.391','Technology>Home Economics>Venison');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.44','Technology>Home Economics>Dried foods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.48','Technology>Home Economics>Food storage');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.5','Technology>Home Economics>Cookbooks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.514','Technology>Home Economics>Gourmet cooking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.555','Technology>Home Economics>Fast foods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.563','Technology>Home Economics>Fatfree cooking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.568','Technology>Home Economics>Thanksgiving (cooking)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.578','Technology>Home Economics>Camp Cooking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.588','Technology>Home Economics>Microwave cooking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.59','Technology>Home Economics>International cooking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.656','Technology>Home Economics>Tofu (cooking)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.694','Technology>Home Economics>Squashes (cooking)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.76','Technology>Home Economics>Barbecuing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.812','Technology>Home Economics>Finger foods (appetizers)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.813','Technology>Home Economics>Soups');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.815','Technology>Home Economics>Waffles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.82','Technology>Home Economics>Onedish cooking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.821','Technology>Home Economics>Casseroles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.84','Technology>Home Economics>Sandwiches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.86','Technology>Home Economics>Desserts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.862','Technology>Home Economics>Ice cream');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.864','Technology>Home Economics>Jellies (home preparation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.865','Technology>Home Economics>Cake Decorating');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('641.874','Technology>Home Economics>Cocktails');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('642','Technology>Home Economics>Dinners');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('642.7','Technology>Home Economics>Dishes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643','Technology>Home Economics>Housing & household equipment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.1','Technology>Home Economics>Dwellings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.12','Technology>Home Economics>Home inspection');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.2','Technology>Home Economics>Solar houses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.25','Technology>Home Economics>Vacation homes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.29','Technology>Home Economics>Mobile homes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.5','Technology>Home Economics>Closets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.53','Technology>Home Economics>Blankets');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('643.7','Technology>Home Economics>Home remodeling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('644','Technology>Home Economics>Household utilities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('645','Technology>Home Economics>Household furnishings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('645.1','Technology>Home Economics>Linoleum');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('645.12','Technology>Home Economics>Rugs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('645.4','Technology>Home Economics>Chairs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('645.5','Technology>Home Economics>Furniture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('645.8','Technology>Home Economics>Outdoor furniture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646','Technology>Home Economics>Sewing, clothing & personal living');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.1','Technology>Home Economics>Sewing materials & equipment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.19','Technology>Home Economics>Notions (home sewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.2','Technology>Home Economics>Sewing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.204','Technology>Home Economics>Hand sewing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.21','Technology>Home Economics>Quilting (home sewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.3','Technology>Home Economics>Clothing & accessories');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.4','Technology>Home Economics>Tailoring');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.402','Technology>Home Economics>Men''s clothing (homesewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.404','Technology>Home Economics>Dressmaking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.42','Technology>Home Economics>Lingerie (home sewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.47','Technology>Home Economics>Maternity garments (homesewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.478','Technology>Home Economics>Costumes (home sewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.48','Technology>Home Economics>Handbags (home sewing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.6','Technology>Home Economics>Clothing care');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.7','Technology>Home Economics>Life skills');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.72','Technology>Home Economics>Cosmetics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.724','Technology>Home Economics>Haircutting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.75','Technology>Home Economics>Bodybuilding');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.76','Technology>Home Economics>Charm (life skills)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('646.77','Technology>Home Economics>Mate selection (lifeskills)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('647','Technology>Home Economics>Management of public households');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('647.95','Technology>Home Economics>Lunchrooms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('648','Technology>Home Economics>Housework (Cleaning, Moving, Organizing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('648.5','Technology>Home Economics>Cleaning house');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649','Technology>Home Economics>Parenting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.1','Technology>Home Economics>Child care');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.122','Technology>Home Economics>Infants (home care)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.154','Technology>Home Economics>Hyperactive children');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.58','Technology>Home Economics>Listening (child care)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.6','Technology>Home Economics>Habits (child training)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.64','Technology>Home Economics>Obedience (home childcare)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('649.68','Technology>Home Economics>Home schooling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('650','Technology>Business>Management & public relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('650.11','Technology>Business>Time management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('650.142','Technology>Business>Job applications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('651','Technology>Business>Office services');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('651.29','Technology>Business>Business Forms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('651.309','Technology>Business>Office  workers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('651.53','Technology>Business>Filing (records management)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('651.752','Technology>Business>Form letters (officeuse)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('652','Technology>Business>Processes of written communication');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('652.1','Technology>Business>Handwriting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('652.3','Technology>Business>Typing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('653','Technology>Business>Shorthand');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('654','Technology>Business>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('654.4','Technology>Business>Upholstery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('655','Technology>Business>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('656','Technology>Business>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('657','Technology>Business>Accounting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658','Technology>Business>Business Management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.114','Technology>Business>Incorporation (management)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.154','Technology>Business>Budgeting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.155','Technology>Business>Loss (financial management)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.3','Technology>Business>Employee management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.306','Technology>Business>Job description');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.401','Technology>Business>Quality control (management)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.408','Technology>Business>Safety management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.456','Technology>Business>Meetings (management use)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.5','Technology>Business>Factory management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.8','Technology>Business>Marketing (management)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('658.87','Technology>Business>Bazaars (Management)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('659','Technology>Business>Advertising & public relations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('659.1','Technology>Business>Advertising');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('660','Technology>Chemical Technology>Chemical engineering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('661','Technology>Chemical Technology>Industrial chemicals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('662','Technology>Chemical Technology>Explosives, fuels & related products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('662.2','Technology>Chemical Technology>Explosives');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('662.6','Technology>Chemical Technology>Fuels');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('663','Technology>Chemical Technology>Beverage technology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('664','Technology>Chemical Technology>Food technology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('664.028','Technology>Chemical Technology>Dehydrated foods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('664.7','Technology>Chemical Technology>Grains, other seeds, their derived products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('664.9','Technology>Chemical Technology>Meats & allied foods');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('665','Technology>Chemical Technology>Industrial oils, fats, waxes & gases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('665.538','Technology>Chemical Technology>Kerosene');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('666','Technology>Chemical Technology>Ceramic & allied technologies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('666.1','Technology>Chemical Technology>Glass');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('666.436','Technology>Chemical Technology>Kilns');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('666.893','Technology>Chemical Technology>Concrete');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('666.94','Technology>Chemical Technology>Cement');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('667','Technology>Chemical Technology>Cleaning, color & coating technologies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('667.13','Technology>Chemical Technology>Laundering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('667.2','Technology>Chemical Technology>Dyes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('667.63','Technology>Chemical Technology>Latex paints');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('668','Technology>Chemical Technology>Technology of other organic products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('668.12','Technology>Chemical Technology>Soaps');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('668.651','Technology>Chemical Technology>Insecticides');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('668.654','Technology>Chemical Technology>Weed killers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('669','Technology>Chemical Technology>Metals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('669.23','Technology>Chemical Technology>Silver');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('669.52','Technology>Chemical Technology>Zinc');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('669.725','Technology>Chemical Technology>Calcium');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('670','Technology>Manufacturing>Manufacturing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('671','Technology>Manufacturing>Metalworking & primary metal products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('672','Technology>Manufacturing>Iron, steel & other iron alloys');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('673','Technology>Manufacturing>Nonferrous metals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('674','Technology>Manufacturing>Lumber processing, wood products & cork');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('675','Technology>Manufacturing>Leather & fur processing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('676','Technology>Manufacturing>Pulp & paper technology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('676.284','Technology>Manufacturing>Tissue paper');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('676.287','Technology>Manufacturing>Wrapping paper');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('677','Technology>Manufacturing>Textiles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('677.028','Technology>Manufacturing>Crocheting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('677.71','Technology>Manufacturing>Ropes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('678','Technology>Manufacturing>Elastomers & elastomer products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('679','Technology>Manufacturing>Other products of specific materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('680','Technology>Handicraft and Occupations>Manufacture for specific uses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('681','Technology>Handicraft and Occupations>Precision instruments & other devices');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('681.1','Technology>Handicraft and Occupations>Instruments for measuring time, counting &');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('681.113','Technology>Handicraft and Occupations>Clocks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('681.114','Technology>Handicraft and Occupations>Watches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('681.2','Technology>Handicraft and Occupations>Testing,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('681.753','Technology>Handicraft and Occupations>Gyroscopes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('682','Technology>Handicraft and Occupations>Small forge work (Blacksmithing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('683','Technology>Handicraft and Occupations>Hardware & household appliances');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('683.3','Technology>Handicraft and Occupations>Locksmithing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('683.4','Technology>Handicraft and Occupations>Guns (small arms)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('683.422','Technology>Handicraft and Occupations>Rifles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('684','Technology>Handicraft and Occupations>Woodworking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('684.1','Technology>Handicraft and Occupations>Furniture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('684.104','Technology>Handicraft and Occupations>Cabinetmaking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('685','Technology>Handicraft and Occupations>Leather, fur goods & related products');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('686','Technology>Handicraft and Occupations>Printing & related activities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('686.225','Technology>Handicraft and Occupations>Publishing (Desktop)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('686.233','Technology>Handicraft and Occupations>Laser printing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('686.442','Technology>Handicraft and Occupations>Xerography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('687','Technology>Handicraft and Occupations>Clothing & accessories');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('688','Technology>Handicraft and Occupations>Other final products & packaging');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('688.1','Technology>Handicraft and Occupations>Miniatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('688.722','Technology>Handicraft and Occupations>Dolls');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('688.8','Technology>Handicraft and Occupations>Bags');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('689','Technology>Handicraft and Occupations>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('690','Technology>Building>Building & construction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('690.092','Technology>Building>Builders');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('690.24','Technology>Building>Remodeling of buildings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('690.8','Technology>Building>Home Construction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('691','Technology>Building>Building materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('691.8','Technology>Building>Metals (building materials)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('692','Technology>Building>Auxiliary construction practices');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('693','Technology>Building>Specific materials & purposes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('693.34','Technology>Building>Tropical Fish');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('694','Technology>Building>Wood construction & carpentry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('695','Technology>Building>Roof covering');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('696','Technology>Building>Utilities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('696.1','Technology>Building>Plumbing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('696.184','Technology>Building>Garbage disposal unit(installation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('697','Technology>Building>Heating, ventilating & air-conditioning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('697.03','Technology>Building>Central heating');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('697.1','Technology>Building>Fireplaces (construction)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('697.7','Technology>Building>Tobacco (manufacturing technology)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('698','Technology>Building>Detail finishing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('698.9','Technology>Building>Installing Tile');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('699','Technology>Building>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('7','Arts and Leisure');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('70','Arts and Leisure>General Art');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700','Arts and Leisure>General Art>Arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.1','Arts and Leisure>General Art>Philosophy of the arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.4','Arts and Leisure>General Art>Special topics of the arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.453','Arts and Leisure>General Art>Beauty (Personal)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.47','Arts and Leisure>General Art>Monsters (art)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.5','Arts and Leisure>General Art>Serial publications of the arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.9','Arts and Leisure>General Art>Historical, geographic, persons');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('700.92','Arts and Leisure>General Art>Artists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('701','Arts and Leisure>General Art>Philosophy of fine & decorative arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('702','Arts and Leisure>General Art>Miscellany of fine & decorative arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('703','Arts and Leisure>General Art>Dictionaries of fine & decorative arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('704','Arts and Leisure>General Art>Special topics in fine & decorative arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('704.948','Arts and Leisure>General Art>Icons (art)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('705','Arts and Leisure>General Art>Serial publications of fine & decorative arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('706','Arts and Leisure>General Art>Organizations & management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('707','Arts and Leisure>General Art>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('708','Arts and Leisure>General Art>Galleries, museums & private collections');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('709','Arts and Leisure>General Art>Art (History)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('710','Arts and Leisure>Landscape Gardening>Landscaping & area planning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('711','Arts and Leisure>Landscape Gardening>Area planning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('712','Arts and Leisure>Landscape Gardening>Landscaping');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('712.6','Arts and Leisure>Landscape Gardening>Yards (landscape architecture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('713','Arts and Leisure>Landscape Gardening>Landscape architecture of trafficways');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('714','Arts and Leisure>Landscape Gardening>Water features');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('715','Arts and Leisure>Landscape Gardening>Woody plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('715.1','Arts and Leisure>Landscape Gardening>Topiary  work');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('716','Arts and Leisure>Landscape Gardening>Herbaceous plants');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('717','Arts and Leisure>Landscape Gardening>Structures in landscape architecture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('718','Arts and Leisure>Landscape Gardening>Landscape design of cemeteries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('719','Arts and Leisure>Landscape Gardening>Natural landscapes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('720','Arts and Leisure>Architecture>Architecture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('720.92','Arts and Leisure>Architecture>Architects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('721','Arts and Leisure>Architecture>Architectural structure');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('721.6','Arts and Leisure>Architecture>Floors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('721.8','Arts and Leisure>Architecture>Fireplaces (architecture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('722','Arts and Leisure>Architecture>Architecture to ca. 300');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('723','Arts and Leisure>Architecture>Architecture from ca. 300 to 1399');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('724','Arts and Leisure>Architecture>Architecture from 1400');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('725','Arts and Leisure>Architecture>Public structures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('725.11','Arts and Leisure>Architecture>Capitols');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('725.4','Arts and Leisure>Architecture>Factories (architecture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('726','Arts and Leisure>Architecture>Buildings for religious purposes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('726.1','Arts and Leisure>Architecture>Shrines (architecture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('727','Arts and Leisure>Architecture>Buildings for education & research');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('728','Arts and Leisure>Architecture>Residential & related buildings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('728.37','Arts and Leisure>Architecture>House plans');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('728.81','Arts and Leisure>Architecture>Castles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('729','Arts and Leisure>Architecture>Design & decoration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('730','Arts and Leisure>Sculpture>Sculpture, ceramics & metalwork');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('731','Arts and Leisure>Sculpture>Processes, forms & subjects of sculpture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('731.75','Arts and Leisure>Sculpture>Masks (sculpture)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('732','Arts and Leisure>Sculpture>Sculpture to ca. 500');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('733','Arts and Leisure>Sculpture>Greek, Etruscan & Roman sculpture');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('734','Arts and Leisure>Sculpture>Sculpture from ca. 500 to 1399');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('735','Arts and Leisure>Sculpture>Sculpture from 1400');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('736','Arts and Leisure>Sculpture>Carving & carvings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('736.982','Arts and Leisure>Sculpture>Origami');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('737','Arts and Leisure>Sculpture>Numismatics & sigillography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('737.4','Arts and Leisure>Sculpture>Coins');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('737.6','Arts and Leisure>Sculpture>Engraved seals,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('738','Arts and Leisure>Sculpture>Ceramic arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('738.136','Arts and Leisure>Sculpture>Kilns (decorative arts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('739','Arts and Leisure>Sculpture>Metals (decorative arts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('739.27','Arts and Leisure>Sculpture>Jewelry (making)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('739.278','Arts and Leisure>Sculpture>Necklaces (making)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('740','Arts and Leisure>Drawing, Decoration and Design>Drawing & decorative arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('741','Arts and Leisure>Drawing, Decoration and Design>Drawing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('741.5','Arts and Leisure>Drawing, Decoration and Design>Cartoon Drawing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('741.6','Arts and Leisure>Drawing, Decoration and Design>Trading cards (illustration)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('741.692','Arts and Leisure>Drawing, Decoration and Design>Labels (illustration)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('742','Arts and Leisure>Drawing, Decoration and Design>Perspective');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('743','Arts and Leisure>Drawing, Decoration and Design>Drawing & drawings by subject');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('744','Arts and Leisure>Drawing, Decoration and Design>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745','Arts and Leisure>Drawing, Decoration and Design>Folk arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.1','Arts and Leisure>Drawing, Decoration and Design>Antiques');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.4','Arts and Leisure>Drawing, Decoration and Design>Decorations (arts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.5','Arts and Leisure>Drawing, Decoration and Design>Handicrafts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.54','Arts and Leisure>Drawing, Decoration and Design>Tissue paper (handicrafts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.592','Arts and Leisure>Drawing, Decoration and Design>Ships in bottles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.593','Arts and Leisure>Drawing, Decoration and Design>Lampshades');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.594','Arts and Leisure>Drawing, Decoration and Design>Greeting cards (handicrafts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.61','Arts and Leisure>Drawing, Decoration and Design>Calligraphy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.67','Arts and Leisure>Drawing, Decoration and Design>Illumination (decorative arts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.7','Arts and Leisure>Drawing, Decoration and Design>Decorative coloring');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.73','Arts and Leisure>Drawing, Decoration and Design>Stenciling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('745.92','Arts and Leisure>Drawing, Decoration and Design>Floral arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('746','Arts and Leisure>Drawing, Decoration and Design>Textile arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('746.44','Arts and Leisure>Drawing, Decoration and Design>Embroidery');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('746.46','Arts and Leisure>Drawing, Decoration and Design>Quilting (arts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('746.92','Arts and Leisure>Drawing, Decoration and Design>Fashion design');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('747','Arts and Leisure>Drawing, Decoration and Design>Interior Decoration');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('748','Arts and Leisure>Drawing, Decoration and Design>Glass');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('748.5','Arts and Leisure>Drawing, Decoration and Design>Stained glass');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('749','Arts and Leisure>Drawing, Decoration and Design>Furniture & accessories');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('750','Arts and Leisure>Painting>Painting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('751','Arts and Leisure>Painting>Techniques, equipment, materials & forms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('751.4','Arts and Leisure>Painting>Art (Technique)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('751.422','Arts and Leisure>Painting>Watercolor painting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('751.43','Arts and Leisure>Painting>Tempera painting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('752','Arts and Leisure>Painting>Color');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('753','Arts and Leisure>Painting>Symbolism, allegory, mythology & legend');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('754','Arts and Leisure>Painting>Genre paintings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('755','Arts and Leisure>Painting>Religion');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('756','Arts and Leisure>Painting>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('757','Arts and Leisure>Painting>Human figures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('758','Arts and Leisure>Painting>Other subjects');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('759','Arts and Leisure>Painting>Historical, geographic & persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('760','Arts and Leisure>Engraving>Graphic arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('761','Arts and Leisure>Engraving>Relief processes (Block printing)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('762','Arts and Leisure>Engraving>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('763','Arts and Leisure>Engraving>Lithographic processes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('764','Arts and Leisure>Engraving>Chromolithography & serigraphy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('765','Arts and Leisure>Engraving>Metal engraving');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('766','Arts and Leisure>Engraving>Mezzotinting, aquatinting & related processes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('767','Arts and Leisure>Engraving>Etching & drypoint');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('768','Arts and Leisure>Engraving>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('769','Arts and Leisure>Engraving>Prints');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('769.55','Arts and Leisure>Engraving>Paper Money');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('769.56','Arts and Leisure>Engraving>Stamps');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('769.57','Arts and Leisure>Engraving>Labels (prints)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('770','Arts and Leisure>Photography>Photography & computer art');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('771','Arts and Leisure>Photography>Techniques, equipment & materials');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('771.1','Arts and Leisure>Photography>Darkrooms (photography)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('772','Arts and Leisure>Photography>Metallic salt processes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('773','Arts and Leisure>Photography>Pigment processes of printing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('774','Arts and Leisure>Photography>Holography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('775','Arts and Leisure>Photography>Digital Photography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('776','Arts and Leisure>Photography>Computer art (Digital art)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('777','Arts and Leisure>Photography>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('778','Arts and Leisure>Photography>Fields & kinds of photography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('779','Arts and Leisure>Photography>Photographs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('780','Arts and Leisure>Music>Music');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('780.148','Arts and Leisure>Music>Reading music');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('780.78','Arts and Leisure>Music>Concerts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('780.92','Arts and Leisure>Music>Composers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('781','Arts and Leisure>Music>General principles & musical forms');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('781.65','Arts and Leisure>Music>Jazz');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('781.66','Arts and Leisure>Music>Rock music');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('781.68','Arts and Leisure>Music>Classical music');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782','Arts and Leisure>Music>Vocal music');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.1','Arts and Leisure>Music>Operas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.14','Arts and Leisure>Music>Musicals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.25','Arts and Leisure>Music>Sacred songs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.27','Arts and Leisure>Music>Hymns');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.29','Arts and Leisure>Music>Liturgical music');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.323','Arts and Leisure>Music>Kyrie (music)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.421','Arts and Leisure>Music>Jazz (songs)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('782.5','Arts and Leisure>Music>Choirs');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('783','Arts and Leisure>Music>Voice');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('783.99','Arts and Leisure>Music>Kazoo');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('784','Arts and Leisure>Music>Instruments & instrumental ensembles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('784.184','Arts and Leisure>Music>Symphonies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('784.19','Arts and Leisure>Music>Instruments (music)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('785','Arts and Leisure>Music>Ensembles with one instrument per part');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('786','Arts and Leisure>Music>Keyboard instruments');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('787','Arts and Leisure>Music>Stringed instruments');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('787.7','Arts and Leisure>Music>Zither');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('787.87','Arts and Leisure>Music>Guitars');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('787.89','Arts and Leisure>Music>Ukuleles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('788','Arts and Leisure>Music>Wind instruments');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('789','Arts and Leisure>Music>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('790','Arts and Leisure>Amusements and Recreation>Sports, games & entertainment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('790.1','Arts and Leisure>Amusements and Recreation>Leisure');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('790.13','Arts and Leisure>Amusements and Recreation>Hobbies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('790.132','Arts and Leisure>Amusements and Recreation>Collecting (recreation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('790.133','Arts and Leisure>Amusements and Recreation>Toys');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791','Arts and Leisure>Amusements and Recreation>Public performances');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.068','Arts and Leisure>Amusements and Recreation>Theme parks');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.3','Arts and Leisure>Amusements and Recreation>Circuses');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.35','Arts and Leisure>Amusements and Recreation>Sideshows');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.43','Arts and Leisure>Amusements and Recreation>Cinema');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.437','Arts and Leisure>Amusements and Recreation>Film scripts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.44','Arts and Leisure>Amusements and Recreation>Radio (performing arts)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.446','Arts and Leisure>Amusements and Recreation>Soap operas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('791.8','Arts and Leisure>Amusements and Recreation>Show animals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('792','Arts and Leisure>Amusements and Recreation>Drama (theater)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('792.024','Arts and Leisure>Amusements and Recreation>Visual effects (dramatic performances)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('792.026','Arts and Leisure>Amusements and Recreation>Theatrical costumes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('792.23','Arts and Leisure>Amusements and Recreation>Comedies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('792.82','Arts and Leisure>Amusements and Recreation>Choreography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793','Arts and Leisure>Amusements and Recreation>Indoor games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.2','Arts and Leisure>Amusements and Recreation>Party Planning');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.3','Arts and Leisure>Amusements and Recreation>Dance');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.33','Arts and Leisure>Amusements and Recreation>Ballroom dancing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.73','Arts and Leisure>Amusements and Recreation>Quizzes (recreation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.795','Arts and Leisure>Amusements and Recreation>Games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.809','Arts and Leisure>Amusements and Recreation>Magicians (performers)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('793.93','Arts and Leisure>Amusements and Recreation>Fantasy games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('794','Arts and Leisure>Amusements and Recreation>Board Games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('794.8','Arts and Leisure>Amusements and Recreation>Computer games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('795','Arts and Leisure>Amusements and Recreation>Gambling (recreation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('795.38','Arts and Leisure>Amusements and Recreation>Lotteries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('795.4','Arts and Leisure>Amusements and Recreation>Card Games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796','Arts and Leisure>Amusements and Recreation>Athletic Games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.3','Arts and Leisure>Amusements and Recreation>Ball games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.312','Arts and Leisure>Amusements and Recreation>Handball');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.322','Arts and Leisure>Amusements and Recreation>Kicking (American football)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.33','Arts and Leisure>Amusements and Recreation>Football');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.334','Arts and Leisure>Amusements and Recreation>Soccer');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.352','Arts and Leisure>Amusements and Recreation>Golf');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.357','Arts and Leisure>Amusements and Recreation>Baseball');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.4','Arts and Leisure>Amusements and Recreation>Weight lifting, track & field,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.42','Arts and Leisure>Amusements and Recreation>Track & field');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.48','Arts and Leisure>Amusements and Recreation>Olympic Games');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.5','Arts and Leisure>Amusements and Recreation>Hiking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.51','Arts and Leisure>Amusements and Recreation>Backpacking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.522','Arts and Leisure>Amusements and Recreation>Rock climbing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.6','Arts and Leisure>Amusements and Recreation>Cycling & related activities');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.7','Arts and Leisure>Amusements and Recreation>Driving motor vehicles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.72','Arts and Leisure>Amusements and Recreation>Auto Racing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.79','Arts and Leisure>Amusements and Recreation>Motor homes (recreation)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.8','Arts and Leisure>Amusements and Recreation>Martial Arts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.812','Arts and Leisure>Amusements and Recreation>Wrestling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.815','Arts and Leisure>Amusements and Recreation>Karate');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.9','Arts and Leisure>Amusements and Recreation>Snow sports');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.91','Arts and Leisure>Amusements and Recreation>Ice skating');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('796.962','Arts and Leisure>Amusements and Recreation>Hockey');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('797','Arts and Leisure>Amusements and Recreation>Aquatic & air sports');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('797.122','Arts and Leisure>Amusements and Recreation>Canoeing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('797.124','Arts and Leisure>Amusements and Recreation>Sailing (sports)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('797.125','Arts and Leisure>Amusements and Recreation>Motorboating');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('797.23','Arts and Leisure>Amusements and Recreation>Skin diving');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('797.5','Arts and Leisure>Amusements and Recreation>Air sports');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('798','Arts and Leisure>Amusements and Recreation>Equestrian sports & animal racing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('798.092','Arts and Leisure>Amusements and Recreation>Equestrians');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('798.6','Arts and Leisure>Amusements and Recreation>Coaching');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799','Arts and Leisure>Amusements and Recreation>Fishing, hunting & shooting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799.1','Arts and Leisure>Amusements and Recreation>Fishing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799.2','Arts and Leisure>Amusements and Recreation>Hunting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799.202','Arts and Leisure>Amusements and Recreation>Guns (sports)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799.26','Arts and Leisure>Amusements and Recreation>Big Game Hunting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799.276','Arts and Leisure>Amusements and Recreation>Deer (hunting)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('799.3','Arts and Leisure>Amusements and Recreation>Shooting other than game');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('8','Literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('80','Literature>By Topic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('800','Literature>By Topic>Literature, rhetoric & criticism');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('801','Literature>By Topic>Philosophy & theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('802','Literature>By Topic>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('803','Literature>By Topic>Dictionaries & encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('804','Literature>By Topic>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('805','Literature>By Topic>Serial publications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('806','Literature>By Topic>Organizations & management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('807','Literature>By Topic>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808','Literature>By Topic>English Grammar');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.1','Literature>By Topic>Poetry Writing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.2','Literature>By Topic>Playwriting And Screenwriting');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.3','Literature>By Topic>Fiction Writing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.4','Literature>By Topic>Essay Writing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.5','Literature>By Topic>Public Speaking');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.53','Literature>By Topic>Debating');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.543','Literature>By Topic>Storytelling');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.6','Literature>By Topic>Letter Writing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.7','Literature>By Topic>Comedy Writing');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.8','Literature>By Topic>Anthologies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.802','Literature>By Topic>Narration (literature)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.803','Literature>By Topic>Heroism (literature)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.81','Literature>By Topic>Literary forms (genres)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.813','Literature>By Topic>Narrative poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.814','Literature>By Topic>Odes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.817','Literature>By Topic>Humorous poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.82','Literature>By Topic>Drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.83','Literature>By Topic>Fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.831','Literature>By Topic>Short stories');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.838','Literature>By Topic>Fantasy fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.839','Literature>By Topic>Humorous fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.84','Literature>By Topic>Essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.85','Literature>By Topic>Speeches (literature)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.86','Literature>By Topic>Letters (literature)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.87','Literature>By Topic>Humor (literature)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.882','Literature>By Topic>Jokes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('808.9','Literature>By Topic>Non-English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('809','Literature>By Topic>History And Criticism Of Three Or More Works');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('809.3','Literature>By Topic>Fiction  writers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810','Literature>American and Canadian>American Literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.1','Literature>American and Canadian>Literary Theory and Criticism - General');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.2','Literature>American and Canadian>Abridged or Condensed Works');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.3','Literature>American and Canadian>Dictionaries And Encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.4','Literature>American and Canadian>Literary Criticism - Specific Authors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.5','Literature>American and Canadian>Periodicals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.52','Literature>American and Canadian>American Literature - 1900-1945');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.54','Literature>American and Canadian>American Literature - 1945+');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.6','Literature>American and Canadian>Societies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.7','Literature>American and Canadian>Study and Teaching');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.8','Literature>American and Canadian>Anthologies and Collections');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('810.9','Literature>American and Canadian>History of American Literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811','Literature>American and Canadian>Poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811.1','Literature>American and Canadian>Colonial (1607-1776)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811.2','Literature>American and Canadian>Post-Revolutionary (1776-1830)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811.3','Literature>American and Canadian>Middle 19th Century (1830-1861)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811.4','Literature>American and Canadian>Later 19th Century (1861-1900)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811.5','Literature>American and Canadian>20th Century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('811.6','Literature>American and Canadian>21st Century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('812','Literature>American and Canadian>Drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813','Literature>American and Canadian>Fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.1','Literature>American and Canadian>Colonial 1607-1776');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.2','Literature>American and Canadian>Post-Revolutionary 1776-1830');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.3','Literature>American and Canadian>Middle 19th Century 1830-1861');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.4','Literature>American and Canadian>Later 19th Century 1861-1900');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.49','Literature>American and Canadian>Minor novelists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.5','Literature>American and Canadian>20th Century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.52','Literature>American and Canadian>Fiction>20th Century>1900-1944');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.54','Literature>American and Canadian>Fiction>20th Century>1945-1999');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('813.6','Literature>American and Canadian>21st Century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('814','Literature>American and Canadian>Essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('815','Literature>American and Canadian>American Speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('816','Literature>American and Canadian>American Letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('817','Literature>American and Canadian>American Wit and Humor');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818','Literature>American and Canadian>Authors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818.1','Literature>American and Canadian>Colonial 1607-1776');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818.2','Literature>American and Canadian>Post-Revolutionary 1776-1830');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818.3','Literature>American and Canadian>Middle 19th Century 1830-61');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818.4','Literature>American and Canadian>Later 19th Century 1861-1900');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818.5','Literature>American and Canadian>20th Century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('818.6','Literature>American and Canadian>21st Century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('819','Literature>American and Canadian>Canadian literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820','Literature>English>English & Old English literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.1','Literature>English>Philosophy And Psychology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.2','Literature>English>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.3','Literature>English>Dictionaries And Encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.4','Literature>English>Essays on English Literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.5','Literature>English>Periodicals');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.6','Literature>English>Societies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.7','Literature>English>Education And Research');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.8','Literature>English>Collections');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('820.9','Literature>English>Biography And History');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('821','Literature>English>English poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822','Literature>English>English Drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.1','Literature>English>Early English 1066-1400');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.2','Literature>English>Pre-Elizabethan 1400-1558');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.3','Literature>English>Elizabethan 1558-1625');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.33','Literature>English>Works by Shakespeare');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.4','Literature>English>Post-Elizabethan 1625-1702');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.5','Literature>English>Queen Anne 1702-45');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.6','Literature>English>Later 18th century 1745-1800');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.7','Literature>English>Early 19th century 1800-37');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.8','Literature>English>Victorian period 1837-1900');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('822.9','Literature>English>1900-');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823','Literature>English>Literature>English>Fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.01','Literature>English>Short Stories');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.1','Literature>English>Early English 1066-1400');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.2','Literature>English>Pre-Elizabethan 1400-1558');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.3','Literature>English>Elizabethan 1558-1625');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.4','Literature>English>Post-Elizabethan 1625-1702');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.5','Literature>English>Queen Anne 1702-45');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.6','Literature>English>Later 18th century 1745-1800');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.7','Literature>English>Early 19th century 1800-37');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.8','Literature>English>Victorian period 1837-1900');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('823.9','Literature>English>Modern Period');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('824','Literature>English>English essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('825','Literature>English>English speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('826','Literature>English>English letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('827','Literature>English>English humor & satire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('828','Literature>English>Authors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829','Literature>English>Old English literature,ca. 450-1100');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.1','Literature>English>Poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.2','Literature>English>Cædmon');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.3','Literature>English>Beowulf');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.4','Literature>English>Cynewulf');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.5','Literature>English>Homilies and religious');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.7','Literature>English>Alfred the Great');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.8','Literature>English>Miscellaneous');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('829.9','Literature>English>Historical and biographical');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('830','Literature>German>German & related literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('831','Literature>German>German poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('832','Literature>German>German drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('833','Literature>German>German fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('834','Literature>German>German essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('835','Literature>German>German speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('836','Literature>German>German letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('837','Literature>German>German humor & satire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('838','Literature>German>German miscellaneous writings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('839','Literature>German>Other Germanic literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('839.2','Literature>German>Frisian literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('840','Literature>French>French & related literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('841','Literature>French>French poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('842','Literature>French>French drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('843','Literature>French>French fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('844','Literature>French>French essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('845','Literature>French>French speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('846','Literature>French>French letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('847','Literature>French>French humor & satire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('848','Literature>French>French miscellaneous writings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('849','Literature>French>Occitan & Catalan literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('850','Literature>Italian and Romanian>Italian, Romanian & related literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('851','Literature>Italian and Romanian>Italian poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('852','Literature>Italian and Romanian>Italian drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('853','Literature>Italian and Romanian>Italian fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('854','Literature>Italian and Romanian>Italian essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('855','Literature>Italian and Romanian>Italian speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('856','Literature>Italian and Romanian>Italian letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('857','Literature>Italian and Romanian>Italian humor & satire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('858','Literature>Italian and Romanian>Italian miscellaneous writings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('859','Literature>Italian and Romanian>Romanian & related literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('860','Literature>Spanish and Portuguese>Spanish Literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('861','Literature>Spanish and Portuguese>Spanish poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('862','Literature>Spanish and Portuguese>Spanish drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('863','Literature>Spanish and Portuguese>Spanish fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('864','Literature>Spanish and Portuguese>Spanish essays');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('865','Literature>Spanish and Portuguese>Speeches,addresses,etc.,Spanish');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('866','Literature>Spanish and Portuguese>Spanish letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('867','Literature>Spanish and Portuguese>Spanish wit and humor');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('868','Literature>Spanish and Portuguese>Authors');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('869','Literature>Spanish and Portuguese>Portuguese Literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('870','Literature>Latin>Latin & Italic literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('871','Literature>Latin>Latin poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('872','Literature>Latin>Latin dramatic poetry & drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('873','Literature>Latin>Latin epic poetry & fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('874','Literature>Latin>Latin lyric poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('875','Literature>Latin>Latin speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('876','Literature>Latin>Latin letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('877','Literature>Latin>Latin humor & satire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('878','Literature>Latin>Latin miscellaneous writings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('879','Literature>Latin>Literatures of other Italic languages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('880','Literature>Greek and Other Classical>Classical & modern Greek literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('881','Literature>Greek and Other Classical>Classical Greek poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('882','Literature>Greek and Other Classical>Classical Greek dramatic poetry & drama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('883','Literature>Greek and Other Classical>Classical Greek epic poetry & fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('884','Literature>Greek and Other Classical>Classical Greek lyric poetry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('885','Literature>Greek and Other Classical>Classical Greek speeches');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('886','Literature>Greek and Other Classical>Classical Greek letters');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('887','Literature>Greek and Other Classical>Classical Greek humor & satire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('888','Literature>Greek and Other Classical>Classical Greek miscellaneous writings');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('889','Literature>Greek and Other Classical>Modern Greek literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('890','Literature>Other Languages>Other literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('891','Literature>Other Languages>East Indo-European & Celtic literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('891.6','Literature>Other Languages>Celtic literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('891.7','Literature>Other Languages>East');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('891.8','Literature>Other Languages>Slavic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('892','Literature>Other Languages>Afro-Asiatic literatures and Semitic literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('893','Literature>Other Languages>Non-Semitic Afro-Asiatic literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('894','Literature>Other Languages>Altaic, Uralic, Hyperborean & Dravidian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('894.5','Literature>Other Languages>Finno-Ugric');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('894.6','Literature>Other Languages>Ainu literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('894.8','Literature>Other Languages>Dravidian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('895','Literature>Other Languages>Literatures of East & Southeast Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('896','Literature>Other Languages>African literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('897','Literature>Other Languages>Native American literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('898','Literature>Other Languages>South American native literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('899','Literature>Other Languages>Austronesian & other literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('899.92','Literature>Other Languages>Basque');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('899.95','Literature>Other Languages>Sumerian literature');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('899.96','Literature>Other Languages>Caucasian literatures');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('9','Biography and History');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('90','Biography and History>History');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('900','Biography and History>History>History');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('901','Biography and History>History>Philosophy & theory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('902','Biography and History>History>Miscellany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('903','Biography and History>History>Dictionaries And Encyclopedias');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('904','Biography and History>History>Catastrophes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('905','Biography and History>History>Serial publications');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('906','Biography and History>History>Organizations & management');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('907','Biography and History>History>Education, research & related topics');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('907.4','Biography and History>History>Exhibitions');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('908','Biography and History>History>Kinds of persons treatment');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('909','Biography and History>History>Civilization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('909.0491497','Biography and History>History>Romanies');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('909.07','Biography and History>History>Crusades');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('909.81','Biography and History>History>Nineteenth century');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('909.825','Biography and History>History>Nineteen fifties');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('910','Biography and History>Geography, Voyages and Travel>Geography & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('910.46','Biography and History>Geography, Voyages and Travel>Hotels');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('910.468','Biography and History>Geography, Voyages and Travel>RV camps');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('910.9','Biography and History>Geography, Voyages and Travel>Explorations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('910.92','Biography and History>Geography, Voyages and Travel>Explorers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('911','Biography and History>Geography, Voyages and Travel>Historical geography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('912','Biography and History>Geography, Voyages and Travel>Atlases');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('913','Biography and History>Geography, Voyages and Travel>Ancient World');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('914','Biography and History>Geography, Voyages and Travel>Geography of & travel in Europe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('914.919','Biography and History>Geography, Voyages and Travel>Travel Guides');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('915','Biography and History>Geography, Voyages and Travel>Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('916','Biography and History>Geography, Voyages and Travel>Celts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917','Biography and History>Geography, Voyages and Travel>Geography of & travel in North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.1','Biography and History>Geography, Voyages and Travel>Canada--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.11','Biography and History>Geography, Voyages and Travel>British Columbia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.123','Biography and History>Geography, Voyages and Travel>Alberta--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.124','Biography and History>Geography, Voyages and Travel>Saskatchewan--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.127','Biography and History>Geography, Voyages and Travel>Manitoba--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.13','Biography and History>Geography, Voyages and Travel>Ontario--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.14','Biography and History>Geography, Voyages and Travel>Quebec--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.16','Biography and History>Geography, Voyages and Travel>Nova Scotia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.17','Biography and History>Geography, Voyages and Travel>Prince Edward--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.182','Biography and History>Geography, Voyages and Travel>Labrador--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.188','Biography and History>Geography, Voyages and Travel>Saint Pierre--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.191','Biography and History>Geography, Voyages and Travel>Yukon Territory--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.193','Biography and History>Geography, Voyages and Travel>Northwest Territories (1999-)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.1952','Biography and History>Geography, Voyages and Travel>Baffin Region (Qikiqtaaluk)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.1958','Biography and History>Geography, Voyages and Travel>Keewatin Region (Kivallik)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.281','Biography and History>Geography, Voyages and Travel>Guatemala--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.282','Biography and History>Geography, Voyages and Travel>Belize--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.283','Biography and History>Geography, Voyages and Travel>Honduras--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.284','Biography and History>Geography, Voyages and Travel>El Salvador--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.285','Biography and History>Geography, Voyages and Travel>Nicaragua--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.286','Biography and History>Geography, Voyages and Travel>Costa Rica--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.287','Biography and History>Geography, Voyages and Travel>Panama--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.2875','Biography and History>Geography, Voyages and Travel>Panama Canal');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.29','Biography and History>Geography, Voyages and Travel>West Indies (Antilles)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.291','Biography and History>Geography, Voyages and Travel>Cuba--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.292','Biography and History>Geography, Voyages and Travel>Jamaica and Cayman Islands--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.293','Biography and History>Geography, Voyages and Travel>Dominican Republic--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.294','Biography and History>Geography, Voyages and Travel>Haiti--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.295','Biography and History>Geography, Voyages and Travel>Puerto Rico--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.296','Biography and History>Geography, Voyages and Travel>Bahama Islands--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.29722','Biography and History>Geography, Voyages and Travel>Virgin Islands--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.2976','Biography and History>Geography, Voyages and Travel>Guadeloupe--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.2986','Biography and History>Geography, Voyages and Travel>Dutch West Indies/Netherlands islands--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.299','Biography and History>Geography, Voyages and Travel>Bermuda--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.3','Biography and History>Geography, Voyages and Travel>United States (Travel)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.41','Biography and History>Geography, Voyages and Travel>Maine--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.42','Biography and History>Geography, Voyages and Travel>New Hampshire--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.43','Biography and History>Geography, Voyages and Travel>Vermont--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.44','Biography and History>Geography, Voyages and Travel>Massachusetts--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.45','Biography and History>Geography, Voyages and Travel>Rhode Island--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.46','Biography and History>Geography, Voyages and Travel>Connecticut--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.47','Biography and History>Geography, Voyages and Travel>New York (State)--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.48','Biography and History>Geography, Voyages and Travel>Pennsylvania--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.49','Biography and History>Geography, Voyages and Travel>New Jersey--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.51','Biography and History>Geography, Voyages and Travel>Delaware--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.52','Biography and History>Geography, Voyages and Travel>Maryland--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.53','Biography and History>Geography, Voyages and Travel>District of Columba--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.54','Biography and History>Geography, Voyages and Travel>West Virginia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.55','Biography and History>Geography, Voyages and Travel>Virginia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.56','Biography and History>Geography, Voyages and Travel>North Carolina--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.57','Biography and History>Geography, Voyages and Travel>South Carolina--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.58','Biography and History>Geography, Voyages and Travel>Georgia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.59','Biography and History>Geography, Voyages and Travel>Florida--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.61','Biography and History>Geography, Voyages and Travel>Alabama--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.62','Biography and History>Geography, Voyages and Travel>Mississippi--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.63','Biography and History>Geography, Voyages and Travel>Louisiana--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.64','Biography and History>Geography, Voyages and Travel>Texas--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.66','Biography and History>Geography, Voyages and Travel>Oklahoma--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.67','Biography and History>Geography, Voyages and Travel>Arkansas--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.68','Biography and History>Geography, Voyages and Travel>Tennessee--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.69','Biography and History>Geography, Voyages and Travel>Kentucky--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.71','Biography and History>Geography, Voyages and Travel>Ohio--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.72','Biography and History>Geography, Voyages and Travel>Indiana--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.73','Biography and History>Geography, Voyages and Travel>Illinois--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.74','Biography and History>Geography, Voyages and Travel>Michigan--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.75','Biography and History>Geography, Voyages and Travel>Wisconsin--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.76','Biography and History>Geography, Voyages and Travel>Minnesota--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.77','Biography and History>Geography, Voyages and Travel>Iowa--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.78','Biography and History>Geography, Voyages and Travel>Missouri--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.81','Biography and History>Geography, Voyages and Travel>Kansas--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.82','Biography and History>Geography, Voyages and Travel>Nebraska--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.83','Biography and History>Geography, Voyages and Travel>South Dakota--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.84','Biography and History>Geography, Voyages and Travel>North Dakota--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.86','Biography and History>Geography, Voyages and Travel>Montana--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.87','Biography and History>Geography, Voyages and Travel>Wyoming--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.88','Biography and History>Geography, Voyages and Travel>Colorado--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.89','Biography and History>Geography, Voyages and Travel>New Mexico--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.91','Biography and History>Geography, Voyages and Travel>Arizona--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.92','Biography and History>Geography, Voyages and Travel>Utah--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.93','Biography and History>Geography, Voyages and Travel>Nevada--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.94','Biography and History>Geography, Voyages and Travel>California--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.95','Biography and History>Geography, Voyages and Travel>Oregon--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.96','Biography and History>Geography, Voyages and Travel>Idaho--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.97','Biography and History>Geography, Voyages and Travel>Washington--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.98','Biography and History>Geography, Voyages and Travel>Alaska--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('917.984','Biography and History>Geography, Voyages and Travel>Southwestern Alaska');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918','Biography and History>Geography, Voyages and Travel>Geography of & travel in South America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.1','Biography and History>Geography, Voyages and Travel>Brazil--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.2','Biography and History>Geography, Voyages and Travel>Argentina--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.3','Biography and History>Geography, Voyages and Travel>Chile--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.4','Biography and History>Geography, Voyages and Travel>Bolivia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.5','Biography and History>Geography, Voyages and Travel>Peru--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.61','Biography and History>Geography, Voyages and Travel>Colombia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.66','Biography and History>Geography, Voyages and Travel>Ecuador--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.7','Biography and History>Geography, Voyages and Travel>Venezuela--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.81','Biography and History>Geography, Voyages and Travel>Guyana--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.82','Biography and History>Geography, Voyages and Travel>French Guiana (Guyane)--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.83','Biography and History>Geography, Voyages and Travel>Surinam (Suriname)--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.92','Biography and History>Geography, Voyages and Travel>Paraguay--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('918.95','Biography and History>Geography, Voyages and Travel>Uruguay--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('919','Biography and History>Geography, Voyages and Travel>Geography of & travel in other areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('919.4','Biography and History>Geography, Voyages and Travel>Australia--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('919.711','Biography and History>Geography, Voyages and Travel>Falkland Islands (Islas Malvinas)--description & travel');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920','Biography and History>Biography>Biography & genealogy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.1','Biography and History>Biography>Bibliographers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.2','Biography and History>Biography>Librarians');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.3','Biography and History>Biography>Encyclopedists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.4','Biography and History>Biography>Publishers, Booksellers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.5','Biography and History>Biography>Journalists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.6','Biography and History>Biography>Academicians');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.7','Biography and History>Biography>By Gender');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.8','Biography and History>Biography>Eccentrics, cranks, fools, insane, etc.');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('920.9','Biography and History>Biography>Phrenologists, somnambulists, mindreaders, magicians, etc.');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('921','Biography and History>Biography>Of Philosophy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('922','Biography and History>Biography>Obituaries');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('923','Biography and History>Biography>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('924','Biography and History>Biography>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925','Biography and History>Biography>Of Science');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.1','Biography and History>Biography>Mathematicians');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.2','Biography and History>Biography>Astronomers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.3','Biography and History>Biography>Physicists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.4','Biography and History>Biography>Chemists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.5','Biography and History>Biography>Geologists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.6','Biography and History>Biography>Paleontologists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.7','Biography and History>Biography>Biologists And Anthropologists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.8','Biography and History>Biography>Botanists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('925.9','Biography and History>Biography>Zoologists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('926','Biography and History>Biography>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('927','Biography and History>Biography>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('928','Biography and History>Biography>(Optional number)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('928.1','Biography and History>Biography>American writers');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929','Biography and History>Biography>Genealogy and Heraldry');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.1','Biography and History>Biography>Genealogy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.2','Biography and History>Biography>Family histories');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.3','Biography and History>Biography>Census records (genealogy)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.44','Biography and History>Biography>Baby names');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.6','Biography and History>Biography>Tartans');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.7','Biography and History>Biography>Knighthood');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.92','Biography and History>Biography>National flags');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('929.97','Biography and History>Biography>Names');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('930','Biography and History>Ancient World>History of ancient world (to ca. 499)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('930.1','Biography and History>Ancient World>Archaeology');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('930.102','Biography and History>Ancient World>Excavation (archaeological technique)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('930.109','Biography and History>Ancient World>Archaeologists');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('931','Biography and History>Ancient World>China to 420');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('932','Biography and History>Ancient World>Egypt to 640');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('933','Biography and History>Ancient World>Palestine to 70');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('934','Biography and History>Ancient World>India to 647');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('935','Biography and History>Ancient World>Mesopotamia & Iranian Plateau to 637');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('936','Biography and History>Ancient World>Europe north & west of Italy to ca. 499');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('937','Biography and History>Ancient World>Italy & adjacent territories to 476');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('937.06','Biography and History>Ancient World>Roman Empire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('938','Biography and History>Ancient World>Greece to 323');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('939','Biography and History>Ancient World>Other parts of ancient world to ca. 640');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('940','Biography and History>Europe>History of Europe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('940.12','Biography and History>Europe>Dark Ages');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('940.192','Biography and History>Europe>Black Death (History)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('940.3','Biography and History>Europe>World  Wars');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('940.531','Biography and History>Europe>Holocaust');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('941','Biography and History>Europe>British Isles');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('942','Biography and History>Europe>England And Wales');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('943','Biography and History>Europe>Central Europe and Germany');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('943.086','Biography and History>Europe>Third Reich');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('944','Biography and History>Europe>France');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('945','Biography and History>Europe>Italy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('946','Biography and History>Europe>Spain');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('947','Biography and History>Europe>Eastern Europe and Russia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('948','Biography and History>Europe>Scandinavia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('949','Biography and History>Europe>Other parts of Europe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('950','Biography and History>Asia>History of Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('951','Biography and History>Asia>China (country)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('951.9','Biography and History>Asia>Korea');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('951.904','Biography and History>Asia>Korean  War,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('952','Biography and History>Asia>Japan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('953','Biography and History>Asia>Arabian Peninsula & adjacent areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('953.67','Biography and History>Asia>Kuwait');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('954','Biography and History>Asia>South Asia and India');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('955','Biography and History>Asia>Iran');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('956','Biography and History>Asia>Middle East');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('957','Biography and History>Asia>Siberia (Asiatic Russia)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('958','Biography and History>Asia>Central Asia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('959','Biography and History>Asia>Asia (History)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('959.6','Biography and History>Asia>Cambodia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('959.7','Biography and History>Asia>Vietnam');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('960','Biography and History>Africa>History of Africa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('961','Biography and History>Africa>Tunisia & Libya');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('962','Biography and History>Africa>Egypt');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('963','Biography and History>Africa>Ethiopia & Eritrea');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('964','Biography and History>Africa>Northwest African coast & offshore islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('965','Biography and History>Africa>Algeria');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('966','Biography and History>Africa>West Africa & offshore islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('967','Biography and History>Africa>Central Africa & offshore islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('968','Biography and History>Africa>Southern Africa and the Republic of South Africa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('969','Biography and History>Africa>South Indian Ocean islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('970','Biography and History>North America>History of North America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('970.00497','Biography and History>North America>American native peoples');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('970.01','Biography and History>North America>Early history to 1599');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('970.011','Biography and History>North America>Earliest history to 1492');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('970.015','Biography and History>North America>Columbus, Christopher--North American');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('970.1','Biography and History>North America>Native Americans history');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971','Biography and History>North America>Canada');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.02','Biography and History>North America>Early America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.1','Biography and History>North America>British Columbia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.23','Biography and History>North America>Alberta');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.24','Biography and History>North America>Saskatchewan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.27','Biography and History>North America>Manitoba');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.3','Biography and History>North America>Ontario');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.4','Biography and History>North America>Quebec');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.6','Biography and History>North America>Nova Scotia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.7','Biography and History>North America>Prince Edward Island');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.82','Biography and History>North America>Labrador');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.88','Biography and History>North America>Saint Pierre and Miquelon');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.91','Biography and History>North America>Yukon Territory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.93','Biography and History>North America>Northwest Territories (1999- )');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.95','Biography and History>North America>Nunavut');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.952','Biography and History>North America>Baffin Region (Qikiqtaaluk Region)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('971.958','Biography and History>North America>Keewatin Region (Kivallik Region)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972','Biography and History>North America>Mexico');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.6','Biography and History>North America>Southern Gulf states of Mexico');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.8','Biography and History>North America>Central America (History)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.81','Biography and History>North America>Guatemala');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.82','Biography and History>North America>Belize');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.83','Biography and History>North America>Honduras');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.84','Biography and History>North America>El Salvador');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.85','Biography and History>North America>Nicaragua');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.86','Biography and History>North America>Costa Rica');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.87','Biography and History>North America>Panama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.875','Biography and History>North America>Canal Area');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.9','Biography and History>North America>West Indies (Antilles) and Bermuda');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.91','Biography and History>North America>Cuba');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.92','Biography and History>North America>Jamaica and Cayman Islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.93','Biography and History>North America>Dominican Republic');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.94','Biography and History>North America>Haiti');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.95','Biography and History>North America>Puerto Rico');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.96','Biography and History>North America>Bahama Islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.9722','Biography and History>North America>Virgin Islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.976','Biography and History>North America>Guadeloupe');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.986','Biography and History>North America>Netherlands islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('972.99','Biography and History>North America>Bermuda');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973','Biography and History>North America>United States (History)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.046','Biography and History>North America>Hispanic History');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.0496073','Biography and History>North America>African Americans');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.05','Biography and History>North America>African Americans (History)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.1','Biography and History>North America>Early History to 1607');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.2','Biography and History>North America>Colonial period, 1607-1775');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.25','Biography and History>North America>Colonial period, 1689-1732');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.26','Biography and History>North America>Period of extension');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.3','Biography and History>North America>Revolution and confederation (1775-89)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.3092','Biography and History>North America>United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.311','Biography and History>North America>Stamp Act (U.S.history)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.313','Biography and History>North America>Declaration of Independence,');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.318','Biography and History>North America>Period of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.4','Biography and History>North America>Washington Through Jefferson Administrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.44','Biography and History>North America>Administration of John Adams');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.46','Biography and History>North America>Administration of Thomas Jefferson');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.47','Biography and History>North America>Tripolitan War, 1801-1805');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.52','Biography and History>North America>War of 1812, 1812-1815');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.53','Biography and History>North America>War with Algiers, 1815');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.61','Biography and History>North America>Administration of James Knox Polk');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.62','Biography and History>North America>Mexican War, 1845-1848');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.66','Biography and History>North America>Administration of Franklin Pierce');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.7','Biography and History>North America>Administration of Abraham Lincoln');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.711','Biography and History>North America>Underground railroad (Civil War,U.S.)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.7113','Biography and History>North America>Wilmot Proviso, 1847');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.713','Biography and History>North America>Secession of Souther States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.8','Biography and History>North America>Reconstruction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.82','Biography and History>North America>Administration of Ulysses Grant');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.83','Biography and History>North America>Administration of Rutherford Hayes');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.84','Biography and History>North America>Administration of James Garfield');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.85','Biography and History>North America>First Administration of Grover Cleveland');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.86','Biography and History>North America>Administration of Benjamin Harrison');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.87','Biography and History>North America>Second Administration of Grover Cleveland');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.88','Biography and History>North America>Administration of William McKinley');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.89','Biography and History>North America>Spanish-American War');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.9','Biography and History>North America>Roosevelt Administration and Beyond');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.91','Biography and History>North America>Roosevelt thru Truman Administrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.911','Biography and History>North America>Administration of Theodore Roosevelt');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.912','Biography and History>North America>Administration of William Howard Taft');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.92','Biography and History>North America>Eisenhower thru Clinton Administrations');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.921','Biography and History>North America>Administration of Dwight Eisenhower');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.922','Biography and History>North America>Administration of John F. Kennedy');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.923','Biography and History>North America>Administration of Lyndon B. Johnson');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.924','Biography and History>North America>Administration of Richard M. Nixon');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.925','Biography and History>North America>Administration of Gerald Ford');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.926','Biography and History>North America>Administration of Jimmy Carter');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.927','Biography and History>North America>Administration of Ronald Reagan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.928','Biography and History>North America>Administration of George Herbert Walker Bush');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.929','Biography and History>North America>Administration of Bill Clinton');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.93','Biography and History>North America>George W. Bush Administration and Beyond');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.931','Biography and History>North America>Administration of George W. Bush');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('973.932','Biography and History>North America>Administration of Barack Obama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974','Biography and History>North America>Northeastern United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.1','Biography and History>North America>Maine');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.2','Biography and History>North America>New Hampshire');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.3','Biography and History>North America>Vermont');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.4','Biography and History>North America>Massachusetts');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.5','Biography and History>North America>Rhode Island');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.6','Biography and History>North America>Connecticut');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.7','Biography and History>North America>New York (State)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.702','Biography and History>North America>New York (State)--1620-1776');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.8','Biography and History>North America>Pennsylvania');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('974.9','Biography and History>North America>New Jersey');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975','Biography and History>North America>Southeastern U.S.');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.1','Biography and History>North America>Delaware');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.2','Biography and History>North America>Maryland');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.3','Biography and History>North America>District of');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.4','Biography and History>North America>West Virginia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.5','Biography and History>North America>Virginia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.6','Biography and History>North America>North Carolina');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.7','Biography and History>North America>South Carolina');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.8','Biography and History>North America>Georgia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.9','Biography and History>North America>Florida');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.901','Biography and History>North America>Early');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('975.902','Biography and History>North America>English');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976','Biography and History>North America>South central United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.1','Biography and History>North America>Alabama');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.2','Biography and History>North America>Mississippi');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.3','Biography and History>North America>Louisiana');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.302','Biography and History>North America>French period, 1718-1763');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.304','Biography and History>North America>French and territorial');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.4','Biography and History>North America>Texas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.6','Biography and History>North America>Oklahoma');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.7','Biography and History>North America>Arkansas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.8','Biography and History>North America>Tennessee');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('976.9','Biography and History>North America>Kentucky');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977','Biography and History>North America>North central United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.1','Biography and History>North America>Ohio');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.2','Biography and History>North America>Indiana');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.3','Biography and History>North America>Illinois');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.4','Biography and History>North America>Michigan');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.5','Biography and History>North America>Wisconsin');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.6','Biography and History>North America>Minnesota');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.7','Biography and History>North America>Iowa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('977.8','Biography and History>North America>Missouri');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978','Biography and History>North America>Western United States');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.1','Biography and History>North America>Kansas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.2','Biography and History>North America>Nebraska');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.3','Biography and History>North America>South Dakota');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.4','Biography and History>North America>North Dakota');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.6','Biography and History>North America>Montana');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.7','Biography and History>North America>Wyoming');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.8','Biography and History>North America>Colorado');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('978.9','Biography and History>North America>New Mexico');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979','Biography and History>North America>Great Basin & Pacific Slope region');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.1','Biography and History>North America>Arizona');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.2','Biography and History>North America>Utah');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.3','Biography and History>North America>Nevada');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.4','Biography and History>North America>California');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.5','Biography and History>North America>Oregon');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.6','Biography and History>North America>Idaho');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.7','Biography and History>North America>Washington');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.8','Biography and History>North America>Alaska');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('979.84','Biography and History>North America>Southwestern Alaska');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('980','Biography and History>South America>History of South America');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('981','Biography and History>South America>Brazil');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('982','Biography and History>South America>Argentina');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('983','Biography and History>South America>Chile');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('984','Biography and History>South America>Bolivia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('985','Biography and History>South America>Peru');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('986','Biography and History>South America>Colombia & Ecuador');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('986.1','Biography and History>South America>Colombia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('986.6','Biography and History>South America>Ecuador');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('987','Biography and History>South America>Venezuela');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('988','Biography and History>South America>Guiana');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('988.1','Biography and History>South America>Guyana');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('988.2','Biography and History>South America>French Guiana (Guyane)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('988.3','Biography and History>South America>Surinam (Suriname)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('989','Biography and History>South America>Paraguay & Uruguay');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('989.2','Biography and History>South America>Paraguay');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('989.5','Biography and History>South America>Uruguay');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('990','Biography and History>Pacific>History of other areas');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('991','Biography and History>Pacific>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('992','Biography and History>Pacific>[Unassigned]');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('993','Biography and History>Pacific>New Zealand');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('993.0049944','Biography and History>Pacific>Maori (New Zealand people)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994','Biography and History>Pacific>Australia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.1','Biography and History>Pacific>Western Australia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.2','Biography and History>Pacific>Central Australia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.23','Biography and History>Pacific>South Australia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.29','Biography and History>Pacific>Northern Territory');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.3','Biography and History>Pacific>Queensland');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.4','Biography and History>Pacific>New South Wales');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.5','Biography and History>Pacific>Victoria');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.6','Biography and History>Pacific>Tasmania');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('994.7','Biography and History>Pacific>Australian');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('995','Biography and History>Pacific>Melanesia and New Guinea');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('996','Biography and History>Pacific>Other parts of Pacific and Polynesia');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('996.13','Biography and History>Pacific>American Samoa');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('996.5','Biography and History>Pacific>Pacific Islands (Trust Territory)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('996.9','Biography and History>Pacific>Hawaii');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('997','Biography and History>Pacific>Atlantic Ocean islands');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('997.11','Biography and History>Pacific>Falkland Islands (Islas Malvinas)');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('998','Biography and History>Pacific>Arctic islands & Antarctica');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('999','Biography and History>Pacific>Extraterrestrial civilization');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('B','Non-Standard>Biography');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('FIC','Non-Standard>Fiction');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('J','Non-Standard>Juvenile');\
            INSERT OR IGNORE INTO _lc_genre_mapping VALUES('R','Non-Standard>Reference');\
            COMMIT;")


    return mysql
