import unittest
from functionInstrumentor import *

"""
Tests para el instrumentor profile creado en clases
"""

class TestFunctionInstrumentor(unittest.TestCase):

    # Recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    # Recibe el path del codigo a analizar (filename) y el path donde el nuevo codigo se escribira (writeFile) y corre el profiler
    def instrument_file(self, filename, writeFile):
        tree = self.get_ast_from_file(filename)

        FunctionProfiler.reset()

        newTree = instrument(tree)

        # Estas lineas son para escribir el nuevo AST en un archivo
        #f = open(writeFile, "w")
        #f.write(unparse(newTree))
        #f.close()

        try:
            exec(compile(newTree, filename="<ast>", mode ="exec"), locals(), locals())
        except:
            print("An error ocurred! My injected code may cause problems")


    """ Nombre: test_executed_functions1
        Codigo a ser analizado: input_code/code1.py
        Descripcion: Test para evaluar la funcion report_executed_functions en el siguiente caso:
        - Linea 1 - 14:  Definicion de funciones (report_executed_functions solo considera funciones que fueron ejecutadas)
        - Linea 17 - 18: Llamada a algunas funciones
        

        Resultado esperado:
        [('test_sum', []),
        ('sum', [2, 3]),
        ('test_sum_tuple' , []),
        ('sum', [3, 7])]
    """

    def test_executed_functions1(self):

        self.instrument_file("input_code/code1.py", "code1.py")

        result = FunctionProfiler.getInstance().report_executed_functions()

        expected = [
        ('test_sum', []),
        ('sum', [2, 3]),
        ('test_sum_tuple' , []),
        ('sum', [3, 7])]


        self.assertEqual(result, expected)

    """ Nombre: test_executed_functions2
        Codigo a ser analizado: input_code/code2.py
        Descripcion: Test para evaluar la funcion report_executed_functions en el siguiente caso:
        - Linea 1 - 14:  Definicion de funciones (report_executed_functions solo considera funciones que fueron ejecutadas)
        - Linea 16 - 19: Llamada a algunas funciones
        

        Resultado esperado:
        [('factorial', [3]),
        ('factorial', [1]),
        ('abs', [2]),
        ('abs', [4])]
    """

    def test_executed_functions2(self):

        self.instrument_file("input_code/code2.py", "code2.py")

        result = FunctionProfiler.getInstance().report_executed_functions()

        expected = [
        ('factorial', [3]),
        ('factorial', [1]),
        ('abs', [2]),
        ('abs', [4])]


        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
