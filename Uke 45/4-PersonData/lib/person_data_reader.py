import os


def read_persons(filename: str, include_header=False):
    if not os.path.exists(filename):
        return f"Filen '{filename}' eksisterer ikke."

    person_data_list = []
    with open(filename, "r", encoding="utf-8") as file_read:
        for idx, line in enumerate(file_read):
            if idx == 0 and not include_header:
                continue
            # lager en array med feltene fra linjen
            # split funksjonen gir en liste tilbake, men med str
            person_arr = line.rstrip("\n").split(",")

            if idx == 0 and include_header:
                person_data_list.append(person_arr)
                continue

            # 1. validering, sjekke at vi har 4 felter
            if not len(person_arr) == 4:
                print(f"Feil format på filen: linenr {idx} -> {line}")
                continue

            # person_arr = ["phnavn", "phetternavn", "age", "gender" ]
            first_name, last_name, age, gender = person_arr

            # 2. validering, sjekker at at vi har verdier i alle felt
            if not all([first_name, last_name, age, gender]):
                print(f"Feil i data, mangleer felter: linenr {idx}, {line}")
                continue

            # 3. Validering, sjekker at age er en int
            if not age.isdigit():
                print(f"Feil i data, age er ikke et tall: linenr {idx}, {line}")
                continue
            # 4. sjekker at kjønn er "kvinne" eller "Mann"
            if not gender.lower() in ["kvinne", "mann"]:
                print(f"Feil i data, kjønn stemmer ikke: linenr: {idx}, {line}")

            # Nå har vi gyldig  data på denne linjen
            # passe på å legge inn riktig datatype på alder
            person_data_list.append((first_name, last_name, int(age), gender))

    return person_data_list
