import time
import keyboard #trouver la solution pour que la pause soit une vraie pause du programme

def afficher_heure():
    heures, minutes, secondes = map(int, time.strftime("%H:%M:%S").split(':'))
    while True:
        try:
            ask_heure = input("Voulez vous changer l'heure (y/n) ? ")
            if ask_heure.lower() == 'y':
                nouvelle_heure = input("Entrez une heure au format HH:MM:SS : ")
                heures, minutes, secondes = map(int, nouvelle_heure.split(':'))
                if heures < 0 or heures > 23:
                    print("Erreur : les heures doivent être comprises entre 00 et 23 heures.")
                elif minutes < 0 or minutes > 59 or secondes < 0 or secondes > 59:
                    print("Erreur :les minutes et secondes doivent être comprises entre 00 et 59.")
                else:
                    break
            elif ask_heure.lower() == 'n':
                break
            else:
                print("Erreur : veuillez entrer une réponse valide : (y/n).")
        except ValueError:
            print("Erreur : veuillez entrer une heure au format HH:MM:SS.")
    return heures, minutes, secondes

def reveil():
    heure_alarme, minute_alarme, seconde_alarme = map(int, time.strftime("%H:%M:%S").split(':'))
    while True:
        try:
            alarme = input("Voulez-vous régler une alarme (y/n) ? ")
            if alarme.lower() == 'y':
                nouvelle_alarme = input("Entrez une heure au format HH:MM:SS : ")
                heure_alarme, minute_alarme, seconde_alarme = map(int, nouvelle_alarme.split(':'))
                if heure_alarme < 0 or heure_alarme > 23:
                    print("Erreur : les heures doivent être comprises entre 00 et 23 heures.")
                elif minute_alarme < 0 or minute_alarme > 59 or seconde_alarme < 0 or seconde_alarme > 59:
                    print("Erreur :les minutes et secondes doivent être comprises entre 00 et 59.")
                else:
                    break
            elif alarme.lower() == 'n':
                break
            else:
                print("Erreur : veuillez entrer une réponse valide : (y/n).")
        except ValueError:
            print("Erreur : veuillez entrer une heure au format HH:MM:SS.")
    return heure_alarme, minute_alarme, seconde_alarme

def afficher_heure_format():
    while True:
        mode = input("Choisissez un mode d'affichage : 1 (hh:mm:ss) ou 2 (hh:mm:ss AM/PM) : ")
        if mode in ['1', '2']:
            return mode
        else:
            print("Erreur : veuillez entrer un mode d'affichage valide : 1 ou 2.")

def horloge(heures, minutes, secondes, heure_alarme, minute_alarme, seconde_alarme, mode):
    while True:
        #if keyboard.is_pressed('space'):
            #print("Programme en pause. Appuyez sur une touche pour continuer...")
            #keyboard.read_key()
        if mode == '1':
            print(f"{heures:02}:{minutes:02}:{secondes:02}")
        elif mode == '2':
            if heures < 13:
                print(f"{heures:02}:{minutes:02}:{secondes:02} AM")
            else:
                print(f"{heures-12:02}:{minutes:02}:{secondes:02} PM")
        time.sleep(1)
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
        if heures == 24:
            heures = 0
        if (heures, minutes, secondes) == (heure_alarme, minute_alarme, seconde_alarme):
            print("C'est l'heure de votre alarme !\n"*3)

mode = afficher_heure_format()
heures, minutes, secondes = afficher_heure()
heure_alarme, minute_alarme, seconde_alarme = reveil()
horloge(heures, minutes, secondes, heure_alarme, minute_alarme, seconde_alarme, mode)



