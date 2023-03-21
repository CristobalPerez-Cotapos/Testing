
class Person:

    def fullName(self):
        return self.firstName + self.lastName
 

class Fruit:
    def __init__(self, name, vitamins):
        self.name = name
        self.vitamins = vitamins

    def to_string(self, name):
        print(self.name + "with vitamins " + self.vitamins)