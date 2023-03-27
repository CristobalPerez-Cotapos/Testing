from .rule import *


class SuperInitNotCalledVisitor(WarningNodeVisitor):
    
        def __init__(self):
            super().__init__()
            self.currentClass = None
            self.currentMethod = None
            self.is_super = False
            self.line = None
    
        def visit_ClassDef(self, node: ClassDef):
            # check if the class has a parent
            if len(node.bases) > 0:
                self.line = node.lineno
                self.currentClass = node.name
                NodeVisitor.generic_visit(self, node)
                if not self.is_super:
                    self.addWarning('SuperInitNotCalled', self.line, 'subclass ' + self.currentClass + ' does not call to super().__init__()')
                self.is_super = False
                self.currentClass = None
    
        def visit_FunctionDef(self, node: FunctionDef):
            # check if the method is __init__
            if self.currentClass != None:
                self.currentMethod = node.name
                NodeVisitor.generic_visit(self, node)
                self.currentMethod = None
    
        def visit_Call(self, node: Call):
            # check if super() is not called in __init__
            if self.currentClass != None and self.currentMethod != None:
                
                if self.currentMethod == '__init__':
                    
                    if isinstance(node.func, Name):
                        if node.func.id == 'super':
                            self.is_super = True

            NodeVisitor.generic_visit(self, node)
        
        def visit_Name(self, node: Name):
            if node.id == 'super':
                self.is_super = True
            NodeVisitor.generic_visit(self, node)

class SuperInitNotCalledRule(Rule):
        
            def analyze(self, ast):
                visitor = SuperInitNotCalledVisitor()
                visitor.visit(ast)
                return visitor.warningsList()