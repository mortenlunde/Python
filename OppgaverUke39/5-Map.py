#%% Bruk map for å øke alle verdier i listen [1, 2, 3, 4] med 1.
num_list = [1, 2, 3, 4]


def pluss_en(tall):
    return tall + 1


print("Oppgave 1: ", list(map(pluss_en, num_list)))

#%% Konverter alle strengene i listen ['1', '2', '3'] til heltall.
string_list = ["1", "2", "3"]


def stringtoint(tall):
    return int(tall)


print("Oppgave 2: ", list(map(stringtoint, string_list)))

#%% Skriv en funksjon som returnerer første bokstav i hvert ord fra
# listen ['apple', 'banana', 'cherry'] ved hjelp av map.
fruist_list = ['apple', 'banana', 'cherry']


def forstebokstav(bokstav):
    return bokstav[0]


print("Oppgave 3: ", list(map(forstebokstav, fruist_list)))

#%% Bruk map for å lage en ny liste der hvert element er lengden av ord fra listen ['apple', 'banana', 'cherry'].
sweet_fruits = ['apple', 'banana', 'cherry']


def length(num):
    return len(num)


sweet_fruits_length = list(map(length, sweet_fruits))
print("Oppgave 4: ", sweet_fruits_length)

#%% Bruk map for å lage en ny dictionary fra to lister, der den første listen
# ['a', 'b', 'c'] er nøkler og den andre [1, 2, 3] er verdiene.
alpha_list = ['a', 'b', 'c']
digit_list = [1, 2, 3]


def dictlist(alpha, digit):
    return alpha, digit


print("Oppgave 5: ", dict(map(dictlist, alpha_list, digit_list)))
