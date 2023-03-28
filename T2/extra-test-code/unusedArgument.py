
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

def funcion(x, z):
    a = z
    return a
