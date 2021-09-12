class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Height:
    def __init__(self):
        self.height=0
def height(root):
    if root==None:
        return 0
    return max(height(root.left),height(root.right))+1

def isBalanced(root):
    if root is None:
        return True
    lh=Height()
    rh=Height()
    lh.height=height(root.left)
    rh.height=height(root.right)
    l=isBalanced(root.left)
    r=isBalanced(root.right)
    if abs(lh.height-rh.height)<=1:
        return l and r 
    return False