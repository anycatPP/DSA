def partition(head):
    before_head=ListNode(0)
    before_runner=before_head
    after_head=ListNode(0)
    after_runner=after_head

    while head is not None:
        if head.val<x:
            before_runner.next=head
            before_runner=before_runner.next
        else:
            after_runner.next=head
            after_runner=after_runner.next
        head=head.next
    after_runner.next=None
    before_runner.next=after_head.next
    return before_head.next