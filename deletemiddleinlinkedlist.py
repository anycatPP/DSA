class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addToList(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=newNode
    def __str__(self):
        linkedListStr=""
        temp=self.head
        while temp:
            linkedListStr += str(temp.data)+"->"
            temp=temp.next
        return linkedListStr+"NULL"
    def deleteMid(self):
        if(self.head is None or self.head.next is None):
            return 
        slow_ptr=self.head
        fast_ptr=self.head
        preve=None
        while(fast_ptr is not None and fast_ptr.next is not None):
            fast_ptr=fast_ptr.next.next
            prev=slow_ptr
            slow_ptr=slow_ptr.next
        prev.next=slow_ptr.next