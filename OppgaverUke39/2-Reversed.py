#%% Reverser listen [1, 2, 3, 4, 5].
tall_liste = [1, 2, 3, 4, 5]
print("Oppgave 1: ", sorted(tall_liste, reverse=True))

#%% Konverter en streng 'hello' til en liste og reverser den ved hjelp av reversed.
tekst = "hello"
tom_liste = []
for i in tekst:
    tom_liste.append(i)
print("Oppgave 2: ", list(reversed(tom_liste)))

#%% Reverser tuplet (1, 2, 3, 4, 5).
tall_tuplet = (1, 2, 3, 4, 5)
print("Oppgave 3: ", tuple(reversed(tall_tuplet)))

#%% Hvordan ville du brukt reversed for å reversere nøklene i en dictionary?
animal_dict = {"Hund": "Bruno", "Katt": "Pusur", "Hest": "Frøya", "Ku": "Dagros", "Løve": "Simba"}
animal_dict_sort = sorted(animal_dict.keys())
animal_dict_empty = {}

print("Oppgave 4:", end=" ")
for dyr in animal_dict_sort:
    navn = animal_dict[dyr]
    animal_dict_empty[dyr] = navn

animal_dict_rev = {navn: key for navn, key in reversed(animal_dict_empty.items())}
print(animal_dict_rev)

#%% Reverser rekkefølgen av ord i strengen 'PycharmProjects er gøy' ved hjelp av reversed.
morsom_tekst = 'PycharmProjects er gøy'
morsom_list = morsom_tekst.split()
print(list(reversed(morsom_list)))
