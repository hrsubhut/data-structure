class Solution(object):
    def maxProduct(self, nums):
        score_n = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                score =(nums[i]-1)*(nums[j]-1)
                if score > score_n:
                    score_n =score
                else:
                    continue
        return score_n
        