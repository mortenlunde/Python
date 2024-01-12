from math import pi


def capitalize(prompt):
    """
    Koverterer alle ord til å ha stor forbokstav ved å bruke funksjonen .title(). Siden vi også kjører sjekk
    for hvert tegn så sørger vi for at input ikke kan være blank og at det er minst 1 bokstav.
    :param prompt: Input- string fra bruker
    :return: Input- string fra bruker med stor forbokstav i hvert ord.
    """
    while True:
        user_string = input(prompt)
        if any(char.isalpha() for char in user_string):
            return user_string.title()
        else:
            print('Du må skrive inn en gyldig tekst med minst én bokstav.')


def metertokilometer(usr_input):
    """
    Funksjonen sjekker at det kommer inn et tall enten i form av heltall eller desimaltall. Dersom det er tall som
    kommer inn så gjøres denne om til float, deler tallet på 1000 for å få meter til kilometer og gir svaret i
    retur med 3 desimaler. Vi sjekker at det er et positivt tall, og gir feilmelding om det er negativt tall
    eller om det ikke er tall som blir tastet inn. Koden looper helt til den får et positivt tall.
    :param usr_input: Bruker- input som skal være positivt tall
    :return: brukertall/1000 med 3 desimaler. Alternativt feilmelding om tallet er mindre enn 0 eller er string
    """
    while True:
        try:
            input_float = float(usr_input)
            if input_float > 0:
                return round((input_float / 1000), 3), input_float
            else:
                print('Du må skrive inn et positivt tall.')
        except ValueError:
            print('Du må skrive inn et gyldig tall, enten heltall eller desimaltall adskilt med punktum')
        usr_input = input('Skriv inn antall meter du ønsker å konvertere til kilometer: ')


def circle_area_converter(usr_r):
    """
    Tar inn bruker sin input, sjekker at det er heltall eller desimaltall. Dersom tallet er positivt så vil
    funksjonen returnere arealet til en sirkel med radius av brukerinput.
    :param usr_r: bruker sin input som skal være et positivt tall
    :return: brukertall*pi² med 3 desimaler. Alternativt feilmelding om tallet er mindre enn 0 eller er string
    """
    while True:
        try:
            radius = float(usr_r)
            if radius > 0:
                return round(pi * radius * radius, 3), radius
            else:
                print('Du må skrive et positivt tall.')
        except ValueError:
            print('Du må skrive inn et gyldig tall, enten heltall eller desimaltall adskilt med punktum.')
        usr_r = input('Skriv inn en ønsket radius (i cm) på en sirkel du ønsker cm²: ')


""" Disse to funksjonene kunne nesten blitt slått sammen, velge om vi skal regne m->km eller cm->cm² i det vi kaller
funksjonen. På en side så får vi kortere kode, men jeg føler det er litt mer oversiktig å skille de av. Men vi 
kunne altså lett gjort det på tilsvarende måte som i oppgave 1 """


def most_frequent_letter(str_input):
    """
    Denne funskjonen tar en tekst fra bruker, scanner tegn for tegn og dersom tegn er en bokstav så legges det til
    i dictionary hvor bokstav er key og antall ganger det er gjentatt som value. Looper gjennom hele tekstek som er
    konvertert til små bokstaver for å telle feks a og A som sammebokstav. Siden vi bruker .isalpha() så er det kun
    bokstaver og ikke whitespace/tall/spesialtegn som legges til i dictionary. Dersom input er blank eller ikke
    inneholder noen bokstaver så returnerer funksjonen feilmelding til konsoll. Den lager så variabel most_used_letter
    som henter høyeste value ved bruk av max().
    :param str_input: Bruker sin tekst- input
    :return: En tuple av mest brukte bokstav og antall ganger gjentatt.
    """
    letters = {}
    try:
        for letter in str_input.lower():
            if letter.isalpha():
                letters[letter] = letters.get(letter, 0) + 1
        most_used_letter = max(letters, key=letters.get)
        return most_used_letter, letters[most_used_letter]
    except TypeError:
        print('Du mangler tekst eller har ingen bokstaver i setningen.')


def main():
    """
    Kaller på de forskjellge funksjonene og besvarer oppgavespørsmålene
    :return: None
    """
    # A. Lag en funksjon som tar inn en tekstreng som parameter og returnerer teksten der hvert ord
    # starter med en stor bokstav.
    user_sentance = capitalize('Skriv inn en setning: ')
    print(f'Din setning med stor bokstav for hvert ord er: {user_sentance}')

    # B. Skriv en funksjon som konverterer meter til kilometer. Funksjonen skal ta imot antall meter
    # som argument og returnere tilsvarende antall kilometer. Den bør også sjekke at inndataen er
    # positiv og er et tall. Hvis ikke, skal funksjonen returnere en passende feilmelding.
    user_input = input('Skriv inn antall meter du ønsker å konvertere til kilometer: ')
    result, final_input = metertokilometer(user_input)
    print(f'{final_input} meter er {result} kilometer')

    # C. Skriv en funksjon som tar en radius som inndata og returnerer arealet av en sirkel med den
    # radiusen. (Tips: import math -> og bruk math.pi). Den bør også sjekke at inndataen er positiv
    # og er et tall. Hvis ikke, skal funksjonen returnere en passende feilmelding.
    user_radius = input('Skriv inn en ønsket radius (i cm) på en sirkel du ønsker cm²: ')
    areal, radius = circle_area_converter(user_radius)
    print(f'En sirkel med radius {radius}cm har et areal på: {round(areal, 2)} cm²')

    # D. Lag en funksjon som finner ut bokstaven som forekommer oftest i setningen. Funksjonen skal ta imot en tekstreng
    # som argument. Funksjonen skal returnere en tuple der det første elementet er bokstaven som forekommer oftest,
    # og det andre elementet er antall ganger denne bokstaven forekommer i teksten.
    letter, freq = most_frequent_letter(user_sentance)
    print(f'Bokstaven som forekom flest ganger fra setningen du lagde først: {letter} - {freq} ganger.')


if __name__ == "__main__":
    main()
