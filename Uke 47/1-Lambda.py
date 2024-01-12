#%% Lambda
def add(x, y):
    return x+y


print(add(5, 4))

add_2 = lambda x, y: x+y
print(add_2(5, 4))
print((lambda a, b: a+b)(2, 3))


def sort_dict_age(d: dict):
    return d['age']


def sort_dict_name(d: dict):
    return d['name']


list_dicts = [
    {'name': 'Vegard', 'age': 50},
    {'name': 'Tor', 'age': 22},
    {'name': 'Siv', 'age': 30},
    {'name': 'Anne', 'age': 30},
    {'name': 'Beate', 'age': 66}
]

print(list_dicts)
l_sorted_age = sorted(list_dicts, key=sort_dict_age)
l_sorted_age_lambda = sorted(list_dicts, key=lambda d: d['age'])
l_sorted_name = sorted(list_dicts, key=sort_dict_name)
l_sorted_name_lambda = sorted(list_dicts, key=lambda d: d['name'])

print(l_sorted_age)
print(l_sorted_age_lambda)
print(l_sorted_name)
print(l_sorted_name_lambda)
