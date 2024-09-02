




# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def __add__(self, other):
#         return self.area() + other.area()

# class Square(Shape):
#     def __init__(self, side):
#         super().__init__('Square')
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# square = Square(5)
# circle = Circle(7)

# # Printing areas of Square and Circle using polymorphism
# print(f"Area of {square.name}:", square.area())
# print(f"Area of {circle.name}:", circle.area())

# # Adding areas of Square and Circle using operator overloading
# total_area = square + circle
# print("Total area:", total_area)



class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __add__(self, other):
        if isinstance(other, Person):
            return f"{self.name} and {other.name} are friends"
        else:
            raise TypeError("Can only add Person objects")

aryan = Person("Aryan")
vihaan = Person("Vihaan")
zayn = Person("Zayn")

# Using polymorphism to print information 
print(aryan)
print(vihaan)
print(zayn)

# Using operator overloading to show friendship
print(aryan + vihaan)
print(vihaan + zayn)

