# A single nod eof singly linked list 
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=Node(data)
        if(self.head):
            current=self.head
            while(current.next):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    def printLL(self):
        node=self.head
        while node:
            print(str(node.data)+">>",end=" ")
            node=node.next
        print("NULL")
    def printMiddle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("the middle element is ",slow.data)

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
if __name__=='__main__':

    LL=LinkedList()
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(5)
    LL.insert(5)
    LL.insert(5)
    LL.printLL()
    LL.flatten(LL.head)