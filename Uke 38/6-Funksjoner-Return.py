#%% Funksjoner som returnerer verdier

x = 23
y = 56
z = x + y

print(f"Sum = {z}")

x = 43
y = 12
z = x + y
print(f"Sum = {z}")


def xplusy(a: int, b: int) -> int:
    c = a + b
    return c


print("Sum = ", xplusy(12, 43))
