class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        minimum = total =  nums[0]
        for i in range(1,len(nums)):
            total+= nums[i]
            minimum = max(minimum , math.ceil(total/(i+1)))
        
        return minimum 