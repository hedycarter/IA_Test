import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import random
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty("rate", 170)


def parler(text):
    engine.say(text)
    engine.runAndWait()


def greetme():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        parler("Bonjour Mr Hady")

    if 12 <= current_hour < 18:
        parler("Bonaprés midi Monsieur Fofana")

    if current_hour >= 18 and current_hour != 0:
        parler("Bonsoir Mr Hady")


# set femal voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
greetme()
engine.say("comment vas tu")
engine.runAndWait()


def ecouter():
    try:
        with sr.Microphone() as source:
            print("parlez maintenant")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            command.lower()
    except:
        pass
    return command


def lancer_assistant():
    command = ecouter()
    print(command)
    if "musique" in command:
        song = command.replace("musique", "")
        parler("musiaue en cours...")
        pywhatkit.playonyt(song)
    elif "heure" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        parler("actuellement a bamako, il est : " + time)

    elif 'et toi' in command:
        parler('je vais hyper bien merci')

    elif 'Bonjour' in command:
        parler('bonjour,ca va?')

    elif "sortir" in command:
        parler("Désolé, je suis un peu souffrante")
    elif "es-tu en couple" in command:
        parler("je suis pas interessé")

    elif "de toi" in command:
        parler("s'implement test. les partisant de la théorie des anciens astronaute vous dirons que je "
               "viens d'une civilisation trés avancée. cette alienne théorie vous dirons; que je viens dune autre "
               "système solaire "
               "mais toute ce que je peux vous dire est que j'ai été programmé par Monsieur Fofana")

    elif "âge" in command:
        parler("j'ai l'âge d'une cirquit; mais je suis immortelle")

    elif "tes points fort" in command:
        parler("je peux vous donné l'heur, la météo pour chaque jour de la semaine; je peux demaré ou arrêter n'importe quelle application,"
               "je peux aussi vous annalysé une masse des données trés volumuné et plein d'autre chose")

    elif "comment tu t'appel" in command:
        parler("je m'appel test")

    elif "merci" in command:
        parler("de rien. je vous en prie !")

    elif "Dieu existe" in command:
        parler("je ne parle pas de religion; céla provoque toujours de conflit")

    elif "Ok" in command:
        parler("trés bien")
    elif "la fin du monde" in command:
        parler("oui je le peux; mais tu ne voudrais pas le savoir")

    else:
        print('je ne comprends pas')


while True:
    lancer_assistant()
