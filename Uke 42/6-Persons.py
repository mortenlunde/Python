import os
import sys

# 1. Beregn den totale alderen for alle menn i datasettet.
# 2. Beregn den totale alderen for alle kvinner i datasettet.

file = "persons.csv"
if not os.path.exists(file):
    print(f"Filen {file} finnes ikke. Avslutter programmet.")
    sys.exit()
else:
    with open(file, "r", encoding="utf-8") as f:
        header = f.readline().rstrip().split(',')
        header_kjonn = header.index("Kjønn")
        header_alder = header.index("Alder")
        tot_ald_menn = 0
        tot_ald_kvinner = 0
        utskrift_menn = ""
        utskrift_kvinner = ""

        for line in f:
            arr = line.rstrip().split(',')
            kjonn = arr[header_kjonn]
            alder = int(arr[header_alder])

            if kjonn == "Mann":
                tot_ald_menn += alder
                utskrift_menn += f"{alder} + "
            elif kjonn == "Kvinne":
                tot_ald_kvinner += alder
                utskrift_kvinner += f"{alder} + "

        utskrift_menn = utskrift_menn.rstrip(" + ")
        utskrift_kvinner = utskrift_kvinner.rstrip(" + ")

        print("Total alder menn:", utskrift_menn, "=", tot_ald_menn)
        print("Total alder kvinner:", utskrift_kvinner, "=", tot_ald_kvinner)


# 3. Hvor mange menn er det i datasettet?
# 4. Hvor mange kvinner er det i datasettet?

if not os.path.exists(file):
    print(f"Filen {file} finnes ikke. Avslutter programmet.")
    sys.exit()
else:
    with open(file, "r", encoding="utf-8") as f:
        header = f.readline().rstrip().split(',')
        header_kjonn = header.index("Kjønn")
        tot_ant_menn = 0
        tot_ant_kvinner = 0

        for line in f:
            arr = line.rstrip().split(',')
            kjonn = arr[header_kjonn]

            if kjonn == "Mann":
                tot_ant_menn += 1
            elif kjonn == "Kvinne":
                tot_ant_kvinner += 1

        print(f"Antall menn i datasettet: {tot_ant_menn}\nAntall kvinner i datasettet: {tot_ant_kvinner}")
