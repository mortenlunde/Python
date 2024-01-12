import os
from typing import List, Tuple
from Oppgave6Alt import clear_last_line

math_functions = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}


def read_excercises_from_file(filename: str) -> None | List[Tuple[str, int, str, int, str]]:
    if not os.path.isfile(filename):
        print(f'Finner ikke filen {filename}.txt')
        return None

    _results = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                _values = line.split()
                opgnr, a, op, b, eq = _values

                if not a.isdigit() or not b.isdigit():
                    print('Har ikke fått inn tallverdier.')
                    continue

                _results.append((opgnr, int(a), op, int(b), eq))
        return _results

    except FileNotFoundError as e:
        print(e)
    except IOError as ioe:
        print(ioe)
    except ValueError as ve:
        print(ve)
    except Exception as ee:
        print(ee)


def solve_excercises(excercises: List[Tuple[str, int, str, int, str]]) -> List[str]:
    _exc_results = []
    for oppg, a, op, b, eq in excercises:
        if op not in math_functions:
            print(f'Støtter ikke operator {op}')
            continue

        svar = math_functions[op](a, b)
        if isinstance(svar, float):
            svar = round(svar, 2)
        result = f'{oppg} {a} {op} {b} {eq} {svar}\n'
        _exc_results.append(result)
    return _exc_results


if __name__ == '__main__':
    chose_file = input('Hvilken fil ønsker du å få løsninger på: ') + '.txt'
    solution_file = f'{chose_file[:-4]}-løsning.txt'
    try:
        exercises = read_excercises_from_file(chose_file)
        solutions = solve_excercises(exercises)
        with open(solution_file, 'w') as fw:
            for solution in solutions:
                fw.write(solution)
            clear_last_line(fw)

        print(f'Fil {solution_file} er opprettet med suksess.')
    except FileNotFoundError as fe:
        print('Fil ikke funnet')
