import random as rnt

# Generer et tilfeldig heltall mellom 1 og 10, og vis det til brukeren.
heltall1 = rnt.randint(1, 10)
print("Her er et tilfeldig heltall: ", heltall1)

# Generer et tilfeldig flyttall mellom 0 og 1, og multipliser det med 100. Vis resultatet.
desimaltall1 = rnt.uniform(0, 1)
desimaltall2 = desimaltall1 * 100
print("Her er et tilfeldig desimaltall multiplisert med 100: ", round(desimaltall2, 2))

# Generer et tilfeldig heltall mellom 5 og 15. Spør brukeren om å gjette tallet.
gjetteTall = rnt.randint(5, 15)
brukergjettetall = int(input("Gjett et tilfeldig tall mellom 5 og 15: "))
if gjetteTall == brukergjettetall:
    print("Du gjettet riktig!")
else:
    print(f"Du gjettet feil. Riktig tall var {gjetteTall}")

# Generer to tilfeldige heltall og spør brukeren om å finne summen av dem.
# Programmet må også gi tilbakemelding om svaret er riktig eller galt.
heltall2 = rnt.randint(1, 100)
heltall3 = rnt.randint(1, 100)

print(f"Du fikk tallene {heltall2} og {heltall3}. Multipliser disse. Hva får du da? ")
heltall4 = int(input())
if heltall2 * heltall3 == heltall4:
    print(f"Dette er korrekt. {heltall2} x {heltall3} = {heltall2 * heltall3}.")
else:
    print(f"Dette er dessverre feil. {heltall2} x {heltall3} = {heltall2 * heltall3}")

# Generer et tilfeldig heltall mellom 1 og 2. La 1 representere True og 2 representere False.
heltall5 = rnt.randint(1, 2)
heltallBool = True
if heltall5 == 1:
    heltallBool = True
elif heltall5 == 2:
    heltallBool = False
print(f"Du fikk et tilfeldig tall som var {heltall5} og dette ga oss verdien {heltallBool}.")

# Generer tre tilfeldige heltall. Vis brukeren det største og det minste tallet.
heltall6 = rnt.randint(1, 100)
heltall7 = rnt.randint(1, 100)
heltall8 = rnt.randint(1, 100)
minstetall = min(heltall6, heltall7, heltall8)
storstetall = max(heltall6, heltall7, heltall8)

print(f"Du fikk tallene {heltall6} - {heltall7} - {heltall8}")

print(f"Det største og minste tallet her er: {minstetall} og {storstetall}")

# Generer et tilfeldig heltall. Doble det og vis begge tallene til brukeren.
heltall9 = rnt.randint(1, 100)
print(f"Du fikk tallet {heltall9} og det dobbelte av dette er {heltall9 * 2}")

# Generer et tilfeldig flyttall mellom 10 og 20, og rund det av til nærmeste heltall. Vis begge.
floattall1 = rnt.uniform(10.0, 20.0)
print(f"Du fikk et tilfeldig desimaltall {(round(floattall1, 2))} og nærmeste hele tall for dette er {(round(floattall1))}.")

# Generer et tilfeldig heltall mellom 1 og 100. Del det med 2 og vis begge tallene til brukeren.
heltall10 = rnt.randint(1, 100)
print(f"Du fikk tallet {heltall10}. Dette tallet dividert med 2 er {heltall10 / 2}")

# Generer et tilfeldig heltall mellom 50 og 100. Trekk fra 25 og vis begge tallene til brukeren.
heltall11 = rnt.randint(50, 100)
print(f"Du fikk tallet {heltall11} og dette subtrahert med 25 er {heltall11 - 25}.")
