import random


def shuffle(input_string):
    temp_list = list(input_string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


def lower_case():
    return chr(random.randint(97, 122))


def upper_case():
    return chr(random.randint(65, 90))


def integer():
    return chr(random.randint(48, 57))


def special_chr():
    return chr(random.randint(33, 47))


def create_pass():
    temp_password = lower_case() + upper_case() + integer() + special_chr()
    password_len = random.randint(8, 16)
    while len(temp_password) < password_len:
        temp_password += random.choice([lower_case(), upper_case(), integer(), special_chr()])
    password = shuffle(temp_password)
    return password, len(temp_password)


passw, lentgh = create_pass()
print(f"Her er et tilfeldig generert sterkt passord med 8-16 tegn: {passw}")
print(f"I dette tilfellet {lentgh} tegn")
