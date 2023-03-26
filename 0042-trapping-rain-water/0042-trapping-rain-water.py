class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0 
        longest_to_left = [0]
        longest_to_right = [0]
        for i in range(len(height)) :
            longest_to_left.append(max(height[i] , longest_to_left[-1]))        
        for i in range(len(height)-1 , -1,-1) :
            longest_to_right.append(max(height[i] , longest_to_right[-1]))
        longest_to_right.reverse()   
        for block in range(len(height)) :
            shortest = min(longest_to_left[block] , longest_to_right[block])   
            if shortest > height[block]:
                trapped_water += shortest -height[block]
       
        return trapped_water