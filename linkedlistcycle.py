class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
head=None
def push(new_data):
    global head
    new_node=Node(new_data)
    new_node.next=head
    head=new_node
def detectLoop(h):
    global head
    if(head==None):
        return False
    else:
        while(head!=None):
            if(head.data==-1):
                return True
            else:
                head.data==-1
                head=head.next
    return False
push(1);
push(2);
push(3);
push(4);
push(5);
head.next.next.next.next.next = head.next.next
if (detectLoop(head)):
    print("1")
else:
    print("0")