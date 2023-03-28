from .rule import *

## check if variables are longer than 15 and raise a warning

class LongVariableNameVisitor(WarningNodeVisitor):

  

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, Name):
                if len(target.id) > 15:
                    self.addWarning('VariableLongName', node.lineno, 'variable ' + target.id + ' has a long name')

            # check in a class
            if isinstance(target, Attribute):
                if len(target.attr) > 15:
                    self.addWarning('VariableLongName', node.lineno, 'variable ' + target.attr + ' has a long name')
        NodeVisitor.generic_visit(self, node)
            

class LongVariableNameRule(Rule):

    def analyze(self, ast):
        visitor = LongVariableNameVisitor()
        visitor.visit(ast)
        return visitor.warningsList()


