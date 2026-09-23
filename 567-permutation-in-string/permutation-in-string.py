class Solution(object):
    def checkInclusion(self, s1, s2):
        sort = sorted(s1)

        for i in range(len(s2)-len(s1)+1):
            sub =s2[i:i+len(s1)]

            if sorted(sub) == sort:
                return True
        return False

       