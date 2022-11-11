import os
import xml.dom.minidom

img_path = 'F://test/empty/img-empty/'
# xml_path = 'F://test/empty/xml-empty/'
txt_path = 'F://test/empty/txt-empty/'

txts = os.listdir(txt_path)

for img_file in os.listdir(img_path):
    if img_file.split('.')[0] not in txts:
        img_name = os.path.splitext(img_file)[0]

        # write into the xml text file
        # open(txt_path + '%s.txt' % img_name, 'w').close()
        fp = open(txt_path + '%s.txt' % img_name, 'w+')
        fp.close()
