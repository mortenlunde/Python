print('A) Lag et program som ber brukeren om å skrive inn en setning. Programmet skal deretter telle antall ord i '
      'setningen og skrive ut dette tallet.')
user_sentance = input("Skriv en en setning med flere ord: ")
print(f'Antall ord i setningen din: {len(user_sentance.split(" "))}')

print('\nB) Modifiser programmet slik at det også teller antall vokaler og konsonanter i setningen.')
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø']
vowel_count = 0
consonant_count = 0
letter_count = 0
user_sentance_splitted = user_sentance.split()
new_sentence = ''
for word in user_sentance_splitted:
    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1
        elif letter == ' ':
            pass
        else:
            consonant_count += 1
        letter_count += 1
print(f'Antall bokstaver i setningen din: {letter_count}, antall vokaler: '
      f'{vowel_count} og antall konsonanter er {consonant_count}')

print('\nC) Lag et program som reverserer rekkefølgen av ordene i setningen innskrevet av brukeren.')
print(*user_sentance_splitted[::-1])

print('\nD) Skriv et program som finner det lengste ordet i setningen og skriver det ut.')
longest_word = max(user_sentance_splitted, key=len)
print(f'D) Det lengste ordet i setningen: {longest_word}')

print('\nE)Lag et program som krypterer setningen ved å bytte ut hver bokstav med den '
      'neste bokstaven i alfabetet (z blir til a).')


print('\nE) Lag et program som krypterer setningen ved å bytte ut hver bokstav med den '
      'neste bokstaven i alfabetet (z blir til a).')


def encrypt_letter(boks):
    if boks.isalpha():
        shifted_char = chr((ord(boks) - ord('a') + 1) % 26 + ord('a')) if letter.islower() else \
                       chr((ord(boks) - ord('A') + 1) % 26 + ord('A'))
        return shifted_char
    else:
        return boks


encrypted_sentence = ''.join([encrypt_letter(letter) for letter in user_sentance])
print(f'Kryptert setning: {encrypted_sentence}')
