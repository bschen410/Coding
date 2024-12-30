class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        return f"The car is driving at {self.speed} km/h"

    def __add__(*other):
        return sum(obj.speed for obj in other)


test = Car("Toyota", 100)
tes2 = Car("BMW", 200)
test3 = Car("Audi", 300)
print(test + tes2 + test3)
