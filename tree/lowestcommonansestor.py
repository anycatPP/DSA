#lowest common ancestor in tree


def lowestCommonAncestor(root,node1,node2):
    if root==None:
        return None
    if root==node1 or root==node2:
        return root
    left=lowestCommonAncestor(root.left,node1,node2)
    right=lowestCommonAncestor(root.right,node1,node2)
    if left is not None and right is not None:
        return root
    if left is None and right is None:
        return None
    return left if left is not None else right