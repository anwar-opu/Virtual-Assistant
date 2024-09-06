import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()

talk("as salam alaykum can i help you?")
def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=10)  # phrase time limit
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A, %B,%d, %Y')
        print(date)
        talk('Today is' + date)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command or 'allah hafiz' in command:
        talk('Khuda Hafiz')
        exit()
    else:
        talk('i did not get it but i am going to search it for you')
        pywhatkit.search(command)


while True:
    run_alexa()
