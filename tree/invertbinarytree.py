def binarytree(root):
    if root==None:
        return root
    left=binarytree(root.left)
    right=binarytree(root.right)
    #swaps
    root.right=left
    root.left=right
    return root
