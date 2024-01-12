#%% Sorter listen [3, 1, 4, 1, 5, 9, 2, 6, 5] i stigende rekkefølge.
tall_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Oppgave 1: ", sorted(tall_list))

#%% Sorter listen ['apple', 'Banana', 'Cherry'] alfabetisk, uavhengig av store/små bokstaver.
fruit_list = ['apple', 'Banana', 'Cherry']
fruit_list_lower = []
for i in fruit_list:
    fruit_list_lower.append(i.lower())
print("Oppgave 2: ", fruit_list_lower)

#%% Sorter tuplet (6, 2, 9, 1, 5, 3) i synkende rekkefølge.
num_tuple = (6, 2, 9, 1, 5, 3)
print("Oppgave 3: ", sorted(num_tuple)[::-1])

#%% Sorter listen med ord ['apple', 'banana', 'cherry'] basert på lengden av hvert ord.
fruit_list_len = sorted(fruit_list, key=len)
print("Oppgave 4: ", fruit_list_len)

#%% Sorter en liste med dictionaries basert på en bestemt nøkkel.
animal_dict = {"Hund": "Bruno", "Katt": "Pusur", "Hest": "Frøya", "Ku": "Dagros", "Løve": "Simba"}
animal_dict_sort = sorted(animal_dict.keys())
animal_dict_empty = {}
print("Oppgave 5:", end=" ")
for dyr in animal_dict_sort:
    navn = animal_dict[dyr]
    animal_dict_empty[dyr] = navn
print(animal_dict_empty)
