from xml.dom import minidom

mydoc = minidom.parse('items.xml')
items = mydoc.getElementsByTagName('item')
for el in items:
    print(el.attributes['name'].value)
for el in items:
    print(el.firstChild.data)
