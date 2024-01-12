# Repitisjon for løkke
# range(start, stop, step) =>
# Lage en løkke som printer ut tallene 5 til 15
# Start=5, Stop=16, Step=1
for i in range(5, 16, 1):
    print(i, end=" ")

print("\n")

for n in range(1, 11):
    print("x " * n)

print("")

for n in range(10, 0, -1):
    print("x " * n)

for n in range(1, 10):
    print("|"+"_|" * 5)

print("")

for n in range(1, 6):
    print("|"+"_|" * 5)
    print(("_|") * 4)
