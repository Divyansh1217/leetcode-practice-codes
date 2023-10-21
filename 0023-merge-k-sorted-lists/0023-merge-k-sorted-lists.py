# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=b=ListNode()
        arr=[]
        for i in lists:
            while i!=None:
                arr.append(i.val)
                i=i.next
        for i in sorted(arr):
            b.next=ListNode()
            b=b.next
            b.val=i
        return a.next