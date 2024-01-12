
print('A) Lag et program som oppretter en liste med 10 tilfeldige desimaltall.'
      'Bruk en løkke for å finne og skrive ut det største tallet i listen.')

dec_list = [1.2, 5.4, 2.2, 3.2, 0.5, 10.10, 8.9, 15.0, 44.2, 8.1]
biggest_num = 0
for num in dec_list:
    if num > biggest_num:
        biggest_num = num
print(biggest_num)

print('B) Skriv en funksjon som tar en tuple som parameter og returnerer summen av elementene i tuple.')

