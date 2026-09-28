class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        vals = []
        current = head
        
        while current:
            vals.append(current.val)
            current = current.next
            
        return vals == vals[::-1]