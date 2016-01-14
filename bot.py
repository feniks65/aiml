#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiml
import xml.etree.cElementTree as ET
import urllib2
import datetime
import re

#tabela z kursami kupna i sprzedaży walut obcych
adres_tabeli_C = "http://www.nbp.pl/kursy/xml/dir.aspx?tt=C"
url_tables_dir = "http://www.nbp.pl/kursy/xml/"
tabela_C = urllib2.urlopen(adres_tabeli_C)
#w niej trzeba znaleźć xml z dzisiaj

now = datetime.datetime.now()

# zbuduj część nazwy pliku z dzisiejszymi kursami walut
part_filename = str(now.year)[-2:] + str(now.month).zfill(2) + str(now.day) + '.xml'

# poszukaj regex dalszej części pliku
matches = re.search("c[A-Za-z0-9]*" + part_filename, tabela_C.read())

# dzisiejsza strona z kursami walut
actual_exchanges = matches.group()

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
# tree = ET.ElementTree(file='exchange_rates.xml')

bot = aiml.Kernel()
bot.setBotPredicate("name", "Alex")
bot.setBotPredicate("master", "Wojtek")
#bot.learn("random_answers.xml")
#bot.learn("Religion.aiml")

"""
Potrzebuje jakiegoś xmla z najczęściej zadawanymi pytaniami i odpowiedziami po polsku i zamiast nich
muszę go załadować.
"""

bot.learn("UI.aiml")
bot.learn("Default.aiml")
bot.learn("Knowledge.aiml")
bot.learn("Salutations.aiml")
bot.learn("random_answers.xml")


while True:
    print bot.respond(raw_input(" > "))
