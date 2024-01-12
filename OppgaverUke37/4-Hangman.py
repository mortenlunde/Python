# Hangman av Morten Lunde
import sys
import os


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def draw_hangman(feilforsok, antallforsok):
    hangman_stages = [
        """
           _______
          |       |
          |       
          |       
          |       
          |
        """,
        """
           _______
          |       |
          |       O
          |       
          |       
          |
        """,
        """
           _______
          |       |
          |       O
          |       |
          |       
          |
        """,
        """
           _______
          |       |
          |       O
          |      /|
          |       
          |
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |       
          |
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      /
          |
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
          |
        """
    ]

    max_stage = len(hangman_stages) - 1
    first_stage = int(feilforsok / antallforsok * max_stage)

    if first_stage <= max_stage:
        print(hangman_stages[first_stage])


# Input av valgfritt ord og antall forsøk
gjett_ord = input("Tast inn et ord vi skal gjette på: ").lower()
antall_forsok = int(input("Tast inn antall ugyldige forsøk spiller har: "))
feil_forsok = 0
ferdig_gjettet_ord = set()

# Skjul det vi har tastet inn slik at ordet blir usynlig for den som skal gjette
clear_console()

skjult_ord = (len(gjett_ord) * "_ ")
print(f"Ordet du skal gjette på er: {skjult_ord}, og du har {antall_forsok} forsøk.")

# ------------
# Spill- løkke
# ------------

while antall_forsok != feil_forsok:
    skjuld_ord_vis = ''.join([letter if letter in ferdig_gjettet_ord else '_' for letter in gjett_ord])
    print(f"Ordet så langt: {skjuld_ord_vis}")

    gjett_bokstav = input("Gjett en bokstav i ordet: ".lower())

    if len(gjett_bokstav) != 1 or not gjett_bokstav.isalpha():
        print("Du kan bare gjette på en bokstav av gangen, og du kan ikke gjette tall. Prøv igjen.")
        continue

    if gjett_bokstav in ferdig_gjettet_ord:
        print("Du har allerede gjettet denne bokstav. Prøv igjen.")
        ferdig_gjettet_ord.add(gjett_bokstav)
        continue

    if gjett_bokstav in gjett_ord:
        print("Du gjettet en riktig bokstav.")
        ferdig_gjettet_ord.add(gjett_bokstav)
    else:
        print("Denne bokstaven er ikke i ordet. Prøv igjen.")
        ferdig_gjettet_ord.add(gjett_bokstav)
        feil_forsok += 1
        draw_hangman(feil_forsok, antall_forsok)
    if all(letter in ferdig_gjettet_ord for letter in gjett_ord):
        print(f"Du vant! Riktig ord var: ´{gjett_ord.capitalize()}´")
        break
    elif antall_forsok == feil_forsok:
        print(f"Du tapte. Du har 0 forsøk igjen. Ordet var ´{gjett_ord.capitalize()}´.")
        break
