# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        x,y=head,dummy
        for i in range(n):
            x=x.next
        while x:
            x=x.next
            y=y.next
        y.next=y.next.next
        return dummy.next
