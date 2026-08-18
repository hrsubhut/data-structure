class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for c in s:
            if not  stack or stack[-1]!= c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)
        
    
        