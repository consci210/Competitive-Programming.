class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0 
        longest_to_left = [0]
        longest_to_right = [0]
        length = len(height)
        for i in range(length) :
            longest_to_left.append(max(height[i] , longest_to_left[-1]))        
            longest_to_right.append(max(height[length-i-1] , longest_to_right[-1]))
         
        for block in range(length) :
            shortest = min(longest_to_left[block] , longest_to_right[length-block])   
            if shortest > height[block]:
                trapped_water += shortest -height[block]
       
        return trapped_water