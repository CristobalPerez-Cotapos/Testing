from ast import *
from pprint import pprint


class RewriterCommand:
    def apply(self, ast):
        # Por defecto retorna el mismo AST sin ninguna modificacion
        return ast
