import random
import pyttsx3
import string
import pygame
import speech_recognition as sr
import wikipedia
import pywhatkit as kit
import os
import smtplib
import pyautogui
import clipboard
import requests
import pywhatkit
import psutil
import socket
import openai
import time as timer

from secrets_1 import senderEmail, senderPassword, openai_api_key
from datetime import datetime


# Chemin des applications
paths = {
    'discord': "C:\\Users\\Dell\\AppData\\Local\\Discord\\app-1.0.9011\\Discord.exe",
    'postman': "C:\\Users\\Dell\\AppData\\Local\\Postman\\Postman.exe",
    'vscode': "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}


# Parler
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


# Faire une demande
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("En écoute ...")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        print("Analyse ...")
        query = r.recognize_google(audio, language='fr-FR')
        return query
    except sr.UnknownValueError:
        speak("Je n'ai pas compris votre demande")
        return ""
    except sr.RequestError as e:
        speak("Impossible d'obtenir la réponse à votre demande ; {0}".format(e))
        return ""


# Donner l'heure
def time():
    h = datetime.now().strftime('%I:%M:%S')
    speak("Il est actuellement : "+ h)


# Donner la date
def date():
    day = str(datetime.now().day)
    month = str(datetime.now().strftime('%B'))
    year = str(datetime.now().year)
    speak("Nous sommes le : " + day + month + year)


# Saluer
def hello():
    currentHour = datetime.now().hour
    if currentHour > 6 and currentHour < 18 :
        speak("Bonjour Alexis, je suis Skynet Cyberdyne Systems en quoi puis-je être utile ?")
    else:
        speak("Bonsoir Alexis, je suis Skynet Cyberdyne Systems en quoi puis-je être utile ?")


# Ouvrir discord
def discord():
    os.startfile(paths['discord'])


# Ouvrir postman
def postman():
    os.startfile(paths['postman'])


# Ouvrir un terminal
def terminal():
    os.system('start cmd')


# Recherche sur google
def google(query):
    kit.search(query)


# Recherche sur wikipedia
def search_wikipedia(query):
    wikipedia.set_lang("fr")
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.PageError:
        speak("Je n'ai pas trouvé d'informations sur Wikipedia à propos de "+query)


# Envoyer un mail
def send_email(target, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderEmail, senderPassword)
    server.sendmail(senderEmail, target, content)
    server.close()

# NEW !!
def send_email(target, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderEmail, senderPassword)
    server.sendmail(senderEmail, target, content)
    server.close()


# Jouer de la musique
def play_music():
    album = "C:\\Users\\Dell\\Music"
    song = os.listdir(album)
    for i in range(len(song)):
        os.startfile(os.path.join(album, song[i]))


# Enregistrer un texte
def remember():
    speak("Que dois-je enregistrer ?")
    text = command()
    if text:
        speak("Vous m'avez demandé d'enregistrer : " + text)
        file = open("note.text", "w")
        file.write(text)
        file.close()


# Annoncer le texte
def remember_me():
    file = open("note.text", "r")
    speak("Vous m'avez demandé d'écrire" + file.read())


# Capture d'écran
def capture():
    image = pyautogui.screenshot()
    image.save("Images/capture.png")
    speak("J'ai fait une capture d'écran")


# Processeur et batterie
def info_computer():
    processor = str(psutil.cpu_percent())
    speak(processor + "pourcent utilisé par le processeur")
    battery = psutil.sensors_battery()
    if battery:
        value = battery.percent
        speak(f'le système est à {value} pourcent du niveau de batterie')
    else:
        speak("Je ne peux pas déterminer le niveau de batterie")


# Adresse IP
def ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    speak("Votre adresse ip est : " + ip)


# Pile ou face
def coinFlip():
    pygame.init()
    pygame.mixer.music.load("Musics/coinflip.mp3")
    answers = ["je lance la pièce", "c'est parti"]
    random.seed()
    speak(random.choice(answers))
    pygame.mixer.music.play()
    timer.sleep(2)
    coinSides = ["pile", "face"]
    random.seed()
    result = random.choice(coinSides)
    answerResult = [f"c'est {result}", f"j'ai eu {result}"]
    random.seed()
    speak(random.choice(answerResult))
    pygame.mixer.music.stop()
    pygame.quit()


# Lancer un dé
def diceRoll():
    pygame.init()
    pygame.mixer.music.load("Musics/dice.mp3")
    answers = ["Okay", "Je lance le dé"]
    random.seed()
    speak(random.choice(answers))
    pygame.mixer.music.play()
    timer.sleep(2)
    dicePoints = ["1", "2", "3", "4", "5", "6"]
    random.seed()
    result = random.choice(dicePoints)
    answerResult = [f"J'ai eu {result}", f"Le dé affiche {result}"]
    random.seed()
    speak(random.choice(answerResult))
    pygame.mixer.music.stop()
    pygame.quit()


# Faire des blagues
def jokes():
    jokesList = [
        "C'est l'histoire du p’tit dej, tu la connais ? Pas de bol.",
        "Que demande un footballeur à son coiffeur ? La coupe du monde s’il vous plait",
        "C'est l'histoire d'un pingouin qui respire par les fesses Un jour il s’assoit et il meurt",
        "Comment s'appelle le cul de la Schtroumpfette ? Le Blu-ray"
    ]
    random.seed()
    speak(random.choice(jokesList))


# Ouvrir vscode
def vscode():
    os.startfile(paths['vscode'])


# Youtube
def search_on_youtube():
    speak("Que dois-je chercher sur youtube ?")
    topic = command()
    pywhatkit.playonyt(topic)


# Dire le texte copié
def copied_text():
    text = clipboard.paste()
    speak(f"Le texte copié est : {text}")


# Créer mot de pass
def password():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass = ("".join[0:passlen])
    print(newpass)
    speak(f"Votre nouveau mot de passe est :{newpass}")


# Météo
def weather():
    speak("Dans quelle ville ?")
    city = command()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}"
    res = requests.get(url)
    data = res.json()
    weather = data['weather'] [0] ['main']
    temp = data['main']['temp']
    desp = data['weather'] [0] ['description']
    temp = round((temp - 32) * 5/9)
    print(weather, temp, desp)
    speak(f"La température est de {temp} degrés")


# Chat GPT
prompt = "conversation with chatGPT"
def chat_gpt(prompt):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Humain:", " AI:"]
    )
    data = response.choices[0].text
    speak(data)