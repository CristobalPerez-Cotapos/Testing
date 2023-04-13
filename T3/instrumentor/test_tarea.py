import unittest
from classInstrumentor import *

"""
Tests para el instrumentor profile de clases creado en la tarea 3
IMPORTANTE: No olvide que el archivo donde esta el instrumentor de la tarea
se debe llamar classInstrumentor.py para importar los archivos necesarios para las pruebas.
Caso contrario importe lo necesario en este archivo.
"""

class TestClassProfiler(unittest.TestCase):

    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    # Funcion que recibe un path del archivo a ser leido y el nombre del archivo a generar y devuelve un ast con codigo inyectado
    def get_instrumentation(self, filename, name):
        tree = self.get_ast_from_file(filename)

        ClassProfiler.reset()

        newTree = instrument(tree)

        f = open(name, "w")
        f.write(unparse(newTree))
        f.close()

        return newTree

    """ Nombre: test_methods_executed
        Codigo a ser analizado: input_code/code_task.py
        Descripcion: Test para evaluar la funcion report_methods_executed en el siguiente caso:
        - Linea 1:       Definicion clase Rectangle
        - Linea 3 - 19:  Definicion de metodos de Rectangle (report_methods_executed solo considera metodos que fueron ejecutados)
        - Linea 23 - 49: Definicion de funciones de testeo (report_methods_executed no toma en cuenta metodos que no pertenecen a un clase, 
                        se los considerara por defecto metodos de testeo)
        

        Resultado esperado:
        [('__init__', 3, 'Rectangle'),
        ('get_area', 7, 'Rectangle'),
        ('get_perimeter', 10, 'Rectangle'),
        ('__eq__', 19, 'Rectangle')]
    """

    def test_methods_executed(self):
        newTree = self.get_instrumentation('input_code/code_task.py', 'code_task.py')

        from code_task import Rectangle

        try:
            exec(compile(newTree, filename="<ast>", mode ="exec"), locals(), locals())
        except:
            print("An error ocurred! My injected code may cause problems")

        result = ClassProfiler.getInstance().report_executed_methods()

        expectedExecutedMethods = [
        ('__init__', 3, 'Rectangle'),
        ('get_area', 7, 'Rectangle'),
        ('get_perimeter', 10, 'Rectangle'),
        ('__eq__', 19, 'Rectangle')]


        self.assertEqual(result, expectedExecutedMethods)


        """ Nombre: test_executed_by
        Codigo a ser analizado: input_code/code_task.py
        Descripcion: Test para evaluar la funcion report_executed_by en el siguiente caso:
        - Linea 1:       Definicion clase Rectangle
        - Linea 3 - 19:  Definicion de metodos de Rectangle (report_executed_by solo considera metodos que fueron ejecutados por X funcion)
        - Linea 23 - 49: Definicion de funciones de testeo (report_executed_by retorna una lista de metodos de la clase W que fueron
                        ejecutados por la funcion de testeo X)
        

        * Resultado esperado para report_executed_by('test_area'):
        [('__init__', 3, 'Rectangle'), ('get_area', 7, 'Rectangle')]
        * Resultado esperado para report_executed_by('test_perimeter'):
        [('__init__', 3, 'Rectangle'), ('get_perimeter', 10, 'Rectangle')]
        * Resultado esperado para report_executed_by('test_compare1'):
        [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        * Resultado esperado para report_executed_by('test_compare2'):
        [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        * Resultado esperado para report_executed_by('test_compare3'):
        [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        * Resultado esperado para report_executed_by('test_compare_equal'):
        [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
    """

    def test_executed_by(self):

        newTree = self.get_instrumentation('input_code/code_task.py', 'code_task.py')

        from code_task import Rectangle

        try:
            exec(compile(newTree, filename="<ast>", mode ="exec"), locals(), locals())
        except:
            print("An error ocurred! My injected code may cause problems")


        result = ClassProfiler.getInstance().report_executed_by('test_area')

        expected = [('__init__', 3, 'Rectangle'), ('get_area', 7, 'Rectangle')]
        
        self.assertEqual(result, expected)

        result = ClassProfiler.getInstance().report_executed_by('test_perimeter')

        expected = [('__init__', 3, 'Rectangle'), ('get_perimeter', 10, 'Rectangle')]
        
        self.assertEqual(result, expected)

        result = ClassProfiler.getInstance().report_executed_by('test_compare1')

        expected = [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        
        self.assertEqual(result, expected)

        result = ClassProfiler.getInstance().report_executed_by('test_compare2')

        expected = [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        
        self.assertEqual(result, expected)

        result = ClassProfiler.getInstance().report_executed_by('test_compare2')

        expected = [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        
        self.assertEqual(result, expected)

        result = ClassProfiler.getInstance().report_executed_by('test_compare_equal')

        expected = [('__init__', 3, 'Rectangle'), ('__eq__', 19, 'Rectangle')]
        
        self.assertEqual(result, expected)


    """ Nombre: test_methods_executed1
        Codigo a ser analizado: input_code/code_task1.py
        Descripcion: Test para evaluar la funcion report_methods_executed en el siguiente caso:
        - Linea 3:       Definicion clase Point
        - Linea 3 - 19:  Definicion de metodos de Point (report_methods_executed solo considera metodos que fueron ejecutados)
        - Linea 21 - 43: Definicion de funciones de testeo (report_methods_executed no toma en cuenta metodos que no pertenecen a un clase, 
                        se los considerara por defecto metodos de testeo)
        

        Resultado esperado:
        [('__init__', 5, 'Point'),
        ('__eq__', 14, 'Point'),
        ('__str__', 17, 'Point')]
    """

    def test_methods_executed1(self):
        newTree = self.get_instrumentation('input_code/code_task1.py', 'code_task1.py')

        from code_task1 import Point

        try:
            exec(compile(newTree, filename="<ast>", mode ="exec"), locals(), locals())
        except:
            print("An error ocurred! My injected code may cause problems")

        result = ClassProfiler.getInstance().report_executed_methods()

        expectedExecutedMethods = [
        ('__init__', 5, 'Point'),
        ('__eq__', 14, 'Point'),
        ('__str__', 17, 'Point')]


        self.assertEqual(result, expectedExecutedMethods)


        """ Nombre: test_executed_by1
        Codigo a ser analizado: input_code/code_task1.py
        Descripcion: Test para evaluar la funcion report_executed_by en el siguiente caso:
        - Linea 3:       Definicion clase Point
        - Linea 3 - 19:  Definicion de metodos de Point (report_executed_by solo considera metodos que fueron ejecutados por X funcion)
        - Linea 21 - 43: Definicion de funciones de testeo (report_executed_by retorna una lista de metodos de la clase W que fueron
                        ejecutados por la funcion de testeo X)
        

        * Resultado esperado para report_executed_by('test_str'):
        [('__init__', 5, 'Point'), ('__str__', 17, 'Point')]
        * Resultado esperado para report_executed_by('test_compare1'):
        [('__init__', 5, 'Point'), ('__eq__', 14, 'Point')]
    """

    def test_executed_by1(self):

        newTree = self.get_instrumentation('input_code/code_task1.py', 'code_task1.py')

        from code_task1 import Point

        try:
            exec(compile(newTree, filename="<ast>", mode ="exec"), locals(), locals())
        except:
            print("An error ocurred! My injected code may cause problems")


        result = ClassProfiler.getInstance().report_executed_by('test_str')

        expected = [('__init__', 5, 'Point'), ('__str__', 17, 'Point')]
        
        self.assertEqual(result, expected)

        result = ClassProfiler.getInstance().report_executed_by('test_compare1')

        expected =  [('__init__', 5, 'Point'), ('__eq__', 14, 'Point')]
        
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
