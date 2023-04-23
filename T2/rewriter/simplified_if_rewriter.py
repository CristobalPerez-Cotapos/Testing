from .rewriter import *


class SimplifiedIfTransformer(NodeTransformer):
    def visit_Return(self, node):
        NodeTransformer.generic_visit(self, node)
        if isinstance(node.value, IfExp):
            if isinstance(node.value.body, Constant) and isinstance(node.value.orelse, Constant):
                if node.value.body.value == True and node.value.orelse.value == False:
                    new_value = node.value.test
                    return Return(value=new_value)
                elif node.value.body.value == False and node.value.orelse.value == True:
                    new_value = UnaryOp(op=Not(), operand=node.value.test)
                    return Return(value=new_value)



class SimplifiedIfRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree