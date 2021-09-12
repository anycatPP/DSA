class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
    def zigzagtraversal(root):
        if root is None:
            return
        currentLevel=[]
        nextLevel=[]
        ltr=True
        currentLevel.append(root)
        while len(currentLevel)>0:
            temp=currentLevel.pop(-1)
            print(temp.data," ",end="")
            if ltr:
                if temp.left:
                    nextLevel.append(temp.left)
                if temp.right:
                    nextLevel.append(temp.right)
            else:
                if temp.right:
                    nextLevel.append(temp.right)
                if temp.left:
                    nextLevel.append(temp.left)
            if len(currentLevel)==0:
                ltr=not ltr
                currentLevel=nextLevel
                nextLevel=currentLevel
                