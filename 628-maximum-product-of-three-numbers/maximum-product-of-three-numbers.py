class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        ans= 1
        for i in range(-1,-4,-1):
            ans=ans*nums[i]

        ans

        sec_ans =nums[0]*nums[1]*nums[-1]

        return max(sec_ans,ans)
        


        