class Solution(object):
    def reverseString(self, s):
        n= len(s)
        left =0
        right =n-1
        while left<right:
            s[right],s[left]=s[left],s[right]
            left +=1
            right -=1
            
