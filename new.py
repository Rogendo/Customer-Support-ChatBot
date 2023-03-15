
# importing basic libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import logging
import speech_recognition as sr

logging.basicConfig(level=logging.INFO)

# new instance of chatbot
chatbot = ChatBot(
    'customer support',
    # database used is sql
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapter=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(chatbot)

# train the bot with some responses
trainer.train([
    'How can I help you?',
    'Hello',
    'How are you?',
    'i am well',
    'Great, lets dive in',
    'what support is offered?',
    'I can help you by giving you a list of the services we offer here at Hubybibi which include Therapy sessions and marriage councelling.',
    'I need an appointment.',
    'I can help you book an appointment. Are you going for therapy sessions or marriage councel?',
    'Therapy sessions ',
    'give me your name and email adress',
    'peter snowman, peter@gmail.com',
    'Your appointment is underway, you will receive an email.'
])



while True:
    try:
        r = sr.Recognizer()
        mic = sr.Microphone()
        print("Speak here")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            heard_audio = r.recognize_google(audio)
            print("You said: " + heard_audio)

        bot_response = chatbot.get_response(heard_audio)
        print(bot_response)

    # ctr + c will interrupt the running bot
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
