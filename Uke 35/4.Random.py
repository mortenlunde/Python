import random as rnd

# Skrive ut et tilfeldig tall mellom 1 og 100
print(rnd.randint(1, 100))

# Tilfeldig tall mellom 0 og 100
print((rnd.randrange(0, 100, 2)))
print((rnd.randrange(1, 100, 2)))

# Tilfeldig desimaltall
print(round(rnd.uniform(1, 10), 2))
