# What is OOP
# OOP stands for Object-Oriented Programming.

# Advantages of OOP

# 1.Provides a clear structure to programs
# 2.Makes code easier to maintain, reuse, and debug
# 3.Helps keep your code DRY (Don't Repeat Yourself)
# 4.Allows you to build reusable applications with  less code

# What are Classes and Objects?

# Classes and objects are the two core concepts in object-oriented programming.

# A class defines what an object should look like, and an object is created based on that class.

# When you create an object from a class, it inherits all the variables and functions defined inside that class.


# Create a Class

# To create a class, use the keyword class follow by the class name.

# Any function defined inside a class is called a method.


class Circle:
    pi = 3.143

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        """
        Return the area of the circle.
        """
        return (self.radius**2) * Circle.pi

    def get_circumference(self):
        """
        Returns the circumference of the circle.
        """
        return 2 * Circle.pi * self.radius

    def __str__(self) -> str:
        return f"Circle with area of {self.get_area()} and circumference of {self.get_circumference()}"


class Square:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        """
        Returns the area of the square.
        """
        return self.length * 2

    def get_perimeter(self):
        """
        Returns the perimeter of the square.
        """
        return 4 * self.length

    def __str__(self) -> str:
        return f"Square with area of {self.get_area()} and perimeter of {self.get_perimeter()}"


if __name__ == "__main__":
    # Create Object

    # Now we can use the class name to create objects.

    circle1 = Circle(radius=5)
    print("Area:", circle1.get_area())
    print("Circumference:", circle1.get_circumference())
    print("Pi:", circle1.pi)

    print("")

    circle2 = Circle(radius=10)
    print("Area:", circle2.get_area())
    print("Circumference:", circle2.get_circumference())
    print("Pi:", circle2.pi)


# Special methods or Magic methods or Dunder Methods
# The __init__() Method

# All classes have a method called __init__(), which is always executed when the class is being initiated.

# Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created

# Note: The __init__() method is called automatically every time the class is being used to create a new object.


# Create Methods

# You can create your own methods inside objects. Methods in objects are functions that belong to the object.


# The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
