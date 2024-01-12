#%% 1. Definer en funksjon som returnerer summen av to tall.
def add():
    return x + y


# Skriv inn ønskede tall:
x = 10
y = 5
print(add())


#%% 2. Definer en funksjon som returnerer produktet av to tall.
def prod():
    return a * b


a = 2
b = 3
print(prod())


#%% 3. Definer en funksjon som returnerer kvotienten av to tall.
def div():
    return c / d


c = 10
d = 4
print(div())


#%% 4. Definer en funksjon som tar en liste som argument og returnerer summen av elementene i listen.
def num_add(tall):
    num_sum = 0
    for s in tall:
        num_sum += s
    return num_sum


num_list = [2, 3, 4, 6, 9, 99, 3]
print(num_add(num_list))


#%% 5. Definer en funksjon som tar en liste som argument og returnerer produktet av elementene i listen.
def num_prod(tall):
    num_sum = tall[0]
    for s in tall:
        num_sum *= s
    return num_sum


num_list = [2, 3, 4, 6, 9, 99, 3]
print(num_prod(num_list))


# 6. Definer en funksjon som tar en liste som argument og returnerer den største verdien i listen.
def num_max(tall):
    num_maxed = 0
    for s in tall:
        if s > num_maxed:
            num_maxed = s
    return num_maxed


num_list = [2, 3, 4, 6, 9, 99, 3]
print(num_max(num_list))


# 7. Definer en funksjon som tar en liste som argument og returnerer den minste verdien i listen.
def num_min(tall):
    num_minimum = tall[0]
    for s in tall:
        if s < num_minimum:
            num_minimum = s
    return num_minimum


num_list = [2, 3, 4, 6, 9, 99, 3, 1, 8, 55]
print(num_min(num_list))


# 8. Definer en funksjon som tar en liste som argument og returnerer gjennomsnittet av elementene i listen.
def num_avgerage(tall):
    num_avg = 0
    for s in tall:
        num_avg += s
    return num_avg / len(tall)


num_list = [2, 3, 4, 6, 9, 99, 3]
print(num_avgerage(num_list))


# 9. Definer en funksjon som tar en liste og et tall som argumenter, og returnerer en ny liste med
# alle elementene i den opprinnelige listen multiplisert med tallet.
def list_x_tall(liste, tall):
    return [s * tall for s in liste]


num_list = [2, 3, 4, 6, 9, 99, 3]
gange_tall = 2
new_list = list_x_tall(num_list, gange_tall)
print(new_list)


# 10. Definer en funksjon som tar en streng som argument og returnerer strengen reversert.
def str_reversed(tekst):
    return tekst[::-1]


tekst_streng = "Skriv en valgfri tekst her"
print(str_reversed(tekst_streng))
