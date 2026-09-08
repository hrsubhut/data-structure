class Solution(object):
    def twoSum(self, nums, target):
        n =len(nums)
        for i in range(n): 
            q = target-nums[i]
            for j in range(i+1,n):
                if q == nums[j]:
                    return[i,j]
                    
