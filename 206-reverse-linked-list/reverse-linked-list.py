class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            nxt = curr.next    # Store the next node
            curr.next = prev   # Reverse the pointer
            prev = curr        # Move prev forward
            curr = nxt         # Move curr forward
            
        return prev            # prev becomes the new head