# While løkke

x = 0

while x < 10:
    print(x, end=" ")
    x += 1

x = 0
print("\n")

# Skrive ut tallene 0 - 9
while True:
    print(x, end=" ")
    x += 1

    if x > 9:
        break

# Skrive ut tallene 1 2 3 4 6 7 8 9 10 (ikke 5) med en while løkke

x = 0
print("\n")

while x < 10:
    x += 1
    if x == 5:
        continue
    print(x, end=" ")
