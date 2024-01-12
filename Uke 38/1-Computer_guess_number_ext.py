# Spill - Datamaskinen skal gjette på et tall mellom 1 og 100
import random

lavestetall, hoyestetall = 1, 100
gjettetall = 0

while True:
    gjett_str = input(f"Hvilket tall skal PC gjette på? ({lavestetall}, {hoyestetall}): ")
    if not gjett_str.isdigit():
        print("Du må skrive inn et gyldig tall.")
        continue

    gjettetall = int(gjett_str)

    if not lavestetall >= gjettetall and gjettetall <= hoyestetall:
        break

    print("Tallet ditt er utenfor range. Velg et tall mellom 1 og 100).")

forsok = 0

while True:
    tilfeldigtall = random.randrange(lavestetall, hoyestetall)
    forsok += 1
    if gjettetall == tilfeldigtall:
        break
print(f"Du tastet inn tallet {gjett_str} og PC´en trengte {forsok} på å gjette tallet.")
