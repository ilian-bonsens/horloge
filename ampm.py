import time

def mode():
    heures, minutes, secondes = map(int, time.strftime("%H:%M:%S").split(':'))
    while True:
        try: 
            ask_heure = input("Choisissez un mode d'affichage : 1 (hh:mm:ss) ou 2 (hh:mm:ss AM/PM) : ")
            if ask_heure == '1':
                print(f"{heures:02}:{minutes:02}:{secondes:02}")
                break
            if ask_heure == '2':
                print(f"{heures:02}:{minutes:02}:{secondes:02}")
                break
        except ValueError:
            print()

mode()