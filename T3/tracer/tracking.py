import sys
import inspect
from types import *
import traceback
from stackInspector import StackInspector

""" Clase para rastrear que partes de codigo se ejecutan.
Use de la siguiente forma: with Tracer(): block() """


class Tracer(StackInspector):

    # Inicializa las variables para rastrear un bloque de codigo y mandar logs a 'file'
    def __init__(self, *, file=sys.stdout):
        self.original_trace_function = None
        self.file = file

    """Funcion de rastreo que llama a imprimir los eventos y evita que rastreemos nuestros propios metodos
    Por el momento esta funcion envuelve a:
    - Un evento (event): Es una cadena que puede tener los siguientes valores:
        * 'line' 	- una nueva linea siendo ejecutada
        * 'call' 	- una funcion que acaba de ser llamada
        * 'return' 	- el retorno de una funcion
    - Un frame: El frame de ejecucion actual, es decir, un objeto de rastreo (e.g., una funcion). 
    Un frame tiene los siguientes atributos:
        * frame.f_lineno - la linea actual
        * frame.f_locals - las variables actuales (es un dictionary)
        * frame.f_code 	- el codigo actual (Code) que tiene el atributo frame.f_code.co_name (el nombre del la funcion actual)

    """

    def traceit(self, frame, event, arg):
        if self.our_frame(frame) or self.problematic_frame(frame):
            # No rastrearemos nuestros propios metodos
            pass
        else:
            self.log(event, frame.f_lineno, frame.f_code.co_name, frame.f_locals)
        return self.traceit

    # Es como un print(), pero siempre lo manda a archivo dado en la inicializacion (self.file), que por defecto es la consola.
    def log(self, *objects, sep: str = ' ', end: str = '\n', flush=True):
        print(*objects, sep=sep, end=end, file=self.file, flush=flush)

    # Esta funcion se llama al comienzo de un bloque 'with' y comienza con el rastreo
    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)

        # La linea de abajo que esta comentada tambien permite rastrear al bloque actual
        # inspect.currentframe().f_back.f_trace = self.traceit
        return self

    # Esta funcion se llama al final de un bloque 'with' y termina el rastreo.
    # Retorna 'None' si _todo funciona bien y si retorna 'False' significa que hubo un error interno (por nuestra clase Tracer o subclases).
    def __exit__(self, exc, exc_value, exc_traceback):
        sys.settrace(self.original_trace_function)

        # Note que debemos retornar un valor 'False' para indicar que hubo un error interno y levantar las excepciones correspondientes.
        if self.is_internal_error(exc, exc_value, exc_traceback):
            return False
        else:
            # Significa que _todo funciona bien
            return None


def remove_html_tags(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out


with Tracer():
    remove_html_tags("<b>abc</b>")
