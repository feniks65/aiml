#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiml
import xml.etree.ElementTree as ElementTree
import urllib2
import datetime
import re

def getSiteWithExchangeRates( adres_tabC ):
	date_now = datetime.datetime.now()
	daydelta = datetime.timedelta(days=1)

	part_filename = str(date_now.year)[-2:] + str(date_now.month).zfill(2) + str(date_now.day) + '.xml'
	tabela_C = urllib2.urlopen(adres_tabC)
	if None == tabela_C:
		print "Nie mogę pobrać strony z tabelą C"
		return None
	else:
		matches = re.search("c[A-Za-z0-9]*" + part_filename, tabela_C.read())
		while None == matches:
			part_filename = str(date_now.year)[-2:] + str(date_now.month).zfill(2) + str((date_now-daydelta).day) + '.xml'
			matches = re.search("c[A-Za-z0-9]*" + part_filename, tabela_C.read())
	return matches.group()	


def transformNbpXmlToAiml( file_path )
	"""Funkcja zwróci ścieżkę do xmla z odpowiednimi zwrotami do załadowanie do parsera aiml"""
	
	#załaduj plik dane z xml'a
	tree = ElementTree.parse('exchange_rates.xml')
	root = tree.getroot()

	for child in root:
		print child.tag, child.attrib
	

#tabela z kursami kupna i sprzedaży walut obcych
adres_tabeli_C = "http://www.nbp.pl/kursy/xml/dir.aspx?tt=C"
url_tables_dir = "http://www.nbp.pl/kursy/xml/"

# dzisiejsza strona z kursami walut
actual_exchanges = getSiteWithExchangeRates(adres_tabeli_C) 

#sciagnij plik z serwera z nbpu do pliku
# pobierz aktualną datę, przeszukaj stronę
# http://www.nbp.pl/kursy/xml/dir.aspx?tt=C
# pod kątem tego pliku z aktualną datą
# pobierz ten plik

exchange_rates_site = urllib2.urlopen(url_tables_dir + actual_exchanges)
exchange_rates_fd = open('exchange_rates.xml','wb')
exchange_rates_fd.write(exchange_rates_site.read())
exchange_rates_fd.close()

#załaduj plik dane z xml'a
tree = ElementTree.parse('exchange_rates.xml')
root = tree.getroot()

for child in root:
	print child.tag, child.attrib

bot = aiml.Kernel()
bot.setBotPredicate("name", "Alex")
bot.setBotPredicate("master", "Wojtek")
#bot.learn("random_answers.xml")
#bot.learn("Religion.aiml")

"""
Potrzebuje jakiegoś xmla z najczęściej zadawanymi pytaniami i odpowiedziami po polsku i zamiast nich
muszę go załadować.
"""

#bot.learn("UI.aiml")
bot.learn("Default.aiml")
bot.learn("Knowledge.aiml")
bot.learn("Salutations.aiml")
bot.learn("random_answers.xml")


while True:
    print bot.respond(raw_input(" > "))
