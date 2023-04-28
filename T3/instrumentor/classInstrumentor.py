from ast import *
import os
from profiler import Profiler


class ClassInstrumentor(NodeTransformer):
    # Implemente la clase ClassInstrumentor que hereda de la clase NodeTransformer. 
    # Implemente los m ́etodos de visita necesarios para inyectar el codigo usando los metodos de clase de ClassProfiler 
    # y recolectar la informacionn requerida para esta tarea.

    def __init__(self):
        self.functions_called = []
        self.currentFunction = None
        self.currentClass = None


    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse("from classInstrumentor import ClassProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)

        return transformedNode
    
    def visit_ClassDef(self, node: ClassDef):
        
        self.currentClass = node.name
        transformedNode = NodeTransformer.generic_visit(self, node)
        self.currentClass = None
        
        return transformedNode

    def visit_FunctionDef(self, node: FunctionDef):

        if self.currentClass is not None:
            print(self.currentClass)
            print("current function: ", self.currentFunction)
            transformedNode = NodeTransformer.generic_visit(self, node)
            # Inyectamos codigo para llamar al profiler en la primera linea de la definicion de una funcion
            argList = list(map(lambda x: x.arg, transformedNode.args.args))
            argList.insert(0, self.currentClass)
            # record the method name, the line number of the method def and the methood class
            self.functions_called.append((transformedNode.name, transformedNode.lineno, self.currentClass))
            # injectedCode = parse('ClassProfiler.record(\''+ transformedNode.name + '\', ' + str(transformedNode.lineno) +  ' , \'' + self.currentClass + ' , \'' + self.currentFunction + '\')')
            injectedCode = parse('ClassProfiler.record(\''+ transformedNode.name + '\', ' + str(transformedNode.lineno) + ' , \'' + self.currentClass + '\')')
        
            if isinstance(transformedNode.body, list):
                transformedNode.body.insert(0, injectedCode.body[0])
            else:
                transformedNode.body = [injectedCode.body[0], node.body]


            fix_missing_locations(transformedNode)

        
            return transformedNode
        else:
            # if it is not a methd, save the function name and the line number
            self.currentFunction = node.name
            
            injectedCode = parse('ClassProfiler.currentFunction = \'' + self.currentFunction + '\'')
            transformedNode = NodeTransformer.generic_visit(self, node)
            transformedNode.body.insert(0, injectedCode.body[0])
            fix_missing_locations(transformedNode) 
            
        
            return transformedNode
 


class ClassProfiler(Profiler):

    currentClass = None
    currentFunction = None

    @classmethod
    def record(cls, method_name, method_lineno, method_class):
    # def record(cls, method_name, method_lineno, method_class, currentFunction):
        cls.getInstance().ins_record(method_name, method_lineno, method_class)
        # cls.getInstance().ins_record(method_name, method_lineno, method_class, currentFunction)
        print("Method " + method_name + " in class " + method_class + " at line " + str(method_lineno) + " was called.")
    
    # Metodos de instancia
    def __init__(self):
        # use a set to avoid duplicates
        self.classes_called = set()
        self.list_of_classes = []
        self.classes_executed_by = dict()
        self.list_of_classes_executed_by = []
        
 

    def ins_record(self, method_name, method_lineno, method_class):
    # def ins_record(self, method_name, method_lineno, method_class, currentFunction):
        #append the function name, the class name and the arguments to the list, only if it is a method
        #check if the element has already been added
        self.classes_called.add((method_name, method_lineno, method_class))

        if self.classes_executed_by.get(self.currentFunction) is None:
            self.classes_executed_by[self.currentFunction] = set()
            self.classes_executed_by[self.currentFunction].add((method_name, method_lineno, method_class))
        else:
            self.classes_executed_by[self.currentFunction].add((method_name, method_lineno, method_class))

        # self.classes_executed_by[currentFunction] = (method_name, method_lineno, method_class)
        
        # set the current class to none if it is a method
        

    def report_executed_classes(self):
        print("-- Executed classes --")
        for (fun, args) in self.classes_called:
            if len(args) != 0:
                print("Class " + fun + " with arguments " + " ".join(str(arg) for arg in args))
            else:
                print("Class " + fun + " with no arguments.")
        return self.classes_called

    def report_executed_methods(self):
        # dont report functions, just methods of a class
        print("-- Executed methods --")
        for (method, lineno, class1) in self.classes_called:
            self.list_of_classes.append((method, lineno, class1))

        # sort the list by lineno
        self.list_of_classes.sort(key=lambda x: x[1])
        return self.list_of_classes
    
    def report_executed_by(self, function_name):
        for (method, lineno, class1) in self.classes_executed_by[function_name]:
            self.list_of_classes_executed_by.append((method, lineno, class1))
        
        self.list_of_classes_executed_by.sort(key=lambda x: x[1])
        lista = self.list_of_classes_executed_by
        self.list_of_classes_executed_by = []

        return lista



def instrument(ast):
    visitor = ClassInstrumentor()
    return visitor.visit(ast)


    