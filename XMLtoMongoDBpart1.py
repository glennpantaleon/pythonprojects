#Glenn Pantaleon
#IBM Project
#XML Law Documents to Mongo DB part 1(Parse XML Documents both US Law and State Laws)
#Type out a python application to parse a XML Law Documents to Mongo DB
#06/26/15

import os
from xml.dom import minidom , Node

class XMLReader:

    def __init__(self,dir,filename):
        'Sets up the file path'
        self.dir        = dir
        self.filename   = filename
        self.path       = os.path.join(self.dir,self.filename)
        self.uscDoc     = minidom.parse(self.path)


    def extract_uscDoc_main(self):
        'Extracts uscDoc and main from the xml'
        uscDoc = self.uscDoc.getElementsByTagName('uscDoc')[0]
        main = uscDoc.getElementsByTagName('main')[0]
        return main

    def extract_xmltitle_number(self):

        'Extracts title number in uscDoc'
        main = self.extract_uscDoc_main()
        titles_num = main.getElementsByTagName('num')
        for title_num in titles_num:
            title_val_num = title_num.firstChild.data
            return title_val_num


    def extract_xmltitle_name(self):
        'Extracts title value head aka the title name in uscDoc'
        main = self.extract_uscDoc_main()
        titles_head= main.getElementsByTagName('heading')
        for title_head in titles_head:
            tile_valhead = title_head.firstChild.data
            return tile_valhead




    def get_law_text_data(self,nodelist):
        'Designed to obtain the text data from xml file, this funtion is used in the "handle" funtions below'
        xml_text_data = []
        for text_node in nodelist:
            if text_node.nodeType == text_node.TEXT_NODE:
                xml_text_data.append(text_node.data)
            return xml_text_data


    def extract_xmlcontent1(self,title):
        'Extracts text data from the title node of xml file'
        main = self.extract_uscDoc_main()
        xml_note_nodes = main.getElementsByTagName(title)
        i=0

        for xml_note_node in xml_note_nodes:
            xml_p_node = xml_note_node.getElementsByTagName('p')[i]
            xml_ref_node = xml_note_node.getElementsByTagName('ref')[i]

            self.handle_p_text(xml_p_node)
            self.handle_ref_text(xml_ref_node)
            i += 1

    def extract_xmlcontent2(self,notes):
        'Extracts text data from the notes node of xml file'
        main = self.extract_uscDoc_main()
        xml_note_nodes = main.getElementsByTagName(notes)
        i = 0

        for xml_note_node in xml_note_nodes:
            xml_p_node = xml_note_node.getElementsByTagName('p')[i]
            #xml_ref_node = xml_note_node.getElementsByTagName('ref')[0]

            self.handle_p_text(xml_p_node)
            #self.handle_ref_text(xml_ref_nodes)

    def extract_xmlcontent3(self,section):
        'Extracts text data from the section node of xml file'
        main = self.extract_uscDoc_main()
        xml_note_nodes = main.getElementsByTagName(section)
        i = 0


        'Code below shows all the nodes under the "note tag", need to find out how to get all nodes'
        for xml_note_node in xml_note_nodes:
            xml_p_node = xml_note_node.getElementsByTagName('p')[0]
            xml_ref_node = xml_note_node.getElementsByTagName('ref')[0]
            #xml_col_contents = xml_note_content.getElementsByTagName('column')
            #xml_head_contents = xml_note_content.getElementsByTagName('heading')[0]
            'LEARN HOW TO GET THE TEXT OF EACH CONTENT NODE'

            self.handle_p_text(xml_p_node)
            self.handle_ref_text(xml_ref_node)
            #self.handle_col_text(xml_col_contents)
            #self.handle_head_text(xml_note_contents)
            #print (xml_p_contents,xml_ref_contents,xml_col_contents,xml_head_contents)
            i += 1


    def handle_p_text(self,xml_p):
        print('%s' % self.get_law_text_data(xml_p.childNodes))

    def handle_ref_text(self,xml_ref):
        print ('%s' % self.get_law_text_data(xml_ref.childNodes))


    def handle_col_text(self,xml_col):
        print ('%s' % self.get_law_text_data(xml_col.childNodes))


    def handle_head_text(self,xml_heading):
        print ('%s' % self.get_law_text_data(xml_heading.childNodes))


    '''Code below Works, but only gets first line ergo first child node
        for xml_node in xml_note_contents:
            xmlnote_p_node = self.getChildByNote(xml_node)
            for xmlnote_node in xmlnote_p_node:
                note_list = xmlnote_node.childNodes[0].data
                xml_fullcontent.append(note_list)
            return xml_fullcontent
    '''





xml = XMLReader('law_data1','usc01.xml')
print (xml.extract_xmltitle_number())
print (xml.extract_xmltitle_name())
print (xml.extract_xmlcontent1('title'))
print (xml.extract_xmlcontent2('notes'))
print (xml.extract_xmlcontent3('section'))










