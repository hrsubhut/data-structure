class Solution(object):
    def maxArea(self, height):
        n=len(height)
        i = 0
        j =n-1
        area = 0
        for h in height:
            value= (j - i) * min(height[i], height[j])
            if area < value:
                area = value
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return area
        
        
        

        