import random

# Oppgave 1
print("Oppgave 1: Her er 5 tilfeldige tall mellom 1 og 100:")
runde_en = [random.randrange(1, 100) for _ in range(5)]
print(runde_en, end=" ")

# Oppgave 2
runde_en_sortert = sorted(runde_en)
print(f"\n\nOppgave 2: Her er de samme tallene, sortert fra lav til høy:\n{runde_en_sortert}")

# Oppgave 3
print("\nOppgave 3: Her er 100 tilfeldige tall mellom 1 og 200:")
runde_to = [random.randrange(1, 200) for _ in range(100)]
for n in range(0, 100, 10):
    print(runde_to[n:n+10])

# Oppgave 4
print("\nOppgave 4: Her er de samme tallene, men alle tall fra og med 100 er fjernet:")
runde_to_filtrert = [i for i in runde_to if i <= 100]
for i in range(0, 100, 10):
    print(runde_to_filtrert[i:i+10])

# Oppgave 5
print("\nOppgave 5: Her er de samme 100 tilfeldige tallene, men alle tall som kan deles på 3 er fjernet:")
runde_to_tredelt = [d for d in runde_to if d % 3 != 0]
for d in range(0, 100, 10):
    print(runde_to_tredelt[d:d+10])
