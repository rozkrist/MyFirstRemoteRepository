# 1.Create a class named Car that has the following attributes: make, model, and year. It should also have a method called get_info() that returns a string with the car's make, model, and year.

class Car:
     def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         
     def get_info(self):
       return str(self.make) + " "+ str(self.model) + " "+ str(self.year)

car1=Car("BMW", "X5", 2022)
car2=Car("Toyota", "RAV4", 2015)
car3=Car("MiniCooper", "Clubman", 2018)

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())