#%% lage en tallrekke fra 1 til 20 i en liste

liste_tall = [i for i in range(1, 21)]
print(*liste_tall)

partall_liste = [n for n in range(0, 21) if n % 2 == 0]
print(*partall_liste)

kvadrat_liste = [x*x for x in range(1, 11)]
print(*kvadrat_liste)

#%% Set
arr = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
arr_sett = set(arr)
print(*arr)
print(*arr_sett)

#%% syntaks
my_set = {1, 2, 2, 3, 2, 3, 2}
print(*my_set)

#%% to sett
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7}

ab = a.union(b)  # Samlet unik
print("Union:", *ab)

ab_int = a.intersection(b)  # felles unik
print("Intersection:", *ab_int)

ab_diff = a.difference(b)  # hva a har som b ikke har
print("Difference", *ab_diff)

ab_sym_diff = a.symmetric_difference(b)  # hva a har som b ikke har og b har som ikke a har
print("Symetric difference", *ab_sym_diff)
