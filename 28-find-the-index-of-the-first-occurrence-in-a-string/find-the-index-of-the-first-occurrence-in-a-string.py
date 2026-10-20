class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle ) if needle in haystack else -1
        