class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_values={}
        for index,num1 in enumerate(nums):
            complement = target-num1
            if complement in possible_values:
                return([index,possible_values[complement]])
            possible_values[num1]= index 
        
        
        