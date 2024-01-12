class Bankkonto:
    def __init__(self, kontonummer, balanse=0):
        self.kontonummer = kontonummer
        self.balanse = balanse

    def innskudd(self, belop):
        self.balanse += belop

    def uttak(self, belop):
        self.balanse -= belop


konto_1 = Bankkonto("9250.15.47100", 23539)
konto_2 = Bankkonto("9320.00.29922", 115680)

Bankkonto.innskudd(konto_1, 500)
print(konto_1.kontonummer, konto_1.balanse)

Bankkonto.uttak(konto_2, 3000)
print(konto_2.kontonummer, konto_2.balanse)
