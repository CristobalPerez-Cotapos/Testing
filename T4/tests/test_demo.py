from src.clock_factory import *
from unittest import TestCase

"""
 Este archivo contiene un test demo que la unica funcion es ejecutar metodos
 del ClockFactory para probar la libreria de coverage.
 Tienen que remplazar o eliminar este test cuando desarrollen su tarea.
"""


class TestDemo(TestCase):
    def test_demo(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        for i in range(100):
            clock.increment()
            print(clock.str())