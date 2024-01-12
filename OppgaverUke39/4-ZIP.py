#%% Bruk zip for å kombinere listen ['a', 'b', 'c'] med listen [1, 2, 3] til en liste av tupler.
letter_list = ["a", "b", "c"]
num_list = [1, 2, 3]
combined_list = tuple(zip(letter_list, num_list))
print("Oppgave 1: ", combined_list)

#%% Kombiner to lister av tall der den ene er [1, 2, 3] og den andre er [4, 5, 6]
# til en ny liste med summer av parrede elementer ved hjelp av zip og map.
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1_2 = list(zip(list_1, list_2))


def sum_list(tall1, tall2):
    return tall1 + tall2


print("Oppgave 2: ", list(map(sum_list, list_1, list_2)))

#%% Lag en dictionary der nøklene er fra listen ['Anna', 'Bob', 'Charlie']
# og verdiene er fra listen [25, 30, 35] ved hjelp av zip.
name_list = ['Anna', 'Bob', 'Charlie']
age_list = [25, 30, 35]
people_list = dict(zip(name_list, age_list))
print("Oppgave 3: ", people_list)

#%% Kombiner tre lister ved hjelp av zip: ['a', 'b', 'c'], [1, 2, 3], og ['apple', 'banana', 'cherry'].
abc_list = ['a', 'b', 'c']
numb_list = [1, 2, 3]
fruit_list = ['apple', 'banana', 'cherry']
zip_list = list(zip(abc_list, numb_list, fruit_list))
print("Oppgave 4: ", zip_list)

#%% Hvordan ville du brukt zip for å splitte en liste av tupler
# (f.eks. [('a', 1), ('b', 2), ('c', 3)]) i to separate lister?
unzipped_list = [('a', 1), ('b', 2), ('c', 3)]
zip_1, zip_2 = zip(*unzipped_list)
print(f"Oppgave 5:  Liste 1: {zip_1}, Liste 2: {zip_2}")
