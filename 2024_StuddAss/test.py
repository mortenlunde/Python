# oppgave 1

# 1.
navn = input("navn: Nasrudin")
print(f"hei, {navn}!")

# 2.
tall = 5
if tall > 0:
    print("tallet er posetivt")
elif tall < 0:
    print("tallet er negativt.")
else:
    print("tallet er null")
# 3

tall = float(input("ditt tall"))
dobbelte_tall = tall * 2
print(f"det dobbelte av {tall} er {dobbelte_tall}")

# 4
tekst = input("Dette arbeidskravet")
baklengs_tekst = tekst[::-1]
print(f"Baklengs dette arbeidskravet: {baklengs_tekst}")

# oppgave 2

# 1
import random

tilfeldige_tall = [random.randint(1, 100) for _ in range(5)]


print("liste med 5 tilfeldige heltall:", tilfeldige_tall)

# 2

import random

tilfeldige_tall = [random.randint(1, 100) for _ in range(5)]

print(f"opprinelig liste med tilfeldige heltall: {tilfeldige_tall}")

tilfeldige_tall.sort()

print(f"sortert liste i stigende rekkefølge: {tilfeldige_tall}")

# 3
import random

tilfeldige_tall = [random.randint(1, 200) for _ in range(100)]

print("liste med 100 tilfeldige heltall mellom 1 og 200")
print(tilfeldige_tall)

# 4
import random

tilfeldige_tall = [random.randint(1, 200) for _ in range(100)]

print("opprinnelig liste med 100 tilfeldige heltall mellom 1 og 200:")
print(tilfeldige_tall)

print(tilfeldige_tall)
filfeldige_tall = [tall for tall in tilfeldige_tall if tall <= 100]

print("Liste med tall som er mindre enn eller lik 100: ")
print(tilfeldige_tall)
# 5
import random

tilfeldige_tall = [random.randint(1, 200) for _ in range(100)]

print("opprinnelig liste med 100 tilfeldige heltall mellom 1 og 200.")
print(tilfeldige_tall)

filtrerte_tall = [tall for tall in tilfeldige_tall if tall <= 100 and tall % 3 != 0]
print("liste med tall som er mindre enn eller lik 100, ot ikke deleling med 3: ")
print(filtrerte_tall)

# Oppgave 3

# 1
dyr = ["hund", "katt", "elefant", "løve", "fugl"]
for dyr_i_liste in dyr:
    print(dyr_i_liste)
# 2
dyr = ["hund", "katt", "elefant", "løve", "fugl"]
navn = ["tom", "jens", "thomas", "ole", "kari"]
for i in range(len(dyr)):
    print(f"{navn[i]} er en {dyr[i]}")

# 3
dyr = ["hund", "katt", "elefant", "løve", "fugl"]
print(f"første dyr : {dyr[0]}")
print(f"siste dyr :{dyr[-1]}")
# 4
dyr = ["hund", "katt", "elefant", "løve", "fugl", ]
dyr_reversert = sorted(dyr, reverse=True)
print("liste med dyr i reversert alfabetisk rekkefølge:")
print(dyr_reversert)

# 5
navn = ["tom", "jens", "thomas", "ole", "kari"]
dyr = ["hund", "katt", "elefant", "løve", "fugl"]
dyrenavn_dict = {navn[i]: dyr[i] for i in range(len(navn))}
for navn, dyretype in dyrenavn_dict.items():
    print(f"{navn} er en {dyretype}")


# Oppgave 4

def vis_meny():
    print("\nVelkommen til Kalkulatoren!")
    print("1. Addisjon (Pluss)")
    print("2. Subtraksjon (Minus)")
    print("3. Multiplikasjon")
    print("4. Divisjon")
    print("5. Avslutt")


def addisjon():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    print(f"Summen av {tall1} og {tall2} er {tall1 + tall2}")


def subtraksjon():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    print(f"Differansen mellom {tall1} og {tall2} er {tall1 - tall2}")


def multiplikasjon():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    print(f"Produktet av {tall1} og {tall2} er {tall1 * tall2}")


def divisjon():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    if tall2 == 0:
        print("Feil: Du kan ikke dele på null!")
    else:
        print(f"Kvotienten av {tall1} delt på {tall2} er {tall1 / tall2}")


while True:
    vis_meny()
    valg = input("Gjør et valg (1-5): ")

    if valg == '1':
        addisjon()
    elif valg == '2':
        subtraksjon()
    elif valg == '3':
        multiplikasjon()
    elif valg == '4':
        divisjon()
    elif valg == '5':
        print("Avslutter programmet...")
        break
    else:
        print("svaret er ugyldig.")