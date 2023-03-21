def example1(a, b, c, d, e, f, x, y, z):
    first = [a, b, c]
    second = [d, e, f]
    third = [x, y, z]

    return [first, second, third]

def example2(x, y):
    return x + y


class Person:
    def __init__(self, firstName, lastName, birthdate, nationality, address, city, country):
        self.firstName = firstName
        self.lastName = lastName
        self.birthdate = birthdate
        self.nationality = nationality
        self.address = address
        self.city = city
        self.country = country

    def fullName(self):
        return self.firstName + self.lastName
