import random as rnd

print('A) Lag et program som simulerer en terningkast. Programmet skal kaste en terning et gitt antall ganger og '
      'registrere resultatet av hvert kast. ')

result = []
num_of_throws = rnd.randint(5, 10)

while num_of_throws > 0:
    result.append(rnd.randint(1, 6))
    num_of_throws -= 1

print(*result)

print('\nB) Skriv en funksjon som tar en liste av tall og returnerer en liste med de unike tallene i listen. ')
result_new = []
for i in result:
    if i not in result_new:
        result_new.append(i)
print(result_new)

print('\nC) Lag et program som leser inn en fil og skriver ut hver linje i filen baklengs. ')
filename = 'LoremIpsum.txt'
with open(filename, 'r') as f:
    for line in f.readlines():
        print(line.strip()[::-1])

print('\nD) Skriv et program som lager en histogramgrafikk i konsollen basert på en liste av tall. ')


def generate_histogram(data):
    max_value = max(data)
    min_value = min(data)

    # Normaliser tallene mellom 0 og 9 for å skape histogrammet
    normalized_data = [int(9 * (x - min_value) / (max_value - min_value)) for x in data]

    # Opprett histogrammet
    histogram = [[' ' for _ in range(10)] for _ in range(len(data))]

    for y, value in enumerate(normalized_data):
        histogram[y][value] = '*'

    # Skriv ut histogrammet
    for row in reversed(histogram):
        print(' '.join(row))


# Eksempelbruk:
data_list = [3, 5, 8, 2, 7, 1, 4, 6, 3, 6, 8, 1, 4, 10, 3, 9, 3, 4, 5, 5, 6]
generate_histogram(data_list)

print('\nE) Lag et program som leser inn navn og alder fra brukeren og lagrer disse i en dictionary. '
      'Programmet skal deretter skrive ut alle navnene og alderen sortert etter alder.')


def people_reader():
    people_list = {}
    while True:
        name = input('Skriv inn et navn (eller "exit" for å avslutte): ')
        if name.lower() == 'exit':
            break

        age = input('Skriv inn alder: ')

        try:
            age = int(age)
        except ValueError:
            print('Du må skrive inn et gyldig heltall som alder.')
            continue

        people_list[name] = age

    return people_list


result = people_reader()
result_sorted = sorted(result.items(), key=lambda x: x[1])

for i in result_sorted:
    print(*i)
