def deleteMid(self):
    if(self.head is None or self.head.next is None):
        return 
    slow_ptr=self.head
    fast_ptr=self.head
    prev=None
    while(fast_ptr is not None and fast_ptr.next is not None):
        fast_ptr=fast_ptr.next.next
        prev=slow_ptr
        slow_ptr=slow_ptr.next
    prev.next=slow_ptr.next