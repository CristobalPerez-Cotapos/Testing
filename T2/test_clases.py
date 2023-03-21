import unittest
from rules import *
from rewriter import *

# Tests para las reglas y transformaciones creadas en clase

class TestWarnings(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    """ Nombre: test_eval_used
        Codigo a ser analizado: input-code/code-eval-used.py
        Descripcion: Test para evaluar rule eval_used considerando los siguientes escenarios:
        - Linea 1: Una llamada normal - eval("2")
        - Linea 4: Una llamada dentro de una funcion - eval("2 + 2")
        - Linea 15: Una llamada dentro de un metodo de una clase - eval("[1, 2, 3]")
        
        Resultado esperado:
        [Warning('EvalWarning', 1, 'eval should not be used!!'),
        Warning('EvalWarning', 4, 'eval should not be used!!'),
        Warning('EvalWarning', 15, 'eval should not be used!!')]
    """

    def test_eval_used(self):
        tree = self.get_ast_from_file('input-code/code-eval-used.py')

        evalRule = EvalUsedRule()
        result = evalRule.analyze(tree)

        expectedWarnings = [
        Warning('EvalWarning', 1, 'eval should not be used!!'),
        Warning('EvalWarning', 4, 'eval should not be used!!'),
        Warning('EvalWarning', 15, 'eval should not be used!!')]

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_dummy_if
        Codigo a ser analizado: input-code/code-dummy-if.py
        Descripcion: Test para evaluar rule dummy_if considerando los siguientes escenarios:
        - Linea 2: Uso de if True dentro de una funcion con un solo statement el if
        - Linea 7: Uso de if anidados, if True dentro del body de If
        - Linea 18: Uso de if anidados, if True dentro del body de else
        
        Resultado esperado:
        [Warning('DummyIfWarning', 2, 'this if does not have any sense!'),
        Warning('DummyIfWarning', 7, 'this if does not have any sense!'),
        Warning('DummyIfWarning', 18, 'this if does not have any sense!')]
    """

    def test_dummy_if(self):
        tree = self.get_ast_from_file('input-code/code-dummy-if.py')

        dummyIfRule = DummyIfRule()
        result = dummyIfRule.analyze(tree)

        expectedWarnings = [
        Warning('DummyIfWarning', 2, 'this if does not have any sense!'),
        Warning('DummyIfWarning', 7, 'this if does not have any sense!'),
        Warning('DummyIfWarning', 18, 'this if does not have any sense!')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_many_arguments
        Codigo a ser analizado: input-code/code-many-arguments.py
        Descripcion: Test para evaluar rule many_arguments considerando los siguientes escenarios:
        - Linea 1: Definicion de funcion example1 con 9 argumentos
        - Linea 8: Definicion de funcion example2 con 2 argumentos
        - Linea 13: Definicion de metodo __init__ con 7 argumentos a parte del self
        - Linea 24: Definicion de metodo fullName con solo self como argumento
        
        Resultado esperado:
        [Warning('ManyArguments', 1, 'function example1 defined with many arguments!'),
        Warning('ManyArguments', 13, 'function __init__ defined with many arguments!')]
    """

    def test_many_arguments(self):
        tree = self.get_ast_from_file('input-code/code-many-arguments.py')

        manyArgsRule = ManyArgumentsRule()
        result = manyArgsRule.analyze(tree)

        expectedWarnings = [
        Warning('ManyArguments', 1, 'function example1 defined with many arguments!'),
        Warning('ManyArguments', 13, 'function __init__ defined with many arguments!')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_uncoupled_method
        Codigo a ser analizado: input-code/code-uncoupled-method.py
        Descripcion: Test para evaluar rule uncoupled method considerando los siguientes escenarios:
        - Linea 1: Definicion de funcion que no tiene atributos - no la deberia considerar porque no esta definida dentro de una clase
        - Linea 8: Definicion de funcion __init__ - usa atributos
        - Linea 12: Definicion de funcion fullName - usa atributos
        - Linea 15: Definicion de metodo doit que no usa atributos
        - Linea 18: Definicion de metodo something que no usa atributos
        
        Resultado esperado:
        [Warning('UncoupledMethodWarning', 15, 'method doit does not use any attribute'),
        Warning('UncoupledMethodWarning', 18, 'method something does not use any attribute')]
    """

    def test_uncoupled_method(self):
        tree = self.get_ast_from_file('input-code/code-uncoupled-method.py')

        uncoupledMethodRule = UncoupledMethodRule()
        result = uncoupledMethodRule.analyze(tree)

        expectedWarnings = [
        Warning('UncoupledMethodWarning', 15, 'method doit does not use any attribute'),
        Warning('UncoupledMethodWarning', 18, 'method somethig does not use any attribute')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_uninitialized_attribute
        Codigo a ser analizado: input-code/code-uninitialized-attribute.py
        Descripcion: Test para evaluar rule uninitialized attribute considerando los siguientes escenarios:
        - Linea 5: Uso de atributos no inicializados
        - Linea 8: Definicion de clase que inicializa atributos
        
        Resultado esperado:
        [Warning('UninitilizeAttrWarning', 5, 'attribute firstName was not initialized'),
        Warning('UninitilizeAttrWarning', 5, 'attribute lastName was not initialized')]
    """

    def test_uninitialized_attribute(self):
        tree = self.get_ast_from_file('input-code/code-uninitialized-attribute.py')

        uninitializedAttr = UninitializedAttributeRule()
        result = uninitializedAttr.analyze(tree)


        expectedWarnings = [
        Warning('UninitilizeAttrWarning', 5, 'attribute firstName was not initialized'),
        Warning('UninitilizeAttrWarning', 5, 'attribute lastName was not initialized')]

        self.assertEqual(result, expectedWarnings)
        

class TestTransformers(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree


    """ Nombre: test_eval_rewriter
        Codigo a ser analizado: input-code/code-eval-used.py
        Descripcion: Test para evaluar transformador eval rewriter considerando los siguientes escenarios:
        - Linea 1: Una llamada normal - eval("2")
        - Linea 4: Una llamada dentro de una funcion - eval("2 + 2")
        - Linea 15: Una llamada dentro de un metodo de una clase - eval("[1, 2, 3]")
        
        Resultado esperado: expected-code/code-eval-used.py
    """

    def test_eval_rewriter(self):
        tree = self.get_ast_from_file('input-code/code-eval-used.py')

        command = LiteralEvalRewriterCommand()
        tree = command.apply(tree)

        # Se exporta el AST transformado a un archivo en el folder transformed-code

        expectedCode = self.get_ast_from_file('expected-code/code-eval-used.py')

        self.assertEqual(dump(tree), dump(expectedCode))


    """ Nombre: test_if_true_rewriter
        Codigo a ser analizado: input-code/code-dummy-if.py
        Descripcion: Test para evaluar transformador if true considerando los siguientes escenarios:
        - Linea 2: Uso de if True dentro de una funcion con un solo statement el if
        - Linea 7: Uso de if anidados, if True dentro del body de If
        - Linea 18: Uso de if anidados, if True dentro del body de else
        
        Resultado esperado: expected-code/code-dummy-if.py
    """

    def test_if_true_rewriter(self):
        tree = self.get_ast_from_file('input-code/code-dummy-if.py')

        command = IfTrueRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('expected-code/code-dummy-if.py')

        self.assertEqual(dump(tree), dump(expectedCode))




if __name__ == '__main__':
    unittest.main()
