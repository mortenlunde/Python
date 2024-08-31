# Plan
# 3 spørsmål med 3 alternativer
# Presentere spørsmål og svar for spiller
# Les svar fra spiller
# Teste svar fra spiller og gi tilbakemelding
# Gi en totalscore til spiller

totalsum = 0

# Spørsmål 1
print("Spørsmål 1: Hva er datatypen til verdien 10?  (1, 2 eller 3)")

# Alternativer spm 1
print("1. int\n2. str\n3. float")
svar1 = int(input("Svar ved å skrive inn alternativ nummer: "))
print(f"Du valgte alternativ nummer: {svar1}")
if svar1 == 1:
    print("Korrekt!")
    totalsum += 1
else:
    print("Feil!")

# Spørsmål 2
print("Spørsmål 2: Hva er datatypen til verdien ´hello´?  (1, 2 eller 3)")

# Alternativer spm 2
print("1. int\n2. str\n3. float")
svar2 = int(input("Svar ved å skrive inn alternativ nummer: "))
print(f"Du valgte alternativ nummer: {svar2}")
if svar2 == 2:
    print("Korrekt!")
    totalsum += 1
else:
    print("Feil!")

# Spørsmål 3
print("Spørsmål 3: Hva er datatypen til verdien True eller False?  (1, 2 eller 3)")

# Alternativer spm 3
print("1. int\n2. bool\n3. float")
svar3 = int(input("Svar ved å skrive inn alternativ nummer: "))
print(f"Du valgte alternativ nummer: {svar3}")
if svar3 == 2:
    print("Korrekt!")
    totalsum += 1
else:
    print("Feil!")

print(f"Du fikk totalt {totalsum} riktige svar.")
