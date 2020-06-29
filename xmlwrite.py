import xml.etree.ElementTree as ET

data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'items1')
item2 = ET.SubElement(items, 'items2')
item1.set('name', 'items1')
item2.set('name', 'items2')
item1.text = 'value1'
item2.text = 'value2'
strdata = ET.tostring(data)
myfile = open('ma.xml', 'w')
myfile.write(strdata.decode())
myfile.close()
