#!/usr/bin/env python

import xml.etree.ElementTree as ElementTree

tree = ElementTree.parse('exchange_rates.xml')
root = tree.getroot()

for child in root:
	print child.tag, child.attrib
	for childchild in child:
		print childchild.tag, childchild.attrib
