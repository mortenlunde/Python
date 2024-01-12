

print('A) Lag et program som leser inn et tall og skriver ut Fibonacci-sekvensen opp til det tallet.')

while True:
    fib = input('Skriv inn det høyeste tallet du ønsker i en fibonacci-sekvens (positivt heltall): ')
    fib_list = [0, 1]
    try:
        if int(fib) > 0:
            while fib_list[-1] + fib_list[-2] <= int(fib):
                fib_list.append(fib_list[-1] + fib_list[-2])
            print(*fib_list)
            break
        else:
            print('Tallet må være større enn 0.')
            continue
    except ValueError as ve:
        print('Du må skrive inn et gyldig heltall.')
        continue

print('B) Skriv en funksjon som tar to lister som parametere og returnerer en ny liste som '
      'inneholder elementene som er felles for de to listene. ')

list_a = [1, 2, 'hei', 3, 0, 22, 'Morten', 100]
list_b = [1, 2, 'morten', 3, 4, 00, 8, 10, 22, 'hei']


def check_for_commons(lst1, lst2):
    common_list = set(lst1) & set(lst2)
    print(*common_list)


check_for_commons(list_a, list_b)

print('C) Lag et program som leser inn en rekke tall og finner medianen av disse tallene.')
med_list = [1, 3, 8, 9, 10, 22, 30, 50, 74, 101]


def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        mid1 = sorted_lst[(n // 2) - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


resultat = median(med_list)
print(f'Median av {med_list} er {resultat}')

print('D) Skriv et program som leser inn en streng og bruker en dictionary'
      'for å telle antall forekomster av hver bokstav i strengen.')
read_string = input('Skriv inn et ord/setning: ')
read_dict = {}

for let in read_string:
    if let.isalnum():
        let = let.lower()
        if let in read_dict:
            read_dict[let] += 1
        else:
            read_dict[let] = 1

print(read_dict)
