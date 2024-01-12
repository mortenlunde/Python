#%% 1. Skriv ut tallene fra 1 til 100 ved hjelp av en for- løkke.
for i in range(1, 101):
    print(i, end=" ")
print("\n")

#%% 2. Skriv ut alle partall fra 0 til 100 ved hjelp av en for- løkke.
for o in range(0, 101, 2):
    print(o, end=" ")
print("\n")

#%% 3. Skriv ut alle oddetall fra 1 til 99 ved hjelp av en for- løkke.
for p in range(1, 100, 2):
    print(p, end=" ")
print("\n")

#%% 4. Lag en multiplikasjonstabell ved hjelp av en for- løkke.
for g in range(1, 11):
    for g2 in range(1, 11):
        print(f"{g}x{g2} = {g * g2}")
print("")

#%% 5. Skriv et program som regner ut summen av tallene fra 1 til n ved hjelp av en for- løkke.
start_n = 0
stop_n = 101    # Skriv inn ønsket tall her
for n in range(start_n, stop_n):
    start_n += n
print(start_n, "\n")

#%% 6. Skriv et program som regner ut produktet av tallene fra 1 til n ved hjelp av en for- løkke.
start_g = 1
stop_g = 5    # Skriv inn ønsket tall her
for g in range(start_g, stop_g):
    start_g *= g
print(start_g, "\n")

#%% 7. Bruk en for- løkke til å beregne gjennomsnittet av en liste med tall.
num_list = [2, 4, 6, 8, 10]
avg = 0
for a in range(len(num_list)):
    avg += num_list[a]
avg = avg / len(num_list)
print(avg, "\n")

#%% 8. Bruk en for- løkke til å finne det største tallet i en liste.
num_list_max = [2, 20, 6, 22, 10]
max_num = 0
for x in range(len(num_list_max)):
    if num_list_max[x] > max_num:
        max_num = num_list_max[x]
print(f"Største tallet i listen er {max_num} \n")

#%% 9. Bruk en for- løkke til å finne det minste tallet i en liste.
num_list_min = [2, 20, 6, 8, 10, 1, 7, 9]
min_num = num_list_min[0]
for y in range(len(num_list_min)):
    if num_list_min[y] < min_num:
        min_num = num_list_min[y]
print(f"Minste tallet i listen er {min_num} \n")

#%% 10. Bruk en for- løkke til å finne summen av kvadratene av tallene fra 1 til n.
n = 10  # Velg et tall
kvad_sum = 0

for i in range(1, n + 1):
    kvadrat = i * i
    kvad_sum += kvadrat

print("Summen av kvadratene fra 1 til", n, "er:", kvad_sum)
