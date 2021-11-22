import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("parlez maintenant...")
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language='fr-FR')
            command.lower()
    except:
        pass
    return command



def lancer_Test():
    command=ecouter()
    print(command)
    if 'Test! je veux que tu mets la chanson de' in command:
        chanteur=command.replace('mets la chanson de','')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'Tu peux me donner l\'heure s\'il vous plait?' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)
    elif 'Bonjour Test!' in command:
        parler('bonjour,ça va?')

    elif 'ça va bien merci !' in command:
        parler('là c\'est super alors.')
    
    elif 'je veux te connaître d\'avantage si possible' in command:
        parler('que tu savoir sur moi Monsieur?')
    elif 'tout!' in command:
        parler('ok, je m\'appel Test je suis une assistante virtuel de Monsieur Fofana. je suis doté des algorithme qui me permet de faire plein des choses')
    
    elif 'ah bon? comme quoi par exemple?' in command:
        parler('de jouer la music via youtube')
    else:

        
        print('je ne comprends pas, pouvez vous reprendre s\'il vous plaît?')


while True:
    lancer_Test()