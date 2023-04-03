# 4.Create a class named Person that has the following attributes: name, age, and address. It should also have a method called get_info() that returns a string with the person's name, age, and address.

class Person:
    def __init__(self, name, age, address):
          self.name = name
          self.age = age
          self.address = address

   
    def get_info(self):
         return f'Persons name is {self.name}, he/she is {self.age} years old and lives in {self.address}'

person1 = Person("Peter Green", 24, "Wisdom street 14, Texas, US")
person2 = Person("Anna Smith",56, "Silent street 45,Nashville, US")

print(person1.get_info())
print(person2.get_info())

