class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Vehicle("Ford", "Mustang")       # Create a Car class
car2 = Vehicle("Audi", "A3")
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")     # Create a Plane class

for x in (car1, car2, boat1, plane1):
    print(x.brand, end=" ")
    print(x.model, end=" ")
    x.move()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name, p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name, "and I am", self.age, "years old.")


p1 = Person("John", 36)
p1.age = 40
p1.myfunc()
