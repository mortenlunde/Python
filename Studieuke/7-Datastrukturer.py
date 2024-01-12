import math


#%% 1. Lag en liste med de første 10 primtallene og skriv ut dem.
def primtall(tall):
    if tall <= 1:
        return False
    elif tall <= 3:
        return True
    elif tall % 2 == 0 or tall % 3 == 0:
        return False
    i = 5
    while i * i <= tall:
        if tall % i == 0 or tall % (i + 2) == 0:
            return False
        i += 6
    return True


primtall_list = []
sjekk_tall = 0  # Vi sjekker tall fra 0 og oppover
while len(primtall_list) < 10:
    if primtall(sjekk_tall):
        primtall_list.append(sjekk_tall)
    sjekk_tall += 1
print(primtall_list)


#%% 2. Lag en tuple med de første 10 partallene og skriv ut dem.
primtall_tuple = ()
sjekk_tall = 0
while len(primtall_tuple) < 10:
    if primtall(sjekk_tall):
        primtall_tuple += (sjekk_tall,)
    sjekk_tall += 1
print(primtall_tuple)


#%% 3. Lag en dictionary med 10 nøkkel-verdi-par der nøklene er
# tall fra 1 til 10 og verdiene er de kvadratiske røttene av nøklene.
kvad_dic = {}
for x in range(1, 11):
    kvad_dic[x] = round(math.sqrt(x), 2)
print(kvad_dic)


#%% 4. Lag et program som tar en liste med tall og returnerer en sortert versjon av listen.
random_liste = (2, 7, 22, 87, 1, 99, 222, 23, 150)
random_liste = sorted(random_liste)
print(random_liste)


#%% 5. Lag et program som tar en liste med strenger og returnerer en sortert
# versjon av listen basert på lengden av strengene.
def sjekk_lengde(tekst):
    return len(tekst)


random_string_list = ["Hei", "Morten", "Backend", "Programmering", "Best"]
random_string_list.sort(key=sjekk_lengde)
print(random_string_list)


#%% 6. Lag et program som tar en dictionary og returnerer en liste av nøklene sortert basert på verdiene.
opg_6_dict = {1: "En", 2: "To", 3: "Tre", 4: "Fire", 5: "Fem"}
opg_6_list = sorted(opg_6_dict.keys(), key=lambda k: opg_6_dict[k])
print(opg_6_list)


#%% 7. Lag et program som tar en liste med tall og returnerer en liste med de unike tallene fra den opprinnelige listen.
ikke_unik_liste = [1, 2, 3, 3, 8, 9, 0, 1, 4, 10, 8, 99, -5]
unik_liste = []
for u in ikke_unik_liste:
    if u not in unik_liste:
        unik_liste.append(u)
print(unik_liste)


#%% 8. Lag et program som tar en liste med tall og returnerer en tuple med den minste og største verdien i listen.
unik_tuple = min(unik_liste), max(unik_liste)
print(unik_tuple)


#%% 9. Lag et program som tar to lister og returnerer en liste med elementene som finnes i begge listene.
liste_1 = [1, 3, 4, 9, 0, 2, 7, 22]
liste_2 = [3, 88, 99, 1, 7, 10, 11, 21]
liste_tom = []
for g in liste_1:
    if g in liste_2:
        liste_tom.append(g)
print(liste_tom)


#%% 10. Lag et program som tar en liste med tall og returnerer en dictionary
# der nøklene er tallene og verdiene er frekvensen av hvert tall i listen.
num_dic = {}
for h in ikke_unik_liste:
    if h not in num_dic:
        num_dic[h] = ikke_unik_liste.count(h)
print(num_dic)
