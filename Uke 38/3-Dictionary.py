#%%
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# Dictionary -> ordbok med ´key´med tilhørende ´value´
my_dict = {"Morten": 32, "Yngve": 50, "Craig": 40, "Jan Robert": 30}
print(my_dict)

#%% Hente verdier
age_morten = my_dict["Morten"]
print(age_morten)
print(my_dict.get("Yngve"))

#%% Sette og oppdatere i dictionary
my_dict["Craig"] = 42
print(my_dict)

my_dict.update({"Jan Robert": 29})
print(my_dict)

#%% Slette
my_dict.pop("Craig")
del my_dict["Yngve"]
print(my_dict)

#%% Pop
print(my_dict)
alder_morten = my_dict.pop("Morten")
print(alder_morten)
print(my_dict)

my_dict = {"Morten": 32, "Yngve": 50, "Craig": 40, "Jan Robert": 30}

#%% Liste av nøkler og verdier
keys = my_dict.keys()
values = my_dict.values()
print(type(keys), type(values))
print(keys, values)

items = my_dict.items()
print(items)

#%% Kopiering av dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)

#%% Slette alle elementer i dictionary
my_dict_copy.clear()
print(my_dict_copy)
print(my_dict)
