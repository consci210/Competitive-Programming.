class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1 
        
        while left < right   :
            
            value = numbers[left] + numbers[right]
            if value == target :
                left += 1 
                right += 1 
                return [left , right]
                
            elif value > target :
                right -=1 
            
            else :
                left+=1  
            
       