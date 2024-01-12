def main():
    # A. Lag en liste som inneholder fem valgfrie frukter.
    fruits = ['Eple', 'Appelsin', 'Melon', 'Ananas', 'Blåbær']

    # A.1. Skriv ut alle elementene ved hjelp av en for-løkke.
    for f in fruits:
        print(f, end=" ")
    print('')

    # A.2. Skriv ut alle elementene ved hjelp av en while-løkke.
    list_start = 0
    while len(fruits) > list_start:
        print(fruits[list_start], end=" ",)
        list_start += 1
    print('')

    # B. For hver frukt, tilordne en farge til frukten og opprett en annen liste med disse fargene. Skriv
    # ut fruktens navn sammen med dens farge. Eks: "Eplet er rødt."
    fruit_colors = ['Rød', 'Oransje', 'Rød/grønn', 'Brun/gul', 'Blå']
    for f, ff in zip(fruits, fruit_colors):
        print(f, 'er', ff, end="\n")

    # C. Skriv ut det andre og fjerde elementet fra fruktlisten.
    print(fruits[1], fruits[3])

    # D. Skriv ut fruktlisten i alfabetisk rekkefølge.
    print(*sorted(fruits))

    # E. Ta utgangspunkt i frukt-listen og farge-listen fra oppgave A og B og lag en dictonary med
    # fruktene som nøkler og deres farger som verdier. Skriv ut hver kombinasjon som "Eple: Rød".
    fruit_dict = dict(zip(fruits, fruit_colors))
    for k, v in fruit_dict.items():
        print(f'{k}: {v}')

    # F. Du har blitt gitt en liste med dictionaries som inneholder personers navn og alder.
    list_dicts = [
        {'name': 'Vegard', 'age': 50},
        {'name': 'Tor', 'age': 22},
        {'name': 'Siv', 'age': 30},
        {'name': 'Anne', 'age': 30},
        {'name': 'Beate', 'age': 66}
    ]
    # F.1. Sorter listen basert på alder i stigende rekkefølge.
    print(sorted(list_dicts, key=lambda x: x['age']))

    # F.2. I tilfeller hvor to personer har samme alder, skal du sortere dem alfabetisk basert på navnet.
    print(sorted(list_dicts, key=lambda x: (x['age'], x['name'])))


if __name__ == "__main__":
    main()
