totalsum = 0
sporsmaal = ["Spørsmål 1: Hva er datatypen til verdien 10?  (1, 2 eller 3)",
             "Spørsmål 2: Hva er datatypen til verdien ´hello´?  (1, 2 eller 3)",
             "Spørsmål 3: Hva er datatypen til verdien True eller False?  (1, 2 eller 3)"]
fasit = [3, 1, 2]

for i in range(len(sporsmaal)):
    print(sporsmaal[i])
    print("1. str\n2. bool\n3. int")
    svar = int(input("Svar ved å skrive inn alternativ nummer: "))
    if fasit[i] == svar:
        print("Du svarte riktig")
        totalsum += 1
    else:
        print("Du svarte feil")

print(f"Du fikk totalt {totalsum} riktige svar.")
