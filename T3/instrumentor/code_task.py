from classInstrumentor import ClassProfiler

class Rectangle:

    def __init__(self, width, height):
        ClassProfiler.record('__init__', 3, 'Rectangle')
        self.width = width
        self.height = height

    def get_area(self):
        ClassProfiler.record('get_area', 7, 'Rectangle')
        return self.width * self.height

    def get_perimeter(self):
        ClassProfiler.record('get_perimeter', 10, 'Rectangle')
        return self.width * 2 + self.height * 2

    def set_width(self, width):
        ClassProfiler.record('set_width', 13, 'Rectangle')
        self.width = width

    def set_height(self, height):
        ClassProfiler.record('set_height', 16, 'Rectangle')
        self.height = height

    def __eq__(self, other):
        ClassProfiler.record('__eq__', 19, 'Rectangle')
        return self.width == other.width and self.height == other.height

def test_area():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, 'Incorrect area'

def test_perimeter():
    rectangle = Rectangle(5, 7)
    assert rectangle.get_perimeter() == 24, 'Incorrect perimeter'

def test_compare1():
    rectangle1 = Rectangle(2, 3)
    rectangle2 = Rectangle(5, 7)
    assert rectangle1 != rectangle2, 'Different rectangles'

def test_compare2():
    rectangle1 = Rectangle(2, 3)
    rectangle2 = Rectangle(5, 3)
    assert rectangle1 != rectangle2, 'Different rectangles'

def test_compare3():
    rectangle1 = Rectangle(2, 5)
    rectangle2 = Rectangle(2, 7)
    assert rectangle1 != rectangle2, 'Different rectangles'

def test_compare_equal():
    rectangle1 = Rectangle(2, 5)
    rectangle2 = Rectangle(2, 5)
    assert rectangle1 == rectangle2, 'Equal rectangles'
test_area()
test_perimeter()
test_compare1()
test_compare2()
test_compare3()
test_compare_equal()