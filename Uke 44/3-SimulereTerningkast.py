import random
from matplotlib import pyplot as plt

liste_terning_stat = [1, 2, 3, 4, 5, 6]
resultat = {ter_nr: 0 for ter_nr in liste_terning_stat}

while True:
    user_input = input("Hvor mange ganger ønsker du å kaste terningen? Svar: ")
    if user_input.isdigit():
        ant_kast = int(user_input)
        if ant_kast > 0:
            for _ in range(ant_kast):
                kast = random.choice(liste_terning_stat)
                resultat[kast] += 1

            x_verdier = [f"Enere ({resultat[1]})\n({resultat[1] / ant_kast:.0%})",
                         f"Toere ({resultat[2]})\n({resultat[2] / ant_kast:.0%})",
                         f"Treere ({resultat[3]})\n({resultat[3] / ant_kast:.0%})",
                         f"Firere ({resultat[4]})\n({resultat[4] / ant_kast:.0%})",
                         f"Femere ({resultat[5]})\n({resultat[5] / ant_kast:.0%})",
                         f"Seksere ({resultat[6]})\n({resultat[6] / ant_kast:.0%})"]

            counts = [resultat[ter_nr] for ter_nr in liste_terning_stat]

            plt.suptitle('Simulering av terningkast', fontsize=18, fontweight='bold')
            plt.xlabel("Terningkast", fontweight='bold')
            plt.ylabel(f"Antall kast ({ant_kast})", fontweight='bold')

            plt.bar(x_verdier, counts)
            plt.xticks(fontsize=8)
            plt.show()
        else:
            print("Antallet kast må være større enn null.")
    else:
        print("Du må skrive inn et gyldig tall.")

    exit_choice = input("Vil du fortsette? (ja/nei): ")
    if exit_choice.lower() != "ja":
        break
