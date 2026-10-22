# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # 1. Remove any matching values from the beginning of the list
        while head is not None and head.val == val:
            head = head.next

        # 2. Initialize pointers after cleaning the head
        curr = head
        prev = None

        # 3. Traverse through the rest of the list
        while curr is not None:
            if curr.val == val:
                # Skip the current node
                prev.next = curr.next
            else:
                # Move prev forward only if we don't delete
                prev = curr
            
            curr = curr.next

        return head