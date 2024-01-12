import os
import sys

FILENAME = "testtt.txt"
FILENAME_WRITE = "test.log"

# Metode 1 <- Best
if not os.path.exists(FILENAME) and not os.path.isfile(FILENAME):
    print(f"Finner ikke filen {FILENAME}")
    pass
else:
    with open(FILENAME, "r", encoding="utf-8") as f_to_read:
        for line in f_to_read:
            print(line)

# Metode 2
'''
f_to_read = open(FILENAME, "r")
for line in f_to_read:
    print(line)
f_to_read.close()
'''

# Vi skriver til en ny fil. Lages hvis den ikke finnes
with open(FILENAME_WRITE, "w", encoding="utf-8") as fwrite:
    for i in range(1, 201):
        fwrite.write(f"{i}\n")

# Vi legger til tekst
with open(FILENAME_WRITE, "a", encoding="utf-8") as fwrite:
    for i in range(200, 301):
        fwrite.write(f"{i}\n")
