import random as rnd
import os


def create_task(x, y):
    operator = rnd.choice(['+', '-', '*', '/'])

    if operator == '+':
        return f"{x} + {y} = "
    elif operator == '-':
        return f"{x} - {y} = "
    elif operator == '*':
        return f"{x} * {y} = "
    elif operator == '/':
        while y == 0 or x % y != 0:
            x = rnd.randint(1, 100)
            y = rnd.randint(1, 100)
        return f"{x} / {y} = "


def calculate_result(expression):
    operators = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__floordiv__}
    operator = next((op for op in operators if op in expression), None)
    if operator:
        x, y = map(int, expression.split(operator))
        return operators[operator](x, y)
    return None


def clear_last_line(reader):
    reader.seek(0, os.SEEK_END)
    reader.truncate(reader.tell() - 1)
