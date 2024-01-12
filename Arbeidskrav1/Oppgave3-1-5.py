# Oppgave 1
print("Oppgave 1: Fem valgfrie dyr")
dyr_liste = ["Hund", "Katt", "Hest", "Ku", "Løve"]

for i in range(5):
    print(dyr_liste[i], end=" ")

# Oppgave 2
print("\n\nOppgave 2: Gi dyrene navn")
dyr_liste_med_navn = ["Bruno", "Pusur", "Frøya", "Dagros", "Simba"]

for n in range(5):
    print(f"{dyr_liste_med_navn[n]} er en {dyr_liste[n]}.")

# Oppgave 3
print("\nOppgave 3: Skriv ut første og siste dyr på listen")
print(f"Første dyr på listen er {dyr_liste[0]} og det siste på listen er {dyr_liste[-1]}.")

# Oppgave 4
dyr_liste_reversed = sorted(dyr_liste, reverse=True)
print(f"\nOppgave 4: Listen med dyr reversert alfabetisk er: ")
for x in range(5):
    print(dyr_liste_reversed[x], end=" - ")

# Oppgave 5
print("\n\nOppgave 5: Lag samme listen med dyr og navn, i datatypen Dictionary")
dyr_liste_dict = {"Hund": "Bruno", "Katt": "Pusur", "Hest": "Frøya", "Ku": "Dagros", "Løve": "Simba"}

for dyr, navn in dyr_liste_dict.items():
    print(f"{navn} er en {dyr}.")
