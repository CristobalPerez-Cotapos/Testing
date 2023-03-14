import unittest
from model import *
from parser import *
from metrics import *


class TestParser(unittest.TestCase):
    # Testing the parser
    def test_number(self):
        ast1 = NumberNode(27)
        ast2 = parser("27")
        self.assertEqual(ast1, ast2)

    def test_sum(self):
        ast1 = AdditionNode(NumberNode(2), NumberNode(3))
        ast2 = parser("(+ 2 3)")
        self.assertEqual(ast1, ast2)

    def test_subs(self):
        ast1 = SubtractionNode(NumberNode(34), NumberNode(27))
        ast2 = parser("(- 34 27)")
        self.assertEqual(ast1, ast2)

    def test_mix(self):
        ast1 = SubtractionNode(AdditionNode(NumberNode(289), NumberNode(1)), SubtractionNode(NumberNode(30), NumberNode(23)))
        ast2 = parser("(- (+ 289 1) (- 30 23))")
        self.assertEqual(ast1, ast2)

    def test_mix2(self):
        ast1 = AdditionNode(NumberNode(88), SubtractionNode(AdditionNode(NumberNode(912), NumberNode(208)), NumberNode(546)))
        ast2 = parser("(+ 88 (- (+ 912 208) 546))")
        self.assertEqual(ast1, ast2)

    # Testing eval
    def test_sum_eval(self):
        ast = parser("(+ 25 30)")
        result = ast.eval()
        self.assertEqual(result, 55)

    def test_subs_eval(self):    
        ast = parser("(- 912 28)")
        result = ast.eval()
        self.assertEqual(result, 884)

    def test_mix_eval(self):
        ast = parser("(- (+ 57 10) (- 48 20))")
        result = ast.eval()
        self.assertEqual(result, 39)

    # Testing to_string
    def test_to_string(self):
        ast1 = SubtractionNode(AdditionNode(NumberNode(2), NumberNode(1)), SubtractionNode(NumberNode(3), NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(- (+ 2 1) (- 3 2))")

    # testing visitor
    def test_number_counter(self):
        visitor = NumberCounter()
        ast = parser("(+ (+ 145 12) 2789)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)

    def test_addition_counter(self):
        visitor = AdditionCounter()
        ast = parser("(+ (+ 1 1) 2)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 2)


if __name__ == '__main__':
    unittest.main()
