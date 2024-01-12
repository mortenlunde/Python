from datetime import date

print('A) Lag et program som konverterer en liste av tall til en liste av deres kvadratrøtter. '
      'Bruk en for-løkke for å gjøre dette. ')
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 22, 33, -3, -5]
sqr_list = []
pos_list = []


def make_square(numlst: list) -> list:
    for i in numlst:
        if i >= 0:
            sqr_list.append(round(i ** 0.5, 3))
        else:
            sqr_list.append(f"Kan ikke beregne kvadratrot av negativt tall: {i}")
    return sqr_list


for square_root in make_square(num_list):
    print(square_root)


print('\nB) Skriv en funksjon som tar en liste som parameter og returnerer en ny liste '
      'med bare de positive tallene fra den opprinnelige listen. ')


def check_pos(numlst: list) -> list:
    for i in numlst:
        if i >= 0:
            pos_list.append(i)
    return pos_list


positive_numbers = check_pos(num_list)
ps = ', '.join(map(str, positive_numbers))
print(ps)

print('\nC) Lag et program som leser inn en tekststreng og skriver ut hver bokstav i '
      'strengen på en ny linje, men i omvendt rekkefølge. ')
user_sentence = input("Skriv en en setning med flere ord: ")
print('Ditt ord i revers på flere linjer: ')
for word in user_sentence.split()[::-1]:
    for letter in word[::-1]:
        print(letter)

print('\nD) Lag et program som leser inn en dato i formatet dd/mm/yyyy, og skriver ut hvilken ukedag datoen faller på.')
user_date = input("Skriv en dato i formatet dd/mm/yyyy: ")
d, m, y = user_date.split('/')
check_date = date(int(y), int(m), int(d))
weekday = check_date.strftime('%A')
print(f'This date was/will be: {weekday}')
