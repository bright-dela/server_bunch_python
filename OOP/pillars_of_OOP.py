# Inheritance
# Allows us to define a class that inherits all the methods and properties from another class.

# The class you inherit from is called the parent class or superclass

#  The class that inherits is the derived class or a subclass

# The super() function
# Make the child inherits all the methods and properties from it parent


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, firstname, lastname, course, student_id):
        super().__init__(firstname, lastname)
        self.course = course
        self.student_id = student_id

    def get_institution_name(self):
        print("I attend ALX.")


# Encapsulation


# Abtraction


# Polymorphism

# poly = many 
# morphism = form

#many forms


