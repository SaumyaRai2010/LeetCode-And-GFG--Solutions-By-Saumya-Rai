# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        itr1=l1
        itr2=l2
        num1=0
        num2=0
        i=1
        j=1
        while itr1:
            num1=num1+ itr1.val*i
            itr1=itr1.next
            i=i*10
        while itr2:
            num2=num2 + itr2.val*j
            itr2=itr2.next
            j=j*10
        total=num1+num2
        result = node = ListNode(total%10)
        total//=10
        while total:
            node.next = ListNode(total%10)
            node = node.next
            total//=10
        
        return result
        
        
        
        
        