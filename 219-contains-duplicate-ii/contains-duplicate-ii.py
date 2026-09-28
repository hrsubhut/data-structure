class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n=len(nums)
        dict ={}

        for i in range(n):
            num= nums[i]
            if num in dict:
                if i-dict[num] <=k:
                    return True

            dict[num]=i
        return False
        