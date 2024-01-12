import json

import lib.person_data_reader as p_reader

data = p_reader.read_persons('persons.csv', True)
data_2 = [dict(zip(data[0], p)) for p in data[1:]]
data_3 = json.dumps(data_2)

print(type(data_3))
print(data_3)
