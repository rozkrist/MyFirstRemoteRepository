# 6.Create a base class named Vehicle that has the following attributes: make, model, and year. It should also have a method called get_info() that returns a string with the vehicle's make, model, and year. Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle.

from dataclasses import dataclass

@dataclass
class Vehicle:
     make:str
     model:str
     year:int
    
     def get_info(self):
         return "Make : " + self.make + ", Model : " + self.model + ", Year : " + str(self.year)
    

@dataclass
class Car(Vehicle):
     number_of_doors:int

@dataclass
class Truck(Vehicle):
     width:float
     max_width:float

     def max_cargo_width(self):
         return self.max_width - self.width

car = Car("Toyota","Rav4",2020,4)
print(car)

truck = Truck("BMW","E61",2020,10000,15000)
print(truck.max_cargo_width())
