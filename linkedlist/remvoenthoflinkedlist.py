def removeNthFromEnd(head,n):
    dummy=ListNode(0)  #listnode to implement
    dummy.next=head
    walker=dummy
    runner=dummy
    for i in range(n+1):
        runner=runner.next
    while(runner is not None):
        runner=runner.next
        walker=walker.next
    walker.next=walker.next.next
    return dummy.next

