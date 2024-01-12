import random
import os
import sys

kort_farge = ["♥ Hjerter", "♠ Spar", "♣ Kløver", "♦ Ruter"]
kort_verdi = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dronning", "Konge", "Ess"]
kortstokk = [{'verdi': verdi, 'farge': farge} for verdi in kort_verdi for farge in kort_farge]


def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def kalkuler_verdi(hand):
    verdi_tot = 0
    ess = 0
    kort_tekst = []

    for kort in hand:
        verdi = kort['verdi']
        farge = kort['farge']
        if verdi in ["Knekt", "Dronning", "Konge"]:
            verdi_tot += 10
        elif verdi == "Ess":
            verdi_tot += 11
            ess += 1
        else:
            verdi_tot += int(verdi)
        kort_tekst.append(f"{farge} {verdi}")

    while verdi_tot > 21 and ess > 0:
        verdi_tot -= 10
        ess -= 1

    return verdi_tot, kort_tekst


def spill():
    spiller_hand = [kortstokk.pop(random.randint(0, len(kortstokk) - 1)),
                    kortstokk.pop(random.randint(0, len(kortstokk) - 1))]
    dealer_hand = [kortstokk.pop(random.randint(0, len(kortstokk) - 1)),
                   kortstokk.pop(random.randint(0, len(kortstokk) - 1))]

    print("Velkommen til en runde med Blackjack.\n")

    while True:
        print("Dette er dine kort:")
        spiller_verdi, spiller_kort = kalkuler_verdi(spiller_hand)
        print(" ".join(spiller_kort))
        print(f"Din verdi er nå: {spiller_verdi}")

        if spiller_verdi == 21:
            print("Blackjack - du vant!")
            break
        elif spiller_verdi > 21:
            print("Du fikk over 21 poeng, du taper.")
            break

        hit = input("Vil du trekke et nytt kort? (j/n)").lower()
        if hit == "j":
            nytt_kort = kortstokk.pop(random.randint(0, len(kortstokk) - 1))
            spiller_hand.append(nytt_kort)
        elif hit == "n":
            break
        else:
            print("Du må velge 'j' eller 'n'")

    if spiller_verdi <= 21:
        while kalkuler_verdi(dealer_hand)[0] < 17:
            dealer_hand.append(kortstokk.pop(random.randint(0, len(kortstokk) - 1)))

        dealer_verdi, dealer_kort = kalkuler_verdi(dealer_hand)
        print("\nDealer sine kort:")
        print(" ".join(dealer_kort))
        print(f"Dealer sin verdi: {dealer_verdi}")

        if dealer_verdi > 21 or spiller_verdi == 21 or (21 >= spiller_verdi > dealer_verdi):
            print("Spiller vinner!")
        elif dealer_verdi == spiller_verdi:
            print("Uavgjort, ingen vinner.")
        else:
            print("Dealer vinner.")
        print()

while True:
    spill()
    if input("\nVil du spille en ny runde (j/n)? ") == "j":
        clear_console()
        continue
    else:
        break
