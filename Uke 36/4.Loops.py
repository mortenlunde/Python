# Vi skriver ut tallene 0 - 9
for mitttall in range(10):
    print(mitttall, end=" ")

print(" ")

#%%
# Vi skriver partallene mellom 0 - 20
for i in range(0, 21, 2):
    print(i, end=" ")

print(" ")

# While løkke
x = 0
while x <= 10:
    print(x, end=" ")
    x += 1
