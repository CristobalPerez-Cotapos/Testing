import unittest
from model import *
from parser import *
from metrics import *


class TestParser(unittest.TestCase):
    # Tests para la tarea 1
    # Deben agregar las clases y modificar los metodos necesarios
    # para que los siguientes tests compilen y pasen
    # usted puede agregar mas tests

    # Tests para el ejercicio 1
    def test_mn(self):
        ast1 = ModuloNode(NumberNode(5), NumberNode(2))
        ast2 = parser("(% 5 2)")
        self.assertEqual(ast1,ast2)

    def test_mn_eval(self):
        ast = parser("(% 5 2)")
        result = ast.eval()
        self.assertEqual(result,1)

    def test_mix_bin(self):
        ast = parser("(% (+ 35 15) (- 30 8))")
        result = ast.eval()
        self.assertEqual(result,6)

    def test_to_string_mn(self):
        ast1 = ModuloNode(AdditionNode(NumberNode(2), NumberNode(8)), SubtractionNode(NumberNode(7), NumberNode(4)))
        self.assertEqual(ast1.to_string(),"(% (+ 2 8) (- 7 4))")

    def test_to_string_mn2(self):
        ast1 = AdditionNode(ModuloNode(NumberNode(7),NumberNode(2)), ModuloNode(NumberNode(13), NumberNode(2)))
        self.assertEqual(ast1.to_string(),"(+ (% 7 2) (% 13 2))")

    def test_module_counter(self):
        visitor = ModuloOperatorCounter()
        ast = parser("(% (% 30 11) (% 65 8))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)

    def test_module_counter2(self):
        visitor = ModuloOperatorCounter()
        ast = parser("(% (+ 6 1) (% 8 5))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 2)

    #Tests para el ejercicio 2
    def test_pp(self):
        ast1 = PlusPlusNode(NumberNode(2))
        ast2 = parser("(++ 2)")
        self.assertEqual(ast1,ast2)

    def test_pp_eval(self):
        ast = parser("(++ 2)")
        result = ast.eval()
        self.assertEqual(result,3)
    
    def test_mm_eval(self):
        ast = parser("(-- 3)")
        result = ast.eval()
        self.assertEqual(result,2)
    
    def test_mix(self):
        ast = parser("(+ (++ 1) (++ 1))")
        result = ast.eval()
        self.assertEqual(result,4)
    
    def test_to_string2(self):
        ast1 = PlusPlusNode(MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast1.to_string(),"(++ (-- 2))")
    
    def test_to_string3(self):
        ast1 = AdditionNode(PlusPlusNode(NumberNode(1)),MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast1.to_string(),"(+ (++ 1) (-- 2))")
    
    def test_unary_counter(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(+ (+ (++ 1) (++ 1)) (- 2 (-- 3)))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)
    
    def test_unary_counter2(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(++ 1)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 1)


if __name__ == '__main__':
    unittest.main()
