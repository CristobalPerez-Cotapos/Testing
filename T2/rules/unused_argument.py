from .rule import *

class UnusedArgumentVisitor(WarningNodeVisitor):
    
    def __init__(self):
        super().__init__()
        self.used_variables = set()
      

    def visit_FunctionDef(self, node):
        # Reset the set of used variables for each function definition
        self.used_variables = set()
        self.generic_visit(node)
        for arg in node.args.args:
            if arg.arg not in self.used_variables:
                self.addWarning('UnusedArgument', node.lineno, 'argument ' + arg.arg + ' is not used')
    

    def visit_Name(self, node):
        if isinstance(node.ctx, Load):
            self.used_variables.add(node.id)
        self.generic_visit(node)

class UnusedArgumentRule(Rule):
    
        def analyze(self, ast):
            visitor = UnusedArgumentVisitor()
            visitor.visit(ast)
            return visitor.warningsList()
                
          
