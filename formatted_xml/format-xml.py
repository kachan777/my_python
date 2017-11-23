from xml.dom import minidom
 
xdoc = minidom.parse('before.xml')
 
elements = xdoc.getElementsByTagName('Item')
node = xdoc.getElementsByTagName('ElementName')
print(node.childNodes.data)
