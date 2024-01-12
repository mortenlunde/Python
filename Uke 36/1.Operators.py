# Matematikk
# Aritmhmetic : +, -, *, /, %, **, //

# +
print(3 + 4)
print(7 - 4)
print(7 / 3)
print(8 * 4)

# **
print(f"2**3 = {2**3}")

# // - heltalls divisjon
print(f"7//3 = {7//3}")

# % => modules (rest)
print(f"7%3 = {7%3}\n")

# Sammenlignin
# Comparison : ==, !=, >, <, >=, <=

x = 3
y = 4
if x == y:
    print("x == y")

if x != y:
    print("x != y")

# > -> Større enn
if x > y:
    print("x er større enn y")

# > -> Mindre enn
if x < y:
    print("x er mindre enn y")

# > -> Mindre enn eller lik
if x <= y:
    print("x er mindre enn y")

# > -> Større enn eller lik
if x >= y:
    print("x er større enn y\n")

# Logical : or, and, not
x = 5
y = 7

# Assignment : =, +=, -=

antall_riktige = 0
antall_riktige = antall_riktige + 1
antall_riktige += 1
antall_riktige -= 1
print(antall_riktige)

if x == 5 or x == 7:
    print("x er 5 eller 7")

if x == 5 and y == 5:
    print("x er 5 og y er 5")

if not (x == 5 and y == 5):
    print("NOT: x er 5 og y er 5")
