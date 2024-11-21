listen = [2, 3, 4, 6, 7, 8]
str_av_listen = ""
for x in listen:
    str_av_listen += str(x)

with open("liste_med_tall.txt", "w") as fil:
    fil.write("\n".join(str_av_listen))

####

liste_som_str = "\n".join(map(str, listen))
print(liste_som_str)

with open("liste_med_tall2.txt", "w") as fil:
    fil.write(liste_som_str)