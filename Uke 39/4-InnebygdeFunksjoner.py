#%% min, max, sum og len

# ZIP
dyr = ["Hund", "Katt", "Hest", "Ku"]
navn = ["Qella", "Jerry", "Frøya", "Dagmar"]

dyr_navn = zip(dyr, navn)

for dyr, navn in dyr_navn:
    print(f"{dyr} heter {navn}")

#%% Reversed
my_tuple = ("A", "B", 1, 2)

reversed_tuple = reversed(my_tuple)
print(tuple(reversed_tuple))

tuple_reversed = my_tuple[::-1]
print(tuple_reversed)

#%% Sorted

arr = ("Morten", "Yngve", "Jan Robert", "Jan Roger", "Kåre", "Jo")
arr_sorted = sorted(arr)

# Sortering alfabetisk
print(arr)
print(arr_sorted)

# Sortering etter lengde på navnet
arr_sorted_len = sorted(arr, key=len)
arr_sorted_len_rev = sorted(arr, key=len, reverse=True)
print(arr_sorted_len)
print(arr_sorted_len_rev)

#%% Filter

arr2 = (1, 2, 3, 4, "a", "b", "f", 7, 0)


# Lager eb ny itereble for bare tall
def arr2_tall(n):
    if isinstance(n, int):
        return True
    return False


res = filter(arr2_tall, arr2)
print(list(res))


#%% Map

arr3 = (3, 9, 4, 2, 0)


def arr3_gange(nr):
    return nr * 2


res2 = (map(arr3_gange, arr3))
print(tuple(res2))
