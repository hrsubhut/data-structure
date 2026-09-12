class Solution(object):
    def sortArray(self, nums):
        def merge_n(arr):
            if len(arr) <= 1:
                return
            
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            merge_n(left)
            merge_n(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:    
                    arr[k] = left[i]
                    i += 1                 
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        merge_n(nums)
      
        return nums
