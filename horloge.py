import time

def afficher_heure():
    while True:
        try:
            ask_heure = input("Voulez vous changer l'heure (y/n) ? ")
            if ask_heure.lower() == 'y':
                nouvelle_heure = input("Entrez une heure au format HH:MM:SS : ")
                elements_heure = nouvelle_heure.split(':')
                heures = int(elements_heure[0])
                minutes = int(elements_heure[1])
                secondes = int(elements_heure[2])
                if heures < 0 or heures > 23:
                    print("Erreur : les heures doivent être comprises entre 00 et 23 heures.")
                elif minutes < 0 or minutes > 59 or secondes < 0 or secondes > 59:
                    print("Erreur :les minutes et secondes doivent être comprises entre 00 et 59.")
                else:
                    break
            elif ask_heure.lower() == 'n':
                heures = int(time.strftime("%H"))
                minutes = int(time.strftime("%M"))
                secondes = int(time.strftime("%S"))
                break
            else:
                print("Erreur : veuillez entrer une réponse valide : (y/n).")
        except ValueError:
            print("Erreur : veuillez entrer une heure au format HH:MM:SS.")
    return heures, minutes, secondes

def horloge(heures, minutes, secondes):
    while True:
        print(f"{heures:02}:{minutes:02}:{secondes:02}")
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

heures, minutes, secondes = afficher_heure()
horloge(heures, minutes, secondes)


