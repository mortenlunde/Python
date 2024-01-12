import os

MAPPENAVN = os.path.join("Files")

if not os.path.exists(MAPPENAVN):
    os.mkdir(MAPPENAVN)
    for y in range(2015, 2024):
        for m in range(1, 13):
            FILENAME = os.path.join(MAPPENAVN, f"{y}-{m:0>2}.txt")
            if not os.path.exists(FILENAME):
                with open(FILENAME, "w", encoding="utf-8") as fwrite:
                    print(f"Opprettet fil: {FILENAME}")
            else:
                print(f"Filen {FILENAME} finnes allerede")
else:
    print(f"Mappen {MAPPENAVN} finnes allerede")
