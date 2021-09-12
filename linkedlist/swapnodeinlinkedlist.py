def swapPairs(head):
    dummy=ListNode(0)
    dummy.next=head
    runner=dummy
    while(runner.next is not None and runner.next.next is not None):
        r1=runner.next
        r2=runner.next.next
        runner.next=r2
        r1.next=r2.next
        r2.next=r1

        runner=runner.next.next
    
    return dummy.next