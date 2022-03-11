# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        node=head
        itr=head
        n=0
        while itr:
            itr=itr.next
            n+=1
        k=k%n
        n-=k
        cnt=0
        itr=head
        prev=None
        while itr and n>0:
            if cnt==n:
                break
            prev=itr
            itr=itr.next
            cnt+=1
        prev.next=None
        
        ans=itr
        if itr is None:
            return head
        while itr.next:
            itr=itr.next
        print(itr)
        itr.next=node
        return ans
        
        
        
        
        
        
        
        
        