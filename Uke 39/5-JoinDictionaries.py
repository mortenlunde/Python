#%% Create dictionary from 2 lists

dyr = ["Hund", "Katt", "Hest", "Ku"]
navn = ["Qella", "Jerry", "Frøya", "Dagmar"]

# Ut fra listen lager vi en dictionary
dyr_navn = dict(zip(dyr, navn))
print(dyr_navn)

# Samme problemstilling med løsning av løkker
dyr_navn_2 = {}
for i in range(len(dyr)):
    dyr_navn_2[dyr[i]] = navn[i]
print(dyr_navn_2)
