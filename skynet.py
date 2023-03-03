from tkinter import *
from PIL import Image, ImageTk
from locale import LC_TIME, setlocale
from threading import Thread
import webbrowser as wb
import os
from functions import speak, hello, command, time, date, discord, postman, terminal, google, search_wikipedia, send_email, play_music, remember, remember_me, capture, info_computer, ip, coinFlip, diceRoll, jokes, chat_gpt

# Langue
setlocale(LC_TIME, "fr_FR")

# Fonction pour arrêter le robot
def stop_robot():
    speak("Merci d'avoir utilisé l'assistant vocal")
    root.destroy()

# Analyse du robot
def run_robot():
    hello()
    while True:
        query = command().lower()

        if "heure" in query:
            time()

        elif "date" in query:
            date()

        elif "discord" in query:
            discord()

        elif "postman" in query:
            postman()

        elif "terminal" in query:
            terminal()

        elif "google" in query:
            speak('Que souhaitez-vous rechercher sur google ?')
            query = command().lower()
            google(query)

        elif "wikipédia" in query:
            speak('Que souhaitez-vous rechercher sur wikipédia ?')
            query = command().lower()
            search_wikipedia(query)
            results = search_wikipedia(query)
            speak(f"d'après wikipédia, {results}")

        elif "email" in query:
            try:
                speak("À qui souhaitez-vous envoyer un email ?")
                target = command()
                speak("Que souhaitez-vous écrire ?")
                content = command()
                send_email(target, content)
                speak("L'email a été envoyé avec succé")
            except Exception as e:
                print(e)
                speak("Erreur dans l'envoi de l'email")

        elif "internet" in query:
            speak("Quelle est l'adresse du site internet ?")
            link = command()
            path = "C:/Program Files/Firefox Developer Edition/firefox.exe %s"
            wb.get(path).open_new_tab(link)

        elif "déconnecter" in query:
            os.system("shutdown -l")
        elif "arrêter ordinateur" in query:
            os.system("shutdown /s/t 1")
        elif "redémarrer ordinateur" in query:
            os.system("shutdown /r/t 1")
        
        elif "musique" in query:
            play_music()

        elif "noter" in query:
            remember()

        elif "lire" in query:
            remember_me()

        elif "capture" in query:
            capture()

        elif "système" in query:
            info_computer()

        elif "ip" in query:
            ip()

        elif "pièce" in query:
            coinFlip()

        elif "dé" in query:
            diceRoll()

        elif "blague" in query:
            jokes()
            
        elif any(word in query for word in ["fermer", "quitter", "éteindre"]):
            stop_robot()

        else:
            speak("Je n'ai pas compris votre demande.")
            # chat_gpt(query)


# Démarrer le thread pour le robot
robot_thread = Thread(target=run_robot)
robot_thread.start()

# Interface utilisateur
root = Tk()
root.geometry("400x400")
root.title("Skynet")

# Charger l'image du visage de robot
image = Image.open("Images/robot-face.png")
robot_face = ImageTk.PhotoImage(image)
canvas = Canvas(root, width=400, height=400)
canvas.pack()
robot = canvas.create_image(200, 200, image=robot_face)
direction = 1
speed = 2

def animate_robot():
    global direction, speed
    canvas.move(robot, speed * direction, 0)
    x1, y1, x2, y2 = canvas.bbox(robot)
    if x2 > canvas.winfo_width() or x1 < 0:
        direction *= -1
    root.after(50, animate_robot)

animate_robot()

root.mainloop()