# 7.Create a base class named Person that has the following attributes: name, age, and address. It should also have a method called get_info() that returns a string with the person's name, age, and address. Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods specific to each role.

@dataclass
class Address:
     street:str
     city:str
     country:str
     house_number:int

     def get_info(self) -> str:
         return self.street + " " + str(self.house_number) + ", " + self.city + ", " + self.country

@dataclass
class Person:
     name:str
     age:int
     address:Address

     def get_info(self):
         return "Name : " + self.name + ";Age : " + str(self.age) + ";Address : " + self.address.get_info()

@dataclass
class Student(Person):
      study_field:str

@dataclass
class Teacher(Person):
     subject:str