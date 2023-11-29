import time

def horloge():
    while True:
        heure = time.strftime("%H:%M:%S")
        print(heure)
        time.sleep(1)

horloge()