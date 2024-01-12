# Oppgave 1
tall_liste = [3, 5, 9, 10, 11]
while_lokke = 0


def test_1(i):
    if i >= 10:
        return f"{i} er større enn eller lik 10."
    else:
        return f"{i} er mindre enn 10."


def test_2(i):
    if i <= 5:
        return f"{i} er mindre enn eller lik 5."
    else:
        return f"{i} er større enn 5."


def test_3(i):
    if 5 <= i <= 10:
        return f"{i} er mellom 5 og 10."
    else:
        return f"{i} er ikke mellom 5 og 10."


print("Oppgave 1: Test verdiene i en liste: ")

for n in tall_liste:
    resultat_1 = test_1(n)
    resultat_2 = test_2(n)
    resultat_3 = test_3(n)
    print(f"{resultat_1} {resultat_2} {resultat_3}")

# Oppgave 2
print("\nOppgave 2: Skriv ut indeks og verdi i listen med for- løkke")
for index, verdi in enumerate(tall_liste):
    print(f"Index {index}: {verdi}")

# Oppgave 3
print("\nOppgave 3: Skriv ut indeks og verdi i listen med while- løkke")
while while_lokke < len(tall_liste):
    verdi = tall_liste[while_lokke]
    print(f"Index {while_lokke}: {verdi}")
    while_lokke += 1

# Oppgave 4
print("\nOppgave 4: Summer alle tallene i listen")
print(f"Summen av alle tallene er: {sum(tall_liste)}")
