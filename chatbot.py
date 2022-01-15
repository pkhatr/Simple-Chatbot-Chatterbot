'''Code to create a simple chatbot quickly'''

# Create a new bot
from chatterbot import ChatBot
bot = ChatBot(
    'Babu', 
    logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'], 
    database_uri='sqlite:///database.sqlite3'
)

# Train the bot (Recommended not required)
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer 

# Conversation list to train the bot is using ListTrainer (Commented out this portion as ChatterBotCorpusTrainer used)
# converse = ['Hello', 'Hi there!', 'How are you doing?', "I'm doing great.", 'That is good to hear', 
# 'Thank you!', "You're welcome.", 'I need your help', 'How can I help you', 'Need help with math', 
# 'Okay, tell me your problem']
# trainer = ListTrainer(bot)
# trainer.train(converse)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')



# Get a response (Response in terminal)
print('Hi My name is Babu and I am a bot! If you want to quit, please type Bye')
while True:
    try:
        utext = input('You: ')
        if utext.lower() == 'bye':
            print('Babu: Bye Bye!')
            break
        else:
            print('Babu: ', bot.get_response(utext))
    except(KeyboardInterrupt, EOFError, SystemExit): 
        break
