import random as rnt

print("Velkommen til spillet ´Stein-Saks-Papir´!\nVi skal nå spille 10 runder. Man Vs Machine.")
print("Tast følgende tall for å velge: 0 = Stein, 1 = Saks og 2 = Papir.\n")

Runde = 0
seierbruker = 0
seiermaskin = 0
uavgjort = 0

while Runde < 10:
    brukerstr = input("Skriv inn ditt valg: ")
    if brukerstr in ["0", "1", "2"]:
        bruker = int(brukerstr)
        machine = rnt.randint(0, 2)

        if bruker == machine:
            print("Det ble uavgjort i denne runden.")
            uavgjort += 1
        elif (bruker == 0 and machine == 1) or (bruker == 2 and machine == 0) or (bruker == 1 and machine == 2):
            print("Du vant denne runden!")
            seierbruker += 1
        else:
            print("Maskin tar seieren i denne runden...")
            seiermaskin += 1

        ordForTall_bruker = ""
        if bruker == 0:
            ordForTall_bruker = "stein"
        elif bruker == 1:
            ordForTall_bruker = "saks"
        elif bruker == 2:
            ordForTall_bruker = "papir"

        ordForTall_machine = ""
        if machine == 0:
            ordForTall_machine = "stein"
        elif machine == 1:
            ordForTall_machine = "saks"
        elif machine == 2:
            ordForTall_machine = "papir"

        print(f"Du valgte {ordForTall_bruker}. Maskin valgte {ordForTall_machine}")
        print(f"Sammenlagt: Seier bruker: {seierbruker} - Seier maskin: {seiermaskin} - Uavgjort: {uavgjort}\n")
        Runde += 1
    else:
        print("Du må skrive inn tall 0, 1 eller 2.")

if seierbruker > seiermaskin:
    print("Gratulerer! Du vant sammenlagt.")
elif seierbruker < seiermaskin:
    print("Maskinen tar seieren sammenlagt.")
else:
    print("Ingenting kan skille deg og maskinen. Like mange seiere til hver av dere.")
print(f"Endelig resultat ble:\nSeiere til deg: {seierbruker}\nSeiere til maskin: {seiermaskin}\nUavgjorte: {uavgjort}")
input()
