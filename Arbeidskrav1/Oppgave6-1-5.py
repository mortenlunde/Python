# Oppgave 6


def sjekkinput(brukerinput):
    while True:
        try:
            godkjent_input = float(input(brukerinput))
            if godkjent_input % 1 == 0:
                return int(godkjent_input)
            else:
                return godkjent_input
        except ValueError:
            print("Dette er ikke et gyldig tall, prøv igjen.")


def addisjon():
    return tall1_input + tall2_input


def subtraksjon():
    return tall1_input - tall2_input


def multiplikasjon():
    return tall1_input * tall2_input


def divisjon():
    return tall1_input / tall2_input


def avslutt():
    return exit()


print("Velkommen til min enkle kalkulator. Velg en av følgende funksjoner ved å skrive inn tallet:\n"
      "1 - Addisjon, 2 - Subtraksjon, 3 - multiplikasjon, 4 - divisjon, 5 - avslutt programmet")

menyvalg = input("Skriv inn ditt menyvalg: ")

while menyvalg != "5":
    if menyvalg == "1":
        tall1_input = sjekkinput("Skriv inn første tall: ")
        tall2_input = sjekkinput("Skriv inn det andre tallet: ")
        print("Summen av dine tall er", addisjon())
    elif menyvalg == "2":
        tall1_input = sjekkinput("Skriv inn første tall: ")
        tall2_input = sjekkinput("Skriv inn det andre tallet: ")
        print("Differansen av dine tall er", subtraksjon())
    elif menyvalg == "3":
        tall1_input = sjekkinput("Skriv inn første tall: ")
        tall2_input = sjekkinput("Skriv inn det andre tallet: ")
        print("Produktet av dine tall er", multiplikasjon())
    elif menyvalg == "4":
        tall1_input = sjekkinput("Skriv inn første tall: ")
        if tall1_input == 0:
            print("Du kan ikke dele med 0. Prøv igjen")
            continue
        tall2_input = sjekkinput("Skriv inn det andre tallet: ")
        if tall2_input == 0:
            print("Du kan ikke dele med 0. Prøv igjen")
            continue
        print("Kvotienten av dine tall er", divisjon())
    elif menyvalg not in ("1", "2", "3", "4", "5"):
        print("Du må skrive et gyldig menyvalg (1-5)")
    else:
        avslutt()
    menyvalg = input("Skriv inn ditt menyvalg: ")
