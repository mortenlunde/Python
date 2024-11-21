dprint('A) Lag et program som oppretter en liste med 5 navn. Deretter, bruk en løkke for å be brukeren'
      'om å legge til 5 til navn i listen. Skriv ut den endelige listen.')

name_list = ['Morten', 'Line', 'Jan Robert', 'Yngve', 'Brian']

print('Du skal legge til 5 navn i en liste: ')
for _ in range(5):
    name_list.append(input('Skriv inn et navn: '))

print(name_list)

print('B) Skriv en funksjon som tar en tuple som parameter og returnerer en reversert versjon av denne tuple.')
name_tuple = tuple(name_list)


def reverse_tuple(tpl):
    return tpl[::-1]


print(reverse_tuple(name_tuple))


print('C) Lag et program som oppretter en dictionary med 5 land som nøkler og deres '
      'hovedsteder som verdier. Skriv ut hvert land og dets hovedstad. ')

land_hovedsteder = {
    "Norge": "Oslo",
    "Sverige": "Stockholm",
    "Danmark": "København",
    "Finland": "Helsinki",
    "Island": "Reykjavik"
}

for land, hovedstad in land_hovedsteder.items():
    print(f"{land} - Hovedstad: {hovedstad}")
