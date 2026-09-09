class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        longest_str=1
        current_str =1
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] ==nums[i-1]+1:
                    current_str +=1
                else:
                    longest_str=max(longest_str,current_str)
                    current_str=1

        return max(longest_str,current_str)
        