#Delete continuous node with sum k form a given linked list 


# 1>>2>>-3>>3>>1 K=3


# approach 
# append node with value zero at the starting of the linked list 
# traverse the given linked list 
# during traversal store the sum of the node value till that 
# node with the refernce of the current node in an unordered map
# If there is node with value (sum-K ) present in the unordered map
# then delete all the node from node corresponding to value (sum -k)
# stored in map to the current node and update the sum as (sum -k) 
# if there is no node with value ( sum -k) present in the unordered map
# then stored then stored the current sum with node in the map


class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def getNode(data):
    temp=ListNode(data)
    temp.next=None
    return temp
def printList(head):
    while(head.next):
        print(head.val,end="->")
        head=head.next
    print(head.val,end="->")
def removeZeroSum(head,K):
    root=ListNode(0)
    root.next=head
    umap=dict()
    umap[0]=root
    sum=0
    while(head!=None):
        sum+=head.val
        if((sum-K)in umap):
            prev=umap[sum-K]
            start=prev
            aux=sum
            sum=sum-K
            while(prev!=head):
                prev=prev.next
                aux+=prev.val
                