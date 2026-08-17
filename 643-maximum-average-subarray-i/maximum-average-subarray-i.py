class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_sum  = current_sum

        for right in range(k,len(nums)):
            current_sum += nums[right]
            current_sum -=nums[right - k]
            max_sum =max(max_sum ,current_sum)
        
        return (max_sum/ float(k))

        