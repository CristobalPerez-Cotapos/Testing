def example1(x):
    a = 2
    b = 7
    return x + a * b


class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        eval("2+2")

    def somethig(self):
        if True:
            print("something")
