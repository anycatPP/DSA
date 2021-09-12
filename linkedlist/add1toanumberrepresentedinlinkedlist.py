import sys
import math
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def newNode(data):
        return Node(data)
    def IterativeReverseList(head):          #O(n)
        prev=curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt  
        return prev  
    def RecursiveReverseList(self,head):
        if not head:
            return None
        newHead=head
        if head.next:
            newHead=self.RecursiveReverseList(head.next)
            head.next.next=head
        head.next=None
        return newHead
    def addone(head):
        head=IterativeReverseList(head)
        k=head
        carry=0
        prev=None
        head.data+=1
        while head is not None and (head.data>9 or carry>0):
            prev=head
            head.data+=carry
            carry=head.data//10
            head.data=head.data%10
            head=head.next
            if carry>0:
                prev.next=Node(carry)
        return IterativeReverseList(k)

