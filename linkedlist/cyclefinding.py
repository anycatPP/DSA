def detectCycle(head):
    if head==None or head.next==None:
        return None
    walker=head
    runner=head
    isCycle=False
    while walker is not None and runner is not None:
        walker=walker.next
        if runner.next==None:
            return None
        runner=runner.next.next 
        if(walker==runner):
            isCycle=True
            break
        if not isCycle:
            return None
        else:
            walker=head
            while(walker is not runner):
                walker=walker.next
                runner=runner.next
    return walker
    