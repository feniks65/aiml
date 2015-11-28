import aiml

# Create the kernel and learn AIML files
bot = aiml.Kernel()
#kernel.learn("speak.xml")
#kernel.learn("random_answers.xml")A
bot.learn("Religion.aiml")
#kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input(" > "))
