# ********************************
# ****** OPPGAVE 2 - LISTER ******
# ********************************

# Oppgave 1
my_list = [24, 7, 10, 17, 20, 5]

# Sum metode 1
print("Summen av tallene i listen, metode 1: ", sum(my_list))

# Sum metode 2
total_sum = 0
for i in my_list:
    total_sum += i
print("Summen av tallene i listen, metode 2: ", total_sum)

# Gjennomsnitt
print(f"Gjennomsnittet av tallene i listen er: {round(float(sum(my_list) / float(len(my_list))), 2)}")

# Oppgave 2
my_list2 = [7, 12, 17, 65, 444, 87, 3, 75]
print(f"Minste verdi i liste nummer 2 er: {min(my_list2)}.")
print(f"Høyeste verdi i liste nummer 2 er: {max(my_list2)}.")

# Oppgave 3
my_list3 = [9, 6, 8, 6, 1, 99, 50, 17, 15]
print("Oddetallene i listen er: ")
for i in range(len(my_list3)):
    if my_list3[i] % 2 != 0:
        print(my_list3[i], end=" ")

total_sum = 0
length = 0
for i in range(len(my_list3)):
    if my_list3[i] % 2 != 0:
        total_sum += my_list3[i]
        length += 1
print(f"\nGjennomsnittet av oddetallene i listen er: {total_sum / length}")

# Oppgave 4
# Liste med unike elementer:
# Les inn en liste med elementer (tekst eller tall).
# Fjern alle duplikate elementer fra listen og lag en ny liste med unike elementer.
# Skriv ut den nye listen.

my_list = ["Hello", 1, 7, "Norge", "Jan", "Morten", 7, 10, 1, "Bye"]
my_unique_list = []

for n in my_list:
    if n not in my_unique_list:
        my_unique_list.append(n)
print(my_unique_list)

# Oppgave 5:
# Les inn en liste med tekststrenger.
# Skriv ut alle tekststrengene i listen i omvendt rekkefølge.

my_string_list = ["Hei", "Fin", "Morten", "Sol", "Sommer"]
print(my_string_list[::-1])

# Oppgave 6
# Les inn en liste med tall.
# Lag en ny liste som kun inneholder partall fra den opprinnelige listen.
# Skriv ut den nye listen.

my_int_list = [7, 10, 11, 13, 5, 20, 2]
my_even_list = []
for i in my_int_list:
    if i % 2 == 0:
        my_even_list.append(i)
print(my_even_list)

# Oppgave 7
# Les inn en liste med tekststrenger.
# Fjern alle elementer i listen som er lengre enn 5 tegn.
# Skriv ut den endrede listen.

my_string_list_new = ["Hei", "Morten", "Elefant", "Hund", "Giraffe", "Baltasar", "Syv"]
x = 0
while x < len(my_string_list_new):
    if len(my_string_list_new[x]) > 5:
        my_string_list_new.pop(x)
    else:
        x += 1
print(my_string_list_new)

# Oppgave 8
# Les inn en liste med tall.
# Sjekk om tallene er i stigende rekkefølge (hver etterfølgende verdi er større enn den forrige).
# Gi tilbakemelding om rekkefølgen er stigende eller ikke.

my_tall_list1 = [1, 4, 6, 8, 10, 20, 25, 50, 100]
my_tall_list2 = [2, 1, 3, 9, 10, 7, 5]
stigende_rekkefolge = True
y = 0

while y < len(my_tall_list1) - 1:
    if my_tall_list1[y] >= my_tall_list1[y+1]:
        stigende_rekkefolge = False
        break
    y += 1

if stigende_rekkefolge:
    print("Tallrekkefølgen er stigende")
else:
    print("Tallrekkefølgen er ikke stigende")

y = 0

while y < len(my_tall_list2) - 1:
    if my_tall_list2[y] >= my_tall_list2[y+1]:
        stigende_rekkefolge = False
        break
    y += 1

if stigende_rekkefolge:
    print("Tallrekkefølgen er stigende")
else:
    print("Tallrekkefølgen er ikke stigende")

# Oppgave 9
# Les inn to lister med tall.
# Finn og skriv ut de felles elementene (tallene som er i begge listene).

my_same_list1 = [0, 1, 2, 9, 7, 10, 20, 5]
my_same_list2 = [1, 6, 10, 20, 4, 21, 13, 9]
my_same_list_tom = []

for t in my_same_list1:
    if t in my_same_list2:
        my_same_list_tom.append(t)
print(my_same_list_tom)

# Oppgave 10
# Les inn en liste med ord.
# Identifiser og skriv ut alle ordene som er palindromer (leses likt baklengs som forover,
# for eksempel "radar" eller "level").

my_palindrom_list = ["Radar", "Level", "Morten", "Python", "Civic"]
palindromer = []


def palindrome(word):
    return word.lower() == word.lower()[::-1]


for word in my_palindrom_list:
    if palindrome(word):
        palindromer.append(word)
print(palindromer)
