# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=0
        ex=head
        while ex:
            a=a+1
            ex=ex.next
        dele=a-n-1
        a=0
        ex=head
        if dele==-1:
            return head.next
        a=0
        while ex:
            if a==dele:
                ex.next=ex.next.next
                break
            ex=ex.next
            a=a+1
        return head
