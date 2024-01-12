#%% Filtrer ut alle oddetallene fra listen [1, 2, 3, 4, 5, 6].
num_list = [1, 2, 3, 4, 5, 6]


def oddetall(i):
    if i % 2 == 0:
        return False
    return True


print("Oppgave 1: ", list(filter(oddetall, num_list)))

#%% Bruk filter for å finne alle ord i listen ['apple', 'banana', 'cherry', 'date'] som har mer enn 5 bokstaver.
fruit_list = ['apple', 'banana', 'cherry', 'date']


def fruit_len(fruit):
    return len(fruit) > 5


print("Oppgave 2: ", list(filter(fruit_len, fruit_list)))

#%% Filtrer ut alle negative tall fra tuplet (-5, -3, 2, 4, -1, 6).
num_tuplet = (-5, -3, 2, 4, -1, 6)


def neg_number(neg):
    return neg < 0


print("Oppgave 3: ", tuple(filter(neg_number, num_tuplet)))

#%% Bruk en kombinasjon av filter og map for å finne alle kvadrater
# av tallene i listen [1, 2, 3, 4, 5] som er større enn 10.
num_list_kvad = [1, 2, 3, 4, 5]


def kvadrat(tall):
    return tall * tall


def kvadrat_filter(kvad):
    return kvad > 10


list_kvad = list(map(kvadrat, num_list_kvad))
list_kvad_filter = list(filter(kvadrat_filter, list_kvad))
print("Oppgave 4: ", list_kvad_filter)

#%% Bruk filter for å hente ut alle par-tall fra en dictionary med tall som nøkler.
number_dict = {
    1: "En",
    2: "To",
    3: "Tre",
    4: "Fire",
    5: "Fem",
    6: "Seks",
    7: "Syv",
    8: "Åtte",
    9: "Ni",
    10: "Ti"
}


def partall(num):
    key, value = num
    if key % 2 == 0:
        return True
    return False


number_dict_partall = dict(filter(partall, number_dict.items()))
print("Oppgave 5: ", number_dict_partall)
