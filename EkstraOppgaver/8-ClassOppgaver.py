# Oppgave 1
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Sete- kapasiteten til {self.name} er {capacity} passasjerer."


modelX = Vehicle("Model X", 240, 18)
print(modelX.max_speed, modelX.mileage)


# Oppgave 2
class Bus(Vehicle):
    pass


# Oppgave 3
merc = Bus("Mercedes Coach", 100, "200000")
print("Merke:", merc.name, "Maks hastighet:", merc.max_speed, "Kjørelengde:", merc.mileage)

# Oppgave 4
merc.seating_capacity(50)
print(merc.seating_capacity(60))


class Color(Vehicle):
    def __init__(self, name, max_speed, mileage, color="Hvit"):
        super().__init__(name, max_speed, mileage)
        Color.color = color


audi = Color("Audi A3", 240, 133337, "Hvit")

print(audi.name, audi.max_speed, audi.max_speed, audi.color)
