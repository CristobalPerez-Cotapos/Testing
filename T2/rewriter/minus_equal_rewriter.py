from .rewriter import *


class MinusEqualTransformer(NodeTransformer):
    def visit_Assign(self, node):
        NodeTransformer.generic_visit(self, node)
        if isinstance(node.value, BinOp) and isinstance(node.value.left, Name):
            if node.value.left.id == node.targets[0].id and isinstance(node.value.op, Sub):
                return AugAssign(node.targets[0], Sub(), node.value.right)
        return node

class MinusEqualsRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(MinusEqualTransformer().visit(ast))
        return new_tree