# Terningspill av Morten Lunde

import random as rnd
points = 0


def kastterning():
    return rnd.randrange(1, 7)


def kasttoterninger():
    terning_1 = rnd.randrange(1, 7)
    terning_2 = rnd.randrange(1, 7)
    return terning_1, terning_2


print("Velkommen til mitt terningspill!")
terningvalg = input("Vil du bruke 1 eller 2 terninger? ")

while terningvalg not in ["1", "2"]:
    print("Du må velge 1 eller 2")
    terningvalg = input("Vil du bruke 1 eller 2 terninger? ")

print("For input velg: 1 - ja 2 - Nei")

while True:
    vil_kaste = input("Vil du kaste terning? ")
    if terningvalg == "1":
        if vil_kaste in ["1", "2"]:
            if vil_kaste == "1":
                terningkast = kastterning()
                points += terningkast
                print(f"Du kastet {terningkast} og du har nå {points} poeng samlet.")
                if points > 100:
                    print("Du har nå over 100 poeng og ingen mulighet for å vinne.")
                    break
            else:
                break
        else:
            print("Du må velge 1 eller 2")

    elif terningvalg == "2":
        if vil_kaste in ["1", "2"]:
            terning_1, terning_2 = kasttoterninger()
            if terning_1 == terning_2:
                points += (terning_1 + terning_2) * 2
                print(f"Du kastet 2 terninger og fikk {terning_1} og {terning_2} og du har nå {points} poeng samlet.")
            else:
                points += terning_1 + terning_2
                print(f"Du kastet 2 terninger og fikk {terning_1} og {terning_2} og du har nå {points} poeng samlet.")
            if points > 100:
                print("Du har nå over 100 poeng og ingen mulighet for å vinne.")
                break
        else:
            print("Du må velge 1 eller 2")

if points == 50:
    print("Du fikk 50 poeng.")
elif points == 100:
    print("Du fikk 100 poeng")
else:
    print(f"Du fikk {points} poeng og det er hverken 50 eller 100 poeng.")
