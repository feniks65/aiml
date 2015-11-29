#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiml
import xml.etree.cElementTree as ET
import urllib2

#sciagnij plik z serwera z nbpu do pliku
exchange_rates_site = urllib2.urlopen("http://www.nbp.pl/kursy/xml/c231z151127.xml")
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
bot.learn("UI.aiml")
bot.learn("Default.aiml")
bot.learn("Knowledge.aiml")
bot.learn("Salutations.aiml")
bot.learn("random_answers.xml")


while True:
    print bot.respond(raw_input(" > "))
