class This:

    def __init__(self, a, b):
        self.a = a
    
    def method(self):
        print(self.a)

class That(This):
        
    def __init__(self, a, b):
        super().__init__(a)

    def method(self):
        print(self.a)


class Other(This):
    
    def __init__(self, a, b):
        a = 0
        self.a = 10

    def method(self):
        print(self.a)

class Other2(That):

    def __init__(self):
        print("Soy una piña")
        self.a = 0