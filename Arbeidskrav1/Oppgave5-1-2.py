# Oppgave 5
def footconverter():
    print("Oppgave 1: Funksjon for å regne om meter til fot")
    inputmeter = input("Skriv inn antall meter du vil regne om til fot: ")
    convert = (float(inputmeter) * 3.28)
    return f"{inputmeter} meter er ≈ {round(convert, 2)} fot"


print(footconverter())


def degreeconverter():
    print("\nOppgave 2: Funksjon for å regne om celsius til fahrenheit")
    inputcelsius = input("Skriv inn grader i celsius for å få dette regnet til fahrenheit: ")
    convert = (float(inputcelsius) * 1.8 + 32)
    return f"{inputcelsius} grader celsius tilsvarer {round(convert, 1)} fahrenfeit."


print(degreeconverter())
