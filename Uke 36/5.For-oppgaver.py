# Oppgave 1
for i in range(10):
    print(i, end=" ")

print(" ")

# Oppgave 2
for i in range(5, 16):
    print(i, end=" ")

print(" ")

# Oppgave 3
for i in range(0, 21, 2):
    print(i, end=" ")


# Oppgave 4
for i in range(1, 20, 2):
    print(i, end=" ")

print(" ")

# Oppgave 5
for i in range(30, 9, -1):
    print(i, end=" ")

print(" ")

# Oppgave 6
for i in range(30, -11, -2):
    print(i, end=" ")

print(" ")

# Oppgave 7
summen = 0
for i in range(1, 11, 1):
    summen += i
    print(f"{i}, og summen så langt er {summen},")

# Oppgave 8
summen2 = 0
for i in range(2, 21, 2):
    summen2 += i
    print(f"{i}, og summen er {summen2}")

print(" ")

# Oppgave 9
for i in range(1, 20, 2):
    summen2 += i
    print(f"{i}, og summen er {summen2}")

print(" ")

# Oppgave 10
gangetall = int(input("Skriv inn et tall i gangetabellen: "))
for i in range(1, 11, 1):
    print(f"{i}x{gangetall}={i * gangetall}")

# Gangetabellen
print(" ")
for j in range(1, 11):
    row = ""
    for i in range(1, 11):
        row += f"{i}x{j}={i * j} \t"
    print(row)