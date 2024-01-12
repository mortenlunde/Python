import random as rnd

print('A) Lag et program som oppretter en liste med 10 tilfeldige heltall. Skriv ut listen, '
      'og deretter skriv ut listen i sortert rekkefølge.')

empty_num_list = [rnd.randint(1, 1000) for _ in range(10)]
print(sorted(empty_num_list))

print('B) Skriv en funksjon som tar en liste som parameter og returnerer en tuple '
      'med det minste og største tallet i listen. ')


def min_max_num_from_list(lst):
    return min(lst), max(lst)


result_tuple = min_max_num_from_list(empty_num_list)
print(f'Det største og minste tallet i listen er: {result_tuple}')

print('C) Lag et program som oppretter en dictionary hvor nøklene er tall fra 1 til 10, og verdiene er '
      'kvadratet av nøklene. Skriv ut denne dictionary.')

sqr_dict = {}
for i in range(1, 11):
    sqr_dict[i] = i**2

for key, value in sqr_dict.items():
    print(f'Tall: {key} - Kvadratrot: {value}')
