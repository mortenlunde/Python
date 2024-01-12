print("Oppgave 1: Skriv et program som leser inn et navn og skriver ut en hilsen til brukeren.Eks «Hei, Ola».")
navn_input = input("Skriv inn ditt navn: ")
print(f"Hei {navn_input}! Velkommen til en hyggelig lesning av mitt første Arbeidskrav.")

print("\nOppgave 2: Skriv et program som leser inn et tall og skriver ut om tallet er positivt, negativt eller null.")
tall_input = input("Skriv inn et vilkårlig heltall: ")
if int(tall_input) == 0:
    print("Du skrev inn tallet 0.")
elif int(tall_input) < 0:
    print("Du skrev inn et negativt tall.")
elif int(tall_input) > 0:
    print("Du skrev inn et positvt tall.")

print("\nOppgave 3: Skriv et program som leser inn et tall og skriver ut det dobbelte.")
tall_input = input("Skriv inn et heltall eller desimaltall: ")
print(f"Du skrev inn tallet {tall_input}, og det dobbelte av dette er {float(tall_input)*2}.")

print("\nOppgave 4: Skriv et program som leser inn en tekst og skriver ut teksten baklengs.")
tekst_input = input("Skriv inn en valgfri tekst som vi vil skrive ut baklengs for deg: ")
print(tekst_input[::-1])
