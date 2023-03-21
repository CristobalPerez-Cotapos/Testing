import unittest
from rules import *
from rewriter import *

"""
Tests para las reglas y transformaciones creadas en la tarea
IMPORTANTE: Si usted implemento la tarea en un nuevo archivo dentro del folder rules o rewriter
no olvide modificar el __init__.py de rules y rewriter para importar los archivos necesarios para su tarea.
Caso contrario importe lo necesario en este archivo
"""

class TestWarnings(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    """ Nombre: test_long_variable_name
        Codigo a ser analizado: test-code/code-long-variable-name.py
        Descripcion: Test para evaluar LongVariableNameRule considerando los siguientes escenarios:
        - Linea 3: Uso de variable de nombre largo : mysuperlistofone
        - Linea 4: Uso de variable de nombre largo : mysuperlistfrom1to10
        - Linea 13: Uso de variable de instancia de nombre largo: completeHomeAddress
        - Linea 2, 11 y 12: Uso de variables de nombre corto (<= 15)
        
        Resultado esperado:
        [Warning('VariableLongName', 3, 'variable mysuperlistofone has a long name'),
        Warning('VariableLongName', 4, 'variable mysuperlistfrom1to10 has a long name'),
        Warning('VariableLongName', 13, 'variable completeHomeAddress has a long name')]
    """

    def test_long_variable_name(self):
        tree = self.get_ast_from_file('test-code/code-long-variable-name.py')

        longNameRule = LongVariableNameRule()
        result = longNameRule.analyze(tree)

        expectedWarnings = [
        Warning('VariableLongName', 3, 'variable mysuperlistofone has a long name'),
        Warning('VariableLongName', 4, 'variable mysuperlistfrom1to10 has a long name'),
        Warning('VariableLongName', 13, 'variable completeHomeAddress has a long name')]

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_unused_argument
        Codigo a ser analizado: test-code/code-unused-argument.py
        Descripcion: Test para evaluar UnusedArgumentRule considerando los siguientes escenarios:
        - Linea 1: En funcion example1, argumento z no es utilizado
        - Linea 4: En funcion example2, argmuento x no es utilizado
        - Linea 15: En funcion change_vitamins, argumento vs no es utilizado
        
        Resultado esperado:
        [Warning('UnusedArgument', 1, 'argument z is not used'),
        Warning('UnusedArgument', 4, 'argument x is not used'),
        Warning('UnusedArgument', 15, 'argument vs is not used')]
    """

    def test_unused_argument(self):
        tree = self.get_ast_from_file('test-code/code-unused-argument.py')

        unusedArgRule = UnusedArgumentRule()
        result = unusedArgRule.analyze(tree)

        expectedWarnings = [
        Warning('UnusedArgument', 1, 'argument z is not used'),
        Warning('UnusedArgument', 4, 'argument x is not used'),
        Warning('UnusedArgument', 15, 'argument vs is not used')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_super_init_not_called
        Codigo a ser analizado: test-code/code-super-init.py
        Descripcion: Test para evaluar SuperInitNotCalledRule considerando los siguientes escenarios:
        - Linea 14: Definicion de __init__ de Apple (subclase de Fruit) con llamada a super().__init__
        - Linea 16: Definicion de __init__ de Pineapple (subclase de Fruit) sin llamada a super().__init__
        
        Resultado esperado:
        [Warning('SuperInitNotCalled', 16, 'subclass Pineapple does not call to super().__init__()')]
    """

    def test_super_init_not_called(self):
        tree = self.get_ast_from_file('test-code/code-super-init.py')

        superInitRule = SuperInitNotCalledRule()
        result = superInitRule.analyze(tree)

        expectedWarnings = [
        Warning('SuperInitNotCalled', 16, 'subclass Pineapple does not call to super().__init__()')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_minus_equal_rewriter
        Codigo a ser analizado: test-code/code-minus-equal.py
        Descripcion: Test para evaluar transformador MinusEqualsRewriterCommand considerando los siguientes escenarios:
        - Linea 2: Asignación a = a - 5
        - Linea 6: Asignación x = x - y
        
        Resultado esperado: expected-code/code-minus-equal.py
    """

    def test_minus_equal_rewriter(self):
        tree = self.get_ast_from_file('test-code/code-minus-equal.py')

        command = MinusEqualsRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('expected-code/code-minus-equal.py')
        self.assertEqual(dump(tree), dump(expectedCode))


    """ Nombre: test_simplified_if
        Codigo a ser analizado: test-code/code-simplified-if.py
        Descripcion: Test para evaluar SimplifiedIfRewriterCommand considerando los siguientes escenarios:
        - Linea 2: Uso de la expresion if cuando puede ser reemplazada por el if.test
        - Linea 7: Uso de la expresion if cuando puede ser reemplazada por el not if.test
        
        Resultado esperado: expected-code/code-simplified-if.py
    """

    def test_simplified_if(self):
        tree = self.get_ast_from_file('test-code/code-simplified-if.py')

        command = SimplifiedIfRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('expected-code/code-simplified-if.py')
        
        self.assertEqual(dump(tree), dump(expectedCode))




if __name__ == '__main__':
    unittest.main()
