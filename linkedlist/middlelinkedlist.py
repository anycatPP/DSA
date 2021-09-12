class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printMiddle(self):
        slow =self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("the middle element is ",slow.data)
