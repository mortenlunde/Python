#%% Sekvens utpakning
# For Tuple og List

my_tuple = ("Morten", "Lunde", 32)
Fornavn, Etternavn, Alder = my_tuple

print(Fornavn, Etternavn, Alder, "\n")

#%% Dictionary

my_dict = {"Fornavn:": "Morten", "Etternavn:": "Lunde", "Alder:": 32}

# UTpakking av key og value
for k, v in my_dict.items():
    print(k, v)
