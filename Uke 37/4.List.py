# Lister

#%%
my_list = [3, 4, 5, 6, 3, 35, 45, 46, 6, 565, 45]
my_list2 = [2, 3, 5, 44, 34]
print(my_list)
print(my_list[2])
my_list.append(13)
print(my_list)
my_list.insert(0, 44)
print(my_list)
my_list.extend(my_list2)
print(my_list)
my_list.remove(3)
print(my_list)
my_list.pop(0)
print(my_list)
my_list_sorted = sorted(my_list)
print(my_list_sorted)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.index(3))
print(my_list.count(3))
my_list3 = my_list.copy()
print(my_list3)
print(len(my_list))
print(min(my_list))
print(max(my_list))
print(sum(my_list))

#%%
for i in my_list:
    print(i, end=" ")

print("")
#%%
while True:
    print(my_list)
    break

#%%
totalsum = 0
for i in my_list:
    totalsum += i
print(totalsum)

n = 0
totalsum = 0
stop = len(my_list) - 1

while n <= stop:
    nr = my_list[n]
    totalsum += nr
    n += 1
print(totalsum)
