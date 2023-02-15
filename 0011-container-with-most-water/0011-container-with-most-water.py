class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        k = len(height) -1
        max_area = 0
    
        while i<k:
            if height[i] < height[k]:
                area = (k-i)*height[i]
                i+=1
            
            elif height[i] > height[k]:
                area = (k-i)*height[k]
                k-=1
            
            else:
                area = (k-i)*height[i]
                i+=1
                k-=1
            
            if area>max_area:
                max_area = area
            
        return max_area