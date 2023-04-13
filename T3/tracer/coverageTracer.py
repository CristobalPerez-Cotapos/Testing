import sys
import ast
import traceback
from types import *
from stackInspector import StackInspector

""" Clase para rastrear funciones que fueron ejecutadas. Para su uso, considere:
with CoverageTracer() as coverage:
    function_to_be_traced()

coverage.report_executed_lines()
"""

class CoverageTracer(StackInspector):

    def __init__(self):
        self.executed_lines = []
        pass

    def traceit(self, frame, event: str, arg):
        if event == "line":
            line = frame.f_lineno
            function_name = frame.f_code.co_name
            if not self.our_frame(frame) and not self.problematic_frame(frame):
                self.executed_lines.append((function_name, line))
        return self.traceit
            

    def report_executed_lines(self):
        result = set(self.executed_lines)
        return sorted(result, key=lambda a: a[1])
    
    def report_execution_count(self):
        results = []
        for line in self.report_executed_lines():
            results.append((line[0], line[1], self.executed_lines.count(line)))
        results = set(results)
        return sorted(results, key=lambda a: a[1])


    
        # Esta funcion se llama al comienzo de un bloque 'with' y comienza con el rastreo
    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)

        return self

    # Esta funcion se llama al final de un bloque 'with' y termina el rastreo.
    # Retorna 'None' si _todo funciona bien y si retorna 'False' significa que hubo un error interno (por nuestra clase Tracer o subclases).
    def __exit__(self, exc_tp, exc_value, exc_traceback: TracebackType):
        sys.settrace(self.original_trace_function)

        # Note que debemos retornar un valor 'False' para indicar que hubo un error interno y levantar las excepciones correspondientes.
        if self.is_internal_error(exc_tp, exc_value, exc_traceback):
            return False
        else:
            # Significa que _todo funciona bien
            return None

