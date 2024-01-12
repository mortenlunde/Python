import random as rnd
import os
from lib.func import create_task, calculate_result, clear_last_line

print('Velkommen til dette programmet for å lage matteoppgaver.')

while True:
    folder = os.path.join("Matteoppgaver")
    choice = input('Skriv inn ønsket operasjon. (1) Lag oppgaver, (2) Få løsningsforlag (3) Avslutt program: ')

    if choice == '1':
        create_file = input('Skriv inn navn du ønsker på filen: ') + '.txt'

        try:
            num_of_tasks = int(input('Skriv inn antall oppgavestykker du ønsker: '))
        except ValueError:
            print("Du må skrive et gyldig heltall.")
            continue

        if not os.path.exists(folder):
            os.mkdir(folder)

        if not os.path.isfile(os.path.join(folder, create_file)):
            with open(os.path.join(folder, create_file), "w", encoding="utf-8") as f:
                print(f"Opprettet fil: {create_file}")
                for i in range(1, num_of_tasks + 1):
                    number = rnd.randint(1, 100)
                    number_2 = rnd.randint(1, 100)
                    f.write(f"{i}: {create_task(number, number_2)}\n")

                clear_last_line(f)

        else:
            print(f"Filen {create_file} finnes allerede")
            continue

    elif choice == '2':
        search_file = input('Skriv inn filnavn på filen du ønsker løsningsforslag på: ') + '.txt'
        solution_file = os.path.join(folder, f'{search_file[:-4]}-losningsforslag.txt')

        if os.path.exists(os.path.join(folder, search_file)):
            with open(os.path.join(folder, search_file), 'r') as f:
                lines = f.readlines()

            with open(solution_file, 'w') as lf:
                updated_lines = []
                for line in lines:
                    parts = line.split(':')
                    if len(parts) == 2:
                        task_info = parts[1].strip().split('=')
                        if len(task_info) == 2:
                            expression = task_info[0].strip()
                            result = calculate_result(expression)
                            updated_lines.append(f"{parts[0]}: {expression} = {result}\n")
                        else:
                            updated_lines.append(line)
                    else:
                        updated_lines.append(line)

                lf.writelines(updated_lines)

                clear_last_line(lf)

            print(f'Løsningsforslag opprettet i fil {solution_file[14:]}')
        else:
            print('Denne filen eksisterer ikke.')
            continue

    elif choice == '3':
        exit()

    else:
        print('Ugyldig menyvalg. Prøv igjen.')
        continue
