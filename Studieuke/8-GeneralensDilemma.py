def sjekk_input(innsats, maks_soldater):
    while True:
        try:
            innsats = int(input(innsats))
            if 0 <= innsats <= maks_soldater:
                return innsats
            else:
                print(f"Du må skrive inn et tall mellom 0 og {maks_soldater}.")
        except ValueError:
            print("Dette er ikke et gyldig tall, prøv igjen.")


def spill():
    spiller_1 = 100  # Soldater
    spiller_2 = 100  # Soldater
    spiller_1_wins = 0
    spiller_2_wins = 0
    omgang = 1

    print("Velkommen til spillet 'Generalens Dilemma")
    print("Regler: Hver spiller har 100 soldater. I opp til 5 ganger skal du sende ut X antall soldater. "
          "Den med flest soldater vinner runden.")
    spiller_1_navn = input("Velg navn på Spiller 1: ").capitalize()
    spiller_2_navn = input("Velg navn på spiller 2: ").capitalize()

    while spiller_1_wins < 3 and spiller_2_wins < 3 and omgang < 5:
        spiller_1_innsats = sjekk_input(f"{spiller_1_navn}: Hvor mange soldater "
                                        f"ønsker du å sende inn i runde {omgang}? ", spiller_1)
        spiller_1 -= spiller_1_innsats
        spiller_2_innsats = sjekk_input(f"{spiller_2_navn}: Hvor mange soldater "
                                        f"ønsker du å sende inn i runde {omgang}? ", spiller_2)
        spiller_2 -= spiller_2_innsats

        omgang += 1
        if spiller_1_innsats > spiller_2_innsats:
            print(f"{spiller_1_navn} vinner denne runden.")
            spiller_1_wins += 1
        elif spiller_1_innsats < spiller_2_innsats:
            print(f"{spiller_2_navn} vinner denne runden.")
            spiller_2_wins += 1
        else:
            print("Uavgjort, ingen vinnere.")

        if spiller_1 <= 0:
            print(f"{spiller_1_navn} har brukt opp alle sine soldater- {spiller_2_navn} vinner resten av rundene.")
            while omgang <= 5:
                omgang += 1
                spiller_2_wins += 1
        elif spiller_2 <= 0:
            print(f"{spiller_2_navn} har brukt opp alle sine soldater")
            while omgang <= 5:
                omgang += 1
                spiller_1_wins += 1

        print(f"Soldater igjen: {spiller_1_navn} - {spiller_1} \t {spiller_2_navn} - {spiller_2}")
        print(f"Antall seiere: {spiller_1_navn} - {spiller_1_wins} \t {spiller_2_navn} - {spiller_2_wins}")
    if spiller_1_wins > spiller_2_wins:
        print(f"{spiller_1_navn} vinner slaget med {spiller_1_wins} seiere "
              f"mot {spiller_2_navn}'s {spiller_2_wins} seiere. Gratulerer!")
    elif spiller_1_wins < spiller_2_wins:
        print(
            f"{spiller_2_navn} vinner slaget med {spiller_2_wins} seiere "
            f"mot {spiller_1_navn}'s {spiller_1_wins} seiere. Gratulerer!")
    else:
        print(f"{spiller_1_navn} og {spiller_2_navn} fikk like mange seiere. Krigen har derfor ingen vinnere.")


while True:
    spill()
    if input("Vil du avslutte spillet (j/n)? ") == "j":
        break
    else:
        continue
