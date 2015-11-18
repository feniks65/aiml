import aiml
import xml
mybot = aiml.Kernel()
mybot.learn('speak.xml')
mybot.respond("what is your name")
