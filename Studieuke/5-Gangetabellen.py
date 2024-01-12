#%% 1. Lag et program som skriver ut gangetabellen slik som du ser under.
for g in range(1, 11):
    for g2 in range(1, 11):
        result = g * g2
        print(f"{g}x{g2} = {result:2}", end="\t")
    print()
