# Spill - Datamaskinen skal gjette på et tall mellom 1 og 100

import random

lavestetall = int(input("Skriv inn det laveste tallet: "))
hoyestetall = int(input("Skriv inn høyeste tall: "))

tilfeldigtall = random.randrange(lavestetall, hoyestetall)
gjettetall = random.randrange(lavestetall, hoyestetall)
forsok = 0

while True:
    forsok += 1
    if tilfeldigtall == gjettetall:
        break
    gjettetall = random.randrange(lavestetall, hoyestetall)
print(f"Tilfeldig tall ble {tilfeldigtall}, og det tok {forsok} forsøk å gjette på samme tall.")
