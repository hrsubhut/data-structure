class Solution(object):
    def concatWithReverse(self, nums):
        n=len(nums)
        s = nums[:]
        l=0
        r=n-1

        while l<r:
            nums[l],nums[r]=nums[r],nums[l]

            l +=1
            r -=1

        return s+nums

        
        