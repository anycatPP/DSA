def maxdepth(node):
    if node is None:
        return 0
    else:
        lDepth=maxDepth(node.left)
        rDepth=maxDepth(node.right)
        if lDepth>rDepth:
            return lDepth+1
        else:
            return rDepth+1