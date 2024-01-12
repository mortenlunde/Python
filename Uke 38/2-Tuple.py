#%%
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# Tuple -> Kan ikke forandres. Immutable type
print(my_tuple)

#%% Index og slicing
elemet = my_tuple[2]
print(elemet)

sub_tuple = my_tuple[1:4]
print(sub_tuple)

#%% Lengde
length = len(my_tuple)
print(length)

#%% Innholdskontroll, sjekker om det er i tupelen
is_3_in_tuple = 3 in my_tuple
print(is_3_in_tuple)

is_3_and_4_in_tuple = 3 and 4 in my_tuple
print(is_3_and_4_in_tuple)

#%% Legge sammen tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)

#%% Repitisjon av tuple
rep_tuple = my_tuple * 3
print(rep_tuple)

#%% Min, Max, Sum
min_my_tuple = min(my_tuple)
max_my_tuple = max(my_tuple)
sum_my_tuple = sum(my_tuple)
print(min_my_tuple, max_my_tuple, sum_my_tuple)
