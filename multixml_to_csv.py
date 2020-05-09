import xml.etree.ElementTree as ET
import csv
import os 

def make_csv(folderpath, xmlfilename):
    tree = ET.parse(os.path.join(folderpath, xmlfilename))
    root = tree.getroot()
    filename, _ = xmlfilename.rsplit('.', 1)
    xml_data_to_csv = open(filename+'.csv', 'w', newline='')
    csv_writer = csv.writer(xml_data_to_csv)
    list_head = []

    count = 0
    for element in root.findall('Employee'):
        list_nodes=[]

        if count == 0:
            name = element.find('name').tag
            list_head.append(name)

            address = element.find('address').tag
            list_head.append(address)

            dept = element.find('dept').tag
            list_head.append(dept)
            csv_writer.writerow(list_head)
            count += 1

        name = element.find('name').text
        list_nodes.append(name)

        address = element.find('address').text
        list_nodes.append(address)

        dept = element.find('dept').text
        list_nodes.append(dept)

        csv_writer.writerow(list_nodes)

    xml_data_to_csv.close()

path = 'D:\python-example'
for filename in os.listdir(path):
    if filename.endswith('.xml'):
        make_csv(path, filename)