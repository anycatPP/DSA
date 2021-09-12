

def flatten(self,root):
    if(root==None or root.right==None):
        return root
    root.right=self.flatten(root.right)
    root=self.merge(root,root.right)
    return root
def merge(self,a,b):
    if(a==None):
        return b
    if(b==None):
        return a
    result=None
    if(a.data<b.data):
        result=a
        result.down=self.merge(a.down,b)
    else:
        result=b
        result.down=self.merge(a,b.down)
    return result
