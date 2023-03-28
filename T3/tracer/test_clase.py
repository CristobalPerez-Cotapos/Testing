import unittest
from ast import *
from functionTracer import *

"""
Tests para el tracer de funciones creado en clases
"""


class TestFunctionTracer(unittest.TestCase):

    # Recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    # Recibe el path del archivo a rastrear y lo ejecuta
    def execute_file(self, filename):
        tree = self.get_ast_from_file(filename)

        with FunctionTracer() as self.funTracer:
            try:
                exec(compile(tree, filename="<ast>", mode="exec"), locals(), locals())
            except:
                print("An error ocurred! The code to analyze cannot be executed")

    """ Nombre: test_executed_functions1
        Codigo a ser analizado: input_code/code1.py
        Descripcion: Test para evaluar la funcion report_executed_functions en el siguiente caso:
        - Linea 1 - 14:  Definicion de funciones (report_executed_functions solo considera funciones que fueron ejecutadas)
        - Linea 17 - 18: Llamada a algunas funciones
        

        Resultado esperado:
        [('sum', 4),
        ('test_sum', 11),
        ('test_sum_tuple' , 13)]
    """

    def test_executed_functions1(self):

        self.execute_file("input_code/code1.py")

        result = self.funTracer.report_executed_functions()

        expected = [
            ('sum', 4),
            ('test_sum', 11),
            ('test_sum_tuple', 13)]

        self.assertEqual(result, expected)

    """ Nombre: test_executed_functions2
        Codigo a ser analizado: input_code/code2.py
        Descripcion: Test para evaluar la funcion report_executed_functions en el siguiente caso:
        - Linea 1 - 14:  Definicion de funciones (report_executed_functions solo considera funciones que fueron ejecutadas)
        - Linea 16 - 19: Llamada a algunas funciones
        

        Resultado esperado:
        [('factorial', 1),
        ('abs', 10)]
    """

    def test_executed_functions2(self):

        self.execute_file("input_code/code2.py")

        result = self.funTracer.report_executed_functions()

        expected = [
            ('factorial', 1),
            ('abs', 10)]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
