class Node:
    def _init_(self, var, low, high):
        self.var = var
        self.low = low
        self.high = high
        
ZEROTERMINAL = Node(0, None, None)
ONETERMINAL = Node(0, None, None)

def expr2bddnode(expr):
    if expr.is_zero():
        return ZEROTERMINAL
    elif expr.is_one():
        return ONETERMINAL
    else:
        
    
