import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('Hello, I am Alexa.. How can I help you')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is '+time)
    elif 'tell me about' in command:
        about=command.replace('tell me about','')
        info=wikipedia.summary(about,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk('here is a joke')
        talk(pyjokes.get_joke())
    elif 'one more' in command:
        talk('here is another one')
        talk(pyjokes.get_joke())
    else:
        talk('sorry, please repeat the command')
while True:
    run_alexa()  
