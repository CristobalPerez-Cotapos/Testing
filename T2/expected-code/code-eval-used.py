literal_eval("2")

def example2():
    literal_eval("2+2")

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        literal_eval("[1, 2, 3]")

    def somethig(self):
        if True:
            print("something")


