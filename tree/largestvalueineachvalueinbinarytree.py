def largestValues(root):
    res=[]
    helper(res,root,0)
    return res

def helper(res,root,d):
    if not root:
        return 
    if (d==len(res)):
        res.append(root.val)
    else:
        res[d]=max(res[d],root.val)
    
    helper(res,root.left,d+1)
    helper(res,root.right,d+1)
    