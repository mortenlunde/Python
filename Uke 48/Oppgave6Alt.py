import random as rnd
import os
from typing import List


def read_pos_int(prompt: str) -> int:
    _nr = 0
    while _nr <= 0:
        str_nr = input(prompt)
        try:
            _nr = int(str_nr)
            if _nr <= 0:
                print('For lavt tall, velg minimum 1.')
        except ValueError as err:
            print(f'Du må skrive et gydig heltall. {err}')
            continue
    return _nr


def create_excercises(ant_oppgaver: int,
                      operators: tuple,
                      min_value: int = 1,
                      max_value: int = 100) -> List[str]:
    _tasks = []
    for i in range(ant_oppgaver):
        tall_a = rnd.randint(min_value, max_value)
        tall_b = rnd.randint(min_value, max_value)
        op = rnd.choice(operators)
        while op == '/' and tall_b == 0:
            tall_b = rnd.randint(min_value, max_value)

        _tasks.append(f'{i+1}: {tall_a} {op} {tall_b} = ')
    return _tasks


def clear_last_line(reader):
    reader.seek(0, os.SEEK_END)
    reader.truncate(reader.tell() - 1)


def save_to_file(filename: str, excercises: List[str]) -> str:
    try:
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                for excercise in excercises:
                    f.write(f'{excercise}\n')
                clear_last_line(f)
            print(f'Filen {filename}.txt er opprettet med suksess.')
        else:
            print(f'Filen {filename}.txt finnes allerede')
            new_filename = input('Hva ønsker du filen skal kalles: ') + '.txt'
            return save_to_file(new_filename, excercises)
    except IOError as ioerr:
        print(ioerr)


if __name__ == '__main__':
    _operators = ('+', '-', '*', '/')
    _antall_oppgaver = read_pos_int('Hvor mange oppgaver skal vi lage: ')
    _excercises = create_excercises(_antall_oppgaver, _operators)

    _save_to_file = input('Hva ønsker du filen skal kalles: ') + '.txt'
    save_to_file(_save_to_file, _excercises)
