class Solution(object):
    #here what i do is normally make a two string and made check for it
    def isPalindrome(self, s):
        s = ''.join(char.lower()for char in s if char.isalnum())
        return s == s[::-1]


        