from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} speaks meow!")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} speaks woof!")
