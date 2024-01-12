import random as rnd
import string

print('A) Lag et program som genererer en tilfeldig passordstreng. Passordet skal inneholde minst 8 tegn, '
      'inkludert minst en stor bokstav, \nen liten bokstav, et tall og et spesialtegn. ')

lowercase_letters = string.ascii_lowercase
lowercase_letters += 'æøå'
uppercase_letters = string.ascii_uppercase
uppercase_letters += 'ÆØÅ'
digits = string.digits
special_characters = '!@#$%^&*()_-+=<>?/.'
all_characters = lowercase_letters + uppercase_letters + digits + special_characters

generated_password = [
    rnd.choice(lowercase_letters),
    rnd.choice(uppercase_letters),
    rnd.choice(digits),
    rnd.choice(special_characters)
]

password_length = rnd.randint(1, 20)
for _ in range(password_length - 4):
    generated_password.append(rnd.choice(all_characters))

rnd.shuffle(generated_password)
generated_password_str = ''.join(generated_password)

print(f'Autogenerert passord: {generated_password_str}')


print('\nB)Skriv et program som sjekker om et gitt passord oppfyller kravene nevnt i oppgave A. ')


def is_valid_password(password):
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)

    return has_lowercase and has_uppercase and has_digit and has_special and len(password) >= 8


if is_valid_password(generated_password_str):
    print('Ditt passord er sikkert nok.')
else:
    print('Ditt passord er ikke sikkert nok.')
