from ast import *
from profiler import Profiler
from functools import reduce

# Clase que permite inyectar codigo de tal forma que podamos reportar que funciones se ejecutan
class FunctionInstrumentor(NodeTransformer):

    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse("from functionInstrumentor import FunctionProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)

        return transformedNode


    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        
        # Inyectamos codigo para llamar al profiler en la primera linea de la definicion de una funcion
        argList = list(map(lambda x: x.arg, transformedNode.args.args))
        injectedCode = parse('FunctionProfiler.record(\''+
        transformedNode.name + '\',[' + ", ".join(argList) + '])')
    
        if isinstance(transformedNode.body, list):
            transformedNode.body.insert(0, injectedCode.body[0])
        else:
            transformedNode.body = [injectedCode.body[0], node.body]

        fix_missing_locations(transformedNode)
        
        return transformedNode


# Clase que rastrea y reporta las funciones que se ejecutan
class FunctionProfiler(Profiler):

    @classmethod
    def record(cls, functionName, args):
        cls.getInstance().ins_record(functionName,args)
    
    # Metodos de instancia
    def __init__(self):
        self.functions_called = []

    def ins_record(self, functionName, args):  
        self.functions_called.append((functionName, args))
        
    def report_executed_functions(self):
        print("-- Executed functions --")
        for (fun, args) in self.functions_called:
            if len(args) != 0:
                print("Function " + fun + " with arguments " + " ".join(str(arg) for arg in args))
            else:
                print("Function " + fun + " with no arguments.")
        return self.functions_called

    
def instrument(ast):
    visitor = FunctionInstrumentor()
    return  fix_missing_locations(visitor.visit(ast))