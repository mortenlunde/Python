import os
import sys

FILE = "persons.csv"


def read_persons(filename: str):
    if not os.path.exists(filename):
        return f"Filen '{filename}' eksisterer ikke."

    person_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if idx == 0:
                continue

            persons_arr = line.rstrip('\n').split(',')

            if not len(persons_arr) == 4:
                print(f"Feil formot i filen: {idx+1} - {line}")
                continue

            first_name, last_name, age, gender = persons_arr

            if not all([first_name, last_name, age, gender]):
                print(f"Feil i data, mangler felter. Linjenummer {idx} - linje {line}")
                continue

            if not age.isdigit():
                print(f"Feil i alder- felt. Linjenummer {idx} - {line}")
                continue

            if not gender.lower() in ["mann", "kvinne"]:
                print(f"Feil i kjønn- feltet. Linjenummer {idx} - {line}")
                continue

            person_list.append((first_name, last_name, int(age), gender))

    return person_list


results = read_persons(FILE)
if isinstance(results, str):
    print(f"Avslutter. Årsak: {results}")
    sys.exit()

print(results)

for r in results:
    print(r)


def get_age_by_gender(person_list: list, gender: str) -> int:
    tot_age = 0
    for person in person_list:
        if person[3] == gender:
            tot_age += person[2]

    return tot_age


def get_gender_count(person_list: list, gender: str) -> int:
    ant_pers = 0
    for p in person_list:
        if p[3] == gender:
            ant_pers += 1

    return ant_pers


age_men = get_age_by_gender(results, "Mann")
age_men_2 = sum([p[2] for p in results if p[3] == "Mann"])

age_woman = get_age_by_gender(results, "Kvinne")

print("Total alder menn: ", age_men)
print("Total alder menn: ", age_men_2)
print("Total alder kvinner: ", age_woman)

tot_men = get_gender_count(results, "Mann")
tot_kvinn = get_gender_count(results, "Kvinne")
print("Totalt antall menn: ", tot_men)
print("Totakt antall kvinner", tot_kvinn)
