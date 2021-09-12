class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
def sortedArrayTobst(arr):
    if not arr:
        return None
    
    mid=(len(arr))/2

    root=Node(arr[mid])

    root.left=sortedArrayTobst(arr[:mid])
    root.right=sortedArrayTobst(arr[mid+1:])
    return root
def preOrder(node):
    if not node:
        return 
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)