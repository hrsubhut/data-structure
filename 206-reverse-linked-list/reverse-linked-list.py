# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        arr = []
        current  = head
        while current is not None:
            arr.append(current.val)
            current = current.next
        
        arr = arr[::-1]
        current1 =head
        for a in arr:
            current1.val = a
            current1 = current1.next

        return head