class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            old = old = res[:]
            for subset in old:
                res.append(subset +[num])

        return res
        