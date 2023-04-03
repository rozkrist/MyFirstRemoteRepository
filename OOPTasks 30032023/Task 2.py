# 2.Create a class named Rectangle that has the following attributes: width and height. It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively.

class Rectangle:
     def __init__(self, width, height):
         self.width = width
         self.height = height

     def area(self):
         return self.width * self.height

     def perimeter(self):
         return (self.width*2)+(self.height*2)

rectangle1= Rectangle(5,8)
rectangle2= Rectangle(1,6)

print(f'The perimeter of rectangle is {rectangle2.perimeter()}')

print(f'The area of Rectangle 1 is {rect1.area()}')
print(f'The perimeter of Rectangle 2 is {rect2.perimeter()}')