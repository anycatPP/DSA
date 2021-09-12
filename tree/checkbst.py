def isBST(root,l,r):
    if(root==None):
        return True
    
    if(l is not None and root.data<=l.data):
        return False
    if(r is not None and root.data<=r.data):
        return False

    return isBST(root.left,l,root) and isBST(root.right,root,r)