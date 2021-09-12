def removeDuplicates(self):
    temp=self.head
    if temp is None:
        return 
    while temp.next is not None:
        if temp.data==temp.next.next:
            new =temp.next.next
            temp.next=None
            temp.next=new
        else:
            temp=temp.next
    return self.head