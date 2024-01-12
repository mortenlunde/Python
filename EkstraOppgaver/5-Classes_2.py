class Bil:
    def __init__(self, merke, modell, aarsmodell, kjoerelengde=0):
        self.merke = merke
        self.modell = modell
        self.aarsmodell = aarsmodell
        self.kjoerelengde = kjoerelengde
        self.fullmodell = merke + " " + modell

    def mil(self):
        return "{} har kjørt {} mil".format(self.fullmodell, self.kjoerelengde)

    def full_info(self):
        return "{} {} {} {}".format(self.aarsmodell, self.merke, self.modell, self.kjoerelengde)


bil_1 = Bil("Audi", "A3", 2017, 23456)
bil_2 = Bil("BMW", "M3", 2023)
for x in (bil_1, bil_2):
    print(x.aarsmodell, end=" ")
    print(x.merke, end=" ")
    print(x.modell, end=" ")
    print(x.kjoerelengde, end="\n")
print("")
print(Bil.mil(bil_1))
print(Bil.mil(bil_2))
