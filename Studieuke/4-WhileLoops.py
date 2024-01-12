import random

#%% 1. Skriv et program som bruker en while-løkke til å be brukeren om input til brukeren skriver "stopp".
tekst_input = ""
while tekst_input != "Stopp":
    tekst_input = str(input("Skriv inn tekst. Når du skriver inn 'stopp' avsluttes programmet. ").capitalize())

#%% 2. Bruk en while-løkke til å skrive ut tallene fra 1 til 10.
t = 0
while t < 10:
    t += 1
    print(t, end=" ")

#%% 3. Bruk en while-løkke til å regne ut summen av tallene fra 1 til n.
n = 10  # Sett inn ønsket tall
n_sum = 0
while n > 0:
    n_sum += n
    n -= 1
print(n_sum)

#%% 4. Bruk en while-løkke til å regne ut produktet av tallene fra 1 til n.
n = 10  # Sett inn ønsket tall
n_sum = 1
while n > 0:
    n_sum *= n
    n -= 1
print(n_sum)

#%% 5. Skriv et program som bruker en while-løkke til å
# finne det første tallet som er større enn 1000 og delelig med 17.
tall = 1000
while tall % 17 != 0:
    tall += 1
print(tall)

#%% 6. Bruk en while-løkke til å beregne gjennomsnittet av en liste med tall.
num_list = [1, 2, 5, 8, 9, 10, 55, 23]
num_sum = 0
i = len(num_list)
while i > 0:
    num_sum += num_list[i - 1]
    i -= 1
avg = num_sum / len(num_list)
print(avg)

#%% 7. Bruk en while-løkke til å finne det største tallet i en liste.
num_list_max = [1, 2, 5, 8, 9, 10, 55, 23]
max_num = 0
k = len(num_list_max)
while k > 0:
    if num_list_max[k - 1] > max_num:
        max_num = num_list_max[k - 1]
    k -= 1
print(max_num)

#%% 8. Bruk en while-løkke til å finne det minste tallet i en liste.
num_list_min = [5, 8, 9, 10, 55, 23, 8, 4, 1, 9, 11]
min_num = num_list_min[0]
x = len(num_list_min)
while x > 0:
    if num_list_min[x - 1] < min_num:
        min_num = num_list_min[x - 1]
    x -= 1
print(min_num)

#%% 9. Skriv et program som bruker en while-løkke til å gjette et tilfeldig generert tall.
random_num = random.randint(1, 100)
guess_num = 0
guess_tries = 0
while random_num != guess_num:
    guess_num = random.randint(1, 100)
    guess_tries += 1
print(f"Tilfeldig tall var {random_num} og vi trengte {guess_tries} forsøk på å gjette nummeret.")

#%% 10. Bruk en while-løkke til å finne summen av kvadratene av tallene fra 1 til n.
n = 10  # Sett inn ønsket tall
n_len = n
n_kvad = 0
while n > 0:
    kvadrat = n * n
    n_kvad += kvadrat
    n -= 1
print(f"Summen av kvadratene fra 1 til {n_len} er: {n_kvad}")
