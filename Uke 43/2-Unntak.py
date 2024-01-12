#%% Lese input
try:
    str_num = input("Skriv inn et tall: ")
    num = int(str_num)
    print(f"Det dobbelte av tallet ditt er: {num*2}")
except ValueError as valErr:
    print(f"Du skrev ikke et gyldig tall. {valErr}")

#%% Lese inn to tall og dividere
try:
    tall_1 = input("Skriv inn et tall: ")
    tall_2 = input("Skriv inn et tall: ")
    tall_1_int = int(tall_1)
    tall_2_int = int(tall_2)
    print(f"Tallene delt på hverandre er {tall_1_int/tall_2_int}")
except ValueError:
    print(f"Du skrev ikke et gyldig tall.")
except ZeroDivisionError:
    print("Du forsøkte å dele på null")

#%% Lese fil
FILE = "test.txt"

try:
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print(f"Fant ikke filen {FILE}")
except IOError:
    print(f"Kan ikke lese filen {FILE}")
except Exception as ex:
    print(ex)
