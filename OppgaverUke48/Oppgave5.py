import random as rnd
from collections import deque

print('A) Skriv en funksjon som sjekker om en streng er et palindrom (leses likt baklengs som forlengs)')


def palindrome(prompt):
    if prompt.lower() == prompt[::-1].lower():
        return print(f'{prompt} er et palindrom.')
    else:
        return print(f'{prompt} er ikke et palindrom.')


palindrome(input('Skriv inn et ord: '))

print('B) Lag et program som genererer en tilfeldig fargekode i hex-format (f.eks. #1a2b3c). ')
hex_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', ]
hex_color = "#"

for i in range(6):
    hex_color += str(rnd.choice(hex_vals))


def colorize_text(text, hex_colorr):
    color_code = f'\033[38;2;{int(hex_colorr[1:3], 16)};{int(hex_colorr[3:5], 16)};{int(hex_colorr[5:], 16)}m'
    reset_code = '\033[0m'
    return f'{color_code}{text}{reset_code}'


text_to_colorize = f'Du fikk hex- verdien/fargekoden: {hex_color}'
colored_text = colorize_text(text_to_colorize, hex_color)
print(colored_text)

print('C) Skriv et program som leser inn en rekke tall fra brukeren og bruker en stabel (stack) for å lagre dem.'
      'Programmet skal deretter skrive ut tallene i motsatt rekkefølge. ')


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def read_numbers():
    numbers = []
    while True:
        try:
            number = input('Skriv inn et tall (avslutt med Enter uten tall): ')
            if not number:
                break
            numbers.append(float(number))
        except ValueError:
            print('Ugyldig tall. Prøv igjen.')

    return numbers


def main():
    number_stack = Stack()

    # Les inn tallene fra brukeren og legg dem på stabelen
    numbers = read_numbers()
    for number in numbers:
        number_stack.push(number)

    # Skriv ut tallene i motsatt rekkefølge ved å poppe dem fra stabelen
    print('Tallene i motsatt rekkefølge:')
    while not number_stack.is_empty():
        print(number_stack.pop())


if __name__ == "__main__":
    main()

print('D) Lag et program som leser inn en setning og bruker en kø (queue) for å skrive '
      'ut ordene i setningen i motsatt rekkefølge.')


# Funksjon for å lese inn en setning fra brukeren
def read_sentence():
    sentence = input('Skriv inn en setning: ')
    return sentence


# Funksjon for å omvende rekkefølgen av ord i en setning
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = deque(words[::-1])
    return reversed_words


# Funksjon for å skrive ut ordene i motsatt rekkefølge ved å bruke en kø (queue)
def print_reverse_order(reversed_words):
    print('Setningen med ord i motsatt rekkefølge:')
    while reversed_words:
        print(reversed_words.popleft())


# Hovedprogram
def main2():
    input_sentence = read_sentence()
    reversed_words = reverse_sentence(input_sentence)
    print_reverse_order(reversed_words)


if __name__ == "__main2__":
    main()
