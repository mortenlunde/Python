

def dict_til_csv(dictionary, key=False):
    if key:
        return ",".join([f"{nokkel}" for (nokkel, verdi) in dictionary.items()]) + "\n"
    return ",".join([f"{verdi}" for (nokkel, verdi) in dictionary.items()]) + "\n"


ordbok = {"Fornavn": "Morten", "Etternavn": "Lunde", "F.år": 1990}
verdi_ = dict_til_csv(ordbok)
ks = dict_til_csv(ordbok, key=True)
print(verdi_)
print(ks)

with open("funk.csv", "a", encoding="utf-8") as file:
    file.write(ks)
    file.write(verdi_)

with open("funk.txt", "r", encoding="utf-8") as file:
    tekst = file.readlines()
print(tekst)
