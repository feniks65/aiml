#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('exchange_rates.xml')
root = tree.getroot()



for child in root:
	print child.tag, " ", child.text
	for child2 in child:
		print "    ", child2.tag, " ", child2.text
		#for child3 in child2:
		#	print "        ", child3.tag, " ", child3.attrib



aiml = ET.Element("aiml")
category = ET.SubElement(aiml, "category")

ET.SubElement(doc, "field1").text = "some value1"
ET.SubElement(doc, "field2").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")
