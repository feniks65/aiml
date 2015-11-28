import aiml

bot = aiml.Kernel()
bot.setBotPredicate("name", "Alex")
bot.setBotPredicate("master", "Wojtek")
bot.learn("speak.xml")
bot.learn("random_answers.xml")
bot.learn("Religion.aiml")


while True:
    print bot.respond(raw_input(" > "))
