from xml.etree import ElementTree

def print_node(node):
    print "====================================="
    for key,value in node.items():
      print "%s:%s" % (key, value)
    for subnode in node.getchildren():
      print "%s:%s" % (subnode.tag, subnode.text)
  
def read_xml(text = '', xmlfile = ''):
    root = ElementTree.fromstring(text)
    eitor = root.getiterator("employee")
    for e in eitor:
        print_node(e)

if __name__ == '__main__':
    read_xml(open("web.xml").read())