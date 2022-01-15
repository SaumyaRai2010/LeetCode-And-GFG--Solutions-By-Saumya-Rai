# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        left=head
        right=self.mid(head)
        temp=right.next
        right.next=None
        right=temp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    
    def mid(self,head):
        fast=head.next
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge(self,left,right):
        node=ListNode(0)
        ans=node
        while left and right:
            if left.val<right.val:
                node.next=left
                left=left.next
            else:
                node.next=right
                right=right.next
            node=node.next
        while left:
            node.next=left
            left=left.next
            node=node.next
        while right:
            node.next=right
            right=right.next
            node=node.next
        return ans.next
        