import os
from lib.func import calculate_result

while True:
    folder = os.path.join("Matteoppgaver")
    search_file = input('Skriv inn filnavn på filen du ønsker løsningsforslag på: ') + '.txt'
    solution_file = f'{search_file}-losningsforslag.txt'

    if os.path.exists(os.path.join(folder, search_file)):
        with open(os.path.join(folder, search_file), 'r') as f:
            lines = f.readlines()

        with open(os.path.join(folder, solution_file), 'w') as lf:
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
            lf.seek(0, os.SEEK_END)
            lf.truncate(lf.tell() - 1)

        print(f'Løsningsforslag lagt til i fil {solution_file}')
        break
    else:
        print('Denne filen eksisterer ikke.')
        continue
