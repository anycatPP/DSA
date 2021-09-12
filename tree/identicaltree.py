def identicalTree(a,b):
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return ((a.data==b.data) and identicalTree(a.left,b.left) 
        and identicalTree(a.right,b.right))
        return False