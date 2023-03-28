import unittest
from ast import *
from coverageTracer import *
from code_task import *

"""
Tests para el tracer de coverage creado en la tarea 3
IMPORTANTE: No olvide que el archivo donde esta el tracer de coverage de la tarea
se debe llamar coverageTracer.py para importar los archivos necesarios para las pruebas.
Caso contrario importe lo necesario en este archivo.
"""


class TestCoverageTracer(unittest.TestCase):
    """ Nombre: test_executed_lines1
        Codigo a ser analizado: remove_html_tags del archivo code_task.py 
        Descripcion: Test para evaluar la funcion report_executed_lines en el siguiente caso:
        - remove_html_tags('<b>abc</b>')

        Resultado esperado:
        [('remove_html_tags' , 2),
        ('remove_html_tags' , 3),
        ('remove_html_tags' , 4),
        ('remove_html_tags' , 6),
        ('remove_html_tags' , 7),
        ('remove_html_tags' , 8),
        ('remove_html_tags' , 9),
        ('remove_html_tags' , 10),
        ('remove_html_tags' , 11),
        ('remove_html_tags' , 13),
        ('remove_html_tags' , 14),
        ('remove_html_tags' , 16)]
    """

    def test_executed_lines1(self):
        with CoverageTracer() as self.coverage:
            remove_html_tags('<b>abc</b>')

        result = self.coverage.report_executed_lines()

        expected = [
            ('remove_html_tags', 2),
            ('remove_html_tags', 3),
            ('remove_html_tags', 4),
            ('remove_html_tags', 6),
            ('remove_html_tags', 7),
            ('remove_html_tags', 8),
            ('remove_html_tags', 9),
            ('remove_html_tags', 10),
            ('remove_html_tags', 11),
            ('remove_html_tags', 13),
            ('remove_html_tags', 14),
            ('remove_html_tags', 16)]

        self.assertEqual(result, expected)

    """ Nombre: test_execution_count1
        Codigo a ser analizado: remove_html_tags del archivo code_task.py 
        Descripcion: Test para evaluar la funcion report_execution_count en el siguiente caso:
        - remove_html_tags('<b>abc</b>')
        

        Resultado esperado:
        [('remove_html_tags', 2, 1), 
        ('remove_html_tags', 3, 1), 
        ('remove_html_tags', 4, 1), 
        ('remove_html_tags', 6, 11), 
        ('remove_html_tags', 7, 10), 
        ('remove_html_tags', 8, 2), 
        ('remove_html_tags', 9, 8),
        ('remove_html_tags', 10, 2), 
        ('remove_html_tags', 11, 6), 
        ('remove_html_tags', 13, 6), 
        ('remove_html_tags', 14, 3), 
        ('remove_html_tags', 16, 1)]
    """

    def test_execution_count1(self):
        with CoverageTracer() as self.coverage:
            remove_html_tags('<b>abc</b>')

        result = self.coverage.report_execution_count()

        expected = [
            ('remove_html_tags', 2, 1),
            ('remove_html_tags', 3, 1),
            ('remove_html_tags', 4, 1),
            ('remove_html_tags', 6, 11),
            ('remove_html_tags', 7, 10),
            ('remove_html_tags', 8, 2),
            ('remove_html_tags', 9, 8),
            ('remove_html_tags', 10, 2),
            ('remove_html_tags', 11, 6),
            ('remove_html_tags', 13, 6),
            ('remove_html_tags', 14, 3),
            ('remove_html_tags', 16, 1)]

        self.assertEqual(result, expected)

    """ Nombre: test_executed_lines2
        Codigo a ser analizado: remove_html_tags del archivo code_task.py 
        Descripcion: Test para evaluar la funcion report_executed_lines en el siguiente caso:
        - remove_html_tags('abc')

        Resultado esperado:
        [('remove_html_tags' , 2),
        ('remove_html_tags' , 3),
        ('remove_html_tags' , 4),
        ('remove_html_tags' , 6),
        ('remove_html_tags' , 7),
        ('remove_html_tags' , 9),
        ('remove_html_tags' , 11),
        ('remove_html_tags' , 13),
        ('remove_html_tags' , 14),
        ('remove_html_tags' , 16)]
    """

    def test_executed_lines2(self):
        with CoverageTracer() as self.coverage:
            remove_html_tags('abc')

        result = self.coverage.report_executed_lines()

        expected = [
            ('remove_html_tags', 2),
            ('remove_html_tags', 3),
            ('remove_html_tags', 4),
            ('remove_html_tags', 6),
            ('remove_html_tags', 7),
            ('remove_html_tags', 9),
            ('remove_html_tags', 11),
            ('remove_html_tags', 13),
            ('remove_html_tags', 14),
            ('remove_html_tags', 16)]

        self.assertEqual(result, expected)

    """ Nombre: test_execution_count2
        Codigo a ser analizado: remove_html_tags del archivo code_task.py 
        Descripcion: Test para evaluar la funcion report_execution_count en el siguiente caso:
        - remove_html_tags('abc')
        

        Resultado esperado:
        [('remove_html_tags', 2, 1),
        ('remove_html_tags', 3, 1),
        ('remove_html_tags', 4, 1),
        ('remove_html_tags', 6, 4),
        ('remove_html_tags', 7, 3),
        ('remove_html_tags', 9, 3),
        ('remove_html_tags', 11, 3), 
        ('remove_html_tags', 13, 3), 
        ('remove_html_tags', 14, 3), 
        ('remove_html_tags', 16, 1)]
    """

    def test_execution_count2(self):
        with CoverageTracer() as self.coverage:
            remove_html_tags('abc')

        result = self.coverage.report_execution_count()

        expected = [
            ('remove_html_tags', 2, 1),
            ('remove_html_tags', 3, 1),
            ('remove_html_tags', 4, 1),
            ('remove_html_tags', 6, 4),
            ('remove_html_tags', 7, 3),
            ('remove_html_tags', 9, 3),
            ('remove_html_tags', 11, 3),
            ('remove_html_tags', 13, 3),
            ('remove_html_tags', 14, 3),
            ('remove_html_tags', 16, 1)]

        self.assertEqual(result, expected)

    """ Nombre: test_executed_lines3
        Codigo a ser analizado: remove_html_tags del archivo code_task.py 
        Descripcion: Test para evaluar la funcion report_executed_lines en el siguiente caso:
        - remove_html_tags("<b link='blue'>'finish'</b>")

        Resultado esperado:
        [('remove_html_tags' , 2),
        ('remove_html_tags' , 3),
        ('remove_html_tags' , 4),
        ('remove_html_tags' , 6),
        ('remove_html_tags' , 7),
        ('remove_html_tags' , 8),
        ('remove_html_tags' , 9),
        ('remove_html_tags' , 10),
        ('remove_html_tags' , 11),
        ('remove_html_tags' , 12),
        ('remove_html_tags' , 13),
        ('remove_html_tags' , 14),
        ('remove_html_tags' , 16)]
    """

    def test_executed_lines3(self):
        with CoverageTracer() as self.coverage:
            remove_html_tags("<b link='blue'>'finish'</b>")

        result = self.coverage.report_executed_lines()

        expected = [
            ('remove_html_tags', 2),
            ('remove_html_tags', 3),
            ('remove_html_tags', 4),
            ('remove_html_tags', 6),
            ('remove_html_tags', 7),
            ('remove_html_tags', 8),
            ('remove_html_tags', 9),
            ('remove_html_tags', 10),
            ('remove_html_tags', 11),
            ('remove_html_tags', 12),
            ('remove_html_tags', 13),
            ('remove_html_tags', 14),
            ('remove_html_tags', 16)]

        self.assertEqual(result, expected)

    """ Nombre: test_execution_count3
        Codigo a ser analizado: remove_html_tags del archivo code_task.py 
        Descripcion: Test para evaluar la funcion report_execution_count en el siguiente caso:
        - remove_html_tags("<b link='blue'>'finish'</b>")
        

        Resultado esperado:
        [('remove_html_tags', 2, 1),
        ('remove_html_tags', 3, 1),
        ('remove_html_tags', 4, 1),
        ('remove_html_tags', 6, 28),
        ('remove_html_tags', 7, 27),
        ('remove_html_tags', 8, 2),
        ('remove_html_tags', 9, 25),
        ('remove_html_tags', 10, 2),
        ('remove_html_tags', 11, 23),
        ('remove_html_tags', 12, 2), 
        ('remove_html_tags', 13, 21), 
        ('remove_html_tags', 14, 8), 
        ('remove_html_tags', 16, 1)]
    """

    def test_execution_count3(self):
        with CoverageTracer() as self.coverage:
            remove_html_tags("<b link='blue'>'finish'</b>")

        result = self.coverage.report_execution_count()

        expected = [
            ('remove_html_tags', 2, 1),
            ('remove_html_tags', 3, 1),
            ('remove_html_tags', 4, 1),
            ('remove_html_tags', 6, 28),
            ('remove_html_tags', 7, 27),
            ('remove_html_tags', 8, 2),
            ('remove_html_tags', 9, 25),
            ('remove_html_tags', 10, 2),
            ('remove_html_tags', 11, 23),
            ('remove_html_tags', 12, 2),
            ('remove_html_tags', 13, 21),
            ('remove_html_tags', 14, 8),
            ('remove_html_tags', 16, 1)]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
