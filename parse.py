#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tree = ET.parse('exchange_rates.xml')
root = tree.getroot()

aiml = ET.Element("aiml")


for pozycja in root.findall('pozycja'):
    nazwa_waluty = pozycja.find('nazwa_waluty').text
    kurs_kupna = pozycja.find('kurs_kupna').text
    kurs_sprzedazy = pozycja.find('kurs_sprzedazy').text
    category = ET.SubElement(aiml, "category")
    nazw_wal = nazwa_waluty.decode('utf8')
    ET.SubElement(category, "pattern").text = " * " + nazw_wal.strip().upper()
    ET.SubElement(category, "template").text = "kurs kupna " + kurs_kupna + " ; kurs sprzedaży " + kurs_sprzedazy 

tree2 = ET.ElementTree(aiml)
tree2.write("kursy_walut.aiml")

"""
for child in root:
	print child.tag, " ", child.text
	for child2 in child:
		print "    ", child2.tag, " ", child2.text
		#for child3 in child2:
		#	print "        ", child3.tag, " ", child3.attrib
"""

"""
aiml = ET.Element("aiml")
category = ET.SubElement(aiml, "category")

ET.SubElement(category, "pattern").text = " * KURS DOLARA"
ET.SubElement(category, "template").text = "kurs dolara 4.05"

tree2 = ET.ElementTree(aiml)
tree2.write("kursy_walut.aiml")
"""
