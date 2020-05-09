import csv
from xml.etree import ElementTree

tree = ElementTree.parse('Employee.xml')
root = tree.getroot()

xml_data_to_csv = open('out.csv', 'w')

list_head=[]

csv_writer= csv.writer(xml_data_to_csv)

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

