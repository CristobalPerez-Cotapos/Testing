from model import *

# Modulo que contiene los visitors creados y cada uno computa una metrica

# Visitador que cuenta la cantidad de nodos de tipo NumberNode que existen en el arbol
class NumberCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_Number(self, node):
        self.counter = self.counter + 1

    def total(self):
        return self.counter


# Visitador que cuenta la cantidad de nodos de tipo AdditionNode que existen en el arbol
class AdditionCounter(Visitor):
    def __init__(self):
        self.counter = 0

    # Los nodos compuestos deben propagar la visita
    def visit_Addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)
        self.counter = self.counter + 1

    def total(self):
        return self.counter
