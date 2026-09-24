class Solution(object):
    def searchInsert(self, nums, target):
        a =0
        b =len(nums)-1
        while a <=b:
            mid = (a+b) //2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                a= mid+1
            else:
                b =mid -1

        return a
             

