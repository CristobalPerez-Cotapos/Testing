import traceback
"""Clase que brinda funciones para facilitar la inspeccion de la pila"""
class StackInspector:

    # Retorna verdad si el frame esta in la clase actual de inspeccion
    def our_frame(self, frame):
        return isinstance(frame.f_locals.get('self'), self.__class__)

    # Retorna verdad si el frame esta involucrado con un <module>
    def problematic_frame(self, frame):
        return frame.f_code.co_name == "<module>"

    # Retorna verdad si alguna excepcion fue generada por el StackInspector o alguna de sus subclases
    def is_internal_error(self, exc_tp, exc_value, exc_traceback):
        if not exc_tp:
            return False

        for frame, lineno in traceback.walk_tb(exc_traceback):
            if self.our_frame(frame):
                return True

        return False

