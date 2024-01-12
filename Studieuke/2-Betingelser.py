#%% 1. Skriv et program som ber brukeren om å oppgi et tall og skriver ut om tallet er positivt, negativt eller null.
chk_pos_or_neg = input("Skriv inn et positivt eller negativt tall: ")
if int(chk_pos_or_neg) >= 0:
    print("Du skrev inn et positivt tall.")
else:
    print("Du skrev inn et negativt tall.")

#%% 2. Skriv et program som ber brukeren om å oppgi et tall og skriver ut om tallet er et partall eller oddetall.
chk_odd_or_even = input("Skriv inn et heltall: ")
if int(chk_odd_or_even) % 2 == 0:
    print("Du skrev inn et partall.")
else:
    print("Du skrev inn et oddetall.")

#%% 3. Skriv et program som ber brukeren om å oppgi tre tall og skriver ut det største tallet.
tall_1 = int(input("Skriv inn tall nummer 1: "))
tall_2 = int(input("Skriv inn tall nummer 2: "))
tall_3 = int(input("Skriv inn tall nummer 3: "))
print(f"Det største tallet du skrev inn var {max(tall_1, tall_2, tall_3)}.")

#%% 4. Skriv et program som ber brukeren om å oppgi to tall og skriver ut
# om det første tallet er større enn, mindre enn eller likt det andre tallet.
num_1 = int(input("Skriv inn tall nummer 1: "))
num_2 = int(input("Skriv inn tall nummer 1: "))
if num_1 > num_2:
    print("Det første tallet er størst.")
elif num_1 < num_2:
    print("Det andre tallet er størst.")
else:
    print("Du skrev inn to like tall.")

#%% 5. Skriv et program som ber brukeren om å oppgi en karakter (A, B, C, D eller F) og
# skriver ut en tekststreng basert på karakteren (for eksempel "Utmerket" for A, "God" for B, etc.).
grade_input = input("Skriv inn karakter du ønsker å gi dette prosjektet (A-F): ").lower()
if grade_input == "a":
    print("A - Fremragende!")
elif grade_input == "b":
    print("B - Meget god")
elif grade_input == "c":
    print("C - Nokså god")
elif grade_input == "d":
    print("D - Tilstrekkelig")
elif grade_input == "f":
    print("F - Ikke bestått")
else:
    print("Du må skrive inn en bokstav mellom A og F.")
